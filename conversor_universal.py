# Importamos Streamlit
import streamlit as st

# Título de la aplicación
st.title("Conversor Universal")


# Autor de la app
st.write("Esta app fue elaborada por Hassel Florez.")


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

# === Conversiones de Temperatura ===
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
        resultado = valor * 9 / 5 + 32
        st.write(f"{valor}°C son {resultado:.2f}°F")
    elif conversion == "Fahrenheit a Celsius":
        resultado = (valor - 32) * 5 / 9
        st.write(f"{valor}°F son {resultado:.2f}°C")
    elif conversion == "Celsius a Kelvin":
        resultado = valor + 273.15
        st.write(f"{valor}°C son {resultado:.2f}K")
    elif conversion == "Kelvin a Celsius":
        resultado = valor - 273.15
        st.write(f"{valor}K son {resultado:.2f}°C")

# === Conversiones de Longitud ===
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
        resultado = valor * 0.3048
        st.write(f"{valor} pies son {resultado:.2f} metros")
    elif conversion == "Metros a pies":
        resultado = valor / 0.3048
        st.write(f"{valor} metros son {resultado:.2f} pies")
    elif conversion == "Pulgadas a centímetros":
        resultado = valor * 2.54
        st.write(f"{valor} pulgadas son {resultado:.2f} cm")
    elif conversion == "Centímetros a pulgadas":
        resultado = valor / 2.54
        st.write(f"{valor} cm son {resultado:.2f} pulgadas")

