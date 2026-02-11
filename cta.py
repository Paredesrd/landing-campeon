import streamlit as st


def render():
    st.markdown("<br>", unsafe_allow_html=True)

    # CSS INTEGRADO (Pegado a la izquierda para evitar errores de renderizado)
    st.markdown("""
<style>
    /* --- ESTATUS DE CUPOS --- */
    .cta-container {
        border: 2px solid #D4AF37;
        background: linear-gradient(180deg, #111111 0%, #1E1E1E 100%);
        padding: 40px 20px;
        border-radius: 15px; 
        text-align: center;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
        margin: 20px 0;
    }
    /* Usamos DIV en lugar de H2 para evitar la cadenita */
    .cta-title {
        color: #FFFFFF;
        text-transform: uppercase;
        font-weight: 900;
        font-size: 1.8em;
        margin-bottom: 10px;
        line-height: 1.2;
        display: block;
    }
    .cta-text {
        color: #B0BEC5;
        font-size: 1.1em;
        margin-bottom: 25px;
    }
    .status-box {
        background-color: #212121;
        border: 1px solid #555;
        border-radius: 4px; 
        padding: 15px;
        margin: 0 auto 30px auto;
        max-width: 500px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }
    .status-dot {
        height: 12px;
        width: 12px;
        background-color: #FF4136;
        border-radius: 50%;
        box-shadow: 0 0 8px #FF4136;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 65, 54, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(255, 65, 54, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 65, 54, 0); }
    }
    .status-text {
        color: #E0E0E0;
        font-weight: bold;
        font-size: 0.95em;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* --- ESTILOS TARJETAS DE CONTACTO --- */
    .contact-header {
        text-align: center;
        color: #D4AF37;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        text-transform: uppercase;
        margin-top: 40px;
        margin-bottom: 25px;
        letter-spacing: 1px;
        font-size: 1.2em;
        border-bottom: 1px solid #333;
        padding-bottom: 10px;
        display: inline-block;
    }

    a.card-link {
        text-decoration: none;
        display: block;
        height: 100%;
    }

    .contact-card {
        background: transparent;
        border: 1px solid #444;
        border-radius: 4px;
        padding: 25px 15px;
        text-align: center;
        transition: all 0.3s ease;
        height: 100%;
        position: relative;
    }

    .contact-card:hover {
        border-color: #25D366; 
        background-color: rgba(37, 211, 102, 0.05);
        transform: translateY(-2px);
    }

    .contact-role {
        color: #D4AF37;
        font-size: 0.8em;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
        display: block;
        font-weight: 600;
    }
    .contact-name {
        color: white;
        font-weight: 900;
        font-size: 1.1em;
        display: block;
        margin-bottom: 20px;
    }

    .contact-cta-btn {
        background-color: transparent; 
        color: #25D366;                
        border: 1px solid #25D366;     
        padding: 10px 15px;
        border-radius: 3px;
        font-size: 0.85em;
        font-weight: bold;
        display: inline-block;
        width: 100%;
        text-transform: uppercase;
        transition: all 0.3s ease;
    }

    .contact-card:hover .contact-cta-btn {
        background-color: #25D366;
        color: white;
    }

    /* --- ESTILO FOOTER INSTITUCIONAL --- */
    .footer-label {
        color: #666; 
        font-size: 0.75em; 
        text-transform: uppercase; 
        letter-spacing: 2px; 
        margin-bottom: 10px; 
        font-weight: bold;
    }
    .footer-brand {
        color: #E0E0E0; 
        font-size: 1.1em; 
        font-weight: 900; 
        margin: 0; 
        letter-spacing: 1px;
        /* IMPORTANTE: Usamos div estilizado, no h3, para evitar cadenitas */
    }
</style>

<div class="cta-container">
<div class="cta-title">NO DEJES SU FUTURO PARA DESPUÉS</div>
<p class="cta-text">
    La próxima generación de líderes se está formando ahora mismo.<br>
    <b>¿Tu hijo estará dentro o se quedará fuera?</b>
</p>
<div class="status-box">
    <div class="status-dot"></div>
    <div class="status-text">CUPOS LIMITADOS POR GRUPO (ALTA EXCLUSIVIDAD)</div>
</div>
</div>
    """, unsafe_allow_html=True)

    # --- BLOQUE 2: CONTACTO ---
    st.markdown("<div style='text-align: center;'><div class='contact-header'>CONTÁCTATE CON NOSOTROS</div></div>",
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    msg_final = "Hola,%20quiero%20saber%20si%20a%C3%BAn%20tienen%20cupo%20disponible%20para%20el%20entrenamiento%20de%20Coraz%C3%B3n%20de%20Campe%C3%B3n."

    # TARJETA 1
    with col1:
        st.markdown(f"""
<a href="https://wa.me/59175008009?text={msg_final}" target="_blank" class="card-link">
    <div class="contact-card">
        <span class="contact-role">Coordinador Académico</span>
        <span class="contact-name">Lic. Domingo Paredes</span>
        <div class="contact-cta-btn">💬 Solicitar Entrevista</div>
    </div>
</a>
        """, unsafe_allow_html=True)

    # TARJETA 2
    with col2:
        st.markdown(f"""
<a href="https://wa.me/59175657140?text={msg_final}" target="_blank" class="card-link">
    <div class="contact-card">
        <span class="contact-role">Neuro - Coach</span>
        <span class="contact-name">Lic. Meliza Mafaile</span>
        <div class="contact-cta-btn">💬 Solicitar Entrevista</div>
    </div>
</a>
        """, unsafe_allow_html=True)

    # CIERRE DE SEGURIDAD + FUNDACIÓN ALETHEIA (TONO COACHING)
    st.markdown("""
<br>
<div style='text-align: center; opacity: 0.7; margin-bottom: 30px;'>
<p style='font-size: 0.8em; color: #888;'>
    🔒 Entrevista de Admisión Requerida.<br>
    No aceptamos a todos los postulantes, filtramos por actitud.
</p>
</div>

<div style='margin-top: 20px; padding-top: 20px; border-top: 1px solid #333; text-align: center;'>
<p class="footer-label">
    IMPULSADO POR:
</p>
<div class="footer-brand">
    🏛️ FUNDACIÓN ALETHEIA
</div>
<p style='color: #555; font-size: 0.7em; margin-top: 5px; font-style: italic;'>
    "Construyendo carácter, forjando destino."
</p>
</div>
<br><br>
    """, unsafe_allow_html=True)