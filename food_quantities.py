# ============================================================
# food_quantities.py
# كل حاجة خاصة بتصنيف food_quantities
# ============================================================
#
# المعادلات هنا مبنية على مصادر عالمية معتمدة:
# - البروتين:  ISSN Position Stand: Protein and Exercise (2017)
# - البروتين وقت الديفيسيت: ISSN Position Stand: Diets and Body Composition (2017)
# - البروتين النباتي: ISSN - Plant-based protein bioavailability (جودة أقل، يحتاج زيادة ~15%)
# - الدهون:    Acceptable Macronutrient Distribution Range - IOM / Dietary Guidelines for Americans
#              + خصائص كل نظام غذائي معروفة (Mediterranean diet studies, Paleo diet composition studies)
# - الكارب:    ISSN / ACSM Guidelines for Carbohydrate Intake in Athletes
# - المياه:    EFSA Scientific Opinion on Water / IOM Dietary Reference Intakes (~35 مل لكل كيلو تقريبًا)
# - الألياف:   USDA Dietary Guidelines for Americans (14g لكل 1000 كالوري)
# - الكرياتين: ISSN Position Stand: Creatine Supplementation and Exercise
# - الكافيين:  FDA / EFSA safe daily intake (حتى 400 مجم لليوم للشخص السليم البالغ)
#
# ملحوظة: القيم دي متوسطات علمية عامة مش استشارة طبية، ولو فيه ملاحظات طبية
# (medicalNotes) لازم الشخص يرجع لدكتور/أخصائي تغذية قبل ما يطبق أي رقم فيها.
#
# ملحوظة تصميم مهمة: كل الحقول اللي شكلها "اختيار من قايمة" (enum) - يعني
# activityLevel, dietGoal, dietType, gender - بيتم التعامل معاها بمطابقة
# دقيقة (exact match) على القيم الحقيقية المتفق عليها مع الفرونت إند، مش
# بالبحث عن كلمة جوه النص. ده عشان نضمن نتيجة صحيحة 100% ومفيش تداخل بين
# الخيارات (زي "Very Active" و"Moderately Active" اللي كلاهما يحتوي "Active").
# ============================================================

FOOD_QUANTITIES_ENTITIES = {
    "السعرات الحرارية": ["calories", "كالوري", "سعرات", "السعرات"],
    "البروتين": ["protein", "بروتين"],
    "الكارب": ["carb", "carbohydrates", "كارب", "كربوهيدرات", "نشويات"],
    "الدهون الصحية": ["fats", "دهون","دهون صحية"],
    "المياه": ["water", "مية", "مياه", "سوائل"],
    "الألياف": ["fiber", "ألياف"],
    "الكرياتين": ["creatine", "كرياتين"],
    "الكافيين": ["caffeine", "كافيين", "قهوة"],
    "الفيتامينات": ["vitamin", "فيتامين"],
}

# أسماء العناصر بالإنجليزي
ENTITY_EN = {
    "السعرات الحرارية": "calories",
    "البروتين": "protein",
    "الكارب": "carbs",
    "الدهون الصحية": "healthy fats",
    "المياه": "water",
    "الألياف": "fiber",
    "الكرياتين": "creatine",
    "الكافيين": "caffeine",
    "الفيتامينات": "vitamins",
}


def DESCRIPTION(entity="عنصر معين؟", lang="ar"):
    if entity is None or entity == "":
        entity = "عنصر معين" if lang != "en" else "a specific nutrient"
    if lang == "en":
        entity_en = ENTITY_EN.get(entity, entity)
        return f"Want me to calculate your daily {entity_en} needs? 🧮"
    return f"عايزني احسبلك احتياجك اليومي من {entity} 🧮"


# ============================================================
# القيم الحقيقية للـ enums (بعد التطبيع عن طريق _norm)
# ============================================================

ACTIVITY_SEDENTARY = "sedentary"
ACTIVITY_LIGHT = "lightly_active"
ACTIVITY_MODERATE = "moderately_active"
ACTIVITY_HIGH = "very_active"

GOAL_LOSS = "weight_loss"
GOAL_GAIN = "muscle_gain"
GOAL_MAINTENANCE = "maintenance"
GOAL_HEALTH = "improve_health"

