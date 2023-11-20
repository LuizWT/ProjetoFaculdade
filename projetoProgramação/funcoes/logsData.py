from collections import Counter

def varrerLog(arq):
    with open(arq, 'r') as arquivo: #Abre o arquivo em modo de leitura
        linhas = arquivo.readlines() #Lê todas as linhas do arquivo
    return linhas

def extrairInfoLog(linhas):
    dadosLogins = []
    usuarios = []
    datas = []
    for linha in linhas:
        dados = linha.strip().split(',')
        users = dados[0]
        if users not in usuarios: #Se o usuario não estiver na lista, adiciona o add na lista
            usuarios.append(users)
            dataLogin = dados[2]
            horaLogin = dados[3]
            horaLogout = dados[4]
            dadosLogins.append((users, dataLogin, horaLogin, horaLogout)) #Extrai a data de login, a hora de login e a hora de logout
            datas.append(dataLogin)
    return dadosLogins, usuarios, datas

def DatasMaiorMenorLogin(datas):
    contagem_datas = Counter(datas) #Usa o Counter para contar a ocorrência de cada data na lista datas.
    dataMaiorLog = contagem_datas.most_common(1)[0][0] #Econtra a data com maior num de login (o 1 como argumento representa a extração das informações mais comuns, já os zeros é para obter os valores com o maiores numeros, no caso os logins)
    dataMenorLog = contagem_datas.most_common()[-1][0] #Encontra a data com menor num de login (Utilizar o mostcommon sem argumento fará com que ele retorne todas as informações mais comuns. O -1 faz com que o ultimo índice seja acessado. Já o 0 é para obter os valores de menor valor)
    return dataMaiorLog, dataMenorLog

def freqLogin(dadosLogins):
    countusers = Counter([dados[0] for dados in dadosLogins]) #Conta a freq de cada usuario da lista
    freqMaior = [usuarios for usuarios, _ in countusers.most_common(1)] #Retorna uma lista de tuplas contendo os elementos mais comuns e a contagem de ocorrências de cada elemento
    freqMenor = [usuarios for usuarios, _ in countusers.most_common()[-1:]]
    return freqMaior, freqMenor

def verifLoginDatas():
    arq = 'log.txt'
    linhas = varrerLog(arq)
    dadosLogins, usuarios, datas = extrairInfoLog(linhas)
    dataMaiorLog, dataMenorLog = DatasMaiorMenorLogin(datas)

    print(f"A data com mais logins foi: {dataMaiorLog}")
    print(f"A data com menos logins foi: {dataMenorLog}")
    data = {dataMaiorLog, dataMenorLog}
    return f'{data}'

def verifLoginUsers():
    arq = 'log.txt'
    linhas = varrerLog(arq)
    dadosLogins, usuarios, datas = extrairInfoLog(linhas)
    dataMaiorLog, dataMenorLog = DatasMaiorMenorLogin(datas)
    freqMaior, freqMenor = freqLogin(dadosLogins)
    print(f"O usuário que mais se loga no sistema é o: {', '.join(freqMaior)}")
    print(f"O usuário que menos se loga no sistema é: {', '.join(freqMenor)}")

    req = [freqMaior, freqMenor]
    return f'{req}'

    
verifLoginDatas()
verifLoginUsers()
