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
nome = "João"
idade = 16
curso = "10.º Ano"
print(f"Olá, eu sou {nome}, tenho {idade} anos e estou no curso {curso}.")
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
preço = 9.99
quantidade = 3
total = preço * quantidade
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
num1 = float(input("Introduz o primeiro número: "))
num2 = float(input("Introduz o segundo número: "))

soma = num1 + num2
subtração = num1 - num2
multiplicação = num1 * num2
divisão = num1 / num2

print(f"A soma é: {soma}.")
print(f"A subtração é: {subtração}.")
print(f"A multiplicação é: {multiplicação}.")
print(f"A divisão é: {divisão}.")
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
área = altura * largura
print(f"A área do retângulo é: {área}.")
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

C = float(input("Introduz a temperatura em graus Celsius: "))
F = (C * 9/5) + 32
print(f"A temperatura em Celsius é: {C}°C.")
print(f"A temperatura em Fahrenheit é: {F}°F.")
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
π = 3.14
área = π * (raio ** 2)
print(f"A área do círculo é: {área}.")
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

idade = int(input("Introduz a tua idade: "))

if idade < 0 or idade > 100:
    print(f"A idade {idade} não está entre 0 e 100.")
elif idade < 18:
    print(f"A idade {idade} é menor do que 18. Ainda és jovem!")
elif idade <= 65:
    print(f"A idade {idade} está entre 18 e 65. És adulto!")
else:
    print(f"A idade {idade} é maior do que 65. Já és idoso!")
```

Ou com uma estrutura de controlo aninhada:

```python

idade = int(input("Introduz a tua idade: "))

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
    print("O número deve ser positivo.")
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
    print("O número deve ser positivo.")
