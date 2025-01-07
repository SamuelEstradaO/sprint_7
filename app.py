import streamlit as st
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go

car_data = pd.read_csv('vehicles_us.csv')
st.header('Analisis de venta de coches')
st.subheader('Datos de los vehiculos en venta')
data = go.Figure(data=[go.Table(header=dict(values=list(car_data.columns)),
                                cells=dict(values=[car_data[column] for column in car_data.columns]))
                       ])
st.write(data)
hist_checkbox = st.checkbox('Construir histograma')  # crear un botón

if hist_checkbox:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    histogram_fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(histogram_fig, use_container_width=True)

scatter_checkbox = st.checkbox('Construir grafico de dispersion')

if scatter_checkbox:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    scatter_fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(scatter_fig, use_container_width=True)
