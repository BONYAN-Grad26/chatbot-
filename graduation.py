import pandas as pd
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from thefuzz import process as fuzz_process

# استيراد كل تصنيف من ملفه
import exercise_help
import injury_precautions
import food_quantities
import plan_edit
import food_details
import greetings
import general_advice

# ============================================================
# تجميع البيانات من كل الملفات
# ============================================================
CLASS_DESCRIPTIONS = {
    "exercise_help":       exercise_help.DESCRIPTION,
    "food_quantities":     food_quantities.DESCRIPTION,
    "injury_precautions":  injury_precautions.DESCRIPTION,
    "plan_edit":           plan_edit.DESCRIPTION,
    "food_details":      food_details.DESCRIPTION,
    "general_advice":    general_advice.DESCRIPTION,
    "greetings":            lambda entity=None, lang="ar": (
        "You haven't told me what you need yet 🤔" if lang == "en" else "لسه محددتش عايز ايه 🤔"
    ),
    "out_of_scope":      lambda entity=None, lang="ar": (
        "Do you need something outside nutrition and exercise? 🤔" if lang == "en" else "محتاج حاجة خارج التغذية والتمرين؟ 🤔"
    ),
}

ENTITY_KEYWORDS = {
    "exercise_help":       exercise_help.EXERCISE_ENTITIES,
    "food_quantities":     food_quantities.FOOD_QUANTITIES_ENTITIES,
    "injury_precautions":  injury_precautions.INJURY_ENTITIES,
    "plan_edit":           plan_edit.PLAN_EDIT_ENTITIES,
    "food_details":        food_details.FOOD_DETAILS_ENTITIES,
    "general_advice":      general_advice.GENERAL_ADVICE_ENTITIES,
    "greetings":            greetings.GREETINGS_ENTITIES,
    "out_of_scope":        {},
}

INTENT_HANDLERS = {
    "exercise_help":      exercise_help.handle,
    "food_quantities":    food_quantities.handle,
    "injury_precautions": injury_precautions.handle,
    "plan_edit":           plan_edit.handle,
    "food_details":     food_details.handle,
    "general_advice":     general_advice.handle,
    "greetings":            greetings.handle,
    "out_of_scope":        lambda user_input, entity, is_short_func, user_data={}, lang="ar": (
        "I'm a chatbot specialized in nutrition and exercise questions and tips only 🏋️🍽️... sorry, I can't help you with what you're asking about"
        if lang == "en" else
        "أنا بوت متخصص في اسئلة ونصايح التغذية والتمارين بس 🏋️🍽️... معلش مقدرش أساعدك في اللي بتسأل عليه"
    ),
}

# ============================================================
# PREPROCESSING
# ============================================================
STOP_WORDS = [
    "أنا", "انا", "في", "على", "من", "إلى", "الى", "و", "أو", "او",
    "هل", "ما", "ماذا", "كيف", "لماذا", "متى", "أين", "اين",
    "هو", "هي", "هم", "نحن", "أنت", "انت", "ده", "دي", "دول",
    "فى", "عن", "مع", "بعد", "قبل", "لو", "لأن", "لان",
    "بس", "يعني", "كده", "كدا", "اللي", "اللى", "إللي",
    "عايز", "عاوز", "بدي", "أريد", "اريد", "محتاج",
    "ال", "الـ", "وال",
    "i", "me", "my", "the", "a", "an", "is", "are", "was",
    "what", "how", "can", "do", "to", "for", "of", "in", "and"
]

VALID_LABELS = list(CLASS_DESCRIPTIONS.keys())
FILE_PATH = "dataset_improved_v2.xlsx"

def preprocess(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s\u0600-\u06FF]', ' ', text)
    text = re.sub(r'\d+', '', text)
    words = text.split()
    words = [w for w in words if w not in STOP_WORDS and len(w) > 1]
    return ' '.join(words)

def is_short(text):
    return len(text.strip().split()) <= 2

# ============================================================
# اكتشاف اللغة
# ============================================================
_ARABIC_RE = re.compile(r'[\u0600-\u06FF]')
_LATIN_RE = re.compile(r'[A-Za-z]')

