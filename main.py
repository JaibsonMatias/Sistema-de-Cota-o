import PySimpleGUI as sg
from cotacao import pegar_cotacao

layout = [
    [sg.Text("Pegar Cotação de Moeda")],
    [sg.InputText(key="nome_cotacao".upper())],
    [sg.Button("Pegar Cotação"), sg.Button("Cancelar")],
    [sg.Text("", key="texto_cotacao")],
]

janela = sg.Window("Sistema de Cotação", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if evento == "Pegar Cotação":
        codigo_cotacao = valores["nome_cotacao".upper()]
        cotacao = pegar_cotacao(codigo_cotacao)
        janela["texto_cotacao"].update(f"A cotação da {codigo_cotacao} é de R$ :{cotacao}")


janela.close()