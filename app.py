import streamlit as st
import sections.styles as styles
import sections.hero as hero
import sections.pain as pain
import sections.subscribe as subscribe
import sections.arsenal as arsenal
import sections.outcomes as outcomes
import sections.methodology as methodology  # <--- NUEVA SECCIÓN IMPORTADA
import sections.urgency as urgency
import sections.cta as cta

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Corazón de Campeón | VENTAJA INJUSTA para tu Hijo",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- INYECCIÓN DE ESTILOS CSS ---
st.markdown(styles.load_css(), unsafe_allow_html=True)

# --- RENDERIZADO DE SECCIONES (FLUJO DE VENTA MAESTRO) ---

# 1. EL GANCHO: Portada de alto impacto
hero.render()

# 2. EL PROBLEMA: Agitación del dolor (Bullying, Debilidad, Futuro)
pain.render()

# 3. LA OFERTA TEMPRANA: Botón impulsivo
subscribe.render()

# 4. LA SOLUCIÓN TÉCNICA: El "Arsenal" (Temario)
arsenal.render()

# 5. LA TRANSFORMACIÓN: Lo que se lleva el niño (Seguridad, Disciplina)
outcomes.render()

# 6. LA LOGÍSTICA: Cómo funciona (Presencial, Grupos pequeños)
methodology.render()  # <--- AQUÍ ENCAJA LA NUEVA SECCIÓN

# 7. LA ESCASEZ: Por qué actuar ahora
urgency.render()

# 8. EL CIERRE FINAL: Botones de WhatsApp y Respaldo Fundación
cta.render()