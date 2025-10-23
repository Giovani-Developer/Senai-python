import psycopg2

def conectar_db ():
    conexao = psycopg2.connect(
    database = 'loja_virtual',
    user = 'postgres',
    password = 'senaisp',
    host = 'localhost',
    port = '5432'
    )
    return conexao