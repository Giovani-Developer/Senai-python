# import requests
# url = ("https://httpbin.org/post")

# dados = {"Usuario": "Giovani", "Curso": "Back-end Python."}

# resposta = requests.post(url, json=dados)

# print("Método: ", resposta.request.method)
# print("Código de status: ", resposta.status_code)
# print("Corpo: ", resposta.json())
############################################################################################

# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# # Dados que serão enviados na requisição
# novo_post = {
#     "title": "Meu primeiro post com py",
#     "body": "Estou aprendendo HTTP",
#     "userId": 11

# }

# resposta = requests.post(url,  json=novo_post)

# print("Status code:", resposta.status_code)
# print("Corpo da requisição:", resposta.json())

##################################################################################################
# import requests

# url = "https://httpbin.org/post"

# post = {
#     "Nome": "Giovani ",
#     "Cidade": "Mogi Guaçu",
#     "Curso": "Senai"

# }

# resposta = requests.post(url, json=post)

# print("Metodo: ", resposta.request.method)
# print("Status code:", resposta.status_code)
# print("Corpo", resposta.json())
# print("URL:" , resposta.url)


# response = requests.get("https://httpbin.org/post")
# dados_user = response.json()


# print(f"Dados do nome: {dados_user['Nome']}")

############################################################################################################

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# dados_atualizados = {
#     "id": 1,
#     "title": "Titulo atualizado",
#     "body": "COnteudo mudados",
#     "userId": 1
# }

# response = requests.put(url, json=dados_atualizados)

# print("Status code:", response.status_code, "Ok")
# print("Corpo:", response.json())

###########################################################################################################3333

# import requests

# url = "https://httpbin.org/put"

# dados = {
#     "id": 1,
#     "nome": "Giovani",
#     "curso": "Python"

# }
# response = requests.put(url, json=dados)

# print("Método: ", response.request.method)
# print("Status code:", response.status_code, "OK")
# print("Corpo", response.json())

####################################################################################################################

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.delete(url)

# print("Status code: ", response.status_code)
# print("Corpo:", response.text)

######################################################################################################################

# import requests

# url = "https://httpbin.org/delete"

# response = requests.delete(url)

# print("Método:", response.request.method)
# print("Status code:", response.status_code, "OK")
# print("Corpo", response.json())

#######################################################################################################################

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# dados_parciais = {
#     "title": "Titulo parcialmente atualizado"

# }

# response = requests.patch(url, json=dados_parciais)

# print("Status code:", response.status_code)
# print("Corpo", response.json())

#######################################################################################################################################

# import requests

# url = "https://httpbin.org/patch/1"

# dados = {
#     "curso": "backend avançado"

# }

# response = requests.patch(url, json=dados)



# if response.status_code >= 200 and response.status_code <= 300:
#     print(f"Status code: ", {response.status_code})
#     print(f"Conteudo da resposta: {response.json()} ")
# else:
#     print(f"A requisição falhou! Codigo: {response.status_code}")

##########################################################################################################################################

# import requests

# url = "https://httpbin.org/anything"
# response = requests.options(url)

# print("Status code:", response.status_code)
# print("Metodos permitidos:", response.headers.get("Allow"))
# print("Todos os headers:", response.headers)

######################################################################################################################################

import requests


def exibir_resposta(metodo, resposta):
    print(f"\n === {metodo}===")
    print(f"Status code: {resposta.status_code}")
    print(f"URL: {resposta.url}")
    print(f"Conteudo: {resposta.json()}")

def requisicao_get():
    params = {
        "Nome": "Giovani",
        "Cidade": "Mogi Guaçu",
        "Idade": 17
    }
    resposta = requests.get("https://httpbin.org/get", params=params)
    exibir_resposta("GET", resposta)




