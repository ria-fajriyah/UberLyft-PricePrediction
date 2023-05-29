import pickle
import streamlit as st

model = pickle.load(open('prediksi_harga.sav', 'rb'))

st.title("Prediksi Harga Taksi")

hour = st.number_input('Input Jam Pemesanan')
day = st.number_input('Input Hari Pemesanan')
distance = st.number_input('Input Jarak Perjalanan')
short_summary = st.number_input('Input Cuaca saat Pemesanan')
cab_type = st.number_input('Input Jenis Taksi')
name = st.number_input('Input Jenis Mobil')
surge_multiplier = st.number_input('Input Pengganda Tarif')

predict = ''

if st.button("Prediksi Harga"):
    predict = model.predict(
        [[hour, day, distance, short_summary, cab_type, name, surge_multiplier]]
    )
    st.write("Prediksi Harga Taksi dalam USD : ", predict)