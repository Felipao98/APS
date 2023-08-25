import tkinter as tk

  
def home():
    global newWindow
    root.withdraw()
    newWindow = tk.Toplevel()
    newWindow.geometry("600x300")
    tk.Label(newWindow, text="Card Information").pack()
    homebutton = tk.Button(newWindow, text="Back to Home Screen", padx=50, pady=50, command=show, fg="black", bg="white")
    homebutton.pack()
      

def show():
    root.update()
    root.deiconify()
    newWindow.destroy()
 
root = tk.Tk()
root.geometry("600x300")
root.maxsize(600, 300)
root.minsize(600, 300)
root.title("eBot")
 
     
mybutton = tk.Button(root, text = "New Window", command = home)
mybutton.pack(pady = 10)
 
root.mainloop()