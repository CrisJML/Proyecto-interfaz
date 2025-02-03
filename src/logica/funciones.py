import pandas as pd

def cargar_datos(ruta_archivo):
    """
    Carga un archivo CSV y devuelve un DataFrame.
    """
    return pd.read_csv(ruta_archivo)

def obtener_tipos_ejercicio(df):
    """
    Extrae los tipos de ejercicio únicos de la columna 'ejercicio'.
    """
    return df['Ejercicio'].unique()

def saludar(nombre):
    return f"¡Hola, {nombre}!"