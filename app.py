import streamlit as st

st.set_page_config(page_title="Timeline IA", layout="centered")

st.title("🧠 Línea de tiempo de la Inteligencia Artificial")

st.write("Usa el slider para recorrer los momentos clave en la historia de la IA.")

# Lista de imágenes almacenadas en GitHub
timeline = {
    1: {
        "titulo": "1950 - Test de Turing",
        "img": "timeline_images/imagen1.jpg",
    },
    2: {
        "titulo": "1956 - Conferencia de Dartmouth",
        "img": "timeline_images/imagen2.jpg",
    },
    3: {
        "titulo": "1997 - Deep Blue vence a Kasparov",
        "img": "timeline_images/imagen3.jpg",
    },
    4: {
        "titulo": "2012 - AlexNet revolución del Deep Learning",
        "img": "timeline_images/imagen4.jpg",
    },
    5: {
        "titulo": "2022 - Avances en modelos generativos",
        "img": "timeline_images/imagen5.jpg",
    },
}

# Slider interactivo
punto = st.slider(
    "Selecciona un punto en la historia",
    min_value=1,
    max_value=5,
    step=1,
)

st.subheader(timeline[punto]["titulo"])

# Mostrar imagen desde GitHub
st.image(timeline[punto]["img"], use_column_width=True)

st.info("Las imágenes se cargan directamente desde la carpeta timeline_images de tu repositorio.")
