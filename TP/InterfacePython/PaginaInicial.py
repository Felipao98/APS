import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.title("Página inicial")
janela.geometry("800x600")

def Pessoaclique():
    print("Informações na página principal")

def Gradeclique():
    print("Grade horária")
    
def Materiaclique():
    print("Matérias ofertadas")

def Historicoclique():
    print("Historico")
    
botaoPessoa = customtkinter.CTkButton(janela, text="Informações pessoais", command=Pessoaclique)
botaoPessoa.pack(padx=10, pady=10)

botaoMateria = customtkinter.CTkButton(janela, text="Matérias ofertadas", command=Materiaclique)
botaoMateria.pack(padx=10, pady=10)

botaoHistorico = customtkinter.CTkButton(janela, text="Histórico", command=Historicoclique)
botaoHistorico.pack(padx=10, pady=10)



janela.mainloop()