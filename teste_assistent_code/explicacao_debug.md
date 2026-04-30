# 🛠️ Correção de Código Python — Explicação

## 📌 Objetivo

Este documento explica os erros encontrados no código original, suas causas e as correções aplicadas para garantir o funcionamento correto e boas práticas de programação.

---

## ❌ 1. Erro de sintaxe no `input` (item 1)

### 🔎 Código com erro

```python
item1 = float(input(Preço do item 1? ))
```

### 💥 Causa

A mensagem dentro do `input()` não está entre aspas.
O Python interpreta isso como código inválido.

### ✅ Correção

```python
item1 = float(input("Preço do item 1? "))
```

---

## ❌ 2. Tipo de dado incorreto no desconto

### 🔎 Código com erro

```python
desconto_cupom = input("Você tem um cupom de desconto? (Digite o percentual ou 0): ")
desconto = subtotal * (desconto_cupom / 100)
```

### 💥 Causa

A função `input()` retorna uma **string**, mas o código tenta fazer um cálculo matemático com ela.

Isso gera erro:

```
TypeError: unsupported operand type(s)
```

### ✅ Correção

Converter o valor para número (`float`):

```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```

---

## ❌ 3. Falta de `f` na string formatada

### 🔎 Código com erro

```python
print(" Item 2:        R$ {total_item2:.2f}")
```

### 💥 Causa

Sem o `f` antes da string, o Python não interpreta `{}` como variável.

### ✅ Correção

```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

---

## ❌ 4. Erro de indentação no `if`

### 🔎 Código com erro

```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

### 💥 Causa

O Python exige indentação (recuo) para definir o bloco de código dentro do `if`.

### ✅ Correção

```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

---

## ❌ 5. Parênteses desnecessários

### 🔎 Código com problema

```python
desconto_cupom = (input(...))
```

### 💥 Causa

Os parênteses não causam erro, mas são desnecessários e deixam o código menos limpo.

### ✅ Correção

```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

---

## ✅ Código Corrigido

```python
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {total:.2f}")
print(linha)
```

---

## 🚀 Conclusão

Com as correções aplicadas:

* ✔️ O código executa sem erros
* ✔️ Os cálculos são feitos corretamente
* ✔️ A saída é exibida de forma formatada
* ✔️ O código segue boas práticas de legibilidade

---

Se quiser evoluir ainda mais, o próximo passo é:

* 🔹 Criar funções (modularização)
* 🔹 Validar entradas do usuário
* 🔹 Transformar isso em um mini sistema de vendas

Posso te ajudar nisso também 👍
