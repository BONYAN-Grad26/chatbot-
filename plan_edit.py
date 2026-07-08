# ============================================================
# plan_edit.py
# كل حاجة خاصة بتصنيف plan_edit
# ============================================================

PLAN_EDIT_ENTITIES = {
    "الأكل": ["breakfast", "فطار", "صباح", "dinner", "عشاء", "بليل", "lunch", "غداء", "العصر", "اكل", "وجبات", "food", "meals"],
    "التمارين": ["تمرين", "رياضي", "exercises", "gym", "جيم"],
}

ENTITY_EN = {
    "الأكل": "meal plan",
    "التمارين": "workout plan",
}

def DESCRIPTION(entity="الأكل أو التمارين", lang="ar"):
    if entity is None or entity == "":
        entity = "الأكل أو التمارين" if lang != "en" else "your meal or workout plan"
    if lang == "en":
        entity_en = ENTITY_EN.get(entity, entity)
        return f"Want me to change your {entity_en}?"
    return f"عايزني اغيرلك جدول {entity}"

# هنا هتحط الـ API calls بتاعت الباك ايند عشان يعمل generate لخطة جديدة
# محتاج تتفق مع زميلك على الـ endpoint

def handle(user_input, entity, is_short_func, user_data={}, lang="ar"):
    """الـ handler الخاص بـ plan_edit - محتاج ربط بالباك ايند"""
    if lang == "en":
        if not entity:
            return "What would you like to change in your plan?"
        entity_en = ENTITY_EN.get(entity, entity)
        if is_short_func(user_input):
            return f"Do you want to edit your {entity_en}?"

        if entity == "الأكل":
            return "Updating your meal plan based on your request"
        elif entity == "التمارين":
            return "Updating your workout plan based on your request"

    if not entity:
        return "عايز تعدل ايه في خطتك؟"
    if is_short_func(user_input):
        return f"هل عايز تعدل {entity}؟"

    if entity == "الأكل":
        return "جاري تعديل جدول أكلك بناء على طلبك"

    elif entity == "التمارين":
        return "جاري تعديل جدول تمارينك بناء على طلبك"
