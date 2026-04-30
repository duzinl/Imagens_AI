# 🔍 Verificador de Números Primos em Python

Este projeto apresenta uma função otimizada e escrita com boas práticas de **Clean Code** para verificar se um número é primo.

---

## 📌 O que é um número primo?

Um número primo é aquele que:

* É maior que 1
* Possui exatamente dois divisores: **1 e ele mesmo**

Exemplos:

```
2, 3, 5, 7, 11, 13...
```

---

## 🧠 Implementação

```python
from math import isqrt

def eh_primo(numero: int) -> bool:
    """
    Verifica se um número é primo.

    Args:
        numero (int): Número a ser verificado

    Returns:
        bool: True se for primo, False caso contrário
    """
    if numero <= 1:
        return False

    if numero in (2, 3):
        return True

    if numero % 2 == 0:
        return False

    for divisor in range(3, isqrt(numero) + 1, 2):
        if numero % divisor == 0:
            return False

    return True
```

---

## ⚙️ Como a função funciona

A função segue uma abordagem eficiente:

1. Descarta números inválidos (≤ 1)
2. Trata diretamente os casos básicos (2 e 3)
3. Elimina números pares rapidamente
4. Testa divisores apenas até a raiz quadrada do número
5. Verifica apenas números ímpares

---

## 🚀 Exemplo de uso

```python
numero = 29

if eh_primo(numero):
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")
```

---

## ⚡ Otimizações aplicadas

* Uso de `math.isqrt()` para maior precisão e performance
* Redução de verificações desnecessárias
* Loop otimizado (apenas números ímpares)
* Retornos antecipados (early return)

---

## 🧹 Boas práticas (Clean Code)

* Nome de variável claro (`numero`)
* Função com responsabilidade única
* Uso de `docstring` padrão
* Código legível e organizado
* Baixa complexidade cognitiva

---

## 📚 Conclusão

A função `eh_primo` demonstra como aplicar conceitos de eficiência e Clean Code em Python, sendo uma solução ideal para aprendizado e uso prático em projetos.

---
