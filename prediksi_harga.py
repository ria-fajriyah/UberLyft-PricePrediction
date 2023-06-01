import pickle
import streamlit as st

model = pickle.load(open('prediksi_harga.sav', 'rb'))

st.title("Prediksi Harga Taksi")

# Membagi visualisasi menjadi 2 kolom
col1, col2 = st.columns(2)

with col1:
    hour = st.number_input('input jam pemesanan (0-23)')
with col2:
    day = st.number_input('input hari pemesanan (1-30)')
with col1:
    distance = st.number_input('input jarak perjalanan dalam mil')
with col2:
    short_summary = st.selectbox('input cuaca saat pemesanan', (0 Clear, 1 Drizzle, 2 Foggy, 3 Light Rain, 4 Mostly Cloudy, 5 Overcast, 6 Party Cloudy, 7 Possible Drizzle, 8 Rain))
with col1:
    cab_type = st.selectbox('input jenis taksi', (0 Lyft, 1 Uber))
with col2:
    name = st.selectbox('input jenis mobil', (0 Black, 1 Black SUV, 2 Lux, 3 Lux Black, 4 Lux Black XL, 5 Lyft, 6 Lyft XL, 7 Shared, 8 Taxi, 9 UberPool, 10 UberX, 11 UberXL, 12 WAF))
with col1:
    surge_multiplier = st.selectbox('input pengganda tarif', (1.00, 1.25, 1.50, 1.75, 2.00, 2.50, 3.00 ))

predict = ''

if st.button("Prediksi Harga"):
    predict = model.predict(
        [[hour, day, distance, short_summary, cab_type, name, surge_multiplier]]
    )
    st.write("Prediksi Harga Taksi dalam USD : ", predict)