# C (10.º Ano) - 13 · Estruturas de Dados Compostas: `struct`, `union` e `enum`

> **Objetivo deste ficheiro**  
> Aprender a representar entidades mais completas em C, agrupando dados relacionados com `struct`, usando nomes simbólicos com `enum` e compreendendo o caso especial de `union`.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. Porque precisamos de estruturas compostas?](#1-porque-precisamos-de-estruturas-compostas)
- [2. O problema das variáveis soltas](#2-o-problema-das-variáveis-soltas)
- [3. `struct`: criar um tipo com vários campos](#3-struct-criar-um-tipo-com-vários-campos)
- [4. `typedef`: simplificar o nome do tipo](#4-typedef-simplificar-o-nome-do-tipo)
- [5. Declarar, inicializar e alterar uma `struct`](#5-declarar-inicializar-e-alterar-uma-struct)
- [6. Acesso a campos com o operador ponto](#6-acesso-a-campos-com-o-operador-ponto)
- [7. Arrays de `struct`](#7-arrays-de-struct)
- [8. `struct` dentro de `struct`](#8-struct-dentro-de-struct)
- [9. Passar `struct` para funções](#9-passar-struct-para-funções)
- [10. Acesso a campos com o operador seta](#10-acesso-a-campos-com-o-operador-seta)
- [11. `enum`: valores com nomes claros](#11-enum-valores-com-nomes-claros)
- [12. `union`: vários formatos no mesmo espaço de memória](#12-union-vários-formatos-no-mesmo-espaço-de-memória)
- [13. Escolher entre `struct`, `enum` e `union`](#13-escolher-entre-struct-enum-e-union)
- [14. Exemplo guiado 1: ficha de aluno](#14-exemplo-guiado-1-ficha-de-aluno)
- [15. Exemplo guiado 2: pequena lista de alunos](#15-exemplo-guiado-2-pequena-lista-de-alunos)
- [16. Checklist mental antes de usar tipos compostos](#16-checklist-mental-antes-de-usar-tipos-compostos)
- [17. Erros comuns](#17-erros-comuns)
- [18. Exercícios propostos](#18-exercícios-propostos)
- [19. Changelog](#19-changelog)

---

## 0. Como usar este módulo

Este módulo deve ser estudado depois de compreenderes bem variáveis, arrays e strings.

A ordem recomendada é:

1. compreender primeiro `struct`, porque é a estrutura composta mais importante neste nível;
2. estudar arrays de `struct`, porque são muito usados em programas reais;
3. perceber `enum`, que melhora a legibilidade do código;
4. deixar `union` para o fim, porque é menos comum e exige mais cuidado.

Uma boa forma de estudar este tema é pensar em objetos do mundo real:

- um aluno;
- um livro;
- um produto;
- uma data;
- uma coordenada;
- uma ficha de inscrição.

Cada um destes elementos tem vários dados associados. Uma `struct` permite juntar esses dados.

---

## 1. Porque precisamos de estruturas compostas?

Os tipos simples guardam apenas um valor:

```c
int numero = 12;
float media = 15.4f;
char inicial = 'R';
```

Mas muitos problemas não são feitos de valores isolados. Por exemplo, um aluno pode ter:

- número;
- nome;
- idade;
- média;
- estado de matrícula.

Se usarmos apenas variáveis soltas, o código começa a ficar difícil de organizar.

Uma `struct` permite criar um tipo novo que agrupa vários campos relacionados.

---

## 2. O problema das variáveis soltas

Imagina que queremos guardar dados de um aluno:

```c
int numero_aluno = 101;
char nome_aluno[50] = "Rita";
float media_aluno = 15.3f;
```

Isto ainda é aceitável para um aluno. Mas para três alunos, o código começa a piorar:

```c
int numero_aluno1;
char nome_aluno1[50];
float media_aluno1;

int numero_aluno2;
char nome_aluno2[50];
float media_aluno2;
```

Problemas desta abordagem:

- há muita repetição;
- é fácil trocar dados de alunos diferentes;
- as variáveis relacionadas não estão agrupadas;
- passar estes dados para funções torna-se pouco prático.

Com `struct`, podemos dizer: "um aluno é composto por estes campos".

---

## 3. `struct`: criar um tipo com vários campos

Uma `struct` define um conjunto de campos.

Exemplo:

```c
struct Aluno {
    int numero;
    char nome[50];
    float media;
};
```

Isto cria a descrição de um tipo chamado `struct Aluno`.

Ainda não criámos nenhum aluno concreto. Apenas dissemos ao compilador como é formado um aluno.

Para criar uma variável desse tipo:

```c
struct Aluno a;
```

Agora `a` tem três campos:

- `a.numero`;
- `a.nome`;
- `a.media`.

Pensa numa `struct` como uma ficha:

| Campo  | Valor |
| ------ | ----- |
| número | 101   |
| nome   | Rita  |
| média  | 15.3  |

---

## 4. `typedef`: simplificar o nome do tipo

Em C, se escrevermos apenas:

```c
struct Aluno {
    int numero;
    char nome[50];
    float media;
};
```

temos de declarar variáveis assim:

```c
struct Aluno a;
```

Com `typedef`, podemos criar um nome mais simples:

```c
typedef struct {
    int numero;
    char nome[50];
    float media;
} Aluno;
```

Agora podemos escrever:

```c
Aluno a;
```

Para alunos do 10.º ano, esta forma costuma ser mais limpa e mais fácil de ler.

Resumo:

- `struct` define campos;
- `typedef` dá um nome mais prático ao tipo.

---

## 5. Declarar, inicializar e alterar uma `struct`

Declaração:

```c
Aluno a;
```

Inicialização direta:

```c
Aluno a = {101, "Rita", 15.3f};
```

Aqui a ordem dos valores tem de corresponder à ordem dos campos na `struct`.

Se a `struct` for:

```c
typedef struct {
    int numero;
    char nome[50];
    float media;
} Aluno;
```

então:

```c
Aluno a = {101, "Rita", 15.3f};
```

significa:

- `numero = 101`;
- `nome = "Rita"`;
- `media = 15.3f`.

Também podemos alterar campos depois:

```c
a.numero = 102;
a.media = 16.0f;
```

Para strings, usamos funções próprias:

```c
#include <string.h>

strcpy(a.nome, "Rita Silva");
```

Não escrevas:

```c
a.nome = "Rita Silva"; // errado em C depois da declaração
```

Arrays de caracteres não podem ser atribuídos diretamente dessa forma depois de criados.

---

## 6. Acesso a campos com o operador ponto

O operador `.` serve para aceder a um campo de uma variável `struct`.

Exemplo completo:

```c
#include <stdio.h>

typedef struct {
    int numero;
    char nome[50];
    float media;
} Aluno;

int main(void) {
    Aluno a = {101, "Rita", 15.3f};

    printf("Numero: %d\n", a.numero);
    printf("Nome: %s\n", a.nome);
    printf("Media: %.1f\n", a.media);

    return 0;
}
```

Leitura do código:

- `a` é uma variável do tipo `Aluno`;
- `a.numero` acede ao número desse aluno;
- `a.nome` acede ao nome desse aluno;
- `a.media` acede à média desse aluno.

Quando o campo é uma string, continuamos a tratar esse campo como um array de `char`.

Exemplo de leitura segura de um nome guardado dentro de uma `struct`:

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    int numero;
    char nome[50];
    float media;
} Aluno;

int main(void) {
    Aluno a;

    printf("Nome: ");
    fgets(a.nome, sizeof a.nome, stdin);
    a.nome[strcspn(a.nome, "\n")] = '\0';

    printf("Nome lido: %s\n", a.nome);

    return 0;
}
```

Repara que usamos `sizeof a.nome`, porque queremos a capacidade do campo `nome`, não a capacidade da `struct` completa.

---

## 7. Arrays de `struct`

Uma `struct` representa um registo. Um array de `struct` representa uma lista de registos.

Exemplo:

```c
Aluno turma[30];
```

Isto cria espaço para 30 alunos.

Para aceder ao primeiro aluno:

```c
turma[0]
```

Para aceder à média do primeiro aluno:

```c
turma[0].media
```

Para percorrer a turma:

```c
for (int i = 0; i < 30; i++) {
    printf("%s\n", turma[i].nome);
}
```

Como ler `turma[i].nome`:

1. `turma[i]` escolhe um aluno no array;
2. `.nome` escolhe o campo `nome` desse aluno.

Para adicionar um aluno à turma com dados pedidos ao utilizador:

```c
for (int i = 0; i < 30; i++) {
    printf("Numero: ");
    scanf("%d", &turma[i].numero);
    printf("Nome: ");
    scanf(" %49[^\n]", turma[i].nome); // leitura segura de string
    printf("Media: ");
    scanf("%f", &turma[i].media);
}
```

---

## 8. `struct` dentro de `struct`

Podemos usar uma `struct` como campo de outra `struct`.

Exemplo:

```c
typedef struct {
    int dia;
    int mes;
    int ano;
} Data;

typedef struct {
    int numero;
    char nome[50];
    Data nascimento;
} Aluno;
```

Agora cada aluno tem uma data de nascimento.

Acesso:

```c
Aluno a = {101, "Rita", {12, 5, 2009}};

printf("%d/%d/%d\n",
       a.nascimento.dia,
       a.nascimento.mes,
       a.nascimento.ano);
```

Como ler `a.nascimento.dia`:

1. `a` é o aluno;
2. `nascimento` é o campo que guarda uma `Data`;
3. `dia` é o campo dentro dessa `Data`.

---

## 9. Passar `struct` para funções

Podemos passar uma `struct` para uma função.

Exemplo:

```c
void mostrar_aluno(Aluno a) {
    printf("%d - %s - %.1f\n", a.numero, a.nome, a.media);
}
```

Chamada:

```c
mostrar_aluno(a);
```

Neste caso, a função recebe uma cópia da `struct`. Alterações feitas dentro da função não alteram o aluno original.

Exemplo:

```c
void alterar_media(Aluno a) {
    a.media = 20.0f;
}
```

Esta função altera apenas a cópia.

Para alterar o original, precisamos de apontadores, que serão aprofundados no módulo 14.

---

## 10. Acesso a campos com o operador seta

Esta secção é uma ponte para o módulo 14, onde os apontadores serão estudados com mais detalhe. Para já, o essencial é reconhecer a diferença entre aceder a uma variável `struct` e aceder a uma `struct` através de um apontador.

Quando temos um apontador para uma `struct`, usamos `->` para aceder aos campos.

Exemplo:

```c
Aluno a = {101, "Rita", 15.3f};
Aluno *p = &a;

p->media = 16.0f;
```

Isto é equivalente a:

```c
(*p).media = 16.0f;
```

Mas `p->media` é muito mais legível.

Regra prática:

- se tens uma variável `struct`, usa `.`;
- se tens um apontador para `struct`, usa `->`.

Comparação:

```c
a.media = 16.0f;   // variável normal
p->media = 16.0f;  // apontador para struct
```

---

## 11. `enum`: valores com nomes claros

Um `enum` permite criar um conjunto de valores com nomes.

Exemplo:

```c
typedef enum {
    INATIVO,
    ATIVO,
    BLOQUEADO
} Estado;
```

Agora podemos escrever:

```c
Estado estado = ATIVO;
```

Isto é melhor do que escrever:

```c
int estado = 1;
```

Porque `1` não explica o que significa. É um número mágico.

Com `enum`, o código fica mais claro:

```c
if (estado == BLOQUEADO) {
    printf("Acesso negado.\n");
}
```

### 11.1 O que existe por baixo?

Internamente, os valores de um `enum` são números inteiros.

Por defeito:

```c
typedef enum {
    INATIVO,    // 0
    ATIVO,      // 1
    BLOQUEADO   // 2
} Estado;
```

Mas no programa devemos usar os nomes, não os números.

---

## 12. `union`: vários formatos no mesmo espaço de memória

`union` é o conceito mais avançado deste módulo. Neste nível, o objetivo principal é compreender a ideia e reconhecer situações simples onde ela pode aparecer. Na maioria dos programas iniciais, `struct` e `enum` serão muito mais úteis.

Uma `union` é parecida com uma `struct` na forma de escrever, mas funciona de maneira muito diferente.

Numa `struct`, todos os campos existem ao mesmo tempo.

Numa `union`, os campos partilham a mesma zona de memória. Isso significa que, na prática, só um campo deve ser considerado válido de cada vez.

Exemplo:

```c
typedef union {
    int inteiro;
    float real;
    char texto[20];
} Valor;
```

Podemos fazer:

```c
Valor v;

v.inteiro = 10;
printf("%d\n", v.inteiro);

v.real = 2.5f;
printf("%.1f\n", v.real);
```

Mas depois de escrever em `v.real`, já não devemos assumir que `v.inteiro` continua válido.

### 12.1 Porque é que `union` existe?

`union` é útil quando uma variável pode ter vários formatos possíveis, mas apenas um de cada vez.

Exemplo conceptual:

- uma mensagem pode transportar um número;
- ou pode transportar um texto;
- ou pode transportar um valor decimal.

Mas para alunos que estão a aprender C pela primeira vez, `union` deve ser vista como um tema mais avançado e usado com cuidado.

### 12.2 `union` com `enum`

Muitas vezes usamos `enum` para indicar qual campo da `union` está ativo.

```c
typedef enum {
    TIPO_INTEIRO,
    TIPO_REAL
} TipoValor;

typedef union {
    int inteiro;
    float real;
} Valor;

typedef struct {
    TipoValor tipo;
    Valor valor;
} Dado;
```

A `struct` guarda:

- o tipo de valor;
- o valor propriamente dito.

Isto ajuda a evitar confusões.

---

## 13. Escolher entre `struct`, `enum` e `union`

| Situação                                           | Escolha mais natural |
| -------------------------------------------------- | -------------------- |
| Quero agrupar vários dados de uma entidade         | `struct`             |
| Quero representar opções ou estados com nomes      | `enum`               |
| Quero guardar valores alternativos no mesmo espaço | `union`              |

Exemplos:

- aluno com número, nome e média -> `struct`;
- estado de uma conta: ativa, inativa, bloqueada -> `enum`;
- valor que pode ser inteiro ou real, mas nunca ambos ao mesmo tempo -> `union`.

Na maioria dos programas iniciais, vais usar muito mais `struct` e `enum` do que `union`.

---

## 14. Exemplo guiado 1: ficha de aluno

Objetivo: representar um aluno com número, nome, média e estado.

Antes do código, decide os tipos:

- número -> `int`;
- nome -> `char[]`;
- média -> `float`;
- estado -> `enum`.

```c
#include <stdio.h>

typedef enum {
    ALUNO_INATIVO,
    ALUNO_ATIVO
} EstadoAluno;

typedef struct {
    int numero;
    char nome[50];
    float media;
    EstadoAluno estado;
} Aluno;

int main(void) {
    Aluno a = {101, "Rita Silva", 15.3f, ALUNO_ATIVO};

    printf("Numero: %d\n", a.numero);
    printf("Nome: %s\n", a.nome);
    printf("Media: %.1f\n", a.media);

    if (a.estado == ALUNO_ATIVO) {
        printf("Estado: ativo\n");
    } else {
        printf("Estado: inativo\n");
    }

    return 0;
}
```

Pontos importantes:

- `EstadoAluno` evita usar `0` e `1` sem significado;
- a `struct Aluno` junta dados que pertencem à mesma entidade;
- `a.estado == ALUNO_ATIVO` é legível mesmo para quem lê o código pela primeira vez.

---

## 15. Exemplo guiado 2: pequena lista de alunos

Objetivo: guardar três alunos e mostrar apenas os que têm média positiva.

```c
#include <stdio.h>

#define TOTAL_ALUNOS 3

typedef struct {
    int numero;
    char nome[50];
    float media;
} Aluno;

int main(void) {
    Aluno turma[TOTAL_ALUNOS] = {
        {101, "Rita", 15.3f},
        {102, "Miguel", 9.8f},
        {103, "Ines", 13.5f}
    };

    printf("Alunos com media positiva:\n");

    for (int i = 0; i < TOTAL_ALUNOS; i++) {
        if (turma[i].media >= 10.0f) {
            printf("%d - %s - %.1f\n",
                   turma[i].numero,
                   turma[i].nome,
                   turma[i].media);
        }
    }

    return 0;
}
```

Como ler a expressão `turma[i].media`:

- `turma` é o array;
- `i` escolhe a posição;
- `.media` escolhe o campo da `struct` nessa posição.

Este padrão é muito comum em programas de gestão simples.

---

## 16. Checklist mental antes de usar tipos compostos

Antes de criares uma `struct`, pergunta:

- Estes dados pertencem todos à mesma entidade?
- Os nomes dos campos são claros?
- A ordem dos campos faz sentido?
- Algum campo deve ser uma string? Se sim, tem tamanho suficiente?
- Se vou ler texto para um campo `char[]`, estou a usar leitura segura, como `fgets`?
- Algum campo representa estado? Talvez um `enum` ajude.
- Vou precisar de vários registos? Talvez precise de um array de `struct`.
- Vou alterar a `struct` dentro de uma função? Então talvez precise de apontador.

---

## 17. Erros comuns

1. Criar muitas variáveis soltas quando uma `struct` seria mais clara.
2. Confundir o nome do tipo com o nome da variável.
3. Esquecer `typedef` e depois tentar declarar sem `struct`.
4. Usar `.` quando se tem um apontador, em vez de `->`.
5. Usar `->` quando se tem uma variável normal, em vez de `.`.
6. Tentar atribuir diretamente uma nova string a um array de `char`.
7. Ler nomes compostos com `scanf("%s", ...)` e perder tudo depois do primeiro espaço.
8. Usar números como estados em vez de `enum`.
9. Usar uma `union` sem guardar qual campo está válido.
10. Não inicializar todos os campos importantes.
11. Passar uma `struct` para uma função e esperar que a original seja alterada.

---

## 18. Exercícios propostos

1. Define uma `struct Livro` com título, autor, ano e preço.
2. Cria uma variável do tipo `Livro` e mostra todos os seus campos.
3. Cria um array com 5 livros e mostra apenas os publicados depois de 2020.
4. Define uma `struct Produto` com código, nome, preço e stock.
5. Cria uma função que receba um `Produto` e mostre os seus dados.
6. Cria um `enum EstadoPedido` com os valores `PENDENTE`, `ENVIADO` e `ENTREGUE`.
7. Acrescenta o `EstadoPedido` a uma `struct Pedido`.
8. Cria uma `struct Data` e usa-a dentro de uma `struct Aluno`.
9. Cria uma função que receba um array de alunos e mostre apenas os alunos com média positiva.
10. Pesquisa um exemplo simples de `union` e explica, por palavras tuas, porque só um campo deve ser usado de cada vez.

---

## 19. Changelog

- **2026-05-18**: reforço pedagógico sobre leitura segura de strings dentro de `struct`, indicação explícita de que `->` antecipa apontadores e clarificação do papel introdutório de `union`.
- **2026-05-11**: expansão pedagógica substancial para alunos do 10.º ano, com explicações progressivas, exemplos guiados, distinção clara entre `struct`, `enum` e `union`, e exercícios.
- **2026-02-23**: reescrita completa do módulo com detalhe pedagógico e exercícios sem resolução.
