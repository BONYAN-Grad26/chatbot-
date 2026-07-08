# ============================================================
# injury_precautions.py
# ============================================================

INJURY_ENTITIES = {
    "الكتف": ["shoulder", "كتف", "الترقوة", "الهنج","الكتف","كتفي"],
    "الظهر": ["back", "ضهر", "قطنية", "عمود فقري","ظهري","الظهر"],
    "الركبة": ["knee", "ركبة", "صابونة","ركبتي","الركبة"],
    "المرفق": ["elbow", "كوع", "المرفق","كوعي","الكوع"],
    "ريست ايدك": ["wrist", "ريست", "معصم", "إيد","ايدي","ريست ايدي"],
    "الرقبة": ["neck", "رقبة", "العنق","رقبتي"],
    "الصدر": ["chest", "صدر", "البنش", "القفص الصدري","الصدر","صدري"],
    "القدم": ["foot", "انكل", "كاحل", "رجل", "مفصل القدم","قدمي","القدم","الرجل","رجلي"],
}

# أسماء أجزاء الجسم بالإنجليزي
BODY_PART_EN = {
    "الكتف": "shoulder",
    "الظهر": "back",
    "الركبة": "knee",
    "المرفق": "elbow",
    "ريست ايدك": "wrist",
    "الرقبة": "neck",
    "الصدر": "chest",
    "القدم": "foot/ankle",
}

def DESCRIPTION(entity="جزء معين", lang="ar"):
    if entity is None or entity == "":
        entity = "جزء معين" if lang != "en" else "a specific body part"
    if lang == "en":
        entity_en = BODY_PART_EN.get(entity, entity)
        return f"Want to know what to do if your {entity_en} hurts and how to avoid injuring it? 🩹"
    return f"عايز تعرف تعمل ايه لو {entity} وجعك وازاي تتفادى اصابته؟ 🩹"

