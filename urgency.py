import streamlit as st

def render():
    st.markdown("""
    <div class="urgency-box">
        ⚠️ ALERTA: SOLO 12 CUPOS DISPONIBLES<br>
        (ESTO NO ES MARKETING FALSO. BUSCAMOS CALIDAD, NO CANTIDAD).
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #B0BEC5;'>Una vez se llenen los 12 espacios, cerramos inscripciones hasta la próxima temporada. Sin excepciones.</p>", unsafe_allow_html=True)