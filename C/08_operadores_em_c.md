![Header](../Images/Header.png)

# C (10.º Ano) - 08 · Operadores em C

> **Objetivo deste ficheiro**  
> Dominar os operadores fundamentais da linguagem C e aplicá-los corretamente em expressões, decisões e cálculos.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. O que são operadores?](#1-o-que-são-operadores)
- [2. Operadores aritméticos](#2-operadores-aritméticos)
- [3. Operadores de atribuição](#3-operadores-de-atribuição)
- [4. Operadores relacionais](#4-operadores-relacionais)
- [5. Operadores lógicos](#5-operadores-lógicos)
- [6. Incremento e decremento](#6-incremento-e-decremento)
- [7. Precedência e associatividade](#7-precedência-e-associatividade)
- [8. Expressões compostas (boas práticas)](#8-expressões-compostas-boas-práticas)
- [9. Exemplo guiado](#9-exemplo-guiado)
- [10. Erros comuns](#10-erros-comuns)
- [11. Changelog](#11-changelog)

---

## 0. Como usar este módulo

1. Revê uma família de operadores de cada vez.
2. Testa expressões pequenas no compilador.
3. Usa parênteses para confirmar entendimento da precedência.

---

## 1. O que são operadores?

Operadores são símbolos que executam operações sobre valores (operandos).

Exemplos:

- `+` soma;
- `>` compara;
- `&&` combina condições.

---

## 2. Operadores aritméticos

Principais:

- `+` adição
- `-` subtração
- `*` multiplicação
- `/` divisão
- `%` resto da divisão inteira

Exemplo:

```c
int a = 10;
int b = 3;
printf("%d\n", a + b); // 13
printf("%d\n", a / b); // 3
printf("%d\n", a % b); // 1
```

Nota importante:

- `int / int` produz resultado inteiro.

---

## 3. Operadores de atribuição

- `=` atribuição simples
- `+=`, `-=`, `*=`, `/=`, `%=` atribuição composta

Exemplo:

```c
int x = 5;
x += 2; // x = 7
x *= 3; // x = 21
```

Usar atribuição composta melhora concisão, mas sem sacrificar clareza.

---

## 4. Operadores relacionais

Comparam valores e devolvem `0` (falso) ou `1` (verdadeiro):

- `==`, `!=`, `>`, `<`, `>=`, `<=`

Exemplo:

```c
int idade = 16;
printf("%d\n", idade >= 18); // 0
```

---

## 5. Operadores lógicos

- `&&` (E)
- `||` (OU)
- `!` (NÃO)

Exemplo:

```c
int idade = 20;
int tem_cartao = 1;
if (idade >= 18 && tem_cartao) {
    printf("Entrada permitida\n");
}
```

---

## 6. Incremento e decremento

- `++` incrementa 1
- `--` decrementa 1

Formas:

- pré-incremento: `++x`
- pós-incremento: `x++`

Diferença aparece quando usado dentro de expressões.

---

## 7. Precedência e associatividade

Sem parênteses, C segue regras de precedência.

Exemplo:

```c
int r = 2 + 3 * 4; // 14
```

Recomendação didática:

- usa parênteses quando houver dúvida;
- prioriza legibilidade sobre "código curto".

---

## 8. Expressões compostas (boas práticas)

Má prática:

```c
if (a + b * c - d / e > 10 && x || y && !z) { ... }
```

Melhor prática:

```c
int cond1 = (a + b * c - d / e > 10);
int cond2 = (x || y);
int cond3 = (!z);

if (cond1 && cond2 && cond3) {
    ...
}
```

---

## 9. Exemplo guiado

```c
#include <stdio.h>

int main(void) {
    int nota1, nota2;
    scanf("%d %d", &nota1, &nota2);

    float media = (nota1 + nota2) / 2.0f;
    int aprovado = (media >= 10.0f);

    printf("Media: %.2f\n", media);
    printf("Aprovado? %d\n", aprovado);

    return 0;
}
```

Conceitos usados:

- aritméticos (`+`, `/`);
- relacional (`>=`);
- atribuição.

---

## 10. Erros comuns

1. Confundir `=` com `==` em condições.
2. Esquecer divisão inteira.
3. Usar expressões muito compactas e difíceis de ler.
4. Abusar de `++` dentro de expressões complexas.
5. Não usar parênteses quando necessário.

---

## 11. Changelog

- **2026-02-23**: reescrita completa com detalhe pedagógico e exercícios sem resolução.

![Footer](../Images/Footer.png)
