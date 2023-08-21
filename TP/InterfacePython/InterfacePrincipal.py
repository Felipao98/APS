import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.title("Login")
janela.geometry("500x300")

def clique():
    print("Fazer login")

texto = customtkinter.CTkLabel(janela, text="Fazer login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar login")
checkbox.pack(padx=10, pady=10)


botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()