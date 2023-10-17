# controller.py
import os
import sys
import getpass
import time
import mysql.connector
from Modelo import model
from Visao import loginCadastro

class Controller:
    def __init__(self, host, user, password, database):
        self.model = model(host, user, password, database)
        self.visao = loginCadastro()

def pesquisa():
    os.system("cls")  # Use "cls" no Windows

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Silvafodao98!",
        database="Software_APS"
    )

    cursor = conn.cursor()
    
    busca = input("\nInforme o nome ou matricula que quer procurar: ")
    
    if busca.isdigit():
        query = f"SELECT Nome, Matricula, Tipo FROM PESSOA WHERE Matricula REGEXP '{busca}'"
        cursor.execute(query)
        result = cursor.fetchall()
        print("\n\n")

        for row in result:
            print(row[0], row[1], row[2])

        time.sleep(5)

    else:
        query = f"SELECT Nome, Matricula, Tipo FROM PESSOA WHERE Nome REGEXP '{busca}'"
        cursor.execute(query)
        result = cursor.fetchall()
        print("\n\n")

        for row in result:
            print(row[0], row[1], row[2])

        time.sleep(5)

def remover_root():
    os.system("cls")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Silvafodao98!",
        database="Software_APS"
    )

    cursor = conn.cursor()

    matricula = input("\nQual Matricula deseja excluir?: ")

    remover = input("\nDeseja realmente excluir o usuário? [Sim/Não]: ")
    if remover.lower() == "sim":
        password = getpass.getpass("Digite sua senha: ")

        query = "SELECT 1 FROM PESSOA WHERE (Matricula = 'admin') AND (Senha = %s)"
        cursor.execute(query, (password,))
        row = cursor.fetchone()

        if row is None:
            print("Senha errada")
        else:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0")
            query = "DELETE FROM PESSOA WHERE Matricula = %s"
            cursor.execute(query, (matricula,))
            cursor.execute("SET FOREIGN_KEY_CHECKS=1")
            conn.commit()

            print("\nUsuario removido!\n")
            time.sleep(5)

    cursor.close()
    conn.close()

def remover_materias():
    os.system("cls")  # Use "cls" no Windows

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Silvafodao98!",
        database="Software_APS"
    )

    cursor = conn.cursor()
    nome = input("\nNome Materia: ")
    matricula = input("\nInforme o ID: ")
    
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    query = "DELETE FROM MATERIAS WHERE (Nome_materia = %s) AND (Id = %s)" 
    values = (nome, matricula)
    cursor.execute(query, values)
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    conn.commit()

    print("\n\Materia Removida!\n")
    time.sleep(2)

    cursor.close()
    conn.close()

def inserir_materias():
    os.system("cls")  # Use "cls" no Windows

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Silvafodao98!",
        database="Software_APS"
    )

    cursor = conn.cursor()
    nome = input("\nNome da Materia: ")
    id_materia = input("\nInforme o Id da materia: ")
    pre_req = input("\nInforme o pré-requisito: ")

    query = "INSERT INTO MATERIAS (Nome_materia, Id, Pre) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome, id_materia, pre_req))
    conn.commit()

    print("\n\tDados Inseridos!\n")
    time.sleep(2)

    cursor.close()
    conn.close()

def inserir_adms():
    os.system("cls")  # Use "cls" no Windows

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Silvafodao98!",
        database="Software_APS"
    )

    cursor = conn.cursor()
    nome = input("\nNome Completo: ")
    matricula = input("\nInforme a Matricula: ")
    senha = getpass.getpass("\nDigite sua senha: ")
    senha_conf = getpass.getpass("\nConfirme sua senha: ")

    if senha != senha_conf:
        return
    
    query = "INSERT INTO PESSOA (Nome, Matricula, Tipo, Senha) VALUES (%s, %s, 'admin', %s)"
    cursor.execute(query, (nome, matricula, senha))
    conn.commit()

    print("\n\tDados Inseridos!\n")
    time.sleep(2)

    cursor.close()
    conn.close()

def remover_cadastro(login):
    os.system("cls")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Silvafodao98!",
        database="Software_APS"
    )

    cursor = conn.cursor()

    remover = input("\nDeseja excluir seu usuário? [Sim/Não]: ")
    if remover.lower() == "sim":
        password = getpass.getpass("Digite sua senha: ")

        query = "SELECT 1 FROM PESSOA WHERE (Matricula = %s) AND (Senha = %s)"
        cursor.execute(query, (login, password))
        row = cursor.fetchone()

        if row is None:
            print("Senha errada")
        else:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0")
            query = "DELETE FROM PESSOA WHERE Matricula = %s" 
            cursor.execute(query, (login,))
            cursor.execute("SET FOREIGN_KEY_CHECKS=1")
            conn.commit()

            print("\nUsuario removido!\n")
            time.sleep(5)
            sys.exit(1)

    cursor.close()
    conn.close()

def gerar_grade(login):
    os.system("cls")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Silvafodao98!",
        database="Software_APS"
    )

    cursor = conn.cursor()

    query = f"SELECT Nome_materia, Id FROM MATERIAS WHERE Id NOT IN(SELECT Id_materia FROM HISTORICO WHERE Id_aluno = {login}) LIMIT 5"
    cursor.execute(query)
    result = cursor.fetchall()
    print("\n\n")

    for row in result:
        print(row[0], row[1])
    
    time.sleep(7)

    cursor.close()
    conn.close()

