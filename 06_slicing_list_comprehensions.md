# Python (10.º Ano) - 05 · Slicing e List Comprehensions

> **Objetivo deste ficheiro**  
> Perceber bem como “cortar” sequências em Python (listas, strings, etc.) com _slicing_ e como criar listas novas a partir de outras de forma compacta usando _list comprehensions_.

---

## Índice

-   [0. Guia para não te perderes](#0-guia-para-não-te-perderes)
-   [1. Revisão rápida: listas e sequências · \[ESSENCIAL\]](#1-revisão-rápida-listas-e-sequências--essencial)
-   [2. Índices e acesso simples · \[ESSENCIAL\]](#2-índices-e-acesso-simples--essencial)
-   [3. Slicing básico: `lista[início:fim]` · \[ESSENCIAL\]](#3-slicing-básico-listainíciofim--essencial)
-   [4. Slicing com passo e índices negativos · \[EXTRA mas muito útil\]](#4-slicing-com-passo-e-índices-negativos--extra-mas-muito-útil)
-   [5. Slicing em strings e outras sequências · \[ESSENCIAL (noção básica)\]](#5-slicing-em-strings-e-outras-sequências--essencial-noção-básica)
-   [6. Introdução a List Comprehensions · \[ESSENCIAL\]](#6-introdução-a-list-comprehensions--essencial)
-   [7. List Comprehensions com condição (filtro) · \[ESSENCIAL\]](#7-list-comprehensions-com-condição-filtro--essencial)
-   [8. List Comprehensions com `if/else` na expressão · \[EXTRA\]](#8-list-comprehensions-com-ifelse-na-expressão--extra)
-   [9. `for` normal vs List Comprehension · \[ESSENCIAL (mentalidade)\]](#9-for-normal-vs-list-comprehension--essencial-mentalidade)
-   [10. Outras comprehensions (sets, dicts, generators) · \[EXTRA / curiosidade\]](#10-outras-comprehensions-sets-dicts-generators--extra--curiosidade)
-   [11. Boas práticas e erros comuns · \[ESSENCIAL (mentalidade)\]](#11-boas-práticas-e-erros-comuns--essencial-mentalidade)
-   [12. Exercícios sobre slicing e comprehensions](#12-exercícios-sobre-slicing-e-comprehensions)
-   [13. Changelog](#13-changelog)

---

## 0. Guia para não te perderes

Aqui aparecem dois temas que costumam baralhar:

-   a sintaxe com dois pontos (`:`) no meio de listas e strings;
-   a sintaxe compacta das **list comprehensions**.

Para te organizares:

-   Foca-te primeiro em:
    -   **Secção 2 e 3** (índices e slicing básico),
    -   **Secção 6 e 7** (list comprehensions simples e com condição).
-   As partes marcadas como **[EXTRA]** lê quando estiveres confortável com o essencial.
-   Usa o interpretador (`python` / VS Code) para ir testando exemplos pequeninos.

---

## 1. Revisão rápida: listas e sequências · [ESSENCIAL]

Vamos relembrar alguns conceitos:

-   Uma **lista** em Python guarda vários valores numa ordem:

```python
numeros = [10, 20, 30, 40, 50]
nomes = ["Ana", "Bruno", "Carla"]
```

-   Uma **string** é também uma sequência de caracteres:

```python
texto = "Programador"
```

-   Outras sequências que aparecem mais tarde:
    -   `tuple` → `tuplo = (1, 2, 3)`
    -   `range` → `range(0, 10, 2)`

Todas estas estruturas têm duas características importantes:

1. Os elementos estão **numa ordem**.
2. Podemos aceder aos elementos usando **índices**.

---

## 2. Índices e acesso simples · [ESSENCIAL]

Antes de fazer _slicing_, tens de estar tranquilo com os **índices**.

-   Em Python, os índices começam em **0**.
-   Índice 0 → primeiro elemento.
-   Índice 1 → segundo, e por aí fora.

```python
numeros = [10, 20, 30, 40, 50]

print(numeros[0])  # 10
print(numeros[1])  # 20
print(numeros[4])  # 50 (5.º elemento)
```

Se tentares aceder a um índice que não existe, tens erro:

```python
print(numeros[5])  # IndexError: list index out of range
```

Também podes usar **índices negativos**:

-   `-1` → último elemento
-   `-2` → penúltimo
-   etc.

```python
print(numeros[-1])  # 50
print(numeros[-2])  # 40
```

Isto funciona de forma semelhante em **strings**:

```python
texto = "Python"
print(texto[0])   # 'P'
print(texto[-1])  # 'n'
```

---

## 3. Slicing básico: `lista[início:fim]` · [ESSENCIAL]

O _slicing_ permite-te obter **uma parte** de uma lista (ou string).

Sintaxe básica:

```python
sublista = lista[inicio:fim]
```

-   `inicio` → índice onde começa (inclui esse elemento).
-   `fim` → índice onde **pára** (não inclui esse elemento).
-   O resultado é uma **nova lista** (não altera a original).

Imagina:

```python
numeros = [10, 20, 30, 40, 50, 60]
# índices:  0   1   2   3   4   5
```

### 3.1. Exemplos simples

```python
print(numeros[0:3])  # [10, 20, 30]  (índices 0, 1, 2)
print(numeros[2:5])  # [30, 40, 50]  (índices 2, 3, 4)
```

Repara: o índice `fim` é **exclusivo**, ou seja, não é incluído na fatia.

### 3.2. Omitir `inicio` ou `fim`

Se **não escreveres** o `inicio`, assume-se o início da lista.  
Se **não escreveres** o `fim`, assume-se o fim da lista.

```python
print(numeros[:3])   # [10, 20, 30]  (do início até antes do índice 3)
print(numeros[3:])   # [40, 50, 60]  (do índice 3 até ao fim)
print(numeros[:])    # cópia da lista inteira
```

Esta forma `lista[:]` é muito usada para fazer uma **cópia superficial** da lista.

---

## 4. Slicing com passo e índices negativos · [EXTRA mas muito útil]

Existe uma forma mais completa:

```python
sublista = lista[inicio:fim:passo]
```

-   `passo` → de quantos em quantos índices avança.
    -   Se for 1 → vai elemento a elemento.
    -   Se for 2 → salta de 2 em 2, etc.

### 4.1. Passo positivo

```python
numeros = [10, 20, 30, 40, 50, 60]

print(numeros[0:6:2])  # [10, 30, 50]
print(numeros[1:6:2])  # [20, 40, 60]
```

Também podes omitir o `inicio` e/ou `fim`:

```python
print(numeros[::2])    # [10, 30, 50]  (do início ao fim, de 2 em 2)
print(numeros[1::2])   # [20, 40, 60]  (a partir do índice 1, de 2 em 2)
```

### 4.2. Passo negativo (reverso)

Se o `passo` for negativo, a sequência anda **para trás**.

```python
numeros = [10, 20, 30, 40, 50, 60]

print(numeros[::-1])   # [60, 50, 40, 30, 20, 10]  (lista ao contrário)
print(numeros[4:1:-1]) # [50, 40, 30]  (dos índices 4 até > 1, a recuar)
```

Para strings:

```python
texto = "Python"
print(texto[::-1])  # "nohtyP"
```

### 4.3. Índices negativos no slicing

Podes misturar índices positivos com negativos:

```python
numeros = [10, 20, 30, 40, 50, 60]
# índices:  0   1   2   3   4   5
# neg.:    -6  -5  -4  -3  -2  -1

print(numeros[1:-1])   # [20, 30, 40, 50]
print(numeros[-3:])    # [40, 50, 60]
print(numeros[:-2])    # [10, 20, 30, 40]
```

---

## 5. Slicing em strings e outras sequências · [ESSENCIAL (noção básica)]

O _slicing_ não é só para listas.  
Funciona com **qualquer sequência** que suporte índices:

-   strings,
-   tuplos,
-   `range` (parcialmente), etc.

### 5.1. Slicing em strings

```python
texto = "Programador"

print(texto[0:4])   # "Prog"
print(texto[:7])    # "Program"
print(texto[4:])    # "ramador"
print(texto[::-1])  # "rodamargorP"
```

Isto é muito útil para:

-   apanhar prefixos e sufixos,
-   eliminar partes iniciais ou finais,
-   verificar certas estruturas (por exemplo, extensões de ficheiros).

### 5.2. Slicing em tuplos

```python
pontos = (10, 20, 30, 40, 50)

print(pontos[1:4])  # (20, 30, 40)
print(pontos[::-1]) # (50, 40, 30, 20, 10)
```

---

## 6. Introdução a List Comprehensions · [ESSENCIAL]

Uma **list comprehension** é uma forma **compacta** de criar listas a partir de outras listas (ou sequências).

Forma geral mais simples:

```python
nova_lista = [expressao for item in iteravel]
```

-   `iteravel` → algo que podes percorrer com `for` (lista, string, range, etc.).
-   `item` → cada elemento do iterável.
-   `expressao` → o que queres pôr na nova lista.

### 6.1. Exemplo: quadrados de números

Versão normal com `for`:

```python
numeros = [1, 2, 3, 4, 5]
quadrados = []

for n in numeros:
    quadrados.append(n ** 2)

print(quadrados)  # [1, 4, 9, 16, 25]
```

Versão com list comprehension:

```python
numeros = [1, 2, 3, 4, 5]
quadrados = [n ** 2 for n in numeros]

print(quadrados)  # [1, 4, 9, 16, 25]
```

### 6.2. Exemplo: converter strings para maiúsculas

```python
nomes = ["ana", "bruno", "carla"]
nomes_maiusc = [nome.upper() for nome in nomes]

print(nomes_maiusc)  # ["ANA", "BRUNO", "CARLA"]
```

Regra mental:

1. Escreve primeiro a versão com `for` “normal”.
2. Se ficas com um padrão “criar lista vazia + append”, considera transformar numa list comprehension.

---

## 7. List Comprehensions com condição (filtro) · [ESSENCIAL]

Podemos adicionar uma **condição** para filtrar elementos:

```python
nova_lista = [expressao for item in iteravel if condição]
```

A `condição` é uma expressão que deve devolver `True` ou `False`.  
Só os elementos para os quais a condição é `True` entram na nova lista.

### 7.1. Exemplo: filtrar números pares

Versão normal:

```python
numeros = [1, 2, 3, 4, 5, 6]
pares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)

print(pares)  # [2, 4, 6]
```

Versão com list comprehension:

```python
numeros = [1, 2, 3, 4, 5, 6]
pares = [n for n in numeros if n % 2 == 0]

print(pares)  # [2, 4, 6]
```

### 7.2. Exemplo: comprimentos de nomes com 4 ou mais letras

```python
nomes = ["Ana", "Bruno", "Carla", "Di"]
comprimentos = [len(nome) for nome in nomes if len(nome) >= 4]

print(comprimentos)  # [5, 5]
```

---

## 8. List Comprehensions com `if/else` na expressão · [EXTRA]

Também é possível pôr um `if/else` na **expressão**, em vez de ser no fim.  
Isto permite transformar os valores de forma diferente conforme o caso.

Forma geral:

```python
nova_lista = [expr_se_verdadeiro if condição else expr_se_falso
              for item in iteravel]
```

Exemplo: classificar números como `"par"` ou `"ímpar"`:

```python
numeros = [1, 2, 3, 4, 5]
tipos = ["par" if n % 2 == 0 else "ímpar" for n in numeros]

print(tipos)  # ["ímpar", "par", "ímpar", "par", "ímpar"]
```

Atenção: não confundas com `if` de filtro.

-   `[...] for n in numeros if condição]` → tira fora alguns elementos.
-   `[..., "par" if condição else "ímpar", ...]` → mantém todos, mas muda o valor.

---

## 9. `for` normal vs List Comprehension · [ESSENCIAL (mentalidade)]

### 9.1. Quando usar `for` normal

-   Quando a lógica é **complicada** (vários `if`, vários passos).
-   Quando há **efeitos secundários** (ex.: `print` dentro do ciclo, escrever em ficheiros).
-   Quando precisas de **debugar** e ver passo a passo.

Exemplo (talvez demasiado para comprehension):

```python
resultado = []
for n in numeros:
    if n % 2 == 0:
        valor = n ** 2
        print("Quadrado de", n, "=", valor)
        resultado.append(valor)
```

### 9.2. Quando usar list comprehension

-   Quando queres **apenas criar uma nova lista** a partir de outra,
-   com uma transformação simples,
-   e opcionalmente um **filtro** simples.

Exemplos típicos:

-   Quadrados, cubos, comprimentos de strings.
-   Filtrar _pares_, _positivos_, _nomes com mais de X letras_, etc.

Regra prática:

> Se precisas de 3 coisas:
>
> 1. lista nova, 2) transformação simples, 3) filtro simples →  
>    **list comprehension** costuma ser uma boa opção.

---

## 10. Outras comprehensions (sets, dicts, generators) · [EXTRA / curiosidade]

A ideia das comprehensions não é exclusiva das listas.

### 10.1. Set comprehension

Cria um **conjunto** (sem repetições):

```python
numeros = [1, 2, 2, 3, 3, 3]
sem_repetidos = {n for n in numeros}

print(sem_repetidos)  # {1, 2, 3}  (ordem não garantida)
```

### 10.2. Dict comprehension

Cria um **dicionário**:

```python
nomes = ["Ana", "Bruno", "Carla"]
tamanhos = {nome: len(nome) for nome in nomes}

print(tamanhos)  # {"Ana": 3, "Bruno": 5, "Carla": 5}
```

### 10.3. Generator expression

Parecido com list comprehension mas com `()` em vez de `[]`.  
Não cria a lista toda de uma vez, vai gerando à medida que é preciso.

```python
numeros = [1, 2, 3, 4, 5]
gen = (n ** 2 for n in numeros)

for valor in gen:
    print(valor)
```

Neste ano, o importante é perceber primeiro bem as **list comprehensions**.

---

## 11. Boas práticas e erros comuns · [ESSENCIAL (mentalidade)]

### 11.1. Não abuses da “magia”

-   Se a expressão fica demasiado longa, a legibilidade piora.
-   Várias condições encadeadas podem tornar o código confuso.

É preferível um `for` normal bem claro do que uma comprehension que ninguém percebe.

### 11.2. Evita efeitos secundários em comprehensions

Tecnicamente podes fazer:

```python
[print(n) for n in numeros]
```

Mas isto é considerado **má prática**:  
uma list comprehension deve ser usada para **criar listas**, não para fazer `print`.

Melhor:

```python
for n in numeros:
    print(n)
```

### 11.3. Atenção a índices no slicing

Erros típicos:

-   Enganar-se a contar (lembrar: o `fim` não é incluído).
-   Esquecer que `lista[a:b]` nunca dá erro se `b` for grande demais; simplesmente corta até onde conseguir:

```python
numeros = [10, 20, 30]
print(numeros[0:10])  # [10, 20, 30]  (não dá erro)
```

-   Usar `[::-1]` sem perceber que está a inverter a sequência.

Sempre que estiveres confuso, escreve numa folha a lista com os índices por baixo e marca o intervalo `[inicio, fim[` (fechado à esquerda, aberto à direita).

---

## 12. Exercícios sobre slicing e comprehensions

> Sugestão: começa nos exercícios básicos, depois passa para os intermédios e desafios.  
> Podes (e deves) testar cada exercício no interpretador Python ou no VS Code.

### Exercício 1 · Slicing básico numa lista · [BÁSICO]

Dada a lista:

```python
numeros = [10, 20, 30, 40, 50, 60, 70]
```

Usando apenas _slicing_ (`lista[inicio:fim]`), cria expressões que devolvam:

1. `[10, 20, 30]`
2. `[40, 50, 60]`
3. `[30, 40, 50, 60]`
4. Uma cópia completa da lista.

---

### Exercício 2 · Slicing com índices negativos · [BÁSICO]

Usa _slicing_ e índices negativos para, a partir de:

```python
letras = ["a", "b", "c", "d", "e", "f"]
```

obter:

1. `["d", "e", "f"]`
2. `["b", "c", "d", "e"]`
3. `["e", "f"]` usando apenas índices negativos.

---

### Exercício 3 · Slicing em strings · [BÁSICO]

Dado:

```python
texto = "Programador Informático"
```

Usa _slicing_ para obter:

1. `"Programador"`
2. `"Informático"`
3. A string ao contrário.

---

### Exercício 4 · Slicing com passo · [MÉDIO]

Com a lista:

```python
nums = list(range(1, 21))  # [1, 2, 3, ..., 20]
```

Usa _slicing_ com `passo` para obter:

1. Todos os números ímpares.
2. Todos os números pares.
3. A lista `[20, 18, 16, 14, 12, 10]`.

---

### Exercício 5 · Quadrados com list comprehension · [BÁSICO]

Cria uma **list comprehension** que, a partir de:

```python
nums = [1, 2, 3, 4, 5]
```

devolva:

```python
[1, 4, 9, 16, 25]
```

---

### Exercício 6 · Filtrar pares com list comprehension · [BÁSICO]

Dada a lista:

```python
nums = [3, 8, 12, 5, 7, 20, 21]
```

Cria uma list comprehension que devolva apenas os **números pares**.

---

### Exercício 7 · Comprimentos de nomes com filtro · [MÉDIO]

Dada a lista:

```python
nomes = ["Ana", "Bruno", "Carla", "Diogo", "Eva"]
```

Cria uma list comprehension que devolva uma lista com os **comprimentos dos nomes** que têm **4 ou mais letras**.

Exemplo de saída:

```python
[5, 5, 5]
```

---

### Exercício 8 · Classificar números como "par"/"ímpar" · [MÉDIO]

Dada a lista:

```python
nums = [1, 2, 3, 4, 5, 6]
```

Usa uma list comprehension com `if/else` na **expressão** para obter:

```python
["ímpar", "par", "ímpar", "par", "ímpar", "par"]
```

---

### Exercício 9 · Misto de slicing e comprehension · [MÉDIO]

Dada a lista:

```python
palavras = ["Python", "Programador", "Lista", "Comprehension"]
```

1. Usa _slicing_ para obter uma nova lista com apenas as **duas últimas letras** de cada palavra (podes usar um `for` normal).
2. Depois, faz o mesmo mas usando uma **list comprehension** (e slicing dentro da expressão).

Exemplo de saída:

```python
["on", "or", "ta", "on"]
```

---

### Exercício 10 (Desafio) · Filtrar e transformar ao mesmo tempo · [DESAFIO]

Dada a lista:

```python
nums = list(range(-5, 11))  # de -5 até 10
```

Usa **uma única list comprehension** para criar uma lista com:

-   os quadrados dos números **positivos**,
-   mas **apenas** daqueles que são **pares**.

Exemplo (não é a resposta completa):

```python
[4, 16, 36, ...]
```

---

### Exercício 11 (Desafio) · Slicing em “janelas” · [DESAFIO]

Dada a lista:

```python
dados = [10, 20, 30, 40, 50, 60]
```

Cria um código que produza uma lista de **sub-listas**, em que cada sub-lista tem 3 elementos consecutivos:

```python
[[10, 20, 30],
 [20, 30, 40],
 [30, 40, 50],
 [40, 50, 60]]
```

Sugestão:

-   Usa um ciclo `for` sobre os índices.
-   Em cada iteração, usa _slicing_ `dados[i:i+3]`.
-   Depois, tenta transformar a solução numa list comprehension.

---

## 13. Changelog

> Registo de alterações importantes a este ficheiro.

-   **2025-11-26 · v1.0**
    -   Criação inicial do documento.
    -   Secções essenciais: revisão de sequências, índices, slicing básico, slicing em strings, introdução a list comprehensions e comprehensions com filtro.
    -   Secções extra: slicing com passo e índices negativos, comprehensions com `if/else`, outras comprehensions (sets, dicts, generators).
    -   Adicionados exercícios graduais (slicing básico, comprehensions, misto slicing+comprehension, desafios).
