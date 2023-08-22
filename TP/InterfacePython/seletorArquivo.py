import os
from tkinter import filedialog

#filenames = filedialog.askopenfilenames()
#print(filenames) #Mostra os endereços do arquivo, nao seleciona diretorio

#dirpath = filedialog.askdirectory()
#print(dirpath) #Seleciona diretorio

origem = filedialog.askdirectory()
destino = filedialog.askdirectory()

with open(os.path.join('InterfacePython', 'diretorios.csv'), 'w') as dircsv:
    dircsv.write('origem,destino')
    dircsv.write(f'{origem},{destino}')