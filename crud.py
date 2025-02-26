import mysql.connector
from config import MYSQL_HOST,MYSQL_USER,MTSQL_PASSWORD,MYSQL_DATABASE

def get_connection():
    return mysql.connector.connect(
        host = MYSQL_HOST,
        user = MYSQL_USER,
        password = MTSQL_PASSWORD,
        database = MYSQL_DATABASE
    )

def create_user(nome,telefone,email,usuario,senha):
    conn = get_connection()
    cursor = conn.cursor()
    query = "insert usuario(nome,telefone,email,senha)VALUES(%s,%s,%s,%s,%s))"
    cursor.execute(query,(nome,telefone,email,usuario,senha))
    conn.commit()
    cursor.close()
    conn.close()

def read_users():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM usuario"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return result

def update_user(user_id,nome,telefone,email,usuario,senha):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE usuario SET nome=%s,telefone=%s,email=%s,senha=%s WHERE idusuario = %s)"
    cursor.execute(query,(nome,telefone,email,usuario,senha,user_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELE FROM usuario WHERE idusuario = %s)"
    cursor.execute(query,(user_id))
    conn.commit()
    cursor.close()
    conn.close()