# C (10.º Ano) - 11 · Funcionalidades de um Editor de Texto

> **Objetivo deste ficheiro**  
> Aprender a usar o editor como ferramenta de produtividade real, reduzindo erros e tempo de desenvolvimento em C.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. Porque o editor importa?](#1-porque-o-editor-importa)
- [2. Funcionalidades essenciais](#2-funcionalidades-essenciais)
- [3. Funcionalidades para C](#3-funcionalidades-para-c)
- [4. Pesquisa e substituição inteligente](#4-pesquisa-e-substituição-inteligente)
- [5. Navegação entre ficheiros e símbolos](#5-navegação-entre-ficheiros-e-símbolos)
- [6. Formatação e estilo](#6-formatação-e-estilo)
- [7. Terminal integrado e tarefas de build](#7-terminal-integrado-e-tarefas-de-build)
- [8. Debug no editor (visão inicial)](#8-debug-no-editor-visão-inicial)
- [9. Boas práticas de utilização](#9-boas-práticas-de-utilização)
- [10. Changelog](#10-changelog)

---

## 0. Como usar este módulo

1. Configura o editor antes de projetos grandes.
2. Pratica atalho por atalho.
3. Usa o terminal integrado diariamente.

---

## 1. Porque o editor importa?

Editor não é só "sítio para escrever".

Editor bem configurado:

- acelera escrita;
- reduz erros de sintaxe;
- facilita navegação no projeto;
- integra compilação e debug.

---

## 2. Funcionalidades essenciais

- abrir projeto por pasta;
- numeração de linhas;
- indentação automática;
- pesquisa global;
- múltiplos cursores;
- histórico de alterações.

---

## 3. Funcionalidades para C

- realce de sintaxe C;
- autocompletar de funções/bibliotecas;
- ver assinatura de funções;
- navegação para definição/declaracão;
- integração com compilador.

---

## 4. Pesquisa e substituição inteligente

Usos reais:

- renomear variável globalmente;
- encontrar usos de função;
- corrigir padrão repetido de erro.

Cuidado: antes de "replace all", confirma contexto.

---

## 5. Navegação entre ficheiros e símbolos

Projetos C crescem rápido com `.c` e `.h`.

Ferramentas úteis:

- "Go to definition";
- "Go to references";
- painel de símbolos por função.

Isto evita perder tempo a procurar manualmente.

---

## 6. Formatação e estilo

Define padrão da turma/equipa:

- 4 espaços;
- chavetas consistentes;
- comprimento máximo de linha;
- nomes claros para funções/variáveis.

Código formatado melhora leitura e revisão.

---

## 7. Terminal integrado e tarefas de build

Vantagens:

- não precisas alternar aplicações;
- compilas e vês erros no mesmo local;
- podes criar comandos automáticos.

Exemplo de tarefa comum:

```bash
gcc -Wall -Wextra -std=c11 src/main.c -o bin/app
```

---

## 8. Debug no editor (visão inicial)

Conceitos:

- breakpoint;
- execução passo a passo;
- inspeção de variáveis.

Objetivo: encontrar causa do erro, não apenas "apagar sintomas".

---

## 9. Boas práticas de utilização

- aprende 10 atalhos essenciais;
- configura tema legível (sem cansar visão);
- mantém extensões necessárias, evita excesso;
- usa snippets para padrões repetidos.

---

## 10. Changelog

- **2026-02-23**: reescrita completa do módulo com foco pedagógico e exercícios sem resolução.