def detect_language(text, previous=None):
    """
    بيكتشف لغة الرسالة: لو فيها حروف عربي بيعتبرها عربي (حتى لو فيها كلمات
    إنجليزية جوه زي أسماء تمارين)، ولو مفيش عربي خالص وفيها حروف لاتينية
    بيعتبرها إنجليزي.

    لو الرسالة مفيهاش أي حروف خالص (زي رقم لوحده "1" أو "2" رداً على سؤال
    توضيحي، أو إيموجي بس) - معندناش أي إشارة لغوية نعتمد عليها، فبنرجع
    "previous" (آخر لغة اتكلم بيها اليوزر في المحادثة) بدل ما نفترض عربي
    بشكل تعسفي ونكسر الاستمرارية لو المحادثة كانت ماشية بالإنجليزي.
    """
    if text:
        if _ARABIC_RE.search(text):
            return "ar"
        if _LATIN_RE.search(text):
            return "en"
    return previous or "ar"

# ============================================================
# FUZZY SEARCH
# ============================================================
def find_entity(user_input, label, threshold=80):
    entities = ENTITY_KEYWORDS.get(label, {})
    if not entities:
        return None, 0

    all_variants = []
    for entity_name, variants in entities.items():
        if isinstance(variants, list):
            for variant in variants:
                all_variants.append((entity_name, variant))

    if not all_variants:
        return None, 0

    variants_list = [v for _, v in all_variants]

    words = user_input.lower().split()
    candidates = words.copy()
    for i in range(len(words) - 1):
        candidates.append(words[i] + " " + words[i+1])
    for i in range(len(words) - 2):
        candidates.append(words[i] + " " + words[i+1] + " " + words[i+2])

    best_entity = None
    best_score = 0
    for candidate in candidates:
        word_threshold = 95 if len(candidate) <= 3 else threshold
        match, score = fuzz_process.extractOne(candidate, variants_list)
        if score >= word_threshold and score > best_score:
            best_score = score
            best_entity = next(name for name, v in all_variants if v == match)

    return best_entity, best_score

# ============================================================
# تصحيح الداتا
# ============================================================

# ============================================================
# TRAIN
# ============================================================
def load_data(file_path):
    df = pd.read_excel(file_path)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    print(f"✅ تم تحميل الداتا: {len(df)} جملة")
    print(f"\n📈 توزيع الداتا:\n{df['label'].value_counts()}")
    return df

def train_model(df):
    df['clean_text'] = df['text'].apply(preprocess)
    X = df['clean_text']
    y = df['label']

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    print(f"\n📚 جمل التدريب: {len(X_train)}")
    print(f"📝 جمل الـ Validation: {len(X_val)}")

    vectorizer = TfidfVectorizer(
        analyzer='char_wb',
        ngram_range=(2,4),
        max_features=10000,
        sublinear_tf=True
    )

    X_train_vec = vectorizer.fit_transform(X_train)
    X_val_vec = vectorizer.transform(X_val)

    model = LogisticRegression(max_iter=1000, C=2, class_weight='balanced')
    model.fit(X_train_vec, y_train)

    train_pred = model.predict(X_train_vec)
    val_pred = model.predict(X_val_vec)

    train_acc = accuracy_score(y_train, train_pred)
    val_acc = accuracy_score(y_val, val_pred)

    print(f"\n{'='*40}")
    print(f"🏋️  دقة التدريب:    {train_acc * 100:.1f}%")
    print(f"📊  دقة Validation: {val_acc * 100:.1f}%")

    diff = train_acc - val_acc
    if diff > 0.15:
        print(f"⚠️  فرق كبير ({diff*100:.1f}%) → ممكن Overfitting!")
    else:
        print(f"✅ الفرق صغير ({diff*100:.1f}%) → الموديل كويس")

    print(f"\n📋 تقرير تفصيلي:\n")
    print(classification_report(y_val, val_pred))

    return model, vectorizer

def save_model(model, vectorizer):
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    print("✅ تم حفظ الموديل!")

