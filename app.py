import streamlit as st

st.set_page_config(page_title="Timeline de Detección de Fraude", layout="centered")

st.title("💳 Timeline de los Avances Tecnológicos en la Detección de Fraude Bancario")

st.write(
    "Alumno: Herwuin Huaman Rivas")


st.write(
    "Usa la barra deslizante para explorar cinco hitos tecnológicos que transformaron la lucha contra el fraude financiero.")

# Datos del timeline
eventos = {
    1: {
        "año": 1987,
        "titulo": "Sistemas de Reglas para Detección de Fraude",
        "descripcion": "Los bancos comienzan a usar sistemas basados en reglas (if–then) para identificar comportamientos sospechosos en transacciones."
    },
    2: {
        "año": 1995,
        "titulo": "Modelos Estadísticos y Scoring",
        "descripcion": "Se introducen modelos como regresión logística y scorecards para medir el riesgo de operaciones fraudulentas."
    },
    3: {
        "año": 2005,
        "titulo": "Machine Learning en Tiempo Real",
        "descripcion": "Los bancos adoptan algoritmos de ML capaces de aprender patrones históricos y detectar anomalías mientras ocurre la transacción."
    },
    4: {
        "año": 2015,
        "titulo": "Redes Neuronales y Deep Learning",
        "descripcion": "Se popularizan modelos profundos que identifican patrones complejos y mejoran la precisión contra fraudes cada vez más sofisticados."
    },
    5: {
        "año": 2022,
        "titulo": "IA Generativa y Sistemas Predictivos Avanzados",
        "descripcion": "Se integran modelos generativos y análisis multimodal para anticipar rutas de fraude, simular ataques y mejorar la prevención proactiva."
    }
}

# Slider
seleccion = st.slider(
    "Selecciona un hito tecnológico:",
    min_value=1,
    max_value=5,
    value=1,
    format="Hito %d"
)

evento = eventos[seleccion]

# Mostrar contenido
st.subheader(f"📌 {evento['año']} — {evento['titulo']}")
st.write(evento["descripcion"])

