import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
#from Controle import control


class SistemaAcademico:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Acadêmico")
        self.logged_in = False

        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Silvafodao98!",
                database="Software_APS"
            )
            print("Conectado no banco!\n")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar {err}\n")
            
        # Tela de Cadastro
        self.register_frame = tk.Frame(root)
        self.username_label_reg = tk.Label(self.register_frame, text="Nome:")
        self.username_label_reg.grid(row=0, column=0)
        self.Nome_entry = tk.Entry(self.register_frame)  # Entrada para Nome
        self.Nome_entry.grid(row=0, column=1)
        self.password_label_reg = tk.Label(self.register_frame, text="Matrícula:")
        self.password_label_reg.grid(row=1, column=0)
        self.Matricula_entry = tk.Entry(self.register_frame)  # Entrada para Matrícula
        self.Matricula_entry.grid(row=1, column=1)
        self.password_label_reg = tk.Label(self.register_frame, text="Senha:")
        self.password_label_reg.grid(row=2, column=0)
        self.Senha_entry = tk.Entry(self.register_frame, show="*")  # Entrada para Senha
        self.Senha_entry.grid(row=2, column=1)
        self.register_button = tk.Button(self.register_frame, text="Cadastrar", command=self.register)
        self.register_button.grid(row=3, columnspan=2)

        # Tela de Login
        self.login_frame = tk.Frame(root)
        self.username_label = tk.Label(self.login_frame, text="Matricula:")
        self.username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)
        self.password_label = tk.Label(self.login_frame, text="Senha:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2)
        self.register_button = tk.Button(self.login_frame, text="Cadastrar", command=self.show_registration_frame)
        self.register_button.grid(row=3, columnspan=2)

        # Tela de Menu
        self.menu_frame = tk.Frame(root)
        self.generate_button = tk.Button(self.menu_frame, text="Listar matérias", command=self.gerar_grade)
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
        self.login_frame.grid()
        self.register_frame.grid_forget()
        self.menu_frame.grid_forget()

        self.subject_ids = []
        self.grade_data = []
        self.historico = []


    def destroy_current_frame(self):
        for widget in self.root.winfo_children():
            widget.grid_forget()

    def show_registration_frame(self):
        self.destroy_current_frame()
        self.register_frame.grid()

    def register(self):
        # Lógica de cadastro de usuário
        Nome = self.Nome_entry.get()
        Matricula = self.Matricula_entry.get()
        Senha = self.Senha_entry.get()
        

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM pessoa WHERE matricula = %s", (Matricula,))
            existing_user = cursor.fetchone()
            if existing_user:
                messagebox.showerror("Erro", "Matricula ja em uso. Insira outra.")
            else:
                query = "INSERT INTO pessoa (nome, matricula, senha) VALUES (%s, %s, %s)"
                cursor.execute(query, (Nome, Matricula, Senha))
                self.connection.commit()
                messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
                self.show_login()
                self.register_frame.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {err}")

    def login(self):
        # Lógica de autenticação
        # Se autenticado com sucesso:
        self.logged_in = True
        self.show_menu()
        self.login_frame.destroy()

    def gerar_grade(self): #PRONTO, espaço para deixar bonito
        # Lógica para gerar grade aleatória
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM materias")
            resultados = cursor.fetchall()

            self.grade_data.clear()

            for resultado in resultados:
                self.grade_data.append((resultado[0], resultado[1], resultado[2]))
            if self.grade_data:
                self.maximiza_grade()  # Mostra a grade tabulada
            else:
                messagebox.showinfo("Grade Vazia", "Não há dados na grade.")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao buscar a tabela: {err}\n")

    def maximiza_grade(self): #PRONTO, espaço para deixar bonito
        grade_window = tk.Toplevel(self.root)
        grade_window.title("Grade Expandida")

        grade_tree = ttk.Treeview(grade_window, columns=("Nome", "ID", "Pré-requisito"), show="headings")
        grade_tree.heading("Nome", text="Nome")
        grade_tree.heading("ID", text="ID")
        grade_tree.heading("Pré-requisito", text="Pré-requisito")
        grade_tree.grid(row=0, column=0, padx=10, pady=10)

        # Preenche a tabela com os dados da grade
        for item in self.grade_data:
            grade_tree.insert("", "end", values=(item[0], item[1], item[2]))

        # Adicione um botão para fechar a janela da grade
        close_button = tk.Button(grade_window, text="Voltar ao menu", command=grade_window.destroy)
        close_button.grid(row=1, column=0, padx=10, pady=10)

    def clear_display(self):
        self.subject_listbox.delete(0, tk.END)
        self.subject_ids.clear()

    def remove_subject(self):
        # Lógica para remover matéria
        messagebox.showinfo("Remover Matéria", "Matéria removida com sucesso!")

    def request_history(self):
        # Lógica para solicitar histórico
        self.show_history_frame()
        
    def show_history_frame(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Seleção de Histórico")

        # Obtém as matérias disponíveis do banco de dados (substitua pela sua lógica de consulta)
        cursor = self.connection.cursor()
        cursor.execute("SELECT Nome_materia, Id FROM materias")
        todas_materias = cursor.fetchall()

        # Criação da Treeview para mostrar as matérias em forma de tabela
        grade_tree = ttk.Treeview(history_window, columns=("ID", "Matéria"), show="headings")
        grade_tree.heading("ID", text="ID")
        grade_tree.heading("Matéria", text="Matéria")
        grade_tree.grid(row=0, column=0, padx=10, pady=10)

        # Checkbox para cada matéria
        checkboxes = []
        def add_checkbox(materia_id):
            var = tk.IntVar()
            checkbox = tk.Checkbutton(grade_tree, variable=var)
            checkboxes.append((materia_id, var))
            grade_tree.window_create("end", window=checkbox)

            for materia_id, _ in todas_materias:
                add_checkbox(materia_id)
                grade_tree.insert("", "end", values=(materia_id, "Matéria " + str(materia_id)))


        # Botão para salvar as matérias selecionadas
        save_button = tk.Button(history_window, text="Salvar", command=lambda: self.save_history(checkboxes, history_window))
        save_button.grid(row=1, column=0, padx=10, pady=10)
    
    def save_history(self, checkboxes, window):
        # Limpa o histórico anterior
        self.historico.clear()

        # Salva as matérias marcadas no histórico do usuário
        for materia_id, var in checkboxes:
            if var.get() == 1:
                self.historico.append(materia_id)

        # Insere as informações no banco de dados (você precisa implementar essa parte)

        # Fecha a janela
        window.destroy()

    def request_subject(self):
        # Lógica para solicitar matéria
        messagebox.showinfo("Solicitar Matéria", "Matéria solicitada com sucesso!")

    def logout(self):
        self.logged_in = False
        self.show_login()

    def show_login(self):
        self.register_frame.grid_forget()
        self.menu_frame.grid_forget()
        self.login_frame.grid()

    def show_menu(self):
        self.login_frame.grid_forget()
        self.register_frame.grid_forget()
        self.menu_frame.grid()

    def __del__(self):
        try:
            self.connection.close()
            print("Conexao encerrada!\n")
        except mysql.connector.Error as err:
            print(f"Erro ao encerrar a conexao: {err}\n")

root = tk.Tk()
sistema = SistemaAcademico(root)

root.mainloop()