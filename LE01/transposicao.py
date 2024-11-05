def cifra_transposicao_codificar(texto, chave):
    # Remover espaços e garantir que o texto seja contínuo
    texto = texto.replace(" ", "")
    
    # Calcular o número de colunas baseado no comprimento da chave
    num_colunas = len(chave)
    num_linhas = (len(texto) + num_colunas - 1) // num_colunas  # arredondar para cima
    
    # Preencher a matriz de acordo com o número de colunas e linhas
    matriz = [''] * num_colunas
    for i in range(len(texto)):
        coluna = i % num_colunas
        matriz[coluna] += texto[i]
    
    # Reordenar colunas conforme a chave
    chave_ordenada = sorted(list(chave))
    texto_cifrado = ''
    for coluna in chave_ordenada:
        index = chave.index(coluna)
        texto_cifrado += matriz[index]
    
    return texto_cifrado

def cifra_transposicao_decodificar(texto_cifrado, chave):
    # Calcular o número de colunas e linhas da matriz
    num_colunas = len(chave)
    num_linhas = (len(texto_cifrado) + num_colunas - 1) // num_colunas  # arredondar para cima
    
    # Determinar quantas células na última linha estão preenchidas
    num_celulas_preenchidas = len(texto_cifrado)
    
    # Ordenar a chave para saber a sequência das colunas cifradas
    chave_ordenada = sorted(list(chave))
    
    # Encontra a ordem original das colunas
    ordem_colunas = [chave.index(coluna) for coluna in chave_ordenada]
    
    # Determinar quantas letras há em cada coluna
    tamanhos_colunas = [num_linhas] * num_colunas
    total_celulas = num_linhas * num_colunas
    excesso = total_celulas - num_celulas_preenchidas
    for i in range(excesso):
        tamanhos_colunas[-(i+1)] -= 1  # Remover uma linha das últimas colunas
    
    # Dividir o texto cifrado de acordo com o tamanho de cada coluna
    indices = []
    indice_atual = 0
    for tamanho in tamanhos_colunas:
        indices.append((indice_atual, indice_atual + tamanho))
        indice_atual += tamanho
    
    # Criar uma lista com as colunas na ordem original
    colunas = [''] * num_colunas
    for i, coluna_index in enumerate(ordem_colunas):
        inicio, fim = indices[i]
        colunas[coluna_index] = texto_cifrado[inicio:fim]
    
    # Reconstruir o texto original linha por linha
    texto_decifrado = ''
    for i in range(num_linhas):
        for coluna in colunas:
            if i < len(coluna):
                texto_decifrado += coluna[i]
    
    return texto_decifrado

# Exemplo de uso
texto = "segredoimportante"
chave = "3124"  # A chave define a ordem das colunas

# Codificar
texto_cifrado = cifra_transposicao_codificar(texto, chave)
print("Texto original:", texto)
print("Texto cifrado:", texto_cifrado)

# Decodificar
texto_decifrado = cifra_transposicao_decodificar(texto_cifrado, chave)
print("Texto decifrado:", texto_decifrado)
