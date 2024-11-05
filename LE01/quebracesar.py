import collections

frequencia_portugues = {
    'a': 13.9, 'b': 1.0, 'c': 4.4, 'd': 5.4, 'e': 12.2, 'f': 1.0,
    'g': 1.2, 'h': 0.8, 'i': 6.9, 'j': 0.4, 'k': 0.1, 'l': 2.8,
    'm': 4.2, 'n': 5.3, 'o': 10.8, 'p': 2.9, 'q': 0.9, 'r': 6.9,
    's': 7.9, 't': 4.9, 'u': 4.0, 'v': 1.3, 'w': 0.0, 'x': 0.3,
    'y': 0.0, 'z': 0.4
}

def descriptografar_cesar(texto, k):
    resultado = ""
    for char in texto:
        resultado += chr((ord(char) - k - 97) % 26 + 97)
    return resultado

def ataque_forca_bruta(texto_cifrado):
    possiveis_textos = []
    for k in range(1, 26):
        texto_descriptografado = descriptografar_cesar(texto_cifrado, k)
        possiveis_textos.append((k, texto_descriptografado))
    return possiveis_textos

def ataque_frequencia(texto_cifrado):
    frequencia_cifrado = collections.Counter(texto_cifrado)
    total_letras = sum(frequencia_cifrado.values())
    frequencia_cifrado = {char: (count / total_letras) * 100 for char, count in frequencia_cifrado.items()}
    menor_erro = float('inf')
    chave_correta = None
    texto_descriptografado = ""
    
    for k in range(26):
        erro_total = 0
        for char in frequencia_portugues:
            char_deslocado = chr((ord(char) + k - 97) % 26 + 97)
            frequencia_char = frequencia_cifrado.get(char_deslocado, 0)
            erro = (frequencia_char - frequencia_portugues[char]) ** 2
            erro_total += erro
        if erro_total < menor_erro:
            menor_erro = erro_total
            chave_correta = k
            texto_descriptografado = descriptografar_cesar(texto_cifrado, k)
    
    return chave_correta, texto_descriptografado

def cifra_cesar(texto, k):
    resultado = ""
    texto = "".join(char.lower() for char in texto if char.isalpha())
    print("Texto formatado:", texto)
    for char in texto:
        resultado += chr((ord(char) + k - 97) % 26 + 97)
    return resultado


texto_original = str(input("Digite o texto a ser cifrado: "))
texto_cifrado = cifra_cesar(texto_original, 3)
print("Texto cifrado:", texto_cifrado)
print("\n=== Ataque por Força Bruta ===")
possiveis_textos = ataque_forca_bruta(texto_cifrado)
for k, texto in possiveis_textos:
    print(f"Chave {k}: {texto}")
print("\n=== Ataque por Análise de Frequência ===")
chave_frequencia, texto_descriptografado = ataque_frequencia(texto_cifrado)
print(f"Chave encontrada: {chave_frequencia}")
print(f"Texto descriptografado: {texto_descriptografado}")
