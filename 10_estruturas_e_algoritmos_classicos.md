# Python (10.º Ano) - 10 · Estruturas e Algoritmos Clássicos

> **Objetivo deste ficheiro**  
> Introduzir pesquisa linear, ordenação básica (bubble e selection) e uma noção simples de eficiência.

---

## 1) O que são algoritmos e porquê estudar?

Um **algoritmo** é um conjunto de passos claros para resolver um problema.  
Exemplos do dia a dia:

-   receita de um bolo (passos na ordem certa);
-   instrucoes para montar um movel;
-   lista de regras para decidir algo.

Na programacao, um algoritmo diz **como** encontrar uma resposta, não apenas **qual** é a resposta.

---

## 2) Pesquisa linear (linear search)

### 2.1 Ideia principal

A **pesquisa linear** percorre uma lista do inicio ao fim, item a item, ate encontrar o valor desejado.

-   se encontrar, termina;
-   se nao encontrar, chega ao fim.

### 2.2 Exemplo simples

```python
def pesquisa_linear(valores, alvo):
    for item in valores:
        if item == alvo:
            return True
    return False

nums = [4, 7, 1, 9, 3]
print(pesquisa_linear(nums, 9))   # True
print(pesquisa_linear(nums, 10))  # False
```

### 2.3 Exemplo com indice

```python
def pesquisa_linear_indice(valores, alvo):
    for i in range(len(valores)):
        if valores[i] == alvo:
            return i
    return -1

nomes = ["Ana", "Bruno", "Carla"]
print(pesquisa_linear_indice(nomes, "Carla"))  # 2
print(pesquisa_linear_indice(nomes, "Duarte")) # -1
```

---

## 3) Ordenacao basica

Ordenar uma lista significa colocar os elementos numa **ordem** (crescente ou decrescente).

Aqui vamos ver duas ordenacoes classicas:

-   **Bubble Sort**
-   **Selection Sort**

Estas ordenacoes nao sao as mais rapidas, mas sao **simples** e boas para aprender.

---

## 4) Bubble Sort (ordenacao por bolha)

### 4.1 Ideia principal

Percorremos a lista varias vezes e, em cada passagem, **trocamos** elementos adjacentes se estiverem fora de ordem.

A cada passagem, o maior elemento "sobe" para o fim.

### 4.2 Exemplo passo a passo (lista pequena)

Lista inicial: `[5, 2, 4]`

-   Compara 5 e 2 -> troca: `[2, 5, 4]`
-   Compara 5 e 4 -> troca: `[2, 4, 5]`

Agora o maior (5) ja esta no fim.  
Fazemos outra passagem para confirmar a ordem.

### 4.3 Implementacao

```python
def bubble_sort(valores):
    n = len(valores)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if valores[j] > valores[j + 1]:
                valores[j], valores[j + 1] = valores[j + 1], valores[j]

nums = [5, 1, 4, 2, 8]
bubble_sort(nums)
print(nums)  # [1, 2, 4, 5, 8]
```

### 4.4 Versao com detecao de trocas

Se numa passagem nao houver trocas, a lista ja esta ordenada e podemos parar.

```python
def bubble_sort_otimizado(valores):
    n = len(valores)
    for i in range(n):
        houve_troca = False
        for j in range(0, n - 1 - i):
            if valores[j] > valores[j + 1]:
                valores[j], valores[j + 1] = valores[j + 1], valores[j]
                houve_troca = True
        if not houve_troca:
            break
```

---

## 5) Selection Sort (ordenacao por selecao)

### 5.1 Ideia principal

Em cada passo, encontramos o **menor** elemento da parte nao ordenada e colocamo-lo na posicao certa.

### 5.2 Exemplo passo a passo (lista pequena)

Lista inicial: `[4, 2, 7, 1]`

-   menor = 1 -> troca com o primeiro elemento  
    lista fica `[1, 2, 7, 4]`
-   agora olhamos para o resto `[2, 7, 4]`  
    menor = 2 -> ja esta na posicao certa
-   ultimo passo: entre `[7, 4]`, menor = 4 -> troca  
    lista final `[1, 2, 4, 7]`

### 5.3 Implementacao

```python
def selection_sort(valores):
    n = len(valores)
    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if valores[j] < valores[indice_min]:
                indice_min = j
        valores[i], valores[indice_min] = valores[indice_min], valores[i]

nums = [4, 2, 7, 1]
selection_sort(nums)
print(nums)  # [1, 2, 4, 7]
```

---

## 6) Comparar pesquisa linear e ordenacao

### Pesquisa linear

-   passa pela lista uma vez;
-   se o alvo estiver no fim, ve todos os elementos;
-   se estiver no inicio, termina logo.

### Ordenacao

-   faz muitas comparacoes e trocas;
-   mesmo com listas pequenas, ja e um pouco mais pesado.

---

## 7) Noção simples de eficiencia

Quando temos **poucos dados**, quase tudo funciona bem.  
Quando temos **muitos dados**, a escolha do algoritmo faz muita diferenca.

### Ideia simples:

-   pesquisar 1 elemento em 10 itens -> rapido
-   pesquisar 1 elemento em 1 000 000 itens -> pode demorar

