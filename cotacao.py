import requests

def pegar_cotacao(codigo_moeda):
    try:
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f"{codigo_moeda}BRL".upper()]["bid"]
        return cotacao
    except:
        erro = "Moeda inválida, digite novamente por favor "
        return erro

