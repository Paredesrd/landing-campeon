import streamlit as st

def render():
    st.markdown("<br>", unsafe_allow_html=True)

    # HTML SIN ESPACIOS A LA IZQUIERDA (Evita errores de visualización)
    st.markdown("""
<style>
.method-title {
    color: #FFFFFF;
    text-transform: uppercase;
    font-weight: 900;
    font-size: 1.6em;
    margin-bottom: 10px;
    text-align: center;
    letter-spacing: 1px;
}
.method-subtitle {
    color: #B0BEC5;
    font-size: 1em;
    text-align: center;
    margin-bottom: 40px;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}
.feature-card {
    background-color: #161616;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 25px;
    text-align: left;
    transition: transform 0.3s ease;
    border-left: 3px solid #D4AF37;
}
.feature-card:hover {
    transform: translateY(-5px);
    background-color: #1a1a1a;
    border-color: #555;
}
.feature-icon {
    font-size: 1.5em;
    margin-bottom: 15px;
    display: block;
}
.feature-title {
    color: #E0E0E0;
    font-weight: 800;
    font-size: 1.1em;
    margin-bottom: 10px;
    text-transform: uppercase;
}
.feature-desc {
    color: #999;
    font-size: 0.9em;
    line-height: 1.6;
}
/* ESTILO PARA EL CUADRO DE FECHAS/LOGÍSTICA */
.logistics-box {
    background-color: #111;
    border: 1px dashed #555;
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    margin-top: 20px;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}
.logistics-title {
    color: #D4AF37;
    font-weight: bold;
    font-size: 1em;
    margin-bottom: 10px;
    text-transform: uppercase;
}
.logistics-text {
    color: #AAA;
    font-size: 0.9em;
    margin-bottom: 15px;
}
.logistics-btn {
    display: inline-block;
    background-color: #25D366;
    color: #fff !important;
    font-weight: bold;
    padding: 10px 20px;
    border-radius: 50px;
    text-decoration: none;
    font-size: 0.9em;
    transition: all 0.3s ease;
    border: 1px solid #1e9e50;
}
.logistics-btn:hover {
    background-color: #1e9e50;
    transform: scale(1.05);
}
</style>

<div class="method-title">ESTRUCTURA OPERATIVA</div>
<p class="method-subtitle">No es un curso de verano para pasar el rato. Es un sistema de entrenamiento diseñado para generar impacto real y medible.</p>

<div class="grid-container">
<div class="feature-card">
<span class="feature-icon">📍</span>
<div class="feature-title">100% PRESENCIAL</div>
<p class="feature-desc">El carácter no se forma por Zoom. Trabajamos cara a cara en Santa Cruz de la Sierra para corregir postura, tono de voz y lenguaje corporal en tiempo real.</p>
</div>
<div class="feature-card">
<span class="feature-icon">⚙️</span>
<div class="feature-title">DINÁMICA ACTIVA</div>
<p class="feature-desc">Cero teoría aburrida. Utilizamos role-playing, desafíos de equipo y situaciones controladas para que aprendan haciendo, no escuchando.</p>
</div>
<div class="feature-card">
<span class="feature-icon">🔒</span>
<div class="feature-title">GRUPOS REDUCIDOS</div>
<p class="feature-desc">Priorizamos la calidad sobre la cantidad. Pocos cupos por horario para garantizar que cada alumno reciba atención personalizada de los licenciados.</p>
</div>
</div>

<div class="logistics-box">
<div class="logistics-title">📅 ¿CUÁNDO EMPEZAMOS Y DÓNDE ES?</div>
<p class="logistics-text">
    Las fechas de inicio y la ubicación exacta de la sede se asignan según la edad de tu hijo y la disponibilidad del grupo.
</p>
<a href="https://wa.me/59175008009?text=Hola,%20quisiera%20conocer%20la%20Fecha%20de%20Inicio,%20Lugar%20y%20Horarios%20disponibles%20para%20el%20programa%20Corazón%20de%20Campeón." target="_blank" class="logistics-btn">
    📲 CONSULTAR PRÓXIMA CONVOCATORIA AQUÍ
</a>
</div>
    """, unsafe_allow_html=True)