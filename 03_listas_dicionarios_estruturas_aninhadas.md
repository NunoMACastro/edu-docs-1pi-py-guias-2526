# Python (10.º Ano) - 03 · Listas, Dicionários e Estruturas Aninhadas

> **Objetivo deste ficheiro**  
> Consolidar o armazenamento de coleções de dados em Python (listas e dicionários) e começar a pensar de forma mais estruturada com estruturas aninhadas.

---

## Índice

-   [0. Como usar este ficheiro](#0-como-usar-este-ficheiro)
-   [1. Listas](#1-listas)
-   [2. Dicionários](#2-dicion%C3%A1rios)
-   [3. Estruturas de dados aninhadas](#3-estruturas-de-dados-aninhadas)
-   [4. Exemplos aplicados](#4-exemplos-aplicados)
-   [5. Exercícios (Listas, Dicionários e Estruturas Aninhadas)](#5-exerc%C3%ADcios-listas-dicion%C3%A1rios-e-estruturas-aninhadas)
-   [6. Changelog](#6-changelog)

---

## 0. Como usar este ficheiro

1. Lê a explicação teórica com atenção.
2. Experimenta todos os exemplos num ficheiro `.py`.
3. Faz pequenas alterações para perceberes o efeito (muda valores, acrescenta elementos, etc.).
4. No fim, resolve os **exercícios**. Começa pelos mais simples e tenta chegar aos desafios.

Este ficheiro liga com os anteriores:

-   `01_introducao_variaveis_tipos_strings_io.md`
-   `02_operadores_e_controlo_de_fluxo_if_ciclos.md`

---

## 1. Listas

### 1.1. O que é uma lista?

Uma **lista** é uma coleção ordenada de elementos.  
Cada elemento tem uma **posição** (índice) começando em 0.

Exemplos de listas:

```python
numeros = [10, 20, 30]              # lista de inteiros
nomes = ["Ana", "Bruno", "Carla"]   # lista de strings
mistura = [10, "Ana", True, 3.14]   # lista com vários tipos
```

-   As listas são **mutáveis**: podes alterar, adicionar e remover elementos.
-   Podem conter qualquer tipo de dados, inclusive outras listas.

---

### 1.2. Acesso por índice

Tal como nas strings, os índices vão de `0` a `len(lista) - 1`.

```python
l = [3, 1, 4]

print(l[0])    # 3  (primeiro elemento)
print(l[1])    # 1
print(l[2])    # 4  (último elemento)
print(l[-1])   # 4  (índice negativo conta a partir do fim)
```

Se tentares aceder a um índice inválido (`l[10]` numa lista com 3 elementos) vais ter um erro `IndexError`.

---

### 1.3. Modificar elementos

Como as listas são mutáveis, podes alterar elementos diretamente:

```python
notas = [12, 15, 9]

notas[2] = 10    # altera o terceiro elemento (índice 2)
print(notas)    # [12, 15, 10]
```

---

### 1.4. Métodos importantes das listas

Alguns métodos muito usados:

```python
l = [3, 1, 4]

l.append(1)        # adiciona 1 no fim -> [3, 1, 4, 1]
l.insert(1, 7)     # insere 7 no índice 1 -> [3, 7, 1, 4, 1]
ultimo = l.pop()   # remove e devolve o último elemento (1)
l.remove(7)        # remove a PRIMEIRA ocorrência de 7
l.clear()          # apaga todos os elementos -> []
```

Vamos ver com mais calma:

-   `append(x)` - acrescenta `x` no fim.
-   `insert(i, x)` - insere `x` na posição `i`, deslocando o resto.
-   `pop()` - remove e devolve o último elemento.
-   `pop(i)` - remove e devolve o elemento no índice `i`.
-   `remove(x)` - remove a primeira ocorrência de `x` (se não existir, dá erro).
-   `clear()` - esvazia a lista.

Mais métodos úteis para análise:

```python
l = [3, 1, 4, 1, 5, 9]

conta_uns = l.count(1)   # quantas vezes aparece o 1
idx_quatro = l.index(4)  # índice da primeira ocorrência do 4

l.sort()                 # ordena a lista (in-place)
l.reverse()              # inverte a ordem (in-place)

print(l)
```

---

### 1.5. Funções úteis: `len`, `sum`, `min`, `max`, `sorted`

Além dos métodos, existem funções que trabalham com listas:

```python
nums = [10, 20, 5, 15]

print(len(nums))      # 4 (número de elementos)
print(sum(nums))      # 50 (soma dos elementos)
print(min(nums))      # 5  (mínimo)
print(max(nums))      # 20 (máximo)

ordenada = sorted(nums)        # devolve NOVA lista ordenada
print(ordenada)                # [5, 10, 15, 20]
print(nums)                    # [10, 20, 5, 15] (não mudou)
```

-   `sorted(lista)` não altera a lista original; devolve uma cópia ordenada.
-   Já `lista.sort()` altera a própria lista.

---

### 1.6. Percorrer listas com `for`

O padrão mais comum é:

```python
numeros = [2, 4, 6, 8]
quadrados = []

for n in numeros:
    quadrados.append(n ** 2)

print(quadrados)   # [4, 16, 36, 64]
```

Também podes percorrer por **índice**:

```python
nomes = ["Ana", "Bruno", "Carla"]

for i in range(len(nomes)):
    print(i, nomes[i])
```

---

### 1.7. Padrões clássicos com listas

1. **Construir uma nova lista a partir de outra**

```python
numeros = [1, -3, 5, -2, 0, 10]
positivos = []

for n in numeros:
    if n > 0:
        positivos.append(n)

print(positivos)   # [1, 5, 10]
```

2. **Calcular a média**

```python
notas = [12, 15, 9, 18]

soma = 0
for n in notas:
    soma += n

media = soma / len(notas)
print("Média =", media)
```

3. **Encontrar o mínimo/máximo sem `min`/`max`**

```python
numeros = [10, 3, 7, 2, 9]

menor = numeros[0]
for n in numeros:
    if n < menor:
        menor = n

print("Menor número:", menor)
```

---

### 1.8. Compreensões de lista (curiosidade)

Uma **compreensão de lista** é uma forma compacta de construir listas.

Exemplos equivalentes:

```python
# Forma "normal"
dados = [1, 2, 3, 4, 5]
dobros = []

for x in dados:
    dobros.append(x * 2)

# Compreensão de lista
dobros2 = [x * 2 for x in dados]

print(dobros2)   # [2, 4, 6, 8, 10]
```

Com condição:

```python
pares = [x for x in dados if x % 2 == 0]   # [2, 4]
```

Para já, o importante é perceber que existe; usa a forma “normal” quando estiveres a aprender e usa compreensões quando te sentires mais confortável.

---

## 2. Dicionários

### 2.1. Ideia chave → valor

Um **dicionário** é uma coleção de pares `chave: valor`.

Exemplos:

```python
pessoa = {
    "nome": "Ana Silva",
    "idade": 28,
    "profissao": "Engenheira"
}

precos = {
    "maçã": 0.79,
    "banana": 0.35,
    "pera": 1.05
}
```

-   As **chaves** normalmente são strings, mas podem ser outros tipos imutáveis.
-   Os **valores** podem ser qualquer coisa (números, strings, listas, dicionários, etc.).

---

### 2.2. Aceder e atualizar valores

```python
pessoa = {
    "nome": "Ana Silva",
    "idade": 28,
    "profissao": "Engenheira"
}

print(pessoa["nome"])    # "Ana Silva"

pessoa["idade"] = 29     # atualiza idade
pessoa["cidade"] = "Lisboa"  # nova chave/valor

print(pessoa)
```

Se tentares aceder a uma chave que não existe (`pessoa["altura"]`), dá erro `KeyError`.

---

### 2.3. O método `get`

`get` permite aceder a uma chave com um **valor por defeito** caso a chave não exista.

```python
pessoa = {
    "nome": "Ana Silva",
    "idade": 28
}

nome = pessoa.get("nome", "Desconhecido")
altura = pessoa.get("altura", "Não definida")

print(nome)    # "Ana Silva"
print(altura)  # "Não definida"
```

---

### 2.4. Remover elementos

```python
pessoa = {
    "nome": "Ana Silva",
    "idade": 28,
    "profissao": "Engenheira"
}

prof = pessoa.pop("profissao")   # remove e devolve o valor
print(prof)        # "Engenheira"
print(pessoa)      # já não tem "profissao"

# Outra forma:
del pessoa["idade"]    # apaga a chave "idade"
```

---

### 2.5. Percorrer dicionários: `keys`, `values`, `items`

Exemplo com dicionário de preços:

```python
precos = {"maçã": 0.79, "banana": 0.35, "pera": 1.05, "uva": 2.40}

# Percorrer CHAVES
for fruta in precos.keys():
    print(fruta, "->", precos[fruta])

# Forma curta (equivalente a precos.keys()):
for fruta in precos:
    print("Chave:", fruta)

# Percorrer VALORES
total = 0.0
for valor in precos.values():
    total += valor

media = total / len(precos)
print("Média dos preços:", round(media, 2))

# Percorrer PARES (chave, valor)
for fruta, valor in precos.items():
    print(f"{fruta} custa {valor:.2f} euros")
```

---

### 2.6. Verificar existência de chaves (`in`)

```python
precos = {"maçã": 0.79, "banana": 0.35, "pera": 1.05}

print("banana" in precos)         # True (chave existe)
print("laranja" in precos)        # False

if "pera" in precos:
    print("Temos preço da pera:", precos["pera"])
```

---

## 3. Estruturas de dados aninhadas

Agora vamos combinar listas e dicionários para representar informação mais rica.

---

### 3.1. Lista de listas (matriz)

Uma **matriz** pode ser representada como lista de listas:

```python
matriz = [
    [1, 2, 3],   # linha 0
    [4, 5, 6],   # linha 1
    [7, 8, 9]    # linha 2
]

print(matriz[0])       # [1, 2, 3]
print(matriz[1][2])    # 6 (linha 1, coluna 2)
```

Percorrer a matriz:

```python
print("Matriz:")
for linha in matriz:         # cada linha é uma lista
    print(linha)
```

Adicionar uma nova linha:

```python
nova_linha = [10, 11, 12]
matriz.append(nova_linha)

print("Matriz atualizada:")
for linha in matriz:
    print(linha)
```

---

### 3.2. Dicionário de listas (turmas e alunos)

```python
turmas = {
    "10A": ["Ana", "Bruno", "Carla"],
    "10B": ["David", "Eva", "Fábio"]
}

for turma, alunos in turmas.items():
    print(f"Turma {turma}:")
    for aluno in alunos:
        print(" -", aluno)
```

Adicionar um novo aluno e uma nova turma:

```python
turmas["10B"].append("Gabriela")    # novo aluno na 10B
turmas["10C"] = ["Helena", "Igor"]  # nova turma
```

---

### 3.3. Dicionário de dicionários (notas por disciplina)

```python
notas = {
    "Ana":   {"Matemática": 18, "Português": 16},
    "Bruno": {"Matemática": 14, "Português": 15}
}

nota_ana_matematica = notas["Ana"]["Matemática"]
print("Nota de Matemática da Ana:", nota_ana_matematica)
```

Percorrer:

```python
for aluno, disciplinas in notas.items():
    print(f"Notas de {aluno}:")
    for disciplina, nota in disciplinas.items():
        print(f" - {disciplina}: {nota}")
```

Adicionar nova disciplina e novo aluno:

```python
notas["Ana"]["Inglês"] = 17
notas["Carla"] = {"Matemática": 19, "Português": 18}
```

Calcular média de um aluno:

```python
alvo = "Ana"
soma_notas = 0
num_disciplinas = 0

for disciplina, nota in notas[alvo].items():
    soma_notas += nota
    num_disciplinas += 1

media = soma_notas / num_disciplinas
print(f"Média de {alvo}: {media:.2f}")
```

---

### 3.4. Lista de dicionários (livros, alunos, etc.)

Exemplo: lista de livros.

```python
livros = [
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "genero": "Distopia"},
    {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954, "genero": "Fantasia"},
    {"titulo": "Dom Quixote", "autor": "Miguel de Cervantes", "ano": 1605, "genero": "Clássico"}
]

print("Lista de livros:")
for livro in livros:
    print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Género: {livro['genero']}")
```

Pesquisar livro por título (ignorando maiúsculas/minúsculas):

```python
titulo_procurado = input("Introduz o título do livro que procuras: ")

encontrado = False
for livro in livros:
    if livro["titulo"].lower() == titulo_procurado.lower():
        print("Livro encontrado:")
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Género: {livro['genero']}")
        encontrado = True
        break

if not encontrado:
    print("Livro não encontrado.")
```

Outro exemplo: lista de alunos com dicionários simples:

```python
alunos = [
    {"nome": "Ana", "idade": 16},
    {"nome": "Bruno", "idade": 17}
]

for aluno in alunos:
    print(f"{aluno['nome']} tem {aluno['idade']} anos")

novo_aluno = {"nome": "Carla", "idade": 16}
alunos.append(novo_aluno)
```

---

## 4. Exemplos aplicados

### 4.1. Temperaturas mensais

Vamos usar uma lista de temperaturas médias mensais e uma lista com os nomes dos meses.

```python
temperaturas = [15.5, 16.0, 18.2, 20.1, 22.5, 25.0, 27.3, 26.8, 24.0, 20.5, 17.8, 15.2]
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
```

Consultar a temperatura de um mês:

```python
mes_procurado = int(input("Número do mês (1-12): "))

if 1 <= mes_procurado <= 12:
    indice = mes_procurado - 1
    print(f"A temperatura média em {meses[indice]} é {temperaturas[indice]} °C.")
else:
    print("Mês inválido.")
```

Calcular a média anual:

```python
media_anual = sum(temperaturas) / len(temperaturas)
print(f"Temperatura média anual: {media_anual:.2f} °C")
```

Encontrar mês mais quente e mais frio (com `max`/`min`):

```python
indice_quente = temperaturas.index(max(temperaturas))
indice_frio = temperaturas.index(min(temperaturas))

print(f"Mês mais quente: {meses[indice_quente]} ({temperaturas[indice_quente]} °C)")
print(f"Mês mais frio: {meses[indice_frio]} ({temperaturas[indice_frio]} °C)")
```

Também podes tentar fazer isto **sem** usar `max` e `min`, usando um ciclo e comparações.

---

### 4.2. Turmas e alunos (estrutura mais complexa)

Exemplo mais completo, juntando tudo: dicionário de turmas, cada turma com:

-   lista de alunos (cada aluno é um dicionário com `nome` e `notas`),
-   nome do professor.

```python
turmas = {
    "10A": {
        "alunos": [
            {"nome": "Ana", "notas": {"Matemática": 18, "Português": 16}},
            {"nome": "Bruno", "notas": {"Matemática": 14, "Português": 15}},
            {"nome": "Carla", "notas": {"Matemática": 12, "Português": 14}}
        ],
        "professor": "Sr. Silva"
    },
    "10B": {
        "alunos": [
            {"nome": "David", "notas": {"Matemática": 10, "Português": 12}},
            {"nome": "Eva", "notas": {"Matemática": 9, "Português": 11}},
            {"nome": "Fábio", "notas": {"Matemática": 15, "Português": 14}}
        ],
        "professor": "Sra. Costa"
    }
}
```

Mostrar lista de alunos e notas por turma:

```python
for turma, info in turmas.items():
    print(f"Turma {turma}:")
    for aluno in info["alunos"]:
        print(f"  Aluno: {aluno['nome']}, Notas: {aluno['notas']}")
    print()
```

Contar quantos alunos têm pelo menos uma negativa (nota < 10) em cada turma:

```python
for turma, info in turmas.items():
    count_negativas = 0
    for aluno in info["alunos"]:
        for nota in aluno["notas"].values():
            if nota < 10:
                count_negativas += 1
                break   # conta o aluno apenas uma vez
    print(f"Turma {turma} tem {count_negativas} alunos com pelo menos uma negativa.")
```

Procurar um aluno e dizer em que turma está:

```python
nome_procurado = input("Nome do aluno a procurar: ")
encontrado = False

for turma, info in turmas.items():
    for aluno in info["alunos"]:
        if aluno["nome"].lower() == nome_procurado.lower():
            print(f"O aluno {nome_procurado} está na turma {turma} com notas: {aluno['notas']}")
            encontrado = True
            break
    if encontrado:
        break

if not encontrado:
    print("Aluno não encontrado.")
```

---

## 5. Exercícios (Listas, Dicionários e Estruturas Aninhadas)

> Tenta resolver estes exercícios usando apenas o que está neste ficheiro e nos anteriores.  
> Alguns são adaptações dos exercícios que já fizeste, mas agora estão organizados por tema.

### Exercício 1 - Lista básica e índices

Cria uma lista com pelo menos 5 números à tua escolha.  
O programa deve:

1. Mostrar a lista completa.
2. Mostrar o primeiro elemento.
3. Mostrar o último elemento.
4. Mostrar o comprimento da lista com `len()`.

> Resolução:

```python
numeros = [10, 25, -3, 42, 7]
print("Lista completa:", numeros)
print("Primeiro elemento:", numeros[0])
print("Último elemento:", numeros[-1])
print("Comprimento da lista:", len(numeros))
```

---

### Exercício 2 - Positivos, negativos e zeros (lista)

Pede 5 números ao utilizador e guarda-os numa lista.  
Depois, percorre a lista e, para cada número, imprime se é:

-   positivo,
-   negativo,
-   ou zero.

> Resolução:

```python
numeros = []
for _ in range(5):
    n = float(input("Introduz um número: "))
    numeros.append(n)

for n in numeros:
    if n > 0:
        print(n, "é positivo")
    elif n < 0:
        print(n, "é negativo")
    else:
        print(n, "é zero")
```

---

### Exercício 3 - Maior e menor sem `max`/`min`

Pede 10 números ao utilizador e guarda-os numa lista.

-   Sem usar `max()` nem `min()`, descobre qual é o maior e o menor número usando um ciclo `for` e comparações.
-   No final, mostra os dois valores.

> Resolução:

```python
numeros = []
for i in range(10):
    n = float(input("Introduz um número: "))
    numeros.append(n)

maior = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print("Maior número:", maior)
print("Menor número:", menor)
```

---

### Exercício 4 - Separar pares e ímpares

Pede ao utilizador que introduza 10 números inteiros e guarda-os numa lista.  
Depois:

1. Cria uma nova lista apenas com os números pares.
2. Cria outra lista apenas com os números ímpares.
3. Mostra as duas listas.

> Resolução:

```python
numeros = []
for _ in range(10): # uma vez que não vamos precisar do índice, usamos _
    n = int(input("Introduz um número inteiro: "))
    numeros.append(n)

pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Números pares:", pares)
print("Números ímpares:", impares)
```

---

### Exercício 5 - Dicionário simples de pessoa

Cria um dicionário que represente uma pessoa com as chaves:

-   `"nome"`,
-   `"idade"`,
-   `"profissao"`.

Depois:

1. Mostra a informação da pessoa organizadamente (com `print` e f-strings).
2. Atualiza a idade (por exemplo, soma 1).
3. Adiciona uma chave `"cidade"`.
4. Remove a chave `"profissao"` com `pop` ou `del`.
5. Mostra o dicionário final.

> Resolução:

```python
pessoa = {
    "nome": "João Silva",
    "idade": 30,
    "profissao": "Programador"
}

print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Profissão: {pessoa['profissao']}") # 1
pessoa["idade"] += 1 # 2
pessoa["cidade"] = "Porto" # 3
pessoa.pop("profissao")  # ou: del pessoa["profissao"] # 4
print("Dicionário final:", pessoa) # 5
```

---

### Exercício 6 - Festival de comida (dicionário de dicionários)

Usa o seguinte dicionário de bancas num festival de comida:

```python
bancas = {
    "TacoTron":   {"vendas": 184, "preco_medio": 6.5, "avaliacao": 4.6},
    "Bao&Buns":   {"vendas": 149, "preco_medio": 7.0, "avaliacao": 4.8},
    "PokeWave":   {"vendas": 132, "preco_medio": 9.0, "avaliacao": 4.2},
    "PastelPower":{"vendas": 210, "preco_medio": 2.0, "avaliacao": 4.9},
    "VeggieVolt": {"vendas": 98,  "preco_medio": 8.5, "avaliacao": 4.4}
}
```

1. Diz qual o restaurante com **melhor avaliação**.
2. Calcula, para cada restaurante, quanto dinheiro fez (`vendas * preco_medio`).
3. Diz qual o restaurante que fez **mais dinheiro**.

> Resolução:

```python
bancas = {
    "TacoTron":   {"vendas": 184, "preco_medio": 6.5, "avaliacao": 4.6},
    "Bao&Buns":   {"vendas": 149, "preco_medio": 7.0, "avaliacao": 4.8},
    "PokeWave":   {"vendas": 132, "preco_medio": 9.0, "avaliacao":  4.2},
    "PastelPower":{"vendas": 210, "preco_medio": 2.0, "avaliacao": 4.9},
    "VeggieVolt": {"vendas": 98,  "preco_medio": 8.5, "avaliacao": 4.4}
}

# 1. Melhor avaliação
melhor_avaliacao = 0
restaurante_top = ""
for nome, info in bancas.items():
    if info["avaliacao"] > melhor_avaliacao:
        melhor_avaliacao = info["avaliacao"]
        restaurante_top = nome
print("Restaurante com melhor avaliação:", restaurante_top, "com", melhor_avaliacao)

# 2. Dinheiro feito por cada restaurante
dinheiro_feito = {}
for nome, info in bancas.items():
    total = info["vendas"] * info["preco_medio"]
    dinheiro_feito[nome] = total
    print(f"{nome} fez {total:.2f} euros.")

# 3. Restaurante que fez mais dinheiro
mais_dinheiro = 0
restaurante_rico = ""
for nome, total in dinheiro_feito.items():
    if total > mais_dinheiro:
        mais_dinheiro = total
        restaurante_rico = nome
print("Restaurante que fez mais dinheiro:", restaurante_rico, "com", mais_dinheiro)
```

---

### Exercício 7 - Matriz 3x3

Cria uma matriz 3x3 (lista de listas) com números inteiros à tua escolha.

1. Mostra a matriz linha a linha.
2. Adiciona uma nova linha à matriz.
3. Calcula a soma de todos os elementos da matriz (com ciclos aninhados).

> Resolução:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 1. Mostrar a matriz
print("Matriz:")
for linha in matriz:
    print(linha)

# 2. Adicionar nova linha
nova_linha = [10, 11, 12]
matriz.append(nova_linha)
print("Matriz atualizada:")
for linha in matriz:
    print(linha)

# 3. Soma de todos os elementos
soma_total = 0
for linha in matriz:
    for elemento in linha:
        soma_total += elemento
print("Soma de todos os elementos da matriz:", soma_total)
```

---

### Exercício 8 - Turmas e alunos (dicionário de listas)

Cria um dicionário de listas onde:

-   as chaves são nomes de turmas (por exemplo, `"10A"`, `"10B"`),
-   os valores são listas de nomes de alunos.

O programa deve:

1. Mostrar a lista de alunos de cada turma.
2. Adicionar uma nova turma com alguns alunos.
3. Mostrar o dicionário atualizado.

> Resolução:

```python
turmas = {
    "10A": ["Ana", "Bruno", "Carla"],
    "10B": ["David", "Eva", "Fábio"]
}

# 1. Mostrar lista de alunos por turma
for turma, alunos in turmas.items():
    print(f"Turma {turma}: {alunos}")

# 2. Adicionar nova turma
turmas["10C"] = ["Gabriela", "Helena", "Igor"]

# 3. Mostrar dicionário atualizado
print("Dicionário de turmas atualizado:")
for turma, alunos in turmas.items():
    print(f"Turma {turma}: {alunos}")
```

---

### Exercício 9 - Turmas com notas (estrutura aninhada)

Usa a estrutura de `turmas` apresentada na secção 4.2 (cada turma tem uma lista de alunos com notas e um professor).

O programa deve:

1. Mostrar, para cada turma, a lista de alunos com as respetivas notas.
2. Para cada turma, dizer quantos alunos têm pelo menos uma negativa.
3. Pedir um nome de aluno ao utilizador e indicar:
    - em que turma está,
    - quais as suas notas.

> Resolução:

```python
# Usa a estrutura de turmas do exemplo anterior
# 1. Mostrar alunos e notas por turma
for turma, info in turmas.items():
    print(f"Turma {turma}:")
    for aluno in info["alunos"]:
        print(f"  Aluno: {aluno['nome']}, Notas: {aluno['notas']}")
    print()
# 2. Contar alunos com negativas
for turma, info in turmas.items():
    count_negativas = 0
    for aluno in info["alunos"]:
        for nota in aluno["notas"].values():
            if nota < 10:
                count_negativas += 1
                break
    print(f"Turma {turma} tem {count_negativas} alunos com pelo menos uma negativa.")
# 3. Procurar aluno
nome_procurado = input("Nome do aluno a procurar: ")
encontrado = False
for turma, info in turmas.items():
    for aluno in info["alunos"]:
        if aluno["nome"].lower() == nome_procurado.lower():
            print(f"O aluno {nome_procurado} está na turma {turma} com notas: {aluno['notas']}")
            encontrado = True
            break
    if encontrado:
        break
if not encontrado:
    print("Aluno não encontrado.")
```

---

### Exercício 10 - Base de dados de livros (lista de dicionários)

Cria uma lista de dicionários, em que cada dicionário representa um livro com:

-   `"titulo"`,
-   `"autor"`,
-   `"ano"`,
-   `"genero"`.

O programa deve:

1. Mostrar todos os livros de forma organizada.
2. Pedir um título ao utilizador e, se o livro existir na lista, mostrar a sua informação completa.
3. Se não existir, indicar que o livro não foi encontrado.

> Resolução:

```python
livros = [
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "genero": "Distopia"},
    {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954, "genero": "Fantasia"},
    {"titulo": "Dom Quixote", "autor": "Miguel de Cervantes", "ano": 1605, "genero": "Clássico"}
]

# 1. Mostrar todos os livros
print("Lista de livros:")
for livro in livros:
    print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Género: {livro['genero']}")
# 2. Pedir título e procurar
titulo_procurado = input("Introduz o título do livro que procuras: ")
encontrado = False
for livro in livros:
    if livro["titulo"].lower() == titulo_procurado.lower():
        print("Livro encontrado:")
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Género: {livro['genero']}")
        encontrado = True
        break
if not encontrado:
    print("Livro não encontrado.")
```

---

### Exercício 11 - Temperaturas mensais

Usa duas listas:

-   `temperaturas` com 12 valores (um por mês),
-   `meses` com os nomes dos meses.

O programa deve:

1. Pedir ao utilizador o número de um mês (1–12) e mostrar a temperatura desse mês.
2. Calcular a temperatura média anual.
3. Indicar o mês mais quente e o mês mais frio:
    - Versão A: usando `max`, `min` e `index`.
    - Versão B (desafio): sem `max`/`min`, apenas com ciclos e comparações.

> Resolução:

```python
temperaturas = [15.5, 16.0, 18.2, 20.1, 22.5, 25.0, 27.3, 26.8, 24.0, 20.5, 17.8, 15.2]
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# 1. Pedir número do mês e mostrar temperatura
mes_procurado = int(input("Número do mês (1-12): "))
if 1 <= mes_procurado <= 12:
    indice = mes_procurado - 1
    print(f"A temperatura média em {meses[indice]} é {temperaturas[indice]} °C.")
else:
    print("Mês inválido.")

# 2. Calcular média anual
media_anual = sum(temperaturas) / len(temperaturas)
print(f"Temperatura média anual: {media_anual:.2f} °C")

# 3. Mês mais quente e mais frio (Versão A)
indice_quente = temperaturas.index(max(temperaturas))
indice_frio = temperaturas.index(min(temperaturas))
print(f"Mês mais quente: {meses[indice_quente]} ({temperaturas[indice_quente]} °C)")
print(f"Mês mais frio: {meses[indice_frio]} ({temperaturas[indice_frio]} °C)")
# Versão B (desafio)
maior_temp = temperaturas[0]
menor_temp = temperaturas[0]
indice_maior = 0
indice_menor = 0
for i in range(len(temperaturas)):
    if temperaturas[i] > maior_temp:
        maior_temp = temperaturas[i]
        indice_maior = i
    if temperaturas[i] < menor_temp:
        menor_temp = temperaturas[i]
        indice_menor = i
print(f"(Desafio) Mês mais quente: {meses[indice_maior]} ({maior_temp} °C)")
print(f"(Desafio) Mês mais frio: {meses[indice_menor]} ({menor_temp} °C)")
```

---

### Exercício 12 (Desafio) - Sistema simples de gestão de escola

Cria uma estrutura de dados (usando listas e dicionários) para representar:

-   várias turmas,
-   cada turma com uma lista de alunos,
-   cada aluno com um nome e dicionário de notas a várias disciplinas.

O programa deve permitir (por menu simples ou sequencialmente):

1. Mostrar todas as turmas e respetivos alunos.
2. Mostrar as notas de um aluno específico (pedido ao utilizador).
3. Para uma turma escolhida, indicar quantos alunos têm média ≥ 10.

Podes começar com dados fixos no código (sem `input()` para criar a estrutura) e focar-te em percorrer e analisar a estrutura.

> Resolução:

```python
turmas = {
    "10A": {
        "alunos": [
            {"nome": "Ana", "notas": {"Matemática": 18, "Português": 16}},
            {"nome": "Bruno", "notas": {"Matemática": 14, "Português": 15}},
            {"nome": "Carla", "notas": {"Matemática": 12, "Português": 14}}
        ],
        "professor": "Sr. Silva"
    },
    "10B": {
        "alunos": [
            {"nome": "David", "notas": {"Matemática": 10, "Português": 12}},
            {"nome": "Eva", "notas": {"Matemática": 9, "Português": 11}},
            {"nome": "Fábio", "notas": {"Matemática": 15, "Português": 14}}
        ],
        "professor": "Sra. Costa"
    }
}

# 1. Mostrar todas as turmas e alunos
for turma, info in turmas.items():
    print(f"Turma {turma}:")
    for aluno in info["alunos"]:
        print(f"  Aluno: {aluno['nome']}, Notas: {aluno['notas']}")
    print()

# 2. Mostrar notas de um aluno específico
nome_procurado = input("Nome do aluno a procurar: ")
encontrado = False
for turma, info in turmas.items():
    for aluno in info["alunos"]:
        if aluno["nome"].lower() == nome_procurado.lower():
            print(f"O aluno {nome_procurado} está na turma {turma} com notas: {aluno['notas']}")
            encontrado = True
            break
    if encontrado:
        break
if not encontrado:
    print("Aluno não encontrado.")

# 3. Contar alunos com média ≥ 10 numa turma escolhida
turma_escolhida = input("Escolhe uma turma (por exemplo, 10A): ")
if turma_escolhida in turmas:
    count_aprovados = 0
    for aluno in turmas[turma_escolhida]["alunos"]:
        soma_notas = sum(aluno["notas"].values())
        num_disciplinas = len(aluno["notas"])
        media = soma_notas / num_disciplinas
        if media >= 10:
            count_aprovados += 1
    print(f"Na turma {turma_escolhida}, {count_aprovados} alunos têm média ≥ 10.")
else:
    print("Turma não encontrada.")
```

---

## 6. Changelog

> Registo de alterações importantes a este ficheiro.

-   **2025-11-17 · v1.2**
    -   Adicionadas soluções aos exercícios todos.
-   **2025-11-17 · v1.1**
    -   TOC atualizado.
-   **2025-11-17 · v1.0**
    -   Criação inicial do documento.
    -   Secções: listas (criação, acesso, métodos, funções, padrões típicos, compreensões), dicionários (chaves/valores, métodos, iteração), estruturas aninhadas (lista de listas, dicionário de listas, dicionário de dicionários, lista de dicionários) e exemplos aplicados (temperaturas, turmas).
    -   Adicionados 12 exercícios graduais sobre listas, dicionários e estruturas aninhadas.

```

```
