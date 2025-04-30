import random
import time

# دالة لعرض النص مع توقف مؤقت لزيادة التشويق
def print_pause(text):
    print(text)
    time.sleep(2)

# دالة للحصول على إدخال صحيح من المستخدم بناءً على خيارات محددة
def get_valid_choice(prompt, options):
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return choice
        print("إدخال غير صالح. حاول مرة أخرى.")

# دالة لتحديث صحة اللاعب بناءً على الحدث
def update_health(health, change, action):
    health += change
    if change > 0:
        print_pause(f"{action} واستعدت {change} من صحتك.")
    else:
        print_pause(f"{action} وخسرت {abs(change)} من صحتك.")
    return health

# دالة تجربة الكوخ، قد تكسب أو تخسر صحة
def house(health):
    print_pause("أنت تقترب من الكوخ بحذر، والظلام يعم المكان، والرياح تعصف بالأشجار.")
    event = random.choice(["تسمع صوت غريب", "تجد باب مفتوح", "لا شيء يحدث"])
    print_pause(f"عند وصولك، {event}.")

    if event == "تسمع صوت غريب":
        print_pause("فجأة، يظهر مخلوق صغير ذو عيون حمراء كالجمرة! يركض نحوك بسرعة!")
        health = update_health(health, -random.randint(5, 10), "تعرضت لهجوم مفاجئ")
    elif event == "تجد باب مفتوح":
        print_pause("أنت تقترب من الباب المهدم، لكن فجأة ينفتح تلقائيًا وكأن الكوخ يدعوك للدخول.")
        print_pause("داخل الكوخ، تجد جرعة غامضة تتوهج بضوء أخضر شاحب. هل تجرؤ على تناولها؟")
        health = update_health(health, random.randint(5, 15), "تناولت الجرعة")
    else:
        print_pause("الكوخ هادئ تمامًا، لكنك تشعر بوجود شيء غير مرئي يراقبك. قررت أخذ نفس عميق وواصلت السير.")

    print(f"\nصحتك الحالية بعد الكوخ: {health}")
    return health

# دالة تجربة القلعة، مغامرة فيها خطر وفرص للشفاء
def castle(health):
    print_pause("أنت تتجه نحو القلعة المهجورة. الجدران متهالكة والنوافذ مغلقة بحواجز من الحديد.")
    event = random.choice(["ترى ضوء خافت", "تسمع صوت صرير الباب", "تجد تمثال غريب"])
    print_pause(f"عند الاقتراب، {event}.")

    if event == "ترى ضوء خافت":
        print_pause("ضوء غريب ينبعث من داخل القلعة، يرقبك بحذر وكأنما يراقبك. هل هو فخ؟")
        health = update_health(health, -random.randint(5, 10), "فجأة، شعاع ضوء حارق يصيبك")
    elif event == "تسمع صوت صرير الباب":
        print_pause("القلعة تفتح أبوابها بعنف وكأنها على استعداد للاحتضان. داخلها، تجد جرعة سحرية.")
        health = update_health(health, random.randint(5, 10), "تناولت الجرعة السحرية")
    else:
        print_pause("التمثال في زاوية القلعة يبتسم لك، لكن ابتسامته تبدو غريبة كأنما تستهزئ بك. تصعد نحوها بحذر.")

    print(f"\nصحتك الحالية بعد القلعة: {health}")
    return health

# دالة التحدي النهائي مع الوحش
def final_challenge(health):
    monster_health = 100  # صحة الوحش الابتدائية

    print("\nأمامك الوحش الضخم الذي يحرس المدخل... رائحته كريهة وأعمدته مغطاة بالدماء.")
    print_pause("الوحش ينظر إليك بعينين مليئتين بالكراهية، ويبدأ الزئير الذي يهز الأرض.")

    while True:
        print(f"\nصحتك: {health}    صحة الوحش: {monster_health}")
        action = input("\nماذا ستفعل؟\n1- الهجوم\n2- الدفاع\nاختر: ")

        if action == "1":
            print("تجمع كل قوتك وتهجم على الوحش، عينيك تشتعل بالغضب!")
            damage_to_monster = random.randint(10, 20)
            monster_health -= damage_to_monster
            print(f"سببت {damage_to_monster} ضررًا للوحش، لكن الوحش يضحك ضحكة مرعبة!")

            if monster_health > 0:
                monster_damage_to_you = random.randint(5, 15)
                health = update_health(health, -monster_damage_to_you, "الوحش يهاجمك")
        elif action == "2":
            print("تتخذ وضعية الدفاع وأنت مستعد لتحمل الصدمات.")
            reduced_damage = random.randint(2, 8)
            health = update_health(health, -reduced_damage, "الوحش يضربك بقوة")
        else:
            print("هذا ليس خيارًا صحيحًا. حاول مجددًا.")
            continue

        # التحقق من الفوز أو الخسارة
        if health <= 0:
            print("\nلقد خسرت كل صحتك. الوحش سحقك!")
            break
        elif monster_health <= 0:
            print("\nلقد هزمت الوحش! أنت بطل المغامرة!")
            break

    return health

# دالة تشغيل اللعبة الأساسية
def play_game():
    health = 100
    name = input("أدخل اسمك: ")
    print_pause(f"مرحباً {name}, مرحبًا بك في مغامرة الغابة المسحورة!")
    print_pause("استعد لمغامرتك...")

    stage = 1  # المرحلة الأولى

    while True:
        print(f"\nصحتك الحالية: {health}")

        # المرحلة الأولى: اختيار الكوخ أو القلعة
        if stage == 1:
            choose = get_valid_choice(
                "\nأمامك طريقان:\n1- التوجه نحو الكوخ\n2- التوجه نحو القلعة\nاختر: ", ["1", "2"]
            )

            if choose == "1":
                health = house(health)
                stage = 2
            elif choose == "2":
                health = castle(health)
                stage = 2

        # المرحلة الثانية: التحدي النهائي
        elif stage == 2:
            print_pause("\nبعد مغامرتك، تجد باباً ضخماً يؤدي إلى التحدي النهائي...")
            health = final_challenge(health)
            break

        if health <= 0:
            print_pause("\nلقد انتهت صحتك. خسرت المغامرة.")
            break

    # ملخص النتيجة
    if health > 100:
        print("لقد خرجت أقوى مما كنت. مغامرة ناجحة.")
    elif health > 0:
        print("نجوت من المغامرة رغم الجروح. أحسنت.")
    else:
        print("نهاية محزنة. حاول مرة أخرى.")

# تشغيل اللعبة بشكل متكرر حسب رغبة المستخدم
while True:
    play_game()
    confirm = get_valid_choice("\nهل ترغب في اللعب مرة أخرى؟ (نعم/لا): ", ["نعم", "لا"])
    if confirm == "لا":
        print_pause("شكرًا للعب! إلى اللقاء.")
        break
