import streamlit as st
import math


# Funciones para calcular áreas y volúmenes

def area_circulo(radio):
    """Calcula el área de un círculo."""
    return math.pi * radio ** 2


def area_triangulo(base, altura):
    """Calcula el área de un triángulo."""
    return 0.5 * base * altura


def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura


def area_trapecio(base_mayor, base_menor, altura):
    """Calcula el área de un trapecio."""
    return ((base_mayor + base_menor) * altura) / 2


def volumen_cubo(lado):
    """Calcula el volumen de un cubo."""
    return lado ** 3


def volumen_esfera(radio):
    """Calcula el volumen de una esfera."""
    return (4 / 3) * math.pi * radio ** 3


def volumen_cilindro(radio, altura):
    """Calcula el volumen de un cilindro."""
    return math.pi * radio ** 2 * altura


def volumen_cono(radio, altura):
    """Calcula el volumen de un cono."""
    return (1 / 3) * math.pi * radio ** 2 * altura


# Título de la aplicación
st.title("Calculadora de Áreas y Volúmenes de Figuras Comunes")

# Menú para seleccionar entre áreas o volúmenes
categoria = st.radio(
    "Selecciona la categoría",
    ("Áreas", "Volúmenes")
)

# Sección de áreas
if categoria == "Áreas":
    opcion_area = st.selectbox(
        'Selecciona la figura para calcular el área',
        ('Área de un Círculo', 'Área de un Triángulo', 'Área de un Rectángulo', 'Área de un Trapecio')
    )

    if opcion_area == 'Área de un Círculo':
        radio = st.number_input('Introduce el radio del círculo', min_value=0.0)
        if radio > 0:
            resultado = area_circulo(radio)
            st.write(f'El área del círculo es: {resultado:.2f} unidades cuadradas')

    elif opcion_area == 'Área de un Triángulo':
        base = st.number_input('Introduce la base del triángulo', min_value=0.0)
        altura = st.number_input('Introduce la altura del triángulo', min_value=0.0)
        if base > 0 and altura > 0:
            resultado = area_triangulo(base, altura)
            st.write(f'El área del triángulo es: {resultado:.2f} unidades cuadradas')

    elif opcion_area == 'Área de un Rectángulo':
        base = st.number_input('Introduce la base del rectángulo', min_value=0.0)
        altura = st.number_input('Introduce la altura del rectángulo', min_value=0.0)
        if base > 0 and altura > 0:
            resultado = area_rectangulo(base, altura)
            st.write(f'El área del rectángulo es: {resultado:.2f} unidades cuadradas')

    elif opcion_area == 'Área de un Trapecio':
        base_mayor = st.number_input('Introduce la base mayor del trapecio', min_value=0.0)
        base_menor = st.number_input('Introduce la base menor del trapecio', min_value=0.0)
        altura = st.number_input('Introduce la altura del trapecio', min_value=0.0)
        if base_mayor > 0 and base_menor > 0 and altura > 0:
            resultado = area_trapecio(base_mayor, base_menor, altura)
            st.write(f'El área del trapecio es: {resultado:.2f} unidades cuadradas')

# Sección de volúmenes
elif categoria == "Volúmenes":
    opcion_volumen = st.selectbox(
        'Selecciona la figura para calcular el volumen',
        ('Volumen de un Cubo', 'Volumen de una Esfera', 'Volumen de un Cilindro', 'Volumen de un Cono')
    )

    if opcion_volumen == 'Volumen de un Cubo':
        lado = st.number_input('Introduce el lado del cubo', min_value=0.0)
        if lado > 0:
            resultado = volumen_cubo(lado)
            st.write(f'El volumen del cubo es: {resultado:.2f} unidades cúbicas')

    elif opcion_volumen == 'Volumen de una Esfera':
        radio = st.number_input('Introduce el radio de la esfera', min_value=0.0)
        if radio > 0:
            resultado = volumen_esfera(radio)
            st.write(f'El volumen de la esfera es: {resultado:.2f} unidades cúbicas')

    elif opcion_volumen == 'Volumen de un Cilindro':
        radio = st.number_input('Introduce el radio del cilindro', min_value=0.0)
        altura = st.number_input('Introduce la altura del cilindro', min_value=0.0)
        if radio > 0 and altura > 0:
            resultado = volumen_cilindro(radio, altura)
            st.write(f'El volumen del cilindro es: {resultado:.2f} unidades cúbicas')

    elif opcion_volumen == 'Volumen de un Cono':
        radio = st.number_input('Introduce el radio del cono', min_value=0.0)
        altura = st.number_input('Introduce la altura del cono', min_value=0.0)
        if radio > 0 and altura > 0:
            resultado = volumen_cono(radio, altura)
            st.write(f'El volumen del cono es: {resultado:.2f} unidades cúbicas')
