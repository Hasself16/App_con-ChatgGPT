import streamlit as st
import pandas as pd
from datetime import datetime


# Título de la aplicación
st.title("Finanzas")


# Autor de la app
st.write("Esta app fue elaborada por Hassel Florez.") ¿Porque no aparece el autor de la app?


# Función para inicializar los datos
def initialize_data():
    if "data" not in st.session_state:
        st.session_state.data = pd.DataFrame(columns=[
            "Fecha", "Categoría", "Tipo", "Monto", "Descripción"
        ])
    if "goals" not in st.session_state:
        st.session_state.goals = pd.DataFrame(columns=["Meta", "Monto", "Progreso"])

# Función para agregar una transacción
def add_transaction(fecha, categoria, tipo, monto, descripcion):
    nueva_fila = {
        "Fecha": fecha,
        "Categoría": categoria,
        "Tipo": tipo,
        "Monto": monto,
        "Descripción": descripcion
    }
    st.session_state.data = pd.concat(
        [st.session_state.data, pd.DataFrame([nueva_fila])],
        ignore_index=True
    )

# Función para calcular reportes
def generate_report(period="Mensual"):
    now = datetime.now()
    if period == "Semanal":
        start_date = now - pd.Timedelta(weeks=1)
    else:  # Mensual
        start_date = now - pd.Timedelta(days=30)
    
    filtered_data = st.session_state.data[
        pd.to_datetime(st.session_state.data["Fecha"]) >= start_date
    ]
    resumen = filtered_data.groupby(["Tipo", "Categoría"])["Monto"].sum()
    return resumen

# Función para agregar metas de ahorro
def add_saving_goal(meta, monto):
    nueva_meta = {
        "Meta": meta,
        "Monto": monto,
        "Progreso": 0
    }
    st.session_state.goals = pd.concat(
        [st.session_state.goals, pd.DataFrame([nueva_meta])],
        ignore_index=True
    )

# Función para mostrar el progreso de metas de ahorro
def update_saving_goal(meta, monto):
    if meta in st.session_state.goals["Meta"].values:
        idx = st.session_state.goals[st.session_state.goals["Meta"] == meta].index[0]
        st.session_state.goals.at[idx, "Progreso"] += monto

# Inicializar datos
initialize_data()

# Configuración de la interfaz
st.title("Gestor de Finanzas Personales")
menu = st.sidebar.radio("Menú", ["Transacciones", "Metas de Ahorro", "Reportes"])

if menu == "Transacciones":
    st.subheader("Registrar una nueva transacción")
    with st.form("form_transaccion"):
        fecha = st.date_input("Fecha", value=datetime.now().date())
        categoria = st.text_input("Categoría")
        tipo = st.selectbox("Tipo", ["Ingreso", "Gasto"])
        monto = st.number_input("Monto", min_value=0.0, step=0.01)
        descripcion = st.text_area("Descripción")
        submit = st.form_submit_button("Agregar")
        
        if submit:
            add_transaction(fecha, categoria, tipo, monto, descripcion)
            st.success("Transacción agregada exitosamente")

    st.subheader("Transacciones registradas")
    st.dataframe(st.session_state.data)

elif menu == "Metas de Ahorro":
    st.subheader("Registrar una nueva meta de ahorro")
    with st.form("form_meta"):
        meta = st.text_input("Meta")
        monto = st.number_input("Monto objetivo", min_value=0.0, step=0.01)
        submit = st.form_submit_button("Agregar")
        
        if submit:
            add_saving_goal(meta, monto)
            st.success("Meta de ahorro agregada exitosamente")

    st.subheader("Progreso de metas de ahorro")
    st.dataframe(st.session_state.goals)

elif menu == "Reportes":
    st.subheader("Generar Reportes")
    periodo = st.selectbox("Periodo", ["Semanal", "Mensual"])
    reporte = generate_report(periodo)
    st.write("Resumen del reporte:")
    st.dataframe(reporte)
