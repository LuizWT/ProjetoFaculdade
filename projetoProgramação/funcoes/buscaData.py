from path import RECORD_PATH as RECORD

import datetime
import os

def historico(log_msg, resultado=None):
    data = datetime.datetime.now()
    data_fmt = data.strftime("%d/%m/%y")
    hora_fmt = data.strftime("%H:%M:%S")
    
    log = f"{data_fmt}, {hora_fmt}, {log_msg}, {resultado}\n"
    
    with open(RECORD, 'a') as arq:
        arq.write(log)

def busca_data():
    data_filtro = input("Digite a data no formato DD/MM/YYYY: ")
    busca_filtro = input("""\033[91m
    [1] Verificação de Datas de Login geral
    [2] Verificação de Datas de Login por usuário
    [3] Verificação de Senhas
    [4] Verificação de tempo médio de Login (Por usuário)
    [5] Verificação de tempo médio de Login (Geral)
    [6] Verificação de quantos usuários estão ativos
    [7] Realizção de backup
    [0] Apagar o terminal
                         
    Digite o número da busca a ser filtrada: \033[0m""")

    os.system('color a')
    with open(RECORD, 'r') as arquivo:
        linhas = arquivo.readlines()

    res = []

    for linha in linhas:
        info = linha.strip().split(', ')
        data_log = info[0]
        busca_log = info[2]

        if data_log == data_filtro and busca_filtro in busca_log: # Verifica se a data é valida e se a busca também é
            res.append(linha)
            print(linha)

    return res