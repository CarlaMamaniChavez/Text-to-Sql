import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

# Cargar variables del entorno
load_dotenv()

# Verifica si se leen correctamente
endpoint = os.environ.get("ENDPOINT")
key = os.environ.get("KEY")
name = os.environ.get("NAME_MODEL")
api = os.environ.get("VERSION")

print("🔍 ENDPOINT:", endpoint)
print("🔍 API KEY:", "OK" if key else "MISSING")
print("🔍 MODEL:", name)
print("🔍 VERSION:", api)

# Probar conexión solo si todo está presente
if not all([endpoint, key, name, api]):
    raise Exception("❌ Faltan variables de entorno.")

# Crear modelo
llm = AzureChatOpenAI(
    azure_endpoint=endpoint,
    api_key=key,
    model=name,
    api_version=api,
    temperature=0
)

# Mensaje de prueba
messages = [
    ("system", "Eres un asistente que traduce inglés a francés."),
    ("human", "Hello, how are you?")
]

# Invocar modelo
response = llm.invoke(messages)
print("✅ Respuesta:", response.content)
