import streamlit as st
import base64
from pathlib import Path

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
# ESTILOS CSS PERSONALIZADOS
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #000000 !important;
    }

    .stApp {
        background-color: #52663D !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #A8BA93 !important;
        border-right: 1px solid #D1EAD9;
    }
    
    [data-testid="stSidebar"] * {
        color: #000000 !important;
    }

    /* Tabs Personalizadas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #29331F;
        border-radius: 10px;
        color: #FFFFFF !important;
        padding: 10px 20px;
        font-weight: 700;
        border: 1px solid #3E4D2F;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00D18F !important;
        color: #000000 !important;
    }

    /* Tarjetas de Proyecto Amplias y Uniformes */
    .project-card {
        background: #29331F !important;
        border: 1px solid #E1EFE6;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
        min-height: 480px;
    }

    .project-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 28px rgba(0, 209, 143, 0.2);
        border-color: #00D18F;
    }

    /* Imágenes uniformes dentro de la tarjeta */
    .card-img {
        width: 100% !important;
        height: 160px !important;
        object-fit: cover !important;
        border-radius: 10px !important;
        margin-top: 8px;
        margin-bottom: 8px;
    }

    .card-img-placeholder {
        background: #1E2617;
        height: 160px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #888888;
        font-size: 0.9rem;
        border: 1px dashed #3E4D2F;
        margin-top: 8px;
        margin-bottom: 8px;
    }

    /* Hero Banner */
    .hero-card {
        background: linear-gradient(135deg, #29331F 0%, #29331F 100%);
        border: 1px solid #BCE5CC;
        border-radius: 16px;
        padding: 32px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0, 209, 143, 0.08);
    }

    /* Botones */
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
    .btn-link.disabled {
        background: #4A5543 !important;
        color: #888888 !important;
        cursor: not-allowed;
        box-shadow: none;
    }

    /* Tags */
    .badge-tag {
        background-color: #E2F5EA !important;
        color: #007A52 !important;
        font-size: 0.75rem !important;
        font-weight: 800 !important;
        padding: 4px 12px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# BARRA LATERAL (SIDEBAR)
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("<h3 style='color:#000000 !important; font-weight:800;'>🌿 Portafolio IA</h3>", unsafe_allow_html=True)
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

    st.markdown("<h5 style='color:#000000 !important; font-weight:700;'>🚀 Contenido</h5>", unsafe_allow_html=True)
    st.markdown("""
    <ol style='color:#000000 !important; font-size:0.9rem; padding-left:18px;'>
        <li><b>Parte 1:</b> Aplicaciones Multimodales (9 Proyectos)</li>
        <li><b>Parte 2:</b> Próximos Desarrollos (8 Espacios)</li>
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
    <h1 style="margin: 4px 0 10px 0; color: #FFFFFF !important; font-weight: 800;">Ecosistema de Aplicaciones de IA 🍃</h1>
    <p style="font-size: 1.05rem; color: #E0E0E0 !important; margin-bottom: 0px; line-height: 1.5;">
        Explora una colección de soluciones inteligentes enfocadas en voz, visión artificial, procesamiento de lenguaje natural e interacción multimodal.
    </p>
</div>
""", unsafe_allow_html=True)

# Proyecto Homenaje Perritos
url_ia = "https://eusbfeqb6hwwjjsjo6gaed.streamlit.app/"
st.markdown(f"""
<div style="background: #29331F; border-left: 5px solid #00D18F; border-radius: 12px; padding: 20px 24px; margin-bottom: 28px; box-shadow: 0 2px 10px rgba(0,0,0,0.04);">
    <h3 style="margin:0; color:#FFFFFF !important; font-weight:800; font-size: 1.2rem;">🐶 Homenaje Canino — Primer Proyecto Streamlit & Git</h3>
    <p style="margin:8px 0 14px 0; color:#DDDDDD !important; font-size: 0.98rem; line-height: 1.5;">
        Página pionera desarrollada con GitHub y Streamlit, potenciada con IA en homenaje a nuestros compañeros de cuatro patas.
    </p>
    <a href="{url_ia}" target="_blank" class="btn-link" style="display:inline-block; width: auto; padding: 10px 24px;">🐾 Explorar Proyecto Perritos</a>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FUNCIÓN AUXILIAR PARA CONVERTIR IMAGEN A BASE64
# ─────────────────────────────────────────────
def get_image_base64(img_path):
    if img_path and Path(img_path).exists():
        with open(img_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        ext = img_path.split('.')[-1].lower()
        if ext == 'jpg': 
            ext = 'jpeg'
        elif ext == 'avif':
            ext = 'avif'
        elif ext == 'webp':
            ext = 'webp'
        return f"data:image/{ext};base64,{encoded}"
    return ""


# ─────────────────────────────────────────────
# FUNCIÓN PARA RENDERIZAR TARJETAS EN UN SOLO BLOQUE HTML
# ─────────────────────────────────────────────
def render_card(tag, title, img_path, description, btn_text, url, disabled=False):
    img_src = get_image_base64(img_path)
    
    if img_src:
        img_html = f'<img src="{img_src}" class="card-img">'
    else:
        img_html = '<div class="card-img-placeholder">🔒 Espacio Vacío / Imagen no encontrada</div>'
    
    if not disabled:
        btn_html = f'<a href="{url}" target="_blank" class="btn-link">{btn_text}</a>'
    else:
        btn_html = f'<a class="btn-link disabled">{btn_text}</a>'

    html_code = f"""
    <div class="project-card">
        <div>
            <span class="badge-tag">{tag}</span>
            <h3 style="color:#FFFFFF !important; font-weight:800; font-size:1.15rem; margin:6px 0 10px 0;">{title}</h3>
            {img_html}
            <p style="color:#CCCCCC !important; font-size:0.92rem; line-height:1.5; margin-top:12px; margin-bottom:12px;">{description}</p>
        </div>
        <div>
            {btn_html}
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# PESTAÑAS DEL PORTAFOLIO
# ─────────────────────────────────────────────
tab1, tab2 = st.tabs(["📌 Parte 1: Proyectos Actuales", "🚀 Parte 2: Próximos Desarrollos"])

# ── PESTAÑA 1: PROYECTOS ACTUALES ──
with tab1:
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        render_card("Audio & Recetas", "🍝 Receta Audible de Gnocchis", "TextoAVoz.webp",
                    "Convierte la lectura de una deliciosa receta de gnocchis a audio en tiempo real con un solo clic.",
                    "🔊 Escuchar Receta", "https://receta-de-gnocchis.streamlit.app/")
    with c2:
        render_card("Traducción & Voz", "🌍 Torre de Babel Políglota", "Traductor.webp",
                    "Graba tu voz y tradúcela de forma instantánea a múltiples idiomas, incluyendo Árabe, Catalán, Francés y más.",
                    "🎙️ Probar Traductor", "https://repositorio-profe-traductor.streamlit.app/")
    with c3:
        render_card("Visión Bilingüe", "📄 Reconocimiento Óptico OCR", "Chat_pdf.png",
                    "Herramienta directa para extraer texto de imágenes subidas o capturadas por cámara y convertirlo en síntesis de voz.",
                    "📷 Probar OCR Estándar", "https://rec-opt-car.streamlit.app/")

    st.markdown("<br>", unsafe_allow_html=True)

    c4, c5, c6 = st.columns(3, gap="medium")
    with c4:
        render_card("Accesibilidad & OCR", "🗣️ Asistente de Lectura & Mutismo", "OCR.jpg",
                    "Sistema de lectura asistida diseñado para convertir fragmentos de texto visual a voz para personas con necesidades del habla.",
                    "📖 Abrir Asistente OCR", "https://repositorio-profe-ocr-audio.streamlit.app/")
    with c5:
        render_card("Bienestar & Inglés", "💬 Terapeuta & English Journal", "sentimientos.webp",
                    "Expresa tus emociones en inglés para recibir orientación terapéutica mientras practicas la redacción en el idioma.",
                    "🌿 Iniciar Sesión", "https://repositoriosentimientos-bv9nizmnom63ycp7x7sdsf.streamlit.app/")
    with c6:
        render_card("Narrativa & Texto", "🔮 Observatorio de Niebla", "Brujp.jpg",
                    "Adéntrate en la torre del Sabio Eldrin y materializa las palabras de tus textos en nubes de niebla mágica.",
                    "🔮 Canalizar Niebla", "https://repositorionube.streamlit.app/")

    st.markdown("<br>", unsafe_allow_html=True)

    c7, c8, c9 = st.columns(3, gap="medium")
    with c7:
        render_card("PLN & Modelos", "🧠 Laboratorio TF-IDF", "cerebro.jpg",
                    "Aprende y experimenta el modelo mental detrás de la clasificación de preguntas y recuperación vectorial de información.",
                    "📊 Analizar TF-IDF", "https://respositorioclasificacion.streamlit.app/")
    with c8:
        render_card("Visión IA & Stock", "📦 ScannerIA — Control de Stock", "inventario.avif",
                    "Auditoría visual automática en tiempo real para negocios y tiendas usando modelos YOLO de detección de objetos.",
                    "🔍 Escanear Inventario", "https://repositorioyolo.streamlit.app/")
    with c9:
        render_card("Clasificador Facial", "👯 Reconocedor: Isa & Susa", "SusaIsa.jpeg",
                    "Modelo de aprendizaje supervisado entrenado con Teachable Machine para clasificar y distinguir entre dos amigas.",
                    "🤖 Probar Clasificador", "https://rpZELkorMwhkkpShF5PvT8YnqRCupnLTNG.streamlit.app/")


# ── PESTAÑA 2: SEGUNDA PARTE (8 CUADROS VACÍOS AMPLIOS) ──
with tab2:
    st.markdown("<h3 style='color:#FFFFFF; font-weight:800; margin-bottom:20px;'>🛠️ Espacio de Desarrollo — Parte 2</h3>", unsafe_allow_html=True)
    
    p1, p2, p3, p4 = st.columns(4, gap="medium")
    with p1:
        render_card("Próximamente", "Proyecto 10", "", "Espacio reservado para tu próximo proyecto de Inteligencia Artificial.", "🔒 En Desarrollo", "#", disabled=True)
    with p2:
        render_card("Próximamente", "Proyecto 11", "", "Espacio reservado para tu próximo proyecto de Inteligencia Artificial.", "🔒 En Desarrollo", "#", disabled=True)
    with p3:
        render_card("Próximamente", "Proyecto 12", "", "Espacio reservado para tu próximo proyecto de Inteligencia Artificial.", "🔒 En Desarrollo", "#", disabled=True)
    with p4:
        render_card("Próximamente", "Proyecto 13", "", "Espacio reservado para tu próximo proyecto de Inteligencia Artificial.", "🔒 En Desarrollo", "#", disabled=True)

    st.markdown("<br>", unsafe_allow_html=True)

    p5, p6, p7, p8 = st.columns(4, gap="medium")
    with p5:
        render_card("Próximamente", "Proyecto 14", "", "Espacio reservado para tu próximo proyecto de Inteligencia Artificial.", "🔒 En Desarrollo", "#", disabled=True)
    with p6:
        render_card("Próximamente", "Proyecto 15", "", "Espacio reservado para tu próximo proyecto de Inteligencia Artificial.", "🔒 En Desarrollo", "#", disabled=True)
    with p7:
        render_card("Próximamente", "Proyecto 16", "", "Espacio reservado para tu próximo proyecto de Inteligencia Artificial.", "🔒 En Desarrollo", "#", disabled=True)
    with p8:
        render_card("Próximamente", "Proyecto 17", "", "Espacio reservado para tu próximo proyecto de Inteligencia Artificial.", "🔒 En Desarrollo", "#", disabled=True)
