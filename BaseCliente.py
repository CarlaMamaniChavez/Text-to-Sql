import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

endpoint =  os.getenv("ENDPOINT")
model_name = "o4-mini"
deployment = "o4-mini"

subscription_key = os.getenv("KEY")
api_version = "2024-12-01-preview"

entrada_user = input("Ingrese su pregunta")

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "{Darle contexto de como debe comportarse el agente}",
        },
        {
            "role": "user",
            "content": entrada_user,
        }
    ],
    max_completion_tokens=100000,
    model=deployment
)

print(response.choices[0].message.content)