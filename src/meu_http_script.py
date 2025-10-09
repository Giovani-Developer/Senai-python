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

# import requests


# def exibir_resposta(metodo, resposta): # parametros passados a funcao para exbir cada metodo.
#     print(f"\n === {metodo}===")
#     print(f"Status code: {resposta.status_code}")
#     print(f"URL: {resposta.url}")
#     print(f"Conteudo: {resposta.json()}")

# def requisicao_get():# passei os paramns e dou um get neles.
#     params = {
#         "Nome": "Giovani",
#         "Cidade": "Mogi Guaçu",
#         "Idade": 17
#     }
#     resposta = requests.get("https://httpbin.org/get", params=params)
#     exibir_resposta("GET", resposta)

# def requisicao_post(): # chamo o metodo POST e mudo todos os parametros.
#     dados = {"nome": "Giovani", "cidade": "Campinas", "idade": 17}
#     resposta = requests.post("https://httpbin.org/post", json=dados)
#     exibir_resposta("POST", resposta)

# def requisicao_put():# metodo PUT altero todos dados.
#     dados = {"nome": "Giovani", "cidade": "Mogi Mirim", "idade": 18}
#     resposta = requests.put("https://httpbin.org/put", json=dados)
#     exibir_resposta("PUT", resposta)

# def requisicao_delete():# metodo DELETE deleto todos os dados.
#     dados = {"user_id": 123}
#     resposta = requests.delete("https://httpbin.org/delete", json=dados)
#     exibir_resposta("DELETE", resposta)

# if __name__ == "__main__":
#     requisicao_get()
#     requisicao_post()
#     requisicao_put()
#     requisicao_delete()

################################################################################################

# import requests

# resposta = requests.get("https://swapi.dev/api/people/1/")

# if resposta.status_code == 200:
#     try:
#         dados = resposta.json()
#         print("===GET===")
#         print("Nome:", dados["name"])
#         print("Cor do cabelo: ", dados["hair_color"])
#         print("Cor dos olhos: ", dados["eye_color"])
#     except ValueError:
#         print("Erro: A resposta não é JSON.")
#         print("Conteúdo da resposta:", resposta.text)
# else:
#     print(" Erro HTTP:", resposta.status_code)

# url = "https://pokeapi.co/api/v2/pokemon/pikachu"

# response = requests.get(url)

# if response.status_code == 200:
#     try:
#         dados1 = response.json()
#         print("=== GET ===")
#         print("Nome", dados1["name"])
#         print("URL:", dados1["url"])
#     except ValueError:
#         print("Erro: a resposta não é JSON")
#         print("Conteúdo da resposta: ", response.text)
# else:
#     print("Erro HTTP: ", response.status_code)

import requests

url = "https://httpbin.org/headers"

headers = {
    "User-Agent": "CursoBackEndPython/1.0 (Aluno: Giovani; +https://capitalapex.com.br)"

}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)
print("\nCabeçalhos recebidos pelo servidor: ")
print(response.json()["headers"])