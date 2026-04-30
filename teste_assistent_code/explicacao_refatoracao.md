# 📊 Explicação do Código Refatorado

## 🔹 Objetivo

A função `calcular_estatisticas` recebe uma lista de números e retorna:

* ✅ Soma total dos valores
* ✅ Média dos valores
* ✅ Maior número da lista
* ✅ Menor número da lista

---

## 🔹 Código

```python
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
```

---

## 🔹 Explicação Linha a Linha

### 📌 Definição da função

```python
def calcular_estatisticas(numeros):
```

Define uma função chamada `calcular_estatisticas` que recebe uma lista chamada `numeros`.

---

### 📌 Docstring

```python
"""
Recebe uma lista de números e retorna:
total, média, maior valor e menor valor.
"""
```

Explica o que a função faz. Isso ajuda outros desenvolvedores (e você no futuro).

---

### 📌 Validação da entrada

```python
if not numeros:
    raise ValueError("A lista não pode estar vazia.")
```

Verifica se a lista está vazia.
Se estiver, gera um erro para evitar divisão por zero.

---

### 📌 Soma dos valores

```python
total = sum(numeros)
```

Usa a função nativa `sum()` para somar todos os elementos da lista.

---

### 📌 Cálculo da média

```python
media = total / len(numeros)
```

Divide o total pela quantidade de elementos (`len()`).

---

### 📌 Maior valor

```python
maior_valor = max(numeros)
```

Usa `max()` para encontrar o maior número da lista.

---

### 📌 Menor valor

```python
menor_valor = min(numeros)
```

Usa `min()` para encontrar o menor número da lista.

---

### 📌 Retorno da função

```python
return total, media, maior_valor, menor_valor
```

Retorna todos os resultados de uma vez (como uma tupla).

---

## 🔹 Uso da função

```python
numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
```

Cria uma lista de números.

```python
total, media, maior, menor = calcular_estatisticas(numeros)
```

Chama a função e armazena os resultados em variáveis separadas.

---

## 🔹 Saída

```python
print("Total:", total)
print("Média:", media)
print("Maior:", maior)
print("Menor:", menor)
```

Exibe os resultados no console:

```
Total: 346
Média: 34.6
Maior: 89
Menor: 2
```

---

## 🔹 Boas práticas aplicadas

* ✔️ Nomes descritivos
* ✔️ Uso de funções nativas (`sum`, `max`, `min`)
* ✔️ Validação de entrada
* ✔️ Código simples e legível
* ✔️ Documentação com docstring

---

Se quiser, posso te gerar uma versão **sem usar funções prontas** (mais “raiz”) ou uma versão com **tipagem (type hints)** para deixar ainda mais profissional.
