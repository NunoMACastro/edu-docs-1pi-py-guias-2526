# C (10.º Ano) - 17 · Exceções e Tratamento de Erros em C

> **Objetivo deste ficheiro**  
> Aprender a tratar erros em C de forma profissional, mesmo sem mecanismo nativo de exceções como `try/catch`.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. Nota essencial: C não tem exceções padrão](#1-nota-essencial-c-não-tem-exceções-padrão)
- [2. Estratégias reais de tratamento de erros](#2-estratégias-reais-de-tratamento-de-erros)
- [3. Códigos de retorno](#3-códigos-de-retorno)
- [4. `errno` e `perror`](#4-errno-e-perror)
- [5. Validação de entrada](#5-validação-de-entrada)
- [6. Falhas de memória e recursos](#6-falhas-de-memória-e-recursos)
- [7. Propagação de erros entre funções](#7-propagação-de-erros-entre-funções)
- [8. Exemplo guiado](#8-exemplo-guiado)
- [9. Boas práticas de robustez](#9-boas-práticas-de-robustez)
- [10. Erros comuns](#10-erros-comuns)
- [11. Exercícios (sem resolução)](#11-exercícios-sem-resolução)
- [12. Changelog](#12-changelog)

---

## 0. Como usar este módulo

1. Foca em códigos de retorno e validações.
2. Treina casos de erro de propósito.
3. Cria hábito de mensagens claras de diagnóstico.

---

## 1. Nota essencial: C não tem exceções padrão

Não existe, na linguagem C padrão, mecanismo nativo como:

- `try`
- `catch`
- `throw`

Por isso o programador deve desenhar caminho de erro explicitamente.

---

## 2. Estratégias reais de tratamento de erros

- retornar `0/1` ou códigos específicos;
- validar argumentos na entrada das funções;
- verificar retorno de funções da biblioteca (`fopen`, `malloc`, `scanf`);
- registar mensagens de erro.

---

## 3. Códigos de retorno

Convenção comum:

- `0` -> sucesso
- diferente de `0` -> erro

Exemplo:

```c
int dividir(int a, int b, int *out) {
    if (b == 0) return 1;
    *out = a / b;
    return 0;
}
```

---

## 4. `errno` e `perror`

Quando funções do sistema falham, `errno` ajuda diagnóstico.

```c
FILE *f = fopen("dados.txt", "r");
if (f == NULL) {
    perror("Falha ao abrir ficheiro");
}
```

---

## 5. Validação de entrada

Utilizador pode inserir dados inválidos.

Exemplos de validação:

- intervalo de nota 0-20;
- número de elementos positivo;
- string não vazia.

---

## 6. Falhas de memória e recursos

Sempre verificar:

- `malloc` / `calloc` / `realloc` retornaram `NULL`?
- ficheiro abriu corretamente?
- ponteiros e descritores foram libertados/fechados?

---

## 7. Propagação de erros entre funções

Função interna deteta erro -> devolve código -> chamador decide ação.

Isto mantém controlo e evita comportamentos silenciosos.

---

## 8. Exemplo guiado

```c
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

int ler_numero_positivo(int *out) {
    int x;
    if (scanf("%d", &x) != 1) return 1;
    if (x <= 0) return 2;
    *out = x;
    return 0;
}

int main(void) {
    int n;
    int err = ler_numero_positivo(&n);

    if (err == 1) {
        printf("Entrada invalida\n");
        return 1;
    }
    if (err == 2) {
        printf("Valor deve ser positivo\n");
        return 2;
    }

    int *v = malloc(n * sizeof(int));
    if (v == NULL) {
        perror("Erro de memoria");
        return errno;
    }

    free(v);
    return 0;
}
```

---

## 9. Boas práticas de robustez

- valida cedo e devolve erro cedo;
- mensagens claras para utilizador;
- usa códigos de erro consistentes;
- liberta recursos mesmo quando há erro;
- evita "engolir" erros sem registo.

---

## 10. Erros comuns

1. Ignorar retorno de `scanf`.
2. Assumir que `malloc` nunca falha.
3. Abrir ficheiro e não verificar `NULL`.
4. Devolver código de erro sem contexto.
5. Esquecer fechar ficheiro em caminhos de erro.

---

## 11. Exercícios (sem resolução)

### Exercício 1 - Divisão segura

Implementa função de divisão com tratamento de divisor zero.

### Exercício 2 - Entrada robusta

Lê inteiro com validação de formato e intervalo.

### Exercício 3 - Códigos de erro

Define tabela de códigos de erro para um mini projeto.

### Exercício 4 - Ficheiros

Abre ficheiro para leitura e trata todos os possíveis erros básicos.

### Exercício 5 - Memória

Aloca vetor dinâmico com validação e mensagens de erro adequadas.

### Exercício 6 - Propagação

Cria cadeia de 3 funções que propagam erros até `main`.

### Exercício 7 - Limpeza de recursos

Garante que ficheiro e memória são libertados em qualquer caminho de erro.

### Exercício 8 - Refatoração

Melhora um código sem tratamento de erros.

### Exercício 9 - Diagnóstico

Usa `perror` e `errno` em 5 cenários distintos.

### Exercício 10 - Testes de erro

Define 15 testes focados apenas em cenários inválidos.

### Exercício 11 - Mensagens de utilizador

Reescreve mensagens técnicas para linguagem compreensível por utilizador final.

### Exercício 12 - Reflexão

Explica por que tratamento de erros faz parte da qualidade do software.

---

## 12. Changelog

- **2026-02-23**: reescrita completa com abordagem detalhada e exercícios sem resolução.
