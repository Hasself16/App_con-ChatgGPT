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

# Funciones para cada conversión
# === Conversión de Temperatura ===
def celsius_a_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9


def celsius_a_kelvin(c):
    return c + 273.15


def kelvin_a_celsius(k):
    return k - 273.15


# === Conversión de Longitud ===
def pies_a_metros(p):
    return p * 0.3048


def metros_a_pies(m):
    return m / 0.3048


def pulgadas_a_centimetros(p):
    return p * 2.54


def centimetros_a_pulgadas(c):
    return c / 2.54


# === Conversión de Peso/Masa ===
def libras_a_kilogramos(l):
    return l * 0.453592


def kilogramos_a_libras(k):
    return k / 0.453592


def onzas_a_gramos(o):
    return o * 28.3495


def gramos_a_onzas(g):
    return g / 28.3495


# === Conversión de Volumen ===
def galones_a_litros(g):
    return g * 3.78541


def litros_a_galones(l):
    return l / 3.78541


def pulgadas_cubicas_a_cm_cubicos(p):
    return p * 16.3871


def cm_cubicos_a_pulgadas_cubicas(c):
    return c / 16.3871


# === Conversión de Tiempo ===
def horas_a_minutos(h):
    return h * 60


def minutos_a_segundos(m):
    return m * 60


def dias_a_horas(d):
    return d * 24


def semanas_a_dias(s):
    return s * 7


# === Conversión de Velocidad ===
def mph_a_kph(mph):
    return mph * 1.60934


def kph_a_mps(kph):
    return kph / 3.6


def nudos_a_mph(n):
    return n * 1.15078


def mps_a_fps(mps):
    return mps * 3.28084


# === Conversión de Área ===
def metros_cuadrados_a_pies_cuadrados(m2):
    return m2 * 10.7639


def pies_cuadrados_a_metros_cuadrados(p2):
    return p2 / 10.7639


def km_cuadrados_a_millas_cuadradas(km2):
    return km2 * 0.386102


def millas_cuadradas_a_km_cuadrados(mi2):
    return mi2 / 0.386102


# === Conversión de Energía ===
def julios_a_calorias(j):
    return j / 4.184


def calorias_a_kilojulios(c):
    return c * 0.004184


def kwh_a_mj(kwh):
    return kwh * 3.6


def mj_a_kwh(mj):
    return mj / 3.6


# === Conversión de Presión ===
def pascales_a_atmosferas(p):
    return p / 101325


def atmosferas_a_pascales(a):
    return a * 101325


def barras_a_psi(b):
    return b * 14.5038


def psi_a_bares(psi):
    return psi / 14.5038


# === Conversión de Tamaño de Datos ===
def megabytes_a_gigabytes(mb):
    return mb / 1024


def gigabytes_a_terabytes(gb):
    return gb / 1024


def kilobytes_a_megabytes(kb):
    return kb / 1024


def terabytes_a_petabytes(tb):
    return tb / 1024


# Submenú y lógica según el tipo de conversión seleccionado
conversion = ""
valor = 0

if tipo_conversion == "Temperatura":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"],
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Celsius a Fahrenheit":
        st.write(f"{valor}°C son {celsius_a_fahrenheit(valor):.2f}°F")
    elif conversion == "Fahrenheit a Celsius":
        st.write(f"{valor}°F son {fahrenheit_a_celsius(valor):.2f}°C")
    elif conversion == "Celsius a Kelvin":
        st.write(f"{valor}°C son {celsius_a_kelvin(valor):.2f}K")
    elif conversion == "Kelvin a Celsius":
        st.write(f"{valor}K son {kelvin_a_celsius(valor):.2f}°C")

# Repetir estructura similar para Longitud, Peso/Masa, Volumen, etc.
# ...

