import streamlit as st

# Configuración de página
st.set_page_config(page_title="Timeline de Fraude Bancario", layout="centered")

st.title("💳 Timeline Interactivo: Evolución Tecnológica en la Detección de Fraude Bancario")
st.write(
    "Usa la barra deslizante para explorar cinco hitos importantes en la lucha contra el fraude bancario."
)

# Datos del timeline
eventos = {
    1: {
        "año": 2000,
        "titulo": "Sistemas basados en reglas",
        "descripcion": "Los primeros sistemas antifraude analizaban patrones usando reglas fijas como límites de monto, horarios y ubicaciones.",
        "img": "timeline1.png"
    },
    2: {
        "año": 2008,
        "titulo": "Modelos estadísticos avanzados",
        "descripcion": "Los bancos implementan modelos como regresión logística y árboles de decisión para predecir fraude con mayor precisión.",
        "img": "timeline2.png"
    },
    3: {
        "año": 2014,
        "titulo": "Machine Learning en producción",
        "descripcion": "Se integran modelos de aprendizaje supervisado que detectan actividades sospechosas en tiempo real.",
        "img": "timeline3.png"
    },
    4: {
        "año": 2017,
        "titulo": "Deep Learning para análisis complejo",
        "descripcion": "Las redes neuronales permiten reconocer patrones avanzados como secuencias, comportamientos atípicos y redes criminales.",
        "img": "timeline4.png"
    },
    5: {
        "año": 2023,
        "titulo": "IA Generativa y sistemas modernos",
        "descripcion": "Los bancos usan IA generativa para simular fraude, mejorar alertas y crear sistemas adaptativos de seguridad.",
        "img": "timeline5.png"
    }
}

# Slider
seleccion = st.slider(
    "Selecciona un hito de la historia:",
    min_value=1,
    max_value=5,
    value=1,
    format="Hito %d"
)

evento = eventos[seleccion]

# Mostrar contenido
st.subheader(f"📌 {evento['año']} — {evento['titulo']}")
st.write(evento["descripcion"])

# Mostrar imagen del hito
st.image(evento["img"], use_container_width=True)

