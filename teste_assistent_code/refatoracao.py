def calcular_estatisticas(numeros):
    """
    Recebe uma lista de números e retorna:
    total, média, maior valor e menor valor.
    """
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")

    total = sum(numeros)
    media = total / len(numeros)
    maior_valor = max(numeros)
    menor_valor = min(numeros)

    return total, media, maior_valor, menor_valor


# Uso da função
numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

total, media, maior, menor = calcular_estatisticas(numeros)

print("Total:", total)
print("Média:", media)
print("Maior:", maior)
print("Menor:", menor)