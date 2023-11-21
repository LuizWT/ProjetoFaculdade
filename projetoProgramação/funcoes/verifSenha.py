from path import LOG_PATH as LOG

def verificar_senha():
    usuarios_ativos = set()
    senhas_letras = 0
    senhas_digitos = 0
    senhas_alfanumericas = 0

    with open(LOG, "r") as arquivo_log:
        for linha in arquivo_log:
            dados = linha.strip().split(',')
            identificacao_usuario = dados[0]
            senha = dados[1]

            usuarios_ativos.add(identificacao_usuario)

            if senha.isalpha():
                senhas_letras += 1
            elif senha.isdigit():
                senhas_digitos += 1
            else:
                senhas_alfanumericas += 1

    return len(usuarios_ativos), senhas_letras, senhas_digitos, senhas_alfanumericas

def senha_verificada():
    usuarios, letras, digitos, alfanumericas = verificar_senha()
    print("Senhas (APENAS LETRAS):", letras)
    print("Senhas (APENAS DÍGITOS):", digitos)
    print("Senhas (ALFANUMÉRICAS):", alfanumericas)
    qnt = {letras, digitos, alfanumericas}
    return str(qnt)