# ============================================================
# PREDICT
# ============================================================
def predict(text, model, vectorizer):
    clean = preprocess(text)
    vec = vectorizer.transform([clean])
    proba = model.predict_proba(vec)[0]

    sorted_indices = proba.argsort()[::-1]
    best_label = model.classes_[sorted_indices[0]]
    second_label = model.classes_[sorted_indices[1]]
    best_score = proba[sorted_indices[0]]
    diff = best_score - proba[sorted_indices[1]]

    return best_label, second_label, best_score, diff

# ============================================================
# RESPONSE DISPATCH
# ============================================================
def get_response(label, user_input, entity, user_data={}, lang="ar"):
    handler = INTENT_HANDLERS.get(label)
    if handler:
        result = handler(user_input, entity, is_short, user_data, lang)
        if result is None:
            return f"[{label} | entity: {entity}]"
        return result
    return (
        "Sorry, I can't help you with what you're asking about right now 🙏"
        if lang == "en" else
        "معلش، مش قادر أساعدك في اللي بتسأل عنه دلوقتي 🙏"
    )

def deliver_response(label, user_input, entity, original_text, lang="ar"):
    response = get_response(label, user_input, entity, {}, lang)
    print(f"بوت: {response}")

    return label

def build_clarification_question(best_label, s_label, entity_best, entity_second, user_input, lang="ar"):
    desc1 = CLASS_DESCRIPTIONS.get(best_label, best_label)
    desc2 = CLASS_DESCRIPTIONS.get(s_label, s_label)
    if lang == "en":
        return f"{desc1(entity_best, lang)} or {desc2(entity_second, lang)}, or something else entirely ❓"
    return f"{desc1(entity_best)} ولا {desc2(entity_second)} ولا عايز حاجة تانية ❓"

