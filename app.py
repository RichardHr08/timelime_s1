import streamlit as st 
import os

st.set_page_config(page_title="Timeline de IA", layout="centered")

# --- 2. RUTAS DE IMÁGENES CORREGIDAS ---

# Cambia la ruta de la carpeta a una cadena vacía, ya que están en la raíz.
# Esto hace que las rutas sean relativas al archivo app.py
IMAGE_FOLDER = "" 

# Lista de los nombres de tus 5 imágenes (¡CORRIGE LOS NOMBRES AQUÍ!)
image_files = [
    os.path.join(IMAGE_FOLDER, "timeline1.png"),
    os.path.join(IMAGE_FOLDER, "timeline2.png"),
    os.path.join(IMAGE_FOLDER, "timeline3.png"),
    os.path.join(IMAGE_FOLDER, "timeline4.png"),
    os.path.join(IMAGE_FOLDER, "timeline5.png"),
]


if len(image_files) != 5:
    st.error(f"Error: Se esperaban 5 imágenes, pero se encontraron {len(image_files)} rutas definidas.")
else:
    # --- 3. SLIDER ---
    
    # Etiquetas personalizadas para cada punto del slider para mejorar la UX
    slider_labels = {
        1: "Primer Hito",
        2: "Segundo Hito",
        3: "Tercer Hito",
        4: "Cuarto Hito",
        5: "Quinto Hito"
    }
    
    # Creamos el slider. El valor inicial será 1.
    selected_point = st.slider(
        "Selecciona el punto de la línea de tiempo:",
        min_value=1,
        max_value=5,
        step=1,
        value=1 # Inicia en el primer punto
    )
    
    # --- 4. CÁLCULO Y CARGA DE IMAGEN ---
    
    # Git utiliza un índice base 0, por lo que restamos 1 al valor del slider.
    image_index = selected_point - 1
    image_path = image_files[image_index]
    
    # Título que cambia según el slider
    current_label = slider_labels.get(selected_point, f"Punto {selected_point}")
    st.subheader(f"Mostrando: **{current_label}**")

    try:
        # Carga la imagen usando la ruta relativa.
        st.image(
            image_path,
            caption=f"Imagen cargada para: {current_label}",
            use_column_width=True # Ajusta la imagen al ancho de la columna
        )
        
    except FileNotFoundError:
        st.error(
            f"❌ **Error de Archivo:** No se pudo encontrar el archivo en la ruta: `{image_path}`. "
            "Asegúrate de que el archivo exista y que la mayúscula/minúscula del nombre de la carpeta `timeline_images` sea idéntica."
        )
