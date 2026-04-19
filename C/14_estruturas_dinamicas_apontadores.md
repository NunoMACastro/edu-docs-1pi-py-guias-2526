# C (10.º Ano) - 14 · Estruturas de Dados Dinâmicas: Apontadores, Acesso e Manipulação

> **Objetivo deste ficheiro**  
> Compreender profundamente apontadores e alocação dinâmica em C, com foco em segurança e raciocínio de memória.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. O que é um apontador?](#1-o-que-é-um-apontador)
- [2. Endereço e desreferenciação](#2-endereço-e-desreferenciação)
- [3. Apontadores e arrays](#3-apontadores-e-arrays)
- [4. Alocação dinâmica: `malloc`, `calloc`, `realloc`, `free`](#4-alocação-dinâmica-malloc-calloc-realloc-free)
- [5. Ciclo de vida da memória dinâmica](#5-ciclo-de-vida-da-memória-dinâmica)
- [6. Ponteiros para `struct`](#6-ponteiros-para-struct)
- [7. Introdução a lista ligada](#7-introdução-a-lista-ligada)
- [8. Segurança e boas práticas](#8-segurança-e-boas-práticas)
- [9. Exemplo guiado](#9-exemplo-guiado)
- [10. Erros comuns graves](#10-erros-comuns-graves)
- [11. Changelog](#11-changelog)

---

## 0. Como usar este módulo

1. Revê bem `&` e `*` antes de alocação dinâmica.
2. Desenha memória no papel (endereços e valores).
3. Nunca avances sem entender quando usar `free`.

---

## 1. O que é um apontador?

Apontador é variável que guarda endereço de memória.

```c
int x = 10;
int *p = &x;
```

- `p` guarda endereço de `x`.
- `*p` acede ao valor guardado em `x`.

---

## 2. Endereço e desreferenciação

Operadores:

- `&` obtém endereço;
- `*` desreferencia (acede ao conteúdo).

Exemplo:

```c
int v = 5;
int *p = &v;
printf("%d\n", *p); // 5
```

---

## 3. Apontadores e arrays

Nome de array comporta-se como ponteiro para primeiro elemento.

```c
int a[3] = {10, 20, 30};
int *p = a;
printf("%d\n", p[1]); // 20
```

---

## 4. Alocação dinâmica: `malloc`, `calloc`, `realloc`, `free`

- `malloc`: aloca sem inicializar.
- `calloc`: aloca e inicializa com zero.
- `realloc`: redimensiona bloco.
- `free`: liberta memória.

Exemplo:

```c
int *v = malloc(n * sizeof(int));
if (v == NULL) {
    // tratar erro
}
```

---

## 5. Ciclo de vida da memória dinâmica

Fluxo correto:

1. alocar;
2. verificar `NULL`;
3. usar;
4. libertar com `free`.

Se esqueceres `free`, ocorre fuga de memória (leak).

---

## 6. Ponteiros para `struct`

```c
typedef struct {
    int id;
} Item;

Item *p = malloc(sizeof(Item));
p->id = 100;
free(p);
```

---

## 7. Introdução a lista ligada

Nó com valor e ponteiro para próximo nó.

```c
typedef struct No {
    int valor;
    struct No *proximo;
} No;
```

Estrutura dinâmica cresce conforme necessidade.

---

## 8. Segurança e boas práticas

- inicializa ponteiros com `NULL`;
- verifica resultado de alocação;
- após `free`, define ponteiro para `NULL`;
- evita dupla libertação (`double free`);
- evita uso após libertar (`use-after-free`).

---

## 9. Exemplo guiado

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int *v = malloc(n * sizeof(int));
    if (v == NULL) {
        printf("Falha de memoria\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        v[i] = i + 1;
    }

    for (int i = 0; i < n; i++) {
        printf("%d ", v[i]);
    }
    printf("\n");

    free(v);
    v = NULL;
    return 0;
}
```

---

## 10. Erros comuns graves

1. Usar ponteiro não inicializado.
2. Não verificar `malloc`.
3. Esquecer `free`.
4. `free` duas vezes no mesmo ponteiro.
5. Aceder memória fora do bloco alocado.

---

## 11. Changelog

- **2026-02-23**: reescrita completa com explicação detalhada e exercícios sem resolução.
