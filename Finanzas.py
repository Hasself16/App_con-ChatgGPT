import streamlit as st
import pandas as pd
import numpy as np
import datetime

# Configuración de la página
st.set_page_config(page_title="Finanzas Personales", layout="wide")

# Función para generar reporte
def generar_reporte(df, periodo):
    if periodo == 'Semanal':
        df['Semana'] = df['Fecha'].dt.isocalendar().week
        reporte = df.groupby(['Semana']).sum()
    elif periodo == 'Mensual':
        df['Mes'] = df['Fecha'].dt.month
        reporte = df.groupby(['Mes']).sum()
    else:
        st.warning("Selecciona un periodo válido.")
        return None
    
    return reporte

# Datos de ejemplo
if 'finanzas' not in st.session_state:
    st.session_state.finanzas = pd.DataFrame(columns=['Fecha', 'Categoría', 'Monto', 'Tipo'])

if 'metas_ahorro' not in st.session_state:
    st.session_state.metas_ahorro = pd.DataFrame(columns=['Meta', 'Monto Objetivo', 'Fecha Objetivo'])

# Título de la app
st.title("Aplicación de Finanzas Personales")

# Menú de navegación
menu = ["Ingreso/Gasto", "Metas de Ahorro", "Presupuesto", "Reporte"]
opcion = st.sidebar.selectbox("Selecciona una opción", menu)

# Formulario para registrar ingresos o gastos
if opcion == "Ingreso/Gasto":
    st.header("Registrar Ingreso o Gasto")
    
    tipo = st.radio("¿Es un Ingreso o un Gasto?", ["Ingreso", "Gasto"])
    categoria = st.text_input("Categoría")
    monto = st.number_input(f"Monto de {tipo}", min_value=0.0, step=1.0)
    fecha = st.date_input("Fecha", value=datetime.date.today())
    
    if st.button(f"Registrar {tipo}"):
        nuevo_registro = pd.DataFrame({
            'Fecha': [fecha],
            'Categoría': [categoria],
            'Monto': [monto],
            'Tipo': [tipo]
        })
        
        st.session_state.finanzas = pd.concat([st.session_state.finanzas, nuevo_registro], ignore_index=True)
        st.success(f"{tipo} registrado exitosamente.")
        st.write(st.session_state.finanzas)

# Ingreso de metas de ahorro
elif opcion == "Metas de Ahorro":
    st.header("Registrar Metas de Ahorro")
    
    meta = st.text_input("Meta de Ahorro")
    monto_meta = st.number_input("Monto objetivo", min_value=0.0, step=1.0)
    fecha_meta = st.date_input("Fecha objetivo", value=datetime.date.today())
    
    if st.button("Registrar Meta de Ahorro"):
        nueva_meta = pd.DataFrame({
            'Meta': [meta],
            'Monto Objetivo': [monto_meta],
            'Fecha Objetivo': [fecha_meta]
        })
        
        st.session_state.metas_ahorro = pd.concat([st.session_state.metas_ahorro, nueva_meta], ignore_index=True)
        st.success("Meta de ahorro registrada exitosamente.")
        st.write(st.session_state.metas_ahorro)

# Ingreso de presupuesto
elif opcion == "Presupuesto":
    st.header("Registrar Presupuesto Mensual")
    
    categoria_presupuesto = st.text_input("Categoría del presupuesto")
    monto_presupuesto = st.number_input("Monto presupuestado", min_value=0.0, step=1.0)
    mes_presupuesto = st.selectbox("Mes", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    
    if st.button("Registrar Presupuesto"):
        if 'presupuestos' not in st.session_state:
            st.session_state.presupuestos = pd.DataFrame(columns=['Mes', 'Categoría', 'Monto Presupuestado'])
        
        nuevo_presupuesto = pd.DataFrame({
            'Mes': [mes_presupuesto],
            'Categoría': [categoria_presupuesto],
            'Monto Presupuestado': [monto_presupuesto]
        })
        
        st.session_state.presupuestos = pd.concat([st.session_state.presupuestos, nuevo_presupuesto], ignore_index=True)
        st.success("Presupuesto registrado exitosamente.")
        st.write(st.session_state.presupuestos)

# Reporte de finanzas
elif opcion == "Reporte":
    st.header("Generar Reporte Financiero")
    
    periodo = st.radio("Selecciona el periodo del reporte", ['Semanal', 'Mensual'])
    
    if st.session_state.finanzas.empty:
        st.warning("No tienes registros de ingresos o gastos.")
    else:
        # Generar reporte comparando lo real con lo presupuestado
        df_reportado = generar_reporte(st.session_state.finanzas, periodo)
        
        if df_reportado is not None:
            # Comparación entre presupuesto y lo real
            if 'presupuestos' in st.session_state:
                df_comparado = pd.merge(df_reportado, st.session_state.presupuestos, how='left', 
                                         left_on=['Mes' if periodo == 'Mensual' else 'Semana'], right_on=['Mes'])
                df_comparado['Diferencia'] = df_comparado['Monto'] - df_comparado['Monto Presupuestado']
                st.write(df_comparado)
            else:
                st.warning("No has registrado presupuestos.")
