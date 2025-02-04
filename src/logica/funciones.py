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



def guardar_csv(df, ruta="archivo actualizado.csv"):
    """
    Guarda el DataFrame en un archivo CSV.
    """
    try:
        df.to_csv(ruta, index=False)  # Ajusta la ruta y el nombre del archivo
        print(f"Archivo guardado exitosamente en {ruta}")
        return ruta
    except Exception as e:
        raise ValueError(f"Error al guardar el archivo CSV: {e}")




def agregar_registro(df):
    if not df.empty:
        # Obtener la última fila
        ultima_fila = df.iloc[-1:]
        # Concatenar la última fila con el DataFrame
        df = pd.concat([df, ultima_fila], ignore_index=True)
    return df




def eliminar_ultimo_registro(df):
    """
    Elimina el último registro del DataFrame.
    
    Parámetros:
    df (pd.DataFrame): DataFrame original.

    Retorna:
    pd.DataFrame: DataFrame actualizado sin el último registro.
    """
    try:
        if not df.empty:
            df = df.iloc[:-1]  # Eliminar la última fila
            return df
        else:
            raise ValueError("El DataFrame está vacío.")
    except Exception as e:
        raise ValueError(f"Error al eliminar el último registro: {e}")


       
def mostrar_tabla(df):
    st.dataframe(df,use_container_width=True)

def obtener_tipos_ejercicio(df):
    """
    Extrae los tipos de ejercicio únicos de la columna 'ejercicio'.
    """
    return df['Ejercicio'].unique()
