import psycopg2
from psycopg2 import OperationalError

def conectar():
    try:
        conexao = psycopg2.connect(
            dbname="loja_virtual",
            user="postgres",
            password="senaisp",
            host="localhost",
            port="5432"
        )
        return conexao
    except OperationalError as e:
        print("Erro ao conectar ao banco:", e)
        return None


def obter_clientes():
    conexao = conectar()
    if conexao is None:
        return []

    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email, telefone, data_cadastro FROM loja_virtual")
    clientes = cursor.fetchall()

    cursor.close()
    conexao.close()
    return clientes
