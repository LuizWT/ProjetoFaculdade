from path import LOG_PATH as LOG

def active_users():
    n = []
    arq = open(LOG, 'r')
    for linha in arq.readlines():
        Lin = linha.split(',')
        if Lin[0] not in n:
            n.append(Lin[0])
    qnt = len(n)
    print(f'Quantidade de Usuários Ativos: {qnt}')
    return f'Quantidade de Usuários Ativos: {qnt}'