def escolhaValida():
    try:
        escolha = int(input("\nEscolha a função >> "))
        if escolha < 1 or escolha > 9:
            raise ValueError
        return escolha
    except ValueError:
        print("Por favor, insira um número válido de 1 a 9.")
        return escolhaValida()