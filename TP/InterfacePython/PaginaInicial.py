import customtkinter as CTk
from tkinter import *

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("dark-blue")

janela = CTk.CTk()
janela.title("Página inicial")
#janela.geometry("800x600")
#Configurar novas janelas em "testeNewWindow"


class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue', font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

lst = [#Aqui que vai puxar dados do banco
    (1, 'ES', 'Obrigatório', 60),
    (2, 'Mineração de Dados', 'Optativa', 30),
    (3, 'Pesquisa Operacional', 'Obrigatória', 60),
    (4, 'Aprendizado de Máquina', 'Optativa', 30),
    (5, 'CLP', 'Obrigatória', 30)
]

total_rows = len(lst)
total_columns = len(lst[0])

def Pessoaclique():
    global novaJanela  # Declare a variável como global
    print("Informações na página principal")
    print("Informações em outra página")
    janela.withdraw()
    novaJanela = CTk.CTkToplevel()
    novaJanela.title("Informações pessoais")
    novaJanela.geometry("800x600")
    CTk.CTkLabel(novaJanela, text="Informações").pack()
    retorna = CTk.CTkButton(novaJanela, text="Voltando para o  Inicio", command=retornar)
    retorna.pack()

def retornar():
    print("Retorna ao menu")
    global novaJanela  # Declare a variável como global
    print("Retornou a página inicial")
    janela.update()
    janela.deiconify()
    novaJanela.destroy()

def Gradeclique():
    global novaJanela
    print("Grade horária")
    Table(janela)
    retorna = CTk.CTkButton(novaJanela, text="Voltando para o  Inicio", command=retornar)
    retorna.pack()


def Materiaclique():
    print("Matérias ofertadas")

def Historicoclique():
    print("Histórico")

def retornaPaginaInicial():
    print("Retornou a página inicial")

botaoPessoa = CTk.CTkButton(janela, text="Informações pessoais", command=Pessoaclique)
botaoPessoa.grid(padx=10, pady=10, column=0, row=0) #????, padx = distancia do canto da tela, pady = distancia entre os botões https://www.pythontutorial.net/tkinter/tkinter-grid/

botaoMateria = CTk.CTkButton(janela, text="Matérias ofertadas", command=Materiaclique)
botaoMateria.grid(padx=10, pady=10, column=0, row=1)

botaoHistorico = CTk.CTkButton(janela, text="Histórico", command=Historicoclique)
botaoHistorico.grid(padx=10, pady=10, column=0, row=2)

botaoGrHoraria = CTk.CTkButton(janela, text="Grade Horária", command=Gradeclique)
botaoGrHoraria.grid(padx=10, pady=10, column=0, row=3)

janela.mainloop()