# === Conversiones de Peso/Masa ===
elif tipo_conversion == "Peso/Masa":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        [
            "Libras a kilogramos",
            "Kilogramos a libras",
            "Onzas a gramos",
            "Gramos a onzas",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Libras a kilogramos":
        resultado = valor * 0.453592
        st.write(f"{valor} libras son {resultado:.2f} kg")
    elif conversion == "Kilogramos a libras":
        resultado = valor / 0.453592
        st.write(f"{valor} kg son {resultado:.2f} libras")
    elif conversion == "Onzas a gramos":
        resultado = valor * 28.3495
        st.write(f"{valor} onzas son {resultado:.2f} gramos")
    elif conversion == "Gramos a onzas":
        resultado = valor / 28.3495
        st.write(f"{valor} gramos son {resultado:.2f} onzas")

# === Conversiones de Volumen ===
elif tipo_conversion == "Volumen":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        [
            "Galones a litros",
            "Litros a galones",
            "Pulgadas cúbicas a cm³",
            "Cm³ a pulgadas cúbicas",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Galones a litros":
        resultado = valor * 3.78541
        st.write(f"{valor} galones son {resultado:.2f} litros")
    elif conversion == "Litros a galones":
        resultado = valor / 3.78541
        st.write(f"{valor} litros son {resultado:.2f} galones")
    elif conversion == "Pulgadas cúbicas a cm³":
        resultado = valor * 16.3871
        st.write(f"{valor} pulgadas cúbicas son {resultado:.2f} cm³")
    elif conversion == "Cm³ a pulgadas cúbicas":
        resultado = valor / 16.3871
        st.write(f"{valor} cm³ son {resultado:.2f} pulgadas cúbicas")

# === Conversiones de Tiempo ===
elif tipo_conversion == "Tiempo":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        [
            "Horas a minutos",
            "Minutos a segundos",
            "Días a horas",
            "Semanas a días",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Horas a minutos":
        resultado = valor * 60
        st.write(f"{valor} horas son {resultado:.2f} minutos")
    elif conversion == "Minutos a segundos":
        resultado = valor * 60
        st.write(f"{valor} minutos son {resultado:.2f} segundos")
    elif conversion == "Días a horas":
        resultado = valor * 24
        st.write(f"{valor} días son {resultado:.2f} horas")
    elif conversion == "Semanas a días":
        resultado = valor * 7
        st.write(f"{valor} semanas son {resultado:.2f} días")

# === Conversiones de Velocidad ===
elif tipo_conversion == "Velocidad":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        [
            "Millas/h a km/h",
            "Km/h a m/s",
            "Nudos a mph",
            "m/s a fps",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Millas/h a km/h":
        resultado = valor * 1.60934
        st.write(f"{valor} mph son {resultado:.2f} km/h")
    elif conversion == "Km/h a m/s":
        resultado = valor / 3.6
        st.write(f"{valor} km/h son {resultado:.2f} m/s")
    elif conversion == "Nudos a mph":
        resultado = valor * 1.15078
        st.write(f"{valor} nudos son {resultado:.2f} mph")
    elif conversion == "m/s a fps":
        resultado = valor * 3.28084
        st.write(f"{valor} m/s son {resultado:.2f} fps")

# === Conversiones de Área ===
elif tipo_conversion == "Área":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        [
            "Metros cuadrados a pies cuadrados",
            "Pies cuadrados a metros cuadrados",
            "Kilómetros cuadrados a millas cuadradas",
            "Millas cuadradas a kilómetros cuadrados",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Metros cuadrados a pies cuadrados":
        resultado = valor * 10.7639
        st.write(f"{valor} m² son {resultado:.2f} ft²")
    elif conversion == "Pies cuadrados a metros cuadrados":
        resultado = valor / 10.7639
        st.write(f"{valor} ft² son {resultado:.2f} m²")
    elif conversion == "Kilómetros cuadrados a millas cuadradas":
        resultado = valor * 0.386102
        st.write(f"{valor} km² son {resultado:.2f} mi²")
    elif conversion == "Millas cuadradas a kilómetros cuadrados":
        resultado = valor / 0.386102
        st.write(f"{valor} mi² son {resultado:.2f} km²")

# === Conversiones de Energía ===
elif tipo_conversion == "Energía":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        [
            "Julios a calorías",
            "Calorías a kilojulios",
            "Kilovatios-hora a megajulios",
            "Megajulios a kilovatios-hora",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Julios a calorías":
        resultado = valor / 4.184
        st.write(f"{valor} J son {resultado:.2f} cal")
    elif conversion == "Calorías a kilojulios":
        resultado = valor * 4.184 / 1000
        st.write(f"{valor} cal son {resultado:.2f} kJ")
    elif conversion == "Kilovatios-hora a megajulios":
        resultado = valor * 3.6
        st.write(f"{valor} kWh son {resultado:.2f} MJ")
    elif conversion == "Megajulios a kilovatios-hora":
        resultado = valor / 3.6
        st.write(f"{valor} MJ son {resultado:.2f} kWh")

# === Conversiones de Presión ===
elif tipo_conversion == "Presión":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        [
            "Pascales a atmósferas",
            "Atmósferas a pascales",
            "Barras a libras por pulgada cuadrada",
            "Libras por pulgada cuadrada a bares",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Pascales a atmósferas":
        resultado = valor / 101325
        st.write(f"{valor} Pa son {resultado:.6f} atm")
    elif conversion == "Atmósferas a pascales":
        resultado = valor * 101325
        st.write(f"{valor} atm son {resultado:.2f} Pa")
    elif conversion == "Barras a libras por pulgada cuadrada":
        resultado = valor * 14.5038
        st.write(f"{valor} bar son {resultado:.2f} psi")
    elif conversion == "Libras por pulgada cuadrada a bares":
        resultado = valor / 14.5038
        st.write(f"{valor} psi son {resultado:.6f} bar")

# === Conversiones de Tamaño de Datos ===
elif tipo_conversion == "Tamaño de Datos":
    conversion = st.selectbox(
        "Selecciona la conversión:",
        [
            "Megabytes a gigabytes",
            "Gigabytes a terabytes",
            "Kilobytes a megabytes",
            "Terabytes a petabytes",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Megabytes a gigabytes":
        resultado = valor / 1024
        st.write(f"{valor} MB son {resultado:.6f} GB")
    elif conversion == "Gigabytes a terabytes":
        resultado = valor / 1024
        st.write(f"{valor} GB son {resultado:.6f} TB")
    elif conversion == "Kilobytes a megabytes":
        resultado = valor / 1024
        st.write(f"{valor} KB son {resultado:.6f} MB")
    elif conversion == "Terabytes a petabytes":
        resultado = valor / 1024
        st.write(f"{valor} TB son {resultado:.6f} PB")

# === Advertencia si no se selecciona categoría válida ===
else:
    st.warning("Selecciona una categoría válida para realizar conversiones.")
