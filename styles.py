def load_css():
    return """
    <style>
        /* --- ESTRUCTURA BASE --- */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .block-container {
            padding-top: 0rem;
            padding-bottom: 2rem;
            max-width: 700px;
        }
        body {
            background-color: #0E0E0E; /* Negro aún más profundo */
            color: #E0E0E0;
            font-family: 'Helvetica Neue', sans-serif;
        }

        /* --- ANTI-ENLACES (SEGURIDAD TOTAL) --- */
        [data-testid="stHeaderAction"] { display: none !important; }
        h1 > a, h2 > a, h3 > a, h4 > a, h5 > a, h6 > a { display: none !important; pointer-events: none; }

        /* --- TIPOGRAFÍA --- */
        .main-title {
            font-size: 2.8em;
            font-weight: 900;
            color: #D4AF37; /* Oro Metálico Premium */
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.9);
            margin-bottom: 10px;
            line-height: 1.1;
        }

        .section-title {
            font-size: 1.4em;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            text-transform: uppercase;
            margin-top: 30px;
            margin-bottom: 20px;
            letter-spacing: 1.5px;
        }

        .sub-header {
            text-align: center;
            color: #9E9E9E;
            font-size: 1.0em;
            margin-bottom: 40px;
            font-weight: 400;
            letter-spacing: 1px;
        }

        /* --- NUEVA CAJA DE MANIFIESTO (PREMIUM) --- */
        .pain-box {
            background-color: #161616; /* Gris muy oscuro, casi negro */
            border: 1px solid #333; /* Borde sutil */
            border-left: 4px solid #D4AF37; /* Línea de poder dorada a la izquierda */
            padding: 30px;
            border-radius: 4px; /* Bordes más rectos, más serios */
            margin: 40px 0;
            text-align: left; /* Alineación profesional */
        }
        .pain-box strong {
            color: #D4AF37; /* Resaltados en oro */
            font-weight: 700;
        }
        .pain-box p {
            font-size: 1.15em;
            line-height: 1.6;
            color: #CCCCCC;
            margin-bottom: 15px;
        }
        .pain-box .highlight {
            font-size: 1.3em;
            color: #FFFFFF;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            display: block;
            margin-bottom: 15px;
        }

        /* --- ACORDEONES --- */
        .streamlit-expanderHeader {
            background-color: #161616;
            color: #D4AF37 !important;
            font-weight: bold;
            border: 1px solid #333;
            font-size: 1.1em;
        }
        .streamlit-expanderContent {
            background-color: #111;
            border-top: none;
            padding: 20px;
            border-bottom: 1px solid #333;
            border-left: 1px solid #333;
            border-right: 1px solid #333;
        }

        /* --- URGENCIA --- */
        .urgency-box {
            background: transparent;
            border: 2px solid #D4AF37;
            color: #D4AF37;
            padding: 20px;
            text-align: center;
            font-weight: bold;
            font-size: 1.2em;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin: 40px 0;
        }

        /* --- BOTONES --- */
        .stLinkButton > a {
            width: 100%;
            background: linear-gradient(90deg, #101010, #202020); /* Negro degradado */
            color: #D4AF37 !important; /* Texto Dorado */
            border: 1px solid #D4AF37; /* Borde Dorado */
            border-radius: 4px;
            padding: 18px 25px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 1.1em;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s ease;
        }
        .stLinkButton > a:hover {
            background: #D4AF37; /* Al pasar el mouse se vuelve dorado */
            color: #000000 !important; /* Texto negro */
            transform: translateY(-2px);
            box-shadow: 0 0 15px rgba(212, 175, 55, 0.4);
        }
    </style>
    """