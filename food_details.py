# ============================================================
# food_details.py
# قيم غذائية مرجعية لكل 100 جرام (مصدر: USDA FoodData Central)
# كل عنصر: calories, protein, carbs, fats + ملاحظة مميزة + الفايدة + أنسب وقت للأكل
# ============================================================

FOOD_DETAILS_ENTITIES = {
    "فراخ": ["فراخ", "دجاج", "صدور", "وراك", "chicken"],
    "لحمة": [ "لحم", "ستيك", "مفروم", "meat"],
    "سمك": ["سمك", "سلمون", "fish","بوري","بلطي"],
    "تونة": ["تونة", "tuna"],
    "بيض": ["بيض", "صفار", "eggs"],
    # ألبان
    "لبن": ["لبن", "حليب", "milk"],
    "جبنة": ["جبنة", "قريش", "cheese"],
    "زبادي": ["زبادي", "يوناني", "yogurt"],

    # كارب
    "رز": ["رز", "أرز", "rice"],
    "مكرونة": ["مكرونة", "pasta", "macroni"],
    "شوفان": ["شوفان", "oats"],
    "بطاطس": ["بطاطس", "بطاطا", "potatoes"],
    "عيش": ["عيش", "خبز", "bread","عيش بلدي"],
    "توست":["توست","toast","عيش توست"],
    "محشي": ["محشي", "كرمب", "ورق عنب", "كوسة محشية"],

    # أكلات شعبية وطاقة
    "عسل": ["عسل", "عسل نحل", "عسل اسود", "honey","molases"],
    "فول": ["فول", "مدمس", "beans", "fava_beans"],
    "طعمية": ["طعمية", "فلافل", "falafel"],

    # خضار
    "خيار": ["خيار", "cucumber"],
    "طماطم": ["طماطم", "tomato"],
    "بروكلي": ["بروكلي", "broccoli"],
    "سبانخ": ["سبانخ", "spinach"],
    "خس": ["خس", "جرجير", "lettuce"],
    "بسلة": ["بسلة", "peas"],
    "فاصوليا": ["فاصوليا", "beans"],
    "لوبيا": ["لوبيا", "black_eyed_peas"],
    "كوسة": ["كوسة", "zucchini"],

    # فواكه
    "موز": ["موز", "banana"],
    "تمر": ["تمر", "بلح", "dates"],
    "افوكادو": ["افوكادو", "avocado"],
    "فراولة": ["فراولة", "strawberry"],
    "تفاح": ["تفاح", "apple"],
    "اناناس": ["اناناس", "pineapple"],
    "برتقال": ["برتقال", "orange"],
    "كيوي": ["كيوي", "kiwi"],
    "توت": ["توت", "berries"],
    "بطيخ": ["بطيخ", "watermelon"],
    "مانجو": ["مانجو", "mango"],
    "عنب": ["عنب", "grapes"],
}

# أسماء العناصر بالإنجليزي - بيتستخدموا وقت الرد لليوزر الإنجليزي بس
FOOD_NAMES_EN = {
    "فراخ": "chicken", "لحمة": "red meat", "سمك": "fish", "تونة": "tuna", "بيض": "eggs",
    "لبن": "milk", "جبنة": "cottage cheese", "زبادي": "yogurt",
    "رز": "rice", "مكرونة": "pasta", "شوفان": "oats", "بطاطس": "potatoes",
    "عيش": "bread", "توست": "toast", "محشي": "stuffed vegetables (mahshi)",
    "عسل": "honey", "فول": "fava beans", "طعمية": "falafel",
    "خيار": "cucumber", "طماطم": "tomato", "بروكلي": "broccoli", "سبانخ": "spinach",
    "خس": "lettuce", "بسلة": "peas", "فاصوليا": "beans", "لوبيا": "black-eyed peas", "كوسة": "zucchini",
    "موز": "banana", "تمر": "dates", "افوكادو": "avocado", "فراولة": "strawberry",
    "تفاح": "apple", "اناناس": "pineapple", "برتقال": "orange", "كيوي": "kiwi",
    "توت": "berries", "بطيخ": "watermelon", "مانجو": "mango", "عنب": "grapes",
}


