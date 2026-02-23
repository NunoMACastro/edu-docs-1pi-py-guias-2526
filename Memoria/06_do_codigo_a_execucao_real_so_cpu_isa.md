# Memória (10.º Ano) - 06 · Do Código à Execução Real: SO, CPU, ISA e Ficheiros

> **Objetivo deste ficheiro**  
> Perceber o caminho completo desde o código escrito por uma pessoa até à execução real no computador, incluindo sistema operativo, processador, código de máquina e o que acontece ao abrir/editar/guardar ficheiros.

---

**Pré-requisitos:** [`02_ram_rom_binario_bytes_enderecos.md`](02_ram_rom_binario_bytes_enderecos.md)

## Índice

- [0. Como usar este ficheiro](#0-como-usar-este-ficheiro)
- [1. Visão global: do código à execução](#1-visão-global-do-código-à-execução)
- [2. Código-fonte, bytecode e código de máquina](#2-código-fonte-bytecode-e-código-de-máquina)
- [3. Binário vs código de máquina](#3-binário-vs-código-de-máquina)
- [4. Papel do sistema operativo (SO)](#4-papel-do-sistema-operativo-so)
- [5. Loader: carregar programa para memória](#5-loader-carregar-programa-para-memória)
- [6. Processo vs thread](#6-processo-vs-thread)
- [7. CPU em ação: fetch, decode, execute + ISA](#7-cpu-em-ação-fetch-decode-execute--isa)
- [8. Mini tabela ISA (nível introdutório)](#8-mini-tabela-isa-nível-introdutório)
- [9. Caso real: abrir um programa (ex.: Word)](#9-caso-real-abrir-um-programa-ex-word)
- [10. Caso real: abrir um ficheiro no programa](#10-caso-real-abrir-um-ficheiro-no-programa)
- [11. Caso real: editar e guardar ficheiro](#11-caso-real-editar-e-guardar-ficheiro)
- [12. Caso real: fechar programa](#12-caso-real-fechar-programa)
- [13. O que isto muda no teu raciocínio de programador](#13-o-que-isto-muda-no-teu-raciocínio-de-programador)
- [14. Resumo final](#14-resumo-final)
- [15. Changelog](#15-changelog)

---

## 0. Como usar este ficheiro

Este módulo é de integração: junta hardware + memória + execução.

Estratégia:

1. Lê a secção 1 e fixa o fluxo global;
2. depois aprofunda cada peça (SO, loader, CPU, ISA);
3. no fim, valida com os casos reais (abrir/editar/guardar ficheiro).

---

## 1. Visão global: do código à execução

Fluxo simplificado:

1. pessoa escreve código-fonte (ex.: Python, C, Java);
2. esse código é convertido para um formato executável no sistema;
3. o sistema operativo carrega o programa em memória;
4. CPU executa instruções de máquina;
5. programa interage com memória, disco, teclado, ecrã, rede, etc.

Ideia-chave:

> No fim da cadeia, quem executa é sempre a CPU, através de instruções de máquina.

O mapa mental de stack/heap/frames e execução em Python está no [`04_heap_stack_frames_e_execucao_python.md`](04_heap_stack_frames_e_execucao_python.md).

---

## 2. Código-fonte, bytecode e código de máquina

### Código-fonte

É o texto que o programador escreve.

Exemplo:

```python
print("Olá")
```

### Bytecode (quando aplicável)

Em linguagens como Python, há um passo intermédio (bytecode para máquina virtual).

### Código de máquina

É o formato que a CPU entende diretamente (instruções da arquitetura dela).

Resumo em linha:

`código-fonte -> (compilar / interpretar / VM) -> código de máquina -> CPU executa`

---

## 3. Binário vs código de máquina

### Binário

É representação em 0 e 1 de qualquer informação:

- texto;
- imagens;
- números;
- áudio;
- instruções.

### Código de máquina

É binário com significado de instrução para a CPU, definido pela ISA.

Conclusão:

- todo código de máquina é binário;
- nem todo binário é código de máquina.

Exemplo:

- `01000001` pode representar a letra `A` (dados);
- outra sequência binária pode representar "somar registos" (instrução).

---

## 4. Papel do sistema operativo (SO)

O SO é o gestor do computador.

Funções relevantes aqui:

- criar e terminar processos;
- gerir memória;
- gerir acesso a disco;
- controlar permissões e isolamento;
- escalonar execução na CPU.

Sem SO moderno, programas não teriam esta gestão organizada.

---

## 5. Loader: carregar programa para memória

Quando abres um programa, o loader (com apoio do SO) faz, de forma simplificada:

1. localiza o executável no disco;
2. cria um processo;
3. mapeia secções do programa para memória (código, dados, etc.);
4. prepara stack e heap iniciais;
5. define ponto de entrada;
6. entrega execução à CPU.

Isto acontece em milissegundos, normalmente invisível para o utilizador.

---

## 6. Processo vs thread

### Processo

Instância de programa em execução, com espaço de memória próprio.

### Thread

Fluxo de execução dentro de um processo.

Um processo pode ter várias threads (ex.: interface + tarefas em paralelo).

Regra útil:

- processos isolam melhor;
- threads comunicam mais facilmente dentro do mesmo processo.

---

## 7. CPU em ação: fetch, decode, execute + ISA

A CPU repete continuamente:

1. fetch (buscar instrução);
2. decode (interpretar);
3. execute (executar).

Mas interpretar segundo **que regras**?

Segundo a ISA (Instruction Set Architecture), ou seja, o "vocabulário de instruções" que aquela CPU suporta.

Exemplos de famílias ISA:

- x86-64
- ARM64

Se a instrução não estiver na ISA da CPU, ela não a executa diretamente.

---

## 8. Mini tabela ISA (nível introdutório)

> Isto é conceptual, não é para decorar assembly.

| Instrução (exemplo) | Ideia                    | Efeito simplificado                        |
| ------------------- | ------------------------ | ------------------------------------------ |
| `LOAD R1, [addr]`   | carregar dado da memória | R1 recebe valor no endereço `addr`         |
| `ADD R1, R2`        | somar registos           | R1 passa a ter R1 + R2                     |
| `STORE [addr], R1`  | guardar em memória       | valor de R1 vai para `addr`                |
| `JMP label`         | salto                    | execução continua noutra posição de código |

Estas ideias já chegam para perceber como um programa "se mexe" na CPU.

---

## 9. Caso real: abrir um programa (ex.: Word)

Fluxo simplificado:

1. clicas no ícone;
2. SO encontra executável no disco;
3. loader cria processo e carrega partes para RAM;
4. CPU começa a executar instruções;
5. interface gráfica aparece;
6. dados frequentes podem ir para cache (CPU / sistema).

---

## 10. Caso real: abrir um ficheiro no programa

Exemplo: abrir `trabalho.docx`.

1. Word pede ao SO para abrir ficheiro;
2. SO lê blocos do disco (SSD/HDD);
3. dados vão para RAM;
4. Word interpreta formato do ficheiro;
5. conteúdo é mostrado no ecrã.

Repara: o ficheiro não "vive" só no disco enquanto editas.  
Partes relevantes são carregadas para memória.

---

## 11. Caso real: editar e guardar ficheiro

### Durante edição

- alterações ficam primeiro em memória (buffers/estruturas internas do programa);
- CPU processa ações de teclado/rato e atualiza estado interno;
- interface mostra resultado.

### Ao guardar

1. programa organiza conteúdo no formato do ficheiro;
2. pede ao SO escrita em disco;
3. SO grava blocos no SSD/HDD;
4. quando gravação termina com sucesso, tens persistência real.

Ponto importante:

- "está no ecrã" não significa "já está no disco";
- só guardar confirma persistência (com os mecanismos do SO/programa).

---

## 12. Caso real: fechar programa

Quando fechas:

1. programa termina tarefas em curso;
2. ficheiros/recursos são fechados;
3. SO remove processo;
4. memória desse processo é libertada;
5. CPU deixa de escalonar esse processo.

Se algo não foi guardado, pode perder-se (dependendo do programa e auto-save).

---

## 13. O que isto muda no teu raciocínio de programador

Perceber este fluxo ajuda-te a:

- escrever código mais eficiente;
- entender melhor latência ao abrir/gravar;
- evitar confusão entre RAM e disco;
- diagnosticar problemas de desempenho;
- perceber porque "abstrações" de linguagens de alto nível têm custo real.

---

## 14. Resumo final

- código-fonte precisa de ser transformado para execução;
- CPU executa instruções de máquina segundo ISA;
- SO e loader tratam de processo e memória;
- abrir/editar/guardar ficheiros envolve RAM + CPU + disco + SO;
- binário é formato geral; código de máquina é binário executável pela CPU.

---

**A seguir:** [`04_heap_stack_frames_e_execucao_python.md`](04_heap_stack_frames_e_execucao_python.md)

---

## 15. Changelog

- **2026-02-04**: versão inicial do módulo 06 (execução real, SO, CPU, ISA e ficheiros).
