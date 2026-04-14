# C (10.º Ano) - 06 · Linguagem Estruturada em C

> **Objetivo deste ficheiro**  
> Entender os conceitos centrais da programação estruturada e a anatomia de um programa em C.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. O que é programação estruturada?](#1-o-que-é-programação-estruturada)
- [2. Características da linguagem C](#2-características-da-linguagem-c)
- [3. Estrutura mínima de um programa C](#3-estrutura-mínima-de-um-programa-c)
- [4. Diretivas, funções e blocos](#4-diretivas-funções-e-blocos)
- [5. Sequência, seleção e repetição](#5-sequência-seleção-e-repetição)
- [6. Legibilidade e indentação](#6-legibilidade-e-indentação)
- [7. Exemplo guiado de programa estruturado](#7-exemplo-guiado-de-programa-estruturado)
- [8. Erros comuns](#8-erros-comuns)
- [9. Changelog](#10-changelog)

---

## 0. Como usar este módulo

1. Lê a estrutura mínima e escreve-a de memória.
2. Compara programas "confusos" e "estruturados".
3. Pratica decompor programa em funções pequenas.

---

## 1. O que é programação estruturada?

Paradigma baseado em três blocos de controlo:

- sequência;
- seleção;
- repetição.

Objetivo: código previsível, organizado e fácil de manter.

---

## 2. Características da linguagem C

- linguagem compilada;
- próxima do hardware;
- eficiente e amplamente usada;
- exige cuidado com memória e tipos.

Para iniciantes, C ensina disciplina técnica forte.

---

## 3. Estrutura mínima de um programa C

```c
#include <stdio.h>

int main(void) {
    printf("Ola, mundo!\n");
    return 0;
}
```

Partes:

- `#include <stdio.h>`: biblioteca de entrada/saída;
- `int main(void)`: ponto de entrada;
- `{ ... }`: bloco da função;
- `return 0`: termina com sucesso.

---

## 4. Diretivas, funções e blocos

### Diretivas de pré-processador

Ex.: `#include`, `#define`.

### Funções

Permitem modularizar lógica.

### Blocos

Código entre `{` e `}`; define escopo de variáveis.

---

## 5. Sequência, seleção e repetição

### Sequência

Instruções executadas por ordem.

### Seleção

`if/else` e `switch` para decisões.

### Repetição

`for`, `while`, `do while` para repetir ações.

---

## 6. Legibilidade e indentação

Regras práticas:

- 4 espaços por nível;
- uma instrução por linha (quando possível);
- nomes claros (`total_notas`, não `x1`);
- evitar funções demasiado longas.

Código legível é parte da qualidade do software.

---

## 7. Exemplo guiado de programa estruturado

```c
#include <stdio.h>

int ler_numero(void) {
    int n;
    printf("Numero: ");
    scanf("%d", &n);
    return n;
}

int quadrado(int x) {
    return x * x;
}

int main(void) {
    int valor = ler_numero();
    int resultado = quadrado(valor);
    printf("Quadrado: %d\n", resultado);
    return 0;
}
```

O que este exemplo ensina:

- função para entrada (`ler_numero`);
- função de processamento (`quadrado`);
- `main` simples e clara.

---

## 8. Erros comuns

1. Misturar tudo na `main`.
2. Falta de chavetas em blocos complexos.
3. Indentação inconsistente.
4. Nomes sem significado.
5. Código duplicado em vez de função.

---

## 9. Changelog

- **2026-02-23**: reescrita completa com explicação detalhada e exercícios sem resolução.
