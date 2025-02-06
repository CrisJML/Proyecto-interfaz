import sys
import os
# Agrega la ruta de src/ al PATH de Python

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from logica.funciones import agregar_registro, guardar_csv, cargar_datos, eliminar_ultimo_registro, mostrar_tabla, plot_ejercicios, obtener_opciones

def hide_button():
    st.session_state.show_button = False


def mostrar_ventana_principal():

    #Configurar la página para usar todo el espacio de esta
    st.set_page_config(page_title="FitPlan Analysis", layout="wide")


    if "mostrar_tabla" not in st.session_state:
        st.session_state.mostrar_tabla = False

    if "mostrar_actualizar" not in st.session_state:
        st.session_state.mostrar_actualizar = False

    if "mostrar_grafica" not in st.session_state:
        st.session_state.mostrar_grafica = False

    if "agregar_registro" not in st.session_state:
        st.session_state.agregar_registro = False


    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame()  # Inicializar un DataFrame vacío por si no hay datos  

    #Título de la página
    st.markdown("<h1 style='text-align: center; font-size: 50px;'>FitPlan Analysis</h1>", unsafe_allow_html=True)

    #Cargar el archivo
    st.markdown("<h1 style='text-align: center; font-size: 30px;'>Sube tu registro de entrenamientos aquí:</h1>", unsafe_allow_html=True)
    
    archivo = st.file_uploader("Carga tu archivo", type=["csv"], key="file_uploader", label_visibility="collapsed")

    
    flag = False

    if "file_uploaded" not in st.session_state:
        st.session_state.file_uploaded = False

    if archivo:
        confirm_upload = st.checkbox("Si ya cargó su archivo, marque esta casilla")
        if not confirm_upload:
            if st.button("Carga tu archivo", use_container_width=True):
                flag = True
        
    
    if archivo is not None and flag:  
        st.session_state.df = cargar_datos(archivo)
        st.session_state.df['Fecha'] = pd.to_datetime(st.session_state.df['Fecha'])
        st.session_state.df['Carga [Kg]'] = st.session_state.df['Carga [Kg]'].astype(float)
        st.write("Carga exitosa")


    #Para observar la tabla

    if st.button("Observar tabla", use_container_width=True):
        if st.session_state.df .empty:
            st.write("Cargue primero su archivo...")
        else:
            st.session_state.mostrar_tabla = not st.session_state.mostrar_tabla
            

    if st.session_state.mostrar_tabla:
        mostrar_tabla(st.session_state.df)

    #Para graficar

    if st.button("Observar gráfica", use_container_width=True):
        if st.session_state.df .empty:
            st.write("Cargue primero su archivo...")
        else:
            st.session_state.mostrar_grafica = not st.session_state.mostrar_grafica


    if st.session_state.mostrar_grafica:
         #Seleccionar grupo muscular
        grupos_musculares = st.session_state.df['Grupo muscular'].unique()
        grupo_seleccionado = st.selectbox('Selecciona un grupo muscular', grupos_musculares)

        # Filtrar ejercicios por grupo muscular seleccionado
        ejercicios_grupo = st.session_state.df[st.session_state.df['Grupo muscular'] == grupo_seleccionado]['Ejercicio'].unique()
        
        # Seleccionar ejercicios específicos
        ejercicios_seleccionados = st.multiselect(
            'Selecciona los ejercicios a graficar', 
            ejercicios_grupo, 
            default=ejercicios_grupo
        )

        # **Nuevo: Seleccionar la métrica a graficar**
        metrica_seleccionada = st.selectbox(
            'Selecciona la métrica a graficar',
            ['Series', 'Repeticiones', 'Carga [Kg]']
        )

        # Filtrar el DataFrame según los ejercicios seleccionados
        df_filtrado = st.session_state.df[
            (st.session_state.df['Ejercicio'].isin(ejercicios_seleccionados)) &
            (st.session_state.df['Grupo muscular'] == grupo_seleccionado)
        ]

        # Mostrar el gráfico si se seleccionaron ejercicios
        if ejercicios_seleccionados:
            st.plotly_chart(plot_ejercicios(df_filtrado, ejercicios_seleccionados, metrica_seleccionada))
        else:
            st.write("Por favor, selecciona al menos un ejercicio.")       



    if st.button("Actualizar archivo", use_container_width=True):
        if st.session_state.df .empty:
            st.write("Cargue primero su archivo...")
        else:
            st.session_state.mostrar_actualizar = not st.session_state.mostrar_actualizar  # Cambia estado


    # Mostrar botones adicionales si se activó "Actualizar archivo"
    if st.session_state.mostrar_actualizar:
        col_small1, col_small2, col_small3  = st.columns([0.2, 0.6, 0.2])  # Columnas más pequeñas
        with col_small2:
            
            if st.button("Agregar registro", use_container_width=True):
                    st.session_state.agregar_registro = not st.session_state.agregar_registro

            if st.session_state.agregar_registro:

                # Menús desplegables para seleccionar Grupo Muscular y Ejercicio
                grupo_muscular = st.selectbox("Seleccione el grupo muscular:", obtener_opciones(st.session_state.df, "Grupo muscular"))
                ejercicio = st.selectbox("Seleccione el ejercicio:", obtener_opciones(st.session_state.df, "Ejercicio"))

                # Inputs para Series, Repeticiones, Carga y Fecha
                series = st.number_input("Series", min_value=1, max_value=10, step=1)
                repeticiones = st.number_input("Repeticiones", min_value=1, max_value=50, step=1)
                carga = st.number_input("Carga [Kg]", min_value=0.0, step=0.5)
                fecha = st.date_input("Fecha")

                if st.button("Agregar", use_container_width=True):
                    if grupo_muscular and ejercicio:
                        st.session_state.df = agregar_registro(st.session_state.df, grupo_muscular, ejercicio, series, repeticiones, carga, fecha)
                        st.success("Registro agregado con éxito")
                        mostrar_tabla(st.session_state.df)
                    else:
                        st.error("Debe seleccionar un grupo muscular y un ejercicio")
                


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