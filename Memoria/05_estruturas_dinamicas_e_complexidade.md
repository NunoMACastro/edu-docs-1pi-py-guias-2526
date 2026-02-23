# Memória (10.º Ano) - 05 · Estruturas Dinâmicas e Complexidade (Big-O)

> **Objetivo deste ficheiro**  
> Introduzir estruturas dinâmicas de dados e a noção de complexidade de forma conceptual, com foco em perceber "quando usar o quê" e "porque pode ficar lento".

---

**Pré-requisitos:** [`03_gestao_de_memoria_em_python_referencias_mutabilidade_gc.md`](03_gestao_de_memoria_em_python_referencias_mutabilidade_gc.md)

## Índice

- [0. Como usar este ficheiro](#0-como-usar-este-ficheiro)
- [1. Estruturas estáticas vs dinâmicas](#1-estruturas-estáticas-vs-dinâmicas)
- [2. Pilha (Stack)](#2-pilha-stack)
- [3. Fila (Queue)](#3-fila-queue)
- [4. Lista ligada (Linked List)](#4-lista-ligada-linked-list)
- [5. Árvore binária](#5-árvore-binária)
- [6. Dicionário (Hash Table, visão base)](#6-dicionário-hash-table-visão-base)
- [7. O que é complexidade?](#7-o-que-é-complexidade)
- [8. Big-O sem medo](#8-big-o-sem-medo)
- [9. Comparação simplificada de estruturas](#9-comparação-simplificada-de-estruturas)
- [10. Erros comuns (e correções)](#10-erros-comuns-e-correções)
- [11. Tabela resumo: pontos fortes, fracos e quando usar](#11-tabela-resumo-pontos-fortes-fracos-e-quando-usar)
- [12. Resumo final](#12-resumo-final)
- [13. Changelog](#13-changelog)

---

## 0. Como usar este ficheiro

Este ficheiro é teórico.  
O objetivo não é "decorar fórmulas", mas sim:

- perceber comportamento das estruturas;
- compreender impacto de escolhas no desempenho;
- desenvolver raciocínio para futuros exercícios/projetos.

---

## 1. Estruturas estáticas vs dinâmicas

### Estruturas estáticas (ideia)

Tamanho mais rígido/fixo no modelo clássico.

### Estruturas dinâmicas (ideia)

Podem crescer ou diminuir em execução, conforme necessidade.

### Porque usar dinâmicas?

- flexibilidade;
- melhor adaptação à quantidade de dados real;
- modelação mais natural de muitos problemas.

### Nota importante em Python

A `list` de Python já é uma estrutura dinâmica (implementada como array dinâmico).

Ou seja:

- pode crescer (`append`);
- pode diminuir (`pop`);
- mantém acesso por índice muito rápido em média.

Isto explica porque a `list` é tão usada.

---

## 2. Pilha (Stack)

Regra principal: **LIFO** (Last In, First Out).

> Nota: no Módulo 04 falámos de call stack/stack frames (execução). Aqui "pilha/stack" é a estrutura de dados. Mesma ideia LIFO, contextos diferentes.

Operações típicas:

- `push` (inserir no topo);
- `pop` (remover do topo);
- `peek/top` (ver topo sem remover).

### Exemplo do dia a dia

Pilha de pratos:

- último prato colocado é o primeiro a sair.

### Onde aparece em programação?

- chamada de funções (stack frames);
- operações de desfazer (undo);
- avaliação de expressões.

### Esquema (ASCII)

```text
Base                 Topo
[10] [20] [30] [40]
                 ^ push/pop/peek
```

### Exemplo de inserção (`push`)

```python
pilha = []
pilha.append("A")
pilha.append("B")
# Estado: ["A", "B"] (topo = "B")
```

### Exemplo de pesquisa

```python
pilha = ["A", "B", "C"]  # topo = "C"
alvo = "B"
encontrado = alvo in pilha  # pesquisa linear: O(n)
```

Nota: a pilha foi pensada para trabalhar no topo; pesquisar não é a operação principal.

---

## 3. Fila (Queue)

Regra principal: **FIFO** (First In, First Out).

Operações típicas:

- `enqueue` (entra no fim);
- `dequeue` (sai do início).

### Exemplo do dia a dia

Fila de supermercado:

- quem entra primeiro é atendido primeiro.

### Onde aparece em programação?

- agendamento de tarefas;
- sistemas de atendimento;
- algoritmos de pesquisa em largura (BFS).

### Esquema (ASCII)

```text
Frente                               Trás
  |                                    |
dequeue <- [A] <- [B] <- [C] <- enqueue
```

### Exemplo de inserção (`enqueue`)

```python
from collections import deque

fila = deque()
fila.append("Ana")
fila.append("Bruno")
# Estado: deque(["Ana", "Bruno"])
```

### Exemplo de pesquisa

```python
from collections import deque

fila = deque(["Ana", "Bruno", "Carla"])
alvo = "Bruno"
encontrado = alvo in fila  # pesquisa linear: O(n)
```

Nota: tal como na pilha, pesquisar não é a operação de foco da fila.

---

## 4. Lista ligada (Linked List)

Numa lista ligada, os elementos (nós) estão ligados por referências.

Cada nó costuma ter:

- valor;
- referência para próximo nó (`next`);
- (em lista dupla) referência para anterior (`prev`).

### Vantagem conceptual

Inserções/remoções em certos pontos podem ser eficientes sem mover todos os elementos.

### Desvantagem conceptual

Acesso direto por índice não é tão natural como em arrays/listas dinâmicas comuns.

### Esquema (ASCII)

```text
head
 |
 v
[10|*] -> [25|*] -> [40|None]
```

### Exemplo de inserção (no início)

```python
class No:
    def __init__(self, valor, next=None):
        self.valor = valor
        self.next = next

head = No(25, No(40))
head = No(10, head)  # inserção no início
```

### Exemplo de pesquisa

```python
alvo = 40
atual = head
encontrado = False

while atual is not None:
    if atual.valor == alvo:
        encontrado = True
        break
    atual = atual.next
```

---

## 5. Árvore binária

Estrutura hierárquica.

Cada nó (na versão binária):

- pode ter até dois filhos;
- normalmente chamados de filho esquerdo e filho direito.

### Vocabulário útil

- raiz (root);
- nó pai;
- nó filho;
- folha (nó sem filhos);
- subárvore.

### Aplicações

- organização hierárquica de dados;
- pesquisa;
- representação de expressões.

### Esquema (ASCII)

```text
        8
      /   \
     3    10
    / \     \
   1   6    14
```

### Exemplo de inserção de lista não ordenada (BST, step-by-step)

Regra da BST:

- valores menores vão para a esquerda;
- valores maiores vão para a direita.

Lista de entrada (não ordenada): `8, 3, 10, 1, 6, 14, 7`

**Passo 1: inserir 8 (raiz)**

```text
8
```

**Passo 2: inserir 3**

- 3 < 8 -> vai para a esquerda de 8.

```text
  8
 /
3
```

**Passo 3: inserir 10**

- 10 > 8 -> vai para a direita de 8.

```text
  8
 / \
3  10
```

**Passo 4: inserir 1**

- 1 < 8 -> ir para a esquerda;
- 1 < 3 -> fica à esquerda de 3.

```text
    8
   / \
  3  10
 /
1
```

**Passo 5: inserir 6**

- 6 < 8 -> ir para a esquerda;
- 6 > 3 -> fica à direita de 3.

```text
    8
   / \
  3  10
 / \
1   6
```

**Passo 6: inserir 14**

- 14 > 8 -> ir para a direita;
- 14 > 10 -> fica à direita de 10.

```text
    8
   / \
  3  10
 / \   \
1   6  14
```

**Passo 7: inserir 7**

- 7 < 8 -> ir para a esquerda;
- 7 > 3 -> ir para a direita;
- 7 > 6 -> fica à direita de 6.

```text
      8
    /   \
   3    10
  / \     \
 1   6    14
      \
       7
```

### Ordenação da árvore com BST (in-order)

Para obter os valores por ordem crescente numa BST, fazemos percurso **in-order**:

- visitar subárvore esquerda;
- visitar nó atual;
- visitar subárvore direita.

Aplicando à árvore acima, a ordem de visita fica:

`1, 3, 6, 7, 8, 10, 14`

Isto mostra a ideia central: inserir numa BST e depois fazer in-order produz os números ordenados.

### Exemplo de pesquisa (em BST)

Pesquisar `14`:

- comparar com `8` -> ir para a direita;
- comparar com `10` -> ir para a direita;
- encontrar `14`.

---

## 6. Dicionário (Hash Table, visão base)

Em Python, o `dict` é uma estrutura chave -> valor.

Exemplo:

```python
aluno = {"nome": "Ana", "nota": 17}
```

### Porque é poderoso?

Permite acesso muito rápido por chave em média.

### Atenção pedagógica

"Muito rápido em média" não significa "milagroso em todos os casos", mas no uso normal é excelente.

### Esquema (ASCII)

```text
chave --hash--> índice

"nome" --hash--> [bucket 5] -> "Ana"
"nota" --hash--> [bucket 2] -> 17
```

### Exemplo de inserção

```python
aluno = {}
aluno["nome"] = "Ana"
aluno["nota"] = 17
```

### Exemplo de pesquisa

```python
tem_nota = "nota" in aluno   # True
nota = aluno.get("nota")     # 17
```

---

## 7. O que é complexidade?

Complexidade mede como o custo de um algoritmo cresce quando aumentamos o tamanho da entrada (`n`).

Em geral, olhamos para dois custos:

- **tempo**: quantos passos/operações são necessários;
- **memória**: quanta memória extra é usada.

### O que é `n` na prática?

Depende do problema:

- numa lista, `n` = número de elementos;
- numa string, `n` = número de caracteres;
- numa árvore/grafo, `n` = número de nós.

### Pergunta pedagógica principal

Em vez de perguntar "quanto tempo em segundos?", pergunta:

"Se eu aumentar os dados de 1 000 para 10 000, o custo cresce pouco, muito, ou explode?"

### Exemplo rápido (pesquisa numa lista)

Para procurar um valor numa lista sem ordem:

- no melhor caso, encontra logo no início;
- no pior caso, percorre a lista toda;
- em média, percorre uma parte significativa.

Isto é comportamento **linear**: cresce com `n`.

---

## 8. Big-O

Big-O é a notação usada para expressar a complexidade de forma simplificada.
Big-O descreve a **tendência de crescimento** do custo quando `n` fica grande.

Não dá tempo exato; dá uma classe de crescimento. Ou seja, diz "cresce como `n`", "cresce como `n^2`", etc.

### Regras simples de leitura

- ignoramos constantes: `3n` e `n` ficam na mesma classe (`O(n)`);
- ignoramos termos menos relevantes: `n^2 + n` fica `O(n^2)`;
- focamos o termo que domina para entradas grandes.

### Formas comuns

- `O(1)`: custo aproximadamente constante;
- `O(log n)`: cresce devagar (ex.: dividir problema ao meio);
- `O(n)`: cresce proporcionalmente ao tamanho dos dados;
- `O(n log n)`: comum em ordenações eficientes;
- `O(n^2)`: compara muitos pares (cresce muito depressa).

### Tabela mental de crescimento (aproximada)

Valores maiores -> mais lento

Por exemplo, para n = 10, O(1) é 1 passo, O(log n) é cerca de 3 passos, O(n) é 10 passos, O(n log n) é cerca de 33 passos, e O(n^2) é 100 passos.

| Classe       | `n = 10` | `n = 100` | `n = 1000` |
| ------------ | -------- | --------- | ---------- |
| `O(1)`       | 1        | 1         | 1          |
| `O(log2 n)`  | ~3       | ~7        | ~10        |
| `O(n)`       | 10       | 100       | 1000       |
| `O(n log n)` | ~33      | ~664      | ~9966      |
| `O(n^2)`     | 100      | 10 000    | 1 000 000  |

### Ordenar uma lista: `sort` vs BST

Se tens uma lista não ordenada com `n` elementos:

- usar `sort` (Timsort, em Python) tem custo típico `O(n log n)` no pior/médio caso;
- construir uma BST simples com inserções sucessivas + percurso in-order:
    - média: `O(n log n)` (se árvore ficar razoavelmente equilibrada);
    - pior caso: `O(n^2)` (se árvore degradar para quase lista ligada).

Conclusão prática:

- para ordenar listas simples, `sort` é a escolha mais robusta;
- BST faz sentido quando também precisas de operações dinâmicas de pesquisa/inserção/remoção ao longo do tempo.

### Melhor, médio e pior caso

Para a mesma operação, podem existir cenários diferentes:

- **melhor caso**: situação mais favorável;
- **caso médio**: comportamento típico;
- **pior caso**: limite máximo de custo.

Em sala de aula, costuma-se usar muito o pior caso para garantir que o algoritmo não ultrapassa certo custo.

---

## 9. Comparação simplificada de estruturas

Custos típicos (visão prática, simplificada):

| Estrutura                        | Pesquisa                             | Inserção                                       | Remoção                                        |
| -------------------------------- | ------------------------------------ | ---------------------------------------------- | ---------------------------------------------- |
| Lista (array dinâmico)           | `O(n)` por valor / `O(1)` por índice | `O(1)` no fim (amortizado), `O(n)` no meio     | `O(1)` no fim, `O(n)` no meio                  |
| Pilha                            | `O(n)`                               | `O(1)` no topo                                 | `O(1)` no topo                                 |
| Fila (`deque`)                   | `O(n)`                               | `O(1)` no fim (`enqueue`)                      | `O(1)` no início (`dequeue`)                   |
| Lista ligada                     | `O(n)`                               | `O(1)` se já tens o ponto; `O(n)` para o achar | `O(1)` se já tens o ponto; `O(n)` para o achar |
| Árvore binária de pesquisa (BST) | `O(log n)` média (equilibrada)       | `O(log n)` média (equilibrada)                 | `O(log n)` média (equilibrada)                 |
| Dicionário (hash table)          | `O(1)` em média                      | `O(1)` em média                                | `O(1)` em média                                |

Notas importantes:

- BST pode degradar para `O(n)` se ficar muito desequilibrada;
- dicionário não mantém ordem "natural" de menor para maior;
- "rápido em média" não elimina a necessidade de escolher a estrutura certa para a tarefa.

### Estruturas compostas (aninhadas)

Aqui o custo costuma ser a soma dos passos em cada nível.

| Estrutura                 | Pesquisa                                                              | Inserção                                                       | Remoção                                                                |
| ------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Lista de listas           | `O(n*m)` por valor global / `O(1)` por acesso direto `dados[i][j]`    | `O(1)` no fim (amortizado) / no meio pode chegar a `O(n+m)`    | no fim `O(1)`; no meio pode chegar a `O(n+m)`                          |
| Lista de dicionários      | `O(n)` para achar item na lista + `O(1)` por chave no dicionário      | `O(1)` para `append` + `O(1)` para inserir chave no dicionário | `O(n)` para remover item da lista + `O(1)` para remover chave          |
| Dicionário de listas      | `O(1)` para achar chave + `O(m)` para procurar valor na lista interna | `O(1)` para chave + `O(1)` para `append` na lista interna      | `O(1)` para chave + `O(m)` para remover valor no meio da lista interna |
| Dicionário de dicionários | `O(1)` para chave externa + `O(1)` para chave interna                 | `O(1)` para chave externa + `O(1)` para inserir chave interna  | `O(1)` para chave externa + `O(1)` para remover chave interna          |

Legenda:

- `n`: tamanho da estrutura externa;
- `m`: tamanho médio da estrutura interna.

---

## 10. Erros comuns (e correções)

### Erro 1

"A estrutura mais rápida é sempre a melhor."

**Correção:** depende da operação principal (pesquisar? inserir? remover? manter ordem?).

### Erro 2

"Big-O dá o tempo exato."

**Correção:** Big-O dá tendência de crescimento, não segundos exatos.

### Erro 3

"Dicionário resolve qualquer problema."

**Correção:** excelente para chave-valor, mas não substitui pilhas, filas, árvores, etc.

---

## 11. Tabela resumo: pontos fortes, fracos e quando usar

| Estrutura                 | Pontos fortes                                                   | Pontos fracos                                                    | Quando usar                                                                |
| ------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Lista (array dinâmico)    | simples, versátil, acesso por índice rápido                     | inserir/remover no meio pode ser caro                            | sequência geral de dados, percursos, acesso por posição                    |
| Pilha                     | `push/pop` rápidos no topo, modelo LIFO claro                   | acesso restrito ao topo, pesquisa não é foco                     | undo/redo, histórico de navegação, call stack, backtracking                |
| Fila (`deque`)            | `enqueue/dequeue` rápidos nas extremidades, modelo FIFO natural | acesso aleatório e pesquisa global não são foco                  | filas de tarefas, atendimento, BFS                                         |
| Lista ligada              | inserção/remoção eficiente quando já tens o nó/ponto            | pesquisa e acesso por posição tendem a ser lentos                | cenários com muitas alterações locais e pouca necessidade de índice direto |
| BST (árvore de pesquisa)  | mantém ordem e permite pesquisa/inserção/remoção eficientes     | pode degradar se desequilibrada; implementação é mais complexa   | dados ordenáveis com operações dinâmicas frequentes                        |
| Dicionário (hash table)   | pesquisa/inserção/remoção muito rápidas em média por chave      | não é ideal para ordem natural por valor/chave e intervalos      | mapeamento chave-valor, indexação rápida, contagens                        |
| Lista de listas           | boa para dados tabulares simples e acesso `dados[i][j]`         | pesquisa global por valor pode custar `O(n*m)`                   | matrizes simples, grelhas, tabelas sem chave                               |
| Lista de dicionários      | cada item pode ter campos nomeados (estrutura flexível)         | achar um item pode exigir varrer lista (`O(n)`)                  | registos pequenos (ex.: alunos, produtos) com ordem/importância de lista   |
| Dicionário de listas      | acesso rápido por grupo/chave e coleção interna por chave       | operações na lista interna podem custar `O(m)`                   | agrupar muitos itens por categoria/chave                                   |
| Dicionário de dicionários | acesso direto por duas chaves, estrutura clara para hierarquias | consome mais memória e exige cuidado com chaves em vários níveis | dados hierárquicos (ex.: turma -> aluno -> campos)                         |

---

## 12. Resumo final

- Estruturas dinâmicas adaptam-se ao crescimento dos dados.
- Pilha usa LIFO; fila usa FIFO.
- Lista ligada usa nós e referências.
- Árvores modelam hierarquia.
- Dicionários são muito úteis para acesso por chave.
- Big-O ajuda a antecipar desempenho quando os dados crescem.

---

**A seguir:** [Rota de estudo recomendada](README.md#rota-de-estudo-recomendada)

---

## 13. Changelog

- **2026-02-23**: adicionados esquemas (ASCII), exemplos de inserção/pesquisa, passo a passo de inserção de lista não ordenada em BST, ordenação in-order, reforço pedagógico da complexidade, comparação `sort` vs BST, tabela de estruturas compostas e tabela-resumo de utilização.
- **2026-02-04**: versão inicial do módulo 05.
