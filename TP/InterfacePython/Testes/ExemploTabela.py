from tkinter import *

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

root = Tk()
t = Table(root)
root.mainloop()
