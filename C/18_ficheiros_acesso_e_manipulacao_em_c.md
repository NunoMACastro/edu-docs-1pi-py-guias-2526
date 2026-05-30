![Header](../Images/Header.png)

# C (10.º Ano) - 18 · Ficheiros: Acesso e Manipulação em C

> **Objetivo deste ficheiro**  
> Aprender a ler, escrever e manipular ficheiros em C com foco em segurança, validação e organização de dados.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. Porque trabalhar com ficheiros?](#1-porque-trabalhar-com-ficheiros)
- [2. Conceitos base (`FILE *`)](#2-conceitos-base-file-)
- [3. Modos de abertura](#3-modos-de-abertura)
- [4. Escrita em ficheiros de texto](#4-escrita-em-ficheiros-de-texto)
- [5. Leitura em ficheiros de texto](#5-leitura-em-ficheiros-de-texto)
- [6. Ficheiros binários (introdução)](#6-ficheiros-binários-introdução)
- [7. Posição no ficheiro (`fseek`, `ftell`, `rewind`)](#7-posição-no-ficheiro-fseek-ftell-rewind)
- [8. Tratamento de erros em I/O](#8-tratamento-de-erros-em-io)
- [9. Exemplo guiado](#9-exemplo-guiado)
- [10. Erros comuns](#10-erros-comuns)
- [11. Changelog](#11-changelog)

---

## 0. Como usar este módulo

1. Treina primeiro ficheiros de texto.
2. Valida sempre abertura e fecho.
3. Só depois avança para binário.

---

## 1. Porque trabalhar com ficheiros?

Sem ficheiros, dados desaparecem ao terminar programa.

Com ficheiros, consegues:

- guardar informação;
- reutilizar dados;
- trocar dados entre execuções.

---

## 2. Conceitos base (`FILE *`)

`FILE *` representa ligação ao ficheiro.

Fluxo típico:

1. `fopen`
2. ler/escrever
3. `fclose`

---

## 3. Modos de abertura

- `"r"` leitura (texto)
- `"w"` escrita (texto, cria/limpa)
- `"a"` acrescentar (texto)
- `"rb"`, `"wb"`, `"ab"` para binário
- versões com `+` para leitura/escrita

Escolher modo errado causa erros de comportamento.

---

## 4. Escrita em ficheiros de texto

Funções comuns:

- `fprintf`
- `fputs`
- `fputc`

Exemplo:

```c
FILE *f = fopen("dados.txt", "w");
if (!f) return 1;
fprintf(f, "Ana;16\n");
fclose(f);
```

---

## 5. Leitura em ficheiros de texto

Funções comuns:

- `fscanf`
- `fgets`
- `fgetc`

`fgets` costuma ser mais segura para linhas completas.

---

## 6. Ficheiros binários (introdução)

Funções:

- `fread`
- `fwrite`

Usados para gravar dados em formato não textual.

Vantagens:

- eficiência;
- preservação de estrutura de bytes.

---

## 7. Posição no ficheiro (`fseek`, `ftell`, `rewind`)

Permite navegar no ficheiro.

- `fseek`: mover cursor;
- `ftell`: posição atual;
- `rewind`: voltar ao início.

---

## 8. Tratamento de erros em I/O

Sempre verificar:

- `fopen` retornou `NULL`?
- `fclose` terminou corretamente?
- leitura/escrita devolveu quantidade esperada?

Mensagens claras ajudam muito na depuração.

---

## 9. Exemplo guiado

```c
#include <stdio.h>

int main(void) {
    FILE *f = fopen("notas.txt", "w");
    if (f == NULL) {
        printf("Erro a criar ficheiro\n");
        return 1;
    }

    fprintf(f, "Ana;15\n");
    fprintf(f, "Rui;12\n");
    fclose(f);

    f = fopen("notas.txt", "r");
    if (f == NULL) {
        printf("Erro a abrir ficheiro\n");
        return 1;
    }

    char linha[100];
    while (fgets(linha, sizeof linha, f)) {
        printf("%s", linha);
    }

    fclose(f);
    return 0;
}
```

---

## 10. Erros comuns

1. Esquecer `fclose`.
2. Abrir com modo errado (`w` quando queria `a`).
3. Assumir que leitura sempre funciona.
4. Não validar tamanho de buffer.
5. Misturar texto e binário sem planeamento.

---

## 11. Changelog

- **2026-02-23**: reescrita detalhada do módulo com exercícios sem resolução.

![Footer](../Images/Footer.png)
