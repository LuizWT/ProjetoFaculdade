from datetime import datetime

tempoLogin = {} #armazenar os horarios do login

totalLogin = 0
totUsuarios = 0

with open('log.txt', 'r') as arquivo: #formato r apenas para faer a varredura
    for linha in arquivo:
        dados = linha.strip().split(',')
        identUsers = dados[0]
        horaLogin = datetime.strptime(dados[3], '%H:%M:%S')
        horaLogout = datetime.strptime(dados[4], '%H:%M:%S')
        
        Diflogin = horaLogout - horaLogin
        
        if identUsers in tempoLogin: #atualiza o dicionário do inicio do script
            tempoLogin[identUsers].append(Diflogin)
        else:
            tempoLogin[identUsers] = [Diflogin]
        
        totalLogin += Diflogin.total_seconds()
        totUsuarios += 1

TempoMedioUsers = {}
for usuario, tempos in tempoLogin.items():
    totalDeTempo = sum([tempo.total_seconds() for tempo in tempos]) #tempo médio de cada usuário
    tempoMedio = totalDeTempo / len(tempos)
    TempoMedioUsers[usuario] = tempoMedio

tempoMedioGeral = totalLogin / totUsuarios #tempo médio geral

def horariosPorUsuarios():
    for usuario, tempoMedio in TempoMedioUsers.items():
        print(f"Tempo médio de login do usuário {usuario}: {tempoMedio} em segundos")
        res = {usuario, tempoMedio}
        return res
        
def horariosGerais():
    print(f"\nTempo médio de login geral: {tempoMedioGeral} (em segundos)")
    return tempoMedioGeral

horariosGerais()