INJURY_DATA = {

    "الركبة": {
        "risk_exercises": ["سكوات", "لانجز", "ليج بريس", "ليج اكستنشن", "ليج كيرل"],
        "risk_exercises_en": ["squat", "lunges", "leg press", "leg extension", "leg curl"],
        "common_mistakes": [
            "الركبة بتنهار للداخل في السكوات واللانجز",
            "نزول سريع بدون تحكم في الليج بريس",
            "قفل الركبة بالكامل في الليج اكستنشن",
            "تقدم الركبة كتير لقدام أصابع الرجل في السكوات",
            "زيادة الوزن بسرعة قبل ما الركبة تتعود"
        ],
        "common_mistakes_en": [
            "Knees caving inward during squats and lunges",
            "Lowering too fast without control on the leg press",
            "Fully locking the knee on leg extensions",
            "Letting the knee travel too far past the toes in squats",
            "Increasing weight too quickly before the knee adapts"
        ],
        "prevention": [
            "خلي الركبة في اتجاه أصابع الرجل دايماً",
            "انزل بتحكم وبطيء في أي تمرين للرجل",
            "متقفلش الركبة بالكامل في نهاية الحركة",
            "لو خفت الركبة للداخل، قلل الوزن فوراً"
        ],
        "prevention_en": [
            "Always keep your knee tracking in the direction of your toes",
            "Lower slowly and with control on any leg exercise",
            "Don't fully lock the knee at the end of the movement",
            "If the knee caves inward, reduce the weight immediately"
        ],
        "protection_tips": [
            "سخن الركبة بالمشي أو الدراجة 5-10 دقايق قبل التمرين",
            "قوّي عضلة الكواد والهامستر لأنهم بيحموا الركبة",
            "تمرين وول سيت مفيد لتقوية الركبة",
            "استخدم ركبية لو حاسس بعدم ثبات"
        ],
        "protection_tips_en": [
            "Warm up the knee with 5-10 minutes of walking or cycling before training",
            "Strengthen your quads and hamstrings, since they protect the knee",
            "Wall sits are useful for strengthening the knee",
            "Use a knee sleeve if you feel unstable"
        ],
        "first_aid": "وقف التمرين فوراً، تليج 15-20 دقيقة، ارفع الرجل لفوق، وابعد عن أي تمرين على الركبة لحين التحسن",
        "first_aid_en": "Stop training immediately, ice for 15-20 minutes, elevate the leg, and avoid any knee exercises until it improves",
        "warning_signs": [
            "صوت طق أو فرقعة مع ألم مفاجئ",
            "تورم واضح في الركبة",
            "عدم قدرة على تحمل الوزن على الرجل",
            "ألم مستمر بعد 48 ساعة من الراحة",
            "إحساس إن الركبة بتخذل أو بتتعوج"
        ],
        "warning_signs_en": [
            "A popping or cracking sound with sudden pain",
            "Visible swelling in the knee",
            "Inability to bear weight on the leg",
            "Persistent pain after 48 hours of rest",
            "A feeling that the knee is giving way or buckling"
        ]
    },

    "الكتف": {
        "risk_exercises": ["بنش بريس", "شولدر بريس", "لات بول داون خلف الراس", "دمبل فلاي بمدى واسع", "دايبس"],
        "risk_exercises_en": ["bench press", "shoulder press", "behind-the-neck lat pulldown", "wide-range dumbbell fly", "dips"],
        "common_mistakes": [
            "نزول الباربل للرقبة بدل الصدر في البنش",
            "الشولدر بريس بينزل تحت مستوى الأذن",
            "لات بول داون خلف الراس بيضغط على مفصل الكتف",
            "مدى حركة واسع جداً في الفلاي بيشد المفصل",
            "الكتف بيرتفع عن البنش وقت الضغط"
        ],
        "common_mistakes_en": [
            "Lowering the barbell to the neck instead of the chest on bench press",
            "Lowering the shoulder press below ear level",
            "Behind-the-neck lat pulldowns stressing the shoulder joint",
            "Too wide a range of motion on the fly, straining the joint",
            "Shoulders lifting off the bench during pressing"
        ],
        "prevention": [
            "البار ينزل لمنتصف الصدر مش الرقبة",
            "اللات بول داون للأمام دايماً مش لخلف الراس",
            "خلي انحناءة بسيطة في المرفق في الفلاي",
            "لوحي الكتف مقفولين ومنزلين طول تمارين الصدر",
            "متوسعش في مدى حركة الكتف أكتر من اللازم"
        ],
        "prevention_en": [
            "Lower the bar to the middle of the chest, not the neck",
            "Always pull the lat pulldown to the front, never behind the neck",
            "Keep a slight bend in the elbow during the fly",
            "Keep your shoulder blades locked back and down throughout chest exercises",
            "Don't overextend the shoulder's range of motion"
        ],
        "protection_tips": [
            "سخن الكتف بدوران بطيء للإيدين قبل التمرين",
            "فيس بول وريردلت فلاي مهمين لتوازن عضلات الكتف",
            "متهملش الكتف الخلفي في التدريب",
            "تمارين الدوران الخارجي للكتف بمقاومة خفيفة كإحماء"
        ],
        "protection_tips_en": [
            "Warm up the shoulder with slow arm circles before training",
            "Face pulls and rear delt flys are important for balanced shoulder muscles",
            "Don't neglect the rear deltoid in your training",
            "Light-resistance external rotation exercises as a warm-up"
        ],
        "first_aid": "وقف التمرين فوراً، تليج 15-20 دقيقة، ابعد عن أي رفع للإيد فوق مستوى الكتف لحين التحسن",
        "first_aid_en": "Stop training immediately, ice for 15-20 minutes, avoid raising your arm above shoulder level until it improves",
        "warning_signs": [
            "ألم حاد أثناء الرفع أو أول ما ترفع إيدك",
            "إحساس بضعف مفاجئ في الإيد",
            "تورم أو كدمة في منطقة الكتف",
            "ألم بيصحّيك من النوم",
            "إحساس بخدر أو تنميل في الإيد"
        ],
        "warning_signs_en": [
            "Sharp pain while lifting or as soon as you raise your arm",
            "Sudden weakness in the arm",
            "Swelling or bruising around the shoulder",
            "Pain that wakes you up from sleep",
            "Numbness or tingling in the arm"
        ]
    },

    "الظهر": {
        "risk_exercises": ["ديدليفت", "باربل رو", "هايبر اكستنشن", "سكوات", "شولدر بريس بوزن ثقيل"],
        "risk_exercises_en": ["deadlift", "barbell row", "hyperextension", "squat", "heavy shoulder press"],
        "common_mistakes": [
            "انحناء الضهر في الديدليفت أو السكوات",
            "استخدام الضهر كله في السحب بدل ما يكون ثابت",
            "هايبر اكستنشن فوق مستوى خط الجسم",
            "زيادة الوزن بسرعة قبل إتقان الفورم",
            "تقوس القطنية للخلف في الشولدر بريس"
        ],
        "common_mistakes_en": [
            "Rounding the back during deadlifts or squats",
            "Using the whole back to pull instead of keeping it fixed",
            "Hyperextending above the straight body line",
            "Increasing weight too fast before mastering the form",
            "Arching the lower back excessively during shoulder press"
        ],
        "prevention": [
            "ضهرك مستقيم دايماً في أي تمرين، خصوصاً الديدليفت",
            "شد البطن قبل ما تبدأ أي حركة ثقيلة",
            "البار يفضل قريب من جسمك في الديدليفت",
            "متهزش الجذع في تمارين السحب",
            "ابدأ بوزن خفيف وركز على الفورم الأول"
        ],
        "prevention_en": [
            "Always keep your back straight in any exercise, especially the deadlift",
            "Brace your core before starting any heavy movement",
            "Keep the bar close to your body during the deadlift",
            "Don't swing your torso during pulling exercises",
            "Start with a light weight and focus on form first"
        ],
        "protection_tips": [
            "قوّي عضلات الكور بتمارين البلانك والديد باج",
            "سخن الضهر بحركات Cat-Cow قبل التمرين",
            "هايبر اكستنشن بوزن خفيف كإحماء للضهر قبل الديدليفت",
            "استخدم حزام ظهر بس في الأوزان الثقيلة جداً"
        ],
        "protection_tips_en": [
            "Strengthen your core with planks and dead bugs",
            "Warm up your back with cat-cow movements before training",
            "Light hyperextensions as a back warm-up before deadlifts",
            "Use a lifting belt only for very heavy weights"
        ],
        "first_aid": "توقف فوراً ومتحاولش تكمل، ارتاح في وضع مريح، تليج للمنطقة المؤلمة، ومتحملش أي ثقل لحين التحسن",
        "first_aid_en": "Stop immediately and don't try to continue, rest in a comfortable position, ice the painful area, and avoid carrying any weight until it improves",
        "warning_signs": [
            "ألم حاد مفاجئ في القطنية أثناء التمرين",
            "ألم بيتشعع للرجل أو الإيد (علامة ضغط على عصب)",
            "تنميل أو خدر في الأرجل",
            "ضعف في الأرجل مع الألم",
            "ألم مستمر أكتر من أسبوع مع الراحة"
        ],
        "warning_signs_en": [
            "Sudden sharp pain in the lower back during training",
            "Pain radiating to the leg or arm (a sign of nerve pressure)",
            "Numbness or tingling in the legs",
            "Leg weakness accompanying the pain",
            "Pain persisting more than a week despite rest"
        ]
    },

    "المرفق": {
        "risk_exercises": ["تراي بوش داون", "باي كيرل", "هامر كيرل", "اوفرهيد تراي اكستنشن", "ديدليفت", "باربل رو"],
        "risk_exercises_en": ["tricep pushdown", "bicep curl", "hammer curl", "overhead tricep extension", "deadlift", "barbell row"],
        "common_mistakes": [
            "قفل المرفق بقوة في نهاية تمارين التراي",
            "وزن ثقيل جداً في الباي بيخلي المرفق يتحرك",
            "سرعة عالية في التمرين بتضغط على المفصل",
            "مدى حركة واسع جداً في الاوفرهيد تراي اكستنشن"
        ],
        "common_mistakes_en": [
            "Forcefully locking the elbow at the end of tricep exercises",
            "Weight too heavy on curls, causing the elbow to shift",
            "Moving too fast, which stresses the joint",
            "Too wide a range of motion on overhead tricep extensions"
        ],
        "prevention": [
            "متقفلش المرفق بقوة في نهاية أي تمرين",
            "المرفق ثابت جنب الجسم في تمارين الباي",
            "حركة بطيئة ومتحكم فيها بدل الزخم",
            "ابدأ بوزن خفيف في تمارين الذراع"
        ],
        "prevention_en": [
            "Don't forcefully lock the elbow at the end of any exercise",
            "Keep the elbow fixed at your side during curls",
            "Use slow, controlled movement instead of momentum",
            "Start with light weight in arm exercises"
        ],
        "protection_tips": [
            "سخن المرفق بدوران خفيف وفرد بطيء قبل التمرين",
            "تمارين الساعد بتقوي المنطقة حوالين المرفق",
            "استخدم مرفقية لو حاسس بعدم ارتياح"
        ],
        "protection_tips_en": [
            "Warm up the elbow with light rotations and slow extensions before training",
            "Forearm exercises strengthen the area around the elbow",
            "Use an elbow sleeve if you feel discomfort"
        ],
        "first_aid": "وقف التمرين، تليج 15 دقيقة، ابعد عن أي تمرين للذراع، وارتاح الإيد في وضع مرفوع",
        "first_aid_en": "Stop training, ice for 15 minutes, avoid any arm exercises, and rest the arm in an elevated position",
        "warning_signs": [
            "ألم على الجانب الخارجي أو الداخلي للكوع",
            "تورم واضح في المرفق",
            "عدم قدرة على مد الإيد بالكامل",
            "ألم مستمر حتى في الراحة",
            "تنميل في الأصابع"
        ],
        "warning_signs_en": [
            "Pain on the outer or inner side of the elbow",
            "Visible swelling in the elbow",
            "Inability to fully extend the arm",
            "Persistent pain even at rest",
            "Tingling in the fingers"
        ]
    },

    "ريست ايدك": {
        "risk_exercises": ["باربل كيرل", "باربل بنش بريس", "باربل رو", "بوش أب", "دمبل كيرل"],
        "risk_exercises_en": ["barbell curl", "barbell bench press", "barbell row", "push-up", "dumbbell curl"],
        "common_mistakes": [
            "ثني المعصم للخلف وقت البنش أو البوش أب",
            "قبضة ضعيفة على البار بيخلي المعصم يتلوى",
            "وزن ثقيل جداً على المعصم قبل ما يتقوى",
            "سرعة في الحركة بتضغط على المفصل"
        ],
        "common_mistakes_en": [
            "Bending the wrist backward during bench press or push-ups",
            "A weak grip on the bar, letting the wrist twist",
            "Weight too heavy on the wrist before it's strong enough",
            "Moving too fast, which stresses the joint"
        ],
        "prevention": [
            "خلي المعصم في خط مستقيم مع الساعد طول الحركة",
            "قبضة قوية ومحكمة على البار أو الدمبل",
            "استخدم ربطة معصم في الأوزان الثقيلة"
        ],
        "prevention_en": [
            "Keep the wrist in a straight line with your forearm throughout the movement",
            "Use a firm, tight grip on the bar or dumbbell",
            "Use a wrist wrap for heavy weights"
        ],
        "protection_tips": [
            "تمارين تدوير المعصم الخفيفة كإحماء قبل التمرين",
            "تمارين تقوية الساعد بتحمي المعصم",
            "استخدم ربطات المعصم في الديدليفت والسكوات الثقيل"
        ],
        "protection_tips_en": [
            "Light wrist rotation exercises as a warm-up before training",
            "Forearm-strengthening exercises protect the wrist",
            "Use wrist wraps for heavy deadlifts and squats"
        ],
        "first_aid": "وقف التمرين، تليج، ثبت المعصم بضمادة خفيفة، وابعد عن أي ضغط عليه",
        "first_aid_en": "Stop training, ice the area, stabilize the wrist with a light wrap, and avoid putting any pressure on it",
        "warning_signs": [
            "ألم حاد في المعصم أثناء الإمساك بالأوزان",
            "تورم أو كدمة",
            "إحساس بضعف في القبضة",
            "ألم مستمر في الراحة",
            "تنميل في الأصابع"
        ],
        "warning_signs_en": [
            "Sharp wrist pain while gripping weights",
            "Swelling or bruising",
            "A feeling of weakness in the grip",
            "Persistent pain at rest",
            "Tingling in the fingers"
        ]
    },

    "الرقبة": {
        "risk_exercises": ["لات بول داون خلف الراس", "بنش بريس بدون تثبيت الراس", "شولدر شراجز بوزن ثقيل", "سيتاب بشد الراس باليد"],
        "risk_exercises_en": ["behind-the-neck lat pulldown", "bench press without head support", "heavy shoulder shrugs", "sit-ups pulling the head with your hands"],
        "common_mistakes": [
            "لات بول داون خلف الراس بيضغط على فقرات الرقبة",
            "شد الراس باليدين في تمارين البطن",
            "تحريك الراس وقت البنش أو الضغط",
            "حمل أكياس تقيلة على كتف واحدة"
        ],
        "common_mistakes_en": [
            "Behind-the-neck lat pulldowns stressing the neck vertebrae",
            "Pulling the head with your hands during ab exercises",
            "Moving your head during bench press or pressing movements",
            "Carrying heavy bags on one shoulder"
        ],
        "prevention": [
            "اللات بول داون للأمام دايماً مش لخلف الراس",
            "في تمارين البطن إيدك وراء الراس بس متشدهاش",
            "الراس في خط مستقيم مع الضهر طول التمرين"
        ],
        "prevention_en": [
            "Always pull the lat pulldown to the front, never behind the neck",
            "In ab exercises, keep your hands behind your head but don't pull it",
            "Keep your head in a straight line with your back throughout the exercise"
        ],
        "protection_tips": [
            "تمارين تمديد الرقبة الخفيفة كإحماء قبل التمرين",
            "تمارين تقوية عضلات الرقبة بتقلل الضغط على الفقرات",
            "سادة النوم المناسبة مهمة للراحة بعد التمرين"
        ],
        "protection_tips_en": [
            "Light neck stretches as a warm-up before training",
            "Neck-strengthening exercises reduce pressure on the vertebrae",
            "A proper pillow matters for recovery after training"
        ],
        "first_aid": "وقف التمرين فوراً، راحة تامة، تليج، ومتدورش بالراس بسرعة",
        "first_aid_en": "Stop training immediately, rest completely, ice the area, and avoid turning your head quickly",
        "warning_signs": [
            "ألم بيتشعع من الرقبة للإيد أو الكتف",
            "تنميل أو خدر في الإيدين أو الأصابع",
            "دوخة أو صداع مع ألم الرقبة",
            "ضعف مفاجئ في الإيد",
            "ألم شديد بيمنع حركة الراس"
        ],
        "warning_signs_en": [
            "Pain radiating from the neck to the arm or shoulder",
            "Numbness or tingling in the hands or fingers",
            "Dizziness or headache along with neck pain",
            "Sudden weakness in the arm",
            "Severe pain that prevents head movement"
        ]
    },

    "الصدر": {
        "risk_exercises": ["بنش بريس", "دمبل فلاي", "دايبس", "كيبل كروس اوفر"],
        "risk_exercises_en": ["bench press", "dumbbell fly", "dips", "cable crossover"],
        "common_mistakes": [
            "نزول الدمبل تحت مستوى الكتف في الفلاي",
            "مدى حركة واسع جداً في الكيبل فلاي",
            "الكتف بيرتفع عن البنش وقت الضغط",
            "المرفق بزاوية 90 درجة للخارج في البنش"
        ],
        "common_mistakes_en": [
            "Lowering the dumbbells below shoulder level during the fly",
            "Too wide a range of motion in the cable fly",
            "Shoulders lifting off the bench during pressing",
            "Elbows flared to 90 degrees during the bench press"
        ],
        "prevention": [
            "الدمبل متنزلش تحت مستوى الكتف في الفلاي",
            "مدى حركة معقول ومتحكم فيه",
            "لوحي الكتف منزلين ومقفولين طول التمرين",
            "المرفق بزاوية 45-75 درجة مش 90 في البنش"
        ],
        "prevention_en": [
            "Don't lower the dumbbells below shoulder level in the fly",
            "Use a reasonable, controlled range of motion",
            "Keep your shoulder blades locked down throughout the exercise",
            "Keep your elbows at 45-75 degrees, not 90, during the bench press"
        ],
        "protection_tips": [
            "سخن الكتف والصدر بحركات دائرية خفيفة قبل التمرين",
            "ابدأ بوزن خفيف وزود تدريجي",
            "توازن التدريب بين الصدر والظهر مهم لصحة الكتف"
        ],
        "protection_tips_en": [
            "Warm up your shoulders and chest with light circular movements before training",
            "Start with a light weight and increase gradually",
            "Balancing chest and back training matters for shoulder health"
        ],
        "first_aid": "وقف التمرين، راحة، تليج لو في ورم، وابعد عن أي ضغط على الصدر أو الكتف",
        "first_aid_en": "Stop training, rest, ice if there's swelling, and avoid any pressure on the chest or shoulder",
        "warning_signs": [
            "ألم حاد مفاجئ في الصدر أثناء التمرين",
            "إحساس بشد أو تمزق في الصدر",
            "ألم بيتشعع للكتف أو الإيد",
            "تورم في منطقة الصدر أو الكتف",
            "أي ألم في الصدر مع ضيق تنفس اتصل بالإسعاف فوراً"
        ],
        "warning_signs_en": [
            "Sudden sharp chest pain during training",
            "A feeling of pulling or tearing in the chest",
            "Pain radiating to the shoulder or arm",
            "Swelling around the chest or shoulder",
            "Any chest pain with shortness of breath: call emergency services immediately"
        ]
    },

    "القدم": {
        "risk_exercises": ["سكوات", "لانجز", "كالف ريز", "ليج بريس", "جري أو ركض مفرط"],
        "risk_exercises_en": ["squat", "lunges", "calf raise", "leg press", "excessive running"],
        "common_mistakes": [
            "الكعب بيرتفع عن الأرض في السكوات",
            "الوقوف على أصابع الرجل بدل القدم كلها في الكالف ريز",
            "القدم بتتحول للخارج أو الداخل بشكل مبالغ",
            "جزمة رياضية مش مناسبة للتمرين"
        ],
        "common_mistakes_en": [
            "Heels lifting off the floor during squats",
            "Standing on your toes instead of your whole foot on calf raises",
            "The foot rotating excessively inward or outward",
            "Wearing shoes that aren't suitable for training"
        ],
        "prevention": [
            "القدم كلها ثابتة على الأرض في السكوات",
            "الكالف ريز بنزول كامل وارتفاع كامل",
            "خلي القدم في اتجاه الركبة طول الوقت",
            "استخدم جزمة رياضية مناسبة وداعمة"
        ],
        "prevention_en": [
            "Keep your whole foot planted on the floor during squats",
            "Use a full range of motion, down and up, on calf raises",
            "Keep your foot pointing in the direction of your knee at all times",
            "Use proper, supportive training shoes"
        ],
        "protection_tips": [
            "تمارين تدوير الكاحل كإحماء قبل تمارين الرجل",
            "تمارين توازن (Single leg stand) بتقوي الكاحل",
            "استخدم تيب أو كاحلية لو عندك كاحل ضعيف"
        ],
        "protection_tips_en": [
            "Ankle rotation exercises as a warm-up before leg training",
            "Balance exercises (single-leg stand) strengthen the ankle",
            "Use tape or an ankle brace if you have a weak ankle"
        ],
        "first_aid": "وقف التمرين، رفع الرجل لفوق، تليج، وابعد عن الوقوف عليها فترة",
        "first_aid_en": "Stop training, elevate the leg, ice it, and avoid standing on it for a while",
        "warning_signs": [
            "ألم حاد في الكاحل مع لي أو انزلاق",
            "تورم سريع في القدم أو الكاحل",
            "عدم قدرة على تحمل الوزن على الرجل",
            "كدمة واضحة تحت الجلد",
            "ألم مستمر في الكعب قد يكون التهاب لفافة أخمصية"
        ],
        "warning_signs_en": [
            "Sharp ankle pain following a twist or slip",
            "Rapid swelling in the foot or ankle",
            "Inability to bear weight on the leg",
            "Visible bruising under the skin",
            "Persistent heel pain, which could be plantar fasciitis"
        ]
    },
}

