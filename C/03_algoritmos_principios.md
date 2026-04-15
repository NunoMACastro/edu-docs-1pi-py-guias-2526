# C - 03 · Algoritmos (Princípios)

> **Objetivo deste ficheiro**  
> Construir base algorítmica sólida: formular, validar, comparar e implementar algoritmos em C com clareza e rigor.

---

## Índice

- [0. Como estudar este módulo](#0-como-estudar-este-módulo)
- [1. Resultados de aprendizagem](#1-resultados-de-aprendizagem)
- [2. O que é um algoritmo?](#2-o-que-é-um-algoritmo)
- [3. Propriedades de um bom algoritmo](#3-propriedades-de-um-bom-algoritmo)
- [4. Representações de algoritmos](#4-representações-de-algoritmos)
- [5. Construções fundamentais](#5-construções-fundamentais)
- [6. Correção algorítmica (visão prática)](#6-correção-algorítmica-visão-prática)
- [7. Rastreamento manual (trace)](#7-rastreamento-manual-trace)
- [8. Eficiência (introdução objetiva)](#8-eficiência-introdução-objetiva)
- [9. Padrões algorítmicos iniciais](#9-padrões-algorítmicos-iniciais)
- [10. Exemplo guiado A - Maior de 3 números](#10-exemplo-guiado-a---maior-de-3-números)
- [11. Exemplo guiado B - Soma de 1 até n](#11-exemplo-guiado-b---soma-de-1-até-n)
- [12. Exemplo guiado C - Contagem de positivos/negativos/zeros](#12-exemplo-guiado-c---contagem-de-positivosnegativoszeros)
- [13. Erros comuns e correções](#13-erros-comuns-e-correções)
- [14. Mini-laboratório de algoritmia](#14-mini-laboratório-de-algoritmia)
- [15. Rubrica de autoavaliação](#15-rubrica-de-autoavaliação)
- [16. Checklist de qualidade algorítmica](#16-checklist-de-qualidade-algorítmica)
- [17. Changelog](#17-changelog)

---

## 0. Como estudar este módulo

1. Lê propriedades e construções antes de ver os exemplos em C.
2. Para cada algoritmo, faz trace manual com dados pequenos.
3. Só valida algoritmo quando passar casos normal, limite e inválido.
4. Compara pelo menos duas soluções para o mesmo problema.

---

## 1. Resultados de aprendizagem

No final deste módulo deves conseguir:

- definir algoritmo com precisão técnica;
- avaliar correção, finitude e clareza de uma solução;
- representar algoritmos em texto, pseudocódigo e C;
- usar sequência, seleção e repetição corretamente;
- aplicar trace manual para detetar erros lógicos;
- analisar eficiência de forma introdutória;
- implementar algoritmos em C com validação básica.

---

## 2. O que é um algoritmo?

Algoritmo é uma sequência finita e não ambígua de passos para transformar entradas em saídas.

Elementos obrigatórios:

- entradas bem definidas;
- regras de processamento;
- saída observável;
- condição de paragem.

Sem paragem garantida, não há algoritmo útil.

---

## 3. Propriedades de um bom algoritmo

- **Correção**: produz resultado esperado para casos válidos.
- **Finitude**: termina após número finito de passos.
- **Precisão**: cada passo é claro e executável.
- **Generalidade**: funciona para múltiplas entradas do domínio.
- **Legibilidade**: outra pessoa consegue entender e manter.

Regra prática:

- algoritmo rápido mas errado não serve;
- algoritmo correto e claro é prioridade inicial.

---

## 4. Representações de algoritmos

### 4.1 Texto estruturado

Vantagem:

- rápido para explicar ideia.

Limitação:

- pode ficar ambíguo se mal escrito.

### 4.2 Pseudocódigo

Vantagem:

- aproxima-se da lógica de implementação;
- independente de linguagem.

### 4.3 Fluxograma

Vantagem:

- visualiza fluxo de decisão e repetição.

### 4.4 Código C

Vantagem:

- executável e testável.

Limitação:

- detalhe sintático pode esconder falhas de lógica se saltares etapas.

---

## 5. Construções fundamentais

Todo algoritmo inicial em C apoia-se em três estruturas:

1. sequência;
2. seleção (`if`, `else if`, `else`, `switch`);
3. repetição (`for`, `while`, `do while`).

Quase todos os problemas introdutórios podem ser resolvidos com esta base.

---

## 6. Correção algorítmica (visão prática)

Método operacional:

1. define objetivo com frase testável;
2. escolhe entradas de teste pequenas;
3. executa passo a passo no papel;
4. compara saída com esperado;
5. verifica caminhos alternativos (`if/else`, ciclos com 0 ou 1 iteração);
6. valida limites.

Exemplo de limite:

- soma de 1 até `n`: o que acontece quando `n = 0`?

---

## 7. Rastreamento manual (trace)

Trace = tabela de execução para acompanhar variáveis.

Estrutura típica:

| passo | i | soma | observação |
|---|---:|---:|---|
| inicial | - | 0 | antes do ciclo |
| 1 | 1 | 1 | soma += i |
| 2 | 2 | 3 | soma += i |

Porque fazer trace:

- deteta erros de lógica cedo;
- mostra exatamente onde variável assume valor inesperado.

---

## 8. Eficiência (introdução objetiva)

Pergunta de eficiência:

- quantas operações o algoritmo faz quando dados crescem?

Intuição inicial:

- um ciclo simples cresce com `n`;
- dois ciclos aninhados crescem muito mais rápido.

Exemplo comparativo:

- procurar valor em lista não ordenada: pode percorrer todos;
- se lista ordenada, certas estratégias reduzem comparações.

Numa fase inicial, prioridade recomendada:

1. correção;
2. clareza;
3. eficiência básica.

---

## 9. Padrões algorítmicos iniciais

Padrões que aparecem com frequência:

- acumulação (`soma += valor`);
- contagem (`contador++`);
- procura de máximo/mínimo;
- validação por intervalo;
- classificação por regras;
- varrimento de sequência.

Treinar padrões reduz bloqueios em novos problemas.

---

## 10. Exemplo guiado A - Maior de 3 números

### 10.1 Pseudocódigo

```text
ler a, b, c
maior <- a
se b > maior então
    maior <- b
fim-se
se c > maior então
    maior <- c
fim-se
escrever maior
```

### 10.2 C

```c
#include <stdio.h>

int main(void) {
    int a, b, c;
    int maior;

    printf("Introduz tres inteiros: ");
    scanf("%d %d %d", &a, &b, &c);

    maior = a;

    if (b > maior) {
        maior = b;
    }
    if (c > maior) {
        maior = c;
    }

    printf("Maior = %d\n", maior);
    return 0;
}
```

---

## 11. Exemplo guiado B - Soma de 1 até n

### 11.1 Pseudocódigo

```text
ler n
se n < 1 então
    escrever "n invalido"
    terminar
fim-se
soma <- 0
para i de 1 até n
    soma <- soma + i
fim-para
escrever soma
```

### 11.2 C

```c
#include <stdio.h>

int main(void) {
    int n;
    int soma = 0;

    printf("n: ");
    scanf("%d", &n);

    if (n < 1) {
        printf("n invalido\n");
        return 1;
    }

    for (int i = 1; i <= n; i++) {
        soma += i;
    }

    printf("Soma = %d\n", soma);
    return 0;
}
```

### 11.3 Casos de teste mínimos

- `n = 1` -> `1`
- `n = 5` -> `15`
- `n = 0` -> erro controlado

---

## 12. Exemplo guiado C - Contagem de positivos/negativos/zeros

Problema:

- ler 8 inteiros e contar quantos são positivos, negativos e zero.

```c
#include <stdio.h>

int main(void) {
    int valor;
    int positivos = 0;
    int negativos = 0;
    int zeros = 0;

    for (int i = 0; i < 8; i++) {
        printf("Valor %d: ", i + 1);
        scanf("%d", &valor);

        if (valor > 0) {
            positivos++;
        } else if (valor < 0) {
            negativos++;
        } else {
            zeros++;
        }
    }

    printf("Positivos: %d\n", positivos);
    printf("Negativos: %d\n", negativos);
    printf("Zeros: %d\n", zeros);

    return 0;
}
```

Padrões usados:

- repetição controlada;
- classificação por seleção;
- contadores.

---

## 13. Erros comuns e correções

1. esquecer inicializar acumuladores/contadores;
2. erro de limite (`<` em vez de `<=`, e vice-versa);
3. condição de paragem incorreta em `while`;
4. caminho sem `return` em função não-void;
5. confundir atribuição `=` com comparação `==`;
6. validar mal casos extremos;
7. não testar com dados negativos/zero.

Estratégia de correção:

- reduzir para caso pequeno;
- fazer trace;
- corrigir causa raiz;
- repetir testes.

---

## 14. Mini-laboratório de algoritmia

Objetivo: desenhar e implementar algoritmo robusto em 60 a 90 min.

Problema sugerido:

- "ler `n` notas (n entre 1 e 30), calcular média, maior, menor e percentagem de aprovados".

Passos:

1. definir entradas e validações;
2. escrever pseudocódigo completo;
3. preparar tabela de trace para 1 caso;
4. implementar em C;
5. criar 10 casos de teste;
6. corrigir falhas encontradas;
7. comparar legibilidade da versão inicial com final.

---

## 15. Rubrica de autoavaliação

Pontua de 1 a 5:

- transformo problema em algoritmo claro;
- uso corretamente sequência, seleção e repetição;
- faço trace para validar lógica;
- trato casos limite e inválidos;
- converto pseudocódigo para C sem perder lógica;
- identifico erros de limite;
- comparo soluções com critério técnico.

Interpretação:

- 7 a 16: base frágil;
- 17 a 27: base funcional;
- 28 a 35: base sólida.

---

## 16. Checklist de qualidade algorítmica

Antes de considerar algoritmo concluído:

- define entradas e saídas com precisão;
- tem condição de paragem clara;
- passa caso normal, limite e inválido;
- variáveis iniciadas corretamente;
- condições sem ambiguidade;
- saída coerente com objetivo;
- implementação C preserva algoritmo original.

---

## 17. Changelog

- **2026-04-12**: expansão completa do módulo com foco em correção, trace, eficiência inicial, laboratório e avaliação.
- **2026-02-23**: reescrita detalhada do módulo com foco em fundamentos.
