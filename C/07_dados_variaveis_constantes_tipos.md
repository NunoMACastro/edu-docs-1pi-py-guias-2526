# C (10.º Ano) - 07 · Dados, Variáveis, Declarações, Expressões, Constantes e Tipos

> **Objetivo deste ficheiro**  
> Dominar os blocos base de dados em C: tipos simples, variáveis, expressões e boas práticas de declaração.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. Dados em programação](#1-dados-em-programação)
- [2. Variáveis e declaração](#2-variáveis-e-declaração)
- [3. Tipos de dados simples em C](#3-tipos-de-dados-simples-em-c)
- [4. Constantes: `const` e `#define`](#4-constantes-const-e-define)
- [5. Expressões e atribuições](#5-expressões-e-atribuições)
- [6. Conversões de tipo (casting)](#6-conversões-de-tipo-casting)
- [7. Especificadores de formato (`printf`/`scanf`)](#7-especificadores-de-formato-printfscanf)
- [8. Exemplo guiado](#8-exemplo-guiado)
- [9. Erros comuns](#9-erros-comuns)
- [10. Exercícios (sem resolução)](#10-exercícios-sem-resolução)
- [11. Changelog](#11-changelog)

---

## 0. Como usar este módulo

1. Memoriza os tipos mais usados (`int`, `float`, `double`, `char`).
2. Pratica `printf` e `scanf` com formatos corretos.
3. Treina validação básica de dados.

---

## 1. Dados em programação

Dados são valores que o programa lê, processa e apresenta.

Exemplos:

- idade (`int`);
- temperatura (`float`);
- letra (`char`);
- preço (`double`).

Escolher tipo correto evita erros e desperdício de memória.

---

## 2. Variáveis e declaração

Declaração define tipo e nome:

```c
int idade;
float altura;
char inicial;
```

Inicialização (boa prática):

```c
int idade = 16;
float altura = 1.72f;
char inicial = 'A';
```

---

## 3. Tipos de dados simples em C

- `char`: 1 carácter.
- `int`: inteiro.
- `float`: decimal com precisão simples.
- `double`: decimal com precisão maior.

Qual usar?

- contagens: `int`;
- medições comuns: `float`;
- cálculos mais sensíveis: `double`.

---

## 4. Constantes: `const` e `#define`

### `const`

```c
const int MAX_ALUNOS = 30;
```

### `#define`

```c
#define PI 3.1415926535
```

Uso recomendado:

- valores fixos e significativos;
- evitar "números mágicos" no código.

---

## 5. Expressões e atribuições

Expressão combina valores e operadores:

```c
int total = a + b * 2;
```

Atribuições compostas:

```c
x += 3;
y *= 2;
```

Sempre considerar precedência de operadores e uso de parênteses para clareza.

---

## 6. Conversões de tipo (casting)

Conversão explícita:

```c
int a = 5, b = 2;
float r = (float)a / b; // 2.5
```

Sem cast, `a / b` seria divisão inteira (`2`).

---

## 7. Especificadores de formato (`printf`/`scanf`)

Comuns:

- `%d` para `int`
- `%f` para `float`
- `%lf` para `double` em `scanf`
- `%c` para `char`
- `%s` para string (`char[]`)

Exemplo:

```c
int idade;
scanf("%d", &idade);
printf("Idade: %d\n", idade);
```

Cuidado: `scanf` precisa de endereço (`&`) para variáveis simples.

---

## 8. Exemplo guiado

```c
#include <stdio.h>
#define PI 3.1415926535

int main(void) {
    const int ANO = 2026;
    float raio;

    printf("Raio: ");
    scanf("%f", &raio);

    double area = PI * raio * raio;

    printf("Ano: %d\n", ANO);
    printf("Area: %.2lf\n", area);
    return 0;
}
```

Pontos-chave:

- constante simbólica com `#define`;
- constante de contexto com `const`;
- cálculo com conversão implícita para `double`.

---

## 9. Erros comuns

1. Usar `%f` errado em `scanf` para `double`.
2. Esquecer `&` no `scanf`.
3. Misturar tipos sem perceber perda de precisão.
4. Variáveis sem inicialização.
5. Nomes pouco claros.

---

## 10. Exercícios (sem resolução)

### Exercício 1 - Declarações

Declara 12 variáveis com tipos adequados para um sistema escolar.

### Exercício 2 - Tipos corretos

Para 15 situações, escolhe tipo mais apropriado e justifica.

### Exercício 3 - Constantes

Cria constantes para IVA, limite de faltas e nota máxima.

### Exercício 4 - Expressões

Escreve 10 expressões matemáticas em C com resultado previsto.

### Exercício 5 - Casting

Mostra diferença entre divisão inteira e real em 6 exemplos.

### Exercício 6 - Entrada/saída

Lê nome, idade e média; imprime relatório formatado.

### Exercício 7 - Conversão de unidades

Converte Celsius para Fahrenheit usando `float`.

### Exercício 8 - Validação básica

Lê idade e valida se está entre 0 e 120.

### Exercício 9 - Formatação

Imprime tabela com alinhamento simples (`printf`) para 5 alunos.

### Exercício 10 - Diagnóstico

Corrige um conjunto de 8 linhas com erros de tipos/formato.

### Exercício 11 - Mini programa

Cria calculadora de área e perímetro de retângulo com entradas do utilizador.

### Exercício 12 - Reflexão

Explica por que a escolha do tipo de dados influencia qualidade do programa.

---

## 11. Changelog

- **2026-02-23**: reescrita completa com abordagem detalhada, pedagógica e exercícios sem resolução.
