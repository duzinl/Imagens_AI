# 🐞 Debug e Correção do Código — Explicação Completa

## 🎯 Objetivo

Este documento explica os erros encontrados no código, suas causas e como corrigi-los corretamente, aplicando boas práticas em Python.

---

## ❌ 1. Erro de Tipo (TypeError)

### 🔍 Trecho com erro

```python
desconto_cupom = input("Você tem um cupom de desconto? (Digite o percentual ou 0): ")
desconto = subtotal * (desconto_cupom / 100)
```

### 💥 Causa

A função `input()` retorna uma **string**, mas o código tenta realizar uma operação matemática:

```python
"10" / 100  # inválido
```

Isso gera o erro:

```
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

### ✅ Correção

Converter o valor para número (`float`):

```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

---

## ❌ 2. Erro de Indentação (IndentationError)

### 🔍 Trecho com erro

```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

### 💥 Causa

Python exige **indentação obrigatória** após estruturas como `if`, `for`, `while`.

Erro gerado:

```
IndentationError: expected an indented block
```

### ✅ Correção

```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

---

## ❌ 3. Erro de String Formatada (f-string)

### 🔍 Trecho com erro

```python
print(" Item 2:        R$ {total_item2:.2f}")
```

### 💥 Causa

Falta do prefixo `f` na string.

Sem isso, o Python não interpreta `{}` como variável.

### ✅ Correção

```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

---

## ❌ 4. Erro de Sintaxe no input()

### 🔍 Trecho com erro

```python
item1 = float(input(Preço do item 1? ))
```

### 💥 Causa

Faltam aspas na string `"Preço do item 1? "`.

Erro gerado:

```
SyntaxError
```

### ✅ Correção

```python
item1 = float(input("Preço do item 1? "))
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

## 🧠 Conclusão

Durante o debug, identificamos erros comuns em Python:

| Tipo de Erro     | Causa                     | Solução                 |
| ---------------- | ------------------------- | ----------------------- |
| TypeError        | Uso de string como número | Converter com `float()` |
| IndentationError | Falta de indentação       | Indentar corretamente   |
| Erro de f-string | Falta do `f`              | Usar `f""`              |
| SyntaxError      | String sem aspas          | Adicionar aspas         |

---

## 🚀 Boas Práticas Aplicadas

* Validar tipos de entrada
* Usar f-strings corretamente
* Manter indentação consistente
* Escrever código legível

---

Se quiser, posso evoluir esse código para:

* 💡 Versão com funções
* 🧪 Testes automatizados
* 🧼 Clean Code completo
