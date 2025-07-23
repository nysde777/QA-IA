import requests

# Obtener todos los posts
response = requests.get('https://jsonplaceholder.typicode.com/posts')
print('Status code:', response.status_code)
print('Primer post:', response.json()[0])

# Probar un endpoint inválido
response_invalid = requests.get('https://jsonplaceholder.typicode.com/invalid_endpoint')
print('Status code (inválido):', response_invalid.status_code)
print('Respuesta (inválido):', response_invalid.text)

