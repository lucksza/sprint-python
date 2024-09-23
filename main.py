import tkinter as tk
from tkinter import messagebox, font as tkfont, simpledialog, ttk
import pandas as pd
import random

df_campeoes = pd.read_csv('formula_e_campeoes.csv')

def iniciar_desafio():
    desafio_tipo = desafio_var.get()
    
    if desafio_tipo == "Piloto vs País":
        desafio_piloto_pais()
    elif desafio_tipo == "Piloto vs Montadora":
        desafio_piloto_montadora()

def desafio_piloto_pais():
    campeoes = df_campeoes.sample(5)
    resultado_texto = ""
    
    for _, row in campeoes.iterrows():
        alternativas = [row['País do Piloto Campeão'], "Brasil", "França", "Alemanha"]
        random.shuffle(alternativas)
        resposta = simpledialog.askstring("Desafio Piloto vs País", f"Qual o país de {row['Piloto Campeão']}?\nAlternativas: {', '.join(alternativas)}")
        if resposta and resposta.lower() == row['País do Piloto Campeão'].lower():
            resultado_texto += f"Correto! {row['Piloto Campeão']} é do país {row['País do Piloto Campeão']}\n"
        else:
            resultado_texto += f"Errado! {row['Piloto Campeão']} é do país {row['País do Piloto Campeão']}\n"
    
    messagebox.showinfo("Resultado", resultado_texto)

def desafio_piloto_montadora():
    campeoes = df_campeoes.sample(5)
    resultado_texto = ""
    
    for _, row in campeoes.iterrows():
        alternativas = [row['Montadora do Piloto Campeão'], "DS Techeetah", "Audi", "Jaguar"]
        random.shuffle(alternativas)
        resposta = simpledialog.askstring("Desafio Piloto vs Montadora", f"Qual a montadora de {row['Piloto Campeão']}?\nAlternativas: {', '.join(alternativas)}")
        if resposta and resposta.lower() == row['Montadora do Piloto Campeão'].lower():
            resultado_texto += f"Correto! {row['Piloto Campeão']} correu pela {row['Montadora do Piloto Campeão']}\n"
        else:
            resultado_texto += f"Errado! {row['Piloto Campeão']} correu pela {row['Montadora do Piloto Campeão']}\n"
    
    messagebox.showinfo("Resultado", resultado_texto)

app = tk.Tk()
app.title("Desafios Fórmula-E")
app.geometry("600x700")
app.config(bg="#333")

main_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
title_font = tkfont.Font(family="Helvetica", size=18, weight="bold", slant="italic")

label_titulo = tk.Label(app, text="Desafios de Fórmula-E", font=title_font, fg="#FFF", bg="#333")
label_titulo.pack(pady=20)

label_desafio_tipo = tk.Label(app, text="Escolha o Desafio", font=main_font, fg="#FFF", bg="#333")
label_desafio_tipo.pack(pady=10)

desafios = ["Piloto vs País", "Piloto vs Montadora"]
desafio_var = tk.StringVar(value="Piloto vs País")
desafio_menu = ttk.Combobox(app, textvariable=desafio_var, values=desafios, state="readonly", font=main_font)
desafio_menu.pack(pady=10)

btn_iniciar = tk.Button(app, text="Iniciar Desafio", command=iniciar_desafio, font=main_font, fg="#FFF", bg="#005DB4")
btn_iniciar.pack(pady=20)

curiosidade_label = tk.Label(app, text="Curiosidade: você sabia que um carro de Fórmula-E\npode atingir mais de 300km/h?", font=main_font, fg="#FFF", bg="#333")
curiosidade_label.pack(pady=10)

informacoes_label = tk.Label(app, text="Informações sobre a Fórmula-E:", font=main_font, fg="#FFF", bg="#333")
informacoes_label.pack(pady=20)

informacoes_texto = """
A Fórmula E é a principal competição de automobilismo
com veículos elétricos. Ela teve sua primeira temporada
em 2014-2015 e tem como objetivo promover a inovação
tecnológica sustentável. Pilotos de renome, como Nelson Piquet Jr.
e Lucas di Grassi, já conquistaram o título.
"""
informacoes_area = tk.Label(app, text=informacoes_texto, font=main_font, fg="#FFF", bg="#333", justify="left")
informacoes_area.pack(pady=10)

app.mainloop()
