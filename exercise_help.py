# ============================================================
# exercise_help.py
# كل حاجة خاصة بتصنيف exercise_help
# ============================================================

# الكيوردز ومرادفاتها لكل تمرين
EXERCISE_ENTITIES = {
    "chest_press": ["chest press", "شيست بريس", "دفع للصدر"],
    "inclined_bench_press": ["inclined bench press", "بنش عالي", "بار عالي"],
    "flat_bench_press": ["straight bench press","flat bench press","بنش مستوي", "بار مستوي", "دكة مستوية"],
    "decline_bench_press": ["decline bench press", "بنش مقلوب", "ضغط مقلوب"],
    "chest_fly": ["chest fly", "شيست فلاي", "تفتيح فراشة", "butterfly"],
    "cable_fly": ["cable fly", "كيبل فلاي", "تفتيح كيبل", "تقفيل كيبل", "كروس اوفر"],
    "push_ups": ["push ups", "ضغط"],
    "dips": ["dips", "المتوازي"],
    "shoulder_press": ["shoulder press", "شولدر بريس", "تجميع كتف"],
    "front_raise": ["front raise", "فرونت ريز", "رفرفة امامي", "امامي دمبل"],
    "lateral_raise": ["lateral raise", "لاتيرال ريز", "رفرفة جانبي", "جانبي دمبل"],
    "cable_lateral_raise": ["cable lateral raise", "رفرفة جانبي كيبل", "جانبي كيبل"],
    "rear_delt_fly": ["rear delt fly", "فراشة مقلوب", "كتف خلفي عالجهاز", "رفرفة خلفي"],
    "face_pull": ["face pull", "فيس بول", "سحب للوجه", "خلفي بالكيبل"],
    "shrugs": ["shrugs", "شراجز", "ترابيس", "هز كتاف"],
    "lat_pulldown": ["lat pulldown", "lat pull down", "لات بول داون", "سحب عالي", "سحب امامي"],
    "pull_ups": ["pull ups", "عقلة"],
    "barbell_row": ["barbell row", "باربل رو", "سحب بالبار", "مجنص بالبار"],
    "dumbbell_row": ["dumbbell row", "دمبل رو", "منشار", "سحب دمبل"],
    "cable_row": ["cable row", "كيبل رو", "سحب ارضي"],
    "deadlift": ["deadlift", "ديدليفت", "الرفعة المميتة"],
    "hyperextension": ["hyperextension", "هايبر اكستنشن", "قطنية"],
    "t_bar_row": ["t bar row", "تي بار"],
    "squat": ["squat", "سكوات", "قرفصاء"],
    "lunges": ["lunges", "لانجز", "طعن"],
    "leg_extension": ["leg extension", "ليج اكستنشن", "رفرفة رجل امامي", "تمديد الساقين"],
    "leg_curls": ["leg curl", "ليج كيرل", "رفرفة رجل خلفي", "خلفي نايم", "خلفي قاعد"],
    "leg_press": ["leg press", "ليج بريس", "دفع رجل", "مكبس"],
    "calf_raise": ["calf raise", "سمانة", "رفع الكعبين"],
    "hip_abductor": ["hip abductor", "هيب ابدكتور", "فتح رجل", "جوانب"],
    "hip_adductor": ["hip adductor", "هيب ادكتور", "ضامة", "قفل رجل"],
    "glute_bridge": ["glute bridge", "جلوت بريدج", "الكوبري", "رفع الحوض"],
    "bicep_curl": ["bicep curl", "بايسيبس كيرل", "تبادل دمبل", "باي بالبار"],
    "hammer_curl": ["hammer curl", "شاكوش", "تبادل شاكوش"],
    "tricep_pushdown": ["tricep pushdown", "ترايسبس بوش داون", "تراي حبل", "تراي مسطرة"],
    "overhead_tricep_extension": ["overhead tricep extension", "تراي فرنسي", "تراي خلف الرأس"],
    "abdominal": ["abs", "abdominal", "بطن", "معدة", "crunches"],
    "plank": ["plank", "بلانك", "ثبات"],
}

# وصف التصنيف - بيتستخدم لما الموديل يبقى محتار بين كلاسين
def DESCRIPTION(entity="أي تمرين", lang="ar"):
    if entity is None or entity == "":
        entity = "أي تمرين" if lang != "en" else "any exercise"
    if lang == "en":
        return f"Want me to help you with {entity} or send you a video about it? 🏋️"
    return f"عايزني أساعدك في {entity} أو ابعتلك فيديو عنه؟ 🏋️"

