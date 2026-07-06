import pickle
import uuid
from typing import Any, Dict, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from graduation import (
    CLASS_DESCRIPTIONS,
    build_clarification_question,
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
    }


# ==== تعديل: الدالة بقت بتاخد profile كمان (اختياري) ====
def process_message(user_input: str, state: dict, profile: Optional[Dict[str, Any]] = None) -> str:
    user_lower = user_input.lower()

    # ==== تعديل جديد: لو جالنا profile في الرسالة دي، نحدث بيه الـ state ====
    # بما إن الفرونت إند هيبعته مع كل رسالة، هيتحدث كل مرة تلقائيًا بآخر نسخة
    if profile is not None:
        state["profile"] = profile

    current_profile = state.get("profile")

    if state["waiting_for"] == "entity_confirm":
        if any(w in user_lower for w in ["اه", "أيوه", "ايوه", "yes", "آه","yeah","correct","صح"]):
            fake_input = CLASS_DESCRIPTIONS[state["pending_label"]](state["pending_entity"])
            response = get_response(state["pending_label"], fake_input, state["pending_entity"], current_profile)
            state["last_label"] = state["pending_label"]
            state["waiting_for"] = None
            state["pending_entity"] = None
            state["pending_label"] = None
        elif any(w in user_lower for w in ["لا", "no"]):
            response = "معلش، ممكن توضحلي أكتر؟"
            state["waiting_for"] = None
            state["pending_entity"] = None
            state["pending_label"] = None
        else:
            response = "قولي اه أو لا؟"

    elif state["waiting_for"] == "clarification":
        if any(w in user_lower for w in ["اول", "الاول", "الأول", "1","أول","first"]):
            entity, _ = find_entity(state["last_user_input"], state["last_label"])
            if entity or state["last_label"] in ["greetings","out_of_scope"]:
                fake_input = CLASS_DESCRIPTIONS[state["last_label"]](entity)
                state["waiting_for"] = None
            else:
                fake_input = state["last_user_input"]
                state["waiting_for"] = "followup"
            response = get_response(state["last_label"], fake_input, entity, current_profile)

        elif any(w in user_lower for w in ["تاني", "التاني", "تانى", "التانى", "2","second"]):
            state["last_label"] = state["second_label"]
            entity, _ = find_entity(state["last_user_input"], state["last_label"])
            if entity or state["last_label"] in ["greetings","out_of_scope"]:
                fake_input = CLASS_DESCRIPTIONS[state["last_label"]](entity)
                state["waiting_for"] = None
            else:
                fake_input = state["last_user_input"]
                state["waiting_for"] = "followup"
            response = get_response(state["last_label"], fake_input, entity, current_profile)

        elif any(w in user_lower for w in ["تالت", "غير", "other", "اخر", "3","غيرهم"]):
            response = "تمام، وضحلي أكتر أنت محتاج إيه بالظبط؟"
            state["last_label"] = None
            state["last_user_input"] = ""
            state["waiting_for"] = None
        else:
            response = "قولي الخيار الأول ولا الخيار التاني ولا غيرهم؟"

    elif state["waiting_for"] == "followup":
        combined = state["last_user_input"] + " " + user_input
        entity, _ = find_entity(combined, state["last_label"])
        if not entity:
            response = "عذراً، مش عندي معلومات عن ده دلوقتي!"
            state["waiting_for"] = None
        else:
            fake_input = CLASS_DESCRIPTIONS[state["last_label"]](entity)
            response = get_response(state["last_label"], fake_input, entity, current_profile)
            state["waiting_for"] = None
        state["last_user_input"] = combined

    else:
        state["original_text"] = user_input
        best_label, s_label, best_score, diff = predict(user_input, model, vectorizer)
        entity, _ = find_entity(user_input, best_label)

        if best_score < 0.25 :
                best_label="out_of_scope"
                response = get_response(best_label,user_input,None)
                print(f"بوت: {response}")
                waiting_for = None

        elif diff < 0.1:
            entity_best, _ = find_entity(user_input, best_label)
            entity_second, _ = find_entity(user_input, s_label)

            response = build_clarification_question(
                    best_label, s_label, entity_best, entity_second, user_input
            )
            state["last_label"] = best_label
            state["second_label"] = s_label
            state["last_user_input"] = user_input
            state["waiting_for"] = "clarification"

        else:
            state["last_label"] = best_label
            state["last_user_input"] = user_input

            if is_short(user_input) and entity and best_label not in ["greetings", "out_of_scope"]:
                response = get_response(best_label, user_input, entity, current_profile)
                state["pending_entity"] = entity
                state["pending_label"] = best_label
                state["waiting_for"] = "entity_confirm"
            elif entity:
                response = get_response(best_label, user_input, entity, current_profile)
                state["waiting_for"] = None
            elif best_label not in ["greetings", "out_of_scope"]:
                response = get_response(best_label, user_input, None, current_profile)
                state["waiting_for"] = "followup"
            else:
                response = get_response(best_label, user_input, None, current_profile)
                state["waiting_for"] = None

    return response or "معلش، مش قادر أساعدك دلوقتي."


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
