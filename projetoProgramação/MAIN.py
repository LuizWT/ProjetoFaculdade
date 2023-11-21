import os
import datetime
from funcoes.verifSenha import senhaverificada
from funcoes.logsData import verifLoginDatas, verifLoginUsers
from funcoes.horarios import horariosPorUsuarios, horariosGerais
from funcoes.usuariosAtivos import activeUsers
from funcoes.backup import fazerBackup
from funcoes.buscaData import buscaData
from funcoes.historico import historico
from funcoes.validacaoEscolha import escolhaValida

os.system('color a')
os.system('cls')
def logo():
    print("""

    888      .d88888b.   .d8888b.  
    888     d88P" "Y88b d88P  Y88b  Feito por:
    888     888     888 888    888  Luiz Felipe
    888     888     888 888         
    888     888     888 888  88888 
    888     888     888 888    888 
    888     Y88b. .d88P Y88b  d88P
    88888888 "Y88888P"   "Y8888P8 

    [1] Verificação de Datas de Login geral
    [2] Verificação de Datas de Login por usuário
    [3] Verificação de Senhas
    [4] Verificação de tempo médio de Login (Por usuário)
    [5] Verificação de tempo médio de Login (Geral)
    [6] Verificação de quantos usuários estão ativos
    [7] Filtrar busca por data
    [8] Realização de backup
    [9] Apagar o terminal """)

logo()
while True:
    escolha = escolhaValida()

    if escolha == 1:
        print("\nVerificando login...\n")
        result = verifLoginDatas()
        msg = "[1] Verificacao de Datas de Login geral"
        historico(msg, result)
        

    elif escolha == 2:
        print("\nVerificando login...\n")
        msg = "[2] Verificacao de Datas de Login por usuario"
        result = verifLoginUsers()
        historico(msg, result)


    elif escolha == 3:
        print("\nVerificando senhas...\n")
        result = senhaverificada()
        msg = "[3] Verificacao de Senhas"
        historico(msg, result)


    elif escolha == 4:
        print("\nVerificando horários...\n")
        result = horariosPorUsuarios()
        msg = "[4] Verificacao de tempo medio de Login (Por usuario)"
        historico(msg, result)
        

    elif escolha == 5:
        print("\nVerificando horários...\n")
        result = horariosGerais()
        msg = "[5] Verificacao de tempo medio de Login (Geral)"
        historico(msg, result)


    elif escolha == 6:
        print("Verificando usuários ativos...\n")
        result = activeUsers()
        msg = "[6] Verificacao de quantos usuarios estao ativos"
        historico(msg, result)

    elif escolha == 7:
        print("\n")
        result = buscaData()
        msg = "[8] Filtrar busca por data"
        historico(msg, result)

    elif escolha == 8:
        print("Fazendo o backup...\n")
        result = fazerBackup()
        msg = "[7] Realizacao de backup"
        historico(msg, True)

    elif escolha == 9:
        os.system('cls')
        msg = "[9] Terminal apagado"
        historico(msg, True)
        logo()


    elif escolha is not 1 or 2 or 3 or 4 or 0:
        print("\nEscolha uma opcao valida!")
        msg = "Opcao invalida"
        historico(msg, False)


