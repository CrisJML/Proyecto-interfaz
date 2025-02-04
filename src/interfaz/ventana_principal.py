import sys
import os
# Agrega la ruta de src/ al PATH de Python

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from logica.funciones import agregar_registro, guardar_csv, cargar_datos, eliminar_ultimo_registro, mostrar_tabla


def mostrar_ventana_principal():

    #Configurar la página para usar todo el espacio de esta
    st.set_page_config(page_title="FitPlan Analysis", layout="wide")

    # Inicializar la variable de estado si no existe
    if "mostrar_actualizar" not in st.session_state:
        st.session_state.mostrar_actualizar = False

    if "df" not in st.session_state:  # Asegurarse de que df esté en el estado de sesión
        st.session_state.df = pd.DataFrame()  # Inicializar un DataFrame vacío por si no hay datos    



    #Título de la página
    st.markdown("<h1 style='text-align: center; font-size: 50px;'>FitPlan Analysis</h1>", unsafe_allow_html=True)

    #Cargar el archivo
    st.markdown("<h1 style='text-align: center; font-size: 30px;'>Sube tu registro de entrenamientos aquí:</h1>", unsafe_allow_html=True)
    #st.write("### Sube tu registro de entrenamientos aquí:")

    
    archivo = st.file_uploader("Carga tu archivo", type=["csv"], key="file_uploader", label_visibility="collapsed")

    

    flag = False

    if st.button("Carga tu archivo", use_container_width=True):
            flag = True
            
    if archivo is not None and flag:  
        st.session_state.df = cargar_datos(archivo)
        st.write("Carga exitosa")
    else:   
        st.write("Suba su archivo...")


    if st.button("Observar tabla", use_container_width=True):
        if st.session_state.df .empty:
            st.write("Cargue primero su archivo...")
        else:
            mostrar_tabla(st.session_state.df)


    if st.button("Observar gráfica", use_container_width=True):
            st.write("Has clickeado en 'Observar gráfica'")  # Mensaje de prueba        



    if st.button("Actualizar archivo", use_container_width=True):
            st.session_state.mostrar_actualizar = not st.session_state.mostrar_actualizar  # Cambia estado


    # Mostrar botones adicionales si se activó "Actualizar archivo"
    if st.session_state.mostrar_actualizar:
        col_small1, col_small2, col_small3  = st.columns([0.2, 0.6, 0.2])  # Columnas más pequeñas
        with col_small2:


            if st.button("Agregar registro", use_container_width=True):
                st.session_state.df = agregar_registro(st.session_state.df)
                st.write("Se agregó un registro.") 
                mostrar_tabla(st.session_state.df)


            if st.button("Eliminar último registro", use_container_width=True):
                st.session_state.df = eliminar_ultimo_registro(st.session_state.df)
                st.write("Se eliminó el último registro.") 
                mostrar_tabla(st.session_state.df)


            if st.button("Guardar archivo", use_container_width=True):
                ruta = guardar_csv(st.session_state.df)
                st.write(ruta)
                # Botón de descarga
                with open(ruta, "rb") as f:
                    st.download_button(
                            label="Descargar archivo actualizado",
                            data=f,
                            file_name=ruta,
                            mime="text/csv"
                        )   
                os.remove(ruta)



    if st.button("Salir", use_container_width=True):
            st.write("Ahora puedes cerrar la ventana")
            os._exit(0)  # Detener la ejecución de Streamlit





if __name__ == "__main__":
    mostrar_ventana_principal()