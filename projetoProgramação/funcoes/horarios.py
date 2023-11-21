from path import LOG_PATH as LOG
from datetime import datetime

tempo_login = {} # Armazenar os horarios do Login

total_login = 0
total_usuarios = 0

with open(LOG, 'r') as arquivo: # Formato 'r' (read) apenas para leitura
    for linha in arquivo:
        dados = linha.strip().split(',')
        identidade_usuarios = dados[0]
        hora_login = datetime.strptime(dados[3], '%H:%M:%S')
        hora_logout = datetime.strptime(dados[4], '%H:%M:%S')
        
        diferenca_login = hora_logout - hora_login
        
        if identidade_usuarios in tempo_login: # Atualiza o dicionário do inicio do script
            tempo_login[identidade_usuarios].append(diferenca_login)
        else:
            tempo_login[identidade_usuarios] = [diferenca_login]
        
        total_login += diferenca_login.total_seconds()
        total_usuarios += 1

tempo_medio_usuarios = {}
for usuario, tempos in tempo_login.items():
    tempo_total = sum([tempo.total_seconds() for tempo in tempos]) # Tempo médio de cada usuário
    tempo_medio = tempo_total / len(tempos)
    tempo_medio_usuarios[usuario] = tempo_medio

tempo_medio_geral = total_login / total_usuarios # Tempo médio geral

def horarios_por_usuarios():
    for usuario, tempo_medio in tempo_medio_usuarios.items():
        print(f"Tempo médio de login do usuário {usuario}: {tempo_medio} em segundos")
        res = {usuario, tempo_medio}
        return res
        
def horarios_gerais():
    print(f"Tempo médio de login geral: {tempo_medio_geral} (em segundos)")
    return tempo_medio_geral