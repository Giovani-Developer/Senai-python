# import psycopg2
# from psycopg2 import OperationalError

# def conectar():
#     try:
#         conexao = psycopg2.connect(
#             dbname="postgres",
#             user="postgres",
#             password="senaisp",
#             host="localhost",
#             port="5432"
#         )
        
#         print("Conexão bem-sucedida!")
#         conexao.close()

#     except OperationalError as e:
#         print("Erro ao conectar ao banco de dados:")
#         print(e)


# conectar()

####################################################################################
# import psycopg2

# conexao = psycopg2.connect(
#      dbname="postgres",
#      user="postgres",
#      password="senaisp",
#      host="localhost",
#      port="5432"
    
# )
# cursor = conexao.cursor()
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS clientes (
#         id SERIAL PRIMARY KEY,
#         nome  VARCHAR(80) NOT NULL,
#         email VARCHAR(120) UNIQUE,
#         telefone VARCHAR(20),
#         data_cadastro  DATE DEFAULT CURRENT_DATE       
#         )     
                              
#  ''')

# conexao.commit()
# cursor.close()
# conexao.close()
# print("Tabela 'clientes' criada com sucesso")


###############################################################################
import psycopg2
from psycopg2 import OperationalError


def criar_banco():
    try:
        # 1️⃣ Conecta ao banco padrão (postgres)
        conexao = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="senaisp",
            host="localhost",
            port="5432"
        )
        conexao.autocommit = True
        cursor = conexao.cursor()

        # Cria o banco 'loja_virtual' se ainda não existir
        cursor.execute("SELECT 1 FROM pg_database WHERE datname='loja_virtual'")
        existe = cursor.fetchone()

        if not existe:
            cursor.execute("CREATE DATABASE loja_virtual")
            print("Banco 'loja_virtual' criado com sucesso!")
        else:
            print("Banco 'loja_virtual' já existe.")

        cursor.close()
        conexao.close()

    except OperationalError as e:
        print("Erro ao criar o banco:")
        print(e)


def criar_tabela():
    try:
        # Conecta ao banco 'loja_virtual'
        conexao = psycopg2.connect(
            dbname="loja_virtual",
            user="postgres",
            password="senaisp",
            host="localhost",
            port="5432"
        )
        cursor = conexao.cursor()

        # Cria a tabela se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS loja_virtual (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(80) NOT NULL,
                email VARCHAR(120) UNIQUE,
                telefone VARCHAR(20),
                data_cadastro DATE DEFAULT CURRENT_DATE
            );
        ''')

        cursor.execute('''
            INSERT INTO loja_virtual (nome, email, telefone) VALUES 
            ('Giovani', 'giovani@gmail.com', '(19) 999295742'),
            ('Gabriel', 'gabriel@email.com', '(19)999299999');                 
''')
        cursor.execute('''
        # alterar um valor específico da tabela    
                    
''')





        conexao.commit()
        print("Tabela 'loja_virtual' criada com sucesso!")

        cursor.close()
        conexao.close()

    except OperationalError as e:
        print("Erro ao criar a tabela:")
        print(e)


def conectar():
    try:
        # Testa a conexão
        conexao = psycopg2.connect(
            dbname="loja_virtual",
            user="postgres",
            password="senaisp",
            host="localhost",
            port="5432"
        )
        print("Conexão sucedida!")
        conexao.close()
    except OperationalError as e:
        print("Conexão mal sucedida")
        print(e)



criar_banco()
criar_tabela()
conectar()


########################################################################3
# import psycopg2

# conexao = psycopg2.connect(
#     dbname="postgres",
#     user="postgres",
#     password="senaisp",
#     host="localhost",
#     port="5432"
# )
# conexao.autocommit = True
# cursor = conexao.cursor()

# cursor.execute("CREATE DATABASE loja_virtual")

# cursor.close()
# conexao.close()
# print("Banco criado com sucesso!")

#################################################################
# import psycopg2

# try:
#     conexao = psycopg2.connect(
#         dbname="loja_virtual",
#         user="postgres",
#         password="senaisp",
#         host="localhost",
#         port="5432"
#     )
#     cursor = conexao.cursor()

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS loja_virtual (
#             id SERIAL PRIMARY KEY,
#             nome VARCHAR(80) NOT NULL,
#             email VARCHAR(120) UNIQUE,
#             telefone VARCHAR(20),
#             data_cadastro DATE DEFAULT CURRENT_DATE
#         );
#     ''')

#     conexao.commit()
#     cursor.close()
#     conexao.close()

#     print("✅ Tabela 'loja_virtual' criada (ou já existente).")

# except Exception as e:
#     print("Erro ao criar tabela:", e)
