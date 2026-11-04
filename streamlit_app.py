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
        <p>Электрондық кестелер және Python тілінде программалау (Интерактивті ойындар мен модульдер)</p>
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

# Сіз өз ойындарыңыздың сілтемелерін осы жерге жаза аласыз (GitHub Pages немесе басқа платформалар)
external_links_8 = {
    "2. Математикалық функциялар. Практикалық жұмыс": "https://aliyateacher80-design.github.io/math-func-game/",
    "4. Логикалық функциялар. Практикалық жұмыс": "https://aliyateacher80-design.github.io/logic-func-game/",
    "6. Статистикалық функциялар. Практикалық жұмыс": "https://aliyateacher80-design.github.io/stat-func-game/",
    "9. Файлдармен жұмыс. Практикалық жұмыс": "https://aliyateacher80-design.github.io/files-python-game/",
    "11. For циклі. Практикалық жұмыс": "https://aliyateacher80-design.github.io/for-loop-game/"
}

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
    
    # 2, 4, 6, 9, 11 тақырыптар автоматты түрде сілтеме арқылы ашылатын ойын болып белгіленеді
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
        # Қалған тақырыптар үшін стандартты қойындылар (Тест, Сәйкестендіру, Тренажер)
        tab_test, tab_match, tab_game = st.tabs(["📝 Тест (10 сұрақ)", "🔗 Сәйкестендіру", "💻 Тренажер"])
        
        with tab_test:
            st.markdown(f"#### Функционалдық тест: {selected_topic}")
            with st.form(key=f"test_8_{selected_topic}"):
                for i in range(1, 11):
                    st.radio(f"{i}-сұрақ: {selected_topic} тақырыбы бойынша дұрыс жауапты таңдаңыз:", [
                        "А) Бірінші нұсқа", "Б) Екінші нұсқа", "В) Үшінші нұсқа", "Г) Төртінші нұсқа"
                    ], key=f"t_{selected_topic}_{i}")
                
                if st.form_submit_button("Тестті тексеру және ұпайды есептеу"):
                    if not student_name.strip():
                        st.error("⚠️ Аты-жөніңізді енгізіңіз!")
                    else:
                        st.balloons()
                        st.success(f"Құттықтаймыз, {student_name}! Нәтижеңіз: 10 / 10 ұпай 🌟")
                        st.session_state.results_db.append({
                            "name": student_name, "grade": student_grade, "topic": selected_topic,
                            "task_type": "Тест (10 сұрақ)", "score_num": 10, "score": "10 / 10 ұпай"
                        })

        with tab_match:
            st.markdown(f"#### Сәйкестендіру тапсырмасы: {selected_topic}")
            for item in ["1. Негізгі элемент", "2. Логикалық оператор", "3. Деректер түрі", "4. Нәтиже", "5. Қорытынды"]:
                st.selectbox(f"{item}:", ["-- Таңдаңыз --", "Вариант А", "Вариант Б", "Вариант В", "Вариант Г"], key=f"m_{selected_topic}_{item}")
            
            if st.button("Сәйкестікті растау", key=f"match_btn_{selected_topic}"):
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді жазыңыз!")
                else:
                    st.balloons()
                    st.success(f"Жарайсың, {student_name}! Сәйкестендіру орындалды! 🎯")

        with tab_game:
            st.markdown(f"#### Практикалық тренажер: {selected_topic}")
            step = st.slider("Қадамды таңдаңыз:", 0, 10, 0, key=f"slider_{selected_topic}")
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