DIET_BALANCED = "balanced_diet"
DIET_VEGAN = "vegan"
DIET_PALEO = "paleo"
DIET_HIGH_PROTEIN = "high_protein"
DIET_MEDITERRANEAN = "mediterranean"

GENDER_MALE = "male"
GENDER_FEMALE = "female"


# ============================================================
# Helpers - قراءة بيانات اليوزر بأمان
# ============================================================

def _get(user_data, key, default=None):
    """بيرجع القيمة من user_data لو موجودة، أو الديفولت لو مش موجودة/None"""
    if not user_data:
        return default
    val = user_data.get(key, default)
    return default if val is None else val


def _norm(value):
    """توحيد شكل النص عشان نقارن الـ enums (gender, activityLevel, dietType, dietGoal)"""
    if not value:
        return ""
    return str(value).strip().lower().replace("-", "_").replace(" ", "_")


def _has_user_data(user_data):
    """بنتأكد إن فيه بيانات كفاية للحساب (لازم وزن على الأقل)"""
    return bool(user_data) and _get(user_data, "weightKg") is not None


def _activity_level(user_data):
    """بترجع مستوى النشاط كقيمة موحدة من القيم الأربعة الحقيقية فقط"""
    activity = _norm(_get(user_data, "activityLevel"))
    if activity == ACTIVITY_SEDENTARY:
        return ACTIVITY_SEDENTARY
    if activity == ACTIVITY_LIGHT:
        return ACTIVITY_LIGHT
    if activity == ACTIVITY_MODERATE:
        return ACTIVITY_MODERATE
    if activity == ACTIVITY_HIGH:
        return ACTIVITY_HIGH
    # قيمة غير متوقعة/غير موجودة -> نتعامل معاها كمتوسط (moderately active)
    return ACTIVITY_MODERATE


def _diet_goal(user_data):
    """بترجع هدف الدايت كقيمة موحدة من القيم الأربعة الحقيقية فقط"""
    goal = _norm(_get(user_data, "dietGoal"))
    if goal == GOAL_LOSS:
        return GOAL_LOSS
    if goal == GOAL_GAIN:
        return GOAL_GAIN
    if goal == GOAL_HEALTH:
        return GOAL_HEALTH
    return GOAL_MAINTENANCE


def _diet_type(user_data):
    """بترجع نوع النظام الغذائي كقيمة موحدة من القيم الخمسة الحقيقية فقط"""
    diet = _norm(_get(user_data, "dietType"))
    if diet == DIET_VEGAN:
        return DIET_VEGAN
    if diet == DIET_PALEO:
        return DIET_PALEO
    if diet == DIET_HIGH_PROTEIN:
        return DIET_HIGH_PROTEIN
    if diet == DIET_MEDITERRANEAN:
        return DIET_MEDITERRANEAN
    return DIET_BALANCED


def _gender(user_data):
    g = _norm(_get(user_data, "gender"))
    return GENDER_FEMALE if g == GENDER_FEMALE else GENDER_MALE


# ============================================================
# الحسابات الأساسية
# ============================================================

def calculate_protein(user_data):
    """
    بروتين بناءً على هدف اليوزر (dietGoal) بالدرجة الأولى، ومستوى النشاط
    كعامل مساعد وقت الحفاظ/تحسين الصحة.
    المصدر: ISSN Position Stand - Protein and Exercise (2017)
    - نزول وزن (Weight Loss): 2.3-2.8 g/kg من الـ Lean Mass (حماية العضل وقت الديفيسيت)
    - زيادة عضل (Muscle Gain): 1.6-2.2 g/kg من وزن الجسم
    - محافظة/تحسين صحة: 1.0-1.8 g/kg حسب مستوى النشاط
    + Vegan: زيادة 15% إضافية (جودة امتصاص البروتين النباتي أقل - ISSN)
    """
    weight = _get(user_data, "weightKg", 70)
    lean_mass = _get(user_data, "leanMass")
    goal = _diet_goal(user_data)
    activity = _activity_level(user_data)
    diet = _diet_type(user_data)

    if goal == GOAL_LOSS:
        base = lean_mass if lean_mass else weight * 0.8  # تقدير تقريبي لو الـ lean mass مش متوفرة
        low, high = 2.3, 2.8
        grams_low = round(base * low)
        grams_high = round(base * high)
        basis = "الكتلة الخالية من الدهون (Lean Mass)"
        basis_en = "lean body mass"

    elif goal == GOAL_GAIN:
        low, high = 1.6, 2.2
        grams_low = round(weight * low)
        grams_high = round(weight * high)
        basis = "وزن الجسم الكلي"
        basis_en = "total body weight"

    else:  # Maintenance / Improve Health -> حسب مستوى النشاط
        activity_ranges = {
            ACTIVITY_SEDENTARY: (1.0, 1.2),
            ACTIVITY_LIGHT: (1.2, 1.4),
            ACTIVITY_MODERATE: (1.4, 1.6),
            ACTIVITY_HIGH: (1.6, 1.8),
        }
        low, high = activity_ranges[activity]
        grams_low = round(weight * low)
        grams_high = round(weight * high)
        basis = "وزن الجسم الكلي"
        basis_en = "total body weight"

    # تعويض جودة الامتصاص الأقل للبروتين النباتي
    if diet == DIET_VEGAN:
        grams_low = round(grams_low * 1.15)
        grams_high = round(grams_high * 1.15)

    target = round((grams_low + grams_high) / 2)
    calories = target * 4

    return {
        "low": grams_low,
        "high": grams_high,
        "target": target,
        "calories": calories,
        "basis": basis,
        "basis_en": basis_en,
        "range_per_kg": (low, high),
        "vegan_adjusted": diet == DIET_VEGAN,
    }


