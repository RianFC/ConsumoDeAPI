#  Esse cript foi feio para minha entrevista de emprego
#  para mercado radar. https://www.mercadoradar.com.br/


import os
from time import sleep

import httpx
from colorama import Fore

# mudancae os dados aqui

moedas = ["BTC", "ETH", "LTC"]  # Codinames das cripto moedas
cotacao = "USD"  # Moeda de compra ou venda
time = 30  # Tempo em segundos para cada pesquisa

# Banco de dados

db = {}

# definindo cores com o colorama

vermelho = Fore.RED
verde = Fore.GREEN
azul = Fore.BLUE
norm = Fore.RESET

# definindo cliente para deixar o código carregar mais rápdo
http = httpx.Client()


while True:
    rest = ""
    for moeda in moedas:
        # Carregando todas as moedas na lista moedas
        reqjson = http.request(
            "GET",
            "https://min-api.cryptocompare.com/data/price",
            params=dict(fsym=moeda, tsyms=cotacao),
        ).json()
        crip = reqjson[cotacao]

        rest += f"{moeda}: {cotacao} {crip}"

        # Verificando se tem o argumento anterior para ver a diferença
        if moeda in db:
            mudanca = round((crip / db[moeda] * 100) - 100, 3)

            if mudanca == 0:  # O valor continua o mesmo
                rest += f" {azul}{mudanca}%{norm}"
            elif mudanca > 0:  # O valor aumentou
                rest += f" {verde}+{mudanca}%{norm}"
            else:  # O valor diminuiu
                rest += f" {vermelho}{mudanca}%{norm}"
        rest += "\n"

        # Salvando na db para a proxima requisição
        db[moeda] = crip

    # Limpando o terminal e mandando o resultado
    os.system("cls" if os.name == "nt" else "clear")
    print(rest)

    # Esperando o tempo para a proxima requisição
    sleep(time)
