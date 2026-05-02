# 📘 Explicação da Refatoração do Código

## 🎯 Objetivo

Melhorar o código original aplicando boas práticas de:

* Legibilidade
* Nomenclatura
* Uso de recursos nativos do Python
* Segurança (tratamento de erros)

---

## 🔁 Código Original (Resumo)

```python
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
    return t,m,mx,mn
```

### ⚠️ Problemas identificados:

* Nomes de variáveis pouco descritivos (`c`, `l`, `t`, `m`, etc.)
* Repetição de loops desnecessários
* Falta de validação (lista vazia causa erro)
* Código mais verboso do que o necessário

---

## ✅ Código Refatorado

```python
def calcular_estatisticas(lista_numeros):
    if not lista_numeros:
        raise ValueError("A lista não pode estar vazia")

    total = sum(lista_numeros)
    media = total / len(lista_numeros)
    maior = max(lista_numeros)
    menor = min(lista_numeros)

    return total, media, maior, menor
```

---

## 🔍 Principais Melhorias

### 1. 📛 Nomes mais claros e descritivos

Antes:

```python
def c(l):
```

Depois:

```python
def calcular_estatisticas(lista_numeros):
```

✔️ Agora é possível entender o propósito da função sem ler sua implementação.

---

### 2. 🧠 Uso de funções nativas do Python

Antes:

```python
for i in range(len(l)):
    t = t + l[i]
```

Depois:

```python
total = sum(lista_numeros)
```

✔️ Funções como `sum()`, `max()` e `min()`:

* Reduzem código
* Aumentam legibilidade
* São otimizadas internamente

---

### 3. ⚠️ Tratamento de erro

```python
if not lista_numeros:
    raise ValueError("A lista não pode estar vazia")
```

✔️ Evita problemas como:

* Divisão por zero
* Acesso a índices inexistentes

---

### 4. ✂️ Eliminação de redundância

Antes:

* Dois loops separados
* Inicialização manual de `mx` e `mn`

Depois:

* Tudo resolvido com funções prontas

✔️ Código mais limpo e direto

---

### 5. 📦 Melhor organização e retorno de dados

```python
return total, media, maior, menor
```

✔️ Mantém retorno simples, porém com variáveis nomeadas corretamente no uso

---

### 6. 🖨️ Melhor saída com f-strings

```python
print(f"Total: {total}")
```

✔️ Mais moderno e legível que concatenação tradicional

---

## ⚡ Comparação Geral

| Aspecto      | Antes ❌           | Depois ✅                 |
| ------------ | ----------------- | ------------------------ |
| Legibilidade | Baixa             | Alta                     |
| Tamanho      | Maior             | Menor                    |
| Performance  | Boa               | Melhor (funções nativas) |
| Segurança    | Nenhuma validação | Com tratamento de erro   |
| Manutenção   | Difícil           | Fácil                    |

---

## 🧠 Conclusão

A refatoração transformou um código funcional em um código:

* Mais profissional
* Mais fácil de entender
* Mais seguro e reutilizável

---

## 🚀 Próximos Passos

Você pode evoluir ainda mais:

* Criar testes automatizados (com `pytest`)
* Tipar a função com `type hints`
* Transformar em classe (POO)
* Documentar com docstrings

---

Se quiser, posso fazer essas melhorias para você 👍
