import streamlit as st


def render():
    # Espaciado para separar del mensaje anterior
    st.markdown("<br>", unsafe_allow_html=True)

    # URL de Acción (Contactamos al Lic. Domingo como admisión principal)
    # El mensaje de WhatsApp ya va pre-redactado con intención de compra.
    url_action = "https://wa.me/59175008009?text=Hola,%20acabo%20de%20leer%20la%20oportunidad%20y%20quiero%20POSTULAR%20a%20mi%20hijo%20para%20el%20entrenamiento."

    # Botón de Alta Conversión
    st.link_button("🚀 QUIERO POSTULAR A MI HIJO AHORA", url_action)

    # Espaciado inferior
    st.markdown("<br>", unsafe_allow_html=True)