def calcular_estatisticas(lista_numeros):
    if not lista_numeros:
        raise ValueError("A lista não pode estar vazia")

    total = sum(lista_numeros)
    media = total / len(lista_numeros)
    maior = max(lista_numeros)
    menor = min(lista_numeros)

    return total, media, maior, menor


# Uso da função
numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

total, media, maior, menor = calcular_estatisticas(numeros)

print(f"Total: {total}")
print(f"Média: {media}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")