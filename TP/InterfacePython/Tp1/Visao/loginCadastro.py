import customtkinter as ct
import mysql.connector
from Controle import control

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

###Cadastro
#Visão

global Nome, Matricula, Senha
global Nome_materia, Id, Pre


def abrir_janela():

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

        conn.commit()
        conn.close()

        janela2.destroy()

    
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

    botao = ct.CTkButton(janela2, text="Finalizar", command=RegisterDataBase)
    botao.pack(padx=10, pady=10)

def chamar_dados(treeview):
        
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Silvafodao98!",
        database = "Software_APS"
    )

    cursor = conn.cursor()
        
    cursor.execute("SELECT * FROM MATERIAS")
    dados = cursor.fetchall()

    for record in treeview.get_children():
        treeview.delete(record)
        
    for dado in dados:
        treeview.insert("", "end", values=dado)

    conn.commit()
    conn.close()

def criar_tabela():    

    janela_tabela = ct.CTkToplevel()
    janela_tabela.title("Tabela de matérias")
    janela_tabela.geometry("800x500")

    treeview = ct.CTkTreeview(janela_tabela, columns=("Nome_materia", "Id", "Pre"))
    treeview.heading('#1', text="Nome da materia")
    treeview.heading('#2', text="Id")
    treeview.heading('#3', text="Pre")   
    treeview.pack(padx=10, pady=10)

    chamar_dados(treeview)

    print("Matéria concluída!")

    janela_tabela.destroy()
    janela_tabela.mainloop()

def remover_cadastro():
    janela_remove = ct.CTkToplevel()
    janela_remove.title("Remover cadastro")
    janela_remove.geometry("800x500")

    tree = ct.CTkTabview(janela_remove, selectmode="browse", column=("column1", "column2", "column3"), show='headings')

    tree.column("column1", width=200, minwidth=50)
    tree.heading('#1', text="Materia")

    tree.column("column2", width=100, minwidth=50)
    tree.heading('#2', text="Pre-requisito")

    tree.column("column3", width=300, minwidth=50)
    tree.heading('#3', text="ID_materia")

    tree.pack(row=0, column=0)

    janela_remove.mainloop()

def cliqueL():
    print("Login com sucesso!")
    janela3 = ct.CTkToplevel()
    janela3.title("Menu principal")
    janela3.geometry("800x500")

    botaoConcluir = ct.CTkButton(janela3, text="Solicitar a disciplina", command=criar_tabela)
    botaoConcluir.pack(padx=10, pady=10)

    botaoHistorico = ct.CTkButton(janela3, text="Ver histórico")
    botaoHistorico.pack(padx=10, pady=10)

    botaoGrade = ct.CTkButton(janela3, text="Gerar grade")
    botaoGrade.pack(padx=10, pady=10)

    botaoRemover = ct.CTkButton(janela3, text="Remover cadastro", command=remover_cadastro)
    botaoRemover.pack(padx=10, pady=10)

    botaoLogout = ct.CTkButton(janela3, text="Logout", command=janela)
    botaoLogout.pack(padx=10, pady=10)

    janela3.destroy()
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
