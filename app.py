from flask import Flask, render_template, request, jsonify
import os
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
# Credenciales y datos
server = os.environ["AZURE_SQL_SERVER"]
database = os.environ["AZURE_SQL_DATABASE"]
username = os.environ["AZURE_SQL_USERNAME"]
password = os.environ["AZURE_SQL_PASSWORD"]

# ⚠️ Codificamos usuario y contraseña por seguridad (caracteres especiales como @, ^, etc.)
username_encoded = quote_plus(username)
password_encoded = quote_plus(password)

# ✅ Cadena de conexión corregida para SQLAlchemy + pyodbc + Driver 18
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

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    try:
        response = agent.invoke(user_input)
        final_response_content = response.get("output", str(response))
        return jsonify({"answer": final_response_content})
    except Exception as e:
        return jsonify({"answer": f"Ocurrió un error: {str(e)}"}), 500

@app.route("/suggest", methods=["POST"])
def suggest():
    return jsonify({"suggestion": "Esta función aún no está implementada."})

    
if __name__ == "__main__":
    app.run(debug=True)
