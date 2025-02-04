import pandas as pd
import streamlit as st

def cargar_datos(ruta_archivo):
    """
    Carga un archivo CSV y devuelve un DataFrame.
    """
    try:
        # Intenta cargar el CSV usando pandas
        df = pd.read_csv(ruta_archivo)
        return df
    except Exception as e:
        # Si ocurre algún error, imprime el error
        st.error(f"Error al cargar el archivo: {e}")
        return None  # Retorna None si hay un error


       

def obtener_tipos_ejercicio(df):
    """
    Extrae los tipos de ejercicio únicos de la columna 'ejercicio'.
    """
    return df['Ejercicio'].unique()
