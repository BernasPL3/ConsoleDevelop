import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("ConsoleDevelop")
root.geometry("1000x600")

# Título
title = tk.Label(
    root,
    text="ConsoleDevelop",
    font=("Arial", 28)
)

title.pack(pady=20)

# Texto
subtitle = tk.Label(
    root,
    text="Crie projetos para PSP, PS2 e Nintendo 3DS",
    font=("Arial", 14)
)

subtitle.pack(pady=10)

# Funções
def psp_project():
    messagebox.showinfo(
        "PSP",
        "Projeto PSP criado!"
    )

def ps2_project():
    messagebox.showinfo(
        "PS2",
        "Projeto PS2 criado!"
    )

def ctr_project():
    messagebox.showinfo(
        "3DS",
        "Projeto Nintendo 3DS criado!"
    )

# Botões
btn_psp = tk.Button(
    root,
    text="Novo Projeto PSP",
    width=30,
    height=2,
    command=psp_project
)

btn_psp.pack(pady=10)

btn_ps2 = tk.Button(
    root,
    text="Novo Projeto PS2",
    width=30,
    height=2,
    command=ps2_project
)

btn_ps2.pack(pady=10)

btn_3ds = tk.Button(
    root,
    text="Novo Projeto 3DS",
    width=30,
    height=2,
    command=ctr_project
)

btn_3ds.pack(pady=10)

# Rodar app
root.mainloop()
