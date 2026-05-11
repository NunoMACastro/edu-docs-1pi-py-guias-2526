# C (10.º Ano) - 12 · Estruturas de Dados Estáticas: Strings, Arrays e Matrizes

> **Objetivo deste ficheiro**  
> Aprender a guardar vários valores relacionados numa só estrutura, usando arrays, strings e matrizes em C, com atenção aos limites de memória e aos erros mais comuns.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. Porque precisamos de estruturas de dados?](#1-porque-precisamos-de-estruturas-de-dados)
- [2. O que significa "estrutura estática"?](#2-o-que-significa-estrutura-estática)
- [3. Arrays unidimensionais](#3-arrays-unidimensionais)
- [4. Índices: a parte onde quase todos erram no início](#4-índices-a-parte-onde-quase-todos-erram-no-início)
- [5. Percorrer arrays com ciclos](#5-percorrer-arrays-com-ciclos)
- [6. Ler e processar vários valores](#6-ler-e-processar-vários-valores)
- [7. Arrays e funções](#7-arrays-e-funções)
- [8. Strings em C: texto como array de caracteres](#8-strings-em-c-texto-como-array-de-caracteres)
- [9. Leitura segura de strings](#9-leitura-segura-de-strings)
- [10. Funções úteis da biblioteca `string.h`](#10-funções-úteis-da-biblioteca-stringh)
- [11. Matrizes: arrays com linhas e colunas](#11-matrizes-arrays-com-linhas-e-colunas)
- [12. Percorrer matrizes com dois ciclos](#12-percorrer-matrizes-com-dois-ciclos)
- [13. Exemplo guiado 1: notas de uma turma](#13-exemplo-guiado-1-notas-de-uma-turma)
- [14. Exemplo guiado 2: nomes de alunos](#14-exemplo-guiado-2-nomes-de-alunos)
- [15. Exemplo guiado 3: tabela de temperaturas](#15-exemplo-guiado-3-tabela-de-temperaturas)
- [16. Checklist mental antes de entregar um programa](#16-checklist-mental-antes-de-entregar-um-programa)
- [17. Erros comuns](#17-erros-comuns)
- [18. Exercícios propostos](#18-exercícios-propostos)
- [19. Changelog](#19-changelog)

---

## 0. Como usar este módulo

Este módulo deve ser estudado com calma. Arrays, strings e matrizes parecem simples quando se vê o código pronto, mas exigem um raciocínio muito importante: perceber onde cada valor fica guardado.

Sugestão de estudo:

1. Primeiro compreende arrays simples, como uma lista de notas.
2. Depois passa para strings, que são arrays de `char`.
3. Só depois avança para matrizes, porque exigem pensar em duas coordenadas: linha e coluna.
4. Em todos os exemplos, desenha no papel as posições de memória.
5. Sempre que vires um índice, pergunta: "este índice está dentro dos limites?"

---

## 1. Porque precisamos de estruturas de dados?

Até agora, muitas vezes guardámos valores em variáveis individuais:

```c
int nota1 = 14;
int nota2 = 16;
int nota3 = 11;
```

Isto funciona para poucos valores. Mas imagina uma turma com 30 alunos. Teríamos de criar:

```c
int nota1;
int nota2;
int nota3;
/* ... */
int nota30;
```

Além de ser repetitivo, também se torna difícil processar os dados. Como calcular a média? Como descobrir a maior nota? Como mostrar todas as notas?

Para isso usamos estruturas de dados. Uma estrutura de dados permite guardar vários valores relacionados de forma organizada.

Neste módulo vamos estudar três formas importantes:

- arrays: listas de valores do mesmo tipo;
- strings: texto guardado como array de caracteres;
- matrizes: tabelas com linhas e colunas.

---

## 2. O que significa "estrutura estática"?

Uma estrutura estática tem tamanho definido no momento em que é declarada.

Exemplo:

```c
int notas[30];
```

Aqui estamos a dizer ao C:

- quero um array chamado `notas`;
- cada posição guarda um `int`;
- existem exatamente 30 posições;
- o tamanho não muda durante a execução do programa.

Isto é diferente de estruturas dinâmicas, que serão estudadas no módulo seguinte, onde a memória pode ser pedida durante a execução com funções como `malloc`.

Vantagens das estruturas estáticas:

- são mais simples para começar;
- têm acesso rápido por índice;
- o compilador sabe logo quanto espaço reservar;
- são boas para problemas com limites conhecidos.

Limitações:

- o tamanho é fixo;
- se reservarmos pouco espaço, faltam posições;
- se reservarmos espaço a mais, podemos desperdiçar memória;
- não devemos aceder fora dos limites declarados.

Exemplo de decisão:

```c
#define MAX_ALUNOS 30

int notas[MAX_ALUNOS];
```

Usar uma constante como `MAX_ALUNOS` torna o programa mais fácil de ler e alterar.

---

## 3. Arrays unidimensionais

Um array unidimensional é uma sequência de elementos do mesmo tipo.

Podemos imaginá-lo como uma fila de caixas:

| Índice | 0  | 1  | 2  | 3  | 4  |
| ------ | -- | -- | -- | -- | -- |
| Valor  | 10 | 20 | 30 | 40 | 50 |

Declaração em C:

```c
int valores[5] = {10, 20, 30, 40, 50};
```

Esta declaração cria 5 posições:

- `valores[0]` guarda `10`;
- `valores[1]` guarda `20`;
- `valores[2]` guarda `30`;
- `valores[3]` guarda `40`;
- `valores[4]` guarda `50`.

Repara num detalhe essencial: em C, os índices começam em `0`, não em `1`.

### 3.1 Declarar sem inicializar

```c
int notas[5];
```

Neste caso, o array existe, mas os valores não estão preparados para serem usados. Podem conter lixo de memória.

Por isso, antes de ler uma posição, devemos atribuir-lhe um valor:

```c
notas[0] = 12;
notas[1] = 15;
```

### 3.2 Declarar e inicializar logo

```c
int notas[5] = {12, 15, 9, 18, 14};
```

Também podemos deixar o compilador contar:

```c
int notas[] = {12, 15, 9, 18, 14};
```

Neste caso, o compilador percebe que o array tem 5 posições.

### 3.3 Inicialização parcial

```c
int valores[5] = {10, 20};
```

As primeiras duas posições recebem `10` e `20`. As restantes ficam a `0`.

Resultado:

| Índice | 0  | 1  | 2 | 3 | 4 |
| ------ | -- | -- | - | - | - |
| Valor  | 10 | 20 | 0 | 0 | 0 |

---

## 4. Índices: a parte onde quase todos erram no início

Se um array tem `n` posições, os índices válidos vão de `0` até `n - 1`.

Exemplo:

```c
int v[5];
```

Índices válidos:

- `v[0]`;
- `v[1]`;
- `v[2]`;
- `v[3]`;
- `v[4]`.

Índice inválido:

```c
v[5] = 100; // erro lógico: fora do array
```

Este erro é perigoso porque C normalmente não impede automaticamente este acesso. O programa pode:

- parecer funcionar;
- alterar outra zona de memória;
- dar resultado errado;
- bloquear;
- criar uma falha difícil de encontrar.

Regra simples:

```c
for (int i = 0; i < tamanho; i++) {
    /* i vai de 0 até tamanho - 1 */
}
```

Evita escrever:

```c
for (int i = 0; i <= tamanho; i++) {
    /* errado para arrays: chega a tamanho */
}
```

---

## 5. Percorrer arrays com ciclos

Arrays combinam muito bem com ciclos, porque conseguimos usar uma variável como índice.

Exemplo:

```c
int notas[5] = {12, 15, 9, 18, 14};

for (int i = 0; i < 5; i++) {
    printf("%d\n", notas[i]);
}
```

Como ler este código:

1. `i` começa em `0`;
2. enquanto `i < 5`, o ciclo continua;
3. em cada repetição, usamos `notas[i]`;
4. no fim de cada repetição, `i++` passa para a próxima posição.

Sequência de acesso:

- `i = 0` -> `notas[0]`;
- `i = 1` -> `notas[1]`;
- `i = 2` -> `notas[2]`;
- `i = 3` -> `notas[3]`;
- `i = 4` -> `notas[4]`;
- `i = 5` -> o ciclo termina, porque `5 < 5` é falso.

---

## 6. Ler e processar vários valores

Um caso típico é ler várias notas e calcular a média.

Antes de escrever o programa completo, pensa nos passos:

1. criar um array para guardar as notas;
2. ler cada nota para uma posição;
3. somar todas as notas;
4. dividir pelo número de notas.

Exemplo:

```c
#include <stdio.h>

#define TOTAL_NOTAS 5

int main(void) {
    int notas[TOTAL_NOTAS];
    int soma = 0;

    for (int i = 0; i < TOTAL_NOTAS; i++) {
        printf("Nota %d: ", i + 1);
        scanf("%d", &notas[i]);
        soma += notas[i];
    }

    double media = (double)soma / TOTAL_NOTAS;

    printf("Media: %.2f\n", media);

    return 0;
}
```

Notas importantes:

- usamos `i + 1` apenas para mostrar ao utilizador "Nota 1", "Nota 2", etc.;
- internamente, o array continua a usar índices `0`, `1`, `2`, ...
- usamos `(double)soma` para evitar divisão inteira;
- `TOTAL_NOTAS` evita repetir o número `5` em vários locais.

---

## 7. Arrays e funções

Quando passamos um array para uma função, a função recebe acesso ao array original. Na prática, não é feita uma cópia completa do array.

Por isso, normalmente também passamos o tamanho do array.

Exemplo:

```c
int soma_array(int valores[], int tamanho) {
    int soma = 0;

    for (int i = 0; i < tamanho; i++) {
        soma += valores[i];
    }

    return soma;
}
```

Chamada:

```c
int numeros[4] = {3, 5, 7, 9};
int total = soma_array(numeros, 4);
```

Porque passamos o tamanho?

Porque dentro da função o C não sabe automaticamente quantas posições o array tem. Se a função não souber o limite, pode tentar ler fora do array.

Boa prática:

```c
void mostrar_array(int valores[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", valores[i]);
    }
    printf("\n");
}
```

---

## 8. Strings em C: texto como array de caracteres

Em C, uma string não é um tipo especial como em algumas linguagens. Uma string é um array de `char` terminado por um carácter especial: `'\0'`.

Exemplo:

```c
char nome[4] = "Ana";
```

Na memória fica assim:

| Índice | 0   | 1   | 2   | 3    |
| ------ | --- | --- | --- | ---- |
| Valor  | 'A' | 'n' | 'a' | '\0' |

O `'\0'` chama-se terminador nulo. Ele indica onde o texto acaba.

Isto significa que:

```c
char nome[3] = "Ana"; // errado: falta espaço para '\0'
```

Para guardar `"Ana"` precisamos de 4 posições:

- `A`;
- `n`;
- `a`;
- `\0`.

### 8.1 Declarar strings

Com tamanho explícito:

```c
char nome[20] = "Rita";
```

Com tamanho calculado pelo compilador:

```c
char nome[] = "Rita";
```

Neste caso, o compilador reserva 5 posições: `R`, `i`, `t`, `a`, `\0`.

### 8.2 Um carácter não é uma string

```c
char letra = 'A';       // um carácter
char texto[] = "A";     // string com 'A' e '\0'
```

Aspas simples (`'A'`) representam um carácter.

Aspas duplas (`"A"`) representam uma string.

---

## 9. Leitura segura de strings

Para ler uma palavra simples, poderíamos usar:

```c
scanf("%19s", nome);
```

Mas `scanf("%s", ...)` para no primeiro espaço. Se o utilizador escrever `Ana Silva`, só lê `Ana`.

Para ler uma linha com espaços, usamos `fgets`.

```c
char nome[50];

printf("Nome: ");
fgets(nome, sizeof nome, stdin);
```

`sizeof nome` indica a capacidade total do array. Assim, `fgets` sabe quantos caracteres pode ler.

### 9.1 Remover o `\n` final

Quando usamos `fgets`, normalmente o `\n` produzido pelo Enter também fica guardado na string, se houver espaço.

Podemos removê-lo com `strcspn`:

```c
#include <string.h>

nome[strcspn(nome, "\n")] = '\0';
```

Como pensar nesta linha:

- `strcspn(nome, "\n")` procura a posição onde aparece `\n`;
- se encontrar, devolve esse índice;
- substituímos esse carácter por `'\0'`;
- assim, a string passa a terminar ali.

---

## 10. Funções úteis da biblioteca `string.h`

Para usar funções de strings:

```c
#include <string.h>
```

Funções frequentes:

| Função | Para que serve | Exemplo de ideia |
| ------ | -------------- | ---------------- |
| `strlen` | calcular comprimento da string | quantos caracteres tem o nome |
| `strcmp` | comparar strings | ver se duas palavras são iguais |
| `strcpy` | copiar string | copiar um nome para outro array |
| `strcat` | juntar strings | acrescentar apelido ao nome |
| `strcspn` | procurar primeira ocorrência de certos caracteres | remover `\n` do `fgets` |

### 10.1 `strlen`

```c
char palavra[] = "Ola";
printf("%zu\n", strlen(palavra)); // 3
```

`strlen` não conta o `'\0'`. Conta apenas os caracteres visíveis.

### 10.2 `strcmp`

```c
if (strcmp(opcao, "sair") == 0) {
    printf("A terminar...\n");
}
```

Não compares strings assim:

```c
if (opcao == "sair") { /* errado para comparar conteúdo */ }
```

Em C, `==` não compara o texto guardado em arrays de caracteres.

### 10.3 Cuidado com `strcpy` e `strcat`

Estas funções podem causar problemas se o destino não tiver espaço suficiente.

Exemplo perigoso:

```c
char destino[5];
strcpy(destino, "Programacao"); // não cabe
```

Para o 10.º ano, a regra prática é:

- define arrays com tamanho suficiente;
- evita copiar texto sem saber se cabe;
- prefere exemplos simples e controlados;
- lembra-te sempre do `'\0'`.

---

## 11. Matrizes: arrays com linhas e colunas

Uma matriz é um array bidimensional. Podemos imaginá-la como uma tabela.

Exemplo de matriz com 2 linhas e 3 colunas:

|     | Coluna 0 | Coluna 1 | Coluna 2 |
| --- | -------- | -------- | -------- |
| Linha 0 | 1 | 2 | 3 |
| Linha 1 | 4 | 5 | 6 |

Declaração:

```c
int matriz[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
```

Acesso:

```c
matriz[linha][coluna]
```

Exemplos:

- `matriz[0][0]` -> `1`;
- `matriz[0][2]` -> `3`;
- `matriz[1][0]` -> `4`;
- `matriz[1][2]` -> `6`.

Tal como nos arrays, os índices começam em `0`.

---

## 12. Percorrer matrizes com dois ciclos

Para percorrer uma matriz, usamos normalmente dois ciclos:

- um para as linhas;
- outro para as colunas.

```c
for (int linha = 0; linha < 2; linha++) {
    for (int coluna = 0; coluna < 3; coluna++) {
        printf("%d ", matriz[linha][coluna]);
    }
    printf("\n");
}
```

Como ler este código:

1. escolhemos uma linha;
2. percorremos todas as colunas dessa linha;
3. quando a linha acaba, mudamos de linha;
4. repetimos até não haver mais linhas.

Resultado:

```text
1 2 3
4 5 6
```

---

## 13. Exemplo guiado 1: notas de uma turma

Objetivo: ler 5 notas, calcular média, maior nota e menor nota.

Antes do código, pensa:

- precisamos de guardar várias notas;
- todas são inteiros;
- o número de notas é conhecido;
- um array é adequado.

```c
#include <stdio.h>

#define TOTAL_NOTAS 5

int main(void) {
    int notas[TOTAL_NOTAS];
    int soma = 0;

    for (int i = 0; i < TOTAL_NOTAS; i++) {
        printf("Nota %d: ", i + 1);
        scanf("%d", &notas[i]);
        soma += notas[i];
    }

    int maior = notas[0];
    int menor = notas[0];

    for (int i = 1; i < TOTAL_NOTAS; i++) {
        if (notas[i] > maior) {
            maior = notas[i];
        }

        if (notas[i] < menor) {
            menor = notas[i];
        }
    }

    double media = (double)soma / TOTAL_NOTAS;

    printf("Media: %.2f\n", media);
    printf("Maior nota: %d\n", maior);
    printf("Menor nota: %d\n", menor);

    return 0;
}
```

Pontos importantes:

- `maior` e `menor` começam com `notas[0]`, não com `0`;
- o segundo ciclo começa em `1`, porque a posição `0` já foi usada como referência inicial;
- se todas as notas fossem negativas, começar `maior` em `0` daria erro lógico;
- a conversão para `double` evita perder casas decimais na média.

---

## 14. Exemplo guiado 2: nomes de alunos

Objetivo: ler nomes completos de 3 alunos e mostrá-los no fim.

Aqui precisamos de guardar texto. Como queremos vários nomes, usamos uma matriz de caracteres:

```c
char nomes[3][50];
```

Isto significa:

- existem 3 strings;
- cada string pode ocupar até 49 caracteres visíveis;
- a posição extra é para o `'\0'`.

Código:

```c
#include <stdio.h>
#include <string.h>

#define TOTAL_ALUNOS 3
#define TAM_NOME 50

int main(void) {
    char nomes[TOTAL_ALUNOS][TAM_NOME];

    for (int i = 0; i < TOTAL_ALUNOS; i++) {
        printf("Nome do aluno %d: ", i + 1);
        fgets(nomes[i], sizeof nomes[i], stdin);
        nomes[i][strcspn(nomes[i], "\n")] = '\0';
    }

    printf("\nLista de alunos:\n");

    for (int i = 0; i < TOTAL_ALUNOS; i++) {
        printf("%d - %s\n", i + 1, nomes[i]);
    }

    return 0;
}
```

Como interpretar `nomes[i]`:

- `nomes[0]` é a primeira string;
- `nomes[1]` é a segunda string;
- `nomes[2]` é a terceira string.

Cada uma dessas strings é, por sua vez, um array de `char`.

---

## 15. Exemplo guiado 3: tabela de temperaturas

Objetivo: guardar temperaturas de 2 cidades durante 3 dias.

Isto é uma situação natural para uma matriz:

- linhas: cidades;
- colunas: dias.

```c
#include <stdio.h>

#define CIDADES 2
#define DIAS 3

int main(void) {
    double temperaturas[CIDADES][DIAS];

    for (int cidade = 0; cidade < CIDADES; cidade++) {
        for (int dia = 0; dia < DIAS; dia++) {
            printf("Cidade %d, dia %d: ", cidade + 1, dia + 1);
            scanf("%lf", &temperaturas[cidade][dia]);
        }
    }

    printf("\nTabela de temperaturas:\n");

    for (int cidade = 0; cidade < CIDADES; cidade++) {
        printf("Cidade %d: ", cidade + 1);

        for (int dia = 0; dia < DIAS; dia++) {
            printf("%.1f ", temperaturas[cidade][dia]);
        }

        printf("\n");
    }

    return 0;
}
```

Detalhes a notar:

- `scanf("%lf", ...)` é usado para ler `double`;
- o primeiro índice escolhe a cidade;
- o segundo índice escolhe o dia;
- `cidade + 1` e `dia + 1` são apenas para apresentar números mais naturais ao utilizador.

---

## 16. Checklist mental antes de entregar um programa

Antes de considerar o programa terminado, verifica:

- O array tem tamanho suficiente?
- Todos os índices começam em `0`?
- O ciclo usa `< tamanho` e não `<= tamanho`?
- A variável de tamanho é consistente em todo o programa?
- As strings têm espaço para o `'\0'`?
- Foi evitado `gets`?
- Ao usar `fgets`, removeste o `\n` se isso for necessário?
- Ao usar matrizes, linha e coluna estão na ordem certa?
- O programa inicializa valores antes de os usar?

---

## 17. Erros comuns

1. Aceder a uma posição fora do array, como `v[5]` num array de 5 posições.
2. Esquecer que os índices começam em `0`.
3. Usar `<= tamanho` no ciclo e passar uma posição a mais.
4. Ler uma string sem reservar espaço para o `'\0'`.
5. Comparar strings com `==` em vez de `strcmp`.
6. Usar `gets`, que é insegura e não deve ser usada.
7. Confundir linha com coluna numa matriz.
8. Usar valores de um array antes de os inicializar.
9. Escrever números fixos repetidos em vez de constantes como `MAX_ALUNOS`.
10. Não passar o tamanho do array para funções que precisam de o percorrer.

---

## 18. Exercícios propostos

1. Cria um programa que leia 10 números inteiros para um array e mostre apenas os números pares.
2. Cria um programa que leia 8 notas e calcule quantas são positivas.
3. Cria uma função `maior_valor` que receba um array de inteiros e o seu tamanho, devolvendo o maior valor.
4. Cria um programa que leia um nome completo com `fgets` e mostre quantos caracteres tem, sem contar o `\n`.
5. Cria um programa que leia duas palavras e diga se são iguais usando `strcmp`.
6. Cria uma matriz 3x3 de inteiros, lê os seus valores e mostra a soma de todos os elementos.
7. Cria uma matriz 3x3 e mostra apenas a diagonal principal.
8. Cria uma tabela de notas com 3 alunos e 4 testes, mostrando a média de cada aluno.

---

## 19. Changelog

- **2026-05-11**: expansão pedagógica substancial para alunos do 10.º ano, com explicações passo a passo, exemplos guiados, notas de segurança e exercícios.
- **2026-02-23**: reescrita detalhada do módulo com foco pedagógico e exercícios sem resolução.
