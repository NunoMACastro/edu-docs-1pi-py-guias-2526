# C (10.º Ano) - 13 · Estruturas de Dados Compostas: `struct`, `union` e `enum`

> **Objetivo deste ficheiro**  
> Organizar dados mais ricos em C usando tipos compostos e compreender quando usar cada um.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. Porque estruturas compostas?](#1-porque-estruturas-compostas)
- [2. `struct`: agrupar campos relacionados](#2-struct-agrupar-campos-relacionados)
- [3. Acesso e manipulação com `.` e `->`](#3-acesso-e-manipulação-com--e--)
- [4. Arrays de `struct`](#4-arrays-de-struct)
- [5. `enum`: conjunto de estados simbólicos](#5-enum-conjunto-de-estados-simbólicos)
- [6. `union`: partilha de memória](#6-union-partilha-de-memória)
- [7. Escolha entre `struct`, `union` e `enum`](#7-escolha-entre-struct-union-e-enum)
- [8. Exemplo guiado](#8-exemplo-guiado)
- [9. Erros comuns](#9-erros-comuns)
- [10. Exercícios (sem resolução)](#10-exercícios-sem-resolução)
- [11. Changelog](#11-changelog)

---

## 0. Como usar este módulo

1. Começa por `struct`.
2. Depois estuda `enum` para estados.
3. Só depois avança para `union`, que exige mais atenção.

---

## 1. Porque estruturas compostas?

Tipos simples não chegam para representar entidades reais.

Exemplo: um aluno tem nome, número, média e estado.

Sem `struct`, terias variáveis soltas e confusas.

---

## 2. `struct`: agrupar campos relacionados

```c
typedef struct {
    int numero;
    char nome[50];
    float media;
} Aluno;
```

`typedef` simplifica uso do tipo.

---

## 3. Acesso e manipulação com `.` e `->`

Acesso direto:

```c
Aluno a;
a.media = 14.5f;
```

Acesso por ponteiro:

```c
Aluno *p = &a;
p->media = 15.0f;
```

---

## 4. Arrays de `struct`

Muito útil para listas de registos.

```c
Aluno turma[30];
```

Permite percorrer e processar vários elementos com ciclos.

---

## 5. `enum`: conjunto de estados simbólicos

```c
typedef enum {
    INATIVO,
    ATIVO,
    BLOQUEADO
} Estado;
```

Vantagem: melhora leitura em vez de usar números "mágicos".

---

## 6. `union`: partilha de memória

Todos os campos ocupam a mesma área de memória.

```c
typedef union {
    int i;
    float f;
    char texto[20];
} Dado;
```

Usar quando apenas um formato de valor é usado de cada vez.

---

## 7. Escolha entre `struct`, `union` e `enum`

- `struct`: vários campos ao mesmo tempo.
- `enum`: estados/opções nomeadas.
- `union`: vários formatos alternativos no mesmo espaço.

---

## 8. Exemplo guiado

```c
#include <stdio.h>

typedef enum { ALUNO_ATIVO, ALUNO_INATIVO } EstadoAluno;

typedef struct {
    int numero;
    char nome[40];
    float media;
    EstadoAluno estado;
} Aluno;

int main(void) {
    Aluno a = {101, "Rita", 15.3f, ALUNO_ATIVO};

    printf("Numero: %d\n", a.numero);
    printf("Nome: %s\n", a.nome);
    printf("Media: %.1f\n", a.media);
    printf("Estado: %s\n", a.estado == ALUNO_ATIVO ? "ATIVO" : "INATIVO");

    return 0;
}
```

---

## 9. Erros comuns

1. Confundir `.` com `->`.
2. Não inicializar campos da `struct`.
3. Usar `union` sem saber qual campo está válido.
4. Usar números em vez de `enum` e perder legibilidade.
5. Copiar strings sem verificar tamanho.

---

## 10. Exercícios (sem resolução)

### Exercício 1 - `struct` básico

Cria `struct Livro` com título, autor, ano e disponibilidade.

### Exercício 2 - Leitura e impressão

Lê dados de 3 livros e imprime relatório.

### Exercício 3 - Array de structs

Cria array de 20 alunos e calcula média da turma.

### Exercício 4 - Pesquisa

Procura aluno por número dentro de array de structs.

### Exercício 5 - Atualização

Atualiza estado de um registo (ativo/inativo).

### Exercício 6 - `enum`

Define `enum` para dias da semana e usa em programa simples.

### Exercício 7 - `union`

Cria `union` para representar valor numérico em formatos diferentes.

### Exercício 8 - `struct` com `enum`

Combina `struct Pedido` com `enum EstadoPedido`.

### Exercício 9 - Ponteiros

Manipula `struct` através de ponteiro e operador `->`.

### Exercício 10 - Modularização

Move definições para ficheiro `.h` e implementação para `.c`.

### Exercício 11 - Validação

Valida campos de registo antes de guardar.

### Exercício 12 - Reflexão

Explica porque estruturas compostas tornam o código mais próximo de problemas reais.

---

## 11. Changelog

- **2026-02-23**: reescrita completa do módulo com detalhe pedagógico e exercícios sem resolução.
