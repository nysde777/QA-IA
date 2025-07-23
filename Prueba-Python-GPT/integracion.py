import os
from openai import OpenAI

# Leer la API key desde 'apikey.txt' en la misma carpeta
with open("apikey.txt", "r") as f:
    api_key = f.read().strip()

client = OpenAI(
    api_key=api_key,
)

response = client.responses.create(
    model="gpt-4o-mini-2024-07-18",
    instructions="Eres un experto en QA manual y automation.",
    input="¿Como puedo hacer la integracion con la API de GPT?",
)

print(response.output_text)


