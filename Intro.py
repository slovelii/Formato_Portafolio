import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Creación de interfaces multimadales - Portafolio #1 Susana Marín")
  parrafo = (
    "Esta página será el insumo para encontrar lo que he aprendido en las clases de interfaces "
    "multimodales, donde he podido desarrollar mi creatividad utilizando herramientas propias "
    "de la programación y la IA combinando estas con el diseño interactivo. "
  )
  st.write(parrafo)
  Lista = (
    "Algunas de las cosas que encontrarás son: "
    " 1. Conversiones de texto a voz y voz a texto. "
    " 2. Un traductor de muchas lenguas. "
    " 3. Reconocimientos de sentimientos y objetos. "
  )
  st.write(Lista)

url_ia="https://eusbfeqb6hwwjjsjo6gaed.streamlit.app/"
st.subheader("En este primer enlace encontrarás mi primer trabajo realizado con GitHUb y StreamLit, " 
             "potenciado por medio de Inteligencia artificial en el que rindo homenaje a perritos :) ")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Conversión de texto a voz: Receta de gnocchis")
 image = Image.open('TextoAVoz.webp')
 st.image(image, width=200)
 st.write("En el siguiente enlace encontrarás una deliciosa receta de gnocchis que podrás convertir a audio con un click") 
 url = "https://receta-de-gnocchis.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Lectura de texto: Ayuda a personas con mutismo")
 image = Image.open('OCR.jpg')
 st.image(image, width=200)
 st.write("En esta columna veremos una página que lee fragmentos de textos y ayuda a quienes más lo necesitan.") 
 url = "https://repositorio-profe-ocr-audio.streamlit.app/"
 st.write(f"OCR editado: [Enlace]({url})")

 st.subheader("Análisis de texto TF-IDF: Entendimiento del sistema ")
 image = Image.open('cerebro.jpg')
 st.image(image, width=200)
 st.write("Acá no sólo habrá una clasificación según preguntas, ¡También entenderás cómo sucede!") 
 url = "https://respositorioclasificacion.streamlit.app/"
 st.write(f"TF-IDF: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto: Torre de Babel")
 image = Image.open('Traductor.webp')
 st.image(image, width=200)
 st.write("Acá grabarás tu voz para convertirla a distintos idiomas. Ahora con Árabe, Catalán y Francés incluidos.") 
 url = "https://repositorio-profe-traductor.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Análisis de sentimientos: Terapeuta virtual y asistente en inglés")
 image = Image.open('sentimientos.webp')
 st.image(image, width=190)
 st.write("Comparte tus sentimientos en ginlés apra practicar el idioma y est terapeuta te dará tips") 
 url = "https://repositoriosentimientos-bv9nizmnom63ycp7x7sdsf.streamlit.app/"
 st.write(f"Análisis de sentimientos: [Enlace]({url})")

 st.subheader("Reconocimiento de objetos con YOLO: Contador de inventario")
 image = Image.open('inventario.avif')
 st.image(image, width=200)
 st.write("Si tienes una tienda y neceisstas un conteo rápido de inventario que hay en el momento, esta página es para ti.") 
 url = "https://repositorioyolo.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")


with col3: 
 st.subheader("Lectura de texto - Sin editar")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En esta columna veremos un OCR que lee el texto insertado y lo dice con audio.") 
 url = "https://rec-opt-car.streamlit.app/"
 st.write(f"OCR sin editar: [Enlace]({url})")

 st.subheader("Nube de palabras: Observatorio de Niebla y Palabras")
 image = Image.open('Brujp.jpg')
 st.image(image, width=200)
 st.write("Donde el sabio Eldrin extrae las palabras de tu conjuro.") 
 url = "https://repositorionube.streamlit.app/"
 st.write(f"Nube: [Enlace]({url})")
 
 st.subheader("Entrenando modelos con TM: Isa y Susa")
 image = Image.open('SusaIsa.jpeg')
 st.image(image, width=200)
 st.write("Este modelo fue entrenado para reconocer a dos amiga y ver quién es quién.") 
 url = "https://repositorioreconocimiento.streamlit.app/"
 st.write(f"Teachable Machine: [Enlace]({url})")


