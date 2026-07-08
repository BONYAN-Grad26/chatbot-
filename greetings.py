# ============================================================
# greetings.py
# كل حاجة خاصة بتصنيف greetings
# ============================================================

GREETINGS_ENTITIES = {
    "islamic_greet": ["السلام عليكم"],
    "morning_greet": ["صباح الخير", "صباح النور", "صباحو"],
    "evening_greet": ["مساء الخير", "مساء النور", "مسا مسا"],
    "general_greet": ["hi", "hello", "اهلا", "مرحبا", "ازيك", "hey", "how are u"],
    "thanks": ["شكرا", "تسلم", "حبيبي", "جزاكم الله خيرا", "thanks", "thank you"],
}

DESCRIPTION_TEXT = {
    "ar": "لسة محددتش عايز ايه؟",
    "en": "You haven't told me what you need yet 🤔",
}

def DESCRIPTION(entity=None, lang="ar"):
    return DESCRIPTION_TEXT["en"] if lang == "en" else DESCRIPTION_TEXT["ar"]

# ردود عشوائية لكل نوع تحية
GREETINGS_RESPONSES = {
    "islamic_greet": ["وعليكم السلام ورحمة الله وبركاته! 🌙 أقدر أساعدك ازاي؟"],
    "morning_greet": ["صباح النور! ☀️ انا جاهز لمساعدتك في اللي محتاجه", "صباح الفل عليك! ☀️ اقدر أساعدك ازاي النهاردة؟"],
    "evening_greet": ["مساء النور! 🌙 محتاج مساعدة في إيه؟", "مساء الفل! 🌙 انا جاهز لمساعدتك"],
    "general_greet": ["أهلاً وسهلا بيك! 👋 اقدر أساعدك ازاي النهاردة؟", "هاي! 👋 عامل ايه؟ انا مستعد لاسئلتك واستفساراتك"],
    "thanks": ["العفو! 😊 تحت أمرك دايماً", "ولا يهمك! 🙌 لو احتجت حاجة تانية قولي"],
}

GREETINGS_RESPONSES_EN = {
    "islamic_greet": ["Peace be upon you too! 🌙 How can I help you?"],
    "morning_greet": ["Good morning! ☀️ I'm ready to help you with whatever you need", "Great morning to you! ☀️ How can I help you today?"],
    "evening_greet": ["Good evening! 🌙 What do you need help with?", "Good evening! 🌙 I'm ready to help"],
    "general_greet": ["Welcome! 👋 How can I help you today?", "Hey! 👋 How's it going? I'm ready for your questions"],
    "thanks": ["You're welcome! 😊 Always at your service", "No worries at all! 🙌 Let me know if you need anything else"],
}

def handle(user_input, entity, is_short_func, user_data={}, lang="ar"):
    """الـ handler الخاص بـ greetings"""
    import random
    if lang == "en":
        if not entity:
            return "I'm a chatbot designed to help and guide you, whether it's training or nutrition 🤖💪"
        responses = GREETINGS_RESPONSES_EN.get(entity, ["Welcome! 👋"])
        return random.choice(responses)

    if not entity:
        return "أنا شات بوت مصمم عشان أساعدك وأرشدك سواء في التمرين أو التغذية 🤖💪"
    if any(w in user_input.split() for w in ["السلام", "سلام"]):
        return "وعليكم السلام ورحمة الله وبركاته! 🌙 اقدر اساعدك ازاي؟"
    responses = GREETINGS_RESPONSES.get(entity, ["أهلاً بيك! 👋"])
    return random.choice(responses)
