# C (10.º Ano) - 14 · Estruturas de Dados Dinâmicas: Apontadores, Acesso e Manipulação

> **Objetivo deste ficheiro**  
> Compreender apontadores em C de forma gradual, percebendo endereços de memória, passagem de endereços para alterar valores, relação com arrays e introdução segura à memória dinâmica.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. Porque este tema parece difícil?](#1-porque-este-tema-parece-difícil)
- [2. Memória: pensar em caixas com moradas](#2-memória-pensar-em-caixas-com-moradas)
- [3. O que é um apontador?](#3-o-que-é-um-apontador)
- [4. Endereço e desreferenciação](#4-endereço-e-desreferenciação)
- [5. Declarar apontadores sem confundir o asterisco](#5-declarar-apontadores-sem-confundir-o-asterisco)
- [6. Alterar variáveis através de apontadores](#6-alterar-variáveis-através-de-apontadores)
- [7. Apontadores e funções](#7-apontadores-e-funções)
- [8. Apontadores e arrays](#8-apontadores-e-arrays)
- [9. O valor `NULL`](#9-o-valor-null)
- [10. Memória estática vs memória dinâmica](#10-memória-estática-vs-memória-dinâmica)
- [11. Funções de memória dinâmica](#11-funções-de-memória-dinâmica)
- [12. O ciclo de vida da memória dinâmica](#12-o-ciclo-de-vida-da-memória-dinâmica)
- [13. Apontadores para `struct`](#13-apontadores-para-struct)
- [14. Introdução a listas ligadas](#14-introdução-a-listas-ligadas)
- [15. Exemplo guiado 1: trocar dois valores](#15-exemplo-guiado-1-trocar-dois-valores)
- [16. Exemplo guiado 2: array dinâmico de notas](#16-exemplo-guiado-2-array-dinâmico-de-notas)
- [17. Exemplo guiado 3: criar uma ficha dinamicamente](#17-exemplo-guiado-3-criar-uma-ficha-dinamicamente)
- [18. Segurança: os erros que mais causam problemas](#18-segurança-os-erros-que-mais-causam-problemas)
- [19. Checklist mental antes de usar apontadores](#19-checklist-mental-antes-de-usar-apontadores)
- [20. Exercícios propostos](#20-exercícios-propostos)
- [21. Changelog](#21-changelog)

---

## 0. Como usar este módulo

Apontadores são um dos temas mais importantes de C. Também são um dos temas em que é mais fácil decorar código sem compreender. Esse caminho corre mal depressa.

A forma certa de estudar é:

1. perceber primeiro o que é um endereço de memória;
2. perceber quando um apontador é realmente necessário;
3. treinar `&` e `*` com exemplos pequenos;
4. usar apontadores para alterar variáveis em funções;
5. rever a ligação entre arrays e apontadores;
6. só depois avançar para `malloc` e `free`;
7. desenhar sempre a memória no papel.

Neste módulo, mais importante do que escrever muito código é conseguir responder:

- Que variável existe?
- Onde está guardada?
- Que valor tem?
- O apontador aponta para onde?
- A memória ainda é válida?

---

## 1. Porque este tema parece difícil?

Em muitos temas anteriores, olhamos para uma variável e pensamos apenas no seu valor:

```c
int idade = 16;
```

Mas em C, além do valor, também existe a posição onde esse valor está guardado na memória.

Com apontadores, passamos a trabalhar com duas ideias ao mesmo tempo:

- o valor guardado;
- o endereço onde esse valor está guardado.

Isto exige mais atenção, porque uma coisa é dizer:

```c
idade
```

e outra coisa é dizer:

```c
&idade
```

A primeira expressão refere-se ao valor da variável. A segunda refere-se ao endereço da variável.

---

## 2. Memória: pensar em caixas com moradas

Imagina a memória como um conjunto enorme de caixas. Cada caixa tem:

- uma morada;
- um conteúdo.

Exemplo conceptual:

| Endereço | Conteúdo |
| -------- | -------- |
| 1000 | 16 |
| 1004 | 20 |
| 1008 | 35 |

Se escrevermos:

```c
int idade = 16;
```

podemos imaginar:

- existe uma caixa chamada `idade`;
- dentro dela está o valor `16`;
- essa caixa tem um endereço.

O endereço real pode variar sempre que o programa executa. Por isso, não devemos decorar números de endereços. Devemos compreender a ideia.

---

## 3. O que é um apontador?

Um apontador é uma variável que guarda um endereço de memória.

Exemplo:

```c
int x = 10;
int *p = &x;
```

Leitura:

- `x` é uma variável inteira com o valor `10`;
- `&x` é o endereço de `x`;
- `p` é um apontador para `int`;
- `p` guarda o endereço de `x`.

Podemos imaginar assim:

| Nome | Conteúdo |
| ---- | -------- |
| `x` | `10` |
| `p` | endereço de `x` |

O apontador não guarda o valor `10`. Guarda a localização onde o `10` está.

### 3.1 Porque precisamos de apontadores se já temos variáveis?

Na maioria dos casos simples, não precisamos de apontadores.

Se queremos apenas guardar e usar um valor dentro da mesma função, uma variável normal chega:

```c
int idade = 16;
idade = idade + 1;
printf("%d\n", idade);
```

O apontador torna-se necessário quando precisamos de trabalhar com o endereço de uma variável, e não apenas com uma cópia do seu valor.

Há três situações muito comuns.

Primeira: alterar uma variável criada fora de uma função.

Em C, uma função recebe cópias dos argumentos:

```c
void aniversario_errado(int idade) {
    idade = idade + 1;
}
```

Se chamarmos esta função:

```c
int idade = 16;
aniversario_errado(idade);
```

a variável original continua com `16`, porque a função alterou apenas a cópia.

Para alterar a variável original, a função precisa do endereço:

```c
void aniversario(int *idade) {
    *idade = *idade + 1;
}
```

Chamada:

```c
int idade = 16;
aniversario(&idade);
```

Agora a função consegue chegar à variável original e alterar o valor guardado lá.

Segunda: trabalhar com memória cujo tamanho só é conhecido durante a execução.

Se o programa só descobre durante a execução quantas notas vão existir, não pode criar um array fixo com esse tamanho escrito no código. Nesse caso, pede memória com `malloc`, e `malloc` devolve um apontador para o bloco reservado.

Terceira: ligar dados entre si.

Em estruturas dinâmicas, como listas ligadas, um nó precisa de apontar para o próximo nó. Não basta guardar apenas valores; é preciso guardar ligações entre posições de memória.

Regra prática:

- usa variáveis normais quando só precisas do valor;
- usa apontadores quando precisas do endereço, de alterar o original, de memória dinâmica ou de ligar estruturas entre si.

---

## 4. Endereço e desreferenciação

Há dois operadores essenciais:

| Operador | Nome simples | O que faz |
| -------- | ------------ | --------- |
| `&` | endereço de | obtém a morada de uma variável |
| `*` | conteúdo apontado por | acede ao valor que está no endereço guardado |

Exemplo:

```c
#include <stdio.h>

int main(void) {
    int x = 10;
    int *p = &x;

    printf("Valor de x: %d\n", x);
    printf("Valor apontado por p: %d\n", *p);

    return 0;
}
```

Neste exemplo:

- `p` contém o endereço de `x`;
- `*p` significa "vai ao endereço guardado em `p` e lê o valor que está lá";
- por isso, `*p` mostra `10`.

### 4.1 Alterar através do apontador

```c
int x = 10;
int *p = &x;

*p = 25;
```

Depois desta linha, `x` passa a valer `25`.

Porquê?

Porque `*p` não altera o apontador. Altera o valor que está no sítio para onde o apontador aponta.

---

## 5. Declarar apontadores sem confundir o asterisco

Esta linha:

```c
int *p;
```

significa:

- `p` é um apontador;
- esse apontador deve apontar para um `int`.

Também podes ler como:

```text
*p é um int
```

Ou seja, "o conteúdo apontado por `p` é um inteiro".

### 5.1 Atenção a várias declarações na mesma linha

```c
int *a, b;
```

Isto declara:

- `a` como apontador para `int`;
- `b` como `int` normal.

Não declara dois apontadores.

Para evitar confusão, em contexto de aprendizagem é melhor escrever:

```c
int *a;
int *b;
```

---

## 6. Alterar variáveis através de apontadores

Se tivermos:

```c
int x = 10;
int *p = &x;
```

podemos alterar `x` de duas formas:

```c
x = 20;
```

ou:

```c
*p = 20;
```

As duas acabam por alterar a mesma zona de memória.

Isto é útil quando queremos que uma função consiga alterar uma variável que foi criada fora dela.

---

## 7. Apontadores e funções

Em C, os argumentos são passados por valor. Isto significa que a função recebe uma cópia.

Exemplo:

```c
void tenta_alterar(int x) {
    x = 100;
}
```

Se chamarmos:

```c
int n = 5;
tenta_alterar(n);
```

`n` continua a valer `5`. A função alterou apenas a cópia.

Para alterar o original, passamos o endereço:

```c
void alterar(int *x) {
    *x = 100;
}
```

Chamada:

```c
int n = 5;
alterar(&n);
```

Agora `n` passa a valer `100`.

Como pensar:

- `&n` envia o endereço de `n`;
- `int *x` recebe esse endereço;
- `*x = 100` altera o valor guardado nesse endereço.

---

## 8. Apontadores e arrays

Arrays e apontadores estão muito ligados em C.

Quando escrevemos:

```c
int valores[3] = {10, 20, 30};
```

o nome `valores`, em muitas situações, comporta-se como o endereço do primeiro elemento.

Exemplo:

```c
int *p = valores;
```

Isto é semelhante a:

```c
int *p = &valores[0];
```

Podemos aceder aos elementos:

```c
printf("%d\n", p[0]); // 10
printf("%d\n", p[1]); // 20
printf("%d\n", p[2]); // 30
```

### 8.1 Aritmética de apontadores

Se `p` aponta para `valores[0]`, então:

```c
*(p + 1)
```

acede ao elemento seguinte, ou seja, `valores[1]`.

Exemplo:

```c
printf("%d\n", *(p + 1)); // 20
```

Para começar, é mais legível usar `p[1]`. Mas é importante saber que esta ligação existe.

---

## 9. O valor `NULL`

`NULL` representa um apontador que não aponta para nenhum objeto válido.

Boa prática:

```c
int *p = NULL;
```

Isto é melhor do que deixar o apontador sem valor inicial.

Apontador não inicializado:

```c
int *p;      // perigoso: contém lixo de memória
*p = 10;     // comportamento indefinido
```

Apontador inicializado:

```c
int *p = NULL;

if (p != NULL) {
    *p = 10;
}
```

Regra simples:

- antes de desreferenciar um apontador, garante que ele aponta para memória válida.

---

## 10. Memória estática vs memória dinâmica

Até aqui, muitos arrays tinham tamanho fixo:

```c
int notas[30];
```

Isto reserva espaço para 30 inteiros. O tamanho está definido no código.

Mas às vezes só sabemos o tamanho durante a execução.

Exemplo:

- o utilizador diz quantas notas quer inserir;
- o programa lê esse número;
- só depois reserva memória.

Para isso usamos memória dinâmica.

Memória dinâmica:

- é pedida durante a execução;
- fica disponível até ser libertada;
- exige verificação de erro;
- exige `free` quando já não é necessária.

---

## 11. Funções de memória dinâmica

Estas funções estão na biblioteca:

```c
#include <stdlib.h>
```

### 11.1 `malloc`

`malloc` reserva um bloco de memória, mas não inicializa os valores.

```c
int *v = malloc(5 * sizeof *v);
```

Leitura:

- queremos espaço para 5 inteiros;
- `sizeof *v` calcula o tamanho do elemento para onde `v` aponta;
- `5 * sizeof *v` calcula o total de bytes;
- `v` guarda o endereço do primeiro elemento.

Também poderias escrever `malloc(5 * sizeof(int))`. A forma `sizeof *v` tem uma vantagem: se o tipo de `v` mudar, o cálculo acompanha automaticamente.

Devemos verificar se a alocação falhou:

```c
if (v == NULL) {
    printf("Falha ao reservar memoria.\n");
    return 1;
}
```

### 11.2 `calloc`

`calloc` também reserva memória, mas inicializa tudo com zero.

```c
int *v = calloc(5, sizeof *v);
```

Leitura:

- queremos 5 elementos;
- cada elemento tem tamanho `sizeof *v`;
- os valores começam a zero.

### 11.3 `realloc`

`realloc` tenta redimensionar um bloco já existente.

Exemplo:

```c
int *novo = realloc(v, 10 * sizeof *v);

if (novo == NULL) {
    printf("Falha ao redimensionar memoria.\n");
    free(v);
    return 1;
}

v = novo;
```

Nota importante: não atribuas diretamente a `v` sem verificar.

Se `realloc` falhar, o bloco original continua válido e `v` continua a apontar para ele. No exemplo anterior fazemos `free(v)` porque o programa vai terminar com erro. Se o programa fosse continuar, poderíamos manter `v` e continuar a usar o bloco antigo.

Evita:

```c
v = realloc(v, 10 * sizeof *v); // perigoso se falhar
```

Se `realloc` falhar, podes perder o endereço original e deixar de conseguir libertar a memória antiga.

### 11.4 `free`

`free` liberta memória dinâmica.

```c
free(v);
v = NULL;
```

Depois de `free`, não devemos usar o conteúdo antigo.

Definir o apontador como `NULL` ajuda a evitar acessos acidentais.

---

## 12. O ciclo de vida da memória dinâmica

Sempre que usas memória dinâmica, pensa neste ciclo:

1. declarar o apontador;
2. reservar memória;
3. verificar se a reserva falhou;
4. usar a memória dentro dos limites;
5. libertar a memória;
6. colocar o apontador a `NULL`, se fizer sentido.

Exemplo do padrão:

```c
int *v = malloc(n * sizeof *v);

if (v == NULL) {
    printf("Falha de memoria.\n");
    return 1;
}

/* usar v */

free(v);
v = NULL;
```

Se faltar o `free`, ocorre uma fuga de memória, também chamada memory leak.

Uma fuga de memória acontece quando o programa perde ou deixa de libertar memória que já não precisa.

---

## 13. Apontadores para `struct`

Apontadores também podem apontar para `struct`.

```c
typedef struct {
    int numero;
    float media;
} Aluno;

Aluno a = {101, 15.3f};
Aluno *p = &a;
```

Para aceder através do apontador:

```c
p->media = 16.0f;
```

Isto é equivalente a:

```c
(*p).media = 16.0f;
```

Mas `->` é a forma mais usada.

Também podemos criar uma `struct` dinamicamente:

```c
Aluno *a = malloc(sizeof *a);

if (a == NULL) {
    return 1;
}

a->numero = 101;
a->media = 15.3f;

free(a);
a = NULL;
```

---

## 14. Introdução a listas ligadas

Uma lista ligada é uma estrutura dinâmica formada por nós.

Cada nó guarda:

- um valor;
- um apontador para o próximo nó.

Exemplo de definição:

```c
typedef struct No {
    int valor;
    struct No *proximo;
} No;
```

Porque aparece `struct No *proximo`?

Porque o nó precisa de apontar para outro nó do mesmo tipo.

Visualmente:

```text
[10 | *] -> [20 | *] -> [30 | NULL]
```

Cada bloco é um nó. O último aponta para `NULL`, indicando que a lista acabou.

Neste módulo, o objetivo é apenas perceber a ideia. A implementação completa de listas ligadas exige bastante cuidado com alocação, ligações e libertação de memória.

---

## 15. Exemplo guiado 1: trocar dois valores

Objetivo: criar uma função que troca dois valores inteiros.

Primeiro, pensa no problema:

- se passarmos `a` e `b` normalmente, a função recebe cópias;
- para alterar os originais, precisamos dos endereços;
- por isso, a função recebe `int *`.

```c
#include <stdio.h>

void trocar(int *x, int *y) {
    int temporario = *x;
    *x = *y;
    *y = temporario;
}

int main(void) {
    int a = 10;
    int b = 20;

    trocar(&a, &b);

    printf("a = %d\n", a);
    printf("b = %d\n", b);

    return 0;
}
```

Explicação da função:

- `x` guarda o endereço de `a`;
- `y` guarda o endereço de `b`;
- `*x` é o valor de `a`;
- `*y` é o valor de `b`;
- usamos `temporario` para não perder um dos valores.

Sem a variável temporária, ao fazer `*x = *y`, o valor original de `*x` seria perdido.

---

## 16. Exemplo guiado 2: array dinâmico de notas

Objetivo: perguntar ao utilizador quantas notas quer inserir e reservar memória para esse número.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;

    printf("Quantas notas? ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("Numero invalido de notas.\n");
        return 1;
    }

    int *notas = malloc(n * sizeof *notas);

    if (notas == NULL) {
        printf("Falha ao reservar memoria.\n");
        return 1;
    }

    int soma = 0;

    for (int i = 0; i < n; i++) {
        printf("Nota %d: ", i + 1);
        scanf("%d", &notas[i]);
        soma += notas[i];
    }

    double media = (double)soma / n;
    printf("Media: %.2f\n", media);

    free(notas);
    notas = NULL;

    return 0;
}
```

Pontos importantes:

- validamos `n` antes de reservar memória;
- usamos `malloc(n * sizeof *notas)`;
- verificamos se `malloc` devolveu `NULL`;
- usamos `notas[i]` como num array normal;
- libertamos a memória no fim.

Neste exemplo, o foco está na memória dinâmica. Num programa mais completo, também validaríamos se cada `scanf` conseguiu ler um número e se cada nota está dentro do intervalo esperado.

---

## 17. Exemplo guiado 3: criar uma ficha dinamicamente

Objetivo: criar dinamicamente uma ficha de aluno.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int numero;
    char nome[50];
    float media;
} Aluno;

int main(void) {
    Aluno *aluno = malloc(sizeof *aluno);

    if (aluno == NULL) {
        printf("Falha ao reservar memoria.\n");
        return 1;
    }

    aluno->numero = 101;
    strcpy(aluno->nome, "Rita");
    aluno->media = 15.3f;

    printf("%d - %s - %.1f\n",
           aluno->numero,
           aluno->nome,
           aluno->media);

    free(aluno);
    aluno = NULL;

    return 0;
}
```

Como ler `aluno->media`:

- `aluno` é um apontador;
- aponta para uma `struct Aluno`;
- `->media` acede ao campo `media` dessa `struct`.

Este exemplo é simples, mas mostra uma ideia importante: a memória da `struct` foi pedida durante a execução.

O uso de `strcpy` aqui é seguro porque `"Rita"` é uma string conhecida e cabe no campo `nome`. Se o nome viesse do utilizador, deveríamos usar leitura segura e respeitar o tamanho do array.

---

## 18. Segurança: os erros que mais causam problemas

Apontadores dão muito poder, mas também permitem erros graves.

### 18.1 Apontador não inicializado

```c
int *p;
*p = 10; // errado
```

`p` contém lixo de memória. Não sabemos para onde aponta.

Melhor:

```c
int *p = NULL;
```

### 18.2 Usar memória depois de libertar

```c
free(v);
printf("%d\n", v[0]); // errado
```

Depois de `free`, a memória já não pertence ao programa.

### 18.3 Libertar duas vezes

```c
free(v);
free(v); // errado
```

Isto pode causar erro grave. Depois de libertar:

```c
free(v);
v = NULL;
```

### 18.4 Aceder fora do bloco

```c
int *v = malloc(5 * sizeof *v);
v[5] = 100; // errado: indices validos são 0 a 4
```

Este erro é semelhante ao erro em arrays estáticos.

### 18.5 Esquecer `free`

```c
int *v = malloc(100 * sizeof *v);
/* programa deixa de precisar de v, mas não faz free */
```

Isto cria uma fuga de memória.

---

## 19. Checklist mental antes de usar apontadores

Antes de escrever ou entregar código com apontadores, confirma:

- Preciso mesmo de um apontador, ou uma variável normal chegava?
- O apontador foi inicializado?
- Aponta para uma variável válida ou para memória dinâmica válida?
- Verifiquei se `malloc` ou `calloc` devolveram `NULL`?
- Estou a usar `*` para aceder ao valor apenas quando o endereço é válido?
- O tamanho usado em `malloc` está correto?
- Os índices estão dentro dos limites?
- Fiz `free` quando já não precisava da memória?
- Evitei usar a memória depois de `free`?
- Evitei fazer `free` duas vezes?
- Se usei `realloc`, guardei o resultado primeiro num apontador temporário?

---

## 20. Exercícios propostos

1. Escreve um programa que declare um inteiro, um apontador para esse inteiro e mostre o valor usando a variável e usando o apontador.
2. Cria uma função `incrementar` que receba um apontador para `int` e aumente o valor original em 1.
3. Cria uma função `trocar` que receba dois apontadores para `int` e troque os valores.
4. Cria um programa que leia `n`, reserve dinamicamente um array de `n` inteiros e mostre todos os valores.
5. Altera o exercício anterior para calcular a soma e a média.
6. Cria dinamicamente uma `struct Produto` com código, nome e preço.
7. Cria uma função que receba um apontador para `Produto` e mostre os seus dados.
8. Experimenta inicializar um array dinâmico com `calloc` e confirma que os valores começam a zero.
9. Desenha no papel uma lista ligada com três nós antes de tentar escrever código.
10. Explica, por palavras tuas, a diferença entre o valor de uma variável e o endereço dessa variável.

---

## 21. Changelog

- **2026-05-19**: acrescentada explicação explícita sobre porque e quando usar apontadores em vez de variáveis normais; reforçadas notas sobre `realloc`, `sizeof *p`, validação de input e segurança em strings dentro de `struct` dinâmica.
- **2026-05-11**: expansão pedagógica substancial para alunos do 10.º ano, com explicações graduais sobre memória, apontadores, `NULL`, alocação dinâmica, segurança e exemplos guiados.
- **2026-02-23**: reescrita completa com explicação detalhada e exercícios sem resolução.
