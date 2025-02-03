import sys
import os
# Agrega la ruta de src/ al PATH de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from logica.funciones import cargar_datos, obtener_tipos_ejercicio

def mostrar_ventana_principal():
    st.title("Visualizador de Ejercicios")

    # Cargar archivo CSV
    archivo = st.file_uploader("Sube un archivo CSV", type=["csv"])
    
    if archivo is not None:
        # Leer el archivo CSV
        df = cargar_datos(archivo)
        
        # Mostrar los datos en una tabla
        st.write("Datos cargados:")
        st.dataframe(df)
        
        # Obtener y mostrar los tipos de ejercicio
        tipos_ejercicio = obtener_tipos_ejercicio(df)
        st.write("Tipos de ejercicio disponibles:")
        st.write(tipos_ejercicio)

if __name__ == "__main__":
    mostrar_ventana_principal()