import requests
url = ("https://httpbin.org/post")

dados = {"usuario": "Giovani", "curso": "backend"}

resposta = requests.post(url, json=dados)

print("Método: ", resposta.request.method)
print("Código de status: ", resposta.status_code)
print("Corpo: ", resposta.json())