else:
    for i in range(1, 11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")
```

## Exercício 19

Cria um programa que:

1. Peça ao utilizador para introduzir um número inteiro e positivo.
2. Usando um `for` ou um `while`, o programa deve mostrar os números pares desde 0 até ao número introduzido (inclusive, se for par).

> Resolução:

```python
n = int(input("Introduz um número inteiro e positivo: "))

if n < 0:
    print("O número deve ser positivo.")
else:
    for i in range(0, n + 1, 2):
        print(i)
```

## Exercício 20

Cria um programa que:

1. Peça o nome do utilizador e o coloque numa variável.
2. Depois, usando o `for`ou o `while`, deve dizer quantas vezes a letra `a` aparece no nome.

> Resolução:

```python
nome = input("Introduz o teu nome: ")
contador_a = 0
for letra in nome:
    if letra.lower() == 'a': # o método lower() é usado para garantir que a comparação seja feita de forma case-insensitive, ou seja, tanto 'a' como 'A' serão contados.
        contador_a += 1

print(f"A letra 'a' aparece {contador_a} vezes no nome {nome}.")
```

## Exercício 21

Cria um programa que:

1. Peça ao utilizador 10 números inteiros e positivos, um de cada vez, e guarde-os numa lista.
2. Depois, usando um `for` ou um `while`, o programa deve mostrar todos os números introduzidos, um de cada vez, e dizer se são pares ou ímpares.

> Resolução:

```python

numeros = []
for i in range(10):
    n = int(input(f"Introduz o número {i + 1}: "))
    if n < 0:
        print("O número deve ser positivo.")
    else:
        numeros.append(n)

for n in numeros:
    if n % 2 == 0:
        print(f"O número {n} é par.")
    else:
        print(f"O número {n} é ímpar.")
```

## Exercício 22

Cria um programa que:

1. Peça ao utilizador 5 palavras, uma de cada vez, e guarde-as numa lista.
2. Depois, usando um `for` ou um `while`, o programa deve mostrar todas as palavras introduzidas, uma de cada vez, e dizer quantas letras tem cada palavra.

> Resolução:

```python

palavras = []

for i in range(5):
    palavra = input(f"Introduz a palavra {i + 1}: ")
    palavras.append(palavra)

for palavra in palavras:
    comprimento = len(palavra)
    print(f"A palavra '{palavra}' tem {comprimento} letras.")
```

## Exercício 23

Cria um programa que:

1. Considera a lista:

    ```python
    numeros = [1, 2, 3, 4, 5]
    ```

2. Usando um `for` ou um `while`, o programa deve mostrar o quadrado de cada número da lista, um de cada vez.

> Resolução:

```python
numeros = [1, 2, 3, 4, 5]

for n in numeros:
    quadrado = n ** 2
    print(f"O quadrado de {n} é {quadrado}.")
```

## Exercício 24

Cria um programa que:

1. Peça um numero ao utilizador
2. Calcule a tabuada desse número e guarde os resultados numa lista.
3. Mostre a lista com os resultados.

> Resolução:

```python
n = int(input("Introduz um número inteiro: "))
tabuada = []
for i in range(1, 11):
    resultado = n * i
    tabuada.append(resultado)

print(f"A tabuada de {n} é: {tabuada}.")
```

## Exercício 25

Cria um programa que:

1. Peça ao utilizador para introduzir um número inteiro e positivo.
2. Peça esse número de palavras ao utilizador, uma de cada vez, e guarde-as numa lista.
3. Depois, usando um `for` ou um `while`, o programa deve mostrar todas as palavras introduzidas, uma de cada vez, e dizer se a palavra tem mais de 5 letras ou não.

> Resolução:

```python
n = int(input("Introduz um número inteiro e positivo: "))
if n < 0:
    print("O número deve ser positivo.")
else:
    palavras = []
    for i in range(n):
        palavra = input(f"Introduz a palavra {i + 1}: ")
        palavras.append(palavra)
    for palavra in palavras:
        if len(palavra) > 5:
            print(f"A palavra '{palavra}' tem mais de 5 letras.")
        else:
            print(f"A palavra '{palavra}' tem 5 ou menos letras.")
```

## Exercício 26

Cria um programa que:

1. Peça uma letra ao utilizador.
2. Usando a lista do exercício anterior, deve mostrar todas as palavras que começam com a letra introduzida, uma de cada vez.

> Resolução:

```python

letra = input("Introduz uma letra: ").lower() # converte a letra para minúscula para garantir que a comparação seja case-insensitive.
palavras_com_letra = []

for palavra in palavras:
    if palavra.lower().startswith(letra):
        palavras_com_letra.append(palavra) # o método startswith() é usado para verificar se a palavra começa com a letra introduzida.

if palavras_com_letra:
    print(f"As palavras que começam com a letra '{letra}' são:")
    for palavra in palavras_com_letra:
        print(palavra)
else:
    print(f"Não há palavras que começam com a letra '{letra}'.")
```

## Exercício 27

Cria um programa que:

1. Tenha um dicionário com o teu nome, idade e cidade.
2. Mostre uma mensagem do tipo:

    ```
    O meu nome é <nome>, tenho <idade> anos e vivo em <cidade>.
    ```

> Resolução:

```python
pessoa = {
    "nome": "Maria",
    "idade": 16,
    "cidade": "Lisboa"
}

print(f"O meu nome é {pessoa['nome']}, tenho {pessoa['idade']} anos e vivo em {pessoa['cidade']}.")
```

## Exercício 28

Cria um programa que:

1. Pede um nome, uma idade e uma cidade ao utilizador e guarde-os num dicionário.
2. Mostre uma mensagem do tipo:

    ```
    Foi inserido o nome <nome>, a idade <idade> e a cidade <cidade> no dicionário.
    ```

> Resolução:

```python
pessoa = {}
pessoa["nome"] = input("Introduz o teu nome: ")
pessoa["idade"] = int(input("Introduz a tua idade: "))
pessoa["cidade"] = input("Introduz a tua cidade: ")

print(f"Foi inserido o nome {pessoa['nome']}, a idade {pessoa['idade']} e a cidade {pessoa['cidade']} no dicionário.")
```

## Exercício 29

Cria um programa que:

1. Peça 10 números inteiros e positivos ao utilizador, um de cada vez, e guarde-os numa lista.
2. O programa deve verificar, antes de inserir na lista, se o número é positivo e se já não foi introduzido anteriormente. Se o número for negativo ou já tiver sido introduzido, deve mostrar uma mensagem e pedir novo número, até que sejam introduzidos 10 números válidos. A mensagem a mostrar em caso de número inválido deve ser do tipo:

    ```
    O número <n> é inválido. Introduz um número inteiro e positivo que ainda não tenhas introduzido.
    ```

3. Depois, o programa deve dizer o valor máximo, mínimo e a média dos números introduzidos, mostrando mensagens do tipo:

    ```
    O número máximo é: <max>.
    O número mínimo é: <min>.
    A média dos números é: <média>.
    ```

> Resolução:

```python
numeros = []

while len(numeros) < 10:
    n = int(input(f"Introduz o número {len(numeros) + 1}: "))
    if n < 0 or n in numeros:
        print(f"O número {n} é inválido. Introduz um número inteiro e positivo que ainda não tenhas introduzido.")
    else:
        numeros.append(n)

maximo = max(numeros)
minimo = min(numeros)
media = sum(numeros) / len(numeros)

print(f"O número máximo é: {maximo}.")
print(f"O número mínimo é: {minimo}.")
print(f"A média dos números é: {media}.")
```

## Exercício 30

Cria um programa que:

1. Tenha um dicionário com o teu nome, idade e curso, por exemplo:

    ```python
    pessoa = {
        "nome": "Maria",
        "idade": 16,
        "curso": "10.º Ano"
    }
    ```

2. Mostre uma mensagem do tipo:

    ```
    Olá, eu sou a/o <nome>, tenho <idade> anos e estou no curso <curso>.
    ```

3. Peça ao utilizador qual a sua cidade e adicione essa informação ao dicionário, com a chave "cidade".
4. Mostre uma mensagem do tipo:

    ```
    A minha cidade é: <cidade>.
    ```

> Resolução:

```python

pessoa = {
    "nome": "Maria",
    "idade": 16,
    "curso": "10.º Ano"
}

print(f"Olá, eu sou {pessoa['nome']}, tenho {pessoa['idade']} anos e estou no curso {pessoa['curso']}.")
cidade = input("Introduz a tua cidade: ")
pessoa["cidade"] = cidade
print(f"A minha cidade é: {pessoa['cidade']}.")
```

## Exercício 31

Cria um programa que:

1. Tenha um dicionário com os nomes de 5 países e as suas respetivas capitais, por exemplo:

    ```python
    paises = {
        "Portugal": "Lisboa",
        "Espanha": "Madrid",
        "França": "Paris",
        "Itália": "Roma",
        "Alemanha": "Berlim"
    }
    ```

2. Peça ao utilizador para introduzir o nome de um país e mostre a sua capital, ou uma mensagem do tipo:

    ```
    A capital de <país> é: <capital>.
    ```

    Se o país não estiver no dicionário, deve mostrar uma mensagem do tipo:

    ```
    O país <país> não está no dicionário.
    ```

> Resolução:

```python
paises = {
    "Portugal": "Lisboa",
    "Espanha": "Madrid",
    "França": "Paris",
    "Itália": "Roma",
    "Alemanha": "Berlim"
}

pais = input("Introduz o nome de um país: ")

if pais in paises:
    print(f"A capital de {pais} é: {paises[pais]}.")
else:
    print(f"O país {pais} não está no dicionário.")
```

## Exercício 32

Cria um programa que:

1. Tenha um dicionário com os nomes de 5 frutas e as suas respetivas cores, por exemplo:

    ```python
    frutas = {
        "Maçã": "Vermelha",
        "Banana": "Amarela",
        "Laranja": "Laranja",
        "Uva": "Roxa",
        "Limão": "Verde"
    }
    ```

2. Peça ao utilizador para introduzir o nome de uma fruta e mostre a sua cor, ou uma mensagem do tipo:

    ```
    A cor da fruta <fruta> é: <cor>.
    ```

    Se a fruta não estiver no dicionário, deve mostrar uma mensagem do tipo:

    ```
    A fruta <fruta> não está no dicionário.
    ```

3. Peça ao utilizador para introduzir o nome de uma fruta e a sua cor, e adicione essa informação ao dicionário.

> Resolução:

```python

frutas = {
    "Maçã": "Vermelha",
    "Banana": "Amarela",
    "Laranja": "Laranja",
    "Uva": "Roxa",
    "Limão": "Verde"
}

fruta = input("Introduz o nome de uma fruta: ")
if fruta in frutas:
    print(f"A cor da fruta {fruta} é: {frutas[fruta]}.")
else:
    print(f"A fruta {fruta} não está no dicionário.")
    cor = input(f"Introduz a cor da fruta {fruta}: ")
    frutas[fruta] = cor
    print(f"A fruta {fruta} com a cor {cor} foi adicionada ao dicionário.")
```

## Exercício 33

Cria um programa que:

1. Peça ao utilizador para introduzir uma frase.
2. Crie um dicionário que guarde quantas vezes aparece cada palavra (ignora diferenças entre maiúsculas e minúsculas).
3. Mostre o dicionário final com as contagens.
4. Mostre também a palavra mais frequente e quantas vezes apareceu.
5. Se houver empate na frequência máxima, mostra todas as palavras empatadas.

> Resolução:

```python

frase = input("Introduz uma frase: ")
palavras = frase.split() # divide a frase em palavras usando o método split(), que por padrão divide a string em partes usando os espaços como separadores.
contagem = {}

for palavra in palavras:
    palavra = palavra.lower() # converte a palavra para minúscula para garantir que a contagem seja case-insensitive.
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print("Contagem de palavras:", contagem)
max_frequencia = max(contagem.values())
palavras_mais_frequentes = [palavra for palavra, frequencia in contagem.items() if frequencia == max_frequencia]

# Ou de forma mais simples, usando uma estrutura de controlo:
# max_frequencia = 0
# palavras_mais_frequentes = []
# for palavra, frequencia in contagem.items():
#     if frequencia > max_frequencia:
#         max_frequencia = frequencia
#         palavras_mais_frequentes = [palavra]
#     elif frequencia == max_frequencia:
#         palavras_mais_frequentes.append(palavra)



```

## Exercício 34

Cria um programa que:

1. Tenha um dicionário de produtos, onde cada chave é o nome do produto e o valor é outro dicionário com:
    - `"preco"` (float)
    - `"stock"` (int)

2. Peça ao utilizador para registar uma venda (produto + quantidade).
3. Verifique se o produto existe e se há stock suficiente.
4. Se a venda for válida, atualize o stock e mostre o total a pagar.
5. No fim, mostre:
    - valor total vendido
    - produto com maior faturação
    - lista de produtos esgotados (stock igual a 0)

## Exercício 35

Cria um programa que:

1. Peça ao utilizador para introduzir nomes de alunos e, para cada aluno, várias disciplinas com a respetiva nota.
2. Guarde os dados num dicionário aninhado, por exemplo:

    ```python
    turma = {
        "Ana": {"Matemática": 17, "Português": 15},
        "João": {"Matemática": 12, "Português": 14}
    }
    ```

3. Calcule e mostre:
    - média de cada aluno
    - média de cada disciplina
    - melhor aluno (maior média geral)

4. Mostre os alunos em risco (média inferior a 10).

> Resolução:

```python

turma = {}
while True:
    nome = input("Introduz o nome do aluno (ou 'sair' para terminar): ")
    if nome.lower() == 'sair':
        break

    disciplinas = {}
    while True:
        disciplina = input(f"Introduz o nome da disciplina para o aluno {nome} (ou 'sair' para terminar): ")
        if disciplina.lower() == 'sair':
            break
        nota = float(input(f"Introduz a nota para a disciplina {disciplina}: "))
        disciplinas[disciplina] = nota

    turma[nome] = disciplinas

medias_alunos = {}
for aluno, disciplinas in turma.items():
    media = sum(disciplinas.values()) / len(disciplinas)
    medias_alunos[aluno] = media
    print(f"A média do aluno {aluno} é: {media}.")

medias_disciplinas = {}
for disciplinas in turma.values():
    for disciplina, nota in disciplinas.items():
        if disciplina not in medias_disciplinas:
            medias_disciplinas[disciplina] = []
        medias_disciplinas[disciplina].append(nota)

for disciplina, notas in medias_disciplinas.items():
    media = sum(notas) / len(notas)
    print(f"A média da disciplina {disciplina} é: {media}.")

melhor_aluno = max(medias_alunos, key=medias_alunos.get)
print(f"O melhor aluno é: {melhor_aluno} com média {medias_alunos[melhor_aluno]}.")
alunos_em_risco = [aluno for aluno, media in medias_alunos.items() if media < 10]
if alunos_em_risco:
    print("Alunos em risco (média inferior a 10):")
    for aluno in alunos_em_risco:
        print(aluno)
else:
    print("Não há alunos em risco.")
```

## Exercício 36

Cria um programa que:

1. Receba um texto e construa um índice invertido usando dicionários:
    - cada palavra é uma chave
    - o valor é uma lista ordenada com as posições em que essa palavra aparece no texto

2. Exemplo:
    - texto: `"hoje estudei python e hoje revisei python"`
    - resultado parcial: `{"hoje": [0, 4], "python": [2, 6], ...}`

3. Depois, peça ao utilizador uma palavra e mostre:
    - se existe no índice
    - em que posições aparece
    - quantas ocorrências tem

> Resolução:

```python
texto = input("Introduz um texto: ")
palavras = texto.split()
indice_invertido = {}

for posicao, palavra in enumerate(palavras):
    palavra = palavra.lower() # converte a palavra para minúscula para garantir que o índice seja case-insensitive.
    if palavra in indice_invertido:
        indice_invertido[palavra].append(posicao)
    else:
        indice_invertido[palavra] = [posicao]

palavra_busca = input("Introduz a palavra a buscar: ").lower()
if palavra_busca in indice_invertido:
    posicoes = indice_invertido[palavra_busca]
    ocorrencias = len(posicoes)
    print(f"A palavra '{palavra_busca}' existe no índice.")
    print(f"Posições: {posicoes}")
    print(f"Ocorrências: {ocorrencias}")
else:
    print(f"A palavra '{palavra_busca}' não existe no índice.")
```

## Exercício 37

Cria um programa que:

1. Modele um mapa de cidades com um dicionário de dicionários, onde:
    - cada chave principal é uma cidade
    - cada valor é outro dicionário com cidades vizinhas e a distância entre elas

2. Exemplo:

    ```python
    mapa = {
        "Porto": {"Braga": 55, "Aveiro": 75},
        "Braga": {"Porto": 55, "Guimarães": 25},
        "Aveiro": {"Porto": 75, "Coimbra": 65}
    }
    ```

3. Peça ao utilizador cidade de origem e destino.
4. Encontre o caminho com menor distância total entre as duas cidades (podes usar uma abordagem semelhante ao algoritmo de Dijkstra).
5. Mostre:
    - caminho encontrado (sequência de cidades)
    - distância total
    - mensagem de erro se não existir ligação entre origem e destino

# Funções

## Exercício 38

Cria um programa que:

1. Defina uma função que diga "Olá mundo!".
2. Chame a função para mostrar a mensagem.

# Exercício 39

Cria um programa que:

1. Defina uma função que receba um nome como parâmetro e diga "Olá, <nome>!".
2. Chame a função com o teu nome para mostrar a mensagem.

## Exercício 40

Cria um programa que:

1. Defina uma função que receba dois números como parâmetros e mostre a soma, subtração, multiplicação e divisão desses números.
2. Chame a função com dois números à tua escolha para mostrar os resultados.

## Exercício 41

Cria um programa que:

1. Defina uma função que receba um número como parâmetro e diga se é par ou ímpar.
2. Chame a função com um número à tua escolha para mostrar a mensagem.

## Exercício 42

Usando a função do exercício anterior, cria um programa que:

1. Peça ao utilizador para introduzir 10 números inteiros e positivos, um de cada vez.
2. Introduza os números numa lista e, para cada número, chame a função para dizer se é par ou ímpar.

## Exercício 43

Cria um programa que:

1. Defina uma função que receba uma lista de números como parâmetro e mostre o número máximo, mínimo e a média dos números da lista.
2. Chame a função com uma lista de números à tua escolha para mostrar os resultados.

## Exercício 44

Cria um programa que:

1. Defina uma função que receba um dicionário de produtos (com preço e stock) e um produto a comprar (com quantidade) como parâmetros.
2. A função deve verificar se o produto existe, se há stock suficiente e calcular o total a pagar, atualizando o stock se a compra for válida.
3. Chame a função com um dicionário de produtos e um produto a comprar para mostrar os resultados.
