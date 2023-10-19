import tkinter as tk
from tkinter import messagebox
#import mysql.connector
#from Controle import control


class SistemaAcademico:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Acadêmico")
        self.logged_in = False

        # Tela de Login
        self.login_frame = tk.Frame(root)
        self.login_frame.pack(padx=20, pady=20)
        self.username_label = tk.Label(self.login_frame, text="Nome de Usuário:")
        self.username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)
        self.password_label = tk.Label(self.login_frame, text="Senha:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2)

        # Tela de Cadastro
        self.register_frame = tk.Frame(root)
        self.username_label_reg = tk.Label(self.register_frame, text="Nome de Usuário:")
        self.username_label_reg.grid(row=0, column=0)
        self.username_entry_reg = tk.Entry(self.register_frame)
        self.username_entry_reg.grid(row=0, column=1)
        self.password_label_reg = tk.Label(self.register_frame, text="Senha:")
        self.password_label_reg.grid(row=1, column=0)
        self.password_entry_reg = tk.Entry(self.register_frame, show="*")
        self.password_entry_reg.grid(row=1, column=1)
        self.register_button = tk.Button(self.register_frame, text="Cadastrar", command=self.register)
        self.register_button.grid(row=2, columnspan=2)

        # Tela de Menu
        self.menu_frame = tk.Frame(root)
        self.generate_button = tk.Button(self.menu_frame, text="Gerar Grade Aleatória", command=self.generate_schedule)
        self.generate_button.grid(row=0, column=0)
        self.remove_button = tk.Button(self.menu_frame, text="Remover Matéria", command=self.remove_subject)
        self.remove_button.grid(row=1, column=0)
        self.history_button = tk.Button(self.menu_frame, text="Solicitar Histórico", command=self.request_history)
        self.history_button.grid(row=2, column=0)
        self.subject_button = tk.Button(self.menu_frame, text="Solicitar Matéria", command=self.request_subject)
        self.subject_button.grid(row=3, column=0)
        self.logout_button = tk.Button(self.menu_frame, text="Logout", command=self.logout)
        self.logout_button.grid(row=4, column=0)

        # Ocultar todas as telas no início
        self.login_frame.pack()
        self.register_frame.pack_forget()
        self.menu_frame.pack_forget()

    def login(self):
        # Lógica de autenticação
        # Se autenticado com sucesso:
        self.logged_in = True
        self.show_menu()

    def register(self):
        # Lógica de cadastro de usuário
        # Se cadastrado com sucesso:
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")

    def generate_schedule(self):
        # Lógica para gerar grade aleatória
        messagebox.showinfo("Grade Aleatória", "Grade aleatória gerada com sucesso!")

    def remove_subject(self):
        # Lógica para remover matéria
        messagebox.showinfo("Remover Matéria", "Matéria removida com sucesso!")

    def request_history(self):
        # Lógica para solicitar histórico
        messagebox.showinfo("Solicitar Histórico", "Histórico solicitado com sucesso!")

    def request_subject(self):
        # Lógica para solicitar matéria
        messagebox.showinfo("Solicitar Matéria", "Matéria solicitada com sucesso!")

    def logout(self):
        self.logged_in = False
        self.show_login()

    def show_login(self):
        self.register_frame.pack_forget()
        self.menu_frame.pack_forget()
        self.login_frame.pack()

    def show_menu(self):
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()
        self.menu_frame.pack()

root = tk.Tk()
sistema = SistemaAcademico(root)
root.mainloop()
