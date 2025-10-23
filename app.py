import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado
st.header("🚗 Dashboard de Anuncios de Vehículos")

# Cargar datos
car_data = pd.read_csv("vehicles_us.csv")

# Botón para histograma
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Creación de un histograma para la columna `odometer`")
    fig = px.histogram(car_data, x="odometer", nbins=40,
                       title="Distribución de kilometraje (odometer)")
    st.plotly_chart(fig, use_container_width=True)

# Botón para scatter plot
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Gráfico de dispersión `price` vs `odometer`")
    fig = px.scatter(car_data, x="odometer", y="price",
                     color="condition",
                     title="Precio vs Kilometraje según condición")
    st.plotly_chart(fig, use_container_width=True)
