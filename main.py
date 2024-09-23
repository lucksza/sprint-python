import tkinter as tk
from tkinter import messagebox, font as tkfont
import pandas as pd


df_campeoes = pd.read_csv('formula_e_campeoes.csv')

def consulta_campeao():
    temporada = entry_temporada.get()
    campeao = df_campeoes[df_campeoes['Temporada'] == temporada]
    if not campeao.empty:
        info = (
            f"Temporada: {temporada}\n"
            f"Campeão: {campeao['Piloto Campeão'].values[0]}\n"
            f"País do Campeão: {campeao['País do Piloto Campeão'].values[0]}\n"
            f"Carro do Campeão: {campeao['Carro do Piloto Campeão'].values[0]}\n"
            f"Montadora do Campeão: {campeao['Montadora do Piloto Campeão'].values[0]}"
        )
    else:
        info = f"Temporada {temporada} não encontrada."
    messagebox.showinfo("Resultado", info)

def quiz_campeoes():
    temporada = entry_quiz_ano.get()
    campeao = df_campeoes[df_campeoes['Temporada'] == temporada]
    if campeao.empty:
        messagebox.showinfo("Resultado", f"Temporada {temporada} não encontrada.")
        return
    correto = campeao['Piloto Campeão'].values[0]
    resposta = entry_quiz_resposta.get()
    if resposta.lower() == correto.lower():
        info = (
            f"Correto!\n"
            f"Campeão: {correto}\n"
            f"País do Campeão: {campeao['País do Piloto Campeão'].values[0]}\n"
            f"Carro do Campeão: {campeao['Carro do Piloto Campeão'].values[0]}\n"
            f"Montadora do Campeão: {campeao['Montadora do Piloto Campeão'].values[0]}"
        )
        messagebox.showinfo("Resultado", info)
    else:
        messagebox.showinfo("Resultado", f"Errado! O campeão correto era {correto}.")

app = tk.Tk()
app.title("Fórmula-E")
app.geometry("500x700")
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

label_quiz = tk.Label(app, text="Quiz de Campeões", font=title_font, fg="#FFF", bg="#333")
label_quiz.pack(pady=20)

label_quiz_ano = tk.Label(app, text="Digite o ano da temporada (ex: 2022-23):", font=main_font, fg="#FFF", bg="#333")
label_quiz_ano.pack()
entry_quiz_ano = tk.Entry(app, font=main_font, width=20)
entry_quiz_ano.pack(pady=10)

label_quiz_resposta = tk.Label(app, text="Quem foi o campeão?", font=main_font, fg="#FFF", bg="#333")
label_quiz_resposta.pack()
entry_quiz_resposta = tk.Entry(app, font=main_font, width=20)
entry_quiz_resposta.pack(pady=10)

btn_quiz = tk.Button(app, text="Responder", command=quiz_campeoes, font=main_font, fg="#FFF", bg="#005DB4")
btn_quiz.pack(pady=10)

app.mainloop()
