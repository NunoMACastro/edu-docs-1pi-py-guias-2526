# C (10.º Ano) - 16 · Herança e Polimorfismo (Contexto em C)

> **Objetivo deste ficheiro**  
> Compreender conceitos de herança e polimorfismo e aplicar equivalentes práticos em linguagem C.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. Nota essencial: conceitos vs recursos da linguagem](#1-nota-essencial-conceitos-vs-recursos-da-linguagem)
- [2. Herança: ideia geral](#2-herança-ideia-geral)
- [3. Como simular herança em C (composição)](#3-como-simular-herança-em-c-composição)
- [4. Polimorfismo: ideia geral](#4-polimorfismo-ideia-geral)
- [5. Como simular polimorfismo em C (ponteiros para função)](#5-como-simular-polimorfismo-em-c-ponteiros-para-função)
- [6. Interface comum em C](#6-interface-comum-em-c)
- [7. Exemplo guiado](#7-exemplo-guiado)
- [8. Limites da abordagem](#8-limites-da-abordagem)
- [9. Erros comuns](#9-erros-comuns)
- [10. Changelog](#10-changelog)

---

## 0. Como usar este módulo

1. Primeiro entende o conceito abstrato.
2. Depois estuda o equivalente prático em C.
3. Pratica com exemplos pequenos e bem controlados.

---

## 1. Nota essencial: conceitos vs recursos da linguagem

C não implementa herança/polimorfismo automaticamente.

Mas conseguimos simular comportamentos:

- herança -> composição e reutilização;
- polimorfismo -> ponteiros para função.

---

## 2. Herança: ideia geral

Herança, em OOP, permite criar tipo "filho" a partir de tipo "base".

Benefício: reutilizar estrutura comum.

Em C, fazemos isto colocando uma `struct base` dentro da `struct derivada`.

---

## 3. Como simular herança em C (composição)

```c
typedef struct {
    char nome[40];
} Animal;

typedef struct {
    Animal base;
    int velocidade;
} Cao;
```

`Cao` reutiliza dados comuns de `Animal`.

---

## 4. Polimorfismo: ideia geral

Polimorfismo permite chamar operação comum que varia conforme tipo concreto.

Em C, isso é feito com ponteiro para função.

---

## 5. Como simular polimorfismo em C (ponteiros para função)

```c
typedef void (*FalarFn)(void *self);

typedef struct {
    FalarFn falar;
} InterfaceAnimal;
```

Cada tipo concreta associa sua própria implementação de `falar`.

---

## 6. Interface comum em C

Estratégia prática:

- definir estrutura com funções (semelhante a "tabela virtual" simplificada);
- cada tipo fornece funções compatíveis;
- código cliente chama interface sem conhecer detalhes internos.

---

## 7. Exemplo guiado

```c
#include <stdio.h>

typedef struct {
    const char *nome;
    void (*falar)(const char *nome);
} AnimalOps;

void falar_cao(const char *nome) {
    printf("%s: Au au!\n", nome);
}

void falar_gato(const char *nome) {
    printf("%s: Miau!\n", nome);
}

int main(void) {
    AnimalOps a1 = {"Rex", falar_cao};
    AnimalOps a2 = {"Mimi", falar_gato};

    a1.falar(a1.nome);
    a2.falar(a2.nome);

    return 0;
}
```

Este código mostra polimorfismo por função associada ao "objeto".

---

## 8. Limites da abordagem

- mais manual que linguagens orientadas a objetos;
- sem proteção nativa de visibilidade/herança;
- maior risco de erro se contrato de interface não for respeitado.

Ainda assim, é excelente para entender conceitos com profundidade.

---

## 9. Erros comuns

1. Função com assinatura diferente da esperada na interface.
2. Não inicializar ponteiro de função.
3. Misturar campos sem padrão consistente.
4. Assumir que composição equivale a herança completa.
5. Código cliente depender de detalhes internos.

---

## 10. Changelog

- **2026-02-23**: reescrita detalhada com foco em equivalentes de herança/polimorfismo e exercícios sem resolução.
