# 📘 Explicação da Função `eh_primo`

## 🔍 Objetivo

A função `eh_primo(n)` tem como objetivo verificar se um número inteiro `n` é **primo**.

Um número primo é aquele que:

* É maior que 1
* Possui apenas dois divisores: **1 e ele mesmo**

---

## 🧠 Código da Função

```python
def eh_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True
```

---

## 🪜 Explicação Linha por Linha

### 🔹 `def eh_primo(n):`

Define uma função chamada `eh_primo` que recebe um número `n` como parâmetro.

---

### 🔹 `if n <= 1:`

Verifica se o número é menor ou igual a 1.

➡️ Se for, **não é primo**, pois números primos são maiores que 1.

```python
return False
```

---

### 🔹 `if n == 2:`

Verifica se o número é igual a 2.

➡️ O número 2 é o **único número primo par**.

```python
return True
```

---

### 🔹 `if n % 2 == 0:`

Verifica se o número é divisível por 2 (ou seja, se é par).

➡️ Se for par e diferente de 2, **não é primo**.

```python
return False
```

---

### 🔹 `for i in range(3, int(n**0.5) + 1, 2):`

Aqui está a parte mais importante da otimização 🚀

* `range(3, ...)` → começa do número 3
* `int(n**0.5) + 1` → vai até a **raiz quadrada de n**
* `2` → pula de 2 em 2 (testa apenas números ímpares)

📌 Por que só até a raiz quadrada?

Se um número tiver um divisor maior que a raiz, ele já teria um divisor menor antes disso.

---

### 🔹 `if n % i == 0:`

Verifica se `i` divide `n` exatamente.

➡️ Se sim, encontramos um divisor além de 1 e dele mesmo.

```python
return False
```

---

### 🔹 `return True`

Se nenhum divisor foi encontrado até o final do laço:

➡️ O número é **primo** ✅

---

## ⚡ Resumo da Lógica

1. Elimina números inválidos (`<= 1`)
2. Trata casos especiais (`2`)
3. Remove números pares
4. Testa divisores ímpares até a raiz quadrada
5. Se não encontrar divisor → número primo

---

## 💡 Exemplo

```python
eh_primo(7)   # True
eh_primo(10)  # False
```

---

## 🚀 Possíveis Melhorias

* Validar entrada (garantir que é inteiro)
* Criar versão com tratamento de erros
* Adicionar testes automatizados
* Melhorar legibilidade com comentários

---

Se quiser, posso:

* Criar uma versão ainda mais otimizada 🔥
* Gerar testes unitários 🧪
* Ou transformar isso em um pequeno projeto Python completo 📦
