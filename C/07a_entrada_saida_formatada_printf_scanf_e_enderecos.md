![Header](../Images/Header.png)

# C (10.º Ano) - 07A · Entrada/Saída Formatada (`printf`/`scanf`) e Endereços (`&` e `*`)

> **Objetivo deste ficheiro**  
> Dominar entrada/saída formatada em C com rigor técnico: usar `printf` e `scanf` com formatos corretos, validar entradas e compreender o papel de `&` e `*`.

---

## Índice

- [0. Como usar este módulo](#0-como-usar-este-módulo)
- [1. O que este módulo resolve](#1-o-que-este-módulo-resolve)
- [2. Modelo mental: valor e endereco](#2-modelo-mental-valor-e-endereco)
- [3. `printf` em detalhe](#3-printf-em-detalhe)
- [4. Largura, precisão, alinhamento e escapes](#4-largura-precisão-alinhamento-e-escapes)
- [5. `scanf` em detalhe](#5-scanf-em-detalhe)
- [6. Espaços, separadores e newline no buffer](#6-espaços-separadores-e-newline-no-buffer)
- [7. Strings: `scanf("%s")` vs `fgets`](#7-strings-scanfs-vs-fgets)
- [8. Segurança e robustez na entrada de dados](#8-segurança-e-robustez-na-entrada-de-dados)
- [9. Exemplo guiado progressivo](#9-exemplo-guiado-progressivo)
- [10. Erros comuns e diagnóstico](#10-erros-comuns-e-diagnóstico)
- [11. Ponte para apontadores](#11-ponte-para-apontadores)
- [12. Changelog](#12-changelog)

---

## 0. Como usar este módulo

1. Lê as secções 2, 3 e 5 sem saltar: são a base de quase todos os exercícios com input.
2. Compila sempre com warnings ativados (`-Wall -Wextra -Wpedantic -std=c11`).
3. Treina primeiro com `int`/`double` e só depois avança para strings.
4. Sempre que usares `scanf`, valida o valor de retorno.

---

## 1. O que este módulo resolve

Problemas muito comuns no início:

- programa "aceita lixo" porque `scanf` falhou e o retorno foi ignorado;
- crash ou comportamento indefinido por falta de `&` no `scanf`;
- formatadores trocados (`%d` para `float`, `%f` para `double` em `scanf`);
- leitura incompleta de texto por uso incorreto de `%s`;
- confusão entre valor da variável e endereço da variável.

No fim deste módulo deves conseguir:

- imprimir dados com formatação controlada;
- ler dados de forma segura e validar entrada;
- explicar tecnicamente porque `scanf` precisa de endereços;
- decidir quando usar `scanf("%s")` e quando usar `fgets`.

---

## 2. Modelo mental: valor e endereco

Em C, cada variável fica numa posição de memória (endereço).

```c
int idade = 16;
```

- **valor** de `idade`: `16`;
- **endereço** de `idade`: algo como `0x7ff...` (depende da execução).

Operadores base:

- `&x` -> obtém o endereço de `x`;
- `*p` -> acede ao valor guardado no endereço apontado por `p`.

Exemplo:

```c
int x = 10;
int *p = &x;

printf("Valor de x: %d\n", x);
printf("Endereco de x: %p\n", (void *)&x);
printf("Valor via p: %d\n", *p);
```

Ligação com `scanf`:

- `scanf` precisa de um lugar onde escrever o valor lido;
- por isso passamos o endereço da variável.

```c
int n;
scanf("%d", &n); // correto: scanf escreve no endereco de n
```

Sem `&`, `scanf` recebe um número qualquer como se fosse endereço e pode causar erro grave.

---

## 3. `printf` em detalhe

`printf` imprime texto formatado no ecrã.

Formato geral:

```c
printf("texto ... %<formato> ...", variavel1, variavel2, ...);
```

Especificadores mais usados:

- `%d` -> `int`
- `%u` -> `unsigned int`
- `%f` -> `double` em `printf` (também funciona para `float` por promoção automática)
- `%lf` -> equivalente prático a `%f` em `printf` (preferir `%f` por clareza)
- `%c` -> `char`
- `%s` -> string (`char[]` ou `char *`)
- `%p` -> endereço (ponteiro), com cast para `(void *)`

Exemplo:

```c
int idade = 16;
unsigned int turmas = 3;
double media = 14.75;
char inicial = 'N';
char nome[] = "Nuno";

printf("Idade: %d\n", idade);
printf("Turmas: %u\n", turmas);
printf("Media: %.2f\n", media);
printf("Inicial: %c\n", inicial);
printf("Nome: %s\n", nome);
printf("Endereco de media: %p\n", (void *)&media);
```

Regra crítica:

- ordem e tipo dos argumentos têm de corresponder aos especificadores.

---

## 4. Largura, precisão, alinhamento e escapes

### 4.1 Largura e alinhamento

```c
printf("|%10d|\n", 42);   // alinhado à direita, largura 10
printf("|%-10d|\n", 42);  // alinhado à esquerda, largura 10
```

### 4.2 Precisão em números reais

```c
double x = 3.14159265;
printf("%.2f\n", x); // 3.14
printf("%.4f\n", x); // 3.1416
```

### 4.3 Largura + precisão

```c
double preco = 12.5;
printf("|%8.2f|\n", preco); // largura 8, 2 casas decimais
```

### 4.4 Escapes úteis

- `\n` nova linha
- `\t` tabulação
- `\"` aspas dentro de string
- `\\` barra invertida literal

---

## 5. `scanf` em detalhe

`scanf` lê dados da entrada padrão (teclado por defeito).

Formato geral:

```c
scanf("formato", &var1, &var2, ...);
```

Retorno de `scanf`:

- devolve quantos campos foram lidos com sucesso;
- usar este retorno é obrigatório para código robusto.

Exemplos:

```c
int idade;
if (scanf("%d", &idade) != 1) {
    printf("Entrada invalida para idade.\n");
}
```

```c
int a, b;
if (scanf("%d %d", &a, &b) != 2) {
    printf("Precisavas de inserir dois inteiros.\n");
}
```

Especificadores usuais no `scanf`:

- `%d` -> `int` (usa `&int`)
- `%f` -> `float` (usa `&float`)
- `%lf` -> `double` (usa `&double`)
- `%c` -> `char` (usa `&char`)
- `%s` -> string (`char[]`, normalmente sem `&` porque o array já "decai" para ponteiro)

Exemplo com `double`:

```c
double nota;
if (scanf("%lf", &nota) != 1) {
    printf("Valor invalido.\n");
}
```

---

## 6. Espaços, separadores e newline no buffer

`scanf` trata espaços (` `, `\n`, `\t`) como separadores na maioria dos formatos.

Exemplo:

```c
int d, m, a;
scanf("%d/%d/%d", &d, &m, &a); // lê formato tipo 15/04/2026
```

Caso especial de `%c`:

- `%c` lê também whitespace;
- para ignorar whitespace anterior, usa espaço antes de `%c`.

```c
char opcao;
scanf(" %c", &opcao); // nota o espaço inicial
```

Problema típico:

- ler um número com `scanf` e logo depois uma linha de texto;
- o `\n` pendente pode ser apanhado pela leitura seguinte.

Estratégias:

- usar `fgets` para linhas;
- planear ordem das leituras;
- limpar newline de forma controlada quando necessário.

---

## 7. Strings: `scanf("%s")` vs `fgets`

### 7.1 `scanf("%s")`

Vantagens:

- simples para uma palavra sem espaços.

Limitações:

- para no primeiro espaço;
- risco de overflow sem limite de largura.

Exemplo mais seguro:

```c
char nome[30];
if (scanf("%29s", nome) != 1) {
    printf("Falha na leitura do nome.\n");
}
```

### 7.2 `fgets`

Vantagens:

- lê a linha completa (inclui espaços);
- permite controlar tamanho máximo do buffer.

Exemplo:

```c
char linha[100];
if (fgets(linha, sizeof(linha), stdin) == NULL) {
    printf("Falha na leitura da linha.\n");
}
```

Observação:

- `fgets` pode guardar `\n` no fim da string; normalmente removes depois.

### 7.3 Quando usar cada um

- palavra única (ex.: código curto): `scanf("%Ns", ...)` com limite;
- nome completo, morada, frase: `fgets`.


```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char nome[100];

    printf("Nome completo: ");
    if (fgets(nome, sizeof nome, stdin) == NULL) {
        printf("Erro na leitura.\n");
        return 1;
    }

    // remove o '\n' final, se existir
    nome[strcspn(nome, "\n")] = '\0';

    printf("Leste: %s\n", nome);
    return 0;
}
```

---

## 8. Segurança e robustez na entrada de dados

Boas práticas essenciais:

1. verifica sempre retorno de `scanf`/`fgets`;
2. define limites de tamanho em strings;
3. não uses variáveis que não foram lidas com sucesso;
4. mostra mensagens de erro específicas;
5. compila com warnings ativos para apanhar formatos errados.

Exemplo de padrão robusto:

```c
double preco;
printf("Preco: ");
if (scanf("%lf", &preco) != 1) {
    printf("Entrada invalida para preco.\n");
    return 1;
}
```

---

## 9. Exemplo guiado progressivo

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    int idade;
    double media;
    char turma;
    char nome[64];

    printf("Idade: ");
    if (scanf("%d", &idade) != 1) {
        printf("Erro: idade invalida.\n");
        return 1;
    }

    printf("Media final: ");
    if (scanf("%lf", &media) != 1) {
        printf("Erro: media invalida.\n");
        return 1;
    }

    printf("Turma (A/B/C): ");
    if (scanf(" %c", &turma) != 1) {
        printf("Erro: turma invalida.\n");
        return 1;
    }

    // Consome o '\n' pendente antes do fgets
    int ch;
    while ((ch = getchar()) != '\n' && ch != EOF) { }

    printf("Nome completo: ");
    if (fgets(nome, sizeof(nome), stdin) == NULL) {
        printf("Erro: falha ao ler nome.\n");
        return 1;
    }

    size_t len = strlen(nome);
    if (len > 0 && nome[len - 1] == '\n') {
        nome[len - 1] = '\0';
    }

    printf("\n--- Resumo ---\n");
    printf("Nome: %s\n", nome);
    printf("Idade: %d\n", idade);
    printf("Media: %.2f\n", media);
    printf("Turma: %c\n", turma);
    printf("Endereco da idade: %p\n", (void *)&idade);

    return 0;
}
```

O que este exemplo consolida:

- leitura validada de `int` e `double`;
- uso correto de `" %c"` para `char`;
- leitura de linha com `fgets`;
- remoção de newline;
- impressão de endereço com `%p`.

---

## 10. Erros comuns e diagnóstico

1. **Esquecer `&` em variáveis simples**
   `scanf("%d", n);` (errado) -> deve ser `scanf("%d", &n);`
2. **Formato incompatível**
   `double x; scanf("%f", &x);` (errado) -> usar `%lf`
3. **Ignorar retorno de `scanf`**
   Pode deixar variável sem valor válido.
4. **Overflow em string**
   `scanf("%s", nome);` sem limite é perigoso.
5. **`%c` a ler `\n` inesperado**
   Resolver com espaço antes do `%c` (`" %c"`).

Diagnóstico técnico:

- compila com warnings;
- testa entradas válidas e inválidas;
- adiciona prints temporários para validar fluxo;
- confirma sempre quantos campos foram lidos.

---

## 11. Ponte para apontadores

Neste módulo viste `&` e `*` no contexto de I/O.

Para aprofundar ponteiros, memória dinâmica e estruturas ligadas, segue para:

- [14_estruturas_dinamicas_apontadores.md](./14_estruturas_dinamicas_apontadores.md)

Relação prática:

- aqui: "como passar endereço para funções como `scanf`";
- no módulo 14: "como gerir memória e ponteiros com profundidade".

---

## 12. Changelog

- **2026-04-15**: exercícios refeitos com progressão incremental e foco apenas na matéria coberta até este módulo.
- **2026-04-15**: criação do módulo dedicado de `printf`/`scanf` com explicação de `&` e `*`, validação de input e comparação `scanf` vs `fgets`.

![Footer](../Images/Footer.png)
