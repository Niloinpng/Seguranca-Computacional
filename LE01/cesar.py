def cifra_cesar(texto, k):
    resultado = ""
    texto = "".join(char.lower() for char in texto if char.isalpha())

    for char in texto:
        resultado += chr((ord(char) + k - 97) % 26 + 97)

    return resultado

texto_original = str(input())

texto_cifrado = cifra_cesar(texto_original, 3)

print("Texto original:", texto_original)

print("Texto cifrado:", texto_cifrado)
