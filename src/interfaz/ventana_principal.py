import sys
import os
# Agrega la ruta de src/ al PATH de Python

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import matplotlib.pyplot as plt
from logica.funciones import cargar_datos, obtener_tipos_ejercicio

def mostrar_ventana_principal():

    #Configurar la página para usar todo el espacio de esta
    st.set_page_config(page_title="FitPlan Analysis", layout="wide")

    #Título de la página
    st.markdown("<h1 style='text-align: center; font-size: 50px;'>FitPlan Analysis</h1>", unsafe_allow_html=True)
    st.write("### Sube tu registro de entrenamientos aquí:")
    archivo = st.file_uploader("Carga tu archivo", type=["csv"], key="file_uploader", label_visibility="collapsed")
    if archivo is not None:
        st.write("Carga exitosa")
    col1, col2 = st.columns([1, 3])
    flag1 = False
    flag2 = False
    flag3 = False
    with col1:
        # Botones en una sola columna
        if st.button("Actualizar archivo", use_container_width=True):
            st.write("Has clickeado en 'Actualizar archivo'")  # Mensaje de prueba

        if st.button("Observar gráfica", use_container_width=True):
            st.write("Has clickeado en 'Observar gráfica'")  # Mensaje de prueba

        if st.button("Observar tabla", use_container_width=True):
            flag3 = True

        if st.button("Salir", use_container_width=True):
            st.write("Ahora puedes cerrar la ventana")
            os._exit(0)  # Detener la ejecución de Streamlit

    with col2:
        if flag3 ==True:
            if archivo is not None:
                df = cargar_datos(archivo)
                st.dataframe(df,use_container_width=True)
            else: 
                st.write("Agregue un archivo por favor")    
        
      


if __name__ == "__main__":
    mostrar_ventana_principal()