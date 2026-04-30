import streamlit as st
import pandas as pd
from datetime import date

# 1. Configuración de la página y Logo [cite: 10]
st.set_page_config(page_title="Seguimiento de Obra - Masaveu", layout="centered")
st.title("👷 Control de Seguimiento de Obra")

# Aquí podrías poner la URL de la imagen de tu logo
# st.image("url_de_tu_logo.png", width=200) 

# 2. Identificación del trabajador y fecha [cite: 41, 42]
col1, col2 = st.columns(2)
with col1:
    nombre_trabajador = st.text_input("Nombre del Trabajador:")
with col2:
    fecha_envio = st.date_input("Fecha de envío:", date.today())

# 3. Desplegable de Tareas de Electricista [cite: 11, 12, 16, 21, 31]
tareas = [
    "Trazado y marcado de cajas, tubos y cuadros",
    "Ejecución rozas en paredes y techos",
    "Montaje de soportes",
    "Colocación tubos y conductos",
    "Tendido de cables",
    "Identificación y etiquetado",
    "Conexionado de cables en bornes o regletas",
    "Instalación y conexionado de mecanismos",
    "Fijación de carril DIN y mecanismos en cuadro eléctrico",
    "Cableado interno del cuadro eléctrico",
    "Configuración de equipos domóticos/automáticos",
    "Pruebas de continuidad",
    "Pruebas de aislamiento",
    "Verificación de tierras",
    "Pruebas de funcionamiento"
]
tarea_seleccionada = st.selectbox("Selecciona la tarea realizada:", tareas)

# 4. Desplegable de Estado de la Tarea [cite: 34, 35, 38, 40]
estados = [
    "Avance de la tarea en torno al 25% aprox.",
    "Avance de la tarea en torno al 50% aprox.",
    "Avance de la tarea en torno al 75% aprox.",
    "OK, finalizado sin errores",
    "Finalizado, pero con errores pendientes de corregir",
    "Finalizado y corregidos los errores"
]
estado_seleccionado = st.selectbox("Estado de avance:", estados)

# 5. Generación de Excel y Registro [cite: 43]
if st.button("Registrar y Generar Excel"):
    if nombre_trabajador:
        datos = {
            "Fecha": [fecha_envio],
            "Trabajador": [nombre_trabajador],
            "Tarea": [tarea_seleccionada],
            "Estado": [estado_seleccionado]
        }
        df = pd.DataFrame(datos)
        
        # Crear archivo Excel en memoria
        df.to_excel("informe_obra.xlsx", index=False)
        
        st.success("✅ Registro completado.")
        
        # Botón para descargar el archivo [cite: 43]
        with open("informe_obra.xlsx", "rb") as file:
            st.download_button(
                label="📥 Descargar Excel para el móvil",
                data=file,
                file_name=f"Obra_{fecha_envio}_{nombre_trabajador}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.error("Por favor, introduce tu nombre antes de registrar.")
