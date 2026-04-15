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
- [7. Resumo de IO formatada e ponte para modulo 07A](#7-resumo-de-io-formatada-e-ponte-para-modulo-07a)
- [8. Exemplo guiado](#8-exemplo-guiado)
- [9. Erros comuns](#9-erros-comuns)
- [10. Exercícios (sem resolução)](#10-exercícios-sem-resolução)
- [11. Changelog](#11-changelog)

---

## 0. Como usar este módulo

1. Memoriza os tipos mais usados (`int`, `float`, `double`, `char`).
2. Revê o resumo de I/O neste módulo e aprofunda no módulo `07A`.
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

Em C, o tipo define:

- que tipo de valor a variável guarda;
- quanto espaço de memória ocupa;
- intervalo de valores possível;
- como esse valor é interpretado nas operações.

### 3.1 Inteiros

Tipos principais para números sem parte decimal:

- `short int` (ou `short`)
- `int`
- `long int` (ou `long`)
- `long long int` (ou `long long`)

Versões com sinal:

- `signed` (permite negativos e positivos)
- `unsigned` (apenas zero e positivos, com intervalo máximo maior)

Exemplo:

```c
short ano = 2026;
int alunos = 28;
unsigned int tentativas = 3;
long long populacao = 10500000LL;
```

Limites de cada int:

| Tipo        | Intervalo (signed)                                     | Intervalo (unsigned)           |
| ----------- | ------------------------------------------------------ | ------------------------------ |
| `short`     | -32,768 a 32,767                                       | 0 a 65,535                     |
| `int`       | -2,147,483,648 a 2,147,483,647                         | 0 a 4,294,967295               |
| `long`      | -2,147,483,648 a 2,147,483,647                         | 0 a 4,294,967295               |
| `long long` | -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807 | 0 a 18,446,744,073,709,551,615 |

### 3.2 Reais (vírgula flutuante)

Tipos para valores com casas decimais:

- `float`: precisão simples (aprox. 6 a 7 algarismos significativos);
- `double`: precisão dupla (aprox. 15 a 16 algarismos significativos);
- `long double`: precisão ainda maior (depende do compilador/plataforma).

O que é `double` na prática:

- é um tipo decimal mais preciso que `float`;
- reduz erros de arredondamento em cálculos mais exigentes;
- é normalmente a escolha padrão para cálculos científicos e médias mais sensíveis.

Exemplo:

```c
float temperatura = 21.5f;     // nota o sufixo f
double media = 14.7564231;     // mais precisão
long double constante = 3.141592653589793238L;
```

### 3.3 Caracteres e texto

- `char`: guarda um único carácter (ex.: `'A'`, `'7'`, `'\n'`);
- string em C: array de `char` terminado por `'\0'`.

Exemplo:

```c
char inicial = 'N';
char nome[] = "Nuno";
```

### 3.4 Lógicos e tipo sem valor

- `_Bool` (ou `bool` com `#include <stdbool.h>`): representa verdadeiro/falso;
- `void`: significa "sem valor" (ex.: função que não devolve resultado).

Exemplo:

```c
#include <stdbool.h>
bool ativo = true;
```

### 3.5 Nota sobre tamanhos

O tamanho em bytes pode variar com sistema e compilador. Regra segura:

- não assumir tamanho fixo de `int`, `long`, etc.;
- usar `sizeof(tipo)` para confirmar quando necessário.

Exemplo:

```c
printf("int: %zu bytes\n", sizeof(int));
printf("double: %zu bytes\n", sizeof(double));
```

Qual usar no dia a dia:

- contagens e índices: `int`;
- valores decimais simples: `float` ou `double`;
- cálculos com mais exigência de precisão: `double`;
- estados lógico/sim-não: `bool`;
- texto: `char` e `char[]`.

---

## 4. Constantes: `const` e `#define`

Ambos servem para evitar "números mágicos", mas funcionam de forma diferente.

### 4.1 `const` (constante com tipo)

`const` cria uma variável cujo valor não deve ser alterado.

```c
const int MAX_ALUNOS = 30;
const double PI = 3.141592653589793;
```

Características:

- tem tipo (`int`, `double`, etc.);
- é validado pelo compilador com mais segurança;
- respeita escopo (global ou local da função).

Exemplo de erro detetado:

```c
const int LIMITE = 10;
// LIMITE = 20; // erro: tentativa de alterar constante
```

### 4.2 `#define` (substituição do pré-processador)

`#define` não cria variável. Ele substitui texto antes da compilação.

```c
#define PI 3.141592653589793
#define MAX_NOME 64
```

Características:

- não tem tipo próprio;
- não ocupa "nome de variável" no código compilado;
- costuma ser usado para constantes simples, flags de compilação e macros.

### 4.3 Diferença prática rápida

- `const`: constante tipada e mais segura.
- `#define`: substituição textual, mais flexível, mas mais propensa a erro.

Regra pedagógica útil:

- para valores fixos numéricos, prefere `const`;
- usa `#define` quando precisas mesmo de macro textual.

### 4.4 Cuidado com macros sem parênteses

Macro mal definida:

```c
#define DOBRO(x) x * 2
```

Uso:

```c
int r = DOBRO(3 + 1); // vira 3 + 1 * 2 -> 5 (inesperado)
```

Forma correta:

```c
#define DOBRO(x) ((x) * 2)
```

### 4.5 Boas práticas

1. Usa nomes significativos e em maiúsculas para macros (`MAX_BUFFER`).
2. Prefere `const` para constantes de valor.
3. Evita macros complexas no início; prioriza clareza.
4. Centraliza constantes no topo do ficheiro ou em headers.

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

## 7. Resumo de IO formatada e ponte para modulo 07A

Resumo mínimo neste módulo:

- `printf` imprime valores formatados (ex.: `%d`, `%f`, `%c`, `%s`);
- `scanf` lê valores e precisa de endereço (`&`) para variáveis simples;
- formatos errados em `printf`/`scanf` geram warnings e bugs;
- validar retorno de `scanf` evita usar dados inválidos.

Exemplo curto:

```c
int idade;
if (scanf("%d", &idade) == 1) {
    printf("Idade: %d\n", idade);
}
```

Para explicação detalhada de:

- `printf` (largura, precisão, alinhamento e `%p`);
- `scanf` (retorno, whitespace, newline e validação robusta);
- `&` e `*` (valor vs endereço) e comparação `scanf("%s")` vs `fgets`;

consulta:

- [07a_entrada_saida_formatada_printf_scanf_e_enderecos.md](./07a_entrada_saida_formatada_printf_scanf_e_enderecos.md)

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
    printf("Area: %.2f\n", area);
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

Cria a "ficha digital" de um aluno: número, nome, turma, idade, média atual e percentagem de faltas. Declara variáveis com tipos adequados e nomes claros.

### Exercício 2 - Tipos corretos

Dado um sistema de bicicletas partilhadas, escolhe tipos para: id da bicicleta, quilómetros totais, custo por minuto, estado (disponível/ocupada) e nível de bateria. Justifica cada escolha.

### Exercício 3 - Constantes

Define constantes para: limite de velocidade de trotinete elétrica, preço fixo de desbloqueio e taxa por minuto. Usa `const` e/ou `#define` de forma consistente.

### Exercício 4 - Expressões

Num simulador de treino, calcula calorias estimadas com base em tempo (min), peso (kg) e fator de intensidade. Escreve as expressões em C e prevê os resultados para dois casos de teste.

### Exercício 5 - Casting

Num painel de estatísticas, calcula média de pontos por jogo e taxa de vitórias. Mostra o resultado sem cast e com cast, explicando a diferença no valor apresentado.

### Exercício 6 - Entrada/saída

Lê nome do produto, quantidade e preço unitário. Imprime um resumo de compra alinhado com subtotal e total com 2 casas decimais.

### Exercício 7 - Conversão de unidades

Cria um mini conversor de meteorologia: lê temperatura em Celsius e velocidade do vento em km/h, depois mostra Fahrenheit e m/s com formatação adequada.

### Exercício 8 - Validação básica

Lê a percentagem de bateria de um dispositivo (0 a 100) e valida o valor. Se estiver fora do intervalo, imprime mensagem de erro clara.

### Exercício 9 - Formatação

Mostra um "placar" com 3 jogadores: nome, pontos e precisão (%) com colunas alinhadas em `printf`.

### Exercício 10 - Diagnóstico

Analisa um trecho com erros de tipos e formatos (`%d`, `%f`, `%lf`, uso de `&` no `scanf`) e corrige cada linha, explicando o motivo técnico.

### Exercício 11 - Mini programa

Desenvolve um simulador de consumo elétrico doméstico: lê potência (W), horas de uso por dia e preço por kWh; calcula consumo mensal e custo estimado.

### Exercício 12 - Reflexão

Escreve uma reflexão curta: em que situações um `int` pode causar erro silencioso e quando `float`/`double` é realmente necessário?

---

## 11. Changelog

- **2026-02-23**: reescrita completa com abordagem detalhada, pedagógica e exercícios sem resolução.
- **2026-04-14**: revisão dos exercícios
- **2026-04-15**: secção de I/O reduzida para resumo e ligação para o novo módulo `07A`.
