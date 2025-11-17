# Python (10.º Ano) - 05 · Algoritmos e Padrões de Programação

> **Objetivo deste ficheiro**  
> Deixar de ser apenas “truques de Python” e começar a pensar **como programador**:
>
> -   ler um problema em português,
> -   descobrir quais são os **dados de entrada**,
> -   decidir o que é o **processamento** (contagens, médias, filtragens, etc.),
> -   definir o que deve aparecer como **saída**,
> -   e transformar tudo isso em código com listas, dicionários e funções.

Ao longo deste documento:

-   As secções marcadas como **[ESSENCIAL]** são a base que deves dominar para testes e projetos.
-   As secções marcadas como **[EXTRA]** são para explorar quando já estiveres mais confortável.

---

## Índice

-   [0. Como atacar um problema de programação · [ESSENCIAL]](#0-como-atacar-um-problema-de-programa%C3%A7%C3%A3o--essencial)
-   [1. Padrões clássicos com listas · [ESSENCIAL]](#1-padr%C3%B5es-cl%C3%A1ssicos-com-listas--essencial)
-   [2. Padrões com dicionários · [ESSENCIAL]](#2-padr%C3%B5es-com-dicion%C3%A1rios--essencial)
-   [3. Juntar tudo em funções · [ESSENCIAL]](#3-juntar-tudo-em-fun%C3%A7%C3%B5es--essencial)
-   [4. Estratégia passo-a-passo num problema maior · [ESSENCIAL]](#4-estrat%C3%A9gia-passo-a-passo-num-problema-maior--essencial)
-   [5. Erros típicos e debugging básico · [ESSENCIAL]](#5-erros-t%C3%ADpicos-e-debugging-b%C3%A1sico--essencial)
-   [6. Exercícios - Algoritmos e Padrões de Programação](#6-exerc%C3%ADcios---algoritmos-e-padr%C3%B5es-de-programa%C3%A7%C3%A3o)
-   [7. Changelog](#7-changelog)

---

## 0. Como atacar um problema de programação · [ESSENCIAL]

Muitos erros aparecem porque se começa logo a escrever código, sem pensar.  
Uma abordagem mais segura:

### 0.1. Passo 1 - Ler o enunciado com calma

-   Sublinha ou destaca:
    -   o que é dado (**entrada**),
    -   o que é pedido (**saída**),
    -   pistas sobre o que tens de fazer no meio (**processamento**).

Exemplo de enunciado:

> “Pede ao utilizador as idades de 5 pessoas, calcula a média das idades e diz quantas são maiores ou iguais a 18.”

-   Entradas:
    -   5 idades (números inteiros).
-   Saída:
    -   idade média,
    -   número de pessoas ≥ 18.
-   Processamento:
    -   guardar idades algures (lista),
    -   somar idades para calcular média,
    -   contar quantas idades são ≥ 18.

### 0.2. Passo 2 - Fazer 2–3 exemplos à mão

Escolhe tu os dados e faz as contas no papel.

Exemplo:

-   Idades: 15, 20, 18, 30, 16
-   Soma: 15 + 20 + 18 + 30 + 16 = 99
-   Média: 99 / 5 = 19.8
-   Maiores ou iguais a 18: 20, 18, 30 → 3 pessoas

Já tens uma ideia do que o programa deve fazer.

### 0.3. Passo 3 - Escrever um plano em português (pseudocódigo)

Exemplo de plano:

1. Criar uma lista vazia para guardar as idades.
2. Repetir 5 vezes:
    - pedir uma idade ao utilizador,
    - converter para inteiro,
    - adicionar à lista.
3. Calcular a soma das idades.
4. Calcular a média.
5. Contar quantas idades são ≥ 18.
6. Mostrar a média e o número de maiores ou iguais a 18.

### 0.4. Passo 4 - Transformar o plano em código

Primeiro, sem funções (só para perceber a lógica).  
Depois, refatorar para funções (ver secção 4).

---

## 1. Padrões clássicos com listas · [ESSENCIAL]

Vamos ver **padrões de raciocínio** que aparecem muitas vezes.

### 1.1. Padrão “ler valores e construir lista”

Exemplo: ler 5 idades para uma lista.

```python
idades = []                      # lista vazia

for _ in range(5):               # repete 5 vezes
    idade = int(input("Idade: "))
    idades.append(idade)         # adiciona ao fim da lista

print("Idades:", idades)
```

Este padrão é muito frequente: começar com lista vazia e ir fazendo `append`.

---

### 1.2. Padrão de acumulação (somar valores)

Queremos somar todos os elementos de uma lista.

```python
idades = [15, 20, 18, 30, 16]

total = 0
for idade in idades:
    total += idade       # total = total + idade

media = total / len(idades)
print("Média:", media)
```

Este padrão (variável `total` que começa em 0 e vai acumulando) aparece em:

-   somatórios,
-   cálculos de média,
-   cálculo de totais de vendas, etc.

---

### 1.3. Padrão de contagem condicional

Contar quantos elementos cumprem uma certa condição.

```python
idades = [15, 20, 18, 30, 16]

maiores_ou_iguais_18 = 0
for idade in idades:
    if idade >= 18:
        maiores_ou_iguais_18 += 1

print("Pessoas com 18 ou mais anos:", maiores_ou_iguais_18)
```

Muda-se apenas a condição para contar:

-   negativos,
-   pares,
-   notas ≥ 10, etc.

---

### 1.4. Padrão de mínimo/máximo manual

Sem usar `min()` ou `max()`.

```python
idades = [15, 20, 18, 30, 16]

min_idade = idades[0]       # começa pelo primeiro
max_idade = idades[0]

for idade in idades:
    if idade < min_idade:
        min_idade = idade
    if idade > max_idade:
        max_idade = idade

print("Mínimo:", min_idade)
print("Máximo:", max_idade)
```

Este padrão é importante para quando **não** podemos usar funções prontas (em testes ou desafios).

---

### 1.5. Padrão de filtragem (criar nova lista)

Criar uma nova lista só com elementos que passam no “filtro”.

```python
idades = [15, 20, 18, 30, 16]

maiores_ou_iguais_18 = []          # nova lista
for idade in idades:
    if idade >= 18:
        maiores_ou_iguais_18.append(idade)

print("Idades ≥ 18:", maiores_ou_iguais_18)
```

Muitas vezes queremos manter a lista original e criar uma **versão filtrada**.

---

### 1.6. Padrão de transformação (mapear valores)

Criar uma nova lista com uma transformação aplicada a cada elemento.

```python
numeros = [1, 2, 3, 4]

quadrados = []
for n in numeros:
    quadrado = n ** 2
    quadrados.append(quadrado)

print("Originais:", numeros)
print("Quadrados:", quadrados)
```

Outros exemplos de transformação:

-   converter temperaturas de Celsius para Fahrenheit,
-   normalizar valores (ex.: dividir tudo pelo máximo),
-   converter strings para minúsculas.

---

## 2. Padrões com dicionários · [ESSENCIAL]

Dicionários são ótimos para simular **“pequenas bases de dados” em memória**.

### 2.1. Dicionário simples: chave → valor

Exemplo: pessoas e idades.

```python
idades = {
    "Ana": 16,
    "Bruno": 17,
    "Carla": 15
}

print(idades["Ana"])    # 16
```

---

### 2.2. Procurar uma chave

Verificar se uma pessoa está no dicionário.

```python
nome = input("Nome a procurar: ")

if nome in idades:
    print("Idade de", nome, "é", idades[nome])
else:
    print("Pessoa não encontrada.")
```

É muito comum o padrão:

```python
if chave in dicionario:
    # usar dicionario[chave]
else:
    # lidar com o caso em que a chave não existe
```

---

### 2.3. Contar coisas com dicionários

Contar quantas vezes cada palavra aparece numa lista:

```python
palavras = ["maçã", "banana", "maçã", "pera", "banana", "maçã"]

contagens = {}                         # dicionário vazio

for p in palavras:
    if p in contagens:
        contagens[p] += 1
    else:
        contagens[p] = 1

print(contagens)   # {'maçã': 3, 'banana': 2, 'pera': 1}
```

Isto é um padrão muito importante: dicionário como **mapa de frequências**.

---

### 2.4. Dicionário de listas

Turmas com listas de alunos.

```python
turmas = {
    "10A": ["Ana", "Bruno", "Carla"],
    "10B": ["David", "Eva", "Fábio"]
}

for turma, alunos in turmas.items():
    print(f"Turma {turma} tem {len(alunos)} alunos.")
```

Aqui combinamos:

-   dicionário (`turma` → lista),
-   função `len`,
-   ciclo `for` com `items()`.

---

## 3. Juntar tudo em funções · [ESSENCIAL]

Uma boa prática é separar:

-   **funções puras** (que recebem dados, calculam e devolvem com `return`);
-   a parte do programa que faz `input` e `print`.

### 3.1. Exemplo: média e número de maiores de idade

Primeiro, escrevemos a função para a **lógica**:

```python
def media_e_maiores_ou_iguais_18(idades):
    total = 0
    contagem_maiores = 0

    for idade in idades:
        total += idade
        if idade >= 18:
            contagem_maiores += 1

    media = total / len(idades)
    return media, contagem_maiores
```

Depois, no programa principal:

```python
def ler_idades(qtd):
    idades = []
    for _ in range(qtd):
        idade = int(input("Idade: "))
        idades.append(idade)
    return idades


if __name__ == "__main__":
    idades = ler_idades(5)   # input
    media, maiores = media_e_maiores_ou_iguais_18(idades)  # processamento
    print("Média das idades:", media)                      # output
    print("Maiores ou iguais a 18:", maiores)
```

Assim, se quisermos **testar** a função `media_e_maiores_ou_iguais_18`, podemos chamá-la com listas inventadas (sem `input`).

---

### 3.2. Exemplo: encontrar o mais velho

```python
def mais_velho(pessoas):
    '''
    Recebe um dicionário nome -> idade e devolve o nome da pessoa mais velha.
    '''
    # assumimos que o dicionário não está vazio
    nome_mais_velho = None
    idade_mais_velho = -1

    for nome, idade in pessoas.items():
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            nome_mais_velho = nome

    return nome_mais_velho
```

Programa principal:

```python
if __name__ == "__main__":
    pessoas = {
        "Ana": 16,
        "Bruno": 17,
        "Carla": 15
    }

    nome = mais_velho(pessoas)
    print("Pessoa mais velha:", nome)
```

---

## 4. Estratégia passo-a-passo num problema maior · [ESSENCIAL]

Vamos pegar num enunciado um pouco mais completo.

> “Numa turma, cada aluno tem um nome e notas a várias disciplinas.  
> Pretende-se:
>
> -   mostrar a média de cada aluno,
> -   indicar quantos alunos têm pelo menos uma negativa,
> -   indicar qual o aluno com melhor média.”

### 4.1. Modelar os dados

Podemos usar uma estrutura aninhada:

```python
turma = {
    "alunos": [
        {"nome": "Ana", "notas": {"Matemática": 18, "Português": 16}},
        {"nome": "Bruno", "notas": {"Matemática": 14, "Português": 15}},
        {"nome": "Carla", "notas": {"Matemática": 12, "Português": 9}}
    ]
}
```

### 4.2. Decompor em funções

Podemos definir funções como:

-   media_aluno(aluno) → devolve média das notas desse aluno;
-   contar_alunos_com_negativas(turma) → devolve quantos alunos têm pelo menos uma nota < 10;
-   melhor_aluno(turma) → devolve o nome do aluno com maior média.

### 4.3. Implementação gradual

1. Implementar e testar media_aluno com 1 aluno.
2. Depois, usar media_aluno dentro de melhor_aluno.
3. Por fim, escrever contar_alunos_com_negativas.

Exemplo de media_aluno:

```python
def media_aluno(aluno):
    notas = aluno["notas"].values()
    total = 0
    for nota in notas:
        total += nota
    return total / len(notas)
```

Exemplo de contar_alunos_com_negativas:

```python
def contar_alunos_com_negativas(turma):
    contador = 0
    for aluno in turma["alunos"]:
        for nota in aluno["notas"].values():
            if nota < 10:
                contador += 1
                break           # já sabemos que este aluno tem negativa
    return contador
```

---

## 5. Erros típicos e debugging básico · [ESSENCIAL]

Alguns erros muito comuns:

1. **Esquecer o return numa função**

    - Resultado: a função devolve None e a partir daí o programa começa a falhar.

2. **Misturar print com lógica**

    - Se uma função imprime em vez de devolver, não podes reutilizar o resultado noutro cálculo.

3. **Confundir = com ==**

    - = atribui valores;
    - == compara valores.

4. **Erros de intervalo em range (off-by-one)**

    - Lembrar: range(inicio, fim) vai até fim - 1.

5. **Alterar a variável errada em ciclos ou funções**
    - Exemplos:
        - esquecer i += 1 num while,
        - usar a lista errada num append.

### 5.1. Dicas de debugging

-   Imprime valores intermédios (por exemplo, dentro de ciclos) para ver como o programa está a pensar.
-   Testa funções com dados pequenos e fáceis de prever.
-   Usa assert para garantir que certas condições se verificam:

```python
def soma(a, b):
    return a + b

assert soma(2, 3) == 5
assert soma(-1, 1) == 0
```

Se um assert falhar, o Python lança um erro e isso ajuda a localizar o problema.

---

## 6. Exercícios - Algoritmos e Padrões de Programação

> Sugestão:
>
> -   faz primeiro os Exercícios 1–6;
> -   depois tenta 7–10;
> -   os 11 e 12 são um pouco mais desafiantes.

---

### Exercício 1 - Contagem de positivos, negativos e zeros

Pede ao utilizador n números (escolhe tu o valor de n, por exemplo 10) e:

1. Guarda-os numa lista.
2. Conta quantos são:
    - positivos,
    - negativos,
    - iguais a zero.
3. No fim, mostra as 3 contagens.

Tenta identificar no teu código os padrões de:

-   leitura para lista,
-   contagem condicional.

---

### Exercício 2 - Aprovados e reprovados

Cria uma função contar_aprovados_reprovados(notas) que recebe uma lista de notas (0–20) e:

-   devolve dois valores:
    -   número de aprovados (nota ≥ 10),
    -   número de reprovados (nota < 10).

No programa principal:

1. Cria uma lista com algumas notas (pode ser fixa ou pedida ao utilizador).
2. Chama a função e mostra o resultado.

---

### Exercício 3 - Mínimo e máximo manual

Escreve uma função min_max(lista_numeros) que:

-   recebe uma lista de números,
-   devolve um tuplo (minimo, maximo),
-   não usa min() nem max().

Testa com pelo menos 3 listas diferentes.

---

### Exercício 4 - Filtrar pares e ímpares

Escreve uma função separar_pares_impares(lista_numeros) que:

-   recebe uma lista de inteiros,
-   devolve duas listas:
    -   uma com os números pares,
    -   outra com os números ímpares.

No programa principal:

-   cria uma lista com números de 1 a 20,
-   chama a função e mostra as duas listas.

---

### Exercício 5 - Transformação: quadrados dos números

Escreve uma função quadrados(lista_numeros) que:

-   recebe uma lista de números,
-   devolve uma nova lista com o quadrado de cada número.

Testa:

-   quadrados([1, 2, 3, 4]) → [1, 4, 9, 16].

---

### Exercício 6 - Produtos e preços

Cria um dicionário precos em que:

-   as chaves são nomes de produtos (ex.: "pão", "leite", "sumo"),
-   os valores são os respetivos preços (floats).

Escreve uma função produto_mais_caro(precos) que:

-   recebe o dicionário,
-   devolve o nome do produto com maior preço,
-   não usa max() direto em precos.values() (faz o mínimo/máximo manual usando um ciclo).

---

### Exercício 7 - Idades e maioridade

Cria um dicionário idades (nome → idade) e escreve uma função estatisticas_idades(idades) que devolve:

-   a média das idades,
-   quantas pessoas são maiores ou iguais a 18.

No programa principal, mostra um relatório deste tipo:

```text
Média das idades: X
Maiores ou iguais a 18: Y
```

---

### Exercício 8 - Contar alunos por turma

Cria um dicionário turmas em que:

-   as chaves são nomes de turmas (ex.: "10A", "10B"),
-   os valores são listas com os nomes dos alunos.

Escreve uma função contar_alunos_por_turma(turmas) que:

-   recebe este dicionário,
-   devolve um novo dicionário com:
    -   as mesmas chaves,
    -   como valor, o número de alunos em cada turma.

No fim, mostra algo do género:

```text
Turma 10A -> 3 alunos
Turma 10B -> 4 alunos
```

---

### Exercício 9 - Reprovados por turma

Usa uma estrutura semelhante à de turma na secção 4 (com alunos e notas por disciplina) e escreve uma função:

reprovados_por_turma(turmas) que:

-   recebe um dicionário de turmas,
-   para cada turma, conta quantos alunos têm pelo menos uma negativa,
-   devolve um dicionário do tipo:
    -   "10A" -> número de alunos com negativas, etc.

Mostra depois um pequeno relatório por turma.

---

### Exercício 10 - Algoritmo em português (sem código primeiro)

Lê com atenção este enunciado:

> “Numa escola, cada aluno participa em várias atividades (clube de robótica, desporto, música, etc.).  
> Pretende-se criar um programa que:
>
> -   peça o nome de cada aluno e as atividades em que participa,
> -   permita ver quantos alunos estão em cada atividade,
> -   permita ver em que atividades participa um aluno específico.”

Sem escrever código, faz apenas:

1. Identificação de:
    - entradas,
    - processamento,
    - saídas.
2. Desenho de uma estrutura de dados possível (que listas e dicionários usarias?).
3. Plano em passos numerados (pseudocódigo) de como o programa poderia funcionar.

Só depois, se quiseres, tenta começar a programar.

---

### Exercício 11 (Desafio) - Contador de frequências de letras

Escreve uma função contar_letras(texto) que:

-   recebe uma string,
-   devolve um dicionário em que:
    -   as chaves são letras (ignorando espaços),
    -   os valores são as quantidades de vezes que cada letra aparece.

Exemplo:

-   "banana" → {'b': 1, 'a': 3, 'n': 2}

Dica: podes primeiro converter o texto para minúsculas e ignorar espaços.

---

### Exercício 12 (Desafio) - Refatorar com funções

Escolhe um dos programas que já fizeste (por exemplo, um que trabalhe com turmas, notas ou temperaturas) e:

1. Analisa o código atual.
2. Identifica partes repetidas e blocos lógicos (por exemplo, “calcular média”, “listar reprovados”).
3. Cria pelo menos 3 funções para organizar o código:
    - cada uma com um nome claro,
    - com return em vez de print (quando fizer sentido).
4. Testa o programa novamente e confirma que se comporta da mesma forma.

---

## 7. Changelog

> Registo de alterações a este ficheiro.

-   **2025-11-17 · v1.1**
    -   TOC atualizado.
-   **2025-11-17 · v1.0**
    -   Criação inicial do documento.
    -   Adicionadas secções sobre:
        -   estratégia para atacar problemas (entrada/processamento/saída e pseudocódigo),
        -   padrões clássicos com listas (acumulação, contagem, min/max, filtragem, transformação),
        -   padrões com dicionários (base de dados simples, contagem de frequências, dicionário de listas),
        -   junção de tudo em funções (exemplos com idades e turmas),
        -   erros típicos e dicas de debugging.
    -   Criados 12 exercícios graduais, incluindo desafios com dicionários e refatoração de código em funções.
