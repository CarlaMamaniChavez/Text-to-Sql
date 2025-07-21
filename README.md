# 🧠 CONVERSIÓN DE INSTRUCCIONES EN LENGUAJE NATURAL A CONSULTAS SQL EN BASES DE DATOS TRANSACCIONALES PARA PERSONAL NO TÉCNICO

Este proyecto implementa un asistente conversacional inteligente que interpreta preguntas en lenguaje natural y las convierte en consultas SQL sobre una base de datos transaccional. Está diseñado especialmente para usuarios sin conocimientos técnicos en programación, como contadores, administradores o gerentes, facilitando el acceso rápido a información crítica para la toma de decisiones.

---

## 🚀 Tecnologías utilizadas

- [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/) – Para aprovisionamiento y procesamiento de lenguaje natural con modelos LLM.
- [Azure SQL Database](https://azure.microsoft.com/en-us/products/azure-sql/) – Motor de base de datos transaccional.
- [Flask](https://flask.palletsprojects.com/) – Framework web ligero en Python.
- [LangChain](https://www.langchain.com/) – Orquestación de agentes LLM y ejecución de herramientas como SQL.

---

## 📂 Estructura del proyecto

📁 Text-sql/
├── app.py # Servidor Flask y configuración del agente
├── sql_console.py # Script para pruebas por consola
├── templates/
│ └── index.html # Interfaz conversacional del chatbot
├── static/ # Recursos estáticos (CSS, imágenes, íconos)
├── .env # Variables de entorno
├── requirements.txt # Dependencias del proyecto

## ⚙️ Requisitos previos

- Python 3.10 o superior
- Acceso a un recurso de Azure OpenAI
- Azure SQL Database con tablas `clientes`, `cuentas`, y `ventas`
- Credenciales válidas de acceso

---

## 🔐 Configuración del archivo `.env`

Crea un archivo `.env` en la raíz del proyecto con la siguiente estructura:

- KEY=YOUR_KEY
- ENDPOINT=YOUR_ENDPOINT
- NAME_MODEL=YOUR_MODEL_NAME
- VERSION=YOUR_VERSION_MODEL

- AZURE_SQL_SERVER=YOUR_CONNECTION_SQL_DATABASE
- AZURE_SQL_DATABASE=YOUR_NAME_DB
- AZURE_SQL_USERNAME=ACCESS_YOUR_USSER
- AZURE_SQL_PASSWORD=ACCESS_YOUR_USSER_PASSWORD

---


## 🛠️ Instalación

1. Clona el repositorio: 
git clone https://github.com/CarlaMamaniChavez/Text-to-Sql.git
cd sql-chatbot-azure

2. Crea y activa un entorno virtual:

python -m venv env
source env/bin/activate      # En Linux/macOS
env\Scripts\activate         # En Windows

3. Instala las dependencias:
pip install -r requirements.txt

4. Inicia la aplicación Flask:
python app.py

---

## 💬 ¿Qué puedes preguntar?
El asistente puede responder preguntas como:

¿Cuántas cuentas están vencidas?

¿Cuántos clientes hay registrados?

¿Cuál es el total de ventas realizadas?

¿Qué cliente tiene más cuentas activas?

---
## 🧪 Casos de prueba
El agente analiza el esquema de las tablas y genera la consulta SQL correspondiente usando Azure OpenAI. Las respuestas se devuelven directamente al usuario en lenguaje natural.

## 📌 Créditos
Este proyecto fue desarrollado como parte de una investigación orientada a democratizar el acceso a bases de datos operativas usando IA y lenguaje natural.

## 🛡️ Licencia
Este proyecto está bajo licencia MIT. Puedes modificar y reutilizar libremente con fines académicos o comerciales con atribución.