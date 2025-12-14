# Python (10.º Ano) - 00 · Exercicios de preparação

> **Objetivo deste ficheiro**  
> Preparar os alunos para as avaliações, através de exercícios que envolvem os conceitos básicos de Python.

## Preparação para o teste de 15/12/2025

Matérias que serão avaliadas:

-   Funções:

    -   Definição e invocação de funções
    -   Parâmetros e argumentos
    -   Valores de retorno
    -   _\*args e \*\*kwargs_

-   Ficheiros JSON:
    -   Leitura e escrita de ficheiros JSON

Matérias anteriores que podem ser úteis:

-   Tipos de dados básicos (inteiros, strings, listas, dicionários)
-   Estruturas de controlo (if, for, while)
-   Listas e dicionários

### Exercícios

**Funções Simples sem retorno**

1. Escreve uma função chamada `saudacao` que recebe um nome como parâmetro e imprime uma mensagem de saudação personalizada.

> Resolução:

```python
def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo(a) ao curso de Python.")

# Exemplo de uso:
saudacao("Maria")
```

2. Escreve uma função para cada uma das operações matemáticas básicas (adição, subtração, multiplicação, divisão) que recebe dois números como parâmetros e imprime o resultado da operação.

> Resolução:

```python
def adicionar(a, b):
    print(f"A soma de {a} e {b} é {a + b}")
def subtrair(a, b):
    print(f"A subtração de {a} e {b} é {a - b}")
def multiplicar(a, b):
    print(f"A multiplicação de {a} e {b} é {a * b}")
def dividir(a, b):
    if b != 0:
        print(f"A divisão de {a} por {b} é {a / b}")
    else:
        print("Erro: Divisão por zero não é permitida.")

# Exemplo de uso:
adicionar(5, 3)
subtrair(10, 4)
multiplicar(2, 6)
dividir(8, 2)
dividir(5, 0)
```

3. Cria uma função que calcule a área de um retângulo. A função deve receber a largura e a altura como parâmetros e imprimir a área.

> Resolução:

```python
def area_retangulo(largura, altura):
    area = largura * altura
    print(f"A área do retângulo é {area}")

# Exemplo de uso:
area_retangulo(5, 10)
```

4. Escreve uma função que receba uma lista de números e imprima cada número multiplicado por 2.

> Resolução:

```python
def multiplica_por_dois(numeros):
    for numero in numeros:
        print(numero * 2)

# Exemplo de uso:
multiplica_por_dois([1, 2, 3, 4, 5])
```

---

**Funções**

5. Rescreve as funções dos exercícios 2 e 3 para que retornem o resultado em vez de o imprimir. Testa as funções imprimindo os valores retornados.

> Resolução:

```python
def adicionar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."

def area_retangulo(largura, altura):
    return largura * altura

# Exemplo de uso:
print(adicionar(5, 3))
print(subtrair(10, 4))
print(multiplicar(2, 6))
print(dividir(8, 2))
print(dividir(5, 0))
print(area_retangulo(5, 10))
```

6. Cria uma função que receba uma lista de números e retorne a soma de todos os números pares na lista.

> Resolução:

```python
def soma_pares(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    return soma

# Exemplo de uso:
print(soma_pares([1, 2, 3, 4, 5, 6]))  # Deve retornar 12
```

7. Escreve uma função que receba uma string e retorne o número de vogais na string.

> Resolução:

```python
def contar_vogais(texto):
    vogais = "aeiouAEIOUàáâãäåèéêëìíîïòóôõöùúûüÁÀÂÃÄÅÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜ"
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador

# Exemplo de uso:
print(contar_vogais("Olá, mundo!"))  # Deve retornar 4
```

8. Cria uma função que receba uma lista de palavras e retorne a palavra mais longa da lista.

> Resolução:

```python
def palavra_mais_longa(palavras):
    mais_longa = palavras[0]
    for palavra in palavras:
        if len(palavra) > len(mais_longa):
            mais_longa = palavra
    return mais_longa

# Exemplo de uso:
print(palavra_mais_longa(["casa", "automóvel", "bicicleta", "avião"]))  # Deve retornar "automóvel"
```

9. Escreve uma função que recebe dois parâmetros: uma lista de números e um número. A função deve retornar `True` se o número estiver na lista e `False` caso contrário.

> Resolução:

```python
def numero_na_lista(numeros, numero):
    return numero in numeros # Retorna True se o número estiver na lista, caso contrário False

# Exemplo de uso:
print(numero_na_lista([1, 2, 3, 4, 5], 3))  # Deve retornar True
print(numero_na_lista([1, 2, 3, 4, 5], 6))  # Deve retornar False
```

10. Cria uma função que recebe um dicionário e o mostre de forma organizada.

> Resolução:

