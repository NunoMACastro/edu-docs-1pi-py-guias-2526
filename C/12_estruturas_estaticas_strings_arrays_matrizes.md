# C (10.º Ano) - 12 · Estruturas de Dados Estáticas: Strings, Arrays e Matrizes

> **Objetivo deste ficheiro**  
> Trabalhar corretamente com estruturas estáticas em C, compreendendo memória, acesso e manipulação segura.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. O que significa "estático" neste contexto?](#1-o-que-significa-estático-neste-contexto)
- [2. Arrays unidimensionais](#2-arrays-unidimensionais)
- [3. Strings em C (`char[]`)](#3-strings-em-c-char)
- [4. Funções úteis para strings](#4-funções-úteis-para-strings)
- [5. Arrays multidimensionais (matrizes)](#5-arrays-multidimensionais-matrizes)
- [6. Percurso e manipulação](#6-percurso-e-manipulação)
- [7. Segurança em leitura de strings](#7-segurança-em-leitura-de-strings)
- [8. Exemplo guiado](#8-exemplo-guiado)
- [9. Erros comuns](#9-erros-comuns)
- [10. Exercícios (sem resolução)](#10-exercícios-sem-resolução)
- [11. Changelog](#11-changelog)

---

## 0. Como usar este módulo

1. Treina arrays antes de matrizes.
2. Pratica muito leitura segura de strings.
3. Desenha índices no papel para evitar erros.

---

## 1. O que significa "estático" neste contexto?

Estrutura estática tem tamanho definido no momento da declaração.

Exemplo:

```c
int notas[30];
```

Vantagens:

- simples de usar;
- acesso rápido por índice.

Limitação:

- tamanho fixo.

---

## 2. Arrays unidimensionais

Declaração:

```c
int v[5] = {10, 20, 30, 40, 50};
```

Acesso por índice:

- `v[0]` primeiro elemento;
- `v[4]` último em vetor de 5.

---

## 3. Strings em C (`char[]`)

String em C é array de `char` terminado por `\0`.

```c
char nome[20] = "Ana";
```

Capacidade deve considerar o terminador nulo.

---

## 4. Funções úteis para strings

Biblioteca: `<string.h>`

- `strlen` tamanho;
- `strcpy` copiar;
- `strcat` concatenar;
- `strcmp` comparar.

Usar com cuidado para não ultrapassar buffers.

---

## 5. Arrays multidimensionais (matrizes)

Exemplo 2x3:

```c
int m[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
```

Acesso: `m[linha][coluna]`.

---

## 6. Percurso e manipulação

Vetores:

```c
for (int i = 0; i < n; i++) {
    ...
}
```

Matrizes:

```c
for (int i = 0; i < linhas; i++) {
    for (int j = 0; j < colunas; j++) {
        ...
    }
}
```

---

## 7. Segurança em leitura de strings

Evita `gets` (insegura).

Preferir:

```c
fgets(nome, sizeof nome, stdin);
```

Depois podes remover `\n` final, se necessário.

---

## 8. Exemplo guiado

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char nomes[3][30];

    for (int i = 0; i < 3; i++) {
        printf("Nome %d: ", i + 1);
        fgets(nomes[i], sizeof nomes[i], stdin);
        nomes[i][strcspn(nomes[i], "\n")] = '\0';
    }

    printf("\nLista:\n");
    for (int i = 0; i < 3; i++) {
        printf("- %s\n", nomes[i]);
    }

    return 0;
}
```

---

## 9. Erros comuns

1. Aceder índice fora do limite.
2. Esquecer `\0` em strings.
3. Usar funções de string sem validar capacidade.
4. Confundir tamanho total com tamanho usado.
5. Leitura insegura de texto.

---

## 10. Exercícios (sem resolução)

### Exercício 1 - Vetor básico

Lê 10 inteiros para um vetor e imprime-os na ordem inversa.

### Exercício 2 - Estatísticas

Num vetor de 20 valores, calcula soma, média, máximo e mínimo.

### Exercício 3 - Pares e ímpares

Conta quantos elementos pares e ímpares existem no vetor.

### Exercício 4 - Pesquisa

Implementa pesquisa linear de um valor num array.

### Exercício 5 - Strings

Lê nome completo e imprime quantidade de caracteres.

### Exercício 6 - Comparação de strings

Lê duas palavras e indica se são iguais.

### Exercício 7 - Concatenação

Lê nome e apelido e constrói nome completo.

### Exercício 8 - Matriz 3x3

Lê matriz 3x3 e calcula soma da diagonal principal.

### Exercício 9 - Matriz e condição

Conta quantos valores de matriz 4x4 são maiores que 10.

### Exercício 10 - Ordenação simples

Ordena vetor de 10 elementos por método simples à tua escolha.

### Exercício 11 - Segurança

Reescreve programa de leitura de nomes para evitar overflow.

### Exercício 12 - Reflexão

Explica diferenças práticas entre arrays e estruturas dinâmicas.

---

## 11. Changelog

- **2026-02-23**: reescrita detalhada do módulo com foco pedagógico e exercícios sem resolução.
