# C (10.º Ano) - 21 · Mini Projeto (1 hora)

---

## Índice

- [0. Contexto](#0-contexto)
- [1. Tema do mini projeto](#1-tema-do-mini-projeto)
- [2. Objetivos de aprendizagem](#2-objetivos-de-aprendizagem)
- [3. Regras funcionais do sistema](#3-regras-funcionais-do-sistema)
- [4. Requisitos técnicos obrigatórios](#4-requisitos-técnicos-obrigatórios)
- [5. Entregáveis em papel](#5-entregáveis-em-papel)
- [6. Planeamento sugerido (60 min)](#6-planeamento-sugerido-60-min)
- [7. Estrutura mínima esperada](#7-estrutura-mínima-esperada)
- [8. Casos de teste para simulação manual](#8-casos-de-teste-para-simulação-manual)
- [9. Critérios de avaliação (proposta)](#9-critérios-de-avaliação-proposta)
- [10. Erros mais comuns a evitar](#10-erros-mais-comuns-a-evitar)
- [11. Changelog](#11-changelog)

---

## 0. Contexto

A escola vai organizar uma visita de estudo a um museu interativo.  
Cada aluno deve simular, em C, o cálculo do preço final do bilhete, com validação de dados e decisão de compra.

O trabalho é individual e feito **à mão, em papel**.

---

## 1. Tema do mini projeto

### **Sistema de Bilhetes - Visita de Estudo**

Criar um programa em C que:

1. lê dados do utilizador;
2. calcula o preço final do bilhete;
3. decide se a compra é aprovada com base no saldo disponível;
4. mostra um resumo final no ecrã.

Precisas de criar as variáveis, constantes, definições e lógica necessárias para cumprir os requisitos.

---

## 2. Objetivos de aprendizagem

No final, o aluno deve demonstrar que consegue:

- declarar variáveis e constantes com tipos corretos;
- usar `printf` e `scanf` com formatos adequados;
- aplicar operadores aritméticos, relacionais e lógicos;
- usar estruturas de seleção `if`, `else if` e `else`;
- validar dados de entrada de forma básica.

---

## 3. Regras funcionais do sistema

### 3.1 Dados de entrada

Ler os seguintes dados:

- `nome` (string simples sem espaços);
- `idade` (inteiro);
- `tipo_bilhete` (inteiro):
    - `1` -> Normal
    - `2` -> Estudante
    - `3` -> Sénior
- `dia_semana` (inteiro de `1` a `7`, onde `6` e `7` são fim de semana);
- `tem_cartao_escola` (inteiro: `0` = não, `1` = sim);
- `saldo` (real, em euros).

### 3.2 Constantes obrigatórias

Usar, pelo menos, estas constantes:

- `PRECO_NORMAL = 10.00`
- `PRECO_ESTUDANTE = 7.00`
- `PRECO_SENIOR = 6.00`
- `TAXA_FIM_SEMANA = 2.00`

Podes usar `const` ou `#define`.

### 3.3 Validação obrigatória

Antes de calcular:

- `idade` deve estar entre `1` e `120`;
- `tipo_bilhete` deve ser `1`, `2` ou `3`;
- `dia_semana` deve estar entre `1` e `7`;
- `tem_cartao_escola` deve ser `0` ou `1`;
- `saldo` não pode ser negativo.

Se algum dado for inválido, mostrar mensagem de erro e terminar o programa.

### 3.4 Cálculo do preço

1. Definir o **preço base** com `if / else if / else` a partir de `tipo_bilhete`.
2. Se for fim de semana (`dia_semana == 6 || dia_semana == 7`), somar `TAXA_FIM_SEMANA`.
3. Se `tem_cartao_escola == 1` **e** `tipo_bilhete == 2`, aplicar desconto de `10%`.
4. Se `idade <= 12`, aplicar desconto adicional de `50%` ao valor atual.

### 3.5 Decisão final

- Se `saldo >= preco_final`, compra aprovada.
- Caso contrário, compra recusada e indicar quanto falta (`preco_final - saldo`).

### 3.6 Saída esperada

Mostrar no fim:

- nome;
- tipo de bilhete;
- preço final (2 casas decimais);
- estado da compra (aprovada/recusada);
- valor em falta (se aplicável).

---

## 4. Requisitos técnicos obrigatórios

- incluir `#include <stdio.h>`;
- usar `int`, `float`/`double`, `char[]`;
- usar `scanf` com `&` onde aplicável;
- usar pelo menos:
  - 3 blocos `if/else if/else`;
  - 1 condição com `&&` ou `||`;
- não usar ciclos (`for`, `while`, `do while`);
- não usar funções próprias (apenas `main`).

---

## 5. Entregáveis em papel

Entregar:

1. código C completo e legível;
2. pequena tabela com variáveis e respetivos tipos;
3. duas simulações manuais (duas execuções com dados diferentes);
4. output final esperado para cada simulação.

---

## 6. Planeamento sugerido (60 min)

1. **10 min** - Ler enunciado e planear variáveis/constantes.
2. **30 min** - Escrever o código completo.
3. **15 min** - Simular 2 casos de teste em papel.
4. **5 min** - Rever erros de sintaxe e lógica.

---

## 7. Estrutura mínima esperada

```c
#include <stdio.h>

int main(void) {
    // 1) Declaracoes
    // 2) Leitura com scanf
    // 3) Validacao de dados
    // 4) Calculo do preco com if/else if/else
    // 5) Decisao final de compra
    // 6) Impressao do resumo

    return 0;
}
```

---

## 8. Casos de teste para simulação manual

### Caso A (compra aprovada)

- Nome: `Ana`
- Idade: `16`
- Tipo: `2` (Estudante)
- Dia: `3`
- Cartão escola: `1`
- Saldo: `10.00`

### Caso B (compra recusada)

- Nome: `Rui`
- Idade: `17`
- Tipo: `1` (Normal)
- Dia: `7`
- Cartão escola: `0`
- Saldo: `8.00`

### Caso C (entrada inválida)

- Nome: `Marta`
- Idade: `15`
- Tipo: `4`
- Dia: `2`
- Cartão escola: `1`
- Saldo: `20.00`

---

## 9. Critérios de avaliação (proposta)

- **20%** Tipos de dados e declarações corretas
- **20%** Uso correto de `printf`/`scanf` e formatos
- **25%** Lógica de seleção (`if/else if/else`) correta
- **20%** Cálculo do preço final e decisão de compra
- **15%** Organização, legibilidade e simulação manual

---

## 10. Erros mais comuns a evitar

1. Trocar `=` por `==` nas condições.
2. Esquecer `&` no `scanf` de variáveis simples.
3. Não validar os intervalos antes de calcular.
4. Escrever condições sobrepostas ou contraditórias.
5. Não limitar casas decimais no output monetário (`%.2f`).

---

## 11. Changelog

- **2026-04-23**: criação do mini projeto de 1 hora (versão para trabalho em papel).
