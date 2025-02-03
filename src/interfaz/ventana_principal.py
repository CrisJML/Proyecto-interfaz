import streamlit as st

def mostrar_ventana_principal():
    st.title("Mi Proyecto con Streamlit")
    st.write("¡Bienvenido a mi proyecto!")
    nombre = st.text_input("Introduce tu nombre")
    if st.button("Saludar"):
        st.write(f"¡Hola, {nombre}!")

if __name__ == "__main__":
    mostrar_ventana_principal()