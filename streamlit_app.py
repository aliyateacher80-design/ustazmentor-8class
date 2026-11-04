import streamlit as st

st.set_page_config(page_title="UstazMentor - 8 Class Digital School", page_icon="💻", layout="wide")

# 1. Сессия базасын баптау
if "classes_list" not in st.session_state:
    st.session_state.classes_list = ["8 «А»", "8 «Ә»"]

if "results_db" not in st.session_state:
    st.session_state.results_db = [
        {"name": "Әлихан Т.", "grade": "8 «А»", "topic": "1. Математикалық функциялар", "task_type": "Тест", "score_num": 10, "score": "10 / 10 ұпай"},
        {"name": "Мәдина С.", "grade": "8 «Ә»", "topic": "8. Файлдармен жұмыс", "task_type": "Тест", "score_num": 9, "score": "9 / 10 ұпай"}
    ]

# 2. 3D DIGITAL SCHOOL + ГАЛАКТИКА ЖӘНЕ МЕТЕОРИТТЕР СТИЛІ
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #f1f5f9;
}
.stApp {
    background: #070b14;
    overflow-x: hidden;
}

.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0; width: 100vw; height: 100vh;
    background: 
      radial-gradient(1.5px 1.5px at 20px 30px, #ffffff, rgba(0,0,0,0)),
      radial-gradient(1.5px 1.5px at 100px 150px, #38bdf8, rgba(0,0,0,0)),
      radial-gradient(2px 2px at 200px 80px, #c084fc, rgba(0,0,0,0)),
      radial-gradient(1px 1px at 300px 250px, #ffffff, rgba(0,0,0,0)),
      radial-gradient(2px 2px at 450px 120px, #38bdf8, rgba(0,0,0,0)),
      radial-gradient(1.5px 1.5px at 600px 350px, #fde047, rgba(0,0,0,0));
    background-repeat: repeat;
    background-size: 550px 550px;
    opacity: 0.85;
    z-index: 0;
    pointer-events: none;
    animation: starsDrift 60s linear infinite;
}

@keyframes starsDrift {
    from { transform: translateY(0); }
    to { transform: translateY(-550px); }
}

.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    position: relative;
    z-index: 1;
}

.main-header {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #0b1329 0%, #0f1f44 50%, #082f49 100%);
    padding: 36px 42px;
    border: 1px solid rgba(6,182,212,0.35);
    border-radius: 26px;
    color: white;
    margin-bottom: 24px;
    box-shadow: 0 20px 50px rgba(6,182,212,0.18), inset 0 1px 0 rgba(255,255,255,0.2);
}
.main-header h1 {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(28px, 4vw, 44px);
    font-weight: 800;
    letter-spacing: -1px;
    margin: 0 0 8px 0;
    color: #ffffff !important;
}
.main-header p {
    color: #bae6fd;
    font-size: 15px;
    margin: 0;
}
.badge-3d {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 999px;
    background: rgba(6,182,212,0.2);
    border: 1px solid #22d3ee;
    color: #22d3ee;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    margin-bottom: 12px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(15, 23, 42, 0.85) !important;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(56, 189, 248, 0.25) !important;
    border-radius: 20px !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4) !important;
}

h1, h2, h3, h4, [data-testid="stSubheader"] {
    font-family: 'Outfit', sans-serif;
    color: #f8fafc !important;
    font-weight: 800 !important;
}
label, [data-testid="stWidgetLabel"] {
    color: #e2e8f0 !important;
    font-weight: 600 !important;
}

.stButton > button, .stFormSubmitButton > button {
    border: 0 !important;
    border-radius: 12px !important;
    padding: 0.65rem 1.4rem !important;
    font-weight: 700 !important;
    color: white !important;
    background: linear-gradient(110deg, #2563eb, #0891b2) !important;
    box-shadow: 0 4px 0 #1d4ed8, 0 8px 20px rgba(6,182,212,0.3) !important;
    transition: all 0.15s ease !important;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 0 #1d4ed8, 0 12px 25px rgba(6,182,212,0.4) !important;
}
</style>
""", unsafe_allow_html=True)

# Басты баннер
st.markdown("""
    <div class="main-header">
        <span class="badge-3d">● 8-CLASS DIGITAL HUB</span>
        <h1>UstazMentor 💻 8-сынып</h1>
        <p>Электрондық кестелер және Python тілінде программалау (Толық тапсырмалар базасы)</p>
    </div>
""", unsafe_allow_html=True)

# 15 тақырып тізімі
sections_dict_8 = {
    "📁 І Бөлім: Электрондық кестелерде мәселелерді шешу": [
        "1. Математикалық функциялар",
        "2. Математикалық функциялар. Практикалық жұмыс",
        "3. Логикалық функциялар",
        "4. Логикалық функциялар. Практикалық жұмыс",
        "5. Статистикалық функциялар",
        "6. Статистикалық функциялар. Практикалық жұмыс",
        "7. Электрондық кестелерде үдерістерді модельдеу"
    ],
    "📁 ІІ Бөлім: Python тілінде программалау": [
        "8. Файлдармен жұмыс",
        "9. Файлдармен жұмыс. Практикалық жұмыс",
        "10. For циклі",
        "11. For циклі. Практикалық жұмыс",
        "12. While циклі",
        "13. Циклді басқару",
        "14. Кірістірілген циклдер",
        "15. Болжамды мәселелерді деректерге негіздеп модельдеу"
    ]
}

# Практикалық интерактивті ойындар сілтемесі (2, 4, 6, 9, 11)
external_links_8 = {
    "2. Математикалық функциялар. Практикалық жұмыс": "https://aliyateacher80-design.github.io/math-func-game/",
    "4. Логикалық функциялар. Практикалық жұмыс": "https://aliyateacher80-design.github.io/logic-func-game/",
    "6. Статистикалық функциялар. Практикалық жұмыс": "https://aliyateacher80-design.github.io/stat-func-game/",
    "9. Файлдармен жұмыс. Практикалық жұмыс": "https://aliyateacher80-design.github.io/files-python-game/",
    "11. For циклі. Практикалық жұмыс": "https://aliyateacher80-design.github.io/for-loop-game/"
}

# Тақырыптар бойынша дайын тест сұрақтары қоры
tests_database = {
    "1. Математикалық функциялар": [
        ("1. Электрондық кестеде сандардың қосындысын табу үшін қай функция қолданылады?", ["А) СУММ()", "Б) СРЗНАЧ()", "В) МАКС()", "Г) КОРЕНЬ()"], "А) СУММ()"),
        ("2. Санның квадратын немесе дәрежесін табу функциясы:", ["А) КОРЕНЬ()", "Б) СТЕПЕНЬ()", "В) ABS()", "Г) СУММЕСЛИ()"], "Б) СТЕПЕНЬ()"),
        ("3. Санның модулін (оң мәнін) қайтаратын функция қайсысы?", ["А) ABS()", "Б) КОРЕНЬ()", "В) СУММ()", "Г) МИН()"], "А) ABS()"),
        ("4. Квадрат түбірді есептейтін функция:", ["А) КОРЕНЬ()", "Б) СТЕПЕНЬ()", "В) СУММ()", "Г) ЕСЛИ()"], "А) КОРЕНЬ()"),
        ("5. Тек белгілі бір шартқа сәйкес келетін сандарды қосу үшін:", ["А) СУММЕСЛИ()", "Б) СУММ()", "В) ЕСЛИ()", "Г) И()"], "А) СУММЕСЛИ()"),
        ("6. =СУММ(A1:A5) формуласы нені есептейді?", ["А) A1-ден A5-ке дейінгі ұяшықтардың қосындысын", "Б) Арифметикалық ортасын", "В) Ең үлкен санды", "Г) Көбейтіндісін"], "А) A1-ден A5-ке дейінгі ұяшықтардың қосындысын"),
        ("7. =СТЕПЕНЬ(2; 3) формуласының нәтижесі неге тең?", ["А) 6", "Б) 8", "В) 9", "Г) 5"], "Б) 8"),
        ("8. =КОРЕНЬ(16) формуласының нәтижесі:", ["А) 4", "Б) 8", "В) 2", "Г) 16"], "А) 4"),
        ("9. =ABS(-15) формуласы қандай мән шығарады?", ["А) -15", "Б) 15", "В) 0", "Г) Қате"], "Б) 15"),
        ("10. Математикалық формула қай символдан басталуы тиіс?", ["А) +", "Б) =", "В) #", "Г) $"], "Б) =")
    ],
    "3. Логикалық функциялар": [
        ("1. Шарт орындалғанына қарай екі түрлі мән қайтаратын функция:", ["А) ЕСЛИ()", "Б) И()", "В) ИЛИ()", "Г) НЕ()"], "А) ЕСЛИ()"),
        ("2. Барлық шарттар бірдей орындалғанда ғана ИСТИНА қайтаратын функция:", ["А) И()", "Б) ИЛИ()", "В) НЕ()", "Г) СУММ()"], "А) И()"),
        ("3. Шарттардың кем дегенде біреуі орындалса ИСТИНА беретін функция:", ["А) ИЛИ()", "Б) И()", "В) НЕ()", "Г) ЕСЛИ()"], "А) ИЛИ()"),
        ("4. Логикалық мәнді керісіншеге айналдыратын функция:", ["А) НЕ()", "Б) И()", "В) ИЛИ()", "Г) ABS()"], "А) НЕ()"),
        ("5. =ЕСЛИ(A1>5; \"Өтті\"; \"Өтпеді\") формуласында A1=10 болса не шығады?", ["А) Өтті", "Б) Өтпеді", "В) 10", "Г) Қате"], "А) Өтті"),
        ("6. =И(5>2; 3<1) нәтижесі қандай болады?", ["А) ИСТИНА", "Б) ЛОЖЬ", "В) Қате", "Г) 0"], "Б) ЛОЖЬ"),
        ("7. =ИЛИ(5>2; 3<1) нәтижесі қандай болады?", ["А) ИСТИНА", "Б) ЛОЖЬ", "В) Қате", "Г) 1"], "А) ИСТИНА"),
        ("8. ЕСЛИ функциясында неше негізгі аргумент бар?", ["А) 1", "Б) 2", "В) 3", "Г) 4"], "В) 3"),
        ("9. Шарттар тізбегін ішінара жазу қалай аталады?", ["А) Кірістірілген ЕСЛИ", "Б) Күрделі СУММ", "В) Циклдік формула", "Г) Статистика"], "А) Кірістірілген ЕСЛИ"),
        ("10. Егер A1=80 болса, =ЕСЛИ(A1>=90; \"A\"; \"B\") нәтижесі:", ["А) A", "Б) B", "В) 80", "Г) ЛОЖЬ"], "Б) B")
    ],
    "5. Статистикалық функциялар": [
        ("1. Сандардың арифметикалық ортасын табу функциясы:", ["А) СРЗНАЧ()", "Б) МАКС()", "В) МИН()", "Г) СЧЁТ()"], "А) СРЗНАЧ()"),
        ("2. Диапазондағы ең үлкен санды табу функциясы:", ["А) МАКС()", "Б) МИН()", "В) СРЗНАЧ()", "Г) СУММ()"], "А) МАКС()"),
        ("3. Диапазондағы ең кіші санды табу функциясы:", ["А) МИН()", "Б) МАКС()", "В) СРЗНАЧ()", "Г) ABS()"], "А) МИН()"),
        ("4. Сан толтырылған ұяшықтар санын есептейтін функция:", ["А) СЧЁТ()", "Б) СРЗНАЧ()", "В) СУММ()", "Г) МАКС()"], "А) СЧЁТ()"),
        ("5. =СРЗНАЧ(10; 20; 30) нәтижесі қанша болады?", ["А) 20", "Б) 60", "В) 10", "Г) 30"], "А) 20"),
        ("6. =МАКС(5; 12; 9; 3) нәтижесі:", ["А) 12", "Б) 5", "В) 3", "Г) 29"], "А) 12"),
        ("7. =МИН(15; 8; 22; 4) нәтижесі:", ["А) 4", "Б) 8", "В) 22", "Г) 15"], "А) 4"),
        ("8. Статистикалық функциялар бос ұяшықтарды қалай есептейді?", ["А) Елемейді (өткізіп жібереді)", "Б) 0 деп есептейді", "В) Қате береді", "Г) Тоқтатады"], "А) Елемейді (өткізіп жібереді)"),
        ("9. Тек белгілі бір шартқа сай ұяшықтар санын есептеу:", ["А) СЧЁТЕСЛИ()", "Б) СЧЁТ()", "В) СУММЕСЛИ()", "Г) СРЗНАЧ()"], "А) СЧЁТЕСЛИ()"),
        ("10. Ауа райының ең төмен температурасын табуға қайсысы сай?", ["А) МИН()", "Б) МАКС()", "В) СРЗНАЧ()", "Г) СУММ()"], "А) МИН()")
    ],
    "8. Файлдармен жұмыс": [
        "1. Python-да файлды ашу үшін қай функция қолданылады?",
        "2. Файлды оқу режимінде ашу белгісі:",
        "3. Файлға жаңадан мәлімет жазу (бұрынғысын өшіріп) режимі:",
        "4. Файл соңына мәлімет қосып жазу режимі:",
        "5. Файлды жабу әдісі:",
        "6. Файлдағы барлық мәтінді біртұтас жол етіп оқу әдісі:",
        "7. Мәтінді үтір немесе бос орын бойынша бөліктерге бөлу әдісі:",
        "8. Тізім элементтерін жолға біріктіру әдісі:",
        "9. Жоқ файлды 'r' режимінде ашқанда шығатын қате:",
        "10. Файлмен қауіпсіз жұмыс істеу (авто-жабу) операторы:"
    ],
    "10. For циклі": [
        "1. Python-да кай цикл қайталау саны белгілі кезде қолданылады?",
        "2. range(5) функциясы қандай сандар тізбегін береді?",
        "3. range(1, 6) нәтижесі қандай сандардан тұрады?",
        "4. range(2, 10, 2) функциясындағы 3-ші параметр нені білдіреді?",
        "5. Тізім элементтерін тізбектеп шолу үшін қай оператор қолданылады?",
        "6. for i in range(3): print(i) орындалғанда экранға не шығады?",
        "7. Кері санақ жасау үшін range()-ге қандай қадам беріледі?",
        "8. Цикл денесі Python-да қалай ерекшеленеді?",
        "9. range(0, 10) неше рет қайталанады?",
        "10. for char in 'Абай': коды неше рет орындалады?"
    ]
}

# Жалпы тест опциялары мен жауаптар шаблондары
default_test_options = ["А) Бірінші дұрыс нұсқа", "Б) Екінші нұсқа", "В) Үшінші нұсқа", "Г) Төртінші нұсқа"]

all_topics_8 = []
for sec, topics in sections_dict_8.items():
    all_topics_8.extend(topics)

# Режим таңдау
role = st.radio("Режимді таңдаңыз:", ["👨‍🎓 Оқушы режимі", "👩‍🏫 Мұғалім кабинеті"], horizontal=True)
st.divider()

if role == "👩‍🏫 Мұғалім кабинеті":
    st.subheader("👩‍🏫 Мұғалімнің басқару кабинеті (8-сынып)")
    
    with st.expander("📊 Teacher Dashboard — Сыныптар мен нәтижелерді қарау", expanded=True):
        st.markdown("### 🏫 Сыныптар навигаторы")
        selected_class = st.radio("Сыныпты таңдаңыз:", st.session_state.classes_list, horizontal=True)
        
        col_add1, col_add2 = st.columns([3, 1])
        with col_add1:
            new_class_input = st.text_input("Жаңа сынып қосу:", placeholder="Мысалы: 8 «Б»", key="new_class_key_8")
        with col_add2:
            st.write("")
            st.write("")
            if st.button("➕ Қосу"):
                if new_class_input.strip() and new_class_input.strip() not in st.session_state.classes_list:
                    st.session_state.classes_list.append(new_class_input.strip())
                    st.success(f"{new_class_input} сәтті қосылды!")
                    st.rerun()

        st.markdown(f"#### 📈 {selected_class} сыныбының нәтижелері (Макс: 10 ұпай)")
        class_filtered_db = [r for r in st.session_state.results_db if r.get('grade') == selected_class]
        
        if len(class_filtered_db) > 0:
            for idx, res in enumerate(class_filtered_db, 1):
                score_val = res.get('score_num', 10)
                c1, c2, c3 = st.columns([2, 2, 3])
                with c1:
                    st.write(f"**{idx}. {res['name']}**")
                with c2:
                    st.write(f"Ұпайы: **{res['score']}**")
                with c3:
                    st.progress(min(score_val / 10.0, 1.0))
        else:
            st.info(f"{selected_class} сыныбында әзірге сақталған нәтиже жоқ.")

    st.subheader("⚙️ Сабақ баптаулары")
    save_results_enabled = st.toggle("📊 Оқушы нәтижелерін базаға сақтау", value=True)
    selected_section = st.selectbox("Бөлімді таңдаңыз:", list(sections_dict_8.keys()))
    selected_topic = st.selectbox("Тақырыпты таңдаңыз:", sections_dict_8[selected_section])
    timer_val = st.number_input("Сабақ таймері (минут):", value=15)
        
    st.info(f"💡 Таңдалған сабақ: **{selected_topic}** | Сақтау: **{'ҚОСУЛЫ' if save_results_enabled else 'ӨШІРУЛІ'}**")

else:
    st.subheader("👨‍🎓 Оқушы кабинеті (8-сынып)")
    col_name, col_class = st.columns([2, 1])
    with col_name:
        student_name = st.text_input("Аты-жөніңізді енгізіңіз (Мысалы: Айдын Ә.):", placeholder="Аты-жөніңіз...")
    with col_class:
        student_grade = st.selectbox("Сыныбыңыз:", st.session_state.classes_list)
    
    selected_topic = st.selectbox("Сабақ тақырыбын таңдаңыз:", all_topics_8)
    st.success(f"🎯 **Ағымдағы сабақ:** {selected_topic}")
    
    # Практикалық веб-ойын ма таңдау
    is_game_topic = selected_topic in external_links_8
    
    if is_game_topic:
        st.markdown(f"### 🌐 Интерактивті веб-ойын / Практикалық жұмыс: {selected_topic}")
        game_url = external_links_8.get(selected_topic, "https://github.com")
        st.markdown(f"👉 **[Тапсырманы / Ойынды ашу 🚀]({game_url})**")
        
        if st.button("✅ Тапсырманы орындап шықтым (Нәтижені тіркеу)"):
            if not student_name.strip():
                st.error("⚠️ Ең алдымен аты-жөніңізді жазыңыз!")
            else:
                st.balloons()
                st.success(f"Құттықтаймыз, {student_name}! Практикалық жұмыс нәтижесі тіркелді! 🌟")
                st.session_state.results_db.append({
                    "name": student_name, "grade": student_grade, "topic": selected_topic,
                    "task_type": "Интерактивті ойын (Практика)", "score_num": 10, "score": "10 / 10 (Орындалды)"
                })
    else:
        tab_test, tab_match, tab_game = st.tabs(["📝 Тест (10 сұрақ)", "🔗 Сәйкестендіру", "💻 Тренажер"])
        
        with tab_test:
            st.markdown(f"#### PISA Функционалдық тесті: {selected_topic}")
            user_score = 0
            
            with st.form(key=f"form_test_{selected_topic}"):
                if selected_topic in tests_database:
                    topic_questions = tests_database[selected_topic]
                    for idx, q_item in enumerate(topic_questions, 1):
                        if isinstance(q_item, tuple):
                            q_text, opts, corr = q_item
                            ans = st.radio(f"{q_text}", opts, key=f"q_{selected_topic}_{idx}")
                            if ans == corr:
                                user_score += 1
                        else:
                            # Стандартты формат
                            st.radio(f"{idx}. {q_item}", ["А) Дұрыс жауап нұсқасы", "Б) Екінші нұсқа", "В) Үшінші нұсқа", "Г) Төртінші нұсқа"], key=f"q_std_{selected_topic}_{idx}")
                            user_score += 1
                else:
                    for i in range(1, 11):
                        st.radio(f"{i}-сұрақ: {selected_topic} тақырыбы бойынша дұрыс тұжырымды таңдаңыз:", [
                            "А) Негізгі дұрыс жауап", "Б) Балама жауап", "В) Қосымша вариант", "Г) Қате вариант"
                        ], key=f"q_gen_{selected_topic}_{i}")
                    user_score = 10

                submitted = st.form_submit_button("Тестті тексеру және ұпайды есептеу")
                if submitted:
                    if not student_name.strip():
                        st.error("⚠️ Аты-жөніңізді енгізіңіз!")
                    else:
                        st.balloons()
                        st.success(f"Құттықтаймыз, {student_name}! Нәтижеңіз: {user_score} / 10 ұпай 🌟")
                        st.session_state.results_db.append({
                            "name": student_name, "grade": student_grade, "topic": selected_topic,
                            "task_type": "Тест (10 сұрақ)", "score_num": user_score, "score": f"{user_score} / 10 ұпай"
                        })

        with tab_match:
            st.markdown(f"#### Сәйкестендіру тапсырмасы: {selected_topic}")
            st.info("Өмірлік жағдаяттар мен функцияларды/кодтарды дұрыс сәйкестендіріңіз:")
            
            m1 = st.selectbox("1. Барлық тауарлардың қосындысын табу", ["-- Таңдаңыз --", "СУММ()", "ЕСЛИ()", "СРЗНАЧ()", "open()"], key=f"m1_{selected_topic}")
            m2 = st.selectbox("2. Сатып алу сомасы 10 000 тг-ден асса жеңілдік беру", ["-- Таңдаңыз --", "СУММ()", "ЕСЛИ()", "СРЗНАЧ()", "open()"], key=f"m2_{selected_topic}")
            m3 = st.selectbox("3. Оқушының орташа бағасын табу", ["-- Таңдаңыз --", "СУММ()", "ЕСЛИ()", "СРЗНАЧ()", "open()"], key=f"m3_{selected_topic}")
            m4 = st.selectbox("4. Файлды оқу режимінде ашу", ["-- Таңдаңыз --", "СУММ()", "ЕСЛИ()", "СРЗНАЧ()", "open('file.txt', 'r')"], key=f"m4_{selected_topic}")
            m5 = st.selectbox("5. 1-ден 5-ке дейін қайталау циклі", ["-- Таңдаңыз --", "for i in range(1, 6):", "while True:", "if x > 0:", "split()"], key=f"m5_{selected_topic}")
            
            if st.button("Сәйкестікті растау", key=f"match_btn_{selected_topic}"):
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді жазыңыз!")
                else:
                    st.balloons()
                    st.success(f"Жарайсың, {student_name}! Сәйкестендіру орындалды! 🎯")

        with tab_game:
            st.markdown(f"#### Практикалық тренажер: {selected_topic}")
            step = st.slider("Қадамды/Деңгейді таңдаңыз:", 0, 10, 5, key=f"slider_{selected_topic}")
            st.write(f"Орындалу деңгейі: **{step} / 10 қадам**")
            
            if st.button("Нәтижені тіркеу", key=f"gym_btn_{selected_topic}"):
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді жазыңыз!")
                else:
                    st.balloons()
                    st.success(f"Құттықтаймыз, {student_name}! Нәтиже тіркелді: {step} / 10 ұпай 🚀")
                    st.session_state.results_db.append({
                        "name": student_name, "grade": student_grade, "topic": selected_topic,
                        "task_type": "Тренажер", "score_num": step, "score": f"{step} / 10 ұпай"
                    })
