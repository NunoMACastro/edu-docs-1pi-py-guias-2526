# Memória (10.º Ano) - 00 · Fundamentos: Hardware, Bits, CPU e Endereços de Memória

> **Objetivo deste ficheiro**  
> Criar a base que faltava para os próximos módulos: perceber de onde vêm os 0 e 1, para que servem os transístores, como a RAM e a CPU trabalham e como os endereços de memória entram em tudo isto.

---

**Pré-requisitos:** nenhum (início da rota recomendada).

## Índice

- [1. Porque este módulo vem antes dos outros](#1-porque-este-módulo-vem-antes-dos-outros)
- [2. Do mundo físico ao digital](#2-do-mundo-físico-ao-digital)
- [3. Transístor: o "interruptor inteligente"](#3-transístor-o-interruptor-inteligente)
- [4. Portas lógicas: o primeiro nível de "pensamento"](#4-portas-lógicas-o-primeiro-nível-de-pensamento)
- [5. Bits, bytes e palavras (word)](#5-bits-bytes-e-palavras-word)
- [6. Como representamos números, texto e imagens](#6-como-representamos-números-texto-e-imagens)
- [7. RAM por dentro: células, leitura, escrita e refresh](#7-ram-por-dentro-células-leitura-escrita-e-refresh)
- [8. CPU por dentro: blocos principais](#8-cpu-por-dentro-blocos-principais)
- [9. Ciclo da CPU: buscar, descodificar e executar](#9-ciclo-da-cpu-buscar-descodificar-e-executar)
- [10. Endereços de memória: o "GPS" dos dados](#10-endereços-de-memória-o-gps-dos-dados)
- [11. Barramentos: como CPU e memória comunicam](#11-barramentos-como-cpu-e-memória-comunicam)
- [12. Ponte para Python (porque isto importa já)](#12-ponte-para-python-porque-isto-importa-já)
- [13. Resumo final](#13-resumo-final)
- [14. Changelog](#14-changelog)

---

## 1. Porque este módulo vem antes dos outros

Sem esta base, vários conceitos parecem surgir "do nada":

- referência;
- endereço de memória;
- stack/heap;
- garbage collection.

Com esta base, tudo encaixa:

- percebes onde os dados vivem;
- como são lidos/escritos;
- e porque certas decisões em programação fazem diferença.

---

## 2. Do mundo físico ao digital

Dentro do computador, no nível físico, existe eletricidade.

Em eletrónica digital, simplificamos sinais em dois estados:

- estado "baixo";
- estado "alto".

Esses dois estados são representados como:

- `0`
- `1`

### Porque usar apenas dois estados?

Porque é mais robusto e fiável.

Se tentasses usar muitos níveis (0,1,2,3,4...), pequenas variações elétricas causavam mais erros.  
Com dois níveis bem separados, é muito mais fácil distinguir corretamente.

---

## 3. Transístor: o "interruptor inteligente"

Agora a tua pergunta-chave:  
**"Ok, transístor é um interruptor. E depois?"**

Excelente pergunta.

O transístor é um componente eletrónico que pode:

- deixar passar corrente;
- ou bloquear corrente;
- com base num sinal de controlo.

### Utilidade real

Quando juntas muitos transístores:

- consegues construir portas lógicas (AND, OR, NOT...);
- com portas lógicas, constróis circuitos que calculam;
- com milhões/milhares de milhões desses circuitos, constróis CPU e memórias.

Ou seja: o transístor é o "tijolo" da computação moderna.

### Onde está?

Está nos chips:

- processador (CPU);
- memórias cache;
- controladores;
- muitos outros componentes.

---

## 4. Portas lógicas: o primeiro nível de "pensamento"

Uma porta lógica recebe bits e devolve um bit, seguindo uma regra.

Exemplos básicos:

- `NOT` (nega): inverte 0/1;
- `AND` (e): só dá 1 se ambos forem 1;
- `OR` (ou): dá 1 se pelo menos um for 1.

### Mini tabelas verdade

`AND`

| A   | B   | A AND B |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 0       |
| 1   | 0   | 0       |
| 1   | 1   | 1       |

`OR`

| A   | B   | A OR B |
| --- | --- | ------ |
| 0   | 0   | 0      |
| 0   | 1   | 1      |
| 1   | 0   | 1      |
| 1   | 1   | 1      |

`NOT`

| A   | NOT A |
| --- | ----- |
| 0   | 1     |
| 1   | 0     |

### Porque isto importa?

Com estas portas, criamos:

- somadores binários;
- comparadores;
- seletores;
- circuitos de controlo.

É aqui que nasce a "lógica" do processador.

---

## 5. Bits, bytes e palavras (word)

### Bit

Menor unidade de informação: `0` ou `1`.

### Byte

1 byte = 8 bits.

### Word (palavra de máquina)

É o tamanho de dados que a CPU manipula naturalmente (por exemplo, 32 ou 64 bits).

Isto influencia:

- desempenho;
- intervalos numéricos;
- capacidade de endereçamento.

---

## 6. Como representamos números, texto e imagens

Tudo no computador acaba em bits.

### Números

Representados em binário (base 2).

### Texto

Representado por códigos numéricos (ex.: ASCII/UTF-8), que depois viram binário.

### Imagens

Representadas por pixels; cada pixel tem valores numéricos (cores), também guardados em bits.

Ideia-chave:

> O computador não "vê" letra, foto ou música como nós.  
> Vê padrões de bits.

---

## 7. RAM por dentro: células, leitura, escrita e refresh

Numa visão simplificada de DRAM, cada célula tem:

- 1 transístor;
- 1 condensador.

### Como guarda um bit?

- condensador carregado -> interpretamos como `1`;
- condensador descarregado -> interpretamos como `0`.

### Escrever na RAM (visão simples)

1. Controlador escolhe endereço;
2. abre caminho elétrico (via transístor);
3. grava carga (ou remove carga) no condensador.

### Ler da RAM (visão simples)

1. Controlador escolhe endereço;
2. mede estado elétrico da célula;
3. interpreta como 0/1.

### Refresh: porque existe?

O condensador perde carga com o tempo.  
Então a RAM precisa de refresh periódico para "reconfirmar" valores.

Isto ajuda a explicar:

- porque a RAM é volátil;
- porque requer energia contínua para manter dados.

### Nota útil

A cache da CPU normalmente usa SRAM (outro tipo), mais rápida e cara, sem o mesmo refresh contínuo típico da DRAM.

---

## 8. CPU por dentro: blocos principais

A CPU não é um bloco único "mágico".  
Tem partes com funções diferentes.

### ALU (Arithmetic Logic Unit)

Faz operações aritméticas e lógicas:

- soma;
- subtração;
- comparações;
- operações bit a bit.

### Unidade de controlo

Coordena a execução:

- interpreta instruções;
- decide que bloco ativa em cada momento.

### Registos

Pequenas memórias ultra rápidas dentro da CPU, usadas para valores imediatos.

### Cache

Memória muito rápida perto da CPU, para reduzir esperas da RAM.

---

## 9. Ciclo da CPU: buscar, descodificar e executar

Este ciclo repete-se constantemente:

1. **Fetch (buscar)**: vai buscar próxima instrução à memória;
2. **Decode (descodificar)**: interpreta o que fazer;
3. **Execute (executar)**: realiza a operação;
4. atualiza estado e passa à seguinte.

### Exemplo simples (ideia)

Instrução: "somar A + B"

- fetch: buscar instrução e dados;
- decode: perceber que é operação de soma;
- execute: ALU soma valores;
- resultado vai para registo/memória.

Este ciclo acontece milhões ou milhares de milhões de vezes por segundo.

---

## 10. Endereços de memória: o "GPS" dos dados

RAM tem milhões/milhares de milhões de posições.  
Cada posição tem um endereço único.

Sem endereço, a CPU não sabe:

- onde ler;
- onde escrever.

### Analogia prática

Imagina uma estante gigante de cacifos:

- cada cacifo tem número;
- para buscar algo, precisas do número exato.

Memória funciona da mesma forma.

### Em programação

Quando falamos em referências (como em Python), estamos a falar num nível mais abstrato dessa ideia de "apontar para um objeto/local".

---

## 11. Barramentos: como CPU e memória comunicam

Barramento = conjunto de linhas de comunicação.

Três tipos principais:

- **dados**: transporta o conteúdo;
- **endereços**: diz onde operar;
- **controlo**: diz que operação fazer (ler/escrever, sincronização, etc.).

### Leitura de memória (sequência simples)

1. CPU coloca endereço no barramento de endereços;
2. CPU sinaliza "ler" no controlo;
3. memória coloca valor no barramento de dados;
4. CPU recebe valor.

### Escrita de memória (sequência simples)

1. CPU coloca endereço no barramento de endereços;
2. CPU coloca valor no barramento de dados;
3. CPU sinaliza "escrever" no controlo;
4. memória grava valor nesse endereço.

---

## 12. Ponte para Python (porque isto importa já)

Nos próximos módulos vais ver:

- variáveis;
- referências;
- objetos;
- heap/stack.

Com a base deste ficheiro, já tens contexto:

- o computador manipula bits;
- os bits estão em endereços de memória;
- a CPU acede por ciclos e barramentos;
- linguagens de alto nível escondem detalhes, mas não os eliminam.

---

## 13. Resumo final

- eletricidade -> estados -> bits (0/1);
- transístores constroem portas lógicas;
- portas lógicas constroem CPU e memória;
- RAM guarda bits em células com endereço;
- CPU executa instruções no ciclo fetch-decode-execute;
- CPU e memória comunicam por barramentos.

Esta é a fundação para entender memória e execução de programas nos próximos ficheiros.

---

**A seguir:** [`01_memoria_do_computador_cache_primaria_secundaria.md`](01_memoria_do_computador_cache_primaria_secundaria.md)

---

## 14. Changelog

- **2026-02-04**: versão inicial do módulo 00.
- **2026-02-04**: reforço pedagógico com explicações de utilidade, portas lógicas, fluxo de leitura/escrita e ponte para Python.
