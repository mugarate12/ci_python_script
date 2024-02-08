import mysql.connector
from config.setup import NAME, DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT

if __name__ == '__main__':
    try:
        conn = mysql.connector.connect(
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            host=DATABASE_HOST,
            port=DATABASE_PORT
        )
    except mysql.connector.Error as err:
        print(err)
        exit(1)
    finally:
        cursor = conn.cursor()
        conn = conn
        print('conectei com o banco de dados!')

    print('Seu nome informado na .env é: ')
    print(NAME)
