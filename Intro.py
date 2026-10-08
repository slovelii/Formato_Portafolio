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
# ESTILOS CSS PERSONALIZADOS (ALTA LEGIBILIDAD)
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #000000 !important;
    }

    /* Fondo principal ultra claro */
    .stApp {
        background-color: #52663D !important;
    }

    /* Sidebar verde menta claro con TEXTO NEGRO */
    [data-testid="stSidebar"] {
        background-color: #A8BA93 !important;
        border-right: 1px solid #D1EAD9;
    }
    
    [data-testid="stSidebar"] * {
        color: #000000 !important;
    }

    /* Hero Banner Luminoso */
    .hero-card {
        background: linear-gradient(135deg, #29331F 0%, #29331F 100%);
        border: 1px solid #BCE5CC;
        border-radius: 16px;
        padding: 32px;
        margin-bottom: 28px;
        box-shadow: 0 10px 30px rgba(0, 209, 143, 0.08);
    }

    /* Tarjetas de Proyecto */
    .project-card {
        background: #29331F !important;
        border: 1px solid #E1EFE6;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 24px;
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
    }
    .project-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 28px rgba(0, 209, 143, 0.2);
        border-color: #00D18F;
    }

    /* Botones de Enlace Verde Menta */
    .btn-link {
        display: block;
        width: 100%;
        text-align: center;
        background: linear-gradient(135deg, #00D18F 0%, #00B377 100%);
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        padding: 12px 16px;
        border-radius: 10px;
        text-decoration: none !important;
        margin-top: 14px;
        box-shadow: 0 4px 12px rgba(0, 209, 143, 0.25);
        transition: all 0.2s ease;
    }
    .btn-link:hover {
        background: linear-gradient(135deg, #00B377 0%, #008F5F 100%);
        box-shadow: 0 6px 18px rgba(0, 209, 143, 0.4);
        color: #FFFFFF !important;
    }

    /* Tags destacados */
    .badge-tag {
        background-color: #E2F5EA !important;
        color: #007A52 !important;
        font-size: 0.75rem !important;
        font-weight: 800 !important;
        padding: 4px 12px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Ajuste de imágenes redondeadas */
    [data-testid="stImage"] img {
        border-radius: 12px;
        object-fit: cover;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# BARRA LATERAL (SIDEBAR)
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("<h3 style='color:#000000 !important; font-weight:800;'>🌿 Portafolio #1</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#000000 !important; font-weight:700;'>Susana Marín</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color:#333333 !important; font-size:0.88rem;'>Interfaces Multimodales & Visión por Computadora</p>", unsafe_allow_html=True)
    st.divider()

    st.markdown("<h5 style='color:#000000 !important; font-weight:700;'>💡 Acerca de este espacio</h5>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color:#000000 !important; font-size:0.9rem; line-height:1.5;'>"
        "Este portafolio reúne los proyectos e hitos desarrollados durante el curso de "
        "<b>Interfaces Multimodales</b>, donde combino programación, diseño interactivo "
        "e Inteligencia Artificial para crear experiencias digitales únicas."
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown("<h5 style='color:#000000 !important; font-weight:700;'>🚀 ¿Qué encontrarás aquí?</h5>", unsafe_allow_html=True)
    st.markdown("""
    <ol style='color:#000000 !important; font-size:0.9rem; padding-left:18px;'>
        <li><b>Voz & Audio:</b> Conversión de Texto a Voz (TTS) y Voz a Texto (STT).</li>
        <li><b>Traducción:</b> Herramientas políglotas multilingües.</li>
        <li><b>Análisis de Texto:</b> Proceso TF-IDF y análisis de sentimientos.</li>
        <li><b>Visión IA:</b> Reconocimiento de objetos con YOLO y clasificadores.</li>
    </ol>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("<p style='color:#555555 !important; font-size:0.8rem;'>✨ Diseñado con Streamlit & IA</p>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HERO BANNER / ENCABEZADO
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero-card">
    <span class="badge-tag">✨ Portafolio Interactivo</span>
    <h1 style="margin: 4px 0 10px 0; color: #000000 !important; font-weight: 800;">Ecosistema de Aplicaciones de IA 🍃</h1>
    <p style="font-size: 1.05rem; color: #000000 !important; margin-bottom: 16px; line-height: 1.5;">
        Explora una colección de soluciones inteligentes enfocadas en voz, visión artificial, procesamiento de lenguaje natural e interacción multimodal.
    </p>
</div>
""", unsafe_allow_html=True)

# Proyecto Homenaje Perritos (Enlace Principal)
url_ia = "https://eusbfeqb6hwwjjsjo6gaed.streamlit.app/"
st.markdown(f"""
<div style="background: #29331F; border-left: 5px solid #00D18F; border-radius: 12px; padding: 20px 24px; margin-bottom: 32px; box-shadow: 0 2px 10px rgba(0,0,0,0.04);">
    <h3 style="margin:0; color:#000000 !important; font-weight:800; font-size: 1.2rem;">🐶 Homenaje Canino — Primer Proyecto Streamlit & Git</h3>
    <p style="margin:8px 0 14px 0; color:#000000 !important; font-size: 0.98rem; line-height: 1.5;">
        Página pionera desarrollada con GitHub y Streamlit, potenciada con IA en homenaje a nuestros compañeros de cuatro patas.
    </p>
    <a href="{url_ia}" target="_blank" class="btn-link" style="display:inline-block; width: auto; padding: 10px 24px;">🐾 Explorar Proyecto Perritos</a>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# GRID DE PROYECTOS (3 COLUMNAS)
# ─────────────────────────────────────────────
col1, col2, col3 = st.columns(3, gap="large")

# ── COLUMNA 1 ──
with col1:
    # Proyecto 1: Gnocchis
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Audio & Recetas</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#000000 !important; font-weight:800; font-size:1.15rem; margin:6px 0 10px 0;">🍝 Receta Audible de Gnocchis</h3>', unsafe_allow_html=True)
    try:
        image = Image.open('TextoAVoz.webp')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.markdown('<p style="color:#000000 !important; font-size:0.95rem; line-height:1.5; margin-top:10px;">Convierte la lectura de una deliciosa receta de gnocchis a audio en tiempo real con un solo clic.</p>', unsafe_allow_html=True)
    url = "https://receta-de-gnocchis.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">🔊 Escuchar Receta</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Proyecto 2: OCR Accesibilidad
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Accesibilidad & OCR</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#000000 !important; font-weight:800; font-size:1.15rem; margin:6px 0 10px 0;">🗣️ Asistente de Lectura & Mutismo</h3>', unsafe_allow_html=True)
    try:
        image = Image.open('OCR.jpg')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.markdown('<p style="color:#000000 !important; font-size:0.95rem; line-height:1.5; margin-top:10px;">Sistema de lectura asistida diseñado para convertir fragmentos de texto visual a voz para personas con necesidades del habla.</p>', unsafe_allow_html=True)
    url = "https://repositorio-profe-ocr-audio.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">📖 Abrir Asistente OCR</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Proyecto 3: TF-IDF
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">PLN & Modelos</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#000000 !important; font-weight:800; font-size:1.15rem; margin:6px 0 10px 0;">🧠 Laboratorio TF-IDF</h3>', unsafe_allow_html=True)
    try:
        image = Image.open('cerebro.jpg')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.markdown('<p style="color:#000000 !important; font-size:0.95rem; line-height:1.5; margin-top:10px;">Aprende y experimenta el modelo mental detrás de la clasificación de preguntas y recuperación vectorial de información.</p>', unsafe_allow_html=True)
    url = "https://respositorioclasificacion.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">📊 Analizar con TF-IDF</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ── COLUMNA 2 ──
with col2:
    # Proyecto 4: Torre de Babel
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Traducción & Voz</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#000000 !important; font-weight:800; font-size:1.15rem; margin:6px 0 10px 0;">🌍 Torre de Babel Políglota</h3>', unsafe_allow_html=True)
    try:
        image = Image.open('Traductor.webp')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.markdown('<p style="color:#000000 !important; font-size:0.95rem; line-height:1.5; margin-top:10px;">Graba tu voz y tradúcela de forma instantánea a múltiples idiomas, incluyendo Árabe, Catalán, Francés y más.</p>', unsafe_allow_html=True)
    url = "https://repositorio-profe-traductor.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">🎙️ Probar Traductor de Voz</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Proyecto 5: Sentimientos
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Bienestar & Inglés</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#000000 !important; font-weight:800; font-size:1.15rem; margin:6px 0 10px 0;">💬 Terapeuta & English Journal</h3>', unsafe_allow_html=True)
    try:
        image = Image.open('sentimientos.webp')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.markdown('<p style="color:#000000 !important; font-size:0.95rem; line-height:1.5; margin-top:10px;">Expresa tus emociones en inglés para recibir orientación terapéutica mientras practicas la redacción en el idioma.</p>', unsafe_allow_html=True)
    url = "https://repositoriosentimientos-bv9nizmnom63ycp7x7sdsf.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">🌿 Iniciar Sesión Terapéutica</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Proyecto 6: YOLO Inventario
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Visión IA & Stock</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#000000 !important; font-weight:800; font-size:1.15rem; margin:6px 0 10px 0;">📦 ScannerIA — Control de Stock</h3>', unsafe_allow_html=True)
    try:
        image = Image.open('inventario.avif')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.markdown('<p style="color:#000000 !important; font-size:0.95rem; line-height:1.5; margin-top:10px;">Auditoría visual automática en tiempo real para negocios y tiendas usando modelos YOLO de detección de objetos.</p>', unsafe_allow_html=True)
    url = "https://repositorioyolo.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">🔍 Escanear Inventario</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ── COLUMNA 3 ──
with col3:
    # Proyecto 7: OCR Básico
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Visión Bilingüe</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#000000 !important; font-weight:800; font-size:1.15rem; margin:6px 0 10px 0;">📄 Reconocimiento Óptico OCR</h3>', unsafe_allow_html=True)
    try:
        image = Image.open('Chat_pdf.png')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.markdown('<p style="color:#000000 !important; font-size:0.95rem; line-height:1.5; margin-top:10px;">Herramienta directa para extraer texto de imágenes subidas o capturadas por cámara y convertirlo en síntesis de voz.</p>', unsafe_allow_html=True)
    url = "https://rec-opt-car.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">📷 Probar OCR Estándar</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Proyecto 8: Nube de Palabras
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Narrativa & Texto</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#000000 !important; font-weight:800; font-size:1.15rem; margin:6px 0 10px 0;">🔮 Observatorio de Niebla</h3>', unsafe_allow_html=True)
    try:
        image = Image.open('Brujp.jpg')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.markdown('<p style="color:#000000 !important; font-size:0.95rem; line-height:1.5; margin-top:10px;">Adéntrate en la torre del Sabio Eldrin y materializa las palabras de tus textos en nubes de niebla mágica.</p>', unsafe_allow_html=True)
    url = "https://repositorionube.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">🔮 Canalizar Niebla</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Proyecto 9: Teachable Machine
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Clasificador Facial</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#000000 !important; font-weight:800; font-size:1.15rem; margin:6px 0 10px 0;">👯 Reconocedor: Isa & Susa</h3>', unsafe_allow_html=True)
    try:
        image = Image.open('SusaIsa.jpeg')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.markdown('<p style="color:#000000 !important; font-size:0.95rem; line-height:1.5; margin-top:10px;">Modelo de aprendizaje supervisado entrenado con Teachable Machine para clasificar y distinguir entre dos amigas.</p>', unsafe_allow_html=True)
    url = "https://repositorioreconocimiento.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">🤖 Probar Clasificador</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
