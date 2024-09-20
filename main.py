import tkinter as tk
from tkinter import messagebox, font as tkfont
import pandas as pd
import random

df_campeoes = pd.read_csv('formula_e_campeoes.csv')
df_calendarios = pd.read_csv('formula_e_calendarios.csv')

def consulta_campeao():
    temporada = entry_temporada.get()
    campeao = df_campeoes[df_campeoes['Temporada'] == temporada]
    if not campeao.empty:
        info = f"Temporada: {temporada}\nCampeão: {campeao['Piloto Campeão'].values[0]}"
    else:
        info = f"Temporada {temporada} não encontrada."
    messagebox.showinfo("Resultado", info)

def consulta_calendario():
    pais = entry_pais.get().capitalize()
    corridas = df_calendarios[df_calendarios['País'] == pais]
    if not corridas.empty:
        info = f"País: {pais}\nData: {corridas['Data(s)'].values[0]}"
    else:
        info = f"Corridas não encontradas para o país {pais}."
    messagebox.showinfo("Resultado", info)

def quiz_campeoes():
    temporada = random.choice(df_campeoes['Temporada'].unique())
    correto = df_campeoes[df_campeoes['Temporada'] == temporada]['Piloto Campeão'].values[0]
    resposta = entry_quiz.get()

    if resposta.lower() == correto.lower():
        messagebox.showinfo("Resultado", "Correto!")
    else:
        messagebox.showinfo("Resultado", f"Errado! O correto era {correto}.")

app = tk.Tk()
app.title("Fórmula E - Consulta e Quiz")
app.geometry("500x500")
app.config(bg="#333")

main_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
title_font = tkfont.Font(family="Helvetica", size=18, weight="bold", slant="italic")

label_titulo = tk.Label(app, text="Consulta de Informações", font=title_font, fg="#FFF", bg="#333")
label_titulo.pack(pady=20)

label_temporada = tk.Label(app, text="Digite a temporada (ex: 2022-23):", font=main_font, fg="#FFF", bg="#333")
label_temporada.pack()
entry_temporada = tk.Entry(app, font=main_font, width=20)
entry_temporada.pack(pady=10)

btn_campeao = tk.Button(app, text="Consultar Campeão", command=consulta_campeao, font=main_font, fg="#FFF", bg="#005DB4")
btn_campeao.pack(pady=10)

label_pais = tk.Label(app, text="Digite o país:", font=main_font, fg="#FFF", bg="#333")
label_pais.pack()
entry_pais = tk.Entry(app, font=main_font, width=20)
entry_pais.pack(pady=10)

btn_calendario = tk.Button(app, text="Consultar Corrida", command=consulta_calendario, font=main_font, fg="#FFF", bg="#005DB4")
btn_calendario.pack(pady=10)

label_quiz = tk.Label(app, text="Quiz de Campeões", font=title_font, fg="#FFF", bg="#333")
label_quiz.pack(pady=20)

label_quiz_pergunta = tk.Label(app, text="Quem foi o campeão?", font=main_font, fg="#FFF", bg="#333")
label_quiz_pergunta.pack()
entry_quiz = tk.Entry(app, font=main_font, width=20)
entry_quiz.pack(pady=10)

btn_quiz = tk.Button(app, text="Responder", command=quiz_campeoes, font=main_font, fg="#FFF", bg="#005DB4")
btn_quiz.pack(pady=10)

app.mainloop()
