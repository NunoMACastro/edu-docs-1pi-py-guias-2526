# Python (10.º Ano) - 00 · Exercicios de recuperação

> **Objetivo deste ficheiro**  
> Preparar os alunos para a recuperação, através de exercícios que envolvem os conceitos básicos de Python.

Usa um IDE para escrever os teus programas.

Podes usar o [OnlineGDB](https://www.onlinegdb.com/online_python_compiler) inicialmente uma vez que é muito simples de usar.

# Exercícios Básicos

Exercícios sobre variáveis, tipos de dados, operações aritméticas e entrada e saída de dados.

## Exercício 1

Cria um programa que:

1. Guarda em variáveis o teu `nome`, `idade` e `curso` (em texto).
2. Mostra uma mensagem do tipo:

    ```
    Olá, eu sou a/o <nome>, tenho <idade> anos e estou no curso <curso>.
    ```

> Resolução:

```python
nome = "Maria"
idade = 16
curso = "10.º Ano"

print(f"Olá, eu sou a/o {nome}, tenho {idade} anos e estou no curso {curso}.")
```

## Exercício 2

Cria um programa que:

1.  Guarda em variáveis o `preço` de um produto e a `quantidade` que queres comprar (em números).
2.  Calcula o `total` a pagar, multiplicando o preço pela quantidade.
3.  Mostra uma mensagem do tipo:

        ```
        O total a pagar é: <total>.
        ```

> Resolução:

```python
preco = 12.5
quantidade = 4
total = preco * quantidade

print(f"O total a pagar é: {total}.")
```

## Exercício 3

Cria um programa que:

1. Pede ao utilizador para introduzir dois números (usa a função `input()` e converte os valores para números usando `int()` ou `float()`).
2. Calcula a `soma`, a `subtração`, a `multiplicação` e a `divisão` desses dois números.
3. Mostra os resultados de cada operação em mensagens do tipo:

    ```
    A soma é: <soma>.
    A subtração é: <subtração>.
    A multiplicação é: <multiplicação>.
    A divisão é: <divisão>.
    ```

> Resolução:

```python
numero1 = float(input("Introduz o primeiro número: "))
numero2 = float(input("Introduz o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f"A soma é: {soma}.")
print(f"A subtração é: {subtracao}.")
print(f"A multiplicação é: {multiplicacao}.")
print(f"A divisão é: {divisao}.")
```

## Exercício 4

Cria um programa que:

1. Peça ao utilizador para introduzir a altura e largura de um retângulo (em números).
2. Calcula a área do retângulo (altura x largura)
3. Mostra uma mensagem do tipo:

    ```
    A área do retângulo é: <área>.
    ```

> Resolução:

```python
altura = float(input("Introduz a altura do retângulo: "))
largura = float(input("Introduz a largura do retângulo: "))

area = altura * largura

print(f"A área do retângulo é: {area}.")
```

## Exercício 5

Cria um programa que:

1. Peça ao utilizador para introduzir a temperatura em graus Celsius (em número).
2. Converte a temperatura para Fahrenheit usando a fórmula: `F = (C * 9/5) + 32`
3. Mostra uma mensagem do tipo:

    ```
    A temperatura em Celsius é: <C>°C.
    A temperatura em Fahrenheit é: <F>°F.
    ```

> Resolução:

```python
celsius = float(input("Introduz a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"A temperatura em Celsius é: {celsius}°C.")
print(f"A temperatura em Fahrenheit é: {fahrenheit}°F.")
```

## Exercício 6

Cria um programa que:

1. Peça ao utilizador para introduzir a sua morada (em texto).
2. Mostra uma mensagem do tipo:

    ```
    A tua morada é: <morada>.
    ```

> Resolução:

```python
morada = input("Introduz a tua morada: ")

print(f"A tua morada é: {morada}.")
```

## Exercício 7

Cria um programa que:

1. Peça ao utilizador para introduzir o seu nome e idade (em texto e número).
2. Mostra uma mensagem do tipo:

    ```
    Olá, <nome>! Tens <idade> anos.
    ```

> Resolução:

```python
nome = input("Introduz o teu nome: ")
idade = int(input("Introduz a tua idade: "))

print(f"Olá, {nome}! Tens {idade} anos.")
```

## Exercício 8

Cria um programa que:

1.  Peça ao utilizador para introduzir o raio de um círculo (em número).
2.  Calcula a área do círculo usando a fórmula: `A = π * r^2` (assume que o π = 3.14).
3.  Mostra uma mensagem do tipo:

        ```
        A área do círculo é: <área>.
        ```

> Resolução:

```python
raio = float(input("Introduz o raio do círculo: "))
pi = 3.14
area = pi * raio ** 2

print(f"A área do círculo é: {area}.")
```

## Exercício 9

Cria um programa que:

1.  Peça ao utilizador para introduzir a sua data de nascimento (em texto, formato: DD/MM/AAAA).
2.  Mostra uma mensagem do tipo:

        ```
        A tua data de nascimento é: <data>.
        ```

> Resolução:

```python
data_nascimento = input("Introduz a tua data de nascimento (DD/MM/AAAA): ")

print(f"A tua data de nascimento é: {data_nascimento}.")
```

# Exercícios Intermédios

Exercícios que envolvem estruturas de repetição, de controlo, funções, listas e dicionários.

## Exercício 10

Cria um programa que:

1. Peça ao utilizador para introduzir um número.
2. Verifica se o número é positivo, negativo ou zero e mostra uma mensagem do tipo:

    ```
    O número <n> é positivo.
    ```

    ou

    ```
    O número <n> é negativo.
    ```

    ou

    ```
    O número <n> é zero.
    ```

> Resolução:

```python
n = float(input("Introduz um número: "))

if n > 0:
    print(f"O número {n} é positivo.")
elif n < 0:
    print(f"O número {n} é negativo.")
else:
    print(f"O número {n} é zero.")
```

## Exercício 11

Cria um programa que:

1. Peça ao utilizador para introduzir um número inteiro.
2. Verifica se o número é par ou ímpar e mostra uma mensagem do tipo:

    ```
    O número <n> é par.
    ```

    ou

    ```
    O número <n> é ímpar.
    ```

> Nota: um número é par se o resto da divisão por 2 for igual a 0, ou seja, `n % 2 == 0`. Neste caso `if n % 2 == 0:` é a condição para verificar se o número é par.

> Resolução:

```python
n = int(input("Introduz um número inteiro: "))

if n % 2 == 0:
    print(f"O número {n} é par.")
else:
    print(f"O número {n} é ímpar.")
```

## Exercício 12

Cria um programa que:

1. Peça um nome ao utilizador e diga se o nome tem mais de 5 letras ou não, mostrando uma mensagem do tipo:

    ```
    O nome <nome> tem mais de 5 letras.
    ```

    ou

    ```
    O nome <nome> tem 5 ou menos letras.
    ```

> Nota: para verificar o número de letras de um nome, podes usar a função `len(nome)`, que retorna o comprimento da string.

> Resolução:

```python
nome = input("Introduz um nome: ")

if len(nome) > 5:
    print(f"O nome {nome} tem mais de 5 letras.")
else:
    print(f"O nome {nome} tem 5 ou menos letras.")
```

## Exercício 13

Cria um programa que:

1. Peça ao utilizador para introduzir dois números inteiros.
2. Diga se algum dos números é maior do que o outro, ou se são iguais, mostrando uma mensagem do tipo:

    ```
    O número <n1> é maior do que <n2>.
    ```

    ou

    ```
    O número <n2> é maior do que <n1>.
    ```

    ou

    ```
    Os números <n1> e <n2> são iguais.
    ```

> Resolução:

```python
n1 = int(input("Introduz o primeiro número inteiro: "))
n2 = int(input("Introduz o segundo número inteiro: "))

if n1 > n2:
    print(f"O número {n1} é maior do que {n2}.")
elif n2 > n1:
    print(f"O número {n2} é maior do que {n1}.")
else:
    print(f"Os números {n1} e {n2} são iguais.")
```

## Exercício 14

Cria um programa que:

1. Peça ao utilizador para introduzir a idade.
2. O programa deve verificar se a idade está entre 0 e 100 (inclusive).
3. Se não estiver, deve mostrar uma mensagem do tipo:

    ```
    A idade <n> não está entre 0 e 100.
    ```

4. Se estiver, deve depois verificar se a idade é menor do que 18, entre 18 e 65 (inclusive) ou maior do que 65, mostrando uma mensagem do tipo:

    ```
    A idade <n> é menor do que 18. Ainda és jovem!
    ```

    ou

    ```
    A idade <n> está entre 18 e 65. És adulto!
    ```

    ou

    ```
    A idade <n> é maior do que 65. Já és idoso!
    ```

> Resolução:

```python
idade = int(input("Introduz a idade: "))

if idade < 0 or idade > 100:
    print(f"A idade {idade} não está entre 0 e 100.")
else:
    if idade < 18:
        print(f"A idade {idade} é menor do que 18. Ainda és jovem!")
    elif idade <= 65:
        print(f"A idade {idade} está entre 18 e 65. És adulto!")
    else:
        print(f"A idade {idade} é maior do que 65. Já és idoso!")
```

# Exercício 15

Cria um programa que:

1. Peça ao utilizador para introduzir uma temperatura em graus Celsius.
2. O programa deve verificar se a temperatura é menor do que 0, entre 0 e 30 (inclusive) ou maior do que 30, mostrando uma mensagem do tipo:

    ```
    A temperatura <n>°C é menor do que 0. Está muito frio!
    ```

    ou

    ```
    A temperatura <n>°C está entre 0 e 30. O tempo está agradável!
    ```

    ou

    ```
    A temperatura <n>°C é maior do que 30. Está muito quente!
    ```

> Resolução:

```python
temperatura = float(input("Introduz a temperatura em graus Celsius: "))

if temperatura < 0:
    print(f"A temperatura {temperatura}°C é menor do que 0. Está muito frio!")
elif temperatura <= 30:
    print(f"A temperatura {temperatura}°C está entre 0 e 30. O tempo está agradável!")
else:
    print(f"A temperatura {temperatura}°C é maior do que 30. Está muito quente!")
```

## Exercício 16

Cria um programa que:

1. Peça ao utilizador para introduzir um número inteiro.
2. O programa deve verificar se o número é múltiplo de 3 ou de 5, mostrando uma mensagem do tipo:

    ```
    O número <n> é múltiplo de 3 e de 5.
    ```

    ou

    ```
    O número <n> é múltiplo de 3.
    ```

    ou

    ```
    O número <n> é múltiplo de 5.
    ```

    ou

    ```
    O número <n> não é múltiplo de 3 nem de 5.
    ```

> Para verificar se um número é múltiplo de 3, podes usar a condição `n % 3 == 0`, que verifica se o resto da divisão por 3 é igual a 0.

> Resolução:

```python
n = int(input("Introduz um número inteiro: "))

if n % 3 == 0 and n % 5 == 0:
    print(f"O número {n} é múltiplo de 3 e de 5.")
elif n % 3 == 0:
    print(f"O número {n} é múltiplo de 3.")
elif n % 5 == 0:
    print(f"O número {n} é múltiplo de 5.")
else:
    print(f"O número {n} não é múltiplo de 3 nem de 5.")
```

## Exercício 17

Cria um programa que:

1. Peça ao utilizador para introduzir um número inteiro e positivo.
2. O programa deve fazer uma contagem decrescente desde o número introduzido até 0, mostrando cada número numa linha.

> Resolução:

```python
n = int(input("Introduz um número inteiro e positivo: "))

if n < 0:
    print("O número tem de ser positivo.")
else:
    for i in range(n, -1, -1):
        print(i)
```

## Exercício 18

Cria um programa que:

1. Peça ao utilizador para introduzir um número inteiro e positivo.
2. Usando um `for` ou um `while`, o programa deve mostrar a tabuada do número introduzido, ou seja, os resultados da multiplicação do número por 1, 2, 3, ..., 10.

> Resolução:

```python
n = int(input("Introduz um número inteiro e positivo: "))

if n < 0:
    print("O número tem de ser positivo.")
else:
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
```

## Exercício 19

Cria um programa que:

1. Peça ao utilizador para introduzir um número inteiro e positivo.
2. Usando um `for` ou um `while`, o programa deve mostrar os números pares desde 0 até ao número introduzido (inclusive, se for par).

> Resolução:

```python
n = int(input("Introduz um número inteiro e positivo: "))

if n < 0:
    print("O número tem de ser positivo.")
else:
    for i in range(0, n + 1):
        if i % 2 == 0:
            print(i)
```

## Exercício 20

Cria um programa que:

1. Peça o nome do utilizador e o coloque numa variável.
2. Depois, usando o `for`ou o `while`, deve dizer quantas vezes a letra `a` aparece no nome.

## Exercício 21

Cria um programa que:

1. Peça ao utilizador 10 números inteiros e positivos, um de cada vez, e guarde-os numa lista.
2. Depois, usando um `for` ou um `while`, o programa deve mostrar todos os números introduzidos, um de cada vez, e dizer se são pares ou ímpares.

## Exercício 22

Cria um programa que:

1. Peça ao utilizador 5 palavras, uma de cada vez, e guarde-as numa lista.
2. Depois, usando um `for` ou um `while`, o programa deve mostrar todas as palavras introduzidas, uma de cada vez, e dizer quantas letras tem cada palavra.

## Exercício 23

Cria um programa que:

1. Considera a lista:

    ```python
    numeros = [1, 2, 3, 4, 5]
    ```

2. Usando um `for` ou um `while`, o programa deve mostrar o quadrado de cada número da lista, um de cada vez.

## Exercício 24

Cria um programa que:

1. Peça um numero ao utilizador
2. Calcule a tabuada desse número e guarde os resultados numa lista.
3. Mostre a lista com os resultados.
