import mysql.connector

#PERSISTENCIA CONTROLE SOBRE O BANCO
host = "localhost"
user = "root"
passwd = "Silvafodao98!"
dbname = "Software_APS"

def conectar_banco():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Silvafoda98!",
        database="Solftware_APS"
    )
    return conn

def consultar_banco(query, params=None):
    conn = conectar_banco()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def executar_query(query, params=None):
    conn = conectar_banco()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
