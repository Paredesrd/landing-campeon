import streamlit as st
import streamlit.components.v1 as components


def render():
    # Título de la sección
    st.markdown("<div class='section-title'>📅 NUESTRAS SESIONES DE COACHING (ENTRENAMIENTO):</div>",
                unsafe_allow_html=True)

    # --- DATOS DEL TEMARIO ---
    sesiones = [
        ("📍 SESIÓN 1: EL DESPERTAR DEL CAMPEÓN",
         "<strong>Presencia de Líder:</strong> Tu hijo aprenderá a proyectar seguridad total en solo 2 segundos, ganándose el respeto de todos antes de decir una sola palabra."),

        ("📍 SESIÓN 2: MIS PUNTOS FUERTES",
         "<strong>Ventaja Única:</strong> Rompemos la presión de 'ser perfecto'. Aprenderá a usar sus talentos naturales para destacar y ganar sin sufrir ni compararse con nadie."),

        ("📍 SESIÓN 3: DOMINIO EMOCIONAL",
         "<strong>Mente Fría:</strong> Entrenamos su cerebro para no bloquearse bajo presión. Aprenderá a calmarse y tomar decisiones inteligentes justo cuando otros pierden el control."),

        ("📍 SESIÓN 4: SABER PERDER Y LEVANTARSE",
         "<strong>Carácter Indestructible:</strong> Convertimos el error en gasolina. Dejará de sufrir por perder y usará cada caída como un impulso para levantarse más fuerte."),

        ("📍 SESIÓN 5: EL PODER DE LA DISCIPLINA",
         "<strong>Voluntad de Hierro:</strong> El fin de la pereza. Aprenderá a cumplir sus objetivos aunque no tenga ganas, logrando lo que el 99% abandona a mitad de camino."),

        ("📍 SESIÓN 6: CÓMO HACERME RESPETAR",
         "<strong>Respeto Absoluto:</strong> Enseñamos a tu hijo a poner límites firmes con su postura y su voz, frenando cualquier burla o falta de respeto sin necesidad de pelear."),

        ("📍 SESIÓN 7: LIDERAZGO Y EQUIPO",
         "<strong>Influencia Real:</strong> Dejará de ser uno más del montón para convertirse en el guía que une al equipo, inspira a los demás y los lleva a la victoria."),

        ("📍 SESIÓN 8: MISIÓN CUMPLIDA",
         "<strong>Confianza Blindada:</strong> Sellamos el curso con una seguridad total: tu hijo saldrá sabiendo que no solo sabe competir, sino que nació para ganar.")
    ]

    # --- HTML BOOTSTRAP ---
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            ::-webkit-scrollbar { display: none; }
            body {
                background-color: transparent;
                color: #E0E0E0;
                font-family: 'Helvetica Neue', sans-serif;
                overflow-y: scroll;
            }
            .accordion-item {
                background-color: transparent;
                border: none;
                margin-bottom: 8px;
            }
            .accordion-button {
                background-color: #212121 !important;
                color: #FFD700 !important;
                border: 1px solid #333;
                border-radius: 5px !important;
                font-weight: bold;
                font-size: 16px;
                box-shadow: none !important;
                transition: all 0.2s ease;
                padding: 12px 20px;
            }
            .accordion-button:hover {
                background-color: #333 !important;
                border-color: #FFD700;
            }
            /* Estado ABIERTO */
            .accordion-button:not(.collapsed) {
                background-color: #1a1a1a !important;
                color: #FFD700 !important;
                border-bottom: 2px solid #FFD700;
                border-bottom-left-radius: 0 !important;
                border-bottom-right-radius: 0 !important;
            }
            .accordion-button::after {
                background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23FFD700'%3e%3cpath fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e");
            }
            .accordion-body {
                background-color: #161616;
                color: #CCCCCC;
                border: 1px solid #333;
                border-top: none;
                padding: 15px;
                font-size: 15px;
                line-height: 1.5;
            }
            strong { color: #FFD700; }
        </style>
    </head>
    <body>
        <div class="accordion" id="accordionPanelsStayOpenExample">
    """

    for i, (titulo, contenido) in enumerate(sesiones):
        item_id = f"collapse{i}"
        header_id = f"heading{i}"

        # --- LÓGICA DE APERTURA POR DEFECTO ---
        # Si es el primero (i==0), NO lleva la clase 'collapsed' en el botón
        # y SÍ lleva la clase 'show' en el contenido div.
        if i == 0:
            btn_collapsed_class = ""
            aria_expanded = "true"
            div_show_class = "show"
        else:
            btn_collapsed_class = "collapsed"
            aria_expanded = "false"
            div_show_class = ""

        html_content += f"""
          <div class="accordion-item">
            <h2 class="accordion-header" id="{header_id}">
              <button class="accordion-button {btn_collapsed_class}" type="button" data-bs-toggle="collapse" data-bs-target="#{item_id}" aria-expanded="{aria_expanded}" aria-controls="{item_id}">
                {titulo}
              </button>
            </h2>
            <div id="{item_id}" class="accordion-collapse collapse {div_show_class}" aria-labelledby="{header_id}" data-bs-parent="#accordionPanelsStayOpenExample">
              <div class="accordion-body">
                {contenido}
              </div>
            </div>
          </div>
        """

    html_content += """
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

    components.html(html_content, height=540, scrolling=True)