def calculate_fats(user_data):
    """
    الدهون كنسبة من السعرات اليومية، حسب نوع النظام الغذائي (dietType).
    المصدر: Acceptable Macronutrient Distribution Range (IOM) / Dietary Guidelines for Americans
    - Balanced Diet: 20%-35% (المعيار العام)
    - High Protein: 20%-30% (مساحة أقل لأن البروتين بياخد نسبة أعلى)
    - Mediterranean: 30%-40% (زيت زيتون، مكسرات، أسماك دهنية - معروف بارتفاع الدهون الصحية)
    - Paleo: 30%-40% (مفيش حبوب/بقوليات كمصدر طاقة، فالدهون والبروتين بياخدوا مكانهم)
    - Vegan: 20%-30% (الأنظمة النباتية غالبًا أقل دهون طبيعيًا)
    مع حد أدنى بيولوجي: ~0.5 g/kg من وزن الجسم مهما كان النظام (مهم للهرمونات)
    """
    weight = _get(user_data, "weightKg", 70)
    tdee = _get(user_data, "tdee") or _get(user_data, "dailyCalorieTarget", 2200)
    diet = _diet_type(user_data)

    diet_ranges = {
        DIET_BALANCED: (0.20, 0.35),
        DIET_HIGH_PROTEIN: (0.20, 0.30),
        DIET_MEDITERRANEAN: (0.30, 0.40),
        DIET_PALEO: (0.30, 0.40),
        DIET_VEGAN: (0.20, 0.30),
    }
    pct_low, pct_high = diet_ranges[diet]

    cal_low = tdee * pct_low
    cal_high = tdee * pct_high
    grams_low = round(cal_low / 9)
    grams_high = round(cal_high / 9)

    # حد أدنى بيولوجي - متنزلش تحته حتى لو النظام قليل دهون جدًا
    min_biological = round(weight * 0.5)
    if grams_low < min_biological:
        grams_low = min_biological
        if grams_high < grams_low:
            grams_high = grams_low + 10

    target = round((grams_low + grams_high) / 2)

    return {
        "low": grams_low,
        "high": grams_high,
        "target": target,
        "calories": target * 9,
        "pct_range": (pct_low, pct_high),
        "diet_type": diet,
    }