# بيانات كل تمرين - فيديو ونصايح (عربي وانجليزي)
EXERCISE_DATA = {
    "chest_press": {
        "arabic_video": "https://youtu.be/cJodjVmHgnM?si=IVRJr4GGn0M96Fj4",
        "english_video": "https://youtu.be/n8TOta_pfr4?si=cXUyam0cVpNbNYEY",
        "tips": [
            "اضبط الكرسي بحيث يكون المقبض بمستوى منتصف الصدر تماماً.",
            "افرد كوعك للأمام دون قفل المفصل تماماً في النهاية لحماية المفاصل.",
            "حافظ على ثبات لوحي الكتف للخلف وأسفل ملتصقين بالمسند أثناء الدفع."
        ],
        "tips_en": [
            "Set the seat so the handle sits exactly at mid-chest level.",
            "Extend your elbows forward without fully locking them at the end to protect the joint.",
            "Keep your shoulder blades pulled back and down against the pad throughout the press."
        ]
    },
    "inclined_bench_press": {
        "arabic_video": "https://youtu.be/n9s59oBECdM?si=3tCFQIAGVUJbaR6G",
        "english_video": "https://youtu.be/IP4oeKh1Sd4?si=eJ9ZVMd3L1bt1Pko",
        "tips": [
            "اضبط زاوية الدكة بين 30 إلى 45 درجة للتركيز بدقة على الصدر العلوي.",
            "انزل بالبار ببطء وتحكم حتى يلمس أعلى الصدر ثم ادفع بقوة.",
            "حافظ على تثبيت رجليك بقوة في الأرض لزيادة ثبات وجاذبية الجسم."
        ],
        "tips_en": [
            "Set the bench angle between 30-45 degrees to target the upper chest precisely.",
            "Lower the bar slowly and with control until it touches the upper chest, then press up powerfully.",
            "Keep your feet planted firmly on the floor for better stability and drive."
        ]
    },
    "flat_bench_press": {
        "arabic_video": "https://youtu.be/rGAd-6kaepo?si=uFH5qVakA9-s_iZO",
        "english_video": "https://youtu.be/lAMfO-Yrf_I?si=E1nJva_KzBJ9AFQk",
        "tips": [
            "حافظ على تقوس خفيف وطبيعي في أسفل الظهر مع تثبيت المقعدة على الدكة.",
            "انزل بالبار ببطء حتى يلمس منتصف الصدر (خط الحلمات).",
            "لا تفتح كوعك للخارج بزاوية 90 بل ضمه للداخل قليلاً لحماية مفصل الكتف."
        ],
        "tips_en": [
            "Keep a slight, natural arch in your lower back with your glutes on the bench.",
            "Lower the bar slowly until it touches the middle of your chest (nipple line).",
            "Don't flare your elbows to 90 degrees; tuck them in slightly to protect the shoulder joint."
        ]
    },
    "decline_bench_press": {
        "arabic_video": "https://youtu.be/A2mxX8hyFsk?si=_nGZ0QB1XwVwMIGk",
        "english_video": "https://youtu.be/LfyQBUKR8SE?si=JQ_XeUCdIejYyZXJ",
        "tips": [
            "تأكد من تثبيت قدميك جيداً في مسند الدكة لحماية توازن الجسم وأسفل الظهر.",
            "انزل بالبار باتجاه أسفل الصدر ببطء وتحكم كامل.",
            "ادفع الوزن لأعلى بشكل مستقيم مع التركيز على عصر عضلات الصدر السفلية."
        ],
        "tips_en": [
            "Lock your feet securely under the bench pads to protect your balance and lower back.",
            "Lower the bar toward the bottom of your chest slowly with full control.",
            "Press the weight straight up while focusing on squeezing your lower chest."
        ]
    },
    "chest_fly": {
        "arabic_video": "https://youtu.be/40HCXxMKQ_U?si=7L1iM8_Yf8L9aqRK",
        "english_video": "https://youtu.be/H4mVGHaK2f4?si=bVNeeLA7lmn478wa",
        "tips": [
            "ثبت ظهرك وكتفيك على المقعد طوال التمرين للحفاظ على العزل الصحيح للصدر.",
            "افتح الذراعين ببطء حتى تشعر بإطالة مريحة في عضلات الصدر دون المبالغة في المدى الحركي.",
            "اضغط بالذراعين نحو المنتصف مع عصر عضلات الصدر في نهاية الحركة ثم عد ببطء إلى وضع البداية."
        ],
        "tips_en": [
            "Keep your back and shoulders fixed on the bench throughout for proper chest isolation.",
            "Open your arms slowly until you feel a comfortable stretch in your chest, without overextending the range.",
            "Bring your arms toward the middle, squeezing your chest at the end, then return slowly to the start."
        ]
    },
    "cable_fly": {
        "arabic_video": "https://youtu.be/q_L957m2JxI?si=NUn4-_K20J13Syqz",
        "english_video": "https://youtu.be/8Um35Es-ROE?si=6WlpufbxCoRp5FKo",
        "tips": [
            "خذ خطوة للأمام لضمان وجود مقاومة وشد مستمر من الكابل طوال الحركة.",
            "حافظ على ثبات جذعك وميل خفيف للأمام دون أرجحة الجسد لتوليد القوة.",
            "اعصر الصدر في نهاية الحركة وتخيل أنك تحاول ضم كوعيك لبعضهما وليس يديك فقط."
        ],
        "tips_en": [
            "Step forward to keep constant tension and resistance from the cable throughout the movement.",
            "Keep your torso stable with a slight forward lean, without swinging your body to generate force.",
            "Squeeze your chest at the end, imagining you're bringing your elbows together, not just your hands."
        ]
    },
    "push_ups": {
        "arabic_video": "https://youtu.be/Z_eNt20UaVY?si=F2hmitfLjLD-JFQe",
        "english_video": "https://youtu.be/F0mFvxZelaE?si=bTyAfEAAeuiaLnO_",
        "tips": [
            "حافظ على استقامة جسمك كخط واحد من الرأس إلى الكعبين بدون سقوط الحوض.",
            "ضع يديك باتساع أكبر قليلاً من كتفيك والكوع يميل للخلف بزاوية 45 درجة.",
            "انزل ببطء حتى يقترب صدرك من الأرض ثم ادفع بكامل قوتك لأعلى."
        ],
        "tips_en": [
            "Keep your body in one straight line from head to heels, without letting your hips sag.",
            "Place your hands slightly wider than your shoulders with elbows angled back at 45 degrees.",
            "Lower slowly until your chest is close to the floor, then push up with full force."
        ]
    },
    "dips": {
        "arabic_video": "https://youtu.be/ibPHHrANJRg?si=1rg10thlz1Q2z5BO",
        "english_video": "https://youtu.be/2z8JmcrW-As?si=2fMO8WuQTbmsXlgN",
        "tips": [
            "مل بجذعك للأمام قليلاً للتركيز على الصدر، أو حافظ على استقامتك للترايسبس.",
            "انزل حتى يصبح كوعك بزاوية 90 درجة ولا تبالغ في النزول لحماية مفصل الكتف.",
            "ادفع ببطء وتحكم كامل دون الاعتماد على الاندفاع أو الأرجحة."
        ],
        "tips_en": [
            "Lean your torso forward slightly to target the chest, or stay upright to target the triceps.",
            "Lower until your elbow is around 90 degrees; don't go too deep, to protect the shoulder joint.",
            "Press up slowly with full control rather than relying on momentum or swinging."
        ]
    },
    "shoulder_press": {
        "arabic_video": "https://youtu.be/GEsvaoL-M7Q?si=9o3T7RWpW8tDm3up",
        "english_video": "https://youtu.be/0JfYxMRsUCQ?si=KvXKMF-6DoSnOroj",
        "tips": [
            "اضبط مسند الدكة بزاوية أقل من 90 درجة بقليل (حوالي 80) لراحة أسفل الظهر.",
            "انزل بالوزن حتى يصبح الدمبل بمستوى أذنك أو أسفل ذقنك بقليل لمدى حركي كامل.",
            "ادفع الوزن لأعلى بشكل مستقيم دون قفل الكوعين تماماً في النهاية."
        ],
        "tips_en": [
            "Set the backrest slightly under 90 degrees (around 80) for lower back comfort.",
            "Lower the weight until the dumbbell is level with your ear or slightly below your chin for a full range.",
            "Press the weight straight up without fully locking your elbows at the top."
        ]
    },
    "front_raise": {
        "arabic_video": "https://youtu.be/FFg4UGsB1iI?si=Kb9O68LT6YsUIpJd",
        "english_video": "https://youtu.be/ugPIPY7j-GM?si=BnGE2v7jYDHDfOOa",
        "tips": [
            "ارفع الوزن بمستوى كتفك أو أعلى بقليل ولا تتأرجح بجسدك لتوليد العزم.",
            "حافظ على انحناءة بسيطة جداً وغير متغيرة في كوعك طوال الحركة.",
            "تحكم في الوزن أثناء النزول ولا تدعه يسقط بسرعة بفعل الجاذبية."
        ],
        "tips_en": [
            "Raise the weight to shoulder level or slightly above, without swinging your body for momentum.",
            "Keep a small, unchanging bend in your elbow throughout the movement.",
            "Control the weight on the way down instead of letting it drop quickly from gravity."
        ]
    },
    "lateral_raise": {
        "arabic_video": "https://youtu.be/Ny_W4Hl8rYg?si=jt8tfAoxQ-SuZ43K",
        "english_video": "https://youtu.be/geenhiHju-o?si=VVlBXRwc_LWW65zG",
        "tips": [
            "ارفع الكوعين للخارج وليس اليدين فقط لضمان تفعيل الكتف الجانبي بالكامل.",
            "مل بجذعك للأمام بضع درجات لتوجيه الضغط للرأس الجانبية بدقة متناهية.",
            "لا ترفع الوزن أعلى من مستوى كتفك لتجنب تشغيل ومشاركة عضلات الترباس."
        ],
        "tips_en": [
            "Lead with your elbows outward, not just your hands, to fully engage the side deltoid.",
            "Lean your torso forward a few degrees to direct the tension precisely onto the lateral head.",
            "Don't raise the weight above shoulder level to avoid recruiting the trap muscles."
        ]
    },
    "cable_lateral_raise": {
        "arabic_video": "https://youtu.be/urpQMJp6Y50?si=UeR1myX19RT2na6K",
        "english_video": "https://youtu.be/gjXX8g-VPXI?si=LjL9ef9ISmvK9bJo",
        "tips": [
            "اضبط الكابل في أسفل مستوى لضمان أقصى مدى حركي ومقاومة مستمرة وثابتة.",
            "قف بثبات وامسك بالجهاز باليد الأخرى، ثم ارفع الكابل للخارج ببطء.",
            "تحكم في الوزن تماماً أثناء النزول (الحركة السلبية) للاستفادة القصوى."
        ],
        "tips_en": [
            "Set the cable at the lowest point to ensure maximum range of motion and constant resistance.",
            "Stand steady, hold the machine with your other hand, then raise the cable outward slowly.",
            "Control the weight fully on the way down (the negative phase) for maximum benefit."
        ]
    },
    "rear_delt_fly": {
        "arabic_video": "https://youtu.be/w0Xk5fqhO0E?si=WnD0xNtzdwl5bqS3",
        "english_video": "https://youtu.be/Y59M5fXn8bs?si=9d9US-z49HPgk32f",
        "tips": [
            "اضبط الجهاز بحيث يكون المقبض بمستوى كتفك تماماً عند وضعية البدء.",
            "ارجع بيدك للخلف باستخدام الكتف الخلفي وليس بضم عضلات الظهر العلوية.",
            "حافظ على كوعك مرتفعاً وموازياً للأرض طوال فترات التمرين."
        ],
        "tips_en": [
            "Set the machine so the handle is exactly at shoulder level at the starting position.",
            "Pull your arm back using your rear deltoid, not by squeezing your upper back muscles.",
            "Keep your elbow raised and parallel to the floor throughout the exercise."
        ]
    },
    "face_pull": {
        "arabic_video": "https://youtu.be/j654-gSjqRc?si=jIJiWSOjuMfoaje9",
        "english_video": "https://youtu.be/eFxMixk_qPQ?si=Aq9xTe0BpKHNYkIi",
        "tips": [
            "اضبط بكرة الكابل بمستوى الجبهة أو أعلى منها بقليل للحصول على زاوية سحب صحيحة.",
            "اسحب الحبل باتجاه وجهك مع فتح كوعيك للخارج وعصر عضلات الكتف الخلفي.",
            "تأكد من تدوير المعصم للخلف في نهاية الحركة (عصر خارجي للكتف)."
        ],
        "tips_en": [
            "Set the cable pulley at forehead level or slightly above for a correct pulling angle.",
            "Pull the rope toward your face while flaring your elbows out and squeezing your rear delts.",
            "Rotate your wrists backward at the end of the movement (external shoulder rotation)."
        ]
    },
    "shrugs": {
        "arabic_video": "https://youtu.be/UyxwnTZq-rk?si=iwsC3jxsHxeFV6AW",
        "english_video": "https://youtu.be/cJRVVxmytaM?si=jqCeQffWFgDUJvY3",
        "tips": [
            "ارفع كتفيك لأعلى مباشرة باتجاه أذنيك بتركيز كامل لتفعيل الترباس.",
            "لا تقم بتدوير كتفيك للخلف؛ ارفع لأعلى وانزل لأسفل بشكل مستقيم لحماية المفصل.",
            "اثبت لمدة ثانية واحدة في النقطة العلوية لعصر العضلة بقوة."
        ],
        "tips_en": [
            "Raise your shoulders straight up toward your ears with full focus to activate the traps.",
            "Don't roll your shoulders back; go straight up and down to protect the joint.",
            "Hold for one second at the top to squeeze the muscle hard."
        ]
    },
    "lat_pulldown": {
        "arabic_video": "https://youtu.be/aG71YaS5W5k?si=nsrlki69Hb87AtFB",
        "english_video": "https://youtu.be/AOpi-p0cJkc?si=xPl04zd5b8r2RWg2",
        "tips": [
            "اسحب البار باتجاه أعلى صدرك وليس خلف رقبتك تماماً لحماية مفصل الكتف.",
            "مل بظهرك للخلف بزاوية خفيفة جداً واسحب بتركيز كوعك لأسفل وليس بقوة يدك.",
            "افرد ذراعيك للأعلى ببطء لعمل إطالة كاملة وممتازة لعضلات اللاتس."
        ],
        "tips_en": [
            "Pull the bar toward the top of your chest, not behind your neck, to protect the shoulder joint.",
            "Lean back slightly and focus on pulling your elbows down rather than pulling with your hands.",
            "Extend your arms up slowly for a full, excellent stretch of the lats."
        ]
    },
    "pull_ups": {
        "arabic_video": "https://youtu.be/ON5NoQZGdgc?si=FEvpINsr-wYJ6aP1",
        "english_video": "https://youtu.be/eGo4IYlbE5g?si=neMHNH5HckkIJlTW",
        "tips": [
            "امسك البار باتساع أكبر من كتفيك بقليل مع توجيه كف اليد للأمام والتدلي بالكامل.",
            "اسحب جسمك لأعلى حتى يتخطى ذقنك البار مع الحفاظ على صدرك مرفوعاً للأمام.",
            "انزل ببطء وتحكم كامل حتى تفرد ذراعيك تقريباً للآخر دون ارتخاء عنيف."
        ],
        "tips_en": [
            "Grip the bar slightly wider than your shoulders, palms facing forward, hanging fully.",
            "Pull your body up until your chin clears the bar, keeping your chest lifted forward.",
            "Lower slowly with full control until your arms are nearly fully extended, without a hard drop."
        ]
    },
    "barbell_row": {
        "arabic_video": "https://youtu.be/S1b4XSdWx8k?si=B8Ld8XbCjDbZTea0",
        "english_video": "https://youtu.be/FWJR5Ve8bnQ?si=25SHFse5ZE-ZSkbR",
        "tips": [
            "احنِ ركبتيك قليلاً ومل بظهرك للأمام بزاوية 45 درجة مع استقامة العمود الفقري بالكامل.",
            "اسحب البار باتجاه السرة (البطن السفلى) واعتصر لوحي الكتف معاً.",
            "ثبت جذعك تماماً ولا تقم بأرجحة ظهرك لأعلى وأسفل أثناء رفع الوزن الثقيل."
        ],
        "tips_en": [
            "Bend your knees slightly and lean your torso forward at 45 degrees with your spine fully straight.",
            "Pull the bar toward your navel (lower belly) and squeeze your shoulder blades together.",
            "Keep your torso completely fixed and avoid bouncing your back while lifting heavy weight."
        ]
    },
    "dumbbell_row": {
        "arabic_video": "https://youtu.be/jCqfXS1Uxd4?si=wM1qdONKX741P9W5",
        "english_video": "https://youtu.be/dFzUjzfih7k?si=7YDfQWdz-stw1R4X",
        "tips": [
            "ضع ركبة ويد على الدكة للحصول على ثبات كامل وجعل الظهر مستقيماً وموازياً للأرض.",
            "اسحب الدمبل باتجاه الحوض (الورك) وليس الصدر لتفعيل اللاتس بشكل أكبر وعميق.",
            "انزل بالوزن لأسفل ببطء لعمل إطالة كاملة وممتازة لعضلات الظهر."
        ],
        "tips_en": [
            "Place one knee and hand on the bench for full stability, keeping your back straight and parallel to the floor.",
            "Pull the dumbbell toward your hip, not your chest, to engage the lats more deeply.",
            "Lower the weight slowly for a full, excellent stretch of the back muscles."
        ]
    },
    "cable_row": {
        "arabic_video": "https://youtu.be/Nr54dXCXrk4?si=aP4S-rrvpSMZifYq",
        "english_video": "https://youtu.be/dFzUjzfih7k?si=7YDfQWdz-stw1R4X",
        "tips": [
            "اجلس بظهر مستقيم تماماً وثبت رجليك على المسند مع انحناء خفيف في الركبة.",
            "اسحب المقبض باتجاه بطنك مع ضم لوحي الكتف وعصر الظهر في نهاية الحركة.",
            "لا تمل بجسدك للأمام بشكل مبالغ فيه أو عنيف أثناء رجوع الكابل."
        ],
        "tips_en": [
            "Sit with a completely straight back and brace your feet on the platform with a slight knee bend.",
            "Pull the handle toward your stomach, squeezing your shoulder blades and back at the end.",
            "Don't lean your body forward excessively or violently as the cable returns."
        ]
    },
    "deadlift": {
        "arabic_video": "https://youtu.be/apKzzKJZvvY?si=pfEMvWAbNKKnEWLt",
        "english_video": "https://youtu.be/AweC3UaM14o?si=w3d7U1CBJKAZD7mu",
        "tips": [
            "ضع البار فوق منتصف قدمك تماماً والتصق به بقصبة الرجل قبل بدء الرفع.",
            "حافظ على ظهرك مستقيماً ومشدوداً بالكامل دون أي تقوس أو انحناء لحماية الفقرات.",
            "ادفع الأرض بقدميك وارفع الوزن مع الحفاظ على البار قريباً جداً من ساقيك طوال الرفع."
        ],
        "tips_en": [
            "Position the bar directly over the middle of your foot, close to your shins, before lifting.",
            "Keep your back straight and fully braced without any rounding or arching to protect your spine.",
            "Drive through the floor with your feet and lift the weight while keeping the bar close to your legs throughout."
        ]
    },
    "hyperextension": {
        "arabic_video": "https://youtu.be/VaCD5i5-5uI?si=ELj6pjbMeE0z0qF_",
        "english_video": "https://youtu.be/ph3pddpKzzw?si=ctamhgALCU40RvF3",
        "tips": [
            "اضبط الوسادة بحيث تكون أسفل عظم الحوض مباشرة لتسمح بمدى حركي كامل ومريح.",
            "انزل بظهر مستقيم حتى تشعر بإطالة، ثم ارفع باستخدام عضلات المؤخرة والقطنية.",
            "لا تبالغ في رفع ظهرك للأعلى خلف خط الاستقامة لتجنب الضغط الزائد على الفقرات."
        ],
        "tips_en": [
            "Set the pad just below your hip bone to allow a full, comfortable range of motion.",
            "Lower with a straight back until you feel a stretch, then rise using your glutes and lower back.",
            "Don't raise your back excessively past the straight line to avoid excess pressure on the spine."
        ]
    },
    "t_bar_row": {
        "arabic_video": "https://youtu.be/haB-Ar6YwJc?si=grLNNzCbZEiig_X3",
        "english_video": "https://youtu.be/KDEl3AmZbVE?si=3eqnHw8Azo79BoYW",
        "tips": [
            "قف بثبات واحنِ ظهرك مع الحفاظ على استقامة العمود الفقري بالكامل وشد البطن.",
            "اسحب الوزن باتجاه بطنك مع التركيز على سحب الكوعين لأعلى وعصر عضلات الظهر.",
            "حافظ على ثبات ركبتيك وجذعك تماماً دون الاستعانة بمرجحة الجسم لتوليد الزخم."
        ],
        "tips_en": [
            "Stand firmly and hinge your back while keeping your spine fully straight and your core braced.",
            "Pull the weight toward your stomach, focusing on driving your elbows up and squeezing your back.",
            "Keep your knees and torso completely stable without swinging your body for momentum."
        ]
    },
    "squat": {
        "arabic_video": "https://youtu.be/s3rbxNBE7j8?si=9IMTo7CkSat7-4K0",
        "english_video": "https://youtu.be/aOzrA4FgnM0?si=h8shObQh_p8-b96v",
        "tips": [
            "ضع البار على عضلات الترابيس العليا وليس الرقبة، واجعل قدميك باتساع الكتف.",
            "انزل بالحوض كأنك تجلس على كرسي، مع الحفاظ على استقامة الظهر ودفع الركب للخارج.",
            "اضغط بكعب قدمك في الأرض للدفع لأعلى ولا ترفع كعبك عن الأرض أبداً."
        ],
        "tips_en": [
            "Rest the bar on your upper traps, not your neck, with feet shoulder-width apart.",
            "Lower your hips as if sitting in a chair, keeping your back straight and pushing your knees outward.",
            "Press through your heels to stand up, and never let your heels lift off the floor."
        ]
    },
    "lunges": {
        "arabic_video": "https://youtu.be/NVN0FfB1gnQ?si=NIYaxfT48pfhBSA-",
        "english_video": "https://youtu.be/wrwwXE_x-pQ?si=uapsiNUSxvAjJhB4",
        "tips": [
            "خذ خطوة واسعة ومستقرة للأمام وانزل بركبتك الخلفية حتى تقترب من الأرض ببطء.",
            "تأكد من أن ركبتك الأمامية بزاوية 90 درجة ولا تتخطى مشط قدمك بشكل مبالغ فيه لحماية المفصل.",
            "حافظ على استقامة جذعك وصدرك مرفوعاً للأعلى لضمان التوازن السليم طوال الحركة."
        ],
        "tips_en": [
            "Take a wide, stable step forward and lower your back knee slowly until it nearly touches the floor.",
            "Keep your front knee at 90 degrees and avoid letting it travel too far past your toes to protect the joint.",
            "Keep your torso upright and chest lifted for proper balance throughout the movement."
        ]
    },
    "leg_extension": {
        "arabic_video": "https://youtu.be/AehvZ26uaA4?si=dGsm97VfvzrGkPCI",
        "english_video": "https://youtu.be/swZQC689o9U?si=HLbirGd4gQ8wpi0S",
        "tips": [
            "اضبط مسند الظهر بحيث تكون ركبتك محاذية تماماً لمحور دوران جهاز الأماميات.",
            "افرد رجلك لأعلى بتركيز واثبت لثانية في الأعلى لعصر العضلة الأمامية للفخذ.",
            "انزل بالوزن ببطء وتحكم كامل ولا تتركه يسقط فجأة بحرية للاستفادة من الحركة السلبية."
        ],
        "tips_en": [
            "Adjust the backrest so your knee is perfectly aligned with the machine's pivot point.",
            "Extend your leg up with focus and hold for a second at the top to squeeze the quads.",
            "Lower the weight slowly with full control instead of letting it drop, to benefit from the negative phase."
        ]
    },
    "leg_curls": {
        "arabic_video": "https://youtu.be/JsdemJ_IMEw?si=xm8PpIZpq6_lkZ3m",
        "english_video": "https://youtu.be/t9sTSr-JYSs?si=CDQLRHbqEqq1WThY",
        "tips": [
            "اضبط مسند القدم ليكون فوق كعبك مباشرة (أسفل نهاية عضلة السمانة).",
            "اسحب الوزن باتجاه المؤخرة بتركيز مع تثبيت الحوض تماماً على مقعد الجهاز.",
            "افرد رجلك ببطء وتحكم للاستفادة الكاملة وحماية أربطة الركبة الخلفية."
        ],
        "tips_en": [
            "Set the ankle pad directly above your heel (just below the end of your calf muscle).",
            "Pull the weight toward your glutes with focus, keeping your hips fully pressed on the pad.",
            "Extend your leg back out slowly and with control for full benefit and to protect the hamstring tendons."
        ]
    },
    "leg_press": {
        "arabic_video": "https://youtu.be/ua01o7v6BdM?si=MvTCXi6T0dy6Xwmx",
        "english_video": "https://youtu.be/K5n2vg3oZa4?si=u-SLWkMzEqvEN_Rl",
        "tips": [
            "ضع قدميك باتساع الكتفين على المنصة، وانزل حتى تصبح ركبتك بزاوية 90 درجة تقريباً.",
            "احذر تماماً من قفل أو تفريط ركبتك بعنف في نهاية الحركة لحمايتها من الإصابات البالغة.",
            "حافظ على ثبات أسفل ظهرك ومقعدتك ملتصقين تماماً بالمسند الخلفي أثناء النزول بالوزن."
        ],
        "tips_en": [
            "Place your feet shoulder-width apart on the platform, lowering until your knees are around 90 degrees.",
            "Avoid locking or hyperextending your knees violently at the end of the movement to prevent injury.",
            "Keep your lower back and glutes fully pressed against the backrest as you lower the weight."
        ]
    },
    "calf_raise": {
        "arabic_video": "https://youtu.be/869CEsQMndw?si=Lnp1iY_5dYfZjDSp",
        "english_video": "https://youtu.be/k67UjgvJdEk?si=O7srdggt_pi4433G",
        "tips": [
            "ضع مشط قدمك فقط على المسند واترك الكعب حراً للحصول على كامل المدى الحركي نزولاً وصعوداً.",
            "انزل بكعبك لأسفل نقطة لعمل إطالة، ثم ارفع لأقصى نقطة على أطراف أصابعك لعصر السمانة.",
            "اثبت ثانية في الأعلى واعتصر العضلة، وتجنب استخدام الارتداد السريع المعتمد على الأربطة."
        ],
        "tips_en": [
            "Place only the balls of your feet on the platform, letting your heels hang free for a full range of motion.",
            "Lower your heels to the bottom for a stretch, then rise onto your toes to squeeze the calves.",
            "Hold for a second at the top and squeeze the muscle, avoiding fast tendon-dependent bouncing."
        ]
    },
    "hip_abductor": {
        "arabic_video": "https://youtu.be/KD9WmTV3wEI?si=m_N_9Z2_jO74diVb",
        "english_video": "https://youtu.be/h9BqUMqK-SY?si=bxIz966vUsMQN6Kv",
        "tips": [
            "اجلس بظهر مستقيم وملتصق بالمسند تماماً للحصول على عزل حركي صحيح.",
            "ادفع المساند للخارج بقوة باستخدام عضلات المؤخرة الجانبية واثبت ثانية في النهاية.",
            "ارجع ببطء لمنع الأوزان من الاصطدام ببعضها وضمان مقاومة عضلية مستمرة."
        ],
        "tips_en": [
            "Sit with your back straight and fully against the pad for correct movement isolation.",
            "Push the pads outward forcefully using your outer glute muscles, holding for a second at the end.",
            "Return slowly to prevent the weights from slamming together and to keep constant muscular tension."
        ]
    },
    "hip_adductor": {
        "arabic_video": "https://youtu.be/KD9WmTV3wEI?si=5TzwwQmQMtyaXkhU",
        "english_video": "https://youtu.be/h9BqUMqK-SY?si=bxIz966vUsMQN6Kv",
        "tips": [
            "اضبط الجهاز على مدى حركي واسع ومريح دون التسبب في إجهاد زائد أو تمزق للمفاصل.",
            "ضم رجليك للداخل بتركيز لتشغيل عضلات الفخذ الداخلية وعصرها جيداً في المنتصف.",
            "تحكم في حركة رجوع الوزن للخارج ببطء وبطريقة مدروسة لحماية أربطة الحوض الداخلية."
        ],
        "tips_en": [
            "Set the machine to a wide, comfortable range of motion without causing excess strain on the joints.",
            "Squeeze your legs inward with focus to engage and squeeze your inner thigh muscles at the midpoint.",
            "Control the weight as it returns outward slowly and deliberately to protect your inner hip ligaments."
        ]
    },
    "glute_bridge": {
        "arabic_video": "https://youtu.be/pmUPsOuSYsc?si=K9LStVf1pBzjhXLX",
        "english_video": "https://youtu.be/sh63qy5EV_8?si=ZU926TVmfyLt1a67",
        "tips": [
            "استلقِ على ظهرك واثنِ ركبتيك مع تثبيت قدميك بالكامل على الأرض باتساع الحوض.",
            "ادفع حوضك لأعلى بالتركيز على عصر عضلات المؤخرة (Glutes) وليس أسفل الظهر.",
            "حافظ على استقامة خط الجسم من الكتف للركبة في أعلى نقطة واثبت لثانية."
        ],
        "tips_en": [
            "Lie on your back with knees bent and feet fully planted on the floor, hip-width apart.",
            "Drive your hips up, focusing on squeezing your glutes rather than your lower back.",
            "Keep a straight line from shoulder to knee at the top and hold for a second."
        ]
    },
    "bicep_curl": {
        "arabic_video": "https://youtu.be/WH-fpdbmVew?si=vQ9iWOIzXA0ef7qV",
        "english_video": "https://youtu.be/6DeLZ6cbgWQ?si=ljwGvWryddUThmZb",
        "tips": [
            "ثبّت كوعيك بجانب جذعك تماماً واحذر من تحريكهما للأمام أو الخلف أثناء الرفع.",
            "ارفع الوزن بمدى حركي كامل واعتصر عضلة البايسبس في الأعلى بتركيز.",
            "انزل بالوزن ببطء وتحكم ولا تفرد كوعك بنسبة 100% بعنف في النهاية لحماية المفصل."
        ],
        "tips_en": [
            "Keep your elbows fixed right at your sides, careful not to move them forward or back while lifting.",
            "Lift the weight through a full range of motion and squeeze your biceps hard at the top.",
            "Lower the weight slowly with control, without snapping your elbow fully straight to protect the joint."
        ]
    },
    "hammer_curl": {
        "arabic_video": "https://youtu.be/E0_PK-ta0jQ?si=J9esJMYlMNhv9_Ar",
        "english_video": "https://youtu.be/BRVDS6HVR9Q?si=fIa__E-JWEKUNUam",
        "tips": [
            "امسك الدمبلز بوضعية عمودية (بحيث يكون كف اليد مواجهاً للداخل كأنه مطرقة).",
            "حافظ على ثبات معصم اليد تماماً دون التواء أثناء صعود وهبوط الوزن.",
            "ركز على تشغيل عضلة الساعد (Brachioradialis) والباي الجانبي بالتحكم في الحركة السلبية."
        ],
        "tips_en": [
            "Hold the dumbbells in a vertical grip (palms facing inward, like a hammer).",
            "Keep your wrist completely stable without twisting as the weight goes up and down.",
            "Focus on engaging the brachioradialis and outer bicep by controlling the negative phase."
        ]
    },
    "tricep_pushdown": {
        "arabic_video": "https://youtu.be/Wn7nBZ1vPEg?si=EcLBJzkpTwSKjEh5",
        "english_video": "https://youtu.be/-zLyUAo1gMw?si=hyHbYiw_k8V9vtDY",
        "tips": [
            "قف بثبات مع ميل خفيف جداً للأمام وثبّت كوعيك بجانب جسمك طوال التمرين.",
            "اضغط بالكابل لأسفل حتى تفرد ذراعك تماماً واعتصر عضلات الترايسبس بقوة.",
            "ارجع بالوزن لأعلى ببطء حتى يمر كوعك بزاوية 90 درجة بقليل دون تحريك الكتف."
        ],
        "tips_en": [
            "Stand steady with a very slight forward lean, keeping your elbows fixed at your sides throughout.",
            "Push the cable down until your arm is fully extended, squeezing your triceps hard.",
            "Return the weight up slowly until your elbow is just past 90 degrees, without moving your shoulder."
        ]
    },
    "overhead_tricep_extension": {
        "arabic_video": "https://youtu.be/1WxfkjJC2Ys?si=5Bnj9oSjFnFSp3dO",
        "english_video": "https://youtu.be/ns-RGsbzqok?si=0Dyw4Haq_Qjl3uEO",
        "tips": [
            "ارفع ذراعيك لأعلى واحرص على ضم كوعيك للداخل ومحاذاة الرأس دون فتحهما للخارج.",
            "انزل بالوزن خلف رأسك ببطء لتحقيق أقصى إطالة ممكنة للرأس الطويلة من الترايسبس.",
            "ادفع الوزن لأعلى بتركيز كامل مع الحفاظ على ثبات أسفل الظهر دون تقوس مبالغ فيه."
        ],
        "tips_en": [
            "Raise your arms overhead, keeping your elbows tucked in and aligned with your head rather than flared out.",
            "Lower the weight behind your head slowly for maximum stretch of the triceps' long head.",
            "Press the weight up with full focus while keeping your lower back stable without excessive arching."
        ]
    },
    "abdominal": {
        "arabic_video": "https://youtu.be/5yXV8A3NmpE?si=4BzKPWhqxC6ZKsVZ",
        "english_video": "https://youtu.be/iMRs5SYUKrA?si=N-0CsLJ70k5nF5uz",
        "tips": [
            "عند أداء تمارين البطن (Crunches)، ركز على تقريب قفصك الصدري من حوضك لعصر العضلة.",
            "لا تسحب رقبتك بفتحة يديك خلف الرأس، بل اجعل التركيز والدفع نابعاً من عضلات البطن.",
            "اصعد ببطء واطرد النفس (زفير) عند الانقباض، وانزل ببطء مع أخذ نفس (شهيق)."
        ],
        "tips_en": [
            "When doing crunches, focus on bringing your rib cage toward your pelvis to squeeze the muscle.",
            "Don't pull your neck with your hands behind your head; let the effort come from your abs.",
            "Exhale as you crunch up and inhale slowly as you lower back down."
        ]
    },
    "plank": {
        "arabic_video": "https://youtu.be/TldvfwHQ0lw?si=zsfGERYfoTvaDnqx",
        "english_video": "https://youtu.be/A2b2EmIg0dA?si=g8B9RgqjDSmfRaul",
        "tips": [
            "ارتكز على ساعديك وأطراف قدميك، واجعل جسمك خطاً مستقيماً تماماً من الرأس للكعب.",
            "شد عضلات بطنك ومؤخرتك بقوة لمنع سقوط الحوض لأسفل والتحميل على الفقرات القطنية.",
            "اضغط بساعديك في الأرض لدفع لوحي الكتف لأعلى وتجنب سقوط الصدر لأسفل."
        ],
        "tips_en": [
            "Rest on your forearms and toes, keeping your body in a perfectly straight line from head to heels.",
            "Brace your abs and glutes firmly to prevent your hips from sagging and loading your lower back.",
            "Press your forearms into the floor to lift your shoulder blades up and avoid letting your chest drop."
        ]
    }
}