def DESCRIPTION(entity="اكل معين", lang="ar"):
    # لو الـ entity مبعوت وقيمته None أو فاضي، خليه ياخد القيمة الافتراضية
    if entity is None or entity == "":
        entity = "اكل معين" if lang != "en" else "a specific food"

    if lang == "en":
        entity_en = FOOD_NAMES_EN.get(entity, entity)
        return f"Want to know the nutritional value of {entity_en}? 🍽️"

    return f"عايز تعرف القيمة الغذائية ل{entity}؟ 🍽️"

# ============================================================
# القيم لكل 100 جرام (إلا لو محدد غير ذلك) - مصدر USDA
# ============================================================
FOOD_DETAILS_DATA = {
    "فراخ": {
        "calories": 165, "protein": 31.0, "carbs": 0.0, "fats": 3.6,
        "highlight": "صدور دجاج مطبوخة بدون جلد، أعلى نسبة بروتين وأقل دهون",
        "benefit": "مثالية لبناء وتضخيم العضلات الصافية دون زيادة الدهون، وسهلة الهضم",
        "best_time": "بعد التمرين مباشرة أو كوجبة أساسية وسط اليوم لإمداد العضلات بالبروتين",
        "highlight_en": "Skinless cooked chicken breast, the highest protein and lowest fat option",
        "benefit_en": "Ideal for building lean muscle without adding fat, and easy to digest",
        "best_time_en": "Right after training, or as a main midday meal to fuel your muscles with protein"
    },
    "لحمة": {
        "calories": 250, "protein": 26.0, "carbs": 0.0, "fats": 15.0,
        "highlight": "لحم بقري مشوي (قليل الدسم)، غني بالحديد العضوي والـ الكرياتين الطبيعي",
        "benefit": "يرفع مستويات الطاقة، يعزز القوة البدنية، ويساعد في كفاءة إنتاج خلايا الدم الحمراء",
        "best_time": "في وجبة الغداء أو قبل التمرين بفترة كافية (3-4 ساعات) لأن هضمها يأخذ وقتاً",
        "highlight_en": "Grilled beef (lean cut), rich in heme iron and natural creatine",
        "benefit_en": "Boosts energy levels, supports physical strength, and aids red blood cell production",
        "best_time_en": "At lunch, or 3-4 hours before training since it takes longer to digest"
    },
    "سمك": {
        "calories": 206, "protein": 22.0, "carbs": 0.0, "fats": 12.0,
        "highlight": "سمك سلمون مطبوخ، مصدر ممتاز للأوميجا 3 (Omega-3) والدهون الصحية",
        "benefit": "يقلل التهابات المفاصل بعد التمرين، يدعم صحة القلب، ويعزز الاستشفاء العضلي",
        "best_time": "وجبة الغداء أو العشاء، ممتاز جداً كوجبة استشفاء بعد يوم تمرين شاق",
        "highlight_en": "Cooked salmon, an excellent source of omega-3 and healthy fats",
        "benefit_en": "Reduces post-workout joint inflammation, supports heart health, and aids muscle recovery",
        "best_time_en": "Lunch or dinner; excellent as a recovery meal after a tough training day"
    },
    "تونة": {
        "calories": 130, "protein": 28.0, "carbs": 0.0, "fats": 1.0,
        "highlight": "تونة قطع مصفاة من الزيت (أو في محلول مائي)، بروتين صافي وسريع",
        "benefit": "وجبة اقتصادية وسريعة التحضير لإنقاذ مخازن البروتين، ممتازة للتنشيف لقلة دهونها",
        "best_time": "بعد التمرين، أو كوجبة خفيفة وسريعة في العمل أو الجامعة",
        "highlight_en": "Drained canned tuna (in oil or water), a lean and fast protein source",
        "benefit_en": "A cheap, quick meal to hit your protein needs; great for cutting due to its low fat",
        "best_time_en": "After training, or as a quick light meal at work or college"
    },
    "بيض": {
        "calories": 155, "protein": 13.0, "carbs": 1.1, "fats": 11.0,
        "highlight": "بيض كامل مسلوق، يمتلك أعلى قيمة بيولوجية (Bioavailability) للبروتين",
        "benefit": "يحتوي على جميع الأحماض الأمينية الأساسية، وصفار البيض غني بالكولين المفيد للمخ والهرمونات",
        "best_time": "في وجبة الفطور لزيادة الشبع طوال اليوم، أو كوجبة خفيفة قبل أو بعد التمرين",
        "highlight_en": "Boiled whole eggs, with the highest biological value protein of any food",
        "benefit_en": "Contains all essential amino acids; the yolk is rich in choline, good for the brain and hormones",
        "best_time_en": "At breakfast for lasting satiety, or as a light snack before or after training"
    },

    # ---------------- ألبان ----------------
    "لبن": {
        "calories": 61, "protein": 3.2, "carbs": 4.8, "fats": 3.3,
        "highlight": "مصدر جيد للكالسيوم وفيتامين D",
        "benefit": "مفيد لصحة العظام والأسنان، ومصدر بروتين متكامل",
        "best_time": "في أي وقت، ومفيد قبل النوم لمحتواه من الكازين البطيء الامتصاص",
        "highlight_en": "A good source of calcium and vitamin D",
        "benefit_en": "Good for bone and teeth health, and a complete protein source",
        "best_time_en": "Any time; especially useful before bed due to its slow-digesting casein"
    },
    "جبنة": {
        "calories": 98, "protein": 11, "carbs": 3.4, "fats": 4.3,
        "highlight": "من أعلى مصادر البروتين بين الألبان (جبنة قريش)",
        "benefit": "مفيدة جداً للدايت والتنشيف لأنها عالية البروتين وقليلة السعرات",
        "best_time": "مفيدة كوجبة خفيفة أو قبل النوم",
        "highlight_en": "One of the highest-protein dairy options (cottage cheese)",
        "benefit_en": "Great for dieting and cutting, since it's high in protein and low in calories",
        "best_time_en": "Good as a light snack or before bed"
    },
    "زبادي": {
        "calories": 59, "protein": 10, "carbs": 3.6, "fats": 0.4,
        "highlight": "الزبادي اليوناني تحديداً أعلى بروتين من الزبادي العادي",
        "benefit": "مفيد للهضم لاحتوائه على بروبيوتيك، وبروتين عالي مع دهون منخفضة",
        "best_time": "وجبة خفيفة أو بعد التمرين",
        "highlight_en": "Greek yogurt specifically has more protein than regular yogurt",
        "benefit_en": "Good for digestion thanks to probiotics, with high protein and low fat",
        "best_time_en": "As a snack or after training"
    },

    # ---------------- كارب ----------------
    "رز": {
        "calories": 130, "protein": 2.7, "carbs": 28, "fats": 0.3,
        "highlight": "الرز الأبيض المسلوق، الكارب فيه سريع الامتصاص",
        "benefit": "مصدر طاقة سريع، مفيد حوالين التمرين",
        "best_time": "قبل أو بعد التمرين لتعويض الطاقة بسرعة",
        "highlight_en": "Boiled white rice, its carbs are absorbed quickly",
        "benefit_en": "A fast energy source, useful around training time",
        "best_time_en": "Before or after training to quickly replenish energy"
    },
    "مكرونة": {
        "calories": 131, "protein": 5, "carbs": 25, "fats": 1.1,
        "highlight": "مسلوقة، الكارب فيها أبطأ امتصاص من الرز الأبيض",
        "benefit": "مصدر طاقة جيد، تفضل الووله ويت (whole wheat) لكارب أبطأ وأكتر إشباع",
        "best_time": "وجبة الغدا أو قبل التمرين بساعتين",
        "highlight_en": "Boiled pasta, its carbs are absorbed more slowly than white rice",
        "benefit_en": "A good energy source; prefer whole wheat for slower carbs and more fullness",
        "best_time_en": "At lunch, or 2 hours before training"
    },
    "شوفان": {
        "calories": 389, "protein": 16.9, "carbs": 66, "fats": 6.9,
        "highlight": "غني بالألياف القابلة للذوبان (بيتا جلوكان)",
        "benefit": "مفيد جداً، بيمد بطاقة ثابتة لفترة طويلة وبيحسن الكوليسترول",
        "best_time": "أفضل وقت هو الصبح، وجبة فطار مثالية",
        "highlight_en": "Rich in soluble fiber (beta-glucan)",
        "benefit_en": "Provides steady, long-lasting energy and helps improve cholesterol",
        "best_time_en": "Best in the morning; an ideal breakfast meal"
    },
    "بطاطس": {
        "calories": 77, "protein": 2, "carbs": 17, "fats": 0.1,
        "highlight": "مسلوقة أو مشوية بدون زيت زيادة",
        "benefit": "مصدر بوتاسيوم وكارب جيد، مفيدة لو متعملة بطريقة صحية (مش مقلية)",
        "best_time": "بعد التمرين أو في وجبة الغدا",
        "highlight_en": "Boiled or baked without extra oil",
        "benefit_en": "A good source of potassium and carbs, especially when prepared in a healthy way (not fried)",
        "best_time_en": "After training or at lunch"
    },
    "عيش": {
        "calories": 265, "protein": 9, "carbs": 49, "fats": 3.2,
        "highlight": "العيش الأسمر أفضل من الأبيض لاحتوائه على ألياف أكتر",
        "benefit": "مصدر كارب أساسي، يفضل الأسمر أو البلدي بدل التوست الأبيض المعالج",
        "best_time": "وجبة الفطار أو الغدا",
        "highlight_en": "Whole wheat bread is better than white since it has more fiber",
        "benefit_en": "A staple carb source; whole wheat or baladi bread is better than processed white toast",
        "best_time_en": "At breakfast or lunch"
    },
    "محشي": {
        "calories": 120, "protein": 3, "carbs": 18, "fats": 4,
        "highlight": "بيختلف حسب نوع الحشو (رز وخضار غالباً)",
        "benefit": "وجبة متوسطة السعرات لو مش زودة زيت، فيها خضار وكارب",
        "best_time": "وجبة غدا أو عشا خفيف",
        "highlight_en": "Varies depending on the filling (usually rice and vegetables)",
        "benefit_en": "A moderate-calorie meal if not overloaded with oil, providing vegetables and carbs",
        "best_time_en": "At lunch or as a light dinner"
    },

    # ---------------- أكلات شعبية وطاقة ----------------
    "عسل": {
        "calories": 304, "protein": 0.3, "carbs": 82, "fats": 0,
        "highlight": "سكر طبيعي سريع الامتصاص، 100% كارب تقريباً",
        "benefit": "مفيد بكمية قليلة كمصدر طاقة سريع، مش بديل صحي عن السكر بكميات كبيرة",
        "best_time": "قبل التمرين مباشرة لطاقة سريعة",
        "highlight_en": "Fast-absorbing natural sugar, almost 100% carbs",
        "benefit_en": "Useful in small amounts as a quick energy source; not a healthy substitute for sugar in large quantities",
        "best_time_en": "Right before training for quick energy"
    },
    "فول": {
        "calories": 110, "protein": 7.6, "carbs": 19, "fats": 0.6,
        "highlight": "مصدر بروتين نباتي رخيص وغني بالألياف",
        "benefit": "مفيد جداً، يمد بالشبع لفترة طويلة وبروتين نباتي جيد",
        "best_time": "وجبة الفطار غالباً",
        "highlight_en": "A cheap plant-based protein source, rich in fiber",
        "benefit_en": "Very beneficial; keeps you full for a long time with good plant protein",
        "best_time_en": "Usually at breakfast"
    },
    "طعمية": {
        "calories": 333, "protein": 13, "carbs": 32, "fats": 18,
        "highlight": "مقلية في زيت، فالسعرات والدهون عالية نسبياً",
        "benefit": "فيها بروتين نباتي كويس بس الدهون عالية بسبب القلي، أفضل بالفرن",
        "best_time": "وجبة معتدلة، مش مناسبة لو هدفك تنشيف",
        "highlight_en": "Fried in oil, so calories and fat are relatively high",
        "benefit_en": "Has decent plant protein, but fat is high due to frying; baked is better",
        "best_time_en": "A moderate meal; not ideal if your goal is cutting"
    },

    # ---------------- خضار ----------------
    "خيار": {
        "calories": 15, "protein": 0.7, "carbs": 3.6, "fats": 0.1,
        "highlight": "95% منه مية، سعرات قليلة جداً",
        "benefit": "مفيد جداً للترطيب والشبع بسعرات قليلة",
        "best_time": "في أي وقت، خيار ممتاز للسناك",
        "highlight_en": "95% water, very low in calories",
        "benefit_en": "Great for hydration and fullness with very few calories",
        "best_time_en": "Any time; an excellent snack option"
    },
    "طماطم": {
        "calories": 18, "protein": 0.9, "carbs": 3.9, "fats": 0.2,
        "highlight": "غنية بالليكوبين (مضاد أكسدة قوي)",
        "benefit": "مفيدة جداً، قليلة السعرات وغنية بفيتامين C",
        "best_time": "في أي وقت مع الوجبات",
        "highlight_en": "Rich in lycopene (a powerful antioxidant)",
        "benefit_en": "Very beneficial; low calorie and rich in vitamin C",
        "best_time_en": "Any time, alongside meals"
    },
    "بروكلي": {
        "calories": 34, "protein": 2.8, "carbs": 7, "fats": 0.4,
        "highlight": "من أعلى الخضار في فيتامين C والألياف",
        "benefit": "مفيد جداً، يدعم المناعة والهضم بسعرات قليلة",
        "best_time": "أي وقت، مفيد جنب البروتين في الغدا أو العشا",
        "highlight_en": "One of the highest vegetables in vitamin C and fiber",
        "benefit_en": "Very beneficial; supports immunity and digestion with few calories",
        "best_time_en": "Any time, good alongside protein at lunch or dinner"
    },
    "سبانخ": {
        "calories": 23, "protein": 2.9, "carbs": 3.6, "fats": 0.4,
        "highlight": "مصدر جيد للحديد وفيتامين K",
        "benefit": "مفيدة جداً لدعم الدم والعظام بسعرات قليلة جداً",
        "best_time": "أي وقت مع الوجبات الرئيسية",
        "highlight_en": "A good source of iron and vitamin K",
        "benefit_en": "Very beneficial for blood and bone health with very few calories",
        "best_time_en": "Any time, with main meals"
    },
    "خس": {
        "calories": 15, "protein": 1.4, "carbs": 2.9, "fats": 0.2,
        "highlight": "سعرات شبه معدومة، غالباً مية وألياف",
        "benefit": "مفيد للشبع بدون سعرات، خيار جيد للتنشيف",
        "best_time": "أي وقت، مع السلطات والساندويتشات",
        "highlight_en": "Almost zero calories, mostly water and fiber",
        "benefit_en": "Good for fullness without extra calories, a good option when cutting",
        "best_time_en": "Any time, with salads and sandwiches"
    },
    "بسلة": {
        "calories": 81, "protein": 5.4, "carbs": 14, "fats": 0.4,
        "highlight": "أعلى من باقي الخضار في البروتين والكارب",
        "benefit": "مفيدة، بروتين نباتي وألياف كويسة",
        "best_time": "وجبة غدا أو عشا",
        "highlight_en": "Higher in protein and carbs than most vegetables",
        "benefit_en": "Beneficial; provides decent plant protein and fiber",
        "best_time_en": "At lunch or dinner"
    },
    "فاصوليا": {
        "calories": 127, "protein": 8.7, "carbs": 23, "fats": 0.5,
        "highlight": "غنية بالبروتين النباتي والألياف",
        "benefit": "مفيدة جداً، بديل بروتين نباتي قوي ومشبع",
        "best_time": "وجبة غدا أو عشا",
        "highlight_en": "Rich in plant protein and fiber",
        "benefit_en": "Very beneficial; a strong, filling plant protein alternative",
        "best_time_en": "At lunch or dinner"
    },
    "لوبيا": {
        "calories": 116, "protein": 7.7, "carbs": 21, "fats": 0.5,
        "highlight": "قريبة جداً من الفاصوليا في القيمة الغذائية",
        "benefit": "مفيدة، بروتين نباتي وألياف عالية",
        "best_time": "وجبة غدا أو عشا",
        "highlight_en": "Very close to beans in nutritional value",
        "benefit_en": "Beneficial; good plant protein and high fiber",
        "best_time_en": "At lunch or dinner"
    },
    "كوسة": {
        "calories": 17, "protein": 1.2, "carbs": 3.1, "fats": 0.3,
        "highlight": "سعرات قليلة جداً، غالباً مية",
        "benefit": "مفيدة للشبع بسعرات قليلة، مناسبة للتنشيف",
        "best_time": "أي وقت مع الوجبات",
        "highlight_en": "Very low calorie, mostly water",
        "benefit_en": "Good for fullness with few calories, suitable for cutting",
        "best_time_en": "Any time, with meals"
    },

    # ---------------- فواكه ----------------
    "موز": {
        "calories": 89, "protein": 1.1, "carbs": 23, "fats": 0.3,
        "highlight": "غني بالبوتاسيوم، من أسرع الفواكه في رفع الطاقة",
        "benefit": "مفيد جداً كمصدر طاقة سريع، يقلل تشنج العضلات",
        "best_time": "قبل أو بعد التمرين مباشرة",
        "highlight_en": "Rich in potassium, one of the fastest fruits for boosting energy",
        "benefit_en": "Very useful as a quick energy source, helps reduce muscle cramps",
        "best_time_en": "Right before or after training"
    },
    "تمر": {
        "calories": 277, "protein": 1.8, "carbs": 75, "fats": 0.2,
        "highlight": "من أعلى الفواكه في السكر الطبيعي والسعرات",
        "benefit": "مفيد بكمية قليلة كطاقة سريعة، مش مناسب بكميات كبيرة في الدايت",
        "best_time": "قبل التمرين أو كبديل صحي للحلويات بكمية محدودة",
        "highlight_en": "One of the highest fruits in natural sugar and calories",
        "benefit_en": "Useful in small amounts for quick energy; not suitable in large quantities while dieting",
        "best_time_en": "Before training, or as a limited healthy substitute for sweets"
    },
    "افوكادو": {
        "calories": 160, "protein": 2, "carbs": 9, "fats": 15,
        "highlight": "أعلى فاكهة في الدهون الصحية (غير مشبعة)",
        "benefit": "مفيد جداً لصحة القلب، ومصدر دهون صحية ممتاز",
        "best_time": "أي وقت، مفيد في وجبة فيها بروتين",
        "highlight_en": "The fruit highest in healthy (unsaturated) fats",
        "benefit_en": "Very good for heart health and an excellent source of healthy fats",
        "best_time_en": "Any time, especially good in a meal with protein"
    },
    "فراولة": {
        "calories": 32, "protein": 0.7, "carbs": 7.7, "fats": 0.3,
        "highlight": "سعرات قليلة جداً مع فيتامين C عالي",
        "benefit": "مفيدة جداً للتنشيف، حلاوة بدون سعرات كتير",
        "best_time": "أي وقت كسناك صحي",
        "highlight_en": "Very low calorie with high vitamin C",
        "benefit_en": "Great for cutting; sweetness without a lot of calories",
        "best_time_en": "Any time as a healthy snack"
    },
    "تفاح": {
        "calories": 52, "protein": 0.3, "carbs": 14, "fats": 0.2,
        "highlight": "غني بالألياف القابلة للذوبان (بكتين)",
        "benefit": "مفيد جداً للشبع والهضم بسعرات معتدلة",
        "best_time": "بين الوجبات كسناك",
        "highlight_en": "Rich in soluble fiber (pectin)",
        "benefit_en": "Very good for fullness and digestion at a moderate calorie cost",
        "best_time_en": "Between meals as a snack"
    },
    "اناناس": {
        "calories": 50, "protein": 0.5, "carbs": 13, "fats": 0.1,
        "highlight": "يحتوي على إنزيم البروميلين المساعد للهضم",
        "benefit": "مفيد، سعرات قليلة نسبياً وغني بفيتامين C",
        "best_time": "بين الوجبات أو بعد وجبة دهنية لمساعدة الهضم",
        "highlight_en": "Contains the enzyme bromelain, which aids digestion",
        "benefit_en": "Beneficial; relatively low calorie and rich in vitamin C",
        "best_time_en": "Between meals or after a fatty meal to help digestion"
    },
    "برتقال": {
        "calories": 47, "protein": 0.9, "carbs": 12, "fats": 0.1,
        "highlight": "من أعلى الفواكه في فيتامين C",
        "benefit": "مفيد جداً لدعم المناعة بسعرات قليلة",
        "best_time": "أي وقت، مفيد بعد المجهود أو في الشتاء",
        "highlight_en": "One of the highest fruits in vitamin C",
        "benefit_en": "Very good for supporting immunity with few calories",
        "best_time_en": "Any time; especially good after exertion or in winter"
    },
    "كيوي": {
        "calories": 61, "protein": 1.1, "carbs": 15, "fats": 0.5,
        "highlight": "أعلى من البرتقال في فيتامين C لكل 100 جرام",
        "benefit": "مفيد جداً للمناعة والهضم",
        "best_time": "أي وقت كسناك",
        "highlight_en": "Higher in vitamin C than orange per 100g",
        "benefit_en": "Very good for immunity and digestion",
        "best_time_en": "Any time as a snack"
    },
    "توت": {
        "calories": 57, "protein": 0.7, "carbs": 14, "fats": 0.3,
        "highlight": "من أعلى الفواكه في مضادات الأكسدة",
        "benefit": "مفيد جداً، سعرات قليلة وفايدة عالية لمضادات الأكسدة",
        "best_time": "أي وقت كسناك صحي",
        "highlight_en": "One of the fruits highest in antioxidants",
        "benefit_en": "Very beneficial; low calorie with high antioxidant value",
        "best_time_en": "Any time as a healthy snack"
    },
    "بطيخ": {
        "calories": 30, "protein": 0.6, "carbs": 8, "fats": 0.2,
        "highlight": "92% منه مية، سعرات قليلة جداً",
        "benefit": "مفيد للترطيب في الصيف بسعرات قليلة جداً",
        "best_time": "بين الوجبات في الجو الحر",
        "highlight_en": "92% water, very low in calories",
        "benefit_en": "Good for hydration in summer with very few calories",
        "best_time_en": "Between meals in hot weather"
    },
    "مانجو": {
        "calories": 60, "protein": 0.8, "carbs": 15, "fats": 0.4,
        "highlight": "غني بفيتامين A وC نسبياً عن باقي الفواكه",
        "benefit": "مفيد، بس سكره أعلى من فواكه زي الفراولة فخد بالك من الكمية في الدايت",
        "best_time": "بين الوجبات، أو قبل التمرين بكمية معتدلة",
        "highlight_en": "Relatively rich in vitamin A and C compared to other fruits",
        "benefit_en": "Beneficial, but its sugar is higher than fruits like strawberry, so watch the portion while dieting",
        "best_time_en": "Between meals, or before training in moderate amounts"
    },
    "عنب": {
        "calories": 69, "protein": 0.7, "carbs": 18, "fats": 0.2,
        "highlight": "سكر طبيعي مرتفع نسبياً مقارنة بفواكه التنشيف",
        "benefit": "مفيد بكمية معتدلة، غني بمضادات الأكسدة (خصوصاً العنب الأحمر)",
        "best_time": "كسناك بكمية محدودة، أو قبل التمرين",
        "highlight_en": "Relatively high natural sugar compared to cutting-friendly fruits",
        "benefit_en": "Beneficial in moderate amounts, rich in antioxidants (especially red grapes)",
        "best_time_en": "As a limited-portion snack, or before training"
    },
}