def calculate_carbs(user_data, protein_result=None, fats_result=None):
    """
    الكارب = باقي السعرات بعد البروتين والدهون، مع مدى مرجعي حسب مستوى
    النشاط (activityLevel)، وتخفيض إضافي لنظام Paleo (مفيش حبوب كمصدر أساسي).
    المصدر: ISSN / ACSM Carbohydrate Guidelines for Athletes
    - Sedentary: 2-3 g/kg
    - Lightly Active: 3-5 g/kg
    - Moderately Active: 5-7 g/kg
    - Very Active: 6-10 g/kg
    """
    weight = _get(user_data, "weightKg", 70)
    tdee = _get(user_data, "tdee") or _get(user_data, "dailyCalorieTarget", 2200)
    activity = _activity_level(user_data)
    diet = _diet_type(user_data)

    protein_result = protein_result or calculate_protein(user_data)
    fats_result = fats_result or calculate_fats(user_data)

    activity_ranges = {
        ACTIVITY_SEDENTARY: (2, 3),
        ACTIVITY_LIGHT: (3, 5),
        ACTIVITY_MODERATE: (5, 7),
        ACTIVITY_HIGH: (6, 10),
    }
    low_gkg, high_gkg = activity_ranges[activity]

    if diet == DIET_PALEO:
        # Paleo بيستبعد الحبوب/البقوليات كمصدر أساسي للكارب، فالمدى بيقل عن العادي
        grams_low = round(weight * max(low_gkg - 1, 1))
        grams_high = round(weight * max(high_gkg - 2, low_gkg))
    else:
        # الكارب = باقي السعرات بعد أعلى وأقل حد من البروتين والدهون
        remaining_cal_min = tdee - protein_result["high"] * 4 - fats_result["high"] * 9
        remaining_cal_max = tdee - protein_result["low"] * 4 - fats_result["low"] * 9
        grams_low = max(round(remaining_cal_min / 4), 0)
        grams_high = max(round(remaining_cal_max / 4), grams_low)

    target = round((grams_low + grams_high) / 2)

    return {
        "low": grams_low,
        "high": grams_high,
        "target": target,
        "activity_range_per_kg": (low_gkg, high_gkg),
        "paleo_adjusted": diet == DIET_PALEO,
    }


def calculate_water(user_data):
    """
    المياه اليومية.
    المصدر: EFSA / IOM Dietary Reference Intakes - تقريبًا 35 مل لكل كيلو من وزن الجسم
    + إضافي حسب مستوى النشاط (تعويض العرق):
    - Sedentary: +0 مل
    - Lightly Active: +250 مل
    - Moderately Active: +500 مل
    - Very Active: +750 مل
    """
    weight = _get(user_data, "weightKg", 70)
    activity = _activity_level(user_data)

    base_ml = weight * 35

    extra_by_activity = {
        ACTIVITY_SEDENTARY: 0,
        ACTIVITY_LIGHT: 250,
        ACTIVITY_MODERATE: 500,
        ACTIVITY_HIGH: 750,
    }
    extra_ml = extra_by_activity[activity]

    total_ml = base_ml + extra_ml
    liters = round(total_ml / 1000, 1)

    return {
        "ml": round(total_ml),
        "liters": liters,
        "extra_for_activity_ml": extra_ml,
    }


def calculate_fiber(user_data):
    """
    الألياف اليومية.
    المصدر: USDA Dietary Guidelines for Americans - 14 جم ألياف لكل 1000 كالوري
    مع حد أدنى تقريبي حسب الجندر (Adequate Intake - IOM): رجالة ~38g / ستات ~25g
    """
    tdee = _get(user_data, "tdee") or _get(user_data, "dailyCalorieTarget", 2200)
    gender = _gender(user_data)

    from_calories = round((tdee / 1000) * 14)
    floor = 38 if gender == GENDER_MALE else 25

    target = max(from_calories, floor - 5)  # مانخليش الرقم يبعد جدًا عن الحد الأدنى المعروف

    return {
        "target": target,
        "floor_reference": floor,
    }


def calculate_creatine(user_data):
    """
    الكرياتين مونوهيدرات.
    المصدر: ISSN Position Stand: Creatine Supplementation and Exercise (2017)
    - جرعة محافظة يومية: 3-5 جم لمعظم الناس (مش لازم تتحسب على الوزن أصلاً)
    - جرعة محسوبة أدق: تقريبًا 0.03 جم/كجم يوميًا
    - مرحلة تحميل اختيارية: 0.3 جم/كجم لمدة 5-7 أيام (مش ضرورية)
    """
    weight = _get(user_data, "weightKg", 70)
    calculated = round(weight * 0.03, 1)
    maintenance = min(max(calculated, 3), 5)
    loading = round(weight * 0.3)

    return {
        "maintenance_g": maintenance,
        "loading_g_per_day": loading,
    }