def handle(user_input, entity, is_short_func, user_data={}, lang="ar"):
    if lang == "en":
        if not entity:
            return "Where exactly do you have pain or an injury? 🩹"
        entity_en = BODY_PART_EN.get(entity, entity)
        if is_short_func(user_input):
            return f"Do you have an issue with your {entity_en}? 🩹"

        data = INJURY_DATA.get(entity)
        if not data:
            return f"Sorry, I don't have data on the {entity_en} yet 🙏"

        risk = ", ".join(data["risk_exercises_en"])
        mistakes = "\n".join(f"❌ {m}" for m in data["common_mistakes_en"])
        prevention = "\n".join(f"✅ {p}" for p in data["prevention_en"])
        tips = "\n".join(f"🛡️ {t}" for t in data["protection_tips_en"])
        warnings = "\n".join(f"🚨 {w}" for w in data["warning_signs_en"])

        return (
            f"Sure 🩹 Here are the exercises that need extra care to protect your {entity_en}:\n"
            f"⚠️ {risk}\n\n"
            f"Some common mistakes:\n{mistakes}\n\n"
            f"How to correct and avoid them:\n{prevention}\n\n"
            f"Protection tips:\n{tips}\n\n"
            f"🚑 First thing to do if it happens:\n{data['first_aid_en']}\n\n"
            f"Warning signs to see a doctor right away:\n{warnings}"
        )

    if not entity:
        return "عندك ألم أو إصابة فين بالظبط؟ 🩹"
    if is_short_func(user_input):
        return f"هل عندك مشكلة في {entity}؟ 🩹"

    data = INJURY_DATA.get(entity)
    if not data:
        return f"معلش، البيانات عن {entity} مش متوفرة عندي دلوقتي 🙏"

    risk = "، ".join(data["risk_exercises"])
    mistakes = "\n".join(f"❌ {m}" for m in data["common_mistakes"])
    prevention = "\n".join(f"✅ {p}" for p in data["prevention"])
    tips = "\n".join(f"🛡️ {t}" for t in data["protection_tips"])
    warnings = "\n".join(f"🚨 {w}" for w in data["warning_signs"])

    return (
        f"تمام 🩹 دي التمارين اللي محتاج تاخد بالك منها عشان تحمي {entity}:\n"
        f"⚠️ {risk}\n\n"
        f"دي بعض الأخطاء الشائعة:\n{mistakes}\n\n"
        f"طريقة التصحيح والتفادي:\n{prevention}\n\n"
        f"نصايح للحماية:\n{tips}\n\n"
        f"🚑 أول حاجة تعملها لو حصل إيه:\n{data['first_aid']}\n\n"
        f"العلامات اللي تروح فيها للدكتور فورًا:\n{warnings}"
    )
