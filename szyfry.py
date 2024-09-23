#Importing necersarry  libraries
try:
    import tkinter as tk 
    import subprocess
except ImportError:
    import os
    print("Error importing modules")
    os.system("pip install -r requirements.txt")
    print("Restarting...")
    os.system("python szyfry.py")


root = tk.Tk()

# Button action functions
def vinegr():
    subprocess.run(["python", "vinegre.py"])  
def cezar():
    subprocess.run(["python", "cezar.py"])


#Labels
label = tk.Label(root, text="Wybierz szyfr:")
label.grid(column= 0, row=0)

# Creating buttonds for each cipher
vinegr_b = tk.Button(root, text="Vinegret", command = vinegr)
vinegr_b.grid(column=0, row = 1)

cezar_b = tk.Button(root, text = "Cezar", command= cezar)
cezar_b.grid(column=0, row = 2)

root.mainloop()