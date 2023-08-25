import customtkinter as CTk
from tkinter import *

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("dark-blue")

janela = CTk.CTk()
janela.title("Página inicial")
janela.geometry("800x600")

class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue', font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

lst = [
    (1, 'ES', 'Obrigatório', 60),
    (2, 'Mineração de Dados', 'Optativa', 30),
    (3, 'Pesquisa Operacional', 'Obrigatória', 60),
    (4, 'Aprendizado de Máquina', 'Optativa', 30),
    (5, 'CLP', 'Obrigatória', 30)
]

total_rows = len(lst)
total_columns = len(lst[0])

def Pessoaclique():
    print("Informações na página principal")

def Gradeclique():
    print("Grade horária")
    Table(janela)

def Materiaclique():
    print("Matérias ofertadas")

def Historicoclique():
    print("Histórico")

botaoPessoa = CTk.CTkButton(janela, text="Informações pessoais", command=Pessoaclique)
botaoPessoa.grid(padx=10, pady=10, sticky=NSEW) #????, padx = distancia do canto da tela, pady = distancia entre os botões https://www.pythontutorial.net/tkinter/tkinter-grid/

botaoMateria = CTk.CTkButton(janela, text="Matérias ofertadas", command=Materiaclique)
botaoMateria.grid(padx=10, pady=10)

botaoHistorico = CTk.CTkButton(janela, text="Histórico", command=Historicoclique)
botaoHistorico.grid(padx=10, pady=10)

botaoGrHoraria = CTk.CTkButton(janela, text="Grade Horária", command=Gradeclique)
botaoGrHoraria.grid(padx=10, pady=10)

janela.mainloop()
