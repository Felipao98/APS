import customtkinter as ct
import mysql.connector
from Controle import control

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

###Cadastro
#Visão

global Nome, Matricula, Senha

def abrir_janela():

    janela2 = ct.CTkToplevel()
    janela2.title("Tela de cadastro")
    janela2.geometry("800x500")
    
    

    botao_voltar = ct.CTkButton(janela2, text="Retorna para tela de login", command=janela2.destroy)
    botao_voltar.pack(padx=10, pady=10)
    
    textoC = ct.CTkLabel(janela2, text="Cadastrar usuário")
    textoC.pack(padx=10, pady=10)

    nomeC = ct.CTkEntry(janela2, placeholder_text="Entre com nome:")
    nomeC.pack(padx=10, pady=10)

    matriculaC = ct.CTkEntry(janela2, placeholder_text="Entre com a matrícula:")
    matriculaC.pack(padx=10, pady=10)

    senhaCad = ct.CTkEntry(janela2, placeholder_text="Digite uma senha:", show="*")
    senhaCad.pack(padx=10, pady=10)

    confirma_senhaC = ct.CTkEntry(janela2, placeholder_text="Confirme sua senha:", show="*")
    confirma_senhaC.pack(padx=10, pady=10)

    def RegisterDataBase():
        
        Nome = nomeC.get()
        Matricula = matriculaC.get()
        Senha = senhaCad.get()
        
        
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Silvafodao98!",
            database = "Software_APS"
        )

        cursor = conn.cursor()
        
        control.inserir_pessoa(cursor, (Nome, Matricula, Senha))

        cursor.execute("SELECT * FROM MATERIAS")
        dados = cursor.fetchall()

        cursor.execute("SELECT * FROM HISTORICO")
        dados_historico = cursor.fetchall()


        conn.commit()
        conn.close()

        return dados
        return dados_historico

        janela2.destroy()
    botao = ct.CTkButton(janela2, text="Finalizar", command=RegisterDataBase)
    botao.pack(padx=10, pady=10)

def concluir_materia():
    # Lógica para concluir uma matéria
    janela_tabela = ct.CTkToplevel()
    janela_tabela.title("Tabela de matérias")
    janela_tabela.geometry("800x500")

    tabela = ct.CTkTabview(janela_tabela, data=dados, headers=["Nome_materia", "ID", "Pre"])
    tabela.pack(padx=10, pady=10)

    print("Matéria concluída!")

    janela_tabela.mainloop()


def ver_historico():
    # Lógica para ver o histórico do aluno
    janela_historico = ct.CTkToplevel()
    janela_historico.title("Historico do aluno")
    janela_historico.geometry("800x500")

    histórico = ct.CTkTabview(janela_historico, dataH=dados_historico, headers=["ID_aluno", "ID_materia"])
    histórico.pack(padx=10, pady=10)

    print("Historico do aluno!")

    janela_historico.mainloop()


def gerar_grade():
    # Lógica para gerar a grade de disciplinas
    janela_grade = ct.CTkToplevel()
    janela_grade.title("Grade horaria")
    janela_grade.geometry("800x500")

    grade = ct.CTkTabview(janela_grade, data=dados, headers=["Nome_materia", "ID", "Pre"])
    tabela.pack(padx=10, pady=10)

    print("Grade gerada!")

    janela_grade.mainloop()

def remover_cadastro():
    # Lógica para remover o cadastro do aluno
    print("Cadastro removido!")


def cliqueL():
    print("Login com sucesso!")
    janela3 = ct.CTkToplevel()
    janela3.title("Menu principal")
    janela3.geometry("800x500")

    botaoConcluir = ct.CTkButton(janela3, text="Concluir materia", command=concluir_materia)
    botaoConcluir.pack(padx=10, pady=10)

    botaoHistorico = ct.CTkButton(janela3, text="Ver histórico")
    botaoHistorico.pack(padx=10, pady=10)

    botaoGrade = ct.CTkButton(janela3, text="Gerar grade")
    botaoGrade.pack(padx=10, pady=10)

    botaoRemover = ct.CTkButton(janela3, text="Remover cadastro")
    botaoRemover.pack(padx=10, pady=10)

    botaoLogout = ct.CTkButton(janela3, text="Logout")
    botaoLogout.pack(padx=10, pady=10)



    janela3.mainloop()


janela = ct.CTk()
janela.title("Tela de login")
janela.geometry("800x500")

###Login

texto = ct.CTkLabel(janela, text="Fazer login")
texto.pack(padx=10, pady=10)

matricula = ct.CTkEntry(janela, placeholder_text="Matrícula:")
matricula.pack(padx=10, pady=10)

senha = ct.CTkEntry(janela, placeholder_text="Sua senha:", show="*")
senha.pack(padx=10, pady=10)

checkbox = ct.CTkCheckBox(janela, text="Lembrar login")
checkbox.pack(padx=10, pady=10)

botao = ct.CTkButton(janela, text="Login", command=cliqueL)
botao.pack(padx=10, pady=10)

botaoC = ct.CTkButton(janela, text="Cadastrar aluno", command=abrir_janela)
botaoC.pack(padx=10, pady=10)


janela.mainloop()

