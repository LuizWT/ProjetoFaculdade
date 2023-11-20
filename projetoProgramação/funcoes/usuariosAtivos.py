def activeUsers():
    n = []
    arq = open("log.txt", 'r')
    for linha in arq.readlines():
        Lin = linha.split(',')
        if Lin[0] not in n:
            n.append(Lin[0])
    qnt = len(n)
    print(f'Quantidade de usuarios ativos: {qnt}')
    return f'Quantidade de usuarios ativos: {qnt}'

activeUsers()