# C (10.º Ano) - 21 · Projeto Prático: Mastermind em Consola

---

## Índice

- [0. Contexto](#0-contexto)
- [1. Desafio](#1-desafio)
- [2. Regras essenciais do jogo](#2-regras-essenciais-do-jogo)
- [3. Antes de programar: compreender o problema](#3-antes-de-programar-compreender-o-problema)
- [4. Descobrir os requisitos funcionais](#4-descobrir-os-requisitos-funcionais)
- [5. Pensar nas entradas e saídas](#5-pensar-nas-entradas-e-saídas)
- [6. Escolher estruturas de dados](#6-escolher-estruturas-de-dados)
- [7. Descobrir as funções necessárias](#7-descobrir-as-funções-necessárias)
- [8. Organizar o código](#8-organizar-o-código)
- [9. Testes obrigatórios](#9-testes-obrigatórios)
- [10. Entregáveis](#10-entregáveis)
- [11. Critérios de avaliação](#11-critérios-de-avaliação)
- [12. Melhorias opcionais](#12-melhorias-opcionais)
- [13. Erros comuns a evitar](#13-erros-comuns-a-evitar)
- [14. Changelog](#14-changelog)

---

## 0. Contexto

Vais criar uma versão em consola do jogo **Mastermind**.

Neste jogo, existe um código secreto. O jogador não conhece esse código e tenta descobri-lo através de várias tentativas.

Depois de cada tentativa, o programa dá pistas:

- quantos valores estão certos e na posição certa;
- quantos valores existem no código secreto, mas estão na posição errada.

O projeto deve ser implementado no computador.

---

## 1. Desafio

Cria um programa em C que permita jogar uma versão numérica do Mastermind.

O jogo deve correr no terminal.

O teu trabalho não é apenas escrever código. Antes de programar, tens de analisar o problema e tomar decisões sobre:

- o que o programa deve fazer;
- que dados precisa de guardar;
- que entradas recebe;
- que saídas mostra;
- que funções fazem sentido;
- como vais testar se o jogo está correto.

---

## 2. Regras essenciais do jogo

Na versão base, o jogo deve seguir estas regras:

- o código secreto tem 4 números;
- cada número está entre `1` e `6`;
- não há números repetidos no código secreto;
- o jogador introduz tentativas com 4 números;
- uma tentativa só é válida se também cumprir as regras anteriores;
- uma tentativa inválida não deve contar como tentativa usada;
- o jogador tem um número máximo de tentativas;
- o jogo termina com vitória se o jogador descobrir o código;
- o jogo termina com derrota se o jogador gastar todas as tentativas;
- o jogador pode desistir.

Exemplo de código secreto válido:

```text
2 5 1 6
```

Exemplo de tentativa:

```text
1 2 3 4
```

Exemplo de resposta do programa:

```text
Certos na posicao certa: 1
Certos na posicao errada: 2
```

Durante o jogo, o código secreto não deve ser mostrado ao jogador.

Exemplo completo da UI:

```text
=== Mastermind Numerico ===
Tentativas usadas: 2/10
1 - Inserir tentativa
0 - Desistir
Opcao: 1
==========================
Escreve 4 numeros: 2 1 4 6
Certos na posicao certa: 2
Certos na posicao errada: 1
```

---

## 3. Antes de programar: compreender o problema

Antes de escrever código, responde no teu caderno ou num pequeno documento:

1. O que significa ganhar o jogo?
2. O que significa perder o jogo?
3. O que torna uma tentativa válida?
4. O que torna uma tentativa inválida?
5. Uma tentativa inválida deve gastar uma tentativa do jogador? Porquê?
6. Que informação o jogador precisa de ver depois de cada tentativa?
7. Que informação o programa precisa de guardar, mesmo que não a mostre sempre?

Estas respostas devem orientar o teu código. Se não conseguires responder a estas perguntas, ainda não estás pronto para implementar.

---

## 4. Descobrir os requisitos funcionais

Um requisito funcional descreve algo que o programa deve fazer.

Por exemplo:

```text
O programa deve permitir ao jogador inserir uma tentativa com 4 números.
```

A partir das regras do jogo, identifica os requisitos funcionais óbvios do teu programa.

Deves escrever pelo menos 10 requisitos funcionais.

Para te ajudar, completa frases deste tipo:

1. O programa deve começar por...
2. O programa deve permitir ao jogador...
3. O programa deve validar...
4. O programa deve rejeitar...
5. O programa deve comparar...
6. O programa deve mostrar...
7. O programa deve guardar...
8. O programa deve terminar quando...
9.
10.

Exemplo de formato esperado:

| Nº  | Requisito funcional                                      |
| --- | -------------------------------------------------------- |
| 1   | O programa deve guardar um código secreto com 4 números. |
| 2   | ...                                                      |

Não escrevas requisitos demasiado vagos como:

```text
O programa deve ser bom.
```

Escreve requisitos verificáveis:

```text
O programa deve rejeitar tentativas com números repetidos.
```

---

## 5. Pensar nas entradas e saídas

Antes de programar, identifica que dados entram no programa e que informação deve aparecer no terminal.

### 5.1 Entradas

Responde:

1. O jogador precisa de introduzir o nome?
2. O jogador escolhe uma opção de menu?
3. Como introduz uma tentativa?
4. Que valores são aceites numa tentativa?
5. Que valores devem ser recusados?

Tabela sugerida:

| Entrada                      | Tipo em C | Exemplo válido | Exemplo inválido |
| ---------------------------- | --------- | -------------- | ---------------- |
| opção do menu                | `int`     | `1`            | `9`              |
| primeiro número da tentativa | `int`     | `3`            | `8`              |

### 5.2 Saídas

Responde:

1. Que mensagem aparece no início do jogo?
2. Como o programa mostra as tentativas já feitas?
3. Como mostra os valores certos na posição certa?
4. Como mostra os valores certos na posição errada?
5. Que mensagem aparece em caso de vitória?
6. Que mensagem aparece em caso de derrota?
7. Que mensagem aparece em caso de desistência?

O output não precisa de ser bonito, mas deve ser claro.

Exemplo de interação possível:

```text
=== Mastermind Numerico ===

Tentativas usadas: 2/10

1 - Inserir tentativa
0 - Desistir
Opcao: 1

Escreve 4 numeros: 2 1 4 6

Certos na posicao certa: 2
Certos na posicao errada: 1
```

---

## 6. Escolher estruturas de dados

Agora pensa nos dados que o programa precisa de guardar.

Não escolhas uma estrutura de dados só porque "parece avançada". Escolhe porque resolve uma necessidade concreta.

### 6.1 Dados do código secreto

Perguntas:

1. O código secreto tem quantos valores?
2. Todos os valores são do mesmo tipo?
3. Faz sentido guardar o código secreto num array?

### 6.2 Dados de uma tentativa

Perguntas:

1. Uma tentativa tem os mesmos 4 valores do código secreto?
2. Além dos valores introduzidos, faz sentido guardar o resultado dessa tentativa?
3. Que campos poderiam existir numa `struct` que representa uma tentativa?

### 6.3 Dados do jogo

Perguntas:

1. O programa precisa de guardar várias tentativas?
2. Como podes guardar um histórico de tentativas?
3. Que informação indica se o jogo ainda está a decorrer, terminou com vitória ou terminou com derrota?
4. Faz sentido usar um `enum` para representar o estado do jogo?

### 6.4 Restrições técnicas

Neste projeto deves usar:

- constantes com `#define` ou `const`;
- arrays estáticos;
- pelo menos uma `struct`;
- pelo menos um `enum`;
- pelo menos um array de `struct`;
- funções;
- apontadores para alterar dados dentro de funções.

Neste projeto não deves usar:

- `malloc`;
- `calloc`;
- `realloc`;
- `free`;
- listas ligadas;
- ficheiros.

---

## 7. Descobrir as funções necessárias

Uma boa função tem uma responsabilidade clara.

Antes de escrever código, divide o problema em ações pequenas.

Por exemplo, em vez de teres uma função enorme que faz tudo, podes pensar em ações como:

- mostrar as regras;
- ler uma opção;
- ler uma tentativa;
- verificar se um valor está dentro dos limites;
- verificar se há números repetidos;
- comparar uma tentativa com o código secreto;
- guardar uma tentativa no histórico;
- verificar se o jogo terminou;
- mostrar o resumo final.

Agora completa uma tabela como esta:

| Ação necessária        | Nome possível da função | Recebe dados? | Altera dados? | Devolve resultado? |
| ---------------------- | ----------------------- | ------------- | ------------- | ------------------ |
| Mostrar regras do jogo | `mostrar_regras`        | não           | não           | não                |
| Ler uma tentativa      | ...                     | sim/não       | sim/não       | sim/não            |

Critérios para escolher as funções:

- se uma parte do código tem uma responsabilidade própria, pode ser uma função;
- se precisas de repetir uma tarefa, essa tarefa deve ser uma função;
- se uma função precisa de alterar uma `struct`, deve receber um apontador;
- se uma função apenas precisa de ler dados, pode receber por valor;
- evita funções demasiado longas.

Não há apenas uma lista correta de funções. O importante é conseguires justificar a tua organização.

---

## 8. Organizar o código

Antes de começar a escrever o programa completo, decide a ordem geral do ficheiro.

Uma organização possível é:

```text
1. Includes
2. Constantes
3. Enumerações
4. Structs
5. Protótipos das funções
6. Função main
7. Implementação das funções
```

No `main`, evita colocar todos os detalhes do jogo.

O `main` deve mostrar a sequência principal:

```text
inicializar jogo
mostrar regras
enquanto o jogo estiver a decorrer:
    ler opção
    processar tentativa ou desistência
mostrar resumo final
```

Os detalhes devem ficar dentro das funções.

---

## 9. Testes obrigatórios

Antes de entregares, tens de testar o programa.

Cada teste deve indicar:

- o que estás a testar;
- que dados introduziste;
- qual era o resultado esperado;
- qual foi o resultado obtido.

Deves incluir pelo menos estes testes:

### Teste A - Valor fora do intervalo

Exemplo:

```text
1 2 3 9
```

O programa deve recusar a tentativa.

### Teste B - Número repetido

Exemplo:

```text
1 2 2 4
```

O programa deve recusar a tentativa.

### Teste C - Nenhum número certo

Usa uma tentativa que não tenha valores em comum com o código secreto.

O resultado esperado é:

```text
Certos na posicao certa: 0
Certos na posicao errada: 0
```

### Teste D - Valores certos em posições erradas

Usa uma tentativa que tenha alguns valores do código secreto, mas noutras posições.

O programa deve contar esses valores como certos na posição errada.

### Teste E - Vitória

Introduz exatamente o código secreto.

O programa deve terminar com vitória.

### Teste F - Derrota

Usa todas as tentativas sem descobrir o código.

O programa deve terminar com derrota.

### Teste G - Desistência

Escolhe a opção de desistir.

O programa deve terminar com uma mensagem adequada.

---

## 10. Entregáveis

Entregar:

1. ficheiro `.c` com o código completo;
2. lista de requisitos funcionais identificados;
3. tabela de entradas e saídas;
4. descrição das estruturas de dados escolhidas;
5. tabela das funções criadas e respetiva responsabilidade;
6. explicação curta do algoritmo usado para comparar tentativa e código secreto;
7. registo dos testes obrigatórios.

---

## 11. Critérios de avaliação

- **15%** Identificação clara dos requisitos funcionais.
- **15%** Escolha adequada de estruturas de dados.
- **20%** Implementação correta das regras do jogo.
- **15%** Organização em funções com responsabilidades claras.
- **10%** Uso correto de apontadores para alterar dados.
- **10%** Validação de entradas e tratamento de casos inválidos.
- **10%** Testes manuais completos e coerentes.
- **5%** Legibilidade, nomes claros e apresentação geral.

---

## 12. Melhorias opcionais

Depois da versão base funcionar, podes acrescentar uma ou mais melhorias:

- permitir escolher o número máximo de tentativas;
- permitir escolher dificuldade;
- esconder ou mostrar o código secreto em modo debug;
- gerar o código secreto aleatoriamente sem repetir números;
- permitir códigos com números repetidos;
- mostrar mensagens diferentes conforme o desempenho;
- criar um sistema de pontuação baseado no número de tentativas usadas;
- permitir jogar novamente sem fechar o programa.

As melhorias só devem ser feitas depois de a versão base estar correta.

---

## 13. Erros comuns a evitar

1. Começar a programar sem perceber as regras.
2. Não escrever os requisitos funcionais antes do código.
3. Mostrar o código secreto durante o jogo.
4. Contar tentativas inválidas como tentativas usadas.
5. Não validar valores fora de `1` a `6`.
6. Não validar números repetidos.
7. Confundir valores na posição certa com valores certos na posição errada.
8. Alterar uma cópia de uma `struct` em vez da estrutura original.
9. Esquecer `&` ao chamar funções que recebem apontadores.
10. Usar `.` quando a função recebeu um apontador e devia usar `->`.
11. Aceder fora dos limites dos arrays.
12. Tentar usar `malloc` antes de o tema ter sido trabalhado.

---

## 14. Changelog

- **2026-05-26**: reformulação pedagógica do enunciado para orientar os alunos na descoberta de requisitos funcionais, entradas/saídas, estruturas de dados, funções, organização e testes.
- **2026-05-26**: reformulação do projeto para Mastermind numérico em consola, alinhado com arrays, array de `struct`, `enum`, funções e apontadores antes de `malloc`.
- **2026-05-26**: reformulação anterior para jogo de consola baseado em mapa.
- **2026-04-23**: criação do mini projeto de 1 hora, versão original para trabalho em papel.