def calculate_caffeine(user_data):
    """
    الكافيين - الحد اليومي الآمن.
    المصدر: FDA / EFSA - حتى 400 مجم يوميًا للشخص البالغ السليم (تقريبًا 3-6 مجم/كجم)
    لو فيه ملاحظات طبية تخص القلب أو الحمل، بننزل الرقم وبننصح بمراجعة دكتور.
    (medicalNotes نص حر من المستخدم، فالبحث عن كلمات مفتاحية هنا هو التصميم الصح)
    """
    weight = _get(user_data, "weightKg", 70)
    medical_notes = _norm(_get(user_data, "medicalNotes", ""))

    safe_upper = min(round(weight * 6), 400)

    has_caution_flag = any(
        k in medical_notes for k in ["heart", "قلب", "pregnan", "حمل", "anxiety", "قلق", "ضغط"]
    )
    if has_caution_flag:
        safe_upper = min(safe_upper, 200)

    return {
        "safe_upper_mg": safe_upper,
        "capped_by_medical_notes": has_caution_flag,
    }


# ============================================================
# Formatters - تحويل الأرقام لرسالة عربية أو إنجليزية مفهومة
# ============================================================

def _format_calories(user_data, lang="ar"):
    tdee = _get(user_data, "tdee")
    target = _get(user_data, "dailyCalorieTarget")
    goal = _get(user_data, "dietGoal", "")

    if lang == "en":
        if not tdee and not target:
            return "I need more accurate weight/height/activity data to calculate your calories; please complete your health profile. 📋"
        lines = []
        if tdee:
            lines.append(f"⚡ Your estimated daily energy expenditure (TDEE): {round(tdee)} kcal")
        if target:
            lines.append(f"🎯 Your daily target based on your goal ({goal or 'maintaining weight'}): {round(target)} kcal")
        tips_text = "\n".join(lines)
        return (
            f"Sure 🔥 Here's your calorie breakdown:\n\n{tips_text}\n\n"
            f"💡 This number is an average; if you notice you're gaining or losing weight unexpectedly fast, let me know so we can adjust it."
        )

    if not tdee and not target:
        return "محتاج بيانات وزن/طول/نشاط أدق عشان أحسبلك السعرات، كمل بروفايلك الصحي كامل. 📋"

    lines = []
    if tdee:
        lines.append(f"⚡ معدل حرقك اليومي (TDEE) تقريبًا: {round(tdee)} سعرة")
    if target:
        lines.append(f"🎯 احتياجك اليومي المستهدف بناءً على هدفك ({goal or 'الحفاظ على الوزن'}): {round(target)} سعرة")

    tips_text = "\n".join(lines)
    return (
        f"تمام 🔥 دي حسبة السعرات بتاعتك:\n\n{tips_text}\n\n"
        f"💡 الرقم ده متوسط، لو حسيت إنك بتزود أو بتنزل بسرعة غير متوقعة كلمني نعدله."
    )


def _format_protein(user_data, lang="ar"):
    p = calculate_protein(user_data)
    low, high = p["range_per_kg"]

    if lang == "en":
        vegan_note = "\n\n🌱 We bumped the number up a bit since your diet is vegan, and plant protein absorbs less efficiently than animal protein." if p["vegan_adjusted"] else ""
        return (
            f"Great 💪 Your daily protein needs are roughly between {p['low']} and {p['high']} g "
            f"(about {p['target']} g on average), based on {low}-{high} g per kg of {p['basis_en']}."
            f"{vegan_note}\n\n"
            f"📚 This is based on International Society of Sports Nutrition (ISSN) recommendations.\n"
            f"⏰ Try to spread it across 3-4 meals with 20-40g of protein each so your body can use it best.\n"
            f"🍗 Best protein sources: chicken breast, red meat, eggs, cottage cheese, and Greek yogurt"
        )

    vegan_note = "\n\n🌱 زودنا الرقم شوية لأن نظامك نباتي (Vegan)، والبروتين النباتي جودته في الامتصاص أقل من الحيواني." if p["vegan_adjusted"] else ""
    return (
        f"تمام 💪 احتياجك اليومي من البروتين تقريبًا بين {p['low']} و {p['high']} جم "
        f"(يعني حوالي {p['target']} جم في المتوسط)، محسوبة على أساس {low}-{high} جم لكل كيلو من {p['basis']}."
        f"{vegan_note}\n\n"
        f"📚 ده معتمد على توصيات الجمعية الدولية لتغذية الرياضة (ISSN).\n"
        f"⏰ حاول توزعهم على 3-4 وجبات كل وحدة فيها 20-40 جم بروتين عشان الجسم يستفيد بيهم بشكل أفضل.\n"
        f"🍗 أفضل مصادر البروتين: صدور الفراخ، اللحوم الحمراء، البيض، الجبنة القريش، والزبادي اليوناني"
    )


