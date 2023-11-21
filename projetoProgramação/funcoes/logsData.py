from path import LOG_PATH as LOG
from collections import Counter

def varrer_log(arq):
    with open(arq, 'r') as arquivo: # Abre o arquivo em modo de leitura
        linhas = arquivo.readlines() # Lê todas as linhas do arquivo
    return linhas

def extrair_info_log(linhas):
    dados_logins = []
    usuarios = []
    datas = []
    for linha in linhas:
        dados = linha.strip().split(',')
        users = dados[0]
        if users not in usuarios: # Se o usuario não estiver na lista, adiciona o add na lista
            usuarios.append(users)
            data_login = dados[2]
            hora_login = dados[3]
            hora_logout = dados[4]
            dados_logins.append((users, data_login, hora_login, hora_logout)) # Extrai a data de login, a hora de login e a hora de logout
            datas.append(data_login)
    return dados_logins, usuarios, datas

def datas_maior_menor_login(datas):
    contagem_datas = Counter(datas) # Usa o Counter para contar a ocorrência de cada data na lista datas.
    data_maior_log = contagem_datas.most_common(1)[0][0] # Econtra a data com maior num de login (o 1 como argumento representa a extração das informações mais comuns, já os zeros é para obter os valores com o maiores numeros, no caso os logins)
    data_menor_log = contagem_datas.most_common()[-1][0] # Encontra a data com menor num de login (Utilizar o mostcommon sem argumento fará com que ele retorne todas as informações mais comuns. O -1 faz com que o ultimo índice seja acessado. Já o 0 é para obter os valores de menor valor)
    return data_maior_log, data_menor_log

def frequencia_login(dados_logins):
    count_users = Counter([dados[0] for dados in dados_logins]) # Conta a freq de cada usuario da lista
    freq_maior = [usuarios for usuarios, _ in count_users.most_common(1)] # Retorna uma lista de tuplas contendo os elementos mais comuns e a contagem de ocorrências de cada elemento
    freq_menor = [usuarios for usuarios, _ in count_users.most_common()[-1:]]
    return freq_maior, freq_menor

def verificar_login_datas():
    linhas = varrer_log(LOG)
    dados_logins, usuarios, datas = extrair_info_log(linhas)
    data_maior_log, data_menor_log = datas_maior_menor_login(datas)

    print(f"Data com maior quantidade de logins: {data_maior_log}")
    print(f"Data com menor quantidade de logins: {data_menor_log}")
    data = {data_maior_log, data_menor_log}
    return f'{data}'

def verificar_login_users():
    linhas = varrer_log(LOG)
    dados_logins, usuarios, datas = extrair_info_log(linhas)
    data_maior_log, data_menor_log = datas_maior_menor_login(datas)
    freq_maior, freq_menor = frequencia_login(dados_logins)
    print(f"Usuário que mais se loga no Sistema: {', '.join(freq_maior)}")
    print(f"Usuário que menos se loga no Sistema: {', '.join(freq_menor)}")

    req = [freq_maior, freq_menor]
    return f'{req}'