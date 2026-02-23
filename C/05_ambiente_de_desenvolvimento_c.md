# C (10.º Ano) - 05 · Ambiente de Desenvolvimento

> **Objetivo deste ficheiro**  
> Montar, compreender e usar um ambiente de desenvolvimento em C de forma segura e organizada.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. O que é um ambiente de desenvolvimento?](#1-o-que-é-um-ambiente-de-desenvolvimento)
- [2. Componentes essenciais](#2-componentes-essenciais)
- [3. Editor/IDE](#3-editoride)
- [4. Compilador](#4-compilador)
- [5. Compilar e executar no terminal](#5-compilar-e-executar-no-terminal)
- [6. Avisos do compilador (warnings)](#6-avisos-do-compilador-warnings)
- [7. Estrutura recomendada de projeto](#7-estrutura-recomendada-de-projeto)
- [8. Introdução ao build com Makefile](#8-introdução-ao-build-com-makefile)
- [9. Introdução ao debug](#9-introdução-ao-debug)
- [10. Boas práticas de ambiente](#10-boas-práticas-de-ambiente)
- [11. Exercícios (sem resolução)](#11-exercícios-sem-resolução)
- [12. Changelog](#12-changelog)

---

## 0. Como usar este módulo

1. Verifica primeiro se `gcc` (ou `clang`) está instalado.
2. Faz o ciclo completo: editar -> compilar -> executar -> corrigir.
3. Não ignores warnings.

---

## 1. O que é um ambiente de desenvolvimento?

Conjunto de ferramentas para criar software:

- editor de código;
- compilador;
- terminal;
- depurador;
- (opcional) ferramentas de build e controlo de versão.

Sem ambiente minimamente configurado, programar fica mais lento e confuso.

---

## 2. Componentes essenciais

- **Editor/IDE**: onde escreves código.
- **Compilador**: traduz C para executável.
- **Terminal**: onde corres comandos.
- **Debugger**: ajuda a encontrar erros lógicos.

---

## 3. Editor/IDE

Recomendado para começar:

- VS Code com extensões C/C++;
- Code::Blocks;
- outro editor que permita terminal integrado.

Configurações básicas úteis:

- numeração de linhas;
- indentação de 4 espaços;
- guardar automaticamente;
- destaque de sintaxe.

---

## 4. Compilador

Compiladores comuns:

- `gcc`
- `clang`

Comando típico:

```bash
gcc -Wall -Wextra -std=c11 main.c -o app
```

Explicação:

- `-Wall -Wextra`: ativa avisos importantes;
- `-std=c11`: define versão da linguagem;
- `-o app`: nome do executável.

---

## 5. Compilar e executar no terminal

Exemplo completo:

```bash
gcc -Wall -Wextra -std=c11 main.c -o app
./app
```

Ciclo ideal:

1. altera código;
2. compila;
3. lê erros/avisos;
4. corrige;
5. executa novamente.

---

## 6. Avisos do compilador (warnings)

Warning não é "enfeite". Muitas vezes indica bug real.

Exemplos comuns:

- variável não utilizada;
- conversões perigosas de tipo;
- função sem `return` adequado.

Regra prática: tentar manter projeto com zero warnings.

---

## 7. Estrutura recomendada de projeto

```text
projeto_c/
├── src/
│   ├── main.c
│   ├── menu.c
│   └── dados.c
├── include/
│   ├── menu.h
│   └── dados.h
├── bin/
├── Makefile
└── README.md
```

Vantagens:

- organização clara;
- manutenção mais simples;
- colaboração facilitada.

---

## 8. Introdução ao build com Makefile

Exemplo básico:

```make
CC=gcc
CFLAGS=-Wall -Wextra -std=c11

app: src/main.c
	$(CC) $(CFLAGS) src/main.c -o bin/app
```

Isto evita repetir comandos longos manualmente.

---

## 9. Introdução ao debug

Depurar é investigar comportamentos errados.

Ferramentas iniciais:

- `printf` para inspecionar valores;
- breakpoints em IDE;
- execução passo a passo.

Compilação para debug:

```bash
gcc -g -Wall -Wextra -std=c11 main.c -o app
```

---

## 10. Boas práticas de ambiente

- mantém projeto em pasta dedicada;
- usa nomes claros de ficheiros;
- guarda versões com git;
- documenta como compilar e correr;
- evita código sem backup.

---

## 11. Exercícios (sem resolução)

### Exercício 1 - Verificação de ferramentas

Confirma no teu computador a versão de `gcc` (ou `clang`) e regista resultado.

### Exercício 2 - Hello World

Cria `main.c`, compila com warnings ativos e executa.

### Exercício 3 - Warning intencional

Provoca 2 warnings e depois corrige-os.

### Exercício 4 - Estrutura de pastas

Monta a estrutura `src/include/bin` para um projeto novo.

### Exercício 5 - Separação em ficheiros

Cria `main.c` + `operacoes.c` + `operacoes.h` com pelo menos 2 funções.

### Exercício 6 - Makefile simples

Cria `Makefile` para compilar o projeto do exercício 5.

### Exercício 7 - Debug com printf

Insere mensagens de debug num ciclo e explica o comportamento observado.

### Exercício 8 - Debugger da IDE

Configura breakpoint e executa passo a passo uma função simples.

### Exercício 9 - Documentação técnica

Escreve secção "Como compilar" para o `README` do teu projeto.

### Exercício 10 - Diagnóstico de erro

Recebes erro de compilação por ficheiro `.h` em falta.  
Descreve o processo de diagnóstico.

### Exercício 11 - Qualidade

Define um checklist de qualidade de ambiente antes de entregar trabalho.

### Exercício 12 - Reflexão

Explica porque um bom ambiente reduz erros mesmo para quem está a começar.

---

## 12. Changelog

- **2026-02-23**: reescrita completa com abordagem detalhada e exercícios sem resolução.
