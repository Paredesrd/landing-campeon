import streamlit as st
from PIL import Image

def render():
    try:
        image = Image.open('img4.png')
        st.image(image, use_container_width=True)
    except FileNotFoundError:
        st.error("❌ Error: Falta la imagen 'img4.png'.")
        st.stop()

    # USAMOS DIVS EN LUGAR DE H1/H3 PARA EVITAR ENLACES AUTOMÁTICOS
    st.markdown("<div class='main-title'>CORAZÓN DE CAMPEÓN</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>EL ÚNICO ENTRENAMIENTO MENTAL DE ALTO RENDIMIENTO PARA NIÑOS</div>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>📍 Sede Exclusiva: Santa Cruz de la Sierra - Bolivia</p>", unsafe_allow_html=True)
    st.write("---")