Se um algoritmo faz 100 000 passos e outro faz 10 000, o segundo e mais eficiente.

Nao precisamos de formulas complicadas agora, basta perceber que:

-   **mais passos = mais tempo**;
-   ordenar uma lista costuma ser mais pesado do que apenas procurar um valor.

---

## 8) Quando usar cada coisa

-   **Pesquisa linear**: quando a lista nao esta ordenada e e pequena ou media.
-   **Ordenacao basica**: boa para aprender e para listas pequenas.
-   Para listas grandes, existem algoritmos mais rapidos (veremos mais tarde).

---

## 8.1) Porque aprender isto se existe `sort()`?

E uma pergunta excelente e muito comum. A resposta curta e: **para perceberes o que acontece por tras do `sort()` e para ganhares ferramentas de raciocinio**. Aqui vai a explicacao por partes:

### 1) `sort()` existe, mas nao e magico

O `sort()` ordena porque **usa um algoritmo de ordenacao por dentro**. Esse algoritmo foi criado, testado e escolhido por ser eficiente na maioria dos casos. Se nao souberes o que e um algoritmo de ordenacao, vais tratar o `sort()` como uma \"caixa preta\".

Saber o basico permite:

- entender porque ordenar custa tempo;
- perceber porque listas grandes demoram mais;
- distinguir quando faz sentido ordenar e quando nao.

### 2) Aprender algoritmos treina o raciocinio

Bubble sort e selection sort nao sao ensinados por serem os melhores.  
Sao ensinados porque sao **simples** e mostram ideias fundamentais:

- comparar valores;
- decidir quando trocar;
- repetir passos ate estar ordenado;
- medir quantos passos foram precisos.

Esse raciocinio vai ser usado em muitos problemas diferentes, mesmo que nunca mais uses bubble sort numa aplicacao real.

### 3) Nem sempre podes usar `sort()`

Em alguns exercicios e projetos, o objetivo **e aprender** e nao apenas chegar ao resultado.  
Se usares `sort()` sem perceber, estas a \"saltar\" a aprendizagem.

Tambem ha situacoes em que tens de:

- ordenar por regras especiais (por exemplo, mais novo primeiro, depois alfabetico);
- ordenar partes especificas de uma lista;
- explicar o processo passo a passo.

Sem conhecer o algoritmo, fica dificil adaptar.

### 4) O algoritmo certo faz diferenca

Imagina duas formas de ordenar 10 000 numeros:

- uma faz cerca de 1 000 000 comparacoes;
- outra faz apenas 100 000.

A segunda e muito mais rapida.  
Saber que existem algoritmos diferentes ajuda-te a perceber **porque algumas solucoes sao lentas**.

### 5) No futuro vais estudar algoritmos melhores

Mais tarde, vais conhecer algoritmos como **merge sort** ou **quick sort**.  
Para compreender esses algoritmos, precisas destas bases:

- comparacao e troca;
- percorrer a lista;
- dividir problemas;
- analisar eficiencia.

### Em resumo

- `sort()` e excelente e vais usa-lo muitas vezes.
- Aprender algoritmos classicos serve para entender **como** o `sort()` funciona.
- Isto melhora o teu raciocinio e prepara-te para problemas mais complexos.

---

## 9) Exercicios

### Exercício 1 - Pesquisa linear simples

Cria uma funcao `existe(lista, alvo)` que devolve `True` se o alvo estiver na lista.

---

### Exercício 2 - Pesquisa com indice

Cria uma funcao `indice(lista, alvo)` que devolve o indice do alvo ou `-1` se nao existir.

---

### Exercício 3 - Bubble Sort

Cria uma funcao `ordenar_bubble(lista)` que ordena a lista de forma crescente.

---

### Exercício 4 - Selection Sort

Cria uma funcao `ordenar_selection(lista)` que ordena a lista de forma crescente.

---

### Exercício 5 - Comparar metodos

Dada a lista:

```
[9, 1, 7, 3, 5]
```

1. Ordena com **bubble sort**.
2. Ordena com **selection sort**.
3. Confirma que o resultado e igual.

---

### Exercício 6 - Pesquisa antes e depois da ordenacao

1. Procura o numero 7 numa lista nao ordenada com pesquisa linear.
2. Ordena a lista.
3. Procura de novo e compara o numero de passos (podes usar um contador).

---

### Exercício 7 - Ordenacao decrescente

Adapta o **bubble sort** para ordenar de forma decrescente.

---

### Exercício 8 - Ordenar nomes

Cria uma lista de nomes e ordena-a usando **selection sort**.

---

### Exercício 9 - Pesquisa por nome (ignorar maiusculas)

1. Cria uma lista com nomes.
2. Pede um nome ao utilizador.
3. Pesquisa na lista ignorando maiusculas/minusculas.

Dica: usa `nome.lower()`.

---

### Exercício 10 - Desafio simples

Cria um programa que:

-   pede 5 numeros ao utilizador e guarda numa lista;
-   ordena a lista com **bubble sort**;
-   mostra a lista ordenada.

---

## 10) Changelog

-   `2025-02-XX` · Criacao inicial do ficheiro com pesquisa linear, bubble/selection sort e eficiencia basica.
