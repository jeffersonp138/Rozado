import psycopg2


def get_postgre_connection():
    try:
        conn = psycopg2.connect(
            dbname="seu_banco",
            user="seu_usuario",
            password="sua_senha",
            host="localhost",  # ou o IP do servidor
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None