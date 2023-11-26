import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import altair as alt

titulos_pestanas = ['Página principal', 'Nacional', 'Internacional','Departamentos','Países','Sobre nosotras']
pestaña1, pestaña2, pestaña3, pestaña4, pestaña5, pestaña6 = st.tabs(titulos_pestanas)

with pestaña1:
    st.title('Análisis de Población identificada con DNI de mayor de edad por condición de donante de órganos')
    st.write("Texto sobre donación de órganos")
    st.write("")
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.button("Nacional", type="secondary")
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.bar_chart(chart_data)
        with right_column:
            st.button("Internacional", type="secondary") 
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.bar_chart(chart_data)
            st.caption('Los datos de este gráfico no están actualizados a la fecha actual.')

with pestaña2:
    st.title("Condición de donante de órganos a nivel nacional")
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.button("2022", type="secondary")
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.bar_chart(chart_data)
        with right_column:
            st.button("2023", type="secondary")
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.bar_chart(chart_data)
            st.caption("Los datos de este gráfico no están actualizados a la fecha actual.")

with pestaña3:
    st.title ("Condición de donante de órganos a nivel internacional")
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.button(" 2022", type="secondary")
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.bar_chart(chart_data)
        with right_column:
            st.button(" 2023", type="secondary")
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.bar_chart(chart_data)
            st.caption("Los datos de este gráfico no están actualizados a la fecha actual.")

with pestaña4:
    st.title("Condición de donante de órganos por departamentos")
    option0 = st.selectbox(
        "Elige un año",
        ("2022","2023"))
    if option0 == "2022":
        lista1 = ["Áncash","Amazonas","Apurímac","Arequipa","Ayacucho","Cajamarca","Callao","Cusco","Huánuco","Huancavelica","Ica","Junín","La Libertad","Lambayeque","Lima","Loreto","Madre de Dios","Moquegua","Pasco","Piura","Puno","San Martín","Tacna","Tumbes","Ucayali"]
        lista2 = [330327,37044,52656,569256,100173,194589,480840,295122,93783,39540,294624,184767,575133,338070,4796229,128385,62340,57219,43278,417759,116577,160161,84144,50082,126999]
        chart_data = pd.DataFrame(
            {"Departamento": list(lista1[0]), "Cantidad": list(lista2[0])}
        )
        st.bar_chart(
            chart_data, x="Departamento", y=["Cantidad"]
        )
        st.caption("Los datos de este gráfico no están actualizados a la fecha actual.")
        st.write("")
        st.write("El gráfico muestra la cantidad de personas que aceptaron donar sus órganos durante el año 2022.")
    elif option0 == "2023":
        lista1 = ["Áncash","Amazonas","Apurímac","Arequipa","Ayacucho","Cajamarca","Callao","Cusco","Huánuco","Huancavelica","Ica","Junín","La Libertad","Lambayeque","Lima","Loreto","Madre de Dios","Moquegua","Pasco","Piura","Puno","San Martín","Tacna","Tumbes","Ucayali"]        
        lista2 = [330327,37044,52656,569256,100173,194589,480840,295122,93783,39540,294624,184767,575133,338070,4796229,128385,62340,57219,43278,417759,116577,160161,84144,50082,126999]
        chart_data = pd.DataFrame(
            {"Departamento": list(lista1[:24]), "Cantidad": list(lista2[:24])}
        )
        st.bar_chart(
            chart_data, x="Departamento", y=["Cantidad"]
        )
        st.caption("Los datos de este gráfico no están actualizados a la fecha actual.")
        st.write("")
        st.write("El gráfico muestra la cantidad de personas que aceptaron donar sus órganos durante el año 2023.")

with pestaña5:
    st.title("Condición de donante de órganos por países")
    option3 = st.selectbox(
        "Elige un continente",
        ("África","América","Asia","Europa","Oceanía"))
    if option3 == "África":
        option5 = st.selectbox(
                "Elige un país",
                ("Argelia","Costa de Marfil"))
    elif option3 == "América":
        option5 = st.selectbox(
            "Elige un país",
            ("Antillas Holandesas","Argentina"))
    elif option3 == "Asia":
        option5 = st.selectbox(
            "Elige un país",
            ("Catar","India"))
    elif option3 == "Europa":
        option5 = st.selectbox(
            "ELige un país",
            ("Alemania","Austria"))
    elif option3 == "Oceanía":
        option5 = st.selectbox(
            "Elige un país",
            ("Australia","Nueva Zelanda"))
    option4 = st.selectbox(
        "Elige un año",
        (" 2022","2023"))

with pestaña6:
    st.title("Sobre nosotras")

st.link_button("Para más información de click aquí", "https://www.datosabiertos.gob.pe/dataset/reniec-poblaci%C3%B3n-identificada-con-dni-de-mayor-de-edad-por-condici%C3%B3n-de-donante-de-%C3%B3rganos")
