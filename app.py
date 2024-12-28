import streamlit as st
import pickle
import numpy as np

# Saqlangan modelni yuklash
model = pickle.load(open("random_forest_model.pkl", "rb"))

# Streamlit interfeysi
st.set_page_config(page_title="Tarmoq Hujumlarini Aniqlash", layout="centered")

# Sarlavha va kirish matni
st.markdown(
    """
    <div style="background-color: #f63366; padding: 10px; border-radius: 10px;">
        <h1 style="color: white; text-align: center;">Tarmoq Hujumlarini Aniqlash Tizimi</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("Quyidagi ma'lumotlarni kiriting va tizim hujum bor-yo'qligini aniqlaydi.")

# Ma'lumotlarni ikki ustunga bo'lish
col1, col2 = st.columns(2)

with col1:
    duration = st.number_input("Duration", min_value=0, help="Ushbu sessiyaning davomiyligi (soniya).")
    src_bytes = st.number_input("Source Bytes", min_value=0, help="Manba kompyuterdan uzatilgan baytlar.")
    dst_bytes = st.number_input("Destination Bytes", min_value=0, help="Qabul qiluvchi kompyuterga yuborilgan baytlar.")

with col2:
    wrong_fragment = st.number_input("Wrong Fragment", min_value=0, help="Noto'g'ri fragmentlar soni.")
    hot = st.number_input("Hot", min_value=0, help="Hot aloqalar soni.")

# Qo'shimcha ustunlarni standart qiymatlar bilan to'ldirish
default_values = [0] * (118 - 5)
features = [duration, src_bytes, dst_bytes, wrong_fragment, hot] + default_values

# Bashorat tugmasi
if st.button("Bashorat qilish"):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)[0]
    
    if prediction == 0:
        st.success("✅ Natija: Normal faoliyat")
    else:
        st.error("🚨 Natija: Hujum aniqlangan!")

# Quyida qo'shimcha ma'lumotlar
st.markdown(
    """
    <hr>
    <div style="text-align: center;">
        <p style="color: gray;">© 2024 Tarmoq Hujumlarini Aniqlash Tizimi Norov Beksulton tomonidan yaratildi</p>
    </div>
    """,
    unsafe_allow_html=True,
)
