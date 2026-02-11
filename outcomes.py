import streamlit as st


def render():
    st.markdown("<br>", unsafe_allow_html=True)

    # TÍTULO: EL RESULTADO TANGIBLE
    st.markdown("<div class='section-title'>🏆 EL RESULTADO: SEGURIDAD, DISCIPLINA Y CARÁCTER</div>",
                unsafe_allow_html=True)

    # MENSAJE DE FORTALEZA (Tu elección)
    st.markdown("""
    <p style='text-align: center; color: #B0BEC5; margin-bottom: 40px; font-size: 1.1em; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;'>
    En un mundo frágil, construimos fortaleza. Tu hijo desarrollará la <b>estructura mental necesaria</b> para afrontar cualquier desafío basándose en:
    </p>
    """, unsafe_allow_html=True)

    # COLUMNAS DE VALOR
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style='background-color: #161616; padding: 25px; border-radius: 6px; border: 1px solid #333; height: 100%; border-top: 4px solid #D4AF37;'>
            <h4 style='color: #D4AF37; text-align: center; margin-bottom: 20px; font-weight: 800; font-size: 1.2em; letter-spacing: 1px;'>LO QUE SIENTE (INTERNO)</h4>
            <ul style='list-style-type: none; padding: 0; color: #CCCCCC; line-height: 1.8; font-size: 0.95em;'>
                <li style='margin-bottom: 12px;'>✔️ <b>Autoconfianza Real:</b> Deja de depender de la validación externa o de los "likes".</li>
                <li style='margin-bottom: 12px;'>✔️ <b>Manejo de la Frustración:</b> Entiende que el error es parte del aprendizaje, no un motivo para rendirse.</li>
                <li style='margin-bottom: 12px;'>✔️ <b>Claridad Mental:</b> Aprende a tomar decisiones propias sin seguir ciegamente a los demás.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background-color: #161616; padding: 25px; border-radius: 6px; border: 1px solid #333; height: 100%; border-top: 4px solid #E0E0E0;'>
            <h4 style='color: #E0E0E0; text-align: center; margin-bottom: 20px; font-weight: 800; font-size: 1.2em; letter-spacing: 1px;'>LO QUE SE VE (EXTERNO)</h4>
            <ul style='list-style-type: none; padding: 0; color: #CCCCCC; line-height: 1.8; font-size: 0.95em;'>
                <li style='margin-bottom: 12px;'>✔️ <b>Presencia y Postura:</b> Camina, mira y habla con seguridad. Proyecta respeto inmediato.</li>
                <li style='margin-bottom: 12px;'>✔️ <b>Habilidades Sociales:</b> Capacidad para integrar equipos y liderar situaciones sociales.</li>
                <li style='margin-bottom: 12px;'>✔️ <b>Autodefensa Verbal:</b> Sabe poner límites firmes y frenar el abuso sin violencia.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # CIERRE DE LA SECCIÓN
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; padding: 15px; border-top: 1px solid #333; border-bottom: 1px solid #333;'>
        <p style='color: #888; margin: 0; font-size: 0.9em; letter-spacing: 0.5px;'>
            ESTO NO ES TEORÍA. ES PREPARACIÓN PARA LA VIDA ADULTA.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)