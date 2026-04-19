# C (10.º Ano) - 09 · Estruturas de Controlo em C

> **Objetivo deste ficheiro**  
> Controlar o fluxo do programa com decisões e ciclos, criando soluções robustas e legíveis.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. Fluxo de execução](#1-fluxo-de-execução)
- [2. Seleção com `if`, `else if`, `else`](#2-seleção-com-if-else-if-else)
- [3. Seleção com `switch`](#3-seleção-com-switch)
- [4. Repetição com `while`](#4-repetição-com-while)
- [5. Repetição com `do while`](#5-repetição-com-do-while)
- [6. Repetição com `for`](#6-repetição-com-for)
- [7. `break` e `continue`](#7-break-e-continue)
- [8. Ciclos aninhados](#8-ciclos-aninhados)
- [9. Exemplo guiado completo](#9-exemplo-guiado-completo)
- [10. Erros comuns](#10-erros-comuns)
- [11. Changelog](#11-changelog)

---

## 0. Como usar este módulo

1. Treina primeiro cada estrutura isoladamente.
2. Só depois combina decisões + ciclos no mesmo programa.
3. Testa casos limite para evitar ciclos infinitos.

---

## 1. Fluxo de execução

Por defeito, C executa linha a linha.

Estruturas de controlo permitem:

- escolher caminhos diferentes;
- repetir blocos de código.

---

## 2. Seleção com `if`, `else if`, `else`

Exemplo:

```c
if (nota < 10) {
    printf("Negativa\n");
} else if (nota < 14) {
    printf("Suficiente\n");
} else {
    printf("Boa\n");
}
```

Boa prática: evitar profundidade excessiva de `if` aninhado.

---

## 3. Seleção com `switch`

Útil quando comparas o mesmo valor com várias opções.

```c
switch (opcao) {
    case 1: printf("Novo\n"); break;
    case 2: printf("Listar\n"); break;
    case 0: printf("Sair\n"); break;
    default: printf("Opcao invalida\n");
}
```

Não esquecer `break` para evitar "queda" para o próximo caso.

---

## 4. Repetição com `while`

Executa enquanto condição for verdadeira.

```c
int i = 1;
while (i <= 5) {
    printf("%d\n", i);
    i++;
}
```

---

## 5. Repetição com `do while`

Executa pelo menos uma vez.

```c
int opcao;
do {
    printf("1-Continuar 0-Sair\n");
    scanf("%d", &opcao);
} while (opcao != 0);
```

---

## 6. Repetição com `for`

Bom para contagens conhecidas.

```c
for (int i = 0; i < 10; i++) {
    printf("%d ", i);
}
```

Estrutura: inicialização; condição; atualização.

---

## 7. `break` e `continue`

- `break`: termina ciclo atual.
- `continue`: salta para próxima iteração.

Usar com moderação para não tornar fluxo confuso.

---

## 8. Ciclos aninhados

Ciclo dentro de ciclo.

Exemplo: matriz 3x3.

```c
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        printf("(%d,%d) ", i, j);
    }
    printf("\n");
}
```

---

## 9. Exemplo guiado completo

Menu com repetição e seleção:

```c
#include <stdio.h>

int main(void) {
    int opcao;

    do {
        printf("\n1-Somar\n2-Tabuada\n0-Sair\nOpcao: ");
        scanf("%d", &opcao);

        if (opcao == 1) {
            int a, b;
            scanf("%d %d", &a, &b);
            printf("Soma = %d\n", a + b);
        } else if (opcao == 2) {
            int n;
            scanf("%d", &n);
            for (int i = 1; i <= 10; i++) {
                printf("%d x %d = %d\n", n, i, n * i);
            }
        } else if (opcao != 0) {
            printf("Opcao invalida\n");
        }
    } while (opcao != 0);

    return 0;
}
```

---

## 10. Erros comuns

1. Ciclo infinito por condição nunca atualizada.
2. `switch` sem `break` quando não era intenção.
3. Condições mal escritas (`=` em vez de `==`).
4. Menus sem caso inválido.
5. Falta de validação de entrada.

---

## 11. Changelog

- **2026-02-23**: reescrita completa, foco pedagógico e exercícios sem resolução.
