import pandas as pd
import streamlit as st
import seaborn as sns
import plotly.express as px

def escoger_ejercicios(df):
    return df['Ejercicio'].unique()



def plot_ejercicios(df, ejercicios, metrica):
    # Filtrar los ejercicios seleccionados
    df_filtrado = df[df['Ejercicio'].isin(ejercicios)]
    
    # Crear el gráfico interactivo
    fig = px.line(df_filtrado, 
                  x='Fecha', 
                  y=metrica,  # Variable dinámica en el eje y
                  color='Ejercicio', 
                  markers=True,  
                  title=f'{metrica} por Ejercicio a lo largo del tiempo')
    
    # Personalizar la apariencia
    fig.update_layout(
        xaxis_title='Fecha',
        yaxis_title=metrica,  # Etiqueta dinámica en el eje y
        xaxis=dict(showgrid=True, tickangle=45),
        yaxis=dict(showgrid=True),
        template="plotly_white",
        legend_title="Ejercicios"
    )

    return fig





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




"""def agregar_registro(df):
    if not df.empty:
        # Obtener la última fila
        ultima_fila = df.iloc[-1:]
        # Concatenar la última fila con el DataFrame
        df = pd.concat([df, ultima_fila], ignore_index=True)
    return df"""


# Obtener valores únicos de Grupo Muscular y Ejercicios
def obtener_opciones(df, columna):
    return df[columna].unique().tolist() if not df.empty else []

# Función para agregar un nuevo registro
def agregar_registro(df, grupo, ejercicio, series, repeticiones, carga, fecha):
    nuevo_registro = pd.DataFrame([{
        "Grupo muscular": grupo,
        "Ejercicio": ejercicio,
        "Series": int(series),
        "Repeticiones": int(repeticiones),
        "Carga [Kg]": float(carga),
        "Fecha": pd.to_datetime(fecha)
    }])
    return pd.concat([df, nuevo_registro], ignore_index=True)






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


