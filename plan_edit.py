# ============================================================
# plan_edit.py
# كل حاجة خاصة بتصنيف plan_edit
# ============================================================

PLAN_EDIT_ENTITIES = {
    "الأكل": ["breakfast", "فطار", "صباح", "dinner", "عشاء", "بليل", "lunch", "غداء", "العصر", "اكل", "وجبات", "food", "meals"],
    "التمارين": ["تمرين", "رياضي", "exercises", "gym", "جيم"],
}

def DESCRIPTION (entity="الأكل أو التمارين"): 
   if entity is None or entity == "":
        entity = "الأكل أو التمارين"
   return f"عايزني اغيرلك جدول {entity} 📋"

# هنا هتحط الـ API calls بتاعت الباك ايند عشان يعمل generate لخطة جديدة
# محتاج تتفق مع زميلك على الـ endpoint

def handle(user_input, entity, is_short_func, user_data={}):
    """الـ handler الخاص بـ plan_edit - محتاج ربط بالباك ايند"""
    if not entity:
        return "عايز تعدل ايه في خطتك؟ 📋"
    if is_short_func(user_input):
        return f"هل عايز تعدل {entity}؟ 📋"

    if entity == "الأكل":
        return "تمام 🍽️ جاري تعديل جدول أكلك بناء على طلبك..."

    elif entity == "التمارين":
        return "تمام 🏋️ جاري تعديل جدول تمارينك بناء على طلبك..."
