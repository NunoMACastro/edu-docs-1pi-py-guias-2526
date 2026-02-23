# C (10.º Ano) - 02 · Pensamento Computacional (Princípios)

> **Objetivo deste ficheiro**  
> Aprender a pensar como programador: organizar problemas, identificar padrões e desenhar soluções antes de escrever código C.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. O que é pensamento computacional?](#1-o-que-é-pensamento-computacional)
- [2. Princípio 1 - Decomposição](#2-princípio-1---decomposição)
- [3. Princípio 2 - Reconhecimento de padrões](#3-princípio-2---reconhecimento-de-padrões)
- [4. Princípio 3 - Abstração](#4-princípio-3---abstração)
- [5. Princípio 4 - Algoritmos](#5-princípio-4---algoritmos)
- [6. Fluxo E-P-S (Entrada, Processo, Saída)](#6-fluxo-e-p-s-entrada-processo-saída)
- [7. Do problema real ao código C](#7-do-problema-real-ao-código-c)
- [8. Exemplo guiado completo](#8-exemplo-guiado-completo)
- [9. Erros comuns](#9-erros-comuns)
- [10. Checklist mental antes de programar](#10-checklist-mental-antes-de-programar)
- [11. Exercícios (sem resolução)](#11-exercícios-sem-resolução)
- [12. Changelog](#12-changelog)

---

## 0. Como usar este módulo

1. Lê os 4 princípios com atenção.
2. Tenta aplicar cada princípio a um problema do dia a dia.
3. Só depois passa aos exemplos em C.
4. Faz os exercícios sem saltar os básicos.

---

## 1. O que é pensamento computacional?

É uma forma de resolver problemas de maneira organizada, lógica e repetível.

Não depende de linguagem.  
Primeiro pensamos na solução. Depois codificamos.

Vantagens:

- reduz erros;
- evita bloqueios;
- melhora clareza do código;
- acelera depuração.

---

## 2. Princípio 1 - Decomposição

Decompor = partir um problema grande em partes menores.

Exemplo: "Sistema de notas"

- ler dados;
- validar notas;
- calcular média;
- mostrar relatório.

Cada parte fica mais simples de construir e testar.

---

## 3. Princípio 2 - Reconhecimento de padrões

Padrão = algo que se repete.

Exemplos:

- validar vários valores com regras iguais;
- percorrer listas com ciclos;
- usar menus com estrutura semelhante.

Quando encontras padrão, podes reaproveitar lógica em funções.

---

## 4. Princípio 3 - Abstração

Abstrair = focar no essencial e ignorar detalhes desnecessários naquele momento.

Exemplo:

- essencial: "calcular média";
- detalhe adiado: "cor da interface".

Abstração ajuda a não misturar tudo ao mesmo tempo.

---

## 5. Princípio 4 - Algoritmos

Algoritmo = sequência de passos finitos para resolver um problema.

Bom algoritmo é:

- claro;
- correto;
- finito;
- testável.

---

## 6. Fluxo E-P-S (Entrada, Processo, Saída)

Modelo simples para qualquer problema:

- Entrada: dados recebidos.
- Processo: regras/cálculos aplicados.
- Saída: resultado produzido.

Exemplo (média):

- Entrada: 3 notas.
- Processo: somar e dividir por 3.
- Saída: média final.

---

## 7. Do problema real ao código C

Processo recomendado:

1. Escreve o problema em 2-3 frases.
2. Lista entradas e saídas.
3. Faz algoritmo em texto/pseudocódigo.
4. Só depois escreve C.
5. Testa com casos normais e inválidos.

Exemplo mínimo em C:

```c
#include <stdio.h>

int main(void) {
    float n1, n2, n3;
    scanf("%f %f %f", &n1, &n2, &n3);
    float media = (n1 + n2 + n3) / 3.0f;
    printf("Media: %.2f\n", media);
    return 0;
}
```

---

## 8. Exemplo guiado completo

Problema: "Classificar temperatura ambiente"

Regra:

- < 10: frio
- 10 a 24: ameno
- >= 25: quente

Passo 1 - Decomposição

- ler temperatura;
- aplicar decisão;
- mostrar classificação.

Passo 2 - Padrão

- decisão por intervalos (if/else).

Passo 3 - Abstração

- ignorar origem da temperatura (sensor/manual).

Passo 4 - Algoritmo

- ler valor;
- comparar intervalos;
- imprimir classe.

Código:

```c
#include <stdio.h>

int main(void) {
    float t;
    printf("Temperatura: ");
    scanf("%f", &t);

    if (t < 10.0f) {
        printf("Frio\n");
    } else if (t <= 24.0f) {
        printf("Ameno\n");
    } else {
        printf("Quente\n");
    }

    return 0;
}
```

---

## 9. Erros comuns

1. Querer resolver tudo de uma vez.
2. Não identificar entradas antes de programar.
3. Ignorar validação de dados.
4. Copiar código sem compreender o algoritmo.
5. Confundir detalhe técnico com objetivo principal.

---

## 10. Checklist mental antes de programar

- Qual é exatamente o problema?
- Quais são as entradas?
- Qual é a saída esperada?
- Quais regras devo aplicar?
- Que casos de erro podem acontecer?

---

## 11. Exercícios (sem resolução)

### Exercício 1 - E-P-S

Para cada problema abaixo, identifica entrada, processo e saída:

1. cálculo de IMC;
2. cálculo de desconto;
3. classificar idade em faixa etária.

### Exercício 2 - Decomposição

Decompõe "gestão de biblioteca escolar" em pelo menos 8 subtarefas.

### Exercício 3 - Padrões

Analisa 5 programas simples e identifica padrões repetidos.

### Exercício 4 - Abstração

Escreve dois níveis de descrição do mesmo problema:

- nível geral (negócio);
- nível técnico (programação em C).

### Exercício 5 - Algoritmo textual

Cria algoritmo textual para validar password com regras mínimas.

### Exercício 6 - Pseudocódigo

Escreve pseudocódigo para calcular o maior de 4 números.

### Exercício 7 - Conversão para C

Implementa em C o algoritmo do exercício 6.

### Exercício 8 - Casos de teste

Define 12 testes para o programa do exercício 7.

### Exercício 9 - Diagnóstico

Um colega programou sem decomposição e está bloqueado.  
Escreve um plano de apoio em 6 passos.

### Exercício 10 - Melhorias

Recebes um código funcional mas confuso.  
Lista 10 melhorias orientadas por pensamento computacional.

### Exercício 11 - Aplicação real

Escolhe um problema da escola e descreve como aplicarias os 4 princípios.

### Exercício 12 - Reflexão curta

Em 12 linhas, explica porque "pensar antes de codificar" poupa tempo.

---

## 12. Changelog

- **2026-02-23**: reescrita completa do módulo com explicação detalhada e exercícios sem resolução.
