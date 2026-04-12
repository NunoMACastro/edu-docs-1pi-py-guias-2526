# C - 02 · Pensamento Computacional (Princípios)

> **Objetivo deste ficheiro**  
> Desenvolver pensamento computacional sólido para transformar problemas reais em soluções estruturadas antes da codificação em C.

---

## Índice

- [0. Como estudar este módulo](#0-como-estudar-este-módulo)
- [1. Resultados de aprendizagem](#1-resultados-de-aprendizagem)
- [2. O que é pensamento computacional?](#2-o-que-é-pensamento-computacional)
- [3. Os 4 princípios fundamentais](#3-os-4-princípios-fundamentais)
- [4. Princípio 1 - Decomposição](#4-princípio-1---decomposição)
- [5. Princípio 2 - Reconhecimento de padrões](#5-princípio-2---reconhecimento-de-padrões)
- [6. Princípio 3 - Abstração](#6-princípio-3---abstração)
- [7. Princípio 4 - Algoritmos](#7-princípio-4---algoritmos)
- [8. Modelo E-P-S (Entrada, Processo, Saída)](#8-modelo-e-p-s-entrada-processo-saída)
- [9. Estratégia completa: do problema ao código](#9-estratégia-completa-do-problema-ao-código)
- [10. Exemplo guiado A - Média com validação](#10-exemplo-guiado-a---média-com-validação)
- [11. Exemplo guiado B - Classificação de temperatura](#11-exemplo-guiado-b---classificação-de-temperatura)
- [12. Erros comuns e como evitar](#12-erros-comuns-e-como-evitar)
- [13. Mini-laboratório de pensamento computacional](#13-mini-laboratório-de-pensamento-computacional)
- [14. Exercícios (sem resolução)](#14-exercícios-sem-resolução)
- [15. Rubrica de autoavaliação](#15-rubrica-de-autoavaliação)
- [16. Checklist mental antes de programar](#16-checklist-mental-antes-de-programar)
- [17. Changelog](#17-changelog)

---

## 0. Como estudar este módulo

1. Estuda cada princípio com calma antes de ver código.
2. Em cada exemplo, escreve primeiro algoritmo textual e só depois C.
3. Valida sempre casos normais, limite e inválidos.
4. Usa a checklist final como rotina obrigatória antes de programar.

---

## 1. Resultados de aprendizagem

No final deste módulo deves conseguir:

- explicar os 4 princípios com exemplos próprios;
- decompor problemas em subtarefas executáveis;
- identificar padrões e reutilizar lógica;
- separar essencial de detalhe técnico através de abstração;
- escrever algoritmos claros e testáveis;
- mapear qualquer problema para E-P-S;
- converter plano mental em código C com menor taxa de erro.

---

## 2. O que é pensamento computacional?

É um método para resolver problemas de forma estruturada, lógica e repetível.

Não depende da linguagem.

Ordem correta:

1. compreender problema;
2. estruturar solução;
3. só depois programar.

Sem este método, quem programa tende a:

- improvisar código;
- bloquear em decisões básicas;
- corrigir sintomas e não causas.

Com este método, quem programa consegue:

- antecipar problemas;
- justificar decisões;
- produzir código mais limpo.

---

## 3. Os 4 princípios fundamentais

1. Decomposição
2. Reconhecimento de padrões
3. Abstração
4. Algoritmos

Estes princípios funcionam em conjunto, não isolados.

Fluxo típico:

- decompor para reduzir complexidade;
- encontrar padrões para evitar repetição;
- abstrair para focar no que importa;
- formalizar em algoritmo para executar e testar.

---

## 4. Princípio 1 - Decomposição

Decompor é dividir um problema grande em partes menores controláveis.

Exemplo: "gestão de notas"

- ler dados;
- validar intervalo;
- calcular média;
- classificar resultado;
- mostrar relatório.

Critério de boa decomposição:

- cada subproblema deve ter objetivo claro;
- deve ser testável de forma independente;
- deve reduzir carga cognitiva.

Erro típico:

- decompor demais (fragmentação excessiva) ou de menos (blocos gigantes).

---

## 5. Princípio 2 - Reconhecimento de padrões

Padrão é estrutura que se repete em problemas diferentes.

Padrões comuns em C inicial:

- validação repetida de input;
- acumulação em ciclo;
- menu com `switch`;
- comparação por intervalos com `if/else`.

Vantagem:

- reaproveitar abordagem diminui erros e acelera implementação.

Exemplo:

- classificar temperatura, nota e idade usa a mesma ideia: intervalos + decisão.

---

## 6. Princípio 3 - Abstração

Abstrair é focar no essencial para a decisão atual.

Nível 1 (problema):

- "quero calcular média de três notas".

Nível 2 (algoritmo):

- ler 3 valores -> somar -> dividir por 3 -> mostrar.

Nível 3 (implementação C):

- variáveis `float`, `scanf`, `printf`.

Erro comum:

- mergulhar em detalhe técnico cedo demais e perder objetivo do problema.

---

## 7. Princípio 4 - Algoritmos

Algoritmo é sequência finita e precisa de passos para resolver um problema.

Bom algoritmo deve ser:

- correto;
- claro;
- finito;
- geral;
- testável.

Representações úteis:

- texto estruturado;
- pseudocódigo;
- fluxograma;
- implementação em C.

---

## 8. Modelo E-P-S (Entrada, Processo, Saída)

E-P-S é uma ferramenta prática para organizar pensamento.

- Entrada: dados recebidos;
- Processo: regras e cálculos;
- Saída: resultado produzido.

Exemplo (desconto):

- Entrada: preço e percentagem;
- Processo: cálculo do valor descontado;
- Saída: preço final.

Vantagem pedagógica:

- obriga a clarificar o problema antes de codificar.

---

## 9. Estratégia completa: do problema ao código

Processo recomendado em 8 passos:

1. escrever problema em 2 a 4 frases;
2. identificar E-P-S;
3. listar regras e exceções;
4. decompor em subtarefas;
5. identificar padrões reaproveitáveis;
6. escrever algoritmo/pseudocódigo;
7. converter para C;
8. testar casos normal, limite e inválido.

Atalho perigoso:

- começar em `main()` sem passar pelos passos anteriores.

---

## 10. Exemplo guiado A - Média com validação

Problema:

- ler 3 notas (0 a 20), calcular média e indicar aprovação (`>= 10`).

### 10.1 E-P-S

Entrada:

- `n1`, `n2`, `n3`.

Processo:

- validar cada nota;
- calcular média;
- comparar com limiar.

Saída:

- média + estado (aprovado/reprovado).

### 10.2 Decomposição

1. ler notas;
2. validar;
3. calcular média;
4. classificar;
5. mostrar resultado.

### 10.3 Pseudocódigo

```text
ler n1, n2, n3
se alguma nota < 0 ou > 20 então
    escrever "Notas invalidas"
    terminar
fim-se
media <- (n1 + n2 + n3) / 3
se media >= 10 então
    escrever "Aprovado"
senao
    escrever "Reprovado"
fim-se
escrever media
```

### 10.4 Código C

```c
#include <stdio.h>

int main(void) {
    float n1, n2, n3;

    printf("Introduz 3 notas: ");
    scanf("%f %f %f", &n1, &n2, &n3);

    if (n1 < 0 || n1 > 20 || n2 < 0 || n2 > 20 || n3 < 0 || n3 > 20) {
        printf("Notas invalidas. Use valores entre 0 e 20.\n");
        return 1;
    }

    float media = (n1 + n2 + n3) / 3.0f;

    if (media >= 10.0f) {
        printf("Aprovado\n");
    } else {
        printf("Reprovado\n");
    }

    printf("Media: %.2f\n", media);
    return 0;
}
```

---

## 11. Exemplo guiado B - Classificação de temperatura

Problema:

- classificar temperatura como frio, ameno ou quente.

Regras:

- `< 10` -> frio;
- `10` a `24` -> ameno;
- `>= 25` -> quente.

Código C:

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

Aprendizagem:

- mesma estrutura mental serve para muitos problemas de classificação.

---

## 12. Erros comuns e como evitar

1. querer resolver tudo de uma vez;
2. ignorar definição de entradas e saídas;
3. não tratar dados inválidos;
4. copiar código sem entender;
5. confundir detalhe técnico com objetivo do problema;
6. saltar pseudocódigo;
7. não testar casos limite.

Plano de prevenção:

- checklist E-P-S;
- algoritmo escrito antes do C;
- 3 testes mínimos por funcionalidade.

---

## 13. Mini-laboratório de pensamento computacional

Objetivo: aplicar os 4 princípios num problema real em 45 a 75 min.

Problema sugerido:

- "classificar consumo de água diário".

Passos:

1. descrever problema em 3 frases;
2. montar E-P-S;
3. decompor em 5 subtarefas;
4. identificar 3 padrões reutilizáveis;
5. escrever pseudocódigo;
6. implementar em C;
7. criar 8 testes;
8. registar erros e melhorias.

Entrega:

- um documento curto + código C funcional.

---

## 14. Exercícios (sem resolução)

### Exercício 1 - E-P-S básico

Para 8 problemas do dia a dia, identifica Entrada, Processo e Saída.

### Exercício 2 - Decomposição avançada

Decompõe "sistema de biblioteca" em 12 subtarefas com ordem lógica.

### Exercício 3 - Padrões

Identifica padrões comuns em 6 programas simples já disponíveis.

### Exercício 4 - Abstração por níveis

Escreve 3 níveis de descrição para o mesmo problema: utilizador, algoritmo e C.

### Exercício 5 - Algoritmo textual

Cria algoritmo para validação de password com 4 regras.

### Exercício 6 - Pseudocódigo

Escreve pseudocódigo para maior de 4 números com tratamento de empate.

### Exercício 7 - Conversão para C

Implementa o exercício 6 em C com mensagens claras.

### Exercício 8 - Validação de input

Refatora um programa para rejeitar valores fora de intervalo.

### Exercício 9 - Casos de teste

Define 12 testes para um algoritmo de classificação.

### Exercício 10 - Depuração orientada

Programa com bug lógico: descreve hipótese, teste e correção.

### Exercício 11 - Aplicação prática

Escolhe um problema real e aplica os 4 princípios em relatório curto.

### Exercício 12 - Revisão crítica

Recebes solução funcional mas confusa. Reescreve com melhor pensamento computacional.

### Exercício 13 - Comparação de soluções

Resolve o mesmo problema por duas abordagens e compara clareza.

### Exercício 14 - Planeamento pré-código

Proibido programar durante 20 min: prepara todo o plano antes de escrever C.

### Exercício 15 - Reflexão

Responde: "Porque pensar antes de codificar acelera o desenvolvimento?".

---

## 15. Rubrica de autoavaliação

Pontua de 1 a 5:

- identifico E-P-S com segurança;
- decomponho problemas sem perder coerência;
- reconheço padrões e reaproveito lógica;
- separo essencial de detalhe técnico;
- escrevo algoritmos claros;
- converto algoritmo para C com poucos erros;
- valido casos normais, limite e inválidos.

Interpretação:

- 7 a 16: base frágil;
- 17 a 27: base funcional;
- 28 a 35: base sólida.

---

## 16. Checklist mental antes de programar

Antes de abrir `main.c`, confirma:

- sei exatamente qual problema estou a resolver;
- defini entradas e saídas;
- escrevi regras e exceções;
- decompus em blocos pequenos;
- identifiquei padrões reutilizáveis;
- escrevi pseudocódigo;
- preparei casos de teste mínimos.

Se responderes "não" a 2 ou mais itens, ainda não é hora de programar.

---

## 17. Changelog

- **2026-04-12**: expansão completa do módulo com mais profundidade, estratégia operacional, exemplos e laboratório.
- **2026-02-23**: reescrita completa do módulo com explicação detalhada e exercícios sem resolução.
