import mysql.connector


class Pessoa:
    def __init__(self, nome, matricula, tipo, senha):
        self.nome = nome
        self.matricula = matricula
        self.tipo = tipo
        self.senha = senha
# modelo.py


class modelo:
    def __init__(self, host, user, passwd, dbname):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=passwd,
            database=dbname
        )
        self.cursor = self.conn.cursor()

    def buscar_pessoa_por_matricula(self, matricula):
        query = f"SELECT Nome, Matricula, Tipo FROM PESSOA WHERE Matricula REGEXP '{matricula}'"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def buscar_pessoa_por_nome(self, nome):
        query = f"SELECT Nome, Matricula, Tipo FROM PESSOA WHERE Nome REGEXP '{nome}'"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def remover_pessoa(self, matricula):
        self.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        query = "DELETE FROM PESSOA WHERE Matricula = %s"
        self.cursor.execute(query, (matricula,))
        self.cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        self.conn.commit()

    # Adicione outras funções do modeloo aqui, como inserir_pessoa, buscar_historico, etc.

    def encerrar_conexao(self):
        self.cursor.close()
        self.conn.close()

class Materia:
    def __init__(self, nome, id_materia, pre_req):
        self.nome = nome
        self.id_materia = id_materia
        self.pre_req = pre_req

class Historico:
    def __init__(self, id_aluno, id_materia):
        self.id_aluno = id_aluno
        self.id_materia = id_materia
