import streamlit as st

# Definir una función para calcular el promedio ponderado
def calcular_promedio_ponderado(notas, creditos):
    """Calcula el promedio ponderado a partir de las notas y los créditos."""
    return sum(n * c for n, c in zip(notas, creditos)) / sum(creditos)

# Crear una lista de tipos de asignaturas
TIPOS_ASIGNATURAS = [
    "Disciplinar Obligatoria",
    "Fundamental Obligatoria",
    "Disciplinar Optativa",
    "Fundamental Optativa",
    "Libre Elección"
]

# Configurar la interfaz de usuario con Streamlit
st.title("Calculadora de Promedio Aritmético Ponderado Acumulado (PAPA)")

# Autor de la app
st.write("Esta app fue elaborada por Hassel Florez.") 

st.write(
    "Calcula el Promedio Aritmético Ponderado Acumulado (PAPA) de tus materias "
    "considerando las calificaciones, los créditos y la tipología de asignatura."
)

# Crear listas para almacenar los valores
notas = []
creditos = []
tipologia = []

# Formulario para ingresar las materias
num_materias = st.number_input("Número de materias", min_value=1, max_value=20, step=1)

for i in range(num_materias):
    st.subheader(f"Materia {i + 1}")
    nota = st.number_input(
        f"Nota de la materia {i + 1}", min_value=0.0, max_value=5.0, step=0.1, format="%.1f"
    )
    credito = st.number_input(f"Número de créditos de la materia {i + 1}", min_value=1, max_value=10, step=1)
    tip = st.selectbox(f"Tipo de asignatura {i + 1}", TIPOS_ASIGNATURAS, key=f"tipologia_{i + 1}")
    
    notas.append(nota)
    creditos.append(credito)
    tipologia.append(tip)

# Calcular el Promedio Aritmético Ponderado Acumulado global
papa_global = calcular_promedio_ponderado(notas, creditos)

# Calcular el Promedio Aritmético Ponderado Acumulado por tipología
papa_por_tipologia = {}
for tipo in TIPOS_ASIGNATURAS:
    notas_tipologia = [notas[i] for i in range(num_materias) if tipologia[i] == tipo]
    creditos_tipologia = [creditos[i] for i in range(num_materias) if tipologia[i] == tipo]
    if notas_tipologia:  # Si hay materias de esta tipología
        papa_por_tipologia[tipo] = calcular_promedio_ponderado(notas_tipologia, creditos_tipologia)
    else:
        papa_por_tipologia[tipo] = 0.0

# Mostrar resultados
st.subheader("Resultados")

# Promedio global
st.write(f"**Promedio Aritmético Ponderado Acumulado Global**: {papa_global:.2f}")

# Promedio por tipología
st.write("**Promedio Aritmético Ponderado Acumulado por Tipología**:")
for tipo, promedio in papa_por_tipologia.items():
    st.write(f"{tipo}: {promedio:.2f}")
