import os
#from openai import AzureOpenAI
#from azure.ai.inference import ChatCompletionsClient
#from azure.ai.inference.models import SystemMessage, UserMessage
#from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_openai import AzureChatOpenAI
from langchain_community.agent_toolkits import create_sql_agent


load_dotenv()
endpoint  = os.environ["ENDPOINT"]
key = os.environ["KEY"]
name = os.environ["NAME_MODEL"]
api = os.environ["VERSION"]
# Azure OpenAI
llm = AzureChatOpenAI(
    azure_endpoint= endpoint,
    api_key= key,
    model= name,
    api_version= api, 
    temperature=0
)
'''
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)
'''

# Credenciales y datos
server = os.environ["AZURE_SQL_SERVER"]
database = os.environ["AZURE_SQL_DATABASE"]
username = os.environ["AZURE_SQL_USERNAME"]
password = os.environ["AZURE_SQL_PASSWORD"]

# Codificamos usuario y contraseña por seguridad (caracteres especiales como @, ^, etc.)
username_encoded = quote_plus(username)
password_encoded = quote_plus(password)

#Cadena de conexión corregida para SQLAlchemy + pyodbc + Driver 18
connection_string = (
    f"mssql+pyodbc://{username_encoded}:{password_encoded}@{server}:1433/{database}"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&encrypt=yes"
    "&trustservercertificate=no"
    "&Connection Timeout=30"
)

# Crear engine y base de datos
engine = create_engine(connection_string)
db = SQLDatabase(engine=engine)

# Crear agente LangChain
agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True
)

# Ejecutar consulta de prueba CON TEXTO QUEMADO
response = agent.invoke("¿Cuantas cuentas del estado vencido existen?")
print(response)


#¿Cuantas cuentas del estado vencido existen?

