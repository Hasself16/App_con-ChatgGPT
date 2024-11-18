# Importamos Streamlit
import streamlit as st

# Título de la aplicación
st.title("Conversor Universal")

# Menú principal: Selección de tipo de conversión
tipo_conversion = st.selectbox(
    "Selecciona el tipo de conversión:",
    [
        "Temperatura",
        "Longitud",
        "Peso/Masa",
        "Volumen",
        "Tiempo",
        "Velocidad",
        "Área",
        "Energía",
        "Presión",
        "Tamaño de Datos",
    ],
)


# Definición de funciones de conversión
def celsius_a_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9


def celsius_a_kelvin(c):
    return c + 273.15


def kelvin_a_celsius(k):
    return k - 273.15


def pies_a_metros(p):
    return p * 0.3048


def metros_a_pies(m):
    return m / 0.3048


# Submenú según el tipo de conversión seleccionado
if tipo_conversion == "Temperatura":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        [
            "Celsius a Fahrenheit",
            "Fahrenheit a Celsius",
            "Celsius a Kelvin",
            "Kelvin a Celsius",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Celsius a Fahrenheit":
        st.write(
            f"{valor}°C son {celsius_a_fahrenheit(valor):.2f}°F"
        )
    elif conversion == "Fahrenheit a Celsius":
        st.write(
            f"{valor}°F son {fahrenheit_a_celsius(valor):.2f}°C"
        )
    elif conversion == "Celsius a Kelvin":
        st.write(f"{valor}°C son {celsius_a_kelvin(valor):.2f}K")
    elif conversion == "Kelvin a Celsius":
        st.write(f"{valor}K son {kelvin_a_celsius(valor):.2f}°C")

elif tipo_conversion == "Longitud":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        [
            "Pies a metros",
            "Metros a pies",
            "Pulgadas a centímetros",
            "Centímetros a pulgadas",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Pies a metros":
        st.write(f"{valor} pies son {pies_a_metros(valor):.2f} metros")
    elif conversion == "Metros a pies":
        st.write(f"{valor} metros son {metros_a_pies(valor):.2f} pies")
