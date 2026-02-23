# C (10.º Ano) - 03 · Algoritmos (Princípios)

> **Objetivo deste ficheiro**  
> Construir base sólida de algoritmia: correção, clareza, eficiência inicial e passagem de algoritmo para código C.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. Definição de algoritmo](#1-definição-de-algoritmo)
- [2. Propriedades de um bom algoritmo](#2-propriedades-de-um-bom-algoritmo)
- [3. Representações: texto, pseudocódigo e fluxograma](#3-representações-texto-pseudocódigo-e-fluxograma)
- [4. Construções fundamentais](#4-construções-fundamentais)
- [5. Correção de algoritmos (ideia prática)](#5-correção-de-algoritmos-ideia-prática)
- [6. Eficiência (introdução simples)](#6-eficiência-introdução-simples)
- [7. Exemplos guiados](#7-exemplos-guiados)
- [8. Da ideia ao C](#8-da-ideia-ao-c)
- [9. Erros comuns](#9-erros-comuns)
- [10. Exercícios (sem resolução)](#10-exercícios-sem-resolução)
- [11. Changelog](#11-changelog)

---

## 0. Como usar este módulo

1. Estuda primeiro "propriedades" e "construções".
2. Faz o pseudocódigo antes de codificar.
3. Testa os teus algoritmos com casos limite.

---

## 1. Definição de algoritmo

Algoritmo é uma sequência de passos finitos para resolver um problema.

Características:

- começa com entradas;
- aplica regras;
- termina com saídas.

---

## 2. Propriedades de um bom algoritmo

- **Correção**: devolve resultado certo.
- **Finitude**: termina sempre.
- **Precisão**: passos sem ambiguidade.
- **Generalidade**: funciona para vários casos.
- **Legibilidade**: outra pessoa entende.

---

## 3. Representações: texto, pseudocódigo e fluxograma

### Texto estruturado

Útil para explicar ideias rapidamente.

### Pseudocódigo

Não depende de linguagem específica; aproxima-se de código.

### Fluxograma

Mostra decisões e fluxo visualmente.

---

## 4. Construções fundamentais

Todo algoritmo básico usa:

- sequência;
- seleção (`if`);
- repetição (`for`, `while`).

Estas três estruturas permitem resolver grande parte dos problemas iniciais.

---

## 5. Correção de algoritmos (ideia prática)

Para verificar correção:

1. define claramente o objetivo;
2. cria exemplos pequenos;
3. acompanha passo a passo;
4. verifica se todos os caminhos estão cobertos.

---

## 6. Eficiência (introdução simples)

Dois algoritmos corretos podem ter custos diferentes.

Exemplo:

- procurar número numa lista não ordenada: pode exigir percorrer tudo;
- procurar em lista ordenada com técnica melhor: pode reduzir comparações.

Nesta fase, prioridade é **correção + clareza**; eficiência vem logo a seguir.

---

## 7. Exemplos guiados

### Exemplo A - Maior de 3 números

Pseudocódigo:

```text
ler a, b, c
maior <- a
se b > maior então maior <- b
se c > maior então maior <- c
escrever maior
```

### Exemplo B - Soma de 1 até n

```text
ler n
soma <- 0
para i de 1 até n
    soma <- soma + i
escrever soma
```

---

## 8. Da ideia ao C

Exemplo B em C:

```c
#include <stdio.h>

int main(void) {
    int n;
    int soma = 0;
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        soma += i;
    }

    printf("Soma = %d\n", soma);
    return 0;
}
```

Notas pedagógicas:

- variável acumuladora começa em 0;
- ciclo controla quantas vezes somar;
- atenção a limites (`<= n`).

---

## 9. Erros comuns

1. Algoritmo sem condição de paragem.
2. Confundir símbolo de atribuição com comparação.
3. Não inicializar variáveis acumuladoras.
4. Ignorar casos de entrada inválida.
5. Saltar pseudocódigo e ir direto ao C sem plano.

---

## 10. Exercícios (sem resolução)

### Exercício 1 - Definições

Escreve com as tuas palavras o que são: algoritmo, correção, finitude.

### Exercício 2 - Classificação

Para 10 exemplos dados por ti, indica se são sequência, seleção ou repetição.

### Exercício 3 - Pseudocódigo

Cria pseudocódigo para:

1. calcular área do retângulo;
2. verificar se número é par;
3. converter segundos em horas/minutos/segundos.

### Exercício 4 - Conversão para C

Implementa em C os 3 algoritmos do exercício 3.

### Exercício 5 - Máximo e mínimo

Escreve algoritmo para encontrar maior e menor de 5 valores.

### Exercício 6 - Acumuladores

Cria algoritmo para média de `n` números lidos ao utilizador.

### Exercício 7 - Contadores

Conta quantos números positivos, negativos e zeros foram inseridos.

### Exercício 8 - Validação

Melhora um algoritmo para rejeitar entradas fora do intervalo 0 a 20.

### Exercício 9 - Comparação de abordagens

Resolve o mesmo problema com `for` e com `while`, e compara clareza.

### Exercício 10 - Testes

Define 12 testes para um algoritmo de classificação de notas.

### Exercício 11 - Depuração

Recebes pseudocódigo com erro lógico.  
Identifica o erro e reescreve corretamente.

### Exercício 12 - Reflexão

Explica em que situações um algoritmo "parece certo" mas falha em casos limite.

---

## 11. Changelog

- **2026-02-23**: reescrita detalhada do módulo com foco em fundamentos e exercícios sem resolução.
