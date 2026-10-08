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
# ESTILOS CSS PERSONALIZADOS — LUMINOSO, VERDE MENTA Y TEXTOS NEGROS
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Fondo principal ultra claro y fresco */
    .stApp {
        background-color: #588F31 !important;
    }

    /* Sidebar verde menta claro con TEXTO NEGRO/OSCURO */
    [data-testid="stSidebar"] {
        background-color: #EBF7F1 !important;
        border-right: 1px solid #D1EAD9;
    }
    
    [data-testid="stSidebar"] * {
        color: #111827 !important;
    }
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] h4, 
    [data-testid="stSidebar"] h5, 
    [data-testid="stSidebar"] h6 {
        color: #0C3823 !important;
        font-weight: 800 !important;
    }

    /* Encabezados y títulos principales */
    h1 {
        color: #0C3823 !important;
        font-weight: 800 !important;
        letter-spacing: -1px !important;
    }

    /* Hero Banner Luminoso */
    .hero-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #E2F5EA 100%);
        border: 1px solid #BCE5CC;
        border-radius: 16px;
        padding: 32px;
        margin-bottom: 28px;
        box-shadow: 0 10px 30px rgba(0, 209, 143, 0.08);
    }

    /* Tarjetas de Proyecto en Columnas */
    .project-card {
        background: #FFFFFF;
        border: 1px solid #E1EFE6;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 24px;
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);
    }
    .project-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 28px rgba(0, 209, 143, 0.15);
        border-color: #00D18F;
    }

    /* FORZAR TEXTO NEGRO/OSCURO DENTRO DE LAS COLUMNAS Y TARJETAS */
    .project-card h1, 
    .project-card h2, 
    .project-card h3, 
    .project-card h4, 
    .project-card h5, 
    .project-card h6 {
        color: #111827 !important;
        font-weight: 700 !important;
        margin-top: 6px !important;
        margin-bottom: 8px !important;
    }

    .project-card p, 
    .project-card span, 
    .project-card div {
        color: #1F2937 !important;
        font-size: 0.93rem !important;
        line-height: 1.5 !important;
    }

    /* Botones de Enlace Verde Menta */
    .btn-link {
        display: inline-block;
        width: 100%;
        text-align: center;
        background: linear-gradient(135deg, #00D18F 0%, #00B377 100%);
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
        padding: 10px 16px;
        border-radius: 10px;
        text-decoration: none !important;
        margin-top: 12px;
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
        padding: 4px 10px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 8px;
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
    st.markdown("### 🌿 Portafolio #1")
    st.markdown("#### **Susana Marín**")
    st.caption("Interfaces Multimodales & Visión por Computadora")
    st.divider()

    st.markdown("##### 💡 **Acerca de este espacio**")
    st.write(
        "Este portafolio reúne los proyectos e hitos desarrollados durante el curso de "
        "**Interfaces Multimodales**, donde combino programación, diseño interactivo "
        "e Inteligencia Artificial para crear experiencias digitales únicas."
    )

    st.markdown("##### 🚀 **¿Qué encontrarás aquí?**")
    st.markdown("""
    1. 🗣️ **Voz & Audio:** Conversión de Texto a Voz (TTS) y Voz a Texto (STT).
    2. 🌐 **Traducción:** Herramientas políglotas multilingües.
    3. 🧠 **Análisis de Texto:** Proceso TF-IDF y análisis de sentimientos.
    4. 🔍 **Visión IA:** Reconocimiento de objetos con YOLO y clasificadores.
    """)

    st.divider()
    st.caption("✨ *Diseñado con Streamlit & IA*")


# ─────────────────────────────────────────────
# HERO BANNER / ENCABEZADO
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero-card">
    <span class="badge-tag">✨ Portafolio Interactivo</span>
    <h1 style="margin: 4px 0 10px 0;">Ecosistema de Aplicaciones de IA 🍃</h1>
    <p style="font-size: 1.05rem; color: #1F2937 !important; margin-bottom: 16px;">
        Explora una colección de soluciones inteligentes enfocadas en voz, visión artificial, procesamiento de lenguaje natural e interacción multimodal.
    </p>
</div>
""", unsafe_allow_html=True)

# Proyecto Homenaje Perritos (Enlace Principal)
url_ia = "https://eusbfeqb6hwwjjsjo6gaed.streamlit.app/"
st.markdown(f"""
<div style="background: #FFFFFF; border-left: 5px solid #00D18F; border-radius: 12px; padding: 18px 24px; margin-bottom: 32px; box-shadow: 0 2px 10px rgba(0,0,0,0.03);">
    <h4 style="margin:0; color:#111827 !important; font-weight:700;">🐶 Homenaje Canino — Primer Proyecto Streamlit & Git</h4>
    <p style="margin:6px 0 12px 0; color:#1F2937 !important; font-size: 0.95rem;">
        Página pionera desarrollada con GitHub y Streamlit, potenciada con IA en homenaje a nuestros compañeros de cuatro patas.
    </p>
    <a href="{url_ia}" target="_blank" class="btn-link" style="width: auto; padding: 8px 20px;">🐾 Explorar Proyecto Perritos</a>
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
    st.subheader("🍝 Receta Audible de Gnocchis")
    try:
        image = Image.open('TextoAVoz.webp')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.write("Convierte la lectura de una deliciosa receta de gnocchis a audio en tiempo real con un solo clic.")
    url = "https://receta-de-gnocchis.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">🔊 Escuchar Receta</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Proyecto 2: OCR Accesibilidad
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Accesibilidad & OCR</span>', unsafe_allow_html=True)
    st.subheader("🗣️ Asistente de Lectura & Mutismo")
    try:
        image = Image.open('OCR.jpg')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.write("Sistema de lectura asistida diseñado para convertir fragmentos de texto visual a voz para personas con necesidades del habla.")
    url = "https://repositorio-profe-ocr-audio.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">📖 Abrir Asistente OCR</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Proyecto 3: TF-IDF
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">PLN & Modelos</span>', unsafe_allow_html=True)
    st.subheader("🧠 Laboratorio TF-IDF")
    try:
        image = Image.open('cerebro.jpg')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.write("Aprende y experimenta el modelo mental detrás de la clasificación de preguntas y recuperación vectorial de información.")
    url = "https://respositorioclasificacion.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">📊 Analizar con TF-IDF</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ── COLUMNA 2 ──
with col2:
    # Proyecto 4: Torre de Babel
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Traducción & Voz</span>', unsafe_allow_html=True)
    st.subheader("🌍 Torre de Babel Políglota")
    try:
        image = Image.open('Traductor.webp')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.write("Graba tu voz y tradúcela de forma instantánea a múltiples idiomas, incluyendo Árabe, Catalán, Francés y más.")
    url = "https://repositorio-profe-traductor.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">🎙️ Probar Traductor de Voz</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Proyecto 5: Sentimientos
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Bienestar & Inglés</span>', unsafe_allow_html=True)
    st.subheader("💬 Terapeuta & English Journal")
    try:
        image = Image.open('sentimientos.webp')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.write("Expresa tus emociones en inglés para recibir orientación terapéutica mientras practicas la redacción en el idioma.")
    url = "https://repositoriosentimientos-bv9nizmnom63ycp7x7sdsf.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">🌿 Iniciar Sesión Terapéutica</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Proyecto 6: YOLO Inventario
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Visión IA & Stock</span>', unsafe_allow_html=True)
    st.subheader("📦 ScannerIA — Control de Stock")
    try:
        image = Image.open('inventario.avif')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.write("Auditoría visual automática en tiempo real para negocios y tiendas usando modelos YOLO de detección de objetos.")
    url = "https://repositorioyolo.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">🔍 Escanear Inventario</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ── COLUMNA 3 ──
with col3:
    # Proyecto 7: OCR Básico
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Visión Bilingüe</span>', unsafe_allow_html=True)
    st.subheader("📄 Reconocimiento Óptico OCR")
    try:
        image = Image.open('Chat_pdf.png')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.write("Herramienta directa para extraer texto de imágenes subidas o capturadas por cámara y convertirlo en síntesis de voz.")
    url = "https://rec-opt-car.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">📷 Probar OCR Estándar</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Proyecto 8: Nube de Palabras
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Narrativa & Texto</span>', unsafe_allow_html=True)
    st.subheader("🔮 Observatorio de Niebla")
    try:
        image = Image.open('Brujp.jpg')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.write("Adéntrate en la torre del Sabio Eldrin y materializa las palabras de tus textos en nubes de niebla mágica.")
    url = "https://repositorionube.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">🔮 Canalizar Niebla</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Proyecto 9: Teachable Machine
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<span class="badge-tag">Clasificador Facial</span>', unsafe_allow_html=True)
    st.subheader("👯 Reconocedor: Isa & Susa")
    try:
        image = Image.open('SusaIsa.jpeg')
        st.image(image, use_container_width=True)
    except Exception:
        pass
    st.write("Modelo de aprendizaje supervisado entrenado con Teachable Machine para clasificar y distinguir entre dos amigas.")
    url = "https://repositorioreconocimiento.streamlit.app/"
    st.markdown(f'<a href="{url}" target="_blank" class="btn-link">🤖 Probar Clasificador</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
