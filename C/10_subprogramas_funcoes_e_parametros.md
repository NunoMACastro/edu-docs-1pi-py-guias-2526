# C (10.º Ano) - 10 · Subprogramas: Funções, Variáveis Locais/Globais e Parâmetros

> **Objetivo deste ficheiro**  
> Aprender a modularizar programas em C usando funções, compreendendo escopo e passagem de parâmetros.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. Porque usar funções?](#1-porque-usar-funções)
- [2. Protótipos, definição e chamada](#2-protótipos-definição-e-chamada)
- [3. Parâmetros e argumentos](#3-parâmetros-e-argumentos)
- [4. `return` e tipos de retorno](#4-return-e-tipos-de-retorno)
- [5. Variáveis locais e globais](#5-variáveis-locais-e-globais)
- [6. Passagem por valor em C](#6-passagem-por-valor-em-c)
- [7. Alterar valores com ponteiros](#7-alterar-valores-com-ponteiros)
- [8. Procedimentos vs funções](#8-procedimentos-vs-funções)
- [9. Organização em `.h` e `.c`](#9-organização-em-h-e-c)
- [10. Exemplo guiado](#10-exemplo-guiado)
- [11. Erros comuns](#11-erros-comuns)
- [12. Exercícios (sem resolução)](#12-exercícios-sem-resolução)
- [13. Changelog](#13-changelog)

---

## 0. Como usar este módulo

1. Escreve primeiro funções pequenas.
2. Treina diferença entre local e global.
3. Pratica passagem por ponteiro em exemplos curtos.

---

## 1. Porque usar funções?

Vantagens:

- evita repetição de código;
- organiza o programa;
- facilita testes;
- melhora leitura e manutenção.

Regra simples: cada função deve ter responsabilidade clara.

---

## 2. Protótipos, definição e chamada

Protótipo informa compilador antes da utilização.

```c
int soma(int a, int b); // protótipo

int soma(int a, int b) {
    return a + b;
}
```

---

## 3. Parâmetros e argumentos

- parâmetros: nomes na definição da função;
- argumentos: valores reais na chamada.

```c
int soma(int a, int b); // a,b parâmetros
int r = soma(2, 3);     // 2,3 argumentos
```

---

## 4. `return` e tipos de retorno

Função pode devolver:

- `int`, `float`, `double`, `char`, etc.;
- `void` quando não devolve valor.

Exemplo:

```c
void mostrar_menu(void) {
    printf("1 - Opcao\n");
}
```

---

## 5. Variáveis locais e globais

### Local

Declarada dentro de função/bloco; existe só ali.

### Global

Declarada fora das funções; visível em todo ficheiro.

Uso de globais deve ser controlado para evitar efeitos inesperados.

---

## 6. Passagem por valor em C

Por defeito, C passa cópia do valor.

```c
void tenta_alterar(int x) {
    x = 100;
}
```

`x` alterado dentro da função não muda variável original.

---

## 7. Alterar valores com ponteiros

Para alterar variável externa, passa endereço:

```c
void incrementar(int *v) {
    (*v)++;
}
```

Chamada:

```c
int n = 5;
incrementar(&n);
```

---

## 8. Procedimentos vs funções

Em termos pedagógicos:

- "função" devolve resultado;
- "procedimento" executa ação (`void`).

C usa funções para ambos os casos.

---

## 9. Organização em `.h` e `.c`

- `.h`: protótipos e tipos públicos.
- `.c`: implementação.

Exemplo:

- `operacoes.h` -> `int soma(int a, int b);`
- `operacoes.c` -> código da função.

---

## 10. Exemplo guiado

```c
#include <stdio.h>

int contador_global = 0;

int soma(int a, int b) {
    contador_global++;
    return a + b;
}

void trocar(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

int main(void) {
    int a = 2, b = 3;
    int r = soma(a, b);

    printf("Soma = %d\n", r);
    printf("Chamadas = %d\n", contador_global);

    trocar(&a, &b);
    printf("a=%d b=%d\n", a, b);

    return 0;
}
```

---

## 11. Erros comuns

1. Esquecer protótipo e gerar conflitos de tipo.
2. Confundir passagem por valor com por referência.
3. Abusar de variáveis globais.
4. Funções muito longas e pouco focadas.
5. Não validar ponteiros recebidos.

---

## 12. Exercícios (sem resolução)

### Exercício 1 - Funções básicas

Cria funções para somar, subtrair, multiplicar e dividir.

### Exercício 2 - Retorno

Cria função que devolve maior de dois inteiros.

### Exercício 3 - `void`

Cria procedimento que imprime linha separadora no ecrã.

### Exercício 4 - Locais e globais

Constrói exemplo com uma variável global e duas locais.

### Exercício 5 - Passagem por valor

Demonstra, com programa curto, que variável original não é alterada.

### Exercício 6 - Passagem por ponteiro

Cria função para trocar dois inteiros.

### Exercício 7 - Validação de parâmetros

Cria função de divisão que trate divisor zero.

### Exercício 8 - Modularização

Separa projeto em `main.c`, `operacoes.c`, `operacoes.h`.

### Exercício 9 - Contador de chamadas

Usa variável global para contar quantas vezes função foi chamada.

### Exercício 10 - Refatoração

Transforma programa monolítico em pelo menos 5 funções.

### Exercício 11 - Mini biblioteca

Cria conjunto de funções para manipular notas de alunos.

### Exercício 12 - Reflexão

Explica quando usar retorno e quando usar parâmetro por ponteiro.

---

## 13. Changelog

- **2026-02-23**: reescrita completa com explicação detalhada e exercícios sem resolução.
