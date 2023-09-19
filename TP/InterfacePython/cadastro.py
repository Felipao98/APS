import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela.customtkinter.CTk()
janela.title("Cadastro")
janela.geometry("800x500")

def clique():
    printf("Cadastro finalizado")

texto = customtkinter.CTkLabel(janela, text="Cadastro de aluno")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Entre com email")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Digite uma senha", show="*")
senha.pack(padx=10, pady=10)

confirma_senha = customtkinter.CTkEntry(janela, placeholder_text="Confirme sua senha", show="*")
confirma_senha.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Finalizar", command=clique)
botao.pack(padx=10, pady=10)



janela.mainloop()