# Memória (10.º Ano) - 04 · Heap, Stack, Frames e Execução de Código Python (v2)

> **Objetivo deste ficheiro**  
> Entender, passo a passo, como um programa Python é preparado e executado, onde vivem os dados durante a execução (**stack** e **heap**), e o que acontece em chamadas de função, retorno e recursão.  
> No fim, deves conseguir “ver” mentalmente o que está a acontecer quando o teu código corre — e usar isso para **depurar erros** com mais confiança.

---

**Pré-requisitos:** [`06_do_codigo_a_execucao_real_so_cpu_isa.md`](06_do_codigo_a_execucao_real_so_cpu_isa.md)

## Índice

- [1. O mapa geral: processo, código, stack e heap](#1-o-mapa-geral-processo-código-stack-e-heap)
- [2. O que realmente acontece quando corres um `.py`](#2-o-que-realmente-acontece-quando-corres-um-py)
- [3. Compilar vs interpretar (com mais detalhe)](#3-compilar-vs-interpretar-com-mais-detalhe)
- [4. Python: modelo híbrido (fonte -> bytecode -> execução)](#4-python-modelo-híbrido-fonte---bytecode---execução)
- [5. Bytecode e pasta `__pycache__`](#5-bytecode-e-pasta-__pycache__)
- [6. PVM: o "motor" de execução do Python](#6-pvm-o-motor-de-execução-do-python)
- [7. Memória de execução: stack vs heap](#7-memória-de-execução-stack-vs-heap)
- [8. Stack frames: o que um frame contém](#8-stack-frames-o-que-um-frame-contém)
- [9. Tornar o invisível visível: `locals()`, `id()` e `dis`](#9-tornar-o-invisível-visível-locals-id-e-dis)
- [10. Exemplo completo de chamada de função (com desenho)](#10-exemplo-completo-de-chamada-de-função-com-desenho)
- [11. Exemplo com várias funções (pilha em camadas)](#11-exemplo-com-várias-funções-pilha-em-camadas)
- [12. Retorno, vida dos objetos e garbage collection](#12-retorno-vida-dos-objetos-e-garbage-collection)
- [13. Recursão e `RecursionError`: causa real](#13-recursão-e-recursionerror-causa-real)
- [14. Debug real: o traceback é a stack “impressa”](#14-debug-real-o-traceback-é-a-stack-impressa)
- [15. Erros comuns de alunos neste tema](#15-erros-comuns-de-alunos-neste-tema)
- [16. Exercícios de consolidação](#16-exercícios-de-consolidação)
- [17. Resumo final](#17-resumo-final)
- [18. Changelog](#18-changelog)

---

## 1. O mapa geral: processo, código, stack e heap

### 1.1 Quando corres Python, crias um “processo”

Um **processo** é, de forma simples, “um programa a correr”.

Esse processo tem:

- **código** a ser executado,
- **memória** disponível para o programa,
- **estado de execução** (o que está a fazer agora).

### 1.2 Dentro desse processo, pensa em duas “zonas” lógicas

- **Stack (pilha de execução)**: guarda o contexto das funções ativas (frames).
- **Heap**: guarda os objetos (listas, dicionários, strings, instâncias, etc.).

> Nota importante: isto não são “peças físicas separadas”.  
> É uma divisão **lógica** útil para entender o que acontece durante a execução.

Mais à frente, vamos ver o que são na realidade estas duas “zonas” e como interagem.

---

## 2. O que realmente acontece quando corres um `.py`

Quando clicas em “Run” num ficheiro Python, o processo real (simplificado) é:

1. o interpretador Python abre o ficheiro `.py`;
2. verifica sintaxe;
3. converte para **bytecode**;
4. a máquina virtual do Python executa o bytecode passo a passo;
5. durante execução, cria objetos, chama funções e interage com o sistema operativo.

Ponto importante:

> O CPU não executa texto Python diretamente.  
> Ele executa o **interpretador Python**, e é esse interpretador que “faz acontecer” as ações do teu código.
> Ou seja, o código que tu escreves vive numa "bolha" que é o interpretador. O Interpretador é o que tem acesso direto ao sistema operativo e à CPU, e o teu código é traduzido para algo que o interpretador consegue entender e executar.

---

## 3. Compilar vs interpretar

### Compilar

Compilar significa, em programação, transformar o código fonte de um determinado nível de abstração (ex.: Python) para outro nível (ex.: código máquina ou bytecode) **antes** de executar.

- traduz código fonte para um formato executável **antes** de correr;
- tende a gerar artefactos de compilação (objetos/executável).

### Interpretar

Interpretar significa ler o código fonte e executar as instruções **durante a execução**. As instruções são analisadas e executadas passo a passo.

- analisa e executa durante a execução;
- tende a ser mais dinâmico no desenvolvimento.

### Porque confunde em Python?

Porque Python faz os dois em sequência:

- compila para bytecode;
- executa bytecode na PVM.

Ou seja: chamar Python “só interpretado” é uma simplificação útil, mas incompleta. No entanto essa simplificação pode induzir a erros de compreensão sobre o que acontece.

---

## 4. Python: modelo híbrido (fonte -> bytecode -> execução)

Fluxo mental:

`código fonte (.py)`  
→ `bytecode`  
→ `PVM executa`  
→ `efeitos no programa (prints, cálculos, ficheiros, rede...)`

Isto explica:

- portabilidade de Python;
- porque existe `__pycache__`;
- porque stack/heap aparecem durante execução e não no texto fonte.

---

## 5. Bytecode e pasta `__pycache__`

**Bytecode**:

- é uma representação intermédia;
- não é código-fonte legível;
- não é instrução nativa final da CPU.

Basicamente é uma linguagem de baixo nível que a PVM entende e executa. A PVM vai ler o bytecode e transformar as instruções numa série de operações que o sistema operativo e a CPU conseguem executar.

A pasta `__pycache__` guarda ficheiros `.pyc` (quando aplicável) para acelerar arranques futuros.

Por exemplo, imagina que tens este código:

```python
def soma(a, b):
    return a + b

print(soma(2, 3))
```

Quando executamos este código, ele vai ser compilado em ByteCode, que vai resultar em algo como:

```text
global _start

section .data
    args dq 1, 2, 3, 4
    n    dq 4
    newline db 10

section .bss
    buf resb 32

section .text

soma:
    xor rax, rax
    xor rcx, rcx
.loop:
    cmp rcx, rdi
    jge .done
    add rax, [rsi + rcx*8]
    inc rcx
    jmp .loop
.done:
    ret

utoa_rax_to_buf:
    lea rdi, [buf + 31]
    mov byte [rdi], 0
    mov rbx, 10
    cmp rax, 0
    jne .convert
    dec rdi
    mov byte [rdi], '0'
    mov rsi, rdi
    mov rdx, 1
    ret
.convert:
.loop2:
    xor rdx, rdx
    div rbx
    add dl, '0'
    dec rdi
    mov [rdi], dl
    cmp rax, 0
    jne .loop2
    mov rsi, rdi
    lea rdx, [buf + 31]
    sub rdx, rsi
    ret

_start:
    mov rdi, [n]
    lea rsi, [args]
    call soma
    call utoa_rax_to_buf
    mov rax, 1
    mov rdi, 1
    syscall
    mov rax, 1
    mov rdi, 1
    lea rsi, [newline]
    mov rdx, 1
    syscall
    mov rax, 60
    xor rdi, rdi
    syscall
```

Se reparares, este código, embora pareça mais complicado para nós humanos, é uma divisão de uma tarefa mais complexa (o código original) em operações mais simpless (soma, conversão de inteiro para string, escrita na saída, etc.) que a máquina virtual do Python pode entender e executar.

Sempre que compilamos um bloco de código, ele vai ser convertido numa linguagem de mais baixo nível que, por norma, é uma decomposição em operações mais simples. Eventualmente essas operações simples vão ser traduzidas para chamadas ao sistema operativo e instruções de máquina que o CPU pode executar.

---

## 6. PVM: o "motor" de execução do Python

A PVM (Python Virtual Machine):

- lê bytecode;
- decide que operação runtime executar;
- coordena criação/uso de objetos Python;
- pede serviços ao sistema operativo quando necessário (ex.: abrir ficheiro).

Analogia simples:

- teu código é a receita;
- bytecode é a receita em formato técnico;
- PVM é o cozinheiro que executa passos.

---

## 7. ISA (Instruction Set Architecture)

A ISA é o conjunto de instruções que o CPU entende diretamente.

Depois do código Python ser compilado para bytecode, ele é injetado e exectuado pela PVM. A PVM, por sua vez, vai interpretar o bytecode e comunicar com o Sistema Operativo para realizar as ações necessárias (como alocar memória, ler/escrever ficheiros, etc.).

A seguir, o SO vai fazer a ponte de ligação entre essas ações e as instruções de máquina que o CPU entende. Essas instruções estão definidas pela ISA do CPU (ex.: x86, ARM).

Ou seja, a ISA é basicamente um conjunto de comandos simples que o CPU pode executar diretamente.
Por exemplo, no nosso programa com a função `soma`vai ser decomposto em operações simples que existem na ISA, como:

- carregar valores em registos;
- realizar operações de adição;
- escrever resultados na memória;
- chamar funções do sistema operativo para imprimir resultados, etc.
  O CPU não tem uma instrução “soma de listas” ou “imprime string”, mas tem instruções para manipular dados e chamar o sistema operativo, e é isso que a PVM usa para implementar as funcionalidades do Python.

### 8 Diagrama sobre todo o processo usando Python

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1) PROGRAMADOR                                                              │
│ Escreve código Python (.py)                                                 │
└───────────────┬─────────────────────────────────────────────────────────────┘
                │
                v
┌─────────────────────────────────────────────────────────────────────────────┐
│ 2) FICHEIRO NO DISCO (SSD/HDD)                                              │
│ - O .py é guardado como bytes                                               │
│ - Não está "a correr", está só armazenado                                   │
└───────────────┬─────────────────────────────────────────────────────────────┘
                │ (Quando carregas em Run / python ficheiro.py)
                v
┌─────────────────────────────────────────────────────────────────────────────┐
│ 3) SISTEMA OPERATIVO (SO)                                                   │
│ Cria um PROCESSO para o Python (o interpretador)                            │
│ - Reserva memória para o processo                                           │
│ - Carrega o interpretador Python (executável) para a RAM                    │
│ - Dá permissões, prepara stack/heap, etc.                                   │
└───────────────┬─────────────────────────────────────────────────────────────┘
                │
                v
┌─────────────────────────────────────────────────────────────────────────────┐
│ 4) INTERPRETADOR PYTHON (programa C) A CORRER NA RAM                        │
│ Este é o programa REAL que o CPU executa diretamente.                       │
│ O interpretador lê o teu .py e faz:                                         │
│ a) parsing/validação de sintaxe                                             │
│ b) compilação para BYTECODE (.pyc)                                          │
└───────────────┬─────────────────────────────────────────────────────────────┘
                │
                │ (Opcional: guarda bytecode em **pycache** para acelerar)
                v
┌─────────────────────────────────────────────────────────────────────────────┐
│ 5) BYTECODE (instruções da PVM)                                             │
│ - Não é código de máquina do CPU                                            │
│ - É um formato intermédio: "instruções para a máquina virtual do Python"    │
└───────────────┬─────────────────────────────────────────────────────────────┘
                │
                v
┌─────────────────────────────────────────────────────────────────────────────┐
│ 6) PVM (Python Virtual Machine)                                             │
│ É uma parte do interpretador que faz um loop do tipo:                       │
│ FETCH bytecode -> DECODE -> EXECUTE                                         │
│                                                                             │
│ Para cada instrução de bytecode, a PVM faz operações em objetos Python:     │
│ - cria/usa ints, strings, listas, dicts, etc. (heap)                        │
│ - chama funções (frames na stack)                                           │
│ - pede ao SO ações (I/O: prints, ficheiros, rede, etc.)                     │
└───────────────┬─────────────────────────────────────────────────────────────┘
                │
                │ (Aqui acontece a “ponte” crucial:)
                │ Bytecode NÃO é executado pelo CPU.
                │ Quem executa bytecode é o interpretador (programa nativo).
                v
┌─────────────────────────────────────────────────────────────────────────────┐
│ 7) CPU (ISA: x86/ARM, etc.)                                                 │
│ O CPU só entende INSTRUÇÕES DE MÁQUINA (assembly) da sua ISA.               │
│                                                                             │
│ O que o CPU executa mesmo é:                                                │
│ - o interpretador Python (código máquina)                                   │
│ - + chamadas ao Sistema Operativo                                           │
│                                                                             │
│ Ou seja: o CPU "percebe" o teu programa Python porque executa               │
│ um programa (interpretador) que IMPLEMENTA o significado do Python.         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 9. Memória de execução: stack vs heap (versão mais detalhada)

### 9.1 Antes de stack/heap: “onde é que isto existe afinal?”

Quando corres um programa Python, o Sistema Operativo cria um **processo**.

Um processo tem (entre outras coisas) um **espaço de endereços virtual**:

- imagina uma “régua gigante” numerada (0, 1, 2, 3, …) de endereços;
- **o teu programa vê essa régua como se fosse “a sua memória”**;
- essa memória é **virtual**: é uma abstração controlada pelo Sistema Operativo e pelo CPU.

Isto chama-se **memória virtual**.
Onde fica a **memória virtual**? Na RAM, claro, mas o processo não tem acesso direto a “endereços físicos” da RAM. Ele só tem acesso a “endereços virtuais”.

#### Quem é que transforma “endereços virtuais” em RAM real?

Aqui entra o trio:

- **CPU** (com uma unidade chamada **MMU — Memory Management Unit**)
- **Sistema Operativo** (define as regras)
- **Tabelas de páginas** (_page tables_) do processo

Quando o teu programa “acede ao endereço virtual X”, a **MMU traduz** X para “um sítio na RAM” (ou dispara erro se não existir mapeamento/permissão).

> Tradução para alunos:  
> o programa trabalha com **endereços virtuais**, e o sistema (MMU + SO) faz a ponte para a RAM real.

#### Então stack/heap “são onde”?

A **stack** e o **heap** são **regiões (intervalos) dentro do espaço de endereços virtual do processo**.

Ou seja:

- não são chips separados,
- não são “uma RAM diferente”,
- são “zonas” do mapa de memória do processo, com **usos e regras diferentes**.

Uma thread é uma linha de execução dentro do processo, e cada thread tem a sua própria stack. O heap é partilhado entre threads.

---

### 9.2 O “mapa” típico de memória de um processo

```text
Endereços (virtual) mais altos
┌───────────────────────────────────────────┐
│ Stack (da thread)                         │  ← cresce tipicamente para baixo
│  - frames das funções                     │
│  - variáveis temporárias de execução      │
└───────────────────────────────────────────┘

┌───────────────────────────────────────────┐
│ (zona livre / mapeamentos / bibliotecas)  │
└───────────────────────────────────────────┘

┌───────────────────────────────────────────┐
│ Heap                                      │  ← cresce tipicamente para cima
│  - objetos criados dinamicamente          │
│  - listas, dicts, strings, instâncias     │
└───────────────────────────────────────────┘

┌───────────────────────────────────────────┐
│ Código do programa / bibliotecas          │
│ (texto + dados globais)                   │
└───────────────────────────────────────────┘
Endereços (virtual) mais baixos
```

Notas importantes:

- **cada thread tem a sua própria stack**;
- o **heap é “do processo”** (pode ser partilhado entre threads);
- “stack cresce para baixo e heap para cima” é comum, mas o detalhe exato pode variar.

---

### 9.3 O que é a Stack, em concreto?

A **stack** é uma região de memória usada para gerir **execução de funções**.

Características essenciais:

- existe uma stack **por thread**;
- funciona como uma pilha: **LIFO** (_Last In, First Out_);
- a CPU tem um registo especial: o **SP (Stack Pointer)**, que aponta para o “topo” atual da stack.

#### Como é que a stack é “acedida”?

O acesso é feito por instruções normais da CPU (ler/escrever memória), mas guiadas pelo:

- **SP (Stack Pointer)**
- e pelas regras de chamadas de função (convenções de chamada)

Quando uma função é chamada:

- o sistema “reserva espaço” na stack para o contexto dessa chamada;
- isso cria um **stack frame** (vamos detalhar no capítulo 8).

Quando a função termina:

- esse espaço é libertado “de uma vez” (na prática, o SP volta atrás).

> Por isso é que a stack é muito eficiente:  
> alocar/libertar na stack é quase só mexer num número (o SP).

---

### 9.4 O que é a Heap, em concreto?

O **heap** é a região onde vivem **objetos criados dinamicamente**, que podem sobreviver para além de uma função.

Em Python, quase tudo é objeto:

- `int`, `str`, `list`, `dict`, instâncias, etc.

Então, em geral:

- **os objetos vivem na heap**,
- e as variáveis (nomes) guardam **referências** para esses objetos.
- A stack guarda as referências locais, e o heap guarda os dados reais.
  Por exemplo, quando fazes `x = [1, 2, 3]`, o objeto `[1, 2, 3]` vive no heap, e `x` é uma referência para esse objeto que está na stack.

#### Quem “controla” o heap? (dois níveis)

1. **Sistema Operativo + MMU**

- garantem que o processo só acede a memória permitida;
- fazem a tradução virtual → RAM;
- aplicam permissões (por exemplo, zonas que não podem ser executadas).

2. **Runtime do Python + alocador de memória**

- decide “onde colocar” cada objeto no heap;
- gere blocos livres/ocupados;
- evita pedir ao SO “um bocadinho de memória” a cada objeto (isso seria lento).

Em CPython (o Python mais comum), existe gestão interna para objetos pequenos para ser rápida (conceito: “pools/arenas”).

#### Porque é que o heap é “mais complexo” do que a stack?

Porque no heap:

- alocas e libertas objetos em momentos imprevisíveis;
- podes ter fragmentação (buracos);
- precisas de metadados (“tamanho do bloco”, “livre/ocupado”, etc.);
- precisas de garbage collection (limpar objetos que já não são usados).

---

### 9.5 Resumo prático

- **Stack**: contexto de chamadas de função (**frames**), cresce/encolhe com chamadas/returns, é muito rápida.
- **Heap**: objetos dinâmicos (listas, dicts, strings…), vivem enquanto houver referências, gerida pelo runtime/GC.
- Ambas são zonas dentro do **espaço de memória do processo**.
- O acesso é sempre via CPU a endereços (virtuais), traduzidos pela MMU e controlados pelo SO.
- Em linguagens como C, o programador pode alocar memória na stack (variáveis locais) ou no heap (com `malloc`), mas em Python o programador só interage com objetos no heap, e a stack é gerida automaticamente para as chamadas de função.

---

### 9.6 Exemplos de tipos de dados e onde vivem

```python
x = 10          # int (imutável) → heap
y = "Olá"       # str (imutável) → heap
z = [1, 2, 3]   # O Z é uma referência → stack; a lista é um objeto → heap. O Z aponta para a lista no heap.
```

## Bloco para colar no Módulo 04 — “Para onde vai cada coisa” (Stack/Heap + Referências + Órfãos)

> **Objetivo deste bloco**  
> Ligar diretamente o que foi dito no Módulo 03 (referências/refcount/GC) com o mapa Stack/Heap do Módulo 04.  
> Aqui vais “ver” onde fica o **nome**, onde fica a **referência**, e onde fica o **objeto** (e os dados dele).

---

### (Sugestão de secção nova) 9. Para onde vai cada coisa: nomes, referências e objetos

#### 9.1 O caso mais importante: criar uma lista

Código:

```python
a = [10, 20, 30]
```

Modelo mental (sem tecnicismos desnecessários):

- **`a` (nome)** fica no **frame atual** (stack frame).
- o **objeto lista** fica no **heap**.
- dentro da lista existem **referências** para os objetos `10`, `20`, `30` (que também são objetos no heap).

##### Desenho mental

**Stack (frame atual):**

```text
[ frame atual ]
a  ───────────────►  (objeto lista)
```

**Heap (objetos):**

```text
(objeto lista)  ── contém referências ──►  (10)   (20)   (30)
```

> Em Python, uma lista não “guarda números dentro dela” como se fosse uma caixa de valores.  
> Ela guarda **referências** para objetos.

---

#### 9.2 O que acontece quando fazes alias?

```python
a = [10, 20, 30]
b = a
```

Agora existem **dois nomes** a apontar para o **mesmo objeto lista**.

**Stack:**

```text
[ frame atual ]
a  ──► (mesma lista)
b  ──► (mesma lista)
```

**Heap:**

```text
(lista) ──► (10) (20) (30)
```

Consequência:

```python
b.append(99)
print(a)  # também mudou
```

Porque `a` e `b` são duas referências para o mesmo objeto no heap.

---

#### 9.3 “A lista desaparece quando a função termina?” (caso A: não devolves)

```python
def f():
    temp = [1, 2, 3]
    # não devolvemos

f()
```

Durante a função:

- `temp` existe no frame de `f` (stack)
- a lista existe no heap

Quando `f()` termina:

- o frame de `f` é removido (stack encolhe)
- `temp` deixa de existir
- a lista fica sem referências externas → fica **órfã** → pode ser removida

---

#### 9.4 Caso B: devolves a lista (ela continua viva)

```python
def criar():
    temp = [1, 2, 3]
    return temp

x = criar()
```

- o frame `criar` desaparece
- mas `x` (no frame global) continua a apontar para o mesmo objeto lista
- logo a lista continua viva no heap

---

#### 9.5 Onde entra a contagem de referências neste “mapa”?

Sempre que aparece uma referência nova para o mesmo objeto, o “peso” (refcount) sobe.

Exemplo:

```python
a = [1, 2]
b = a      # +1 referência
del a      # -1 referência (b ainda existe)
del b      # -1 referência -> pode chegar a 0 -> objeto elegível para remoção
```

> A stack (frames) é o sítio onde vivem muitos dos nomes/referências.  
> O heap é o sítio onde vive o objeto.  
> O refcount é a contagem de “quantos fios” ainda ligam ao objeto.

---

#### 9.6 O caso especial: ciclos (porque é que o GC é necessário)

```python
def ciclo():
    a = []
    a.append(a)  # a lista aponta para si própria

ciclo()
```

Quando a função termina:

- o nome `a` desaparece (frame sai da stack)
- mas o objeto lista ainda tem uma referência interna para si mesmo (ciclo)

Isto pode impedir o refcount de chegar a 0.  
O Garbage Collector entra para detetar que aquilo já não é alcançável e limpar.

---

#### 9.7 Exercício rápido (para consolidar “quem está onde”)

1. Desenha stack/heap para isto:

```python
a = [1, 2]
b = a
```

2. Explica o que acontece aqui:

```python
def f():
    x = [1, 2, 3]
f()
```

3. Explica porque este caso pode precisar de GC:

```python
def g():
    a = []
    a.append(a)
g()
```

## 8. Stack frames: o que um frame contém (versão mais detalhada)

### 8.1 O que é “uma frame” em concreto?

Uma **frame** (_stack frame_) é o “pacote” de informação necessário para **uma chamada de função** funcionar.

Pensa numa frame como uma “ficha” que guarda:

- quais são os parâmetros desta chamada?
- quais são as variáveis locais?
- onde é que eu volto quando acabar?
- qual é o estado atual desta execução?

Em termos simples:

> **Cada chamada de função cria 1 frame.**  
> Quando a função retorna, esse frame sai da stack.

---

### 8.2 O que uma stack frame costuma conter (nível baixo / CPU)

Em muitas linguagens, uma frame costuma conter:

- **endereço de retorno** (para onde voltar após terminar)
- **parâmetros** (ou referências para eles)
- **variáveis locais**
- **registos guardados** (estado temporário da CPU)

Isto é o “lado hardware/baixo nível”: a CPU precisa destes dados para continuar a execução corretamente.

---

### 8.3 Em Python há um detalhe crucial: duas camadas de “stack”

Em Python, acontecem duas coisas ao mesmo tempo:

#### Camada A — a stack “real” do interpretador (C stack)

O interpretador Python é um programa (geralmente em C).
Quando ele chama funções internas, usa stack frames normais _do próprio interpretador_ (como qualquer programa).

#### Camada B — as frames de execução do Python (frames Python)

Além disso, para permitir:

- tracebacks,
- `locals()`,
- exceções,
- depuração,

o Python mantém uma estrutura própria para cada chamada de função Python: um **Python frame**.

> Para o aluno, o mais importante:  
> a “frame” que aparece no traceback é a **frame Python** (o contexto lógico da tua função).

---

### 8.4 O que um Python frame contém (nível Python)

De forma conceptual (didática), um frame Python guarda:

- **referência para o código da função** (o que tem de executar)
- **variáveis locais** (o “ambiente” local)
- **referência para globais** (ambiente do módulo)
- **posição atual de execução** (qual passo/instrução vem a seguir)
- **ligação ao frame anterior** (quem chamou esta função)
- (internamente) uma “pilha de valores” usada para avaliar expressões (modelo da VM)

Não precisas decorar a lista — o essencial é:

- uma frame não é magia,
- é uma **estrutura** que representa “uma chamada de função em execução”.

---

### 8.5 Como é que frames são criadas e destruídas?

#### Criar frame (quando chamas uma função)

1. O Python cria um novo contexto de execução para a função.
2. Liga esse contexto ao anterior (para formar a pilha).
3. Começa a executar a função.

#### Destruir frame (quando a função retorna)

1. A função termina.
2. O Python “desempilha” essa frame.
3. As variáveis locais deixam de existir **nesse contexto**.

Atenção:

- objetos criados podem continuar vivos no heap **se existirem referências fora da frame**.

---

### 8.6 Frame vs objeto: a confusão que dá bugs

Regra que resolve a maior parte das dúvidas:

- **Frame** = contexto temporário de execução de uma função (stack)
- **Objeto** = dados reais (lista, dict, string…) (heap)

Quando a função termina:

- o frame desaparece,
- mas os objetos só desaparecem se não houver referências.

Exemplo clássico:

```python
def criar():
    lista = [1, 2, 3]
    return lista

x = criar()
```

- a frame de `criar` desaparece
- mas a lista continua viva porque `x` aponta para ela

---

### 8.7 Como é que isto aparece em debug (traceback)?

Quando dá erro, o Python mostra um traceback com a “pilha de chamadas”:

- `a()` chamou `b()`
- `b()` chamou `c()`
- `c()` falhou aqui

Isto é literalmente a stack de frames representada em texto.

---

### 8.8 Mini-diagrama das frames em camadas

```text
Stack (frames) no momento em que c() está a correr:

Topo
[ frame de c ]   locals: ...
[ frame de b ]   locals: ...
[ frame de a ]   locals: ...
[ frame global ] ...
Base
```

Quando `c()` termina, sai do topo. Depois sai `b()`, depois sai `a()`.

---

### 8.9 Resumo do capítulo 8

- Frame = “pacote” de estado para uma chamada de função.
- Frames são empilhadas (LIFO).
- Em Python, frames explicam traceback e ajudam no debug.
- Frame desaparece no return; objetos podem continuar vivos no heap.

---

## 9. Tornar o invisível visível: `locals()`, `id()` e `dis`

Esta secção é para veres o que normalmente fica escondido.

### 9.1 Ver as variáveis do frame atual com `locals()`

Dentro de uma função:

```python
def exemplo(a):
    b = a + 1
    print("locals:", locals())
    return b

exemplo(10)
```

O `locals()` devolve um dicionário com as variáveis locais do frame.
Isto ajuda a pensar: “ok, este frame tem estas referências”.

### 9.2 Ver identidade (não “endereço físico”) com `id()`

```python
x = [1, 2, 3]
y = x

print(id(x))
print(id(y))
```

Se os `id` forem iguais, é uma pista forte de que `x` e `y` apontam para o **mesmo objeto**.

> Nota pedagógica: pensa em `id()` como **identidade do objeto**.  
> Em muitas implementações, pode coincidir com detalhes internos, mas não escrevas lógica a depender disso.

### 9.3 Ver bytecode (curiosidade controlada) com `dis`

Não precisas perceber tudo, mas é útil para perceber que existe uma “camada intermédia”.

```python
import dis

def soma(a, b):
    return a + b

dis.dis(soma)
```

Vais ver instruções internas que a PVM executa.

---

## 10. Exemplo completo de chamada de função (com desenho)

```python
def dobrar(n):
    resultado = n * 2
    return resultado

x = 5
y = dobrar(x)
print(y)
```

### Passo a passo

1. `x = 5`
    - no frame global existe a referência `x`
    - `x` aponta para o objeto `5` (imutável)

2. chama `dobrar(x)`
    - cria-se um frame novo na stack: frame `dobrar`
    - `n` aponta para o mesmo objeto que `x` (5)

3. `resultado = n * 2`
    - cria-se (ou obtém-se) um objeto `10`
    - `resultado` aponta para `10`

4. `return resultado`
    - devolve-se a referência para `10`
    - o frame `dobrar` é removido da stack

5. `y` (no frame global) passa a apontar para `10`

### Desenho mental

**Stack (frames):**

Durante a execução de `dobrar`:

```
Topo
[ dobrar ]   n -> (5)      resultado -> (10)
[ global ]   x -> (5)      y -> (?)
Base
```

Depois do `return`:

```
Topo
[ global ]   x -> (5)      y -> (10)
Base
```

**Heap (objetos):**

```
(5)   (10)
```

---

## 11. Exemplo com várias funções (pilha em camadas)

```python
def c():
    return "fim"

def b():
    return c()

def a():
    return b()

print(a())
```

Evolução da stack:

1. frame global chama `a()` → `[global, a]`
2. `a()` chama `b()` → `[global, a, b]`
3. `b()` chama `c()` → `[global, a, b, c]`
4. `c()` retorna → remove `c`
5. `b()` retorna → remove `b`
6. `a()` retorna → remove `a`
7. global recebe valor final

Isto é LIFO puro: **a última função a entrar é a primeira a sair**.

---

## 12. Retorno, vida dos objetos e garbage collection

Erro mental clássico:

> “A função acabou, logo o objeto desapareceu.”

Nem sempre.

```python
def criar():
    dados = [1, 2, 3]
    return dados

z = criar()   # a lista continua viva
```

O frame de `criar` desaparece, mas a lista continua porque `z` aponta para ela.

### Regra simples

- um objeto vive enquanto houver **referências** para ele;
- se ficar sem referências, torna-se elegível para limpeza (contagem de referências + GC).

> Nota: aqui a ligação é ao mapa stack/heap/frames; os detalhes de refcount e ciclos estão no Módulo 03.

---

## 13. Recursão e `RecursionError`: causa real

Cada chamada recursiva cria um frame novo.

Sem condição de paragem adequada:

- frames acumulam;
- o Python atinge o limite de recursão;
- surge `RecursionError`.

Exemplo incorreto:

```python
def infinito(n):
    return infinito(n + 1)
```

Exemplo correto (com caso base):

```python
def contar(n):
    if n == 0:
        return 0
    return contar(n - 1)
```

Ponto-chave:

- o problema não é “falta de RAM”;
- o problema é **lógica sem paragem**, que continua a empilhar frames.

---

## 14. Debug real: o traceback é a stack “impressa”

Quando há erro, Python mostra um **traceback**.
Isso é (quase literalmente) a lista das chamadas de função que estavam ativas.

Exemplo:

```python
def c():
    return 10 / 0

def b():
    return c()

def a():
    return b()

a()
```

O traceback mostra:

- o erro (divisão por zero),
- e o caminho `a()` → `b()` → `c()`.

### Como ler (regra prática)

- o traceback é o histórico de chamadas;
- encontras o ponto do problema na linha onde o erro aconteceu (no fundo da cadeia do erro).

Isto liga stack frames a uma coisa prática: **depuração**.

---

## 15. Erros comuns de alunos neste tema

### Erro 1

“Stack e heap são duas peças físicas separadas.”

**Correção:** são regiões lógicas do espaço de memória do processo (modelo mental útil).

### Erro 2

“Variável local guarda o objeto inteiro.”

**Correção:** guarda uma **referência** para o objeto.

### Erro 3

“Return copia sempre tudo.”

**Correção:** muitas vezes passa referências (modelo mental certo para este nível).

### Erro 4

“Se está no heap, nunca sai.”

**Correção:** sai quando deixa de haver referências e o runtime faz limpeza.

### Erro 5

“Recursão falha porque o PC não tem RAM.”

**Correção:** falha porque empilha frames até ao limite (`RecursionError`).

---

## 16. Exercícios de consolidação

> Faz primeiro sem olhar para explicações anteriores. O objetivo é confirmares se a “imagem mental” ficou certa.

### Exercício 1 — o objeto continua vivo?

```python
def f():
    a = [1, 2]
    return a

x = f()
print(x)
```

Responde:

1. A lista continua viva depois do `return`? Porquê?
2. O frame `f` continua vivo? Porquê?

### Exercício 2 — desenha a stack

```python
def c(): return 1
def b(): return c()
def a(): return b()

a()
```

Desenha a stack no momento em que `c()` está a executar.

### Exercício 3 — recursão

Explica porque isto dá erro:

```python
def g():
    return g()
```

E como corrigias (em 1 frase).

### Exercício 4 — traceback (stack visível)

Cria um erro propositado com 3 funções em cadeia (`a()` chama `b()` chama `c()`).
Depois explica o traceback com as tuas palavras:

- “o que me está a dizer?”
- “onde está a linha que interessa?”

### Exercício 5 — referências e alias

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

Responde:

1. Porque é que `a` também muda?
2. O que quer dizer “alias” neste contexto?

---

## 17. Resumo final

- Python não executa texto fonte diretamente; executa via **bytecode + PVM**.
- Cada chamada de função cria um **frame** na stack.
- Objetos vivem tipicamente no **heap**; frames guardam referências locais.
- `return` remove o frame chamado, mas objetos podem continuar vivos se forem referenciados fora.
- Recursão sem caso base acumula frames até `RecursionError`.
- Traceback é a stack “visível” e é uma ferramenta essencial de debug.

---

**A seguir:** [`03_gestao_de_memoria_em_python_referencias_mutabilidade_gc.md`](03_gestao_de_memoria_em_python_referencias_mutabilidade_gc.md)

---

## 18. Changelog

- **2026-02-04**: versão inicial do módulo 04.
- **2026-02-05**: v2 (mapa mental + observação com ferramentas + debug + exercícios).
