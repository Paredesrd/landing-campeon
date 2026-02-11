import streamlit as st
import styles as styles
import hero as hero
import pain as pain
import subscribe as subscribe
import arsenal as arsenal
import outcomes as outcomes
import methodology as methodology
import urgency as urgency
import cta as cta

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Corazón de Campeón | VENTAJA INJUSTA para tu Hijo",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- INYECCIÓN DE ESTILOS CSS ---
st.markdown(styles.load_css(), unsafe_allow_html=True)

# --- RENDERIZADO DE SECCIONES ---
hero.render()
pain.render()
subscribe.render()
arsenal.render()
outcomes.render()
methodology.render()
urgency.render()
cta.render()
