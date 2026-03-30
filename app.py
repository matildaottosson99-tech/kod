import streamlit as st
import pandas as pd
import pickle

# Ladda modell och kolumner
model = pickle.load(open('car_model.pkl', 'rb'))
model_columns = pickle.load(open('model_columns.pkl', 'rb'))

st.title("Bilpris-prediktor")

# Skapa input-fält
year = st.number_input("Årsmodell", min_value=2000, max_value=2026, value=2018)
mileage = st.number_input("Miltal", value=5000)

# Textval 
brand = st.selectbox("Välj märke", ["Toyota", "Honda", "Ford", "Volkswagen", "BMW"])
fuel = st.selectbox("Bränsletyp", ["Petrol", "Diesel", "Electric"])

# Knappen för att räkna ut priset
if st.button("Beräkna pris"):
    input_df = pd.DataFrame(0, index=[0], columns=model_columns)
    
    # Fyll i de numeriska värdena
    if 'Year' in input_df.columns: input_df['Year'] = year
    if 'Mileage' in input_df.columns: input_df['Mileage'] = mileage
    
    # "Tänd" rätt märke och bränsle
    brand_col = f"Brand_{brand}"
    fuel_col = f"Fuel_Type_{fuel}"
    
    if brand_col in input_df.columns: input_df[brand_col] = 1
    if fuel_col in input_df.columns: input_df[fuel_col] = 1
    
    # Gör prediktionen
    prediction = model.predict(input_df)
    
    st.success(f"Det uppskattade marknadsvärdet är: {prediction[0]:,.0f} kr")