def ver_historico(login):
    os.system("cls")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Silvafodao98!",
        database="Software_APS"
    )

    cursor = conn.cursor()

    query = f"SELECT * FROM HISTORICO WHERE Id_aluno = {login}"
    cursor.execute(query)
    result = cursor.fetchall()
    print("\n\n")

    for row in result:
        print(row[0], row[1])
    
    time.sleep(7)

    cursor.close()
    conn.close()

def inserir_historico(login):
    os.system("cls")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Silvafodao98!",
        database="Software_APS"
    )

    cursor = conn.cursor()

    opcao = input("\nDigite o id da materias que concluiu: ")
    query = "INSERT INTO HISTORICO (Id_aluno, Id_materia) VALUES (%s, %s)"
    cursor.execute(query, (login, opcao))
    conn.commit()

    print("\n\tInserido!\n")
    time.sleep(2)

    cursor.close()
    conn.close()

def menu_principal(login):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Silvafodao98!",
        database="Software_APS"
    )

    cursor = conn.cursor()

    query = "SELECT Nome FROM PESSOA WHERE Matricula = %s"
    cursor.execute(query, (login,))
    result = cursor.fetchall()

    for row in result:
        id = str(row[0])

    cursor.close()
    conn.close()

    stop = 0

    while stop == 0:
        os.system("cls")
        print(f"\tBem Vindo(a) Aluno {id}!\n")
        print("1-Concluir Materias\n2-Ver Historico\n3-Gerar Grade\n4-Remover Cadastro\n99-LOGOUT\n")
        op = int(input("Sua escolha: "))

        if op == 1:
            inserir_historico(login)
        elif op == 2:
            ver_historico(login)
        elif op == 3:
            gerar_grade(login)
        elif op == 4:
            remover_cadastro(login)
        elif op == 99:
            stop = 1

    return op

def menu_administrador():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Silvafodao98!",
        database="Software_APS"
    )

    stop = 0

    while stop == 0:
        os.system("cls")
        print(f"\tBem Vindo(a) Admin!\n")
        print("1-Inserir Administradores\n2-Inserir Materias\n3-Remover Materias\n4-Remover Usuarios\n5-Pesquisa\n99-LOGOUT\n")
        op = int(input("Sua escolha: "))

        if op == 1:
            inserir_adms()
        elif op == 2:
            inserir_materias()
        elif op == 3:
            remover_materias()
        elif op == 4:
            remover_root()
        elif op == 5:
            pesquisa()
        elif op == 99:
            stop = 1

    return op

def inserir_pessoa(cursor, dados_pessoais):
    os.system("cls")  # Use "cls" no Windows

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Silvafodao98!",
        database="Software_APS"
    )
    try:
        nome, matricula, senha = dados_pessoais
        query = "INSERT INTO PESSOA (Nome, Matricula, Senha)   VALUES (%s, %s, %s)"
        cursor.execute(query, (nome, matricula, senha))
        conn.commit()
        print("Dados inseridos.\n")
    except mysql.connector.Error as e:
        print("Erro.\n")
        
    cursor = conn.cursor()
    

    print("\n\tDados Inseridos!\n")
    time.sleep(2)

    cursor.close()
    conn.close()


def login():
    os.system("cls")  # Use "cls" no Windows

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Silvafodao98!",
        database="Software_APS"
    )

    cursor = conn.cursor()

    login = input("Matricula: ")
    password = getpass.getpass("\nSENHA: ")

    query = "SELECT Matricula FROM PESSOA WHERE Matricula = %s"
    cursor.execute(query, (login,))
    row = cursor.fetchone()

    if row is None:
        print("Login errado")
        cursor.close()
        conn.close()
        return 0

    query = "SELECT 1 FROM PESSOA WHERE (Matricula = %s) AND (Senha = %s)"
    cursor.execute(query, (login, password))
    row = cursor.fetchone()

    if row is None:
        print("Senha errada")
        cursor.close()
        conn.close()
        return 0

    query = "SELECT Tipo FROM PESSOA WHERE Matricula = %s"
    cursor.execute(query, (login,))
    row = cursor.fetchone()

    if row is not None:
        if row[0] in ["estudante"]:
            menu_principal(login)
        elif row[0] == "admin":
            print("Menu Adm")
            menu_administrador()

    print("\n\n")

    cursor.close()
    conn.close()
    return 1

def menu_inicial():
    stop = False

    while not stop:
        os.system("cls") # Use "cls" no Windows
        print("\tBem Vindo(a)!")
        print("1-Fazer Login\n2-Fazer Cadastro\n99-Sair\n")
        op = int(input("Sua escolha: "))

        if op == 1:
            login()
        elif op == 2:
            inserir_pessoa()
        elif op == 99:
            stop = True
        else:
            print("Escolha inválida")

    return op

def main():
    stop = False

    while not stop:
        os.system("cls")
        op = menu_inicial()

        if op == 99:
            stop = True

if __name__ == "__main__":
    main()