def handle(user_input, entity, is_short_func, user_data={}, lang="ar"):
    """الـ handler الخاص بـ exercise_help"""
    if lang == "en":
        if not entity:
            return "Which exercise do you need help with exactly? 🏋️"
        if is_short_func(user_input):
            return f"Would you like help with the {entity.replace('_', ' ')} exercise? 🏋️"

        data = EXERCISE_DATA.get(entity)
        if not data:
            return f"Sorry, I don't have enough details on this exercise yet 🙏 [entity: {entity}]"

        tips_text = "\n".join(f"✅ {tip}" for tip in data["tips_en"])
        return (
            f"Great 💪 Here are some resources and tips for the {entity.replace('_', ' ')} exercise:\n\n"
            f"🎥 Video explanation in Arabic:\n{data['arabic_video']}\n\n"
            f"🎥 Video explanation in English:\n{data['english_video']}\n\n"
            f"📝 Tips for correct form:\n{tips_text}"
        )

    if not entity:
        return "عايز مساعدة في تمرين إيه بالظبط؟ 🏋️"
    if is_short_func(user_input):
        return f"هل عايزني أساعدك في تمرين {entity}؟ 🏋️"

    data = EXERCISE_DATA.get(entity)
    if not data:
        return f"معلش، لسه مفيش تفاصيل كافية عن التمرين ده 🙏 [entity: {entity}]"

    tips_text = "\n".join(f"✅ {tip}" for tip in data["tips"])
    return (
        f"تمام 💪 دي شوية مصادر ونصايح لتمرين {entity.replace('_', ' ')}:\n\n"
        f"🎥 فيديو شرح بالعربي:\n{data['arabic_video']}\n\n"
        f"🎥 فيديو شرح بالإنجليزي:\n{data['english_video']}\n\n"
        f"📝 نصايح لتنفيذ التمرين صح:\n{tips_text}"
    )
