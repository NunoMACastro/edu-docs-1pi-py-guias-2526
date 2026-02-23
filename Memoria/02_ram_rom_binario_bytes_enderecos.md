# Memória (10.º Ano) - 02 · RAM, ROM, Binário, Bytes e Endereços

> **Objetivo deste ficheiro**  
> Entender, com calma e sem saltos, os conceitos fundamentais de RAM e ROM, sistema binário, bytes, unidades de memória e noções básicas de endereçamento.

---

**Pré-requisitos:** [`01_memoria_do_computador_cache_primaria_secundaria.md`](01_memoria_do_computador_cache_primaria_secundaria.md)

## Índice

- [1. RAM vs ROM (diferença essencial)](#1-ram-vs-rom-diferença-essencial)
- [2. O que é um bit? O que é um byte?](#2-o-que-é-um-bit-o-que-é-um-byte)
- [3. Sistema binário (base 2)](#3-sistema-binário-base-2)
- [4. Converter decimal para binário](#4-converter-decimal-para-binário)
- [5. Converter binário para decimal](#5-converter-binário-para-decimal)
- [6. Texto em código binário (noção inicial)](#6-texto-em-código-binário-noção-inicial)
- [7. Endereço de memória (visão simples)](#7-endereço-de-memória-visão-simples)
- [8. Exercícios de consolidação (binário)](#8-exercícios-de-consolidação-binário)
- [9. Resumo final](#9-resumo-final)
- [10. Changelog](#10-changelog)

---

## 1. RAM vs ROM (diferença essencial)

### RAM (Random Access Memory)

- memória principal de trabalho;
- rápida;
- usada enquanto os programas estão a correr;
- normalmente volátil (perde conteúdo sem energia).

### ROM (Read-Only Memory)

- memória de leitura usada para guardar informação essencial do sistema;
- normalmente não volátil;
- contém firmware/instruções base de arranque.

---

## 2. O que é um bit? O que é um byte?

### Bit

É a menor unidade de informação digital.  
Só pode assumir dois valores:

- 0
- 1

### Byte

Um byte = 8 bits.

Exemplo:

- `01010100` é uma sequência de 8 bits (1 byte).

### Porque é importante?

Porque quase toda a informação num computador pode ser representada em bits:

- números,
- texto,
- imagens,
- áudio,
- instruções.

---

## 3. Sistema binário (base 2)

No sistema decimal (base 10), usamos os dígitos 0..9.  
No sistema binário (base 2), usamos apenas 0 e 1.

### Potências de 2 (muito importante)

| Posição | Potência de 2 | Valor |
| ------- | ------------- | ----- |
| 0       | 2^0           | 1     |
| 1       | 2^1           | 2     |
| 2       | 2^2           | 4     |
| 3       | 2^3           | 8     |
| 4       | 2^4           | 16    |
| 5       | 2^5           | 32    |
| 6       | 2^6           | 64    |
| 7       | 2^7           | 128   |

Cada posição binária representa uma potência de 2.

---

## 4. Converter decimal para binário

Método simples (divisões por 2):

1. Divide o número por 2;
2. Guarda o resto (0 ou 1);
3. Volta a dividir o quociente por 2;
4. Repete até o quociente ser 0;
5. Lê os restos de baixo para cima.

### Exemplo: 13 em binário

13 / 2 = 6 resto 1  
6 / 2 = 3 resto 0  
3 / 2 = 1 resto 1  
1 / 2 = 0 resto 1

Lendo restos de baixo para cima: **1101**

Logo: `13(10) = 1101(2)`

### Método alternativo: "marcar os bits ativos (1)"

Ideia:

1. Escolhe as potências de 2 (normalmente em 8 bits: 128, 64, 32, 16, 8, 4, 2, 1);
2. Começa no maior valor e pergunta: "cabe no número?";
3. Se couber, marca `1` e subtrai esse valor;
4. Se não couber, marca `0`;
5. Continua até chegar ao `1`;
6. O resultado final é a sequência de 0 e 1.

#### Exemplo A: decimal 35

Potências: 32, 16, 8, 4, 2, 1

- 35: cabe 32? sim -> bit = 1, sobra 3
- 3: cabe 16? não -> bit = 0
- 3: cabe 8? não -> bit = 0
- 3: cabe 4? não -> bit = 0
- 3: cabe 2? sim -> bit = 1, sobra 1
- 1: cabe 1? sim -> bit = 1, sobra 0

Resultado: `100011`

Confirmação: 32 + 2 + 1 = 35

Tabela visual (bits ativos):

| Potência de 2 | 32  | 16  | 8   | 4   | 2   | 1   |
| ------------- | --- | --- | --- | --- | --- | --- |
| Bit (0/1)     | 1   | 0   | 0   | 0   | 1   | 1   |
| Valor ativo   | 32  | 0   | 0   | 0   | 2   | 1   |

Soma dos ativos: `32 + 2 + 1 = 35`

#### Exemplo B: decimal 41

Potências: 32, 16, 8, 4, 2, 1

- 41: cabe 32? sim -> 1, sobra 9
- 9: cabe 16? não -> 0
- 9: cabe 8? sim -> 1, sobra 1
- 1: cabe 4? não -> 0
- 1: cabe 2? não -> 0
- 1: cabe 1? sim -> 1, sobra 0

Resultado: `101001`

Confirmação: 32 + 8 + 1 = 41

Tabela visual (bits ativos):

| Potência de 2 | 32  | 16  | 8   | 4   | 2   | 1   |
| ------------- | --- | --- | --- | --- | --- | --- |
| Bit (0/1)     | 1   | 0   | 1   | 0   | 0   | 1   |
| Valor ativo   | 32  | 0   | 8   | 0   | 0   | 1   |

Soma dos ativos: `32 + 8 + 1 = 41`

#### Exemplo C: decimal 27

Potências: 16, 8, 4, 2, 1

- 27: cabe 16? sim -> 1, sobra 11
- 11: cabe 8? sim -> 1, sobra 3
- 3: cabe 4? não -> 0
- 3: cabe 2? sim -> 1, sobra 1
- 1: cabe 1? sim -> 1, sobra 0

Resultado: `11011`

Confirmação: 16 + 8 + 2 + 1 = 27

Tabela visual (bits ativos):

| Potência de 2 | 32  | 16  | 8   | 4   | 2   | 1   |
| ------------- | --- | --- | --- | --- | --- | --- |
| Bit (0/1)     | 0   | 1   | 1   | 0   | 1   | 1   |
| Valor ativo   | 0   | 16  | 8   | 0   | 2   | 1   |

Soma dos ativos: `16 + 8 + 2 + 1 = 27`

> Nota didática: este método ajuda muito a "ver" o sistema binário.  
> O método das divisões é ótimo para procedimento; o dos bits ativos é ótimo para compreensão.

---

## 5. Converter binário para decimal

Método:

1. Escreve as potências de 2 por baixo dos bits;
2. Soma apenas as potências cujos bits são 1.

### Exemplo: `10110`

Posições (da direita para a esquerda):

- 0 -> 2^0 = 1
- 1 -> 2^1 = 2
- 2 -> 2^2 = 4
- 3 -> 2^3 = 8
- 4 -> 2^4 = 16

Bits de `10110`:

- 1·16 + 0·8 + 1·4 + 1·2 + 0·1
- 16 + 4 + 2
- **22**

Logo: `10110(2) = 22(10)`

---

## 6. Texto em código binário (noção inicial)

O computador guarda texto como números, e esses números em binário.

Um padrão comum de codificação é UTF-8 (no contexto moderno).

Exemplo simples (conceito):

- letra `A` -> valor 65 (em tabelas clássicas ASCII)
- 65 em binário = `01000001`

Não precisas decorar tabela completa agora.  
Precisas apenas de perceber a ideia:

**texto -> código numérico -> binário**

### 6.1 ASCII? UTF-8?

ASCII é um padrão antigo (7 bits, 128 caracteres).  
UTF-8 é um padrão moderno (usa 1 a 4 bytes por caractere, suporta muitos idiomas).

Ambos convertem caracteres em números, que depois são convertidos em binário. E vice-versa.

Ou seja, imagina que estás a usar o Microsoft Word que por sua vez usa UTF-8 para guardar o ficheiro:

- Quando escreves `A`, o Word consulta a tabela UTF-8 e vê que `A` = 65.
- Depois, converte 65 para binário: `01000001`.
- Finalmente, guarda `01000001` no ficheiro.

Se leres o ficheiro depois, o processo é invertido.

Ou seja, se num ficheiro word tiveres a frase "Olá, vocês são lindos!", o Word vai guardar tudo isso em binário, usando UTF-8 para converter cada caractere em números e depois em bits. E vai ter um ficheiro com a sequência:

`01001111 01101100 11000011 10100001 00101100 00100000 01110110 01101111 11000011 10100101 01110011 00100000 01110011 11000011 10100111 01101111 01101110 00100000 01101100 01101001 01101110 01100100 01101111 01110011 00100001`

Assim o processador e o software sabem exatamente como interpretar cada parte do ficheiro. Para o software é uma questão de consultar a tabela de codificação correta. Para o processador, é tudo números em binário.

---

## 7. Endereço de memória

Quando um dado está na memória, ele está numa posição específica.

Essa posição tem um "nome técnico": **endereço de memória**.

Analogia:

- Memória = rua com casas;
- Endereço = número da casa;
- Dado = pessoa que vive nessa casa.

Sem endereço, o processador não sabe onde buscar o dado.

### 7.1 Binário (dados) vs binário (instruções)

Neste ponto convém fixar uma distinção muito importante:

- o computador guarda **dados** em binário (texto, números, imagem, etc.);
- a CPU executa **instruções** também em binário (código de máquina).

Ou seja:

- todo código de máquina é binário;
- nem todo binário é código de máquina.

Exemplo didático:

- uma sequência pode representar a letra `A` (dado);
- outra sequência pode representar "somar valores" (instrução da CPU).

Para aprofundar a ponte "binário -> código de máquina -> execução", consulta [`06_do_codigo_a_execucao_real_so_cpu_isa.md`](06_do_codigo_a_execucao_real_so_cpu_isa.md).

---

## 8. Exercícios de consolidação (binário)

> Faz primeiro sem olhar para as resoluções.

### Exercício 1 - Decimal para binário

Converte para binário:

1. `10`
2. `25`
3. `100`
4. `41`

> Resolução

1. `10` -> `1010`
2. `25` -> `11001`
3. `100` -> `1100100`
4. `41` -> `101001`

---

### Exercício 2 - Binário para decimal

Converte para decimal:

1. `1001101`
2. `101011`
3. `1111111111`
4. `1000000`

> Resolução

1. `1001101` -> 64 + 8 + 4 + 1 = `77`
2. `101011` -> 32 + 8 + 2 + 1 = `43`
3. `1111111111` -> 1023
4. `1000000` -> `64`

---

### Exercício 3 - Verdadeiro ou falso

Indica V/F:

1. 1 byte = 16 bits.
2. RAM é normalmente volátil.
3. ROM é usada para guardar firmware.
4. Em binário, usamos os dígitos 0 e 1.

> Resolução

1. Falso
2. Verdadeiro
3. Verdadeiro
4. Verdadeiro

---

### Exercício 4 - Potências de 2

Completa:

1. 2^0 = ?
2. 2^3 = ?
3. 2^5 = ?
4. 2^7 = ?

> Resolução

1. 1
2. 8
3. 32
4. 128

---

### Exercício 5 - Desafio guiado

1. Converte 84 para binário.
2. Converte `01010100` para decimal.
3. Compara os resultados.

> Resolução

1. `84` -> `01010100`
2. `01010100` -> `84`
3. São equivalentes; uma representação é decimal e a outra binária.

---

## 9. Resumo final

- RAM e ROM têm funções diferentes.
- Bit é unidade mínima (0/1); byte tem 8 bits.
- Binário usa base 2 e potências de 2.
- Conversão decimal/binário é essencial para compreender memória.
- Endereço de memória é a localização exata de um dado na RAM.

---

**A seguir:** [`06_do_codigo_a_execucao_real_so_cpu_isa.md`](06_do_codigo_a_execucao_real_so_cpu_isa.md)

---

## 10. Changelog

- **2026-02-04**: versão inicial do módulo 02 com exercícios e resoluções.
