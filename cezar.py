import tkinter as tk
import os
from tkinter import * 
from tkinter import messagebox 

root = tk.Tk()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

label = tk.Label(root, text="Wpisz tekst:")
label.grid(column= 0, row=0)

entry = tk.Entry(root)
entry.grid(column=0, row= 1)

shift_l = tk.Label(root, text="Podaj klucz")
shift_l.grid(column=0, row=2)

shift_e = tk.Entry(root)
shift_e.grid(column=0, row=3)

def cezar():
    text = entry.get().lower()  
    shift = shift_e.get()

    if not shift.isdigit():
        messagebox.showinfo(title="Wynik", message="Podaj prawidłowy klucz (liczba).")
    else:
        cipher_text = ""
        for letter in text:
            if letter in alphabet:  
                position = alphabet.index(letter)
                new_position = (position + int(shift)) % 26  
                cipher_text += alphabet[new_position]
            else:
                cipher_text += letter  

        messagebox.showinfo(title="Wynik", message="Po zakodowaniu tekst to: " + cipher_text)

cezar_b = tk.Button(root, text="Szyfruj", command=cezar)
cezar_b.grid(column=0, row=5)

root.mainloop()