```python
def mostrar_dicionario(dicionario):
    for chave, valor in dicionario.items():
        print(f"{chave}: {valor}")

# Exemplo de uso:
mostrar_dicionario({"nome": "João", "idade": 25, "cidade": "Lisboa"})
```

11. Cria uma função que receba uma lista de dicionários (cada dicionário representa uma pessoa com nome e idade) e retorne a média das idades.

> Resolução:

```python
def media_idades(pessoas):
    total_idade = 0
    for pessoa in pessoas:
        total_idade += pessoa["idade"]
    return total_idade / len(pessoas)
# Exemplo de uso:
pessoas = [{"nome": "Ana", "idade": 30}, {"nome": "Bruno", "idade": 25}, {"nome": "Carla", "idade": 35}]
print(media_idades(pessoas))  # Deve retornar 30.0
```

12. Considera um dicionário com o seguinte formato:

```python
{
    1 : {
        "nome": "Ana",
        "notas": {
            "Matemática": 18,
            "Física": 16,
            "Química": 17
        },
        "faltas": {
            "Matemática": 2,
            "Física": 0,
            "Química": 1
        }
    }
}
```

Cria funções para:

-   Calcular a média das notas de um aluno.
-   Calcular o total de faltas de um aluno.
-   Mostrar todos os alunos de forma organizada.

> Resolução:

```python

def calcular_media_notas(aluno):
    notas = aluno["notas"].values()
    return sum(notas) / len(notas)

# Ou usando o for:
# def calcular_media_notas(aluno):
#     total = 0
#     count = 0
#     for nota in aluno["notas"].values():
#         total += nota
#         count += 1
#     return total / count

def calcular_total_faltas(aluno):
    faltas = aluno["faltas"].values()
    return sum(faltas)

# Ou usando o for:
# def calcular_total_faltas(aluno):
#     total = 0
#     for falta in aluno["faltas"].values():
#         total += falta
#     return total

def mostrar_alunos(alunos):
    for id_aluno, dados in alunos.items():
        print(f"ID: {id_aluno}")
        print(f"Nome: {dados['nome']}")
        print(f"Média das Notas: {calcular_media_notas(dados)}")
        print(f"Total de Faltas: {calcular_total_faltas(dados)}")
        print("-" * 20)
```

---

** args e kwargs **

13. Cria uma função que receba um número variável de argumentos e retorne a soma de todos os argumentos.

> Resolução:

```python
def soma_variavel(*args):
    total = 0
    for numero in args:
        total += numero
    return total
# Exemplo de uso:
print(soma_variavel(1, 2, 3, 4, 5))  # Deve retornar 15
```

14. Cria uma função que receba um número variável de argumentos e retorne o maior e o menor número entre eles.

> Resolução:

```python
def maior_menor(*args):
    maior = max(args)
    menor = min(args)
    return maior, menor

# Exemplo de uso:
maior, menor = maior_menor(3, 1, 4, 1, 5, 9, 2)
print(f"Maior: {maior}, Menor: {menor}")  # Deve retornar Maior: 9, Menor: 1
```

15. Cria uma função que receba um número variável de argumentos e diga quantos são pares e quantos são ímpares.

> Resolução:

```python
def contar_pares_impares(*args):
    pares = 0
    impares = 0
    for numero in args:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

# Exemplo de uso:
pares, impares = contar_pares_impares(1, 2, 3, 4, 5, 6)
print(f"Pares: {pares}, Ímpares: {impares}")  # Deve retornar Pares: 3, Ímpares: 3
```

16. Cria uma função que recebe uma número variável de argumentos nomeados e imprima cada par chave-valor.

> Resolução:

```python
def imprimir_chave_valor(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Exemplo de uso:
imprimir_chave_valor(nome="João", idade=28, cidade="Porto")
```

---

**Ficheiros JSON**

17. Pede ao utilizador para introduzir o nome, idade e cidade. Guarda estes dados num ficheiro JSON com o formato de um dicionário.

> Resolução:

```python
import json

def guardar_dados_utilizador():
    nome = input("Introduza o seu nome: ")
    idade = input("Introduza a sua idade: ")
    cidade = input("Introduza a sua cidade: ")

    dados = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }

    with open("dados_utilizador.json", "w") as ficheiro:
        json.dump(dados, ficheiro, indent=4)

guardar_dados_utilizador()
```

18. Lê o ficheiro JSON criado no exercício anterior e imprime os dados de forma organizada.

> Resolução:

```python

import json
def ler_dados_utilizador():
    with open("dados_utilizador.json", "r") as ficheiro:
        dados = json.load(ficheiro)

    print("Dados do Utilizador:")
    print(f"Nome: {dados['nome']}")
    print(f"Idade: {dados['idade']}")
    print(f"Cidade: {dados['cidade']}")

ler_dados_utilizador()
```

