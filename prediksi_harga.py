import pickle
import streamlit as st

model = pickle.load(open('prediksi_harga.sav', 'rb'))

st.title("Prediksi Harga Taksi")

# Membagi visualisasi menjadi 2 kolom
col1, col2 = st.columns(2)

with col1:
    hour = st.number_input('Input Jam Pemesanan')
with col2:
    day = st.number_input('Input Hari Pemesanan')
with col1:
    distance = st.number_input('Input Jarak Perjalanan')
with col2:
    short_summary = st.number_input('Input Cuaca saat Pemesanan')
with col1:
    cab_type = st.number_input('Input Jenis Taksi')
with col2:
    name = st.number_input('Input Jenis Mobil')
with col1:
    surge_multiplier = st.number_input('Input Pengganda Tarif')

predict = ''

if st.button("Prediksi Harga"):
    predict = model.predict(
        [[hour, day, distance, short_summary, cab_type, name, surge_multiplier]]
    )
    st.write("Prediksi Harga Taksi dalam USD : ", predict)