def handle(user_input, entity, is_short_func, user_data={}, lang="ar"):
    """الـ handler الخاص بـ food_details"""
    if lang == "en":
        if not entity:
            return "Which food exactly do you want the nutritional value for? 🍽️"
        entity_en = FOOD_NAMES_EN.get(entity, entity)
        if is_short_func(user_input):
            return f"Do you want to know the nutritional value of {entity_en}? 🍽️"

        data = FOOD_DETAILS_DATA.get(entity)
        if not data:
            return f"Sorry, nutritional data for {entity_en} isn't available yet 🙏"

        return (
            f"Sure 🍽️ Nutritional value per 100g of {entity_en}:\n\n"
            f"🔥 Calories: {data['calories']} kcal\n"
            f"💪 Protein: {data['protein']} g\n"
            f"🌾 Carbs: {data['carbs']} g\n"
            f"🥑 Fats: {data['fats']} g\n\n"
            f"⭐ Highlight: {data['highlight_en']}\n"
            f"✅ Benefit: {data['benefit_en']}\n"
            f"⏰ Best time to eat: {data['best_time_en']}"
        )

    if not entity:
        return "عايز تعرف القيمة الغذائية لعنصر إيه بالظبط؟ 🍽️"
    if is_short_func(user_input):
        return f"هل عايز تعرف القيمة الغذائية لـ {entity}؟ 🍽️"

    data = FOOD_DETAILS_DATA.get(entity)
    if not data:
        return f"معلش، البيانات الغذائية لـ {entity} مش متوفرة عندي دلوقتي 🙏"

    return (
        f"تمام 🍽️ القيمة الغذائية لكل 100 جرام من {entity}:\n\n"
        f"🔥 السعرات: {data['calories']} سعرة\n"
        f"💪 البروتين: {data['protein']} جرام\n"
        f"🌾 الكارب: {data['carbs']} جرام\n"
        f"🥑 الدهون: {data['fats']} جرام\n\n"
        f"⭐ يتميز بـ: {data['highlight']}\n"
        f"✅ الفايدة: {data['benefit']}\n"
        f"⏰ أنسب وقت للأكل: {data['best_time']}"
    )
