def cifra_transposicao(texto, chave):

    texto = texto.replace(" ", "")
    num_colunas = len(chave)
    num_linhas = (len(texto) + num_colunas - 1) // num_colunas  
    matriz = [""] * num_colunas

    for i in range(len(texto)):
        coluna = i % num_colunas
        matriz[coluna] += texto[i]
    
    chave_ordenada = sorted(list(chave))
    texto_cifrado = ""

    for coluna in chave_ordenada:
        index = chave.index(coluna)
        texto_cifrado += matriz[index]
    
    return texto_cifrado

texto = str(input())
chave = "3124"  
texto_cifrado = cifra_transposicao(texto, chave)
print("Texto original:", texto)
print("Texto cifrado:", texto_cifrado)
