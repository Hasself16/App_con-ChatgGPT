# Importamos la biblioteca Streamlit
import streamlit as st

# Título de la app
st.title("Mi primera app")

# Autor de la app
st.write("Esta app fue elaborada por Hassel Florez.")

# Solicitamos el nombre al usuario
nombre_usuario = st.text_input("Por favor, escribe tu nombre:")

# Mostramos un mensaje personalizado si el usuario ingresa un nombre
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
