import streamlit as st
from PIL import Image

# ─────────────────────────────────────────────
# CONFIGURACIÓN DE PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Portafolio IA — Susana Marín",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# ESTILOS CSS PERSONALIZADOS (DISEÑO LIGERO Y MODERNO)
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #2C3E35 !important;
    }

    /* Fondo principal limpio y luminoso */
    .stApp {
        background-color: #F8F9F6 !important;
    }

    /* Sidebar suave en tonos salvia */
    [data-testid="stSidebar"] {
        background-color: #EBF0E8 !important;
        border-right: 1px solid #D8E2D4;
    }
    
    [data-testid="stSidebar"] * {
        color: #2C3E35 !important;
    }

    /* Tarjetas de Proyecto Minimalistas */
    .project-card {
        background: #FFFFFF !important;
        border: 1px solid #E2EAE0;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 24px;
        height: 100%;
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        box-shadow: 0 4px 12px rgba(44, 62, 53, 0.04);
    }
    
    .project-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 24px rgba(46, 125, 50, 0.12);
        border-color: #2E7D32;
    }

    /* Hero Banner Elegante */
    .hero-card {
        background: linear-gradient(135deg, #EAEFE6 0%, #D8E4D3 100%);
        border: 1px solid #C4D7BC;
        border-radius: 16px;
        padding: 32px;
        margin-bottom: 28px;
        box-shadow: 0 6px 20px rgba(44, 62, 53, 0.04);
    }

    /* Botones de Enlace Modernos */
    .btn-link {
        display: block;
        width: 100%;
        text-align: center;
        background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%);
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
        padding: 10px 14px;
        border-radius: 10px;
        text-decoration: none !important;
        margin-top: 14px;
        box-shadow: 0 4px 12px rgba(46, 125, 50, 0.2);
        transition: all 0.2s ease;
    }
    .btn-link:hover {
        background: linear-gradient(135deg, #1B5E20 0%, #0D3B12 100%);
        box-shadow: 0 6px 16px rgba(46, 125, 50, 0.35);
        color: #FFFFFF !important;
    }

    /* Tags / Badges */
    .badge-tag {
        background-color: #E8F5E9 !important;
        color: #1B5E20 !important;
        font-size: 0.72rem !important;
        font-weight: 800 !important;
        padding: 4px 10px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Ajuste de imágenes */
    [data-testid="stImage"] img {
        border-radius: 10px;
        object-fit: cover;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# BARRA LATERAL (SIDEBAR)
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("<h3 style='font-weight:800;'>🌿 Portafolio IA</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='font-weight:700;'>Susana Marín</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:0.88rem;'>Interfaces Multimodales & Visión por Computadora</p>", unsafe_allow_html=True)
    st.divider()

    st.markdown("<h5 style='font-weight:700;'>💡 Acerca de este espacio</h5>", unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size:0.9rem; line-height:1.5;'>"
        "Este portafolio reúne los proyectos e hitos desarrollados durante el curso de "
        "<b>Interfaces Multimodales</b>, combinando programación, diseño interactivo "
        "e Inteligencia Artificial."
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown("<h5 style='font-weight:700;'>🚀 ¿Qué encontrarás aquí?</h5>", unsafe_allow_html=True)
    st.markdown("""
    <ol style='font-size:0.88rem; padding-left:18px; line-height: 1.6;'>
        <li><b>Voz & Audio:</b> TTS y STT.</li>
        <li><b>Traducción:</b> Herramientas políglotas.</li>
        <li><b>Análisis de Texto:</b> TF-IDF & sentimientos.</li>
        <li><b>Visión IA:</b> YOLO y clasificadores.</li>
    </ol>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("<p style='font-size:0.8rem; color:#555;'>✨ Diseñado con Streamlit & IA</p>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HERO BANNER / ENCABEZADO
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero-card">
    <span class="badge-tag">✨ Portafolio Interactivo</span>
    <h1 style="margin: 4px 0 10px 0; font-weight: 800; color: #1B5E20;">Ecosistema de Aplicaciones de IA 🍃</h1>
    <p style="font-size: 1.05rem; margin-bottom: 12px; line-height: 1.5; color: #2C3E35;">
        Explora una colección de soluciones inteligentes enfocadas en voz, visión artificial, procesamiento de lenguaje natural e interacción multimodal.
    </p>
</div>
""", unsafe_allow_html=True)

# Proyecto Destacado Principal
url_ia = "https://eusbfeqb6hwwjjsjo6gaed.streamlit.app/"
st.markdown(f"""
<div style="background: #FFFFFF; border-left: 5px solid #2E7D32; border-radius: 12px; padding: 18px 22px; margin-bottom: 28px; box-shadow: 0 4px 12px rgba(44,62,53,0.04);">
    <h3 style="margin:0; font-weight:800; font-size: 1.15rem; color:#1B5E20;">🐶 Homenaje Canino — Primer Proyecto Streamlit & Git</h3>
    <p style="margin:6px 0 12px 0; font-size: 0.95rem; line-height: 1.5;">
        Página pionera desarrollada con GitHub y Streamlit, potenciada con IA en homenaje a nuestros compañeros de cuatro patas.
    </p>
    <a href="{url_ia}" target="_blank" class="btn-link" style="display:inline-block; width: auto; padding: 8px 20px;">🐾 Explorar Proyecto Perritos</a>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# DEFINICIÓN DE PROYECTOS POR COLUMNAS (4 COLUMNAS)
# ─────────────────────────────────────────────
# Cada columna contiene una lista de diccionarios con la info de los proyectos.
# Puedes editar, añadir o quitar proyectos aquí de forma muy sencilla.

col1_proyectos = [
    {
        "tag": "Audio & Recetas",
        "title": "🍝 Receta Audible de Gnocchis",
        "img": "TextoAVoz.webp",
        "desc": "Convierte la lectura de una deliciosa receta de gnocchis a audio en tiempo real con un solo clic.",
        "url": "https://receta-de-gnocchis.streamlit.app/",
        "btn_text": "🔊 Escuchar Receta"
    },
    {
        "tag": "Accesibilidad & OCR",
        "title": "🗣️ Asistente de Lectura & Mutismo",
        "img": "OCR.jpg",
        "desc": "Sistema de lectura asistida diseñado para convertir fragmentos de texto visual a voz para personas con necesidades del habla.",
        "url": "https://repositorio-profe-ocr-audio.streamlit.app/",
        "btn_text": "📖 Abrir Asistente OCR"
    },
    {
        "tag": "PLN & Modelos",
        "title": "🧠 Laboratorio TF-IDF",
        "img": "cerebro.jpg",
        "desc": "Aprende y experimenta el modelo mental detrás de la clasificación de preguntas y recuperación vectorial.",
        "url": "https://respositorioclasificacion.streamlit.app/",
        "btn_text": "📊 Analizar con TF-IDF"
    }
]

col2_proyectos = [
    {
        "tag": "Traducción & Voz",
        "title": "🌍 Torre de Babel Políglota",
        "img": "Traductor.webp",
        "desc": "Graba tu voz y tradúcela de forma instantánea a múltiples idiomas, incluyendo Árabe, Catalán, Francés y más.",
        "url": "https://repositorio-profe-traductor.streamlit.app/",
        "btn_text": "🎙️ Probar Traductor"
    },
    {
        "tag": "Bienestar & Inglés",
        "title": "💬 Terapeuta & English Journal",
        "img": "sentimientos.webp",
        "desc": "Expresa tus emociones en inglés para recibir orientación terapéutica mientras practicas la redacción.",
        "url": "https://repositoriosentimientos-bv9nizmnom63ycp7x7sdsf.streamlit.app/",
        "btn_text": "🌿 Sesión Terapéutica"
    },
    {
        "tag": "Visión IA & Stock",
        "title": "📦 ScannerIA — Control de Stock",
        "img": "inventario.avif",
        "desc": "Auditoría visual automática en tiempo real para negocios y tiendas usando modelos YOLO de detección.",
        "url": "https://repositorioyolo.streamlit.app/",
        "btn_text": "🔍 Escanear Inventario"
    }
]

col3_proyectos = [
    {
        "tag": "Visión Bilingüe",
        "title": "📄 Reconocimiento Óptico OCR",
        "img": "Chat_pdf.png",
        "desc": "Herramienta directa para extraer texto de imágenes subidas o capturadas y convertirlo en síntesis de voz.",
        "url": "https://rec-opt-car.streamlit.app/",
        "btn_text": "📷 Probar OCR Estándar"
    },
    {
        "tag": "Narrativa & Texto",
        "title": "🔮 Observatorio de Niebla",
        "img": "Brujp.jpg",
        "desc": "Adéntrate en la torre del Sabio Eldrin y materializa las palabras de tus textos en nubes de niebla mágica.",
        "url": "https://repositorionube.streamlit.app/",
        "btn_text": "🔮 Canalizar Niebla"
    },
    {
        "tag": "Clasificador Facial",
        "title": "👯 Reconocedor: Isa & Susa",
        "img": "SusaIsa.jpeg",
        "desc": "Modelo de aprendizaje supervisado entrenado con Teachable Machine para clasificar entre dos amigas.",
        "url": "https://rpZELkorMwhkkpShF5PvT8YnqRCupnLTNG.streamlit.app/",
        "btn_text": "🤖 Probar Clasificador"
    }
]

# 🌟 NUEVA COLUMNA PERSONALIZABLE (Columna 4)
col4_proyectos = [
    {
        "tag": "Deteccióon de escritura",
        "title": "Adivinador de números con IA",
        "img": "", # Puedes poner el nombre de una imagen o dejar vacío
        "desc": "Este es un espacio reservado para que agregues tus propias ideas, nuevos despliegues o futuros experimentos.",
        "url": "https://tu-enlace-streamlit.streamlit.app/",
        "btn_text": "✨ Ver Proyecto"
    },
    {
        "tag": "Innovación IA",
        "title": "💡 Asistente IA a Medida",
        "img": "",
        "desc": "Modifica este texto y los enlaces directamente en el código para adaptarlo a cualquier nueva práctica del curso.",
        "url": "https://tu-enlace-streamlit.streamlit.app/",
        "btn_text": "🛠️ Explorar Demo"
    }
]


# ─────────────────────────────────────────────
# RENDERIZADO DEL GRID DE 4 COLUMNAS
# ─────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4, gap="medium")

# Función auxiliar para renderizar tarjetas ordenadamente
def render_tarjetas(columna_streamlit, lista_proyectos):
    with columna_streamlit:
        for p in lista_proyectos:
            st.markdown('<div class="project-card">', unsafe_allow_html=True)
            st.markdown(f'<span class="badge-tag">{p["tag"]}</span>', unsafe_allow_html=True)
            st.markdown(f'<h3 style="font-weight:800; font-size:1.1rem; margin:6px 0 8px 0; color:#1B5E20;">{p["title"]}</h3>', unsafe_allow_html=True)
            
            # Intenta cargar la imagen si existe
            if p["img"]:
                try:
                    image = Image.open(p["img"])
                    st.image(image, use_container_width=True)
                except Exception:
                    pass
                    
            st.markdown(f'<p style="font-size:0.9rem; line-height:1.4; margin-top:8px;">{p["desc"]}</p>', unsafe_allow_html=True)
            st.markdown(f'<a href="{p["url"]}" target="_blank" class="btn-link">{p["btn_text"]}</a>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# Renderizar las 4 columnas
render_tarjetas(c1, col1_proyectos)
render_tarjetas(c2, col2_proyectos)
render_tarjetas(c3, col3_proyectos)
render_tarjetas(c4, col4_proyectos)
