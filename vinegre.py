import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return key 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)]) 
    return "".join(key)

def encryption(string, key): 
    encrypt_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i].upper()) + ord(key[i].upper())) % 26
        x += ord('A') 
        encrypt_text.append(chr(x))
    encrypt_text = ''.join(encrypt_text)
    messagebox.showinfo(title="Output", message="Zaszyfrowany tekst to: " + str(encrypt_text))
    return encrypt_text

def decryption(string, key): 
    orig_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i].upper()) - ord(key[i].upper()) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x))
    orig_text = ''.join(orig_text)
    messagebox.showinfo(title="Output", message="Odszyfrowany tekst to: " + str(orig_text))
    return orig_text

# Functions to handle button clicks
def encrypt_text_action():
    string = string_e.get()
    keyword = keyword_e.get()
    key = generateKey(string, keyword)
    encryption(string, key)

def decrypt_text_action():
    string = string_e.get()
    keyword = keyword_e.get()
    key = generateKey(string, keyword)
    decryption(string, key)

if __name__ == "__main__": 
    root.title("Vigenère Cipher")

    # String input
    string_l = tk.Label(text="Podaj ciąg:")
    string_l.grid(column=0, row=0)
    string_e = tk.Entry()
    string_e.grid(column=1, row=0)

    # Key input
    keyword_l = tk.Label(text="Podaj klucz:")
    keyword_l.grid(column=0, row=1)
    keyword_e = tk.Entry()
    keyword_e.grid(column=1, row=1)

    # Buttons for encryption and decryption
    encrypt = tk.Button(text="Szyfruj", command=encrypt_text_action)
    encrypt.grid(column=0, row=2)
    
    decrypt = tk.Button(text="Odszyfruj", command=decrypt_text_action)
    decrypt.grid(column=1, row=2)

    root.mainloop()