def _format_fats(user_data, lang="ar"):
    f = calculate_fats(user_data)
    pct_low, pct_high = f["pct_range"]

    if lang == "en":
        return (
            f"Sure 🥑 Your daily healthy fat needs are roughly between {f['low']} and {f['high']} g "
            f"(about {int(pct_low*100)}%-{int(pct_high*100)}% of your daily calories, based on your diet type).\n\n"
            f"🎯 Focus on healthy fat sources like olive oil, avocado, nuts, and fatty fish, "
            f"and avoid trans fats (fried fast food and processed shortening) as much as possible.\n"
            f"🥑 Best healthy fat sources: olive oil, avocado, and nuts"
        )

    return (
        f"تمام 🥑 احتياجك اليومي من الدهون الصحية تقريبًا بين {f['low']} و {f['high']} جم "
        f"(حوالي {int(pct_low*100)}%-{int(pct_high*100)}% من سعراتك اليومية، بناءً على نظامك الغذائي).\n\n"
        f"🎯 ركز على مصادر الدهون الصحية زي زيت الزيتون، الأفوكادو، المكسرات، والأسماك الدهنية، "
        f"وابعد قدر الإمكان عن الدهون المتحولة (المقليات الجاهزة والسمن الصناعي).\n"
        f"🥑 أفضل مصادر الدهون الصحية: زيت الزيتون، الأفوكادو، والمكسرات"
    )


def _format_carbs(user_data, lang="ar"):
    p = calculate_protein(user_data)
    f = calculate_fats(user_data)
    c = calculate_carbs(user_data, p, f)
    low_gkg, high_gkg = c["activity_range_per_kg"]

    if lang == "en":
        paleo_note = "\n\n🥩 We lowered the number a bit since a Paleo diet doesn't rely on grains or legumes as a main carb source." if c["paleo_adjusted"] else ""
        return (
            f"Sure 🌾 Your daily carbohydrate needs are roughly between {c['low']} and {c['high']} g, "
            f"which covers your energy needs after accounting for protein and fat.\n\n"
            f"🏃 Based on your activity level, the general athletic range is around {low_gkg}-{high_gkg} g per kg of body weight."
            f"{paleo_note}\n\n"
            f"🎯 Prefer complex sources like oats, brown rice, potatoes, and starchy vegetables.\n"
            f"🌾 Best carb sources: oats, white rice, legumes, and whole wheat bread"
        )

    paleo_note = "\n\n🥩 خفّضنا الرقم شوية لأن نظام Paleo مبيعتمدش على الحبوب أو البقوليات كمصدر أساسي للكارب." if c["paleo_adjusted"] else ""
    return (
        f"تمام 🌾 احتياجك اليومي من الكاربوهيدرات تقريبًا بين {c['low']} و {c['high']} جم، "
        f"ده بيغطي احتياجك للطاقة بعد ما حسبنا البروتين والدهون.\n\n"
        f"🏃 بناءً على مستوى نشاطك، المعدل الرياضي العام بيكون في حدود {low_gkg}-{high_gkg} جم لكل كيلو من وزنك."
        f"{paleo_note}\n\n"
        f"🎯 فضّل المصادر المعقدة زي الشوفان، الأرز البني، البطاطا، والخضار النشوية.\n"
        f"🌾 أفضل مصادر الكارب: الشوفان، الأرز الأبيض، البقوليات، والخبز البلدي الأسمر"
    )


def _format_water(user_data, lang="ar"):
    w = calculate_water(user_data)

    if lang == "en":
        extra_note = ""
        if w["extra_for_activity_ml"]:
            extra_note = f" (we added {w['extra_for_activity_ml']} ml extra for your activity level)"
        return (
            f"Sure 💧 Your daily water needs are roughly {w['liters']} liters (about {w['ml']} ml){extra_note}.\n\n"
            f"🌡️ This value increases in hot weather or if you sweat a lot during training, and decreases slightly "
            f"if you eat a lot of vegetables and fruit (since they give you fluids without drinking)."
        )

    extra_note = ""
    if w["extra_for_activity_ml"]:
        extra_note = f" (زودنا {w['extra_for_activity_ml']} مل إضافية عشان مستوى نشاطك)"
    return (
        f"تمام 💧 احتياجك اليومي من المية تقريبًا {w['liters']} لتر (حوالي {w['ml']} مل){extra_note}.\n\n"
        f"🌡️ القيمة دي بتزيد في الجو الحر أو لو بتتعرق كتير في التمرين، وبتقل شوية لو بتاكل خضار وفاكهة كتير "
        f"(لأنها بتديك سوائل من غير ما تشرب)."
    )


