import tkinter as tk 
import subprocess


root = tk.Tk()

def vinegr():
    subprocess.run(["python", "vinegre.py"])  
def cezar():
    subprocess.run(["python", "cezar.py"])


label = tk.Label(root, text="Wybierz szyfr:")
label.grid(column= 0, row=0)

vinegr_b = tk.Button(root, text="Vinegret", command = vinegr)
vinegr_b.grid(column=0, row = 1)

cezar_b = tk.Button(root, text = "Cezar", command= cezar)
cezar_b.grid(column=0, row = 2)

root.mainloop()