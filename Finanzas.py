import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# Función para obtener la fecha de inicio de la semana
def get_week_start(date):
    """Obtiene la fecha de inicio de la semana (lunes) para una fecha dada."""
    return date - timedelta(days=date.weekday())


# Función para generar el reporte de finanzas
def generar_reporte(data, period="semanal"):
    """Genera un reporte comparando presupuesto y gasto real por semana o mes."""
    
    # Asegurarse de que 'fecha' es un tipo de dato datetime
    data['fecha'] = pd.to_datetime(data['fecha'])
    
    if period == "semanal":
        # Obtener la fecha de inicio de la semana para cada registro
        data['semana'] = data['fecha'].apply(get_week_start)
        reporte = data.groupby('semana').agg({'presupuesto': 'sum', 'real': 'sum'})
        reporte['diferencia'] = reporte['presupuesto'] - reporte['real']
    else:
        # Agrupar por mes
        data['mes'] = data['fecha'].dt.to_period('M')
        reporte = data.groupby('mes').agg({'presupuesto': 'sum', 'real': 'sum'})
        reporte['diferencia'] = reporte['presupuesto'] - reporte['real']
    
    return reporte


# Configuración de la app en Streamlit
st.title("Aplicación de Finanzas Personales")

# Inicialización de los datos
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['fecha', 'categoria', 'presupuesto', 'real'])

# Formulario para registrar una nueva transacción
with st.form("formulario_finanzas"):
    st.header("Registrar una nueva transacción")
    fecha = st.date_input("Fecha", value=datetime.today())
    categoria = st.text_input("Categoría (ej. comida, alquiler, transporte)")
    presupuesto = st.number_input("Presupuesto (€)", min_value=0.0, value=0.0, step=10.0)
    real = st.number_input("Real (€)", min_value=0.0, value=0.0, step=10.0)
    submit_button = st.form_submit_button("Registrar")

    if submit_button:
        # Agregar los datos al DataFrame
        st.session_state.data = pd.concat(
            [st.session_state.data, pd.DataFrame([[fecha, categoria, presupuesto, real]], columns=['fecha', 'categoria', 'presupuesto', 'real'])],
            ignore_index=True
        )
        st.success("Transacción registrada con éxito!")

# Mostrar los datos registrados
if len(st.session_state.data) > 0:
    st.subheader("Datos de Finanzas")
    st.dataframe(st.session_state.data)

    # Generar reportes semanales y mensuales
    reporte_semanal = generar_reporte(st.session_state.data, period="semanal")
    reporte_mensual = generar_reporte(st.session_state.data, period="mensual")

    # Mostrar reportes
    st.subheader("Reporte Semanal")
    st.dataframe(reporte_semanal)

    st.subheader("Reporte Mensual")
    st.dataframe(reporte_mensual)
