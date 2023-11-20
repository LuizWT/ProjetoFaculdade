import datetime
import os
def historico(logMsg, resultado=None):
    data = datetime.datetime.now()
    dataFormt = data.strftime("%d/%m/%y")
    horaFormt = data.strftime("%H:%M:%S")
    
    log = f"{dataFormt}, {horaFormt}, {logMsg}, {resultado}\n"
    
    with open('historico.txt', 'a') as arq:
        arq.write(log)

def buscaData():
    dataFiltro = input("Digite a data no formato DD/MM/YYYY: ")
    buscaFiltro = input("""\033[91m
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
    with open('historico.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    res = []

    for linha in linhas:
        info = linha.strip().split(', ')
        dataLog = info[0]
        buscaLog = info[2]

        if dataLog == dataFiltro and buscaFiltro in buscaLog: #verifica se a data é valida e se a busca também é
            res.append(linha)
            print(linha)

    return res