# ============================================================
# MAIN CHAT LOOP
# ============================================================
def chat(model, vectorizer):
    print("\n" + "="*40)
    print("🤖 الشات بوت جاهز! (اكتب 'خروج' للوقف)")
    print("="*40 + "\n")

    last_label = None
    second_label = None
    last_user_input = ""
    waiting_for = None
    pending_entity = None
    pending_label = None
    original_text = ""
    current_lang = "ar"

    while True:
        user_input = input("أنت: ").strip()

        if user_input.lower() in ['خروج', 'exit', 'quit', "اخرج"]:
            print("👋 وداعاً!")
            break
        if not user_input:
            continue

        # ==== تعديل جديد: اللغة بتتقفل على لغة "السؤال الأساسي" ====
        # لو إحنا في فلو توضيحي/تأكيدي (entity_confirm/clarification/followup)
        # منعيدش اكتشاف اللغة من الرد القصير ده، وبنفضل مستخدمين لغة السؤال
        # اللي بدأ الفلو. اللغة بتتحدث فعليًا بس وقت سؤال أساسي جديد (تحت).
        lang = current_lang

        if waiting_for == "entity_confirm":
            user_lower = user_input.lower()

            if any(w in user_lower for w in ["اه", "أيوه", "ايوه", "yes", "آه","صح","correct","yeah"]):
                fake_input = f"{CLASS_DESCRIPTIONS.get(pending_label)(pending_entity, lang)}"
                deliver_response(pending_label, fake_input, pending_entity, original_text, lang)
                last_label = pending_label
                waiting_for = None
                pending_entity = None
                pending_label = None

            elif any(w in user_lower for w in ["لا", "no"]):
                print("بوت: " + ("Alright, can you tell me more?" if lang == "en" else "معلش، ممكن توضحلي أكتر؟"))
                waiting_for = None
                pending_entity = None
                pending_label = None

            else:
                print("بوت: " + ("Yes or no?" if lang == "en" else "قولي اه أو لا؟"))

        elif waiting_for == "clarification":
            user_lower = user_input.lower()

            if any(w in user_lower for w in ["اول", "الاول", "الأول", "1","first","أول"]):
                entity, _ = find_entity(last_user_input, last_label)
                if entity or last_label in ["greetings","out_of_scope"]:
                    fake_input = f"{CLASS_DESCRIPTIONS.get(last_label)(entity, lang)}"
                    waiting_for = None
                else:
                    fake_input = last_user_input
                    waiting_for = "followup"
                deliver_response(last_label, fake_input, entity, original_text, lang)

            elif any(w in user_lower for w in ["تاني", "التاني", "تانى", "التانى", "2","second","ثاني", "الثاني", "ثانى", "الثانى"]):
                last_label = second_label
                entity, _ = find_entity(last_user_input, last_label)
                if entity or last_label in ["greetings","out_of_scope"]:
                    fake_input = f"{CLASS_DESCRIPTIONS.get(last_label)(entity, lang)}"
                    waiting_for = None
                else:
                    fake_input = last_user_input
                    waiting_for = "followup"
                deliver_response(last_label, fake_input, entity, original_text, lang)

            elif any(w in user_lower for w in ["تالت", "غير", "other", "اخر", "3","غيرهم","أخر","آخر"]):
                print("بوت: " + ("Alright, tell me more exactly what you need." if lang == "en" else "تمام، وضحلي أكتر أنت محتاج إيه بالظبط؟"))
                last_label = None
                last_user_input = ""
                waiting_for = None

            else:
                print("بوت: " + ("Say the first option, the second, or something else?" if lang == "en" else "قولي الخيار الأول ولا الخيار التاني ولا حاجة غيرهم؟"))

        elif waiting_for == "followup":
            combined = last_user_input + " " + user_input
            entity, score = find_entity(combined, last_label)

            if not entity:
                print("بوت: " + ("Sorry, I don't have information about that right now!" if lang == "en" else "عذراً، مش عندي معلومات عن ده دلوقتي!"))
                waiting_for = None
            else:
                fake_input = f"{CLASS_DESCRIPTIONS.get(last_label)(entity, lang)}"
                deliver_response(last_label, fake_input, entity, original_text, lang)
                waiting_for = None

            last_user_input = combined

        else:
            # ==== تعديل جديد: سؤال أساسي جديد -> نعيد اكتشاف اللغة ونقفلها ====
            lang = detect_language(user_input, current_lang)
            current_lang = lang

            original_text = user_input
            best_label, s_label, best_score, diff = predict(user_input, model, vectorizer)
            entity, entity_score = find_entity(user_input, best_label)
            if best_score < 0.18 or best_label =="out_of_scope":
                best_label="out_of_scope"
                response = get_response(best_label, user_input, None, {}, lang)
                print(f"بوت: {response}")
                waiting_for = None

            elif diff < 0.1:
                entity_best, _ = find_entity(user_input, best_label)
                entity_second, _ = find_entity(user_input, s_label)
                question = build_clarification_question(best_label, s_label, entity_best, entity_second, user_input, lang)
                print(f"بوت: {question}")
                last_label = best_label
                second_label = s_label
                last_user_input = user_input
                waiting_for = "clarification"

            else:
                last_label = best_label
                last_user_input = user_input

                if is_short(user_input) and entity and best_label not in ["greetings", "out_of_scope"]:
                    response = get_response(best_label, user_input, entity, {}, lang)
                    print(f"بوت: {response}")
                    pending_entity = entity
                    pending_label = best_label
                    waiting_for = "entity_confirm"

                elif entity:
                    deliver_response(best_label, user_input, entity, original_text, lang)
                    waiting_for = None

                elif not entity and best_label not in ["greetings", "out_of_scope"]:
                    response = get_response(best_label, user_input, None, {}, lang)
                    print(f"بوت: {response}")
                    waiting_for = "followup"

                else:
                    deliver_response(best_label, user_input, None, original_text, lang)
                    waiting_for = None

# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    TRAIN_MODE = True

    if TRAIN_MODE:
        df = load_data(FILE_PATH)
        model, vectorizer = train_model(df)
        save_model(model, vectorizer)
    else:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
        print("✅ تم تحميل الموديل المحفوظ!")
    
    chat(model, vectorizer)
