# C - 05 · Ambiente de Desenvolvimento

> **Objetivo deste ficheiro**  
> Montar, compreender e usar um ambiente de desenvolvimento em C com método profissional e prática consistente.

---

## Índice

- [0. Como estudar este módulo](#0-como-estudar-este-módulo)
- [1. Resultados de aprendizagem](#1-resultados-de-aprendizagem)
- [2. O que é um ambiente de desenvolvimento?](#2-o-que-é-um-ambiente-de-desenvolvimento)
- [3. Ferramentas essenciais e o papel de cada uma](#3-ferramentas-essenciais-e-o-papel-de-cada-uma)
- [4. Verificação e preparação do ambiente](#4-verificação-e-preparação-do-ambiente)
- [5. Fluxo de trabalho mínimo (editar -> compilar -> executar -> corrigir)](#5-fluxo-de-trabalho-mínimo-editar---compilar---executar---corrigir)
- [6. O que acontece quando compilas C](#6-o-que-acontece-quando-compilas-c)
- [7. Compilação disciplinada: flags, perfis e qualidade](#7-compilação-disciplinada-flags-perfis-e-qualidade)
- [8. Warnings: leitura, diagnóstico e correção](#8-warnings-leitura-diagnóstico-e-correção)
- [9. Projeto multi-ficheiro: organização correta](#9-projeto-multi-ficheiro-organização-correta)
- [10. Makefile: automatizar build sem dor](#10-makefile-automatizar-build-sem-dor)
- [11. Debug: de `printf` a debugger](#11-debug-de-printf-a-debugger)
- [12. Qualidade extra: sanitizers e análise estática (introdução)](#12-qualidade-extra-sanitizers-e-análise-estática-introdução)
- [13. Git no ambiente de desenvolvimento](#13-git-no-ambiente-de-desenvolvimento)
- [14. Tabela de problemas frequentes (troubleshooting)](#14-tabela-de-problemas-frequentes-troubleshooting)
- [15. Mini-laboratório guiado (completo)](#15-mini-laboratório-guiado-completo)
- [16. Exercícios (sem resolução)](#16-exercícios-sem-resolução)
- [17. Rubrica de autoavaliação](#17-rubrica-de-autoavaliação)
- [18. Checklist final de entrega técnica](#18-checklist-final-de-entrega-técnica)
- [19. Changelog](#19-changelog)

---

## 0. Como estudar este módulo

1. Lê as secções 1 a 6 para perceberes o "porquê" técnico.
2. Executa os comandos das secções 7 a 11 no teu computador.
3. Faz o mini-laboratório completo da secção 15 sem saltar etapas.
4. No fim, resolve exercícios da secção 16 por ordem.
5. Usa a rubrica e checklist para validar se o teu ambiente está realmente sólido.

---

## 1. Resultados de aprendizagem

No final deste módulo, deves conseguir:

- explicar a diferença entre editor, compilador, linker e debugger;
- compilar com flags de qualidade (`-Wall -Wextra -std=c11`);
- organizar projeto em `src/`, `include/`, `bin/`;
- separar código em múltiplos ficheiros `.c` e `.h`;
- criar e usar um `Makefile` funcional;
- diagnosticar erros de compilação e warnings comuns;
- fazer debug básico com `printf` e com breakpoints;
- manter um fluxo de trabalho técnico limpo e repetível.

---

## 2. O que é um ambiente de desenvolvimento?

É o conjunto de ferramentas e práticas que te permite criar software com controlo.

Não é apenas "ter um editor instalado".

Um ambiente de desenvolvimento inclui:

- ferramentas (editor/IDE, compilador, terminal, debugger, build);
- estrutura de projeto (pastas, ficheiros, nomes claros);
- disciplina de trabalho (compilar cedo, corrigir warnings, testar sempre).

Ideia-chave:

- ambiente fraco -> mais erros escondidos;
- ambiente sólido -> erro aparece cedo e é mais fácil corrigir.

---

## 3. Ferramentas essenciais e o papel de cada uma

### 3.1 Editor ou IDE

Função: escrever e navegar código.

Exemplos para início:

- VS Code (com extensão C/C++);
- Code::Blocks;
- CLion (quando disponível);
- outros editores simples com terminal integrado.

Configuração mínima recomendada:

- numeração de linhas;
- indentação com 4 espaços;
- mostrar caracteres invisíveis (opcional, mas útil);
- guardar automático ou hábito de `Ctrl+S` frequente.

### 3.2 Compilador

Função: traduzir C para linguagem de máquina.

Compiladores comuns:

- `gcc`
- `clang`

Se usares bem as flags, o compilador torna-se um orientador técnico.

### 3.3 Linker

Função: juntar vários objetos (`.o`) num executável final.

Muitos iniciantes confundem:

- "compila" -> gera objeto;
- "linka" -> gera executável.

### 3.4 Terminal

Função: executar comandos de build, execução e diagnóstico.

Vantagem pedagógica:

- entendes realmente o processo;
- ficas menos dependente de botões da IDE.

### 3.5 Debugger

Função: parar execução, inspecionar variáveis e avançar passo a passo.

Ferramentas típicas:

- `gdb` (Linux, muitas distros)
- `lldb` (comum em ambientes com clang/macOS)
- debugger integrado da IDE

### 3.6 Build system (Make)

Função: automatizar compilação e evitar comandos repetitivos.

Para projetos pequenos e médios, `make` é excelente para ganhar disciplina.

---

## 4. Verificação e preparação do ambiente

Antes de programar, confirma ferramentas.

```bash
gcc --version
clang --version
make --version
git --version
```

Notas:

- não precisas ter `gcc` e `clang` ao mesmo tempo;
- basta um compilador C funcional + `make` + terminal + editor.

Cria uma pasta de trabalho limpa:

```bash
mkdir -p projeto_c_inicial
cd projeto_c_inicial
```

Estrutura inicial recomendada:

```bash
mkdir -p src include bin docs
touch src/main.c README.md Makefile
```

---

## 5. Fluxo de trabalho mínimo (editar -> compilar -> executar -> corrigir)

Fluxo curto e repetível:

1. editar pequena parte;
2. compilar imediatamente;
3. corrigir erros e warnings;
4. executar;
5. validar comportamento.

Exemplo base:

```c
#include <stdio.h>

int main(void) {
    printf("Ola, C!\n");
    return 0;
}
```

Compilar e correr:

```bash
gcc -Wall -Wextra -std=c11 src/main.c -o bin/app
./bin/app
```

Regra profissional adaptada a iniciantes:

- nunca deixes warnings acumularem;
- nunca programes muito tempo sem compilar.

---

## 6. O que acontece quando compilas C

Compilar C não é um passo único. Há uma pipeline.

### 6.1 Pré-processamento

Processa `#include`, `#define`, condicionais.

```bash
gcc -E src/main.c -o main.i
```

### 6.2 Compilação para assembly

Traduz C para assembly.

```bash
gcc -S src/main.c -o main.s
```

### 6.3 Montagem (assembly -> objeto)

Gera ficheiro objeto.

```bash
gcc -c src/main.c -o main.o
```

### 6.4 Linkagem

Junta objetos e bibliotecas num executável.

```bash
gcc main.o -o bin/app
```

Porque isto importa numa fase inicial?

- ajuda a perceber erros de linker;
- ajuda a perceber porque multi-ficheiro exige organização;
- fortalece compreensão da linguagem C como linguagem compilada.

---

## 7. Compilação disciplinada: flags, perfis e qualidade

### 7.1 Flags base recomendadas

```bash
gcc -Wall -Wextra -std=c11 -g src/main.c -o bin/app
```

Significado:

- `-Wall`: ativa muitos warnings úteis;
- `-Wextra`: warnings adicionais;
- `-std=c11`: define standard da linguagem;
- `-g`: informação de debug para debugger.

### 7.2 Flags com mais rigor

```bash
gcc -Wall -Wextra -Wpedantic -std=c11 -g src/main.c -o bin/app
```

Opcional (mais exigente):

- `-Werror` transforma warning em erro;
- útil para treino disciplinado, mas pode ser duro no início.

### 7.3 Perfil debug vs perfil release

Perfil debug:

```bash
gcc -Wall -Wextra -Wpedantic -std=c11 -g -O0 src/main.c -o bin/app_debug
```

Perfil release:

```bash
gcc -Wall -Wextra -Wpedantic -std=c11 -O2 src/main.c -o bin/app_release
```

Ideia:

- `-O0` facilita debug;
- `-O2` otimiza para desempenho.

---

## 8. Warnings: leitura, diagnóstico e correção

Warning bom é warning lido e corrigido.

### 8.1 Warning: variável não utilizada

Código problemático:

```c
int main(void) {
    int x = 10;
    return 0;
}
```

Correção possível:

- remover variável;
- ou usá-la de forma útil.

### 8.2 Warning: função sem `return` adequado

Código problemático:

```c
int dobro(int n) {
    if (n > 0) {
        return n * 2;
    }
}
```

Correção:

```c
int dobro(int n) {
    if (n > 0) {
        return n * 2;
    }
    return 0;
}
```

### 8.3 Warning: conversão de tipos arriscada

Código problemático:

```c
int idade = 17;
char c = idade;
```

Correção:

- evitar conversão se não fizer sentido;
- converter conscientemente e justificar.

### 8.4 Warning por formato errado em `printf`/`scanf`

Código problemático:

```c
float media = 14.5f;
printf("%d\n", media);
```

Correção:

```c
printf("%.2f\n", media);
```

### 8.5 Estratégia de diagnóstico

Sempre que aparecer warning:

1. lê a mensagem completa;
2. identifica ficheiro + linha;
3. percebe causa real (não apenas sintoma);
4. corrige e recompila;
5. confirma que não surgiram warnings novos.

---

## 9. Projeto multi-ficheiro: organização correta

Problema típico de iniciantes:

- tudo em `main.c`;
- projeto cresce e fica difícil manter.

Modelo recomendado:

```text
projeto_c/
├── src/
│   ├── main.c
│   └── operacoes.c
├── include/
│   └── operacoes.h
├── bin/
├── Makefile
└── README.md
```

### 9.1 Header com include guard

`include/operacoes.h`

```c
#ifndef OPERACOES_H
#define OPERACOES_H

int somar(int a, int b);
int subtrair(int a, int b);

#endif
```

### 9.2 Implementação

`src/operacoes.c`

```c
#include "operacoes.h"

int somar(int a, int b) {
    return a + b;
}

int subtrair(int a, int b) {
    return a - b;
}
```

### 9.3 Uso na `main`

`src/main.c`

```c
#include <stdio.h>
#include "operacoes.h"

int main(void) {
    int a = 12;
    int b = 5;

    printf("Soma: %d\n", somar(a, b));
    printf("Subtracao: %d\n", subtrair(a, b));

    return 0;
}
```

### 9.4 Compilação manual multi-ficheiro

```bash
gcc -Wall -Wextra -Wpedantic -std=c11 -Iinclude src/main.c src/operacoes.c -o bin/app
```

Repara no `-Iinclude`: diz ao compilador onde encontrar headers próprios.

---

## 10. Makefile: automatizar build sem dor

Quando já tens 2 ou mais ficheiros `.c`, Makefile deixa de ser opcional e passa a ser produtividade.

Exemplo recomendado para início sério:

```make
CC      = gcc
CFLAGS  = -Wall -Wextra -Wpedantic -std=c11
DBGFLAGS= -g -O0
RELFLAGS= -O2
INCLUDES= -Iinclude
SRC     = src/main.c src/operacoes.c
BIN     = bin/app

.PHONY: all debug release run clean

all: debug

debug:
	$(CC) $(CFLAGS) $(DBGFLAGS) $(INCLUDES) $(SRC) -o $(BIN)

release:
	$(CC) $(CFLAGS) $(RELFLAGS) $(INCLUDES) $(SRC) -o $(BIN)

run: debug
	./$(BIN)

clean:
	rm -f $(BIN)
```

Comandos úteis:

```bash
make
make run
make release
make clean
```

Erros comuns no Makefile:

1. usar espaços em vez de TAB nas receitas;
2. esquecer `.PHONY` em targets não-ficheiro;
3. esquecer `-Iinclude` quando usas headers próprios.

---

## 11. Debug: de `printf` a debugger

Debug não é "adivinhar". É testar hipóteses com método.

### 11.1 Método `printf` (primeiro nível)

Útil para:

- confirmar valores de variáveis;
- verificar se ciclo entra/sai corretamente;
- rastrear fluxo por blocos (`if`, `else`, loops).

Exemplo:

```c
printf("DEBUG i=%d soma=%d\n", i, soma);
```

Boas práticas:

- marca mensagens de debug com prefixo claro (`DEBUG:`);
- remove ou comenta no final para não poluir output final.

### 11.2 Debugger (segundo nível)

Compila com símbolos:

```bash
gcc -Wall -Wextra -Wpedantic -std=c11 -g -Iinclude src/main.c src/operacoes.c -o bin/app
```

Comandos básicos de debugger (conceito geral):

- `break <linha|funcao>`: criar breakpoint;
- `run`: iniciar execução;
- `next`: próxima linha sem entrar em função;
- `step`: entra em função;
- `print variavel`: ver valor;
- `continue`: continuar até próximo breakpoint.

Se usares IDE, estes comandos aparecem como botões.

### 11.3 Estratégia de debug em 5 passos

1. reproduzir bug de forma consistente;
2. reduzir o cenário ao menor caso possível;
3. observar estado (variáveis, condições, índices);
4. corrigir causa raiz;
5. testar novamente caso normal + caso limite.

---

## 12. Qualidade extra: sanitizers e análise estática (introdução)

Mesmo numa fase inicial, vale conhecer ferramentas que apanham erros difíceis.

### 12.1 AddressSanitizer / UndefinedBehaviorSanitizer

Compilação de diagnóstico:

```bash
gcc -Wall -Wextra -Wpedantic -std=c11 -g -fsanitize=address,undefined src/main.c -o bin/app_san
```

Pode ajudar a apanhar:

- acessos fora dos limites;
- uso de memória inválida;
- comportamentos indefinidos comuns.

### 12.2 Análise estática (visão breve)

Ferramentas como `cppcheck` analisam código sem executar.

Não substituem testes, mas complementam.

---

## 13. Git no ambiente de desenvolvimento

Git não é só para equipas grandes; é segurança para quem está a aprender.

Fluxo mínimo:

```bash
git init
git add .
git commit -m "inicio do projeto C"
```

Ciclo recomendado durante trabalho:

1. altera pouco;
2. compila/testa;
3. commit com mensagem objetiva.

Exemplo de mensagens:

- `adiciona modulo de operacoes`
- `corrige warning de formato em printf`
- `cria makefile com perfis debug/release`

`.gitignore` inicial útil:

```gitignore
bin/
*.o
*.out
*.exe
```

---

## 14. Tabela de problemas frequentes (troubleshooting)

| Sintoma | Causa provável | Como resolver |
|---|---|---|
| `fatal error: operacoes.h: No such file or directory` | include path em falta | compilar com `-Iinclude` e confirmar nome do ficheiro |
| `undefined reference to 'somar'` | ficheiro `.c` da função não foi ligado | incluir `src/operacoes.c` no comando ou no Makefile |
| `permission denied` ao executar | binário sem permissão ou caminho errado | confirmar `./bin/app` e permissões |
| `expected ';'` | ponto e vírgula em falta | ir à linha indicada e verificar linha anterior |
| `Segmentation fault` | acesso inválido à memória | reproduzir, usar debug e validar índices/apontadores |
| Makefile: `missing separator` | espaços em vez de TAB | substituir espaços por TAB nas receitas |

Estratégia geral para erros:

1. lê a primeira mensagem de erro com atenção;
2. corrige o primeiro erro antes dos seguintes;
3. recompila;
4. repete até zero erros e zero warnings relevantes.

---

## 15. Mini-laboratório guiado (completo)

Objetivo: montar mini projeto "Calculadora simples" com estrutura correta, multi-ficheiro, Makefile e debug.

### 15.1 Passo A - Criar estrutura

```bash
mkdir -p lab_calc/src lab_calc/include lab_calc/bin
cd lab_calc
```

### 15.2 Passo B - Criar `include/calc.h`

```c
#ifndef CALC_H
#define CALC_H

int soma(int a, int b);
int sub(int a, int b);
int mult(int a, int b);

#endif
```

### 15.3 Passo C - Criar `src/calc.c`

```c
#include "calc.h"

int soma(int a, int b) {
    return a + b;
}

int sub(int a, int b) {
    return a - b;
}

int mult(int a, int b) {
    return a * b;
}
```

### 15.4 Passo D - Criar `src/main.c`

```c
#include <stdio.h>
#include "calc.h"

int main(void) {
    int a, b;

    printf("Primeiro numero: ");
    scanf("%d", &a);

    printf("Segundo numero: ");
    scanf("%d", &b);

    printf("Soma = %d\n", soma(a, b));
    printf("Subtracao = %d\n", sub(a, b));
    printf("Multiplicacao = %d\n", mult(a, b));

    return 0;
}
```

### 15.5 Passo E - Criar `Makefile`

```make
CC=gcc
CFLAGS=-Wall -Wextra -Wpedantic -std=c11
DBG=-g -O0
INCLUDES=-Iinclude
SRC=src/main.c src/calc.c
BIN=bin/app

.PHONY: all run clean

all:
	$(CC) $(CFLAGS) $(DBG) $(INCLUDES) $(SRC) -o $(BIN)

run: all
	./$(BIN)

clean:
	rm -f $(BIN)
```

### 15.6 Passo F - Compilar, executar e testar

```bash
make
make run
```

Testes mínimos sugeridos:

- entrada normal: `3` e `2`;
- zero: `0` e `5`;
- negativos: `-4` e `2`;
- valores maiores: `1000` e `250`.

### 15.7 Passo G - Injetar erro e depurar

Experiência pedagógica:

1. altera de propósito uma função para devolver resultado errado;
2. recompila;
3. deteta com testes;
4. corrige e confirma.

Aprendizagem real acontece aqui: erro controlado + diagnóstico.

---

## 16. Exercícios (sem resolução)

### Exercício 1 - Inventário do ambiente

Regista versões de compilador, make e git. Explica em 5 linhas para que serve cada ferramenta.

### Exercício 2 - Primeiro build limpo

Compila `hello world` com `-Wall -Wextra -std=c11`. Entrega comando usado e evidência de execução.

### Exercício 3 - Anatomia da compilação

Executa `-E`, `-S`, `-c` e explica em texto curto o ficheiro gerado em cada etapa.

### Exercício 4 - Warnings intencionais

Cria 3 warnings diferentes e corrige-os todos. Documenta: warning, causa, correção.

### Exercício 5 - Projeto multi-ficheiro

Separa um programa em pelo menos 2 ficheiros `.c` e 1 `.h` com include guard.

### Exercício 6 - Erro de linker

Provoca `undefined reference` e descreve o processo de resolução.

### Exercício 7 - Makefile funcional

Cria Makefile com targets `debug`, `release`, `run`, `clean`.

### Exercício 8 - Diagnóstico de include path

Provoca erro de header não encontrado e corrige com `-Iinclude`.

### Exercício 9 - Debug com `printf`

Escolhe um bug lógico simples, usa prints de debug e apresenta conclusão.

### Exercício 10 - Debugger com breakpoint

Usa breakpoint numa função e regista o valor de 3 variáveis durante execução.

### Exercício 11 - Perfil de build

Compara binário debug e release: tamanho, comportamento e utilidade.

### Exercício 12 - Sanitizer

Compila com `-fsanitize=address,undefined`, executa e descreve o que observaste.

### Exercício 13 - Git básico aplicado

Inicializa repositório, faz 4 commits com mensagens técnicas claras.

### Exercício 14 - Projeto final curto do módulo

Cria mini aplicação em C com:

- estrutura `src/include/bin`;
- pelo menos 3 funções próprias;
- Makefile;
- README com instruções de compilação/execução;
- zero warnings no perfil debug.

### Exercício 15 - Reflexão técnica

Responde em 15 a 20 linhas: "Porque um bom ambiente de desenvolvimento reduz bugs antes de eles chegarem ao utilizador?"

---

## 17. Rubrica de autoavaliação

Classifica cada critério de 1 (fraco) a 5 (forte):

- sei compilar no terminal sem depender da IDE;
- compreendo diferença entre erro e warning;
- consigo corrigir warnings comuns sem ajuda direta;
- consigo trabalhar com projeto multi-ficheiro;
- consigo usar Makefile para evitar comandos repetitivos;
- consigo fazer debug básico com método;
- mantenho projeto versionado com git;
- entrego projeto com instruções técnicas claras.

Interpretação rápida:

- 8 a 16 pontos: base ainda frágil (repetir laboratório);
- 17 a 28 pontos: base funcional (praticar consistência);
- 29 a 40 pontos: base sólida (pronto para módulos seguintes).

---

## 18. Checklist final de entrega técnica

Antes de considerares o módulo fechado:

- compilaste com `-Wall -Wextra -Wpedantic -std=c11`;
- o projeto executa sem erros;
- warnings relevantes corrigidos;
- estrutura de pastas está coerente;
- headers têm include guard;
- Makefile tem targets essenciais;
- README explica como compilar e correr;
- repositório git contém histórico legível.

Se algum item falhar, não é fim do mundo: é sinal claro do que corrigir primeiro.

---

## 19. Changelog

- **2026-04-12**: expansão completa do módulo com foco em profundidade técnica, prática guiada, troubleshooting, laboratório e critérios de autoavaliação.
- **2026-02-23**: reescrita completa com abordagem detalhada e exercícios sem resolução.
