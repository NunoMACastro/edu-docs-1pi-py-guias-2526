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
