# C (10.º Ano) - 01 · Ciclo de Vida do Software

> **Objetivo deste ficheiro**  
> Perceber, com linguagem simples e exemplos concretos, como nasce, evolui e se mantém um programa de computador.

---

## Índice

- [0. Como estudar este módulo](#0-como-estudar-este-módulo)
- [1. O que é o ciclo de vida do software?](#1-o-que-é-o-ciclo-de-vida-do-software)
- [2. Fase 1 - Requisitos](#2-fase-1---requisitos)
- [3. Fase 2 - Análise e planeamento](#3-fase-2---análise-e-planeamento)
- [4. Fase 3 - Desenho da solução](#4-fase-3---desenho-da-solução)
- [5. Fase 4 - Implementação (codificação)](#5-fase-4---implementação-codificação)
- [6. Fase 5 - Testes](#6-fase-5---testes)
- [7. Fase 6 - Entrega e operação](#7-fase-6---entrega-e-operação)
- [8. Fase 7 - Manutenção e evolução](#8-fase-7---manutenção-e-evolução)
- [9. Exemplo guiado: mini sistema de gestão de biblioteca](#9-exemplo-guiado-mini-sistema-de-gestão-de-biblioteca)
- [10. Erros comuns de iniciantes](#10-erros-comuns-de-iniciantes)
- [11. Checklist rápido](#11-checklist-rápido)
- [12. Exercícios (sem resolução)](#12-exercícios-sem-resolução)
- [13. Changelog](#13-changelog)

---

## 0. Como estudar este módulo

1. Lê primeiro as fases por ordem.
2. Em cada fase, tenta responder: "que documento/resultado sai daqui?".
3. No exemplo guiado, tenta imaginar como farias o projeto na tua turma.
4. No fim, resolve os exercícios por ordem crescente de dificuldade.

---

## 1. O que é o ciclo de vida do software?

O ciclo de vida do software é o "caminho" de um programa:

- começa numa necessidade (problema real);
- passa por planeamento e desenvolvimento;
- chega ao utilizador;
- continua com correções e melhorias.

Em palavras simples: **um programa não acaba quando compila**. Ele só faz sentido quando resolve bem um problema e continua utilizável ao longo do tempo.

---

## 2. Fase 1 - Requisitos

Nesta fase respondemos: **o que o software deve fazer?**

Tipos de requisitos:

- funcionais: ações que o sistema executa (ex.: "registar aluno");
- não funcionais: qualidade/limites (ex.: "responder em menos de 2s");
- restrições: tecnologia, prazo, orçamento, regras legais.

Exemplo de requisitos simples:

- O programa deve permitir inserir nomes de livros.
- O programa deve permitir pesquisar por título.
- O programa não deve perder dados ao fechar.

Se requisitos estiverem mal escritos, todo o projeto sofre depois.

---

## 3. Fase 2 - Análise e planeamento

Aqui transformamos ideias em trabalho organizado.

Decisões comuns:

- dividir o problema em módulos;
- identificar riscos (pouco tempo, pouco conhecimento);
- definir calendário (o que fazer em cada semana);
- escolher ordem de implementação.

Saídas típicas:

- lista de tarefas;
- prioridades;
- cronograma simples.

---

## 4. Fase 3 - Desenho da solução

Aqui pensamos na arquitetura antes de codificar tudo.

Para 10.º ano, desenho pode ser:

- fluxograma;
- pseudocódigo;
- esquema de ficheiros (`main.c`, `menu.c`, `dados.c`).

Perguntas úteis:

- que dados vou guardar?
- que funções preciso criar?
- como o utilizador interage com o programa?

---

## 5. Fase 4 - Implementação (codificação)

É a fase de escrever código, mas com método.

Boas práticas:

- implementar por partes pequenas;
- compilar frequentemente;
- escrever nomes claros em variáveis/funções;
- comentar apenas o que não é óbvio.

Exemplo de organização:

- `main.c`: fluxo principal;
- `menu.c`: interação com utilizador;
- `dados.c`: guardar e processar dados.

---

## 6. Fase 5 - Testes

Testar não é "correr uma vez e aceitar".

Tipos básicos:

- teste normal: comportamento esperado;
- teste de limite: valores extremos (0, máximo);
- teste inválido: entradas erradas (texto quando esperava número).

Um bom teste responde:

- entrada usada;
- resultado esperado;
- resultado obtido;
- passou/falhou.

---

## 7. Fase 6 - Entrega e operação

Nesta fase o software é disponibilizado.

Pode incluir:

- instruções de execução;
- versão estável;
- documentação para utilizador;
- recolha de feedback.

Entrega sem documentação costuma gerar muitas dúvidas desnecessárias.

---

## 8. Fase 7 - Manutenção e evolução

Depois da entrega aparecem:

- bugs reais;
- novos pedidos;
- melhoria de desempenho;
- adaptação a novas necessidades.

Tipos de manutenção:

- corretiva: corrigir erro;
- adaptativa: ajustar ao ambiente;
- evolutiva: adicionar funcionalidades;
- preventiva: melhorar estrutura para reduzir problemas futuros.

---

## 9. Exemplo guiado: mini sistema de gestão de biblioteca

Problema: escola quer registar livros emprestados.

Aplicação das fases:

1. Requisitos
- registar livro (título, autor, estado);
- marcar empréstimo/devolução;
- listar livros disponíveis.

2. Planeamento
- semana 1: menu + estrutura de dados;
- semana 2: operações básicas;
- semana 3: testes e melhorias.

3. Desenho
- `struct Livro` com campos essenciais;
- funções para inserir/listar/atualizar;
- menu em ciclo.

4. Implementação
- primeiro inserir/listar;
- depois empréstimo/devolução;
- por fim persistência em ficheiro.

5. Testes
- livro normal;
- lista vazia;
- índice inválido.

6. Entrega
- instruções de compilação e execução.

7. Manutenção
- adicionar pesquisa por autor.

---

## 10. Erros comuns de iniciantes

1. Começar logo a codificar sem requisitos.
2. Fazer tudo num único ficheiro gigante.
3. Não testar entradas inválidas.
4. Mudar muitas coisas ao mesmo tempo e perder controlo.
5. Entregar sem instruções mínimas.

---

## 11. Checklist rápido

- O problema está claramente definido?
- Há lista de funcionalidades obrigatórias?
- O trabalho foi dividido em tarefas?
- Existe plano de testes?
- Há registo de alterações?

Se respondeste "não" a várias perguntas, volta às fases anteriores.

---

## 12. Exercícios (sem resolução)

### Exercício 1 - Identificar fases

Lê a situação: "A turma quer criar uma app de registo de material da sala."  
Escreve uma frase para cada fase do ciclo de vida explicando o que farias.

### Exercício 2 - Requisitos funcionais

Define 8 requisitos funcionais para um programa de gestão de alunos.

### Exercício 3 - Requisitos não funcionais

Define 5 requisitos não funcionais para o mesmo programa.

### Exercício 4 - Planeamento semanal

Cria um plano de 3 semanas para desenvolver um mini projeto em C.

### Exercício 5 - Riscos

Lista 5 riscos do teu projeto e uma estratégia de mitigação para cada um.

### Exercício 6 - Desenho de módulos

Propõe estrutura de ficheiros para um programa com menu, dados e ficheiros.

### Exercício 7 - Casos de teste

Cria 10 casos de teste para um programa que calcula médias de notas.

### Exercício 8 - Priorização

Classifica 12 tarefas em: essencial, importante, opcional.

### Exercício 9 - Correção de processo

Recebes um projeto sem testes e sem requisitos escritos.  
Escreve um plano de recuperação em 7 passos.

### Exercício 10 - Manutenção corretiva vs evolutiva

Para 8 mudanças propostas, indica se são corretivas ou evolutivas e justifica.

### Exercício 11 - Documento de entrega

Escreve a estrutura (títulos) de um documento de entrega para utilizador final.

### Exercício 12 - Reflexão

Explica por que razão "programa a funcionar" não é o mesmo que "projeto concluído".

---

## 13. Changelog

- **2026-02-23**: reescrita completa do módulo com versão detalhada, foco pedagógico e exercícios sem resolução.