19. Cria uma função que receba uma lista de dicionários (cada dicionário representa uma pessoa com nome e idade) e guarde esta lista num ficheiro JSON.

> Resolução:

```python
import json
def guardar_lista_pessoas(pessoas, nome_ficheiro):
    with open(nome_ficheiro, "w") as ficheiro:
        json.dump(pessoas, ficheiro, indent=4)

# Exemplo de uso:
pessoas = [{"nome": "Ana", "idade": 30}, {"nome": "Bruno", "idade": 25}, {"nome": "Carla", "idade": 35}]
guardar_lista_pessoas(pessoas, "pessoas.json")
```

20. Cria uma função que leia o ficheiro JSON criado no exercício anterior e retorne a lista de dicionários.

> Resolução:

```python
import json
def ler_lista_pessoas(nome_ficheiro):
    with open(nome_ficheiro, "r") as ficheiro:
        pessoas = json.load(ficheiro)
    return pessoas

# Exemplo de uso:
pessoas = ler_lista_pessoas("pessoas.json")
print(pessoas)
```

21. Cria um programa que permita ao utilizador gerir uma lista de tarefas (to-do list). O programa deve permitir adicionar, remover e listar tarefas. Os dados devem estar guardados num ficheiro JSON. Sem usar exceções.

> Resolução:

```python
import json

def adicionar_tarefa(tarefas, tarefa):
    tarefas.append(tarefa)

def remover_tarefa(tarefas, tarefa):
    if tarefa in tarefas:
        tarefas.remove(tarefa)

def listar_tarefas(tarefas):
    print("Tarefas:")
    for tarefa in tarefas:
        print(f"- {tarefa}")

def guardar_tarefas(tarefas, nome_ficheiro):
    with open(nome_ficheiro, "w") as ficheiro:
        json.dump(tarefas, ficheiro, indent=4)

def ler_tarefas(nome_ficheiro):
    with open(nome_ficheiro, "r") as ficheiro:
        tarefas = json.load(ficheiro)
    return tarefas

def menu():
    tarefas = []
    nome_ficheiro = "tarefas.json"

    tarefas = ler_tarefas(nome_ficheiro)

    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Listar tarefas")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tarefa = input("Introduza a tarefa a adicionar: ")
            adicionar_tarefa(tarefas, tarefa)
            guardar_tarefas(tarefas, nome_ficheiro)
        elif escolha == "2":
            tarefa = input("Introduza a tarefa a remover: ")
            remover_tarefa(tarefas, tarefa)
            guardar_tarefas(tarefas, nome_ficheiro)
        elif escolha == "3":
            listar_tarefas(tarefas)
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()

```

22. Cria as funções para um programa que faça a gestão das notas de alunos de uma turma. O programa deve poder guardar os nomes dos alunos e as suas notas nas diferentes disciplinas. O programa deve manter os dados num ficheiro JSON. Deve ser possível consultar a média de cada aluno e se um determinado aluno tem negativas (e quantas).
    O programa deve ter as seguintes funções:
    guardar_dados_alunos -> Função que recebe uma lista de alunos e a grava num ficheiro.
    ler_dados_alunos -> Função que devolve uma lista com os dados dos alunos gravados em ficheiro
    calcula_media -> Função que recebe uma lista de alunos e mostra a média de cada aluno na lista
    devolve_negativas -> Função que recebe um aluno e devolve quantas negativas esse aluno tem.

> Resolução:

```python
import json
def guardar_dados_alunos(alunos, nome_ficheiro):
    with open(nome_ficheiro, "w") as ficheiro:
        json.dump(alunos, ficheiro, indent=4)

def ler_dados_alunos(nome_ficheiro):
    with open(nome_ficheiro, "r") as ficheiro:
        alunos = json.load(ficheiro)
    return alunos

def calcula_media(alunos):
    for aluno in alunos:
        notas = aluno["notas"].values()
        media = sum(notas) / len(notas)
        print(f"{aluno['nome']} - Média: {media:.2f}")

def devolve_negativas(aluno):
    negativas = 0
    for nota in aluno["notas"].values():
        if nota < 10:
            negativas += 1
    return negativas

# Exemplo de uso:
alunos = [
    {"nome": "Ana", "notas": {"Matemática": 18, "Física": 16, "Química": 9}},
    {"nome": "Bruno", "notas": {"Matemática": 12, "Física": 14, "Química": 11}},
    {"nome": "Carla", "notas": {"Matemática": 8, "Física": 7, "Química": 10}}
]

guardar_dados_alunos(alunos, "alunos.json")
alunos_lidos = ler_dados_alunos("alunos.json")
calcula_media(alunos_lidos)
for aluno in alunos_lidos:
    negativas = devolve_negativas(aluno)
    print(f"{aluno['nome']} - Negativas: {negativas}")
```
