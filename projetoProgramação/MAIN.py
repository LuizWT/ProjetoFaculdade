from funcoes.logsData import verificar_login_datas, verificar_login_users
from funcoes.horarios import horarios_por_usuarios, horarios_gerais
from funcoes.verifSenha import verificar_senha, senha_verificada
from funcoes.validacaoEscolha import escolha_valida
from funcoes.usuariosAtivos import active_users
from funcoes.buscaData import busca_data
from funcoes.backup import fazer_backup
from funcoes.historico import historico

import datetime
import platform
import time
import os

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

def mensagem_com_delay(delay, msg):
    print(f'\n{msg}...\n')
    time.sleep(delay)

logo()
while True:

    escolhas_validas = range(1, (9)+1)
    esc = escolha_valida(escolhas_validas)

    if esc == 1:
        mensagem_com_delay(1, "Verificando Logins")
        result = verificar_login_datas()
        historico("[1] Verificacão de Datas de Login (Geral)", result)
        

    elif esc == 2:
        mensagem_com_delay(1, "Verificando Logins")
        result = verificar_login_users()
        historico("[2] Verificacao de Datas de Login por Usuário", result)


    elif esc == 3:
        mensagem_com_delay(1, "Verificando Senhas")
        result = senha_verificada()
        historico("[3] Verificacão de Senhas", result)


    elif esc == 4:
        mensagem_com_delay(1, "Verificando Horários")
        time.sleep(1.0)
        result = horarios_por_usuarios()
        historico("[4] Verificacao de tempo médio de Login (Por usuário)", result)
        

    elif esc == 5:
        mensagem_com_delay(1, "Verificando Horários")
        result = horarios_gerais()
        historico("[5] Verificacao de tempo médio de Login (Geral)", result)


    elif esc == 6:
        mensagem_com_delay(1, "Verificando Usuários Ativos")
        result = active_users()
        historico("[6] Verificacão de quantos usuários estão ativos", result)

    elif esc == 7:
        mensagem_com_delay(0.5, "Filtrando")
        result = busca_data()
        historico("[8] Filtrar busca por data", result)

    elif esc == 8:
        mensagem_com_delay(1, "Realizando Backup")
        result = fazer_backup()
        historico("[7] Realizacão de Backup", True)

    elif esc == 9:
        sys = platform.system().lower()
        if "linux" in sys or "darwin" in sys:
            os.system('clear')
        else:
            os.system('cls')
        historico("[9] Terminal Apagado", True)
        logo()

    elif esc not in escolhas_validas:
        pass


