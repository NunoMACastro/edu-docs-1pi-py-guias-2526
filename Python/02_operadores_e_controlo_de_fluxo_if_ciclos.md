# Python (10.º Ano) - 02 · Operadores e Controlo de Fluxo (`if`, `for`, `while`)

> **Objetivo deste ficheiro**  
> Dar-te o “motor” da lógica em Python: aprender a usar operadores, tomar decisões com `if/elif/else` e repetir ações com `while` e `for`.

---

## Índice

-   [0. Como usar este ficheiro](#0-como-usar-este-ficheiro)
-   [1. Operadores aritméticos](#1-operadores-aritm%C3%A9ticos)
-   [2. Operadores de comparação](#2-operadores-de-compara%C3%A7%C3%A3o)
-   [3. Operadores lógicos (`and`, `or`, `not`)](#3-operadores-l%C3%B3gicos-and-or-not)
-   [4. Operadores de pertinência e identidade](#4-operadores-de-pertin%C3%AAncia-e-identidade)
-   [5. Atribuições compostas (`+=`, `-=`, ...)](#5-atribui%C3%A7%C3%B5es-compostas----)
-   [6. Truthiness (o que é considerado “verdadeiro” ou “falso”)](#6-truthiness-o-que-%C3%A9-considerado-verdadeiro-ou-falso)
-   [7. Estruturas de seleção: `if`, `elif`, `else`](#7-estruturas-de-sele%C3%A7%C3%A3o-if-elif-else)
-   [8. Ciclo `while` - repetir enquanto a condição for verdadeira](#8-ciclo-while---repetir-enquanto-a-condi%C3%A7%C3%A3o-for-verdadeira)
-   [9. Ciclo `for` - percorrer sequências](#9-ciclo-for---percorrer-sequ%C3%AAncias)
-   [10. `range()` - gerar sequências numéricas](#10-range---gerar-sequ%C3%AAncias-num%C3%A9ricas)
-   [11. Blocos de código e indentação](#11-blocos-de-c%C3%B3digo-e-indenta%C3%A7%C3%A3o)
-   [12. Exercícios (Operadores, `if`, `for`, `while`)](#12-exerc%C3%ADcios-operadores-if-for-while)
-   [13. Changelog](#13-changelog)

---

## 0. Como usar este ficheiro

1. Lê a explicação teórica com calma.
2. Analisa os exemplos e tenta **prever o resultado antes** de os correr.
3. Reproduz os exemplos num ficheiro `.py` e faz pequenas alterações para experimentar.
4. No fim, resolve os **exercícios** (10–12), começando pelos mais fáceis.

Este ficheiro continua o que viste em:

-   `01_introducao_variaveis_tipos_strings_io.md` (variáveis, tipos, strings, `print`, `input`).

---

## 1. Operadores aritméticos

Em Python, os operadores aritméticos básicos são:

| Operador | Significado              | Exemplo  | Resultado |
| -------- | ------------------------ | -------- | --------- |
| `+`      | adição                   | `7 + 3`  | `10`      |
| `-`      | subtração                | `7 - 3`  | `4`       |
| `*`      | multiplicação            | `7 * 3`  | `21`      |
| `/`      | divisão real (float)     | `7 / 3`  | `2.3333…` |
| `//`     | divisão inteira          | `7 // 3` | `2`       |
| `%`      | resto da divisão inteira | `7 % 3`  | `1`       |
| `**`     | potência                 | `2 ** 3` | `8`       |

### 1.1. Diferença entre `/` e `//`

-   `/` devolve sempre um `float` (divisão “real”).
-   `//` faz divisão inteira, **descartando** a parte decimal.

```python
a = 7
b = 3

div_real = a / b     # 2.3333333333...
div_int  = a // b    # 2

print(div_real)
print(div_int)
```

### 1.2. Resto (`%`) e paridade

O operador `%` (módulo) devolve o resto da divisão inteira.

```python
print(7 % 3)   # 1  (7 = 2*3 + 1)
print(10 % 2)  # 0  (10 é múltiplo de 2)
print(11 % 2)  # 1
```

Isto é muito usado para saber se um número é **par** ou **ímpar**:

```python
n = 10

if n % 2 == 0:
    print("Par")
else:
    print("Ímpar")
```

### 1.3. Potência (`**`)

O operador `**` faz potência:

```python
print(2 ** 3)   # 8
print(5 ** 2)   # 25
print(9 ** 0.5) # 3.0  (raiz quadrada, cuidado com floats)
```

---

## 2. Operadores de comparação

Comparadores servem para perguntar “é igual?”, “é maior?”, “é menor?”, etc.  
Dão sempre como resultado um `bool`: `True` ou `False`.

| Operador | Significado    |
| -------- | -------------- |
| `==`     | igual a        |
| `!=`     | diferente de   |
| `>`      | maior que      |
| `>=`     | maior ou igual |
| `<`      | menor que      |
| `<=`     | menor ou igual |

Exemplos:

```python
a = 7
b = 3

print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a <= 10)  # True
```

### 2.1. Encadeamento de comparações

Python permite escrever comparações encadeadas de forma natural:

```python
x = 7

print(1 < x < 10)      # True (1 < x e x < 10)
print(1 < x <= 7)      # True
print(10 < x < 20)     # False
```

Isto é muito útil, por exemplo, para intervalos de notas ou idades.

---

## 3. Operadores lógicos (`and`, `or`, `not`)

Os operadores lógicos combinam condições.

-   `and` - verdadeiro se **ambas** as condições forem verdadeiras.
-   `or` - verdadeiro se **pelo menos uma** condição for verdadeira.
-   `not` - inverte o valor lógico (True → False, False → True).

### 3.1. Tabelas verdade simples

Com `True` e `False`:

| A     | B     | `A and B` | `A or B` |
| ----- | ----- | --------- | -------- |
| True  | True  | True      | True     |
| True  | False | False     | True     |
| False | True  | False     | True     |
| False | False | False     | False    |

`not`:

| A     | `not A` |
| ----- | ------- |
| True  | False   |
| False | True    |

Exemplo combinado:

```python
idade = 20
tem_carta = True

pode_conduzir = idade >= 18 and tem_carta
print(pode_conduzir)   # True se as duas condições forem verdade
```

### 3.2. “Short-circuit” (curto-circuito)

Python **pára de avaliar** assim que já sabe o resultado:

-   No `and`, se a primeira parte for `False`, não precisa de ver o resto.
-   No `or`, se a primeira parte for `True`, também não precisa de ver o resto.

Exemplo ilustrativo:

```python
def diz_ola():
    print("Função diz_ola foi chamada!")
    return True

print(False and diz_ola())   # não chama diz_ola (já sabe que é False)
print(True or diz_ola())     # não chama diz_ola (já sabe que é True)
```

Isto é importante quando a segunda condição é “cara” (ou pode dar erro) - podes usar a primeira condição como “filtro”.

---

## 4. Operadores de pertinência e identidade

### 4.1. Pertinência: `in` e `not in`

Usados para testar se um elemento está dentro de uma sequência (string, lista, etc.) ou das chaves de um dicionário.

```python
# Em strings
print("py" in "python")       # True
print("z" in "python")        # False

# Em listas
numeros = [1, 2, 3, 4]
print(3 in numeros)           # True
print(5 not in numeros)       # True

# Em dicionários (testa CHAVES)
aluno = {"nome": "Ana", "idade": 16}
print("nome" in aluno)        # True
print("Ana" in aluno)         # False (valor, não chave)
```

### 4.2. Identidade: `is` e `is not`

-   `==` compara **valores**.
-   `is` compara se são **o mesmo objeto em memória** (identidade).

No 10.º ano, a utilização mais importante é com `None`:

```python
x = None

if x is None:
    print("x ainda não tem valor útil")
else:
    print("x tem algum valor")
```

Regra prática para já:

-   Para comparar com `None`, usa `is None` ou `is not None`.
-   Para comparar valores (números, strings, etc.), usa `==` / `!=`.

---

## 5. Atribuições compostas (`+=`, `-=`, ...)

As atribuições compostas são uma forma mais curta de atualizar variáveis.

```python
x = 10

x = x + 1    # forma longa
x += 1       # forma curta (equivalente)

x -= 2       # x = x - 2
x *= 3       # x = x * 3
x /= 2       # x = x / 2
x //= 2      # x = x // 2
x %= 5       # x = x % 5
x **= 2      # x = x ** 2
```

São muito usadas em ciclos `for`/`while`, por exemplo para somar ou contar algo.

---

## 6. Truthiness (o que é considerado “verdadeiro” ou “falso”)

Em contextos booleanos (`if`, `while`), nem sempre se usa apenas `True` ou `False`.  
Certos valores contam como **falsos** automaticamente:

-   `0`, `0.0`
-   `""` (string vazia)
-   `[]` (lista vazia)
-   `{}` (dicionário vazio)
-   `None`

Todos os outros valores contam como **verdadeiros**.

```python
if "":
    print("Isto não aparece")    # string vazia é False
else:
    print("String vazia é tratada como False")

if [1, 2, 3]:
    print("A lista não está vazia")  # lista com elementos é True
```

Isto permite escrever condições mais naturais:

```python
texto = input("Escreve algo (ou deixa em branco): ")

if texto:
    print("Obrigado, escreveste:", texto)
else:
    print("Não escreveste nada.")
```

---

## 7. Estruturas de seleção: `if`, `elif`, `else`

Permitem tomar decisões, escolhendo um caminho de execução consoante uma condição.

### 7.1. Estrutura básica

```python
if condicao_principal:
    # bloco 1
    ...
elif outra_condicao:
    # bloco 2
    ...
else:
    # bloco 3 (caso contrário)
    ...
```

Exemplo com notas (0–20):

```python
nota = int(input("Introduz a nota (0-20): "))

if nota < 0 or nota > 20:
    print("Nota inválida.")
else:
    if nota >= 18:
        conceito = "Excelente"
    elif nota >= 14:
        conceito = "Bom"
    elif nota >= 10:
        conceito = "Suficiente"
    else:
        conceito = "Insuficiente"

    print("Conceito:", conceito)
```

Repara que usámos um `if` **aninhado** (dentro do `else`) para tratar primeiro o caso “nota inválida”.

### 7.2. Expressão condicional (operador ternário)

Forma mais compacta de escrever um `if/else` simples.

```python
nota = 15
resultado = "Aprovado" if nota >= 10 else "Reprovado"
print(resultado)
```

Lê-se: “resultado é `'Aprovado'` **se** `nota >= 10`, caso contrário `'Reprovado'`”.

É útil para expressões simples, mas não abuses em lógica complexa (fica difícil de ler).

---

## 8. Ciclo `while` - repetir enquanto a condição for verdadeira

O `while` repete um bloco **enquanto** a condição for `True`.

### 8.1. Estrutura básica

```python
while condicao:
    # bloco a repetir
    ...
```

Exemplo: contar de 1 até 3:

```python
i = 1

while i <= 3:
    print(i)
    i += 1   # MUITO IMPORTANTE: atualizar a variável
```

Sem atualizar `i`, a condição nunca deixaria de ser verdadeira e teríamos um **ciclo infinito**.

### 8.2. Exemplo: validar input

```python
nota = int(input("Nota (0-20): "))

while nota < 0 or nota > 20:
    print("Nota inválida. Tenta novamente.")
    nota = int(input("Nota (0-20): "))

print("Nota aceite:", nota)
```

Aqui usamos `while` para repetir até a condição “nota inválida” deixar de ser verdadeira.

---

## 9. Ciclo `for` - percorrer sequências

O `for` é ideal para **percorrer coleções** (listas, strings, ranges).

### 9.1. Estrutura básica

```python
for elemento in sequencia:
    # usar elemento
    ...
```

Exemplos:

```python
# Percorrer uma lista
nomes = ["Ana", "Bruno", "Carla"]

for nome in nomes:
    print("Olá,", nome)

# Percorrer uma string
palavra = "Python"

for letra in palavra:
    print(letra)
```

O `for` é muito usado com `range()`, que vamos ver a seguir.

---

## 10. `range()` - gerar sequências numéricas

`range()` gera uma sequência de inteiros (não é uma lista, mas comporta-se de forma parecida num `for`).

Formas principais:

-   `range(fim)` → 0, 1, 2, ..., fim-1
-   `range(inicio, fim)` → inicio, inicio+1, ..., fim-1
-   `range(inicio, fim, passo)` → sequência com o passo indicado (pode ser negativo)

Exemplos:

```python
print(list(range(5)))          # [0, 1, 2, 3, 4]
print(list(range(2, 7)))       # [2, 3, 4, 5, 6]
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]
```

Usado com `for`:

```python
# Somar números de 1 a 100
soma = 0
for i in range(1, 101):    # 1, 2, ..., 100
    soma += i

print("Soma =", soma)
```

Percorrer lista por índices:

```python
nomes = ["Ana", "Bruno", "Carla"]

for i in range(len(nomes)):      # 0, 1, 2
    print(i, nomes[i])
```

---

## 11. Blocos de código e indentação

Em muitas linguagens usam-se `{}` para delimitar blocos.  
Em Python, os blocos são definidos pela **indentação** (espaços no início da linha).

### 11.1. Regras importantes

-   Usa **4 espaços** por nível de indentação ou um TAB (não uses TAB misturado com espaços).
-   Todas as linhas com a mesma indentação pertencem ao mesmo bloco.
-   Os dois pontos `:` indicam que a seguir vem um bloco (`if`, `elif`, `else`, `for`, `while`, `def`, etc.).
-   Tudo o que vier depois dos dois pontos pertence ao bloco, até voltares à indentação anterior.

Exemplo com `if/else`:

```python
x = 12

if x > 10:
    # este é o bloco do if
    print("maior que 10")
else:
    # este é o bloco do else
    print("10 ou menos")
print("Fim da verificação")  # já fora do if/else (sem indentação)
```

Exemplo com `while`:

```python
contador = 0

while contador < 3:
    print("Contador:", contador)
    contador += 1   # ainda dentro do bloco do while

print("Fim do ciclo")  # já fora do ciclo (sem indentação)
```

Se a indentação estiver errada, o Python vai dar erros (`IndentationError`) ou, pior, o programa vai fazer algo inesperado.

---

## 12. Exercícios (Operadores, `if`, `for`, `while`)

> Tenta primeiro sem olhar para as soluções anteriores.  
> Alguns exercícios são versões reformuladas dos que já fizeste, mas agora estão agrupados por tema.

### Exercício 1 - Positivo, negativo ou zero

Lê um número inteiro do utilizador e diz se é:

-   “positivo”,
-   “negativo”,
-   ou “zero”.

Usa `if/elif/else`.

> Resolução:

```python
num = int(input("Escreve um número inteiro: "))
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Zero")
```

---

### Exercício 2 - Positivo e par / ímpar

Pede um número ao utilizador. Se o número for **positivo**:

-   diz se é **par** ou **ímpar** (usa `%`).

Se não for positivo, escreve uma mensagem a indicar que o número não é válido para esta verificação.

> Resolução:

```python
num = int(input("Escreve um número inteiro: "))
if num > 0:
    if num % 2 == 0:
        print("Positivo e par")
    else:
        print("Positivo e ímpar")
else:
    print("Número não é positivo.")
```

---

### Exercício 3 - Classificação de nota (0–20)

Lê uma nota inteira entre 0 e 20.

1. Se a nota for inválida (fora do intervalo), mostra uma mensagem de erro.
2. Caso seja válida, imprime:

    - "Excelente" (≥ 18)
    - "Bom" (14–17)
    - "Suficiente" (10–13)
    - "Insuficiente" (< 10)

Usa `if/elif/else`.

> Resolução:

```python
valor = int(input("Introduz a nota (0-20): "))
if valor < 0 or valor > 20:
    print("Nota inválida.")
else:
    if valor >= 18:
        nota = "Excelente"
    elif valor >= 14:
        nota = "Bom"
    elif valor >= 10:
        nota = "Suficiente"
    else:
        nota = "Insuficiente"
    print("Nota:", nota)
```

---

### Exercício 4 - Menor de três números (sem `min()`)

Pede 3 números (podem ser `float`) ao utilizador e, **sem usar** a função `min()`, imprime qual é o menor.

Dica: começa por assumir que o primeiro é o menor e vai comparando com os outros.

> Resolução:

```python
a = float(input("Escreve o 1.º número: "))
b = float(input("Escreve o 2.º número: "))
c = float(input("Escreve o 3.º número: "))

menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

print("O menor número é:", menor)
```

---

### Exercício 5 - Número dentro de um intervalo

Lê um número inteiro e diz se está entre 5 e 15 (inclusive).

Faz a verificação de duas maneiras:

1. Usando `if num >= 5 and num <= 15`.
2. Usando comparação encadeada `if 5 <= num <= 15`.

> Resolução:

```python
num = int(input("Escreve um número inteiro: "))

# Método 1
if num >= 5 and num <= 15:
    print("Está entre 5 e 15 (método 1)")
else:
    print("Não está entre 5 e 15 (método 1)")

# Método 2
if 5 <= num <= 15:
    print("Está entre 5 e 15 (método 2)")
else:
    print("Não está entre 5 e 15 (método 2)")
```

---

### Exercício 6 - Mesmo sinal

Lê dois números inteiros e indica se:

-   têm o **mesmo sinal** (ambos ≥ 0 ou ambos < 0),
-   ou se têm **sinais diferentes**.

Usa operadores lógicos (`and`, `or`).

> Resolução:

```python
a = int(input("Escreve o 1.º número inteiro: "))
b = int(input("Escreve o 2.º número inteiro: "))

if (a >= 0 and b >= 0) or (a < 0 and b < 0):
    print("Têm o mesmo sinal.")
else:
    print("Têm sinais diferentes.")
```

---

### Exercício 7 - Contagem decrescente

Pede um número inteiro ao utilizador.

Se for maior do que 1, faz uma contagem decrescente desse número até 0:

-   1.ª versão: usa um ciclo `for` com `range()`.
-   2.ª versão: usa um ciclo `while`.

Se o número não for maior que 1, mostra uma mensagem de erro.

> Resolução:

```python
n = int(input("Escreve um número inteiro maior que 1: "))
if n > 1:
    # Versão com for
    print("Contagem decrescente (for):")
    for i in range(n, -1, -1):
        print(i)

    # Versão com while
    print("Contagem decrescente (while):")
    contador = n
    while contador >= 0:
        print(contador)
        contador -= 1
else:
    print("Erro: o número não é maior que 1.")
```

---

### Exercício 8 - Somatório de 1 até `n`

Pede um número inteiro **positivo** `n` ao utilizador.

Se for válido:

1. Calcula o somatório `1 + 2 + ... + n` usando um ciclo `for`.
2. Mostra o resultado.

Se não for positivo, mostra mensagem de erro.

> Dica: usa `range(1, n + 1)`.

> Resolução:

```python
n = int(input("Escreve um número inteiro positivo: "))
if n > 0:
    soma = 0
    for i in range(1, n + 1):
        soma += i
    print("O somatório de 1 até", n, "é:", soma)
else:
    print("Erro: o número não é positivo.")
```

---

### Exercício 9 - Tabuada

Pede um número inteiro ao utilizador e mostra a tabuada desse número de 1 a 10, por exemplo:

```text
Tabuada do 7:
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

Usa um ciclo `for`.

> Resolução:

```python
num = int(input("Escreve um número inteiro para ver a tabuada: "))
print("Tabuada do", num, ":")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

---

### Exercício 10 - Jogo do número aleatório (máx. 5 tentativas)

Usando o módulo `random`:

1. Gera um número inteiro aleatório entre 1 e 100.
2. Dá ao utilizador **no máximo 5 tentativas** para adivinhar.
3. Em cada tentativa, diz se o palpite é “maior” ou “menor” do que o número secreto.
4. Se o utilizador acertar, mostra uma mensagem de parabéns com o número de tentativas usadas.
5. Se esgotar as 5 tentativas, revela o número.

Usa um ciclo `while` para controlar o número de tentativas.

> Resolução:

```python
import random

numero_secreto = random.randint(1, 100)
tentativas = 0
max_tentativas = 5
print("Tens 5 tentativas para adivinhar o número entre 1 e 100.")

while tentativas < max_tentativas:
    palpite = int(input("Escreve o teu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Adivinhaste o número em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("O número é maior.")
    else:
        print("O número é menor.")
else:
    print(f"Fim das tentativas! O número era {numero_secreto}.")
```

---

### Exercício 11 - Soma de múltiplos de 3

Usa um ciclo `for` com `range()` para:

1. Somar todos os múltiplos de 3 entre 1 e 100 (inclusive).
2. Mostrar o resultado final.

> Dica: podes usar `if i % 3 == 0` dentro do ciclo, ou então começar logo em 3 e usar um passo de 3: `range(3, 101, 3)`.

> Resolução:

```python
soma = 0
for i in range(3, 101, 3):  # Começa em 3, vai até 100, passo 3
    soma += i
print("A soma dos múltiplos de 3 entre 1 e 100 é:", soma)
```

---

### Exercício 12 (Desafio) - Estatísticas de notas

Escreve um programa que:

1. Vai pedindo notas inteiras ao utilizador (0–20).
2. A introdução da nota `-1` significa “terminar”.
3. No fim, o programa deve mostrar:
    - o número de notas introduzidas,
    - a média das notas,
    - quantas notas são **positivas** (≥ 10),
    - quantas são **negativas** (< 10).

Regras:

-   Ignora a nota `-1` nos cálculos (é só o sinal de paragem).
-   Se o utilizador escrever todas as notas inválidas (ou terminar sem nenhuma válida), trata esse caso (por exemplo, não tentes dividir por zero).

Sugestão: usa um ciclo `while` e acumula:

-   soma das notas,
-   contador de notas,
-   contador de positivas,
-   contador de negativas.

> Resolução:

```python
soma_notas = 0
contador_notas = 0
contador_positivas = 0
contador_negativas = 0

while True:
    nota = int(input("Escreve uma nota (0-20) ou -1 para terminar: "))
    if nota == -1:
        break
    if 0 <= nota <= 20:
        soma_notas += nota
        contador_notas += 1
        if nota >= 10:
            contador_positivas += 1
        else:
            contador_negativas += 1
    else:
        print("Nota inválida, tenta novamente.")
if contador_notas > 0:
    media = soma_notas / contador_notas
    print("Número de notas introduzidas:", contador_notas)
    print("Média das notas:", media)
    print("Número de notas positivas (≥ 10):", contador_positivas)
    print("Número de notas negativas (< 10):", contador_negativas)
else:
    print("Nenhuma nota válida foi introduzida.")
```

---

## 13. Changelog

> Registo de alterações importantes a este ficheiro.

-   **2025-11-17 · v1.2**
    -   Adicionadas soluções aos exercícios todos.
-   **2025-11-17 · v1.1**
    -   TOC atualizado.
-   **2025-11-17 · v1.0**
    -   Criação inicial do documento.
    -   Secções: operadores aritméticos, comparação, lógicos, pertinência/identidade, atribuições compostas, truthiness, `if/elif/else`, `while`, `for`, `range` e indentação.
    -   Adicionados 12 exercícios graduais focados em operadores, decisões e ciclos (`for`/`while`).