def _format_fiber(user_data, lang="ar"):
    f = calculate_fiber(user_data)

    if lang == "en":
        return (
            f"Sure 🌿 Your daily fiber needs are roughly {f['target']} g.\n\n"
            f"🥦 Key sources: leafy greens, legumes (lentils, fava beans, chickpeas), oats, and unpeeled fruit.\n"
            f"✅ Fiber helps with fullness, digestive health, and blood sugar control."
        )

    return (
        f"تمام 🌿 احتياجك اليومي من الألياف تقريبًا {f['target']} جم.\n\n"
        f"🥦 أهم مصادرها: الخضار الورقي، البقوليات (عدس، فول، حمص)، الشوفان، والفواكه بقشرها.\n"
        f"✅ الألياف بتساعد في الشبع، وصحة الجهاز الهضمي، والتحكم في نسبة السكر في الدم."
    )


def _format_creatine(user_data, lang="ar"):
    c = calculate_creatine(user_data)

    if lang == "en":
        return (
            f"Sure ⚡ The recommended daily dose of creatine monohydrate is {c['maintenance_g']} g per day, "
            f"which stays roughly the same regardless of your weight (since the effective scientific dose saturates at a certain point).\n\n"
            f"🚀 If you want faster results, you can optionally do a loading phase at a higher dose (~{c['loading_g_per_day']} g) "
            f"split across the day for 5-7 days only, but it's never necessary and you can skip it and just take the regular dose from day one."
        )

    return (
        f"تمام ⚡ الجرعة اليومية الموصى بيها من الكرياتين مونوهيدرات: {c['maintenance_g']} جم يوميًا، "
        f"وده رقم ثابت تقريبًا معظم الوقت مهما كان وزنك (لأن الجرعة الفعالة علميًا بتتشبع عند حد معين).\n\n"
        f"🚀 لو حابب تستعجل النتيجة، ممكن تعمل مرحلة تحميل اختيارية بجرعة أعلى (~{c['loading_g_per_day']} جم) "
        f"مقسمة على اليوم لمدة 5-7 أيام بس، لكنها مش ضرورية أبدًا وممكن تستغنى عنها وتاخد الجرعة العادية على طول."
    )


def _format_caffeine(user_data, lang="ar"):
    c = calculate_caffeine(user_data)

    if lang == "en":
        caution = ""
        if c["capped_by_medical_notes"]:
            caution = "\n\n⚠️ We noticed you have medical notes that could interact with caffeine, so this number was calculated more cautiously - please check with your doctor."
        return (
            f"Sure ☕ Your safe daily upper limit for caffeine is roughly {c['safe_upper_mg']} mg "
            f"(about {round(c['safe_upper_mg']/95)} cups of coffee, assuming ~95 mg per cup).{caution}\n\n"
            f"🌙 Try to avoid caffeine within 6 hours of bedtime so it doesn't affect your sleep quality."
        )

    caution = ""
    if c["capped_by_medical_notes"]:
        caution = "\n\n⚠️ لاحظنا إن عندك ملاحظات طبية ممكن تتأثر بالكافيين، فالرقم ده اتحسب بحذر أكتر - يفضل تتأكد من دكتورك."
    return (
        f"تمام ☕ الحد الآمن يوميًا من الكافيين بالنسبالك تقريبًا {c['safe_upper_mg']} مجم "
        f"(يعني حوالي {round(c['safe_upper_mg']/95)} كوباية قهوة تقريبًا، بافتراض إن الكوباية فيها ~95 مجم).{caution}\n\n"
        f"🌙 حاول متاخدش كافيين قريب من موعد نومك بـ 6 ساعات عشان مايأثرش على جودة نومك."
    )


