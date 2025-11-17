# Python (10.º Ano) - 01 · Introdução, Variáveis, Tipos, Strings e I/O

> **Objetivo deste ficheiro**  
> Dar-te uma base sólida em Python: o que é programar, como declarar variáveis, conhecer os tipos de dados mais usados, trabalhar com texto (strings) e comunicar com o utilizador usando `print()` e `input()`.

---

## Índice

-   [0. Como usar este ficheiro](#0-como-usar-este-ficheiro)
-   [1. O que é programar?](#1-o-que-%C3%A9-programar)
-   [2. Primeiro contacto com Python](#2-primeiro-contacto-com-python)
-   [3. Variáveis](#3-vari%C3%A1veis)
-   [4. Tipos de dados básicos](#4-tipos-de-dados-b%C3%A1sicos)
-   [5. Strings (texto)](#5-strings-texto)
-   [6. Comentários](#6-coment%C3%A1rios)
-   [7. Entrada e saída: `print()` e `input()`](#7-entrada-e-sa%C3%ADda-print-e-input)
-   [8. Exercícios (Introdução, Variáveis, Tipos, Strings, I/O)](#8-exerc%C3%ADcios-introdu%C3%A7%C3%A3o-vari%C3%A1veis-tipos-strings-io)
-   [9. Changelog](#9-changelog)

---

## 0. Como usar este ficheiro

1. Lê a explicação teórica com calma.
2. Analisa os exemplos de código - tenta prever o resultado **antes** de o correr.
3. Reproduz os exemplos no teu editor / IDE.
4. No fim, resolve os **exercícios** (10–12). Começa pelos mais fáceis e sobe a dificuldade.

Se tiveres dúvidas, anota-as e fala com o professor.

---

## 1. O que é programar?

Programar é dar **instruções muito precisas** ao computador para ele resolver um problema.

-   Em vez de fazeres as contas à mão, dizes ao computador exatamente:
    -   que dados vai ler (entrada),
    -   o que deve fazer com esses dados (processamento),
    -   e o que deve mostrar no ecrã (saída).

Python é uma linguagem de programação **muito usada no mundo real** (web, ciência de dados, inteligência artificial, automação, etc.) e também é muito boa para aprender a programar pela primeira vez.

---

## 2. Primeiro contacto com Python

Há duas formas principais de experimentar Python:

1. **REPL / Consola interativa**  
   Escreves um comando, carregas em Enter e vês logo o resultado.  
   Exemplo na consola de Python:

    ```python
    >>> 2 + 3
    5
    >>> "Olá" * 3
    'OláOláOlá'
    ```

2. **Ficheiros `.py` (scripts)**  
   Guardas o teu código num ficheiro, por exemplo `exemplo.py`, e depois corres esse ficheiro.  
   Vantagem: consegues programas mais longos, organizados e fáceis de guardar.

Neste módulo vamos pensar em ficheiros `.py`, mas todos os exemplos também funcionam na consola interativa.

---

## 3. Variáveis

### 3.1. O que é uma variável?

Uma variável é como **uma etiqueta colada numa caixa** onde guardas um valor.

-   A etiqueta é o **nome da variável**.
-   O conteúdo da caixa é o **valor** (número, texto, etc.).
-   Em Python, o tipo de valor é **inferido automaticamente** (tipagem dinâmica).

Exemplo:

```python
idade = 16            # idade é uma "etiqueta" para o valor inteiro 16
altura = 1.72         # float (número decimal)
nome = "Ana"          # string (texto)
aprovado = True       # booleano (True/False)
```

### 3.2. Nomes de variáveis (convenções)

-   Usar **snake_case**: palavras em minúsculas separadas por `_`  
    → `media_turma`, `numero_alunos`, `nota_final`
-   Não começar com número nem usar espaços:
    -   ✅ `idade_aluno`
    -   ❌ `1idade`, `idade aluno`
-   Evitar nomes como `a`, `b`, `x` em programas reais.  
    É melhor usar nomes que **expliquem o significado**.

### 3.3. Reatribuição (mudar o valor)

A mesma variável pode guardar valores de tipos diferentes ao longo do programa (não é boa prática abusar, mas é possível).

```python
idade = 16
print(idade)          # 16

idade = "dezasseis"   # agora idade guarda uma string
print(idade)          # "dezasseis"
```

Em programas maiores é preferível manter o tipo de cada variável consistente (não misturar demasiado).

---

## 4. Tipos de dados básicos

Python tem vários tipos de dados. Os mais importantes nesta fase:

| Tipo       | Nome           | Exemplo          |
| ---------- | -------------- | ---------------- |
| `int`      | Inteiro        | `10`, `-3`, `0`  |
| `float`    | Decimal        | `3.14`, `-0.5`   |
| `str`      | String (texto) | `"Olá"`, `"123"` |
| `bool`     | Booleano       | `True`, `False`  |
| `NoneType` | Valor “nenhum” | `None`           |

### 4.1. Ver o tipo de um valor

A função `type()` devolve o tipo de um valor ou variável.

```python
numero = 10
texto = "Python"
verdadeiro = True

print(type(numero))     # <class 'int'>
print(type(texto))      # <class 'str'>
print(type(verdadeiro)) # <class 'bool'>
```

### 4.2. Conversões de tipo (casting)

Às vezes é preciso converter entre tipos:

```python
# De string para int/float
idade_str = "16"
idade_int = int(idade_str)         # 16 (int)

altura_str = "1.75"
altura_float = float(altura_str)   # 1.75 (float)

# De número para string
num = 123
num_str = str(num)                 # "123"

# Para booleano (bool)
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False (string vazia)
print(bool("x"))     # True (string não vazia)
```

**Regra importante:**  
`input()` devolve SEMPRE uma `str`.  
Se quiseres trabalhar com números, tens quase sempre de converter.

---

## 5. Strings (texto)

Uma **string** é uma sequência de caracteres: letras, números, espaços, símbolos.

```python
frase = "Olá, Mundo"
palavra = 'Python'   # aspas simples ou duplas funcionam
```

### 5.1. Indexação (aceder a um carácter)

Os caracteres são numerados a partir de **0**.

```python
texto = "Python"

primeiro = texto[0]   # "P"
segundo  = texto[1]   # "y"
ultimo   = texto[-1]  # "n" (índice negativo conta a partir do fim)

print(primeiro, segundo, ultimo)
```

Se tentares aceder a um índice que não existe, dá erro (`IndexError`).

### 5.2. Slicing (fatiar strings)

Podes tirar “fatias” da string: `texto[inicio:fim]` (fim não incluído).

```python
s = "Programação"

fatia1 = s[0:7]    # "Program"
fatia2 = s[2:7]    # "ogram"
fatia3 = s[4:]     # do índice 4 até ao fim -> "ramação"
fatia4 = s[:4]     # do início até ao índice 3 -> "Prog"
invertida = s[::-1]  # string invertida

print(fatia1)
print(invertida)
```

### 5.3. Strings são imutáveis

Não podes alterar um carácter diretamente:

```python
nome = "Ana"
# nome[0] = "J"   # ERRO! (TypeError)

# Em vez disso, crias uma nova string:
novo_nome = "J" + nome[1:]   # "Jna"
```

Sempre que “alteras” uma string, na verdade estás a criar uma nova.

### 5.4. Métodos úteis de strings

Alguns métodos muito usados:

```python
s = "  Olá, Mundo  "

s_strip   = s.strip()           # remove espaços no início e fim
s_lower   = s_strip.lower()     # "olá, mundo"
s_upper   = s_strip.upper()     # "OLÁ, MUNDO"
tem_mundo = "Mundo" in s        # True (operador in)

frase = "um dois três"
palavras = frase.split()        # ["um", "dois", "três"]

juntas = "-".join(["a", "b", "c"])  # "a-b-c"

print(len(s))        # comprimento da string (inclui espaços)
print(len(s_strip))  # comprimento sem espaços das pontas
```

Lista de métodos a conhecer nesta fase (não decora tudo, mas sabe o que fazem em geral):

-   `strip()`, `lstrip()`, `rstrip()`
-   `lower()`, `upper()`, `capitalize()`
-   `replace(antigo, novo)`
-   `split(separador)`
-   `join(lista_de_strings)`
-   `startswith(...)`, `endswith(...)`

---

## 6. Comentários

Comentários servem para **explicar o código**, tanto para ti como para outras pessoas (e para o “tu do futuro”).

-   Em Python, um comentário de linha começa com `#`.
-   Tudo o que está depois do `#` na linha é ignorado pelo interpretador.

```python
# Este programa imprime uma saudação simples
nome = "Ana"               # guarda o nome da pessoa
print("Olá,", nome)        # mostra "Olá, Ana"
```

Mais tarde vamos ver **docstrings**, que são “comentários especiais” usados para documentar funções e módulos.

---

## 7. Entrada e saída: `print()` e `input()`

### 7.1. `print()` - mostrar informação

A função `print()` escreve texto no ecrã.

```python
curso = "PI 10.º"
ano = 2025

print("Bem-vindo ao curso de", curso)
print("Ano letivo:", ano)
```

Podes juntar valores com vírgulas (Python coloca um espaço entre eles por defeito) ou usar **f-strings** (ver abaixo).

### 7.2. `input()` - ler informação

A função `input()` mostra uma mensagem (opcional) e **lê uma linha de texto** escrita pelo utilizador.  
O resultado é sempre uma `str`.

```python
nome = input("Como te chamas? ")      # lê texto
idade_txt = input("Idade? ")          # ainda é string!

print("Tipo de idade_txt:", type(idade_txt))   # <class 'str'>
```

Se quiseres trabalhar com a idade como número (para somar, comparar, etc.), tens de converter:

```python
idade = int(idade_txt)        # converte string para inteiro
print("Daqui a 5 anos terás", idade + 5, "anos.")
```

Também podes converter logo dentro do `input()`:

```python
idade = int(input("Idade? "))
altura = float(input("Altura em metros? "))

print("Tipo de idade:", type(idade))   # int
print("Tipo de altura:", type(altura)) # float
```

### 7.3. f-strings (interpolação e formatação)

As **f-strings** facilitam a construção de frases com variáveis lá dentro.

-   Escreves uma string que começa com `f` ou `F`.
-   Dentro das `{}` colocas o nome da variável ou uma expressão.

```python
nome = "Beatriz"
nota = 17.375

mensagem = f"Aluno: {nome} | Nota: {nota:.2f}"
print(mensagem)  # "Aluno: Beatriz | Nota: 17.38"
```

Na expressão `{nota:.2f}`:

-   `:.2f` significa “formata como número decimal com 2 casas”.

Mais exemplos:

```python
x = 5
y = 3

print(f"{x} + {y} = {x + y}")      # "5 + 3 = 8"

preco = 12.5
print(f"Preço: {preco:.1f} €")     # "Preço: 12.5 €"

nome = "ana"
print(f"Nome formatado: {nome.capitalize()}")
```

---

## 8. Exercícios (Introdução, Variáveis, Tipos, Strings, I/O)

> Sugestão: copia cada exercício para um ficheiro `.py` e resolve-o.  
> Tenta primeiro **sem olhar para a solução**. Só depois compara com a correção.

### Exercício 1 - Dados básicos do aluno

Cria um programa que:

1. Guarda em variáveis o teu `nome`, `idade` e `curso` (em texto).
2. Mostra uma mensagem do tipo:

    ```
    Olá, eu sou a/o <nome>, tenho <idade> anos e estou no curso <curso>.
    ```

Podes usar `print()` normal ou uma f-string.

> Resolução:

```python
nome = "Teu Nome"
idade = 16
curso = "PI 10.º"
print(f"Olá, eu sou a/o {nome}, tenho {idade} anos e estou no curso {curso}.")
```

---

### Exercício 2 - Tipos de dados

Escreve um programa que:

1. Cria as seguintes variáveis:

    ```python
    idade = 16
    altura = 1.70
    nome = "João"
    aprovado = False
    ```

2. Usa `type()` para imprimir o tipo de cada variável.
3. No final, escreve uma frase:

    ```text
    A variável idade é do tipo ...
    ```

(Completa com o tipo correto em texto.)

> Resolução:

```python
idade = 16
altura = 1.70
nome = "João"
aprovado = False

print(f"A variável idade é do tipo {type(idade)}")
print(f"A variável altura é do tipo {type(altura)}")
print(f"A variável nome é do tipo {type(nome)}")
print(f"A variável aprovado é do tipo {type(aprovado)}")
```

---

### Exercício 3 - Conversão de input

Escreve um programa que:

1.  Pede ao utilizador a sua idade (com `input()`).
2.  Converte essa idade para `int`.
3.  Calcula a idade que a pessoa terá daqui a 10 anos.
4.  Mostra uma frase usando uma f-string, por exemplo:

        ```
        Daqui a 10 anos terás 25 anos.
        ```

    > Resolução:

```python
idade_str = input("Qual é a tua idade? ")
idade = int(idade_str)
idade_futura = idade + 10
print(f"Daqui a 10 anos terás {idade_futura} anos.")
```

---

### Exercício 4 - Comprimento de uma palavra

Cria um programa que:

1. Pede ao utilizador uma palavra.
2. Mostra o primeiro e o último carácter da palavra.
3. Mostra quantos caracteres tem a palavra usando `len()`.

> Resolução:

```python
palavra = input("Escreve uma palavra: ")
print("Primeiro carácter:", palavra[0])
print("Último carácter:", palavra[-1])
print("Número de caracteres:", len(palavra))
```

---

### Exercício 5 - Maiúsculas e minúsculas

Escreve um programa que:

1. Pede uma frase ao utilizador.
2. Mostra a frase:
    - toda em maiúsculas,
    - toda em minúsculas,
    - com apenas a primeira letra em maiúscula (`capitalize()`).

> Resolução:

```python
frase = input("Escreve uma frase: ")
print("Maiúsculas:", frase.upper())
print("Minúsculas:", frase.lower())
print("Capitalizada:", frase.capitalize())
```

---

### Exercício 6 - Limpar espaços

Cria um programa que:

1. Pede ao utilizador que escreva uma frase, mas **propositadamente** com espaços a mais no início e no fim.
2. Mostra:
    - o comprimento da frase original (`len()`),
    - a frase sem espaços nas pontas (`strip()`),
    - o comprimento da frase depois de `strip()`.

> Resolução:

```python
frase = input("Escreve uma frase com espaços no início e no fim: ")
print("Comprimento original:", len(frase))
frase_limpa = frase.strip()
print("Frase sem espaços:", frase_limpa)
print("Comprimento sem espaços:", len(frase_limpa))
```

---

### Exercício 7 - Procurar letra na palavra

Escreve um programa que:

1. Pede uma palavra ao utilizador.
2. Pede uma letra ao utilizador.
3. Diz se a letra aparece ou não na palavra, usando o operador `in`.

Exemplo de saída:

```text
A letra "a" existe na palavra "banana".
```

ou

```text
A letra "x" não existe na palavra "banana".
```

> Resolução:

```python
palavra = input("Escreve uma palavra: ")
letra = input("Escreve uma letra: ")
existe = letra in palavra
print(f'A letra "{letra}" {"existe" if existe else "não existe"} na palavra "{palavra}".')
```

---

### Exercício 8 - Conversão de temperatura

Cria um programa que:

1. Pede ao utilizador uma temperatura em graus Celsius (pode ser decimal).
2. Converte esse valor para `float`.
3. Converte para Fahrenheit usando a fórmula:

    \[
    F = C imes 9/5 + 32
    \]

4. Mostra uma mensagem com **2 casas decimais** na temperatura em Fahrenheit.

> Resolução:

```python
celsius_str = input("Temperatura em Celsius: ")
celsius = float(celsius_str)
fahrenheit = celsius * 9/5 + 32
print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")
```

---

### Exercício 9 - Valores “vazios” e `bool()`

Escreve um programa que:

1. Cria as seguintes variáveis:

    ```python
    a = 0
    b = ""
    c = []
    d = "Python"
    e = 123
    ```

2. Usa `bool()` em cada uma e imprime o resultado, por exemplo:

    ```text
    bool(a) -> False
    ```

3. No final, escreve um pequeno comentário (em texto, num `print` ou em comentário) a explicar que valores são considerados `False` em Python.

> Resolução:

```python
a = 0
b = ""
c = []
d = "Python"
e = 123
print(f"bool(a) -> {bool(a)}")
print(f"bool(b) -> {bool(b)}")
print(f"bool(c) -> {bool(c)}")
print(f"bool(d) -> {bool(d)}")
print(f"bool(e) -> {bool(e)}")
# Em Python, valores como 0, string vazia "", lista vazia [], None são  considerados False.
```

---

### Exercício 10 - Questionário simples

Cria um pequeno “questionário” em que o programa pergunta ao utilizador:

-   nome,
-   cidade onde vive,
-   linguagem de programação favorita.

Depois, mostra uma frase organizada, usando uma f-string, por exemplo:

```text
Olá, eu sou a/o <nome>, vivo em <cidade> e a minha linguagem favorita é <linguagem>.
```

> Resolução:

```python
nome = input("Qual é o teu nome? ")
cidade = input("Onde vives? ")
linguagem = input("Qual é a tua linguagem de programação favorita? ")
print(f"Olá, eu sou a/o {nome}, vivo em {cidade} e a minha linguagem favorita é {linguagem}.")
```

---

### Exercício 11 (Desafio) - Formatar um “cartão de aluno”

Cria um programa que:

1. Pede ao utilizador:
    - nome,
    - idade,
    - turma,
    - média (em float).
2. Usa f-strings para mostrar algo do género:

    ```text
    =========================
        CARTÃO DE ALUNO
    =========================
    Nome : Ana Silva
    Idade: 16 anos
    Turma: 10.º PI
    Média: 15.75 valores
    =========================
    ```

Podes usar `
` para quebras de linha e, se quiseres, formatação com casas decimais na média (`{media:.2f}`).

> Resolução:

```python
nome = input("Nome: ")
idade = int(input("Idade: "))
turma = input("Turma: ")
media = float(input("Média: "))
print(f"""=========================
    CARTÃO DE ALUNO
=========================
Nome : {nome}
Idade: {idade} anos
Turma: {turma}
Média: {media:.2f} valores
=========================""")
```

---

## 9. Changelog

> Registo de alterações importantes a este ficheiro.

-   **2025-11-17 · v1.2**
    -   Adicionadas soluções aos exercícios todos.
-   **2025-11-17 · v1.1**
    -   TOC atualizado.
-   **2025-11-17 · v1.0**
    -   Criação inicial do documento.
    -   Secções: introdução, variáveis, tipos básicos, strings, comentários, `print()`/`input()` e f-strings.
    -   Adicionados 12 exercícios graduais (nível: 10.º ano, primeira unidade de Python).
