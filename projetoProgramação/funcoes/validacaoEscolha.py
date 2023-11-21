def escolha_valida(escolhas_validas):
    
    esc = escolhas_validas

    try:
        escolha = int(input("\nEscolha a função >> "))
        if escolha not in esc:
            raise ValueError
        return escolha
    except ValueError:
        print(f"\nPor favor, insira um número válido de {min(esc)} a {max(esc)}.")
        return escolha_valida(esc)