def _format_vitamins(user_data, lang="ar"):
    is_female = _gender(user_data) == GENDER_FEMALE

    if lang == "en":
        extra = "especially iron, vitamin D, and folic acid, which matter more for women." if is_female else "vitamin D and B12 matter especially if you're very active or your diet has restrictions."
        return (
            "Sure 💊 Vitamins are hard to calculate precisely without a blood test, but here are some general important points for you:\n\n"
            "☀️ Vitamin D: important for bones and hormones; most people are deficient, especially with low sun exposure.\n"
            "⚡ Vitamin B12: important for energy, often deficient in people who eat fully plant-based.\n"
            "🛡️ Vitamin C: important for immunity and recovery after training.\n\n"
            f"📌 {extra}\n\n"
            "🩸 If you want a precise number, it's best to get a full blood panel and review it with a doctor or dietitian."
        )

    extra = "خصوصًا الحديد وفيتامين د وحمض الفوليك، دول بيكونوا مهمين أكتر للستات." if is_female else "فيتامين د وB12 مهمين خصوصًا لو نشاطك عالي أو نظامك الغذائي فيه قيود."
    return (
        "تمام 💊 الفيتامينات صعب تتحسب برقم دقيق من غير تحليل دم، لكن في نقط عامة مهمة ليك:\n\n"
        "☀️ فيتامين D: مهم للعظام والهرمونات، وأغلب الناس عندها نقص فيه خصوصًا لو التعرض للشمس قليل.\n"
        "⚡ فيتامين B12: مهم للطاقة، وبيكون ناقص أكتر عند اللي بياكلوا نباتي بالكامل.\n"
        "🛡️ فيتامين C: مهم للمناعة والتعافي بعد التمرين.\n\n"
        f"📌 {extra}\n\n"
        "🩸 لو حابب رقم دقيق، الأفضل تعمل تحليل دم شامل وتشوف نتيجته مع دكتور أو أخصائي تغذية."
    )


_FORMATTERS = {
    "السعرات الحرارية": _format_calories,
    "البروتين": _format_protein,
    "الدهون الصحية": _format_fats,
    "الكارب": _format_carbs,
    "المياه": _format_water,
    "الألياف": _format_fiber,
    "الكرياتين": _format_creatine,
    "الكافيين": _format_caffeine,
    "الفيتامينات": _format_vitamins,
}


# ============================================================
# Handler
# ============================================================

def handle(user_input, entity, is_short_func, user_data=None, lang="ar"):
    """الـ handler الخاص بـ food_quantities - بيحسب بناءً على HealthProfileData بتاع اليوزر"""
    user_data = user_data or {}

    if lang == "en":
        if not entity:
            return "Which nutrient would you like me to calculate your needs for? 🧮"

        entity_en = ENTITY_EN.get(entity, entity)
        if is_short_func(user_input):
            return f"Do you want to know your daily {entity_en} needs? 🧮"

        formatter = _FORMATTERS.get(entity)
        if not formatter:
            return f"Sorry, data about {entity_en} isn't available yet 🙏"

        if entity not in ("الكافيين", "الفيتامينات") and not _has_user_data(user_data):
            return (
                f"To calculate your precise {entity_en} needs, I first need some health data about you 📋 "
                f"(weight, height, gender, activity level, and your goal). Could you complete your health profile and come back to me?"
            )

        return formatter(user_data, "en")

    if not entity:
        return "عايزني احسبلك احتياجك من عنصر ايه بالظبط؟ 🧮"

    if is_short_func(user_input):
        return f"هل عايز تعرف احتياجك من {entity} يوميا ؟ 🧮"

    formatter = _FORMATTERS.get(entity)
    if not formatter:
        return f"معلش، البيانات عن {entity} مش متوفرة عندي دلوقتي 🙏"

    # كافيين وفيتامينات مش محتاجين وزن بالضرورة، لكن باقي الحسابات محتاجة weightKg على الأقل
    if entity not in ("الكافيين", "الفيتامينات") and not _has_user_data(user_data):
        return (
            f"عشان أحسبلك احتياجك الدقيق من {entity} محتاج بيانات صحية عنك الأول 📋 "
            f"(الوزن، الطول، الجندر، مستوى النشاط، وهدفك)، تقدر تكمل بيانات البروفايل الصحي بتاعك وارجعلي؟"
        )

    return formatter(user_data, "ar")
