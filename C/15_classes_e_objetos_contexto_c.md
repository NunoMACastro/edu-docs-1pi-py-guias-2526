# C (10.º Ano) - 15 · Classes e Objetos (Contexto em C)

> **Objetivo deste ficheiro**  
> Entender os conceitos de classes e objetos e aprender como modelar o equivalente em linguagem C.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. Nota essencial: C não tem `class` nativa](#1-nota-essencial-c-não-tem-class-nativa)
- [2. O que é "objeto" em termos de engenharia](#2-o-que-é-objeto-em-termos-de-engenharia)
- [3. Simulação de objeto em C com `struct` + funções](#3-simulação-de-objeto-em-c-com-struct--funções)
- [4. Encapsulamento em C (aproximação prática)](#4-encapsulamento-em-c-aproximação-prática)
- [5. Construtor e destrutor (ideia adaptada)](#5-construtor-e-destrutor-ideia-adaptada)
- [6. API pública vs implementação interna](#6-api-pública-vs-implementação-interna)
- [7. Exemplo guiado: "Conta" como objeto em C](#7-exemplo-guiado-conta-como-objeto-em-c)
- [8. Limitações e vantagens desta abordagem](#8-limitações-e-vantagens-desta-abordagem)
- [9. Erros comuns](#9-erros-comuns)
- [10. Exercícios (sem resolução)](#10-exercícios-sem-resolução)
- [11. Changelog](#11-changelog)

---

## 0. Como usar este módulo

1. Lê primeiro a diferença entre conceito e linguagem.
2. Foca no padrão `struct` + funções.
3. Pratica separação entre `.h` (interface) e `.c` (implementação).

---

## 1. Nota essencial: C não tem `class` nativa

Em C:

- não existe palavra-chave `class`;
- não existe encapsulamento automático como em C++/Java;
- não existe método ligado diretamente ao tipo.

Mas os conceitos podem ser aplicados por design.

---

## 2. O que é "objeto" em termos de engenharia

Pensamento orientado a objetos, de forma geral:

- estado (dados);
- comportamento (operações);
- regras de uso.

Em C, modelamos isso com:

- `struct` para estado;
- funções para comportamento;
- convenções para controlo de acesso.

---

## 3. Simulação de objeto em C com `struct` + funções

Padrão base:

- tipo definido em `.h`;
- funções com prefixo do tipo;
- manipulação por ponteiro.

Exemplo de assinatura:

```c
typedef struct {
    int saldo;
} Conta;

void conta_depositar(Conta *c, int valor);
```

---

## 4. Encapsulamento em C (aproximação prática)

Encapsulamento real em C é por convenção + organização de ficheiros.

Estratégias:

- expor apenas funções no `.h`;
- ocultar detalhes internos no `.c`;
- validar invariantes dentro das funções.

Assim, o utilizador da API não mexe diretamente em tudo.

---

## 5. Construtor e destrutor (ideia adaptada)

Como C não tem construtor automático, usamos funções de inicialização.

```c
void conta_init(Conta *c, int saldo_inicial);
void conta_destroy(Conta *c);
```

Se houver memória dinâmica, `destroy` torna-se obrigatório.

---

## 6. API pública vs implementação interna

Exemplo de organização:

- `conta.h`:
  - tipo `Conta` (público ou opaco);
  - funções públicas (`init`, `depositar`, `levantar`, `saldo`).
- `conta.c`:
  - validações internas;
  - detalhes de cálculo e regras.

Isto melhora manutenção e evita uso incorreto.

---

## 7. Exemplo guiado: "Conta" como objeto em C

`conta.h`:

```c
#ifndef CONTA_H
#define CONTA_H

typedef struct {
    int saldo;
} Conta;

void conta_init(Conta *c, int saldo_inicial);
int conta_depositar(Conta *c, int valor);
int conta_levantar(Conta *c, int valor);
int conta_saldo(const Conta *c);

#endif
```

`conta.c` (ideia):

```c
#include "conta.h"

void conta_init(Conta *c, int saldo_inicial) {
    c->saldo = saldo_inicial;
}

int conta_depositar(Conta *c, int valor) {
    if (valor <= 0) return 0;
    c->saldo += valor;
    return 1;
}
```

Isto já reproduz parte do comportamento de "objeto".

---

## 8. Limitações e vantagens desta abordagem

Limitações:

- sem suporte nativo de métodos/visibilidade;
- disciplina depende da equipa;
- mais trabalho manual.

Vantagens:

- controlo total;
- desempenho elevado;
- base sólida para compreender POO noutras linguagens.

---

## 9. Erros comuns

1. Tratar `struct` como saco de dados sem regras.
2. Expor tudo no `.h` e perder encapsulamento.
3. Não validar estado antes de operar.
4. Esquecer inicialização.
5. Não separar interface de implementação.

---

## 10. Exercícios (sem resolução)

### Exercício 1 - Modelação

Modela entidade `Aluno` como "objeto" em C (`struct` + funções).

### Exercício 2 - API mínima

Cria API para `Livro`: criar, atualizar estado e consultar dados.

### Exercício 3 - Inicialização

Implementa função `init` para 3 tipos diferentes.

### Exercício 4 - Encapsulamento

Reorganiza código para ocultar detalhes internos num `.c`.

### Exercício 5 - Validação de regras

Implementa função que recusa operações inválidas (ex.: saldo negativo).

### Exercício 6 - Modularização

Divide programa em `main.c`, `entidade.c`, `entidade.h`.

### Exercício 7 - Const-correctness

Cria funções de consulta que recebem ponteiro `const`.

### Exercício 8 - Testes manuais

Define 12 testes para validar API de uma entidade.

### Exercício 9 - Refatoração

Converte programa monolítico num design baseado em "objetos" simulados.

### Exercício 10 - Documentação

Escreve documentação de API para uma entidade criada por ti.

### Exercício 11 - Evolução

Acrescenta novo comportamento mantendo compatibilidade da API.

### Exercício 12 - Reflexão

Explica semelhanças e diferenças entre este modelo em C e classes em OOP.

---

## 11. Changelog

- **2026-02-23**: reescrita detalhada do módulo com foco em equivalentes de POO e exercícios sem resolução.
