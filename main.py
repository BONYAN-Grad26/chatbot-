import pickle
import uuid
from typing import Any, Dict, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from graduation import (
    CLASS_DESCRIPTIONS,
    build_clarification_question,
    detect_language,
    find_entity,
    get_response,
    is_short,
    predict,
)

app = FastAPI(title="Bonyaan Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

sessions: dict[str, dict] = {}


def _new_state() -> dict:
    return {
        "last_label": None,
        "second_label": None,
        "last_user_input": "",
        "waiting_for": None,
        "pending_entity": None,
        "pending_label": None,
        "original_text": "",
        "profile": None,  # ==== تعديل جديد: هنا هنخزن آخر profile وصلنا من الفرونت إند ====
        "lang": "ar",  # ==== تعديل جديد: بنخزن آخر لغة اتحددت عشان ردود زي "1"/"2" متكسرش الاستمرارية ====
    }


# ==== تعديل: الدالة بقت بتاخد profile كمان (اختياري) ====
def process_message(user_input: str, state: dict, profile: Optional[Dict[str, Any]] = None) -> str:
    user_lower = user_input.lower()

    # ==== تعديل جديد: اللغة بتتحدد مرة واحدة على أساس "السؤال الأساسي" وبس ====
    # لو إحنا لسه في نص فلو توضيحي (تأكيد/اختيار/استكمال) على سؤال سابق،
    # بنفضل ملتزمين بلغة السؤال الأساسي اللي بدأ الفلو ده (state["lang"])
    # حتى لو الرد القصير ده جه بلغة مختلفة (زي "yes" وسط محادثة عربي، أو
    # "الأول" وسط محادثة إنجليزي) - عشان الرد النهائي يفضل متسق مع لغة
    # السؤال الأصلي مش لغة الرد القصير اللي بيختار بيه اليوزر رقم/تأكيد.
    # اللغة الوحيدة اللي بتتحدث فعليًا هي وقت سؤال جديد كامل (الفرع else تحت).
    locked_lang = state.get("lang", "ar")
    lang = locked_lang

    # ==== تعديل جديد: لو جالنا profile في الرسالة دي، نحدث بيه الـ state ====
    # بما إن الفرونت إند هيبعته مع كل رسالة، هيتحدث كل مرة تلقائيًا بآخر نسخة
    if profile is not None:
        state["profile"] = profile

    current_profile = state.get("profile")

    if state["waiting_for"] == "entity_confirm":
        if any(w in user_lower for w in ["اه", "أيوه", "ايوه", "yes", "آه","yeah","correct","صح"]):
            fake_input = CLASS_DESCRIPTIONS[state["pending_label"]](state["pending_entity"], lang)
            response = get_response(state["pending_label"], fake_input, state["pending_entity"], current_profile, lang)
            state["last_label"] = state["pending_label"]
            state["waiting_for"] = None
            state["pending_entity"] = None
            state["pending_label"] = None
        elif any(w in user_lower for w in ["لا", "no"]):
            response = "Alright, can you tell me more?" if lang == "en" else "معلش، ممكن توضحلي أكتر؟"
            state["waiting_for"] = None
            state["pending_entity"] = None
            state["pending_label"] = None
        else:
            response = "Yes or no?" if lang == "en" else "قولي اه أو لا؟"

    elif state["waiting_for"] == "clarification":
        if any(w in user_lower for w in ["اول", "الاول", "الأول", "1","أول","first"]):
            entity, _ = find_entity(state["last_user_input"], state["last_label"])
            if entity or state["last_label"] in ["greetings","out_of_scope"]:
                fake_input = CLASS_DESCRIPTIONS[state["last_label"]](entity, lang)
                state["waiting_for"] = None
            else:
                fake_input = state["last_user_input"]
                state["waiting_for"] = "followup"
            response = get_response(state["last_label"], fake_input, entity, current_profile, lang)

        elif any(w in user_lower for w in ["تاني", "التاني", "تانى", "التانى", "2","second"]):
            state["last_label"] = state["second_label"]
            entity, _ = find_entity(state["last_user_input"], state["last_label"])
            if entity or state["last_label"] in ["greetings","out_of_scope"]:
                fake_input = CLASS_DESCRIPTIONS[state["last_label"]](entity, lang)
                state["waiting_for"] = None
            else:
                fake_input = state["last_user_input"]
                state["waiting_for"] = "followup"
            response = get_response(state["last_label"], fake_input, entity, current_profile, lang)

        elif any(w in user_lower for w in ["تالت", "غير", "other", "اخر", "3","غيرهم"]):
            response = "Alright, tell me more exactly what you need." if lang == "en" else "تمام، وضحلي أكتر أنت محتاج إيه بالظبط؟"
            state["last_label"] = None
            state["last_user_input"] = ""
            state["waiting_for"] = None
        else:
            response = "Say the first option, the second, or something else?" if lang == "en" else "قولي الخيار الأول ولا الخيار التاني ولا غيرهم؟"

    elif state["waiting_for"] == "followup":
        combined = state["last_user_input"] + " " + user_input
        entity, _ = find_entity(combined, state["last_label"])
        if not entity:
            response = "Sorry, I don't have information about that right now!" if lang == "en" else "عذراً، مش عندي معلومات عن ده دلوقتي!"
            state["waiting_for"] = None
        else:
            fake_input = CLASS_DESCRIPTIONS[state["last_label"]](entity, lang)
            response = get_response(state["last_label"], fake_input, entity, current_profile, lang)
            state["waiting_for"] = None
        state["last_user_input"] = combined

    else:
        # ==== تعديل جديد: ده سؤال أساسي جديد، فهنا بس بنعيد اكتشاف اللغة
        # ونقفلها في الـ state عشان تتستخدم لأي فلو توضيحي/تأكيدي جاي بعد كده ====
        lang = detect_language(user_input, locked_lang)
        state["lang"] = lang

        state["original_text"] = user_input
        best_label, s_label, best_score, diff = predict(user_input, model, vectorizer)
        entity, _ = find_entity(user_input, best_label)

        if best_score < 0.18 or best_label =="out_of_scope":
                best_label="out_of_scope"
                response = get_response(best_label, user_input, None, current_profile, lang)
                print(f"بوت: {response}")
                waiting_for = None

        elif diff < 0.1:
            entity_best, _ = find_entity(user_input, best_label)
            entity_second, _ = find_entity(user_input, s_label)

            response = build_clarification_question(
                    best_label, s_label, entity_best, entity_second, user_input, lang
            )
            state["last_label"] = best_label
            state["second_label"] = s_label
            state["last_user_input"] = user_input
            state["waiting_for"] = "clarification"

        else:
            state["last_label"] = best_label
            state["last_user_input"] = user_input

            if is_short(user_input) and entity and best_label not in ["greetings", "out_of_scope"]:
                response = get_response(best_label, user_input, entity, current_profile, lang)
                state["pending_entity"] = entity
                state["pending_label"] = best_label
                state["waiting_for"] = "entity_confirm"
            elif entity:
                response = get_response(best_label, user_input, entity, current_profile, lang)
                state["waiting_for"] = None
            elif best_label not in ["greetings", "out_of_scope"]:
                response = get_response(best_label, user_input, None, current_profile, lang)
                state["waiting_for"] = "followup"
            else:
                response = get_response(best_label, user_input, None, current_profile, lang)
                state["waiting_for"] = None

    fallback = "Sorry, I can't help you right now." if lang == "en" else "معلش، مش قادر أساعدك دلوقتي."
    return response or fallback


class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None
    # ==== تعديل جديد: الحقل اللي الفرونت إند بيبعته باسم profile ====
    # استخدمنا Dict عادي (مش كلاس مخصص) عشان يقبل بالظبط نفس شكل
    # HealthProfileData اللي عند الفرونت إند من غير ما نكرر تعريفه هنا،
    # ونضمن إنه يتوافق حتى لو زودوا حقول جديدة بعدين.
    profile: Optional[Dict[str, Any]] = None


class ChatResponse(BaseModel):
    response: str
    session_id: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    session_id = req.session_id or str(uuid.uuid4())
    if session_id not in sessions:            
        sessions[session_id] = _new_state()

    # ==== تعديل: بنمرر req.profile لدالة process_message ====
    response = process_message(req.message, sessions[session_id], req.profile)
    return ChatResponse(response=response, session_id=session_id)


@app.delete("/session/{session_id}")
def clear_session(session_id: str):
    sessions.pop(session_id, None)
    return {"status": "cleared"}
