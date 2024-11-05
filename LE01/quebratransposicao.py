def decifra_transposicao(texto_cifrado, chave):
    # Calcular o número de colunas e linhas da matriz
    num_colunas = len(chave)
    num_linhas = (len(texto_cifrado) + num_colunas - 1) // num_colunas  # arredondar para cima

    # Cria a matriz vazia para as colunas
    matriz = [""] * num_colunas

    # Ordena a chave para saber a sequência de leitura das colunas
    chave_ordenada = sorted(list(chave))

    # Encontra a ordem original das colunas
    ordem_colunas = [chave.index(coluna) for coluna in chave_ordenada]

    # Divide o texto cifrado de acordo com o número de linhas
    index = 0
    for coluna in ordem_colunas:
        # Calcula o número de caracteres em cada coluna
        comprimento_coluna = num_linhas if coluna < len(texto_cifrado) % num_colunas else num_linhas - 1
        matriz[coluna] = texto_cifrado[index:index + comprimento_coluna]
        index += comprimento_coluna

    # Reconstrói o texto original linha por linha
    texto_decifrado = ""
    for i in range(num_linhas):
        for coluna in matriz:
            if i < len(coluna):
                texto_decifrado += coluna[i]

    return texto_decifrado

# Exemplo de uso
texto_cifrado = "lnadoumo"  # Texto cifrado usando a chave "3124"
chave = "3124"
texto_decifrado = decifra_transposicao(texto_cifrado, chave)
print("Texto cifrado:", texto_cifrado)
print("Texto decifrado:", texto_decifrado)
