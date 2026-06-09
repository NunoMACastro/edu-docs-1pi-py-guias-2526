![Header](../Images/Header.png)

# C (10.º Ano) - 20 · Exercícios

---

## Índice de exercícios por módulo

1. [07 · Dados, Variáveis, Declarações, Expressões, Constantes e Tipos](#exercicios-07)
2. [07A · Entrada/Saída Formatada (`printf`/`scanf`) e Endereços (`&` e `*`)](#exercicios-07a)
3. [08 · Operadores em C](#exercicios-08)
4. [09 · Estruturas de Controlo em C](#exercicios-09)
5. [10 · Subprogramas: Funções, Variáveis Locais/Globais e Parâmetros](#exercicios-10)
6. [11 · Funcionalidades de um Editor de Texto](#exercicios-11)
7. [12 · Estruturas de Dados Estáticas: Strings, Arrays e Matrizes](#exercicios-12)
8. [13 · Estruturas de Dados Compostas: `struct`, `union` e `enum`](#exercicios-13)
9. [14 · Estruturas de Dados Dinâmicas: Apontadores, Acesso e Manipulação](#exercicios-14)
10. [15 · Classes e Objetos (Contexto em C)](#exercicios-15)
11. [16 · Herança e Polimorfismo (Contexto em C)](#exercicios-16)
12. [17 · Exceções e Tratamento de Erros em C](#exercicios-17)
13. [18 · Ficheiros: Acesso e Manipulação em C](#exercicios-18)
14. [19 · Funcionalidades de Editor de Texto (Produtividade e Debug)](#exercicios-19)

---

<a id="exercicios-07"></a>

## 07 · Dados, Variáveis, Declarações, Expressões, Constantes e Tipos

Fonte: [07_dados_variaveis_constantes_tipos.md](./07_dados_variaveis_constantes_tipos.md)

### Exercício 1 - Declarações

Objetivo: treinar declaração de variáveis com nomes claros e tipos corretos.

Cria um programa que declara variáveis para os seguintes campos de uma ficha digital de aluno:

Número, nome, turma, idade, média e faltas (%).

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Lista os campos da "ficha digital": número, nome, turma, idade, média e faltas (%).
2. Decide o tipo de cada campo antes de escrever código.
3. Define nomes descritivos (evita nomes genéricos como `x`, `a1`, `valor`).
4. Escreve apenas as declarações (com ou sem inicialização, conforme preferires).
5. Revê se cada variável representa exatamente um dado real da ficha.

> Resolução:

```c
#include <stdio.h>

int main() {
    int numero_aluno; // Número de identificação do aluno
    char nome[50];   // Nome completo do aluno (máximo 49 caracteres + '\0')
    char turma[10];  // Turma do aluno (ex.: "10A")
    int idade;       // Idade do aluno em anos
    double media;    // Média final do aluno (pode ter casas decimais)
    double faltas;   // Percentagem de faltas (0.0 a 100.0)

    return 0;
}
```

### Exercício 2 - Tipos corretos

Objetivo: justificar escolhas de tipos com base no domínio do problema.

Num cenário de bicicletas partilhadas, escolhe e justifica os tipos para:

id da bicicleta, quilómetros totais, custo por minuto, estado (disponível/ocupada) e nível de bateria.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Separa os dados do sistema: id, quilómetros, custo/minuto, estado e bateria.
2. Para cada dado, pergunta: "é inteiro, decimal, texto ou estado lógico?"
3. Escolhe um tipo para cada campo e escreve uma mini justificação técnica.
4. Verifica se o tipo escolhido suporta o intervalo esperado de valores.
5. Confirma consistência entre campos parecidos (ex.: valores monetários).

> Resolução:

```c

#include <stdio.h>

int main() {
    int id_bicicleta;          // ID único da bicicleta, geralmente um número inteiro
    double quilometros_totais; // Quilómetros totais percorridos, pode ter casas decimais
    double custo_por_minuto;   // Custo por minuto de uso, valor monetário com casas decimais
    int estado;                // Estado da bicicleta: 0 para disponível, 1 para ocupada (pode ser enum ou bool)
    int nivel_bateria;         // Nível de bateria em percentagem (0 a 100), pode ser inteiro

    return 0;
}
```

### Exercício 3 - Constantes

Objetivo: distinguir quando usar `const` e quando usar `#define`.

Define as constantes de um sistema de mobilidade elétrica:

limite de velocidade, preço fixo de desbloqueio e taxa por minuto.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os valores fixos: limite de velocidade, preço de desbloqueio e taxa por minuto.
2. Decide quais constantes vais declarar com `const` e/ou com `#define`.
3. Mantém uma convenção única de nomes para todas as constantes.
4. Coloca as constantes numa zona visível do programa (topo do ficheiro).
5. Revê se nenhuma constante ficou "hardcoded" no meio dos cálculos.

> Resolução:

```c
#include <stdio.h>

#define LIMITE_VELOCIDADE 25.0 // Limite de velocidade em km/h
#define PRECO_DESBLOQUEIO 1.00 // Preço fixo para desbloquear a bicicleta

const double TAXA_POR_MINUTO = 0.15; // Taxa por minuto de uso

int main() {
    // O programa pode usar as constantes definidas acima para cálculos e lógica
    // Exemplo de uso:
    double custo_total = PRECO_DESBLOQUEIO + (TAXA_POR_MINUTO * 15); // Custo para 15 minutos de uso
    printf("Custo total para 15 minutos: %.2f euros\n", custo_total);
    return 0;
}
```

### Exercício 4 - Expressões

Objetivo: montar uma expressão aritmética e apresentar resultado formatado.

Calcula o custo total de uma viagem de 15 minutos de trotinete, usando:

`#define PRECO_FIXO 1.00` e `const double TAXA_MINUTO = 0.15`.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Declara as constantes obrigatórias: `PRECO_FIXO` e `TAXA_MINUTO`.
2. Define a duração da viagem (15 minutos) numa variável apropriada.
3. Escreve a expressão do custo total separando parte fixa e parte variável.
4. Guarda o resultado numa variável de tipo adequado.
5. Imprime o valor final com formatação monetária (casas decimais consistentes).

> Resolução:

```c
#include <stdio.h>

#define PRECO_FIXO 1.00 // Preço fixo para desbloquear a trotinete
const double TAXA_MINUTO = 0.15; // Taxa por minuto de uso
int main() {
    int duracao_minutos = 15; // Duração da viagem em minutos

    // Calcula o custo total
    double custo_total = PRECO_FIXO + (TAXA_MINUTO * duracao_minutos);

    // Imprime o resultado formatado como valor monetário
    printf("Custo total para %d minutos: %.2f euros\n", duracao_minutos, custo_total);

    return 0;
}
```

### Exercício 5 - Casting

Objetivo: perceber o impacto do casting em divisões e percentagens.

Num painel de estatísticas, calcula média de pontos por jogo e taxa de vitórias:

primeiro sem cast e depois com cast, comparando os resultados.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Cria dados de teste para jogos, pontos totais e vitórias.
2. Calcula média e taxa usando apenas divisão inteira.
3. Calcula novamente os mesmos indicadores com cast explícito.
4. Mostra os dois resultados lado a lado no output.
5. Escreve uma explicação curta sobre porque os valores mudam.

> Resolução:

```c
#include <stdio.h>

int main() {
    int jogos = 10;          // Total de jogos
    int pontos_totais = 85;  // Total de pontos marcados
    int vitorias = 6;        // Total de vitórias

    // Cálculo sem cast (divisão inteira)
    int media_pontos_sem_cast = pontos_totais / jogos; // Resultado inteiro
    int taxa_vitorias_sem_cast = (vitorias * 100) / jogos; // Resultado inteiro em percentagem

    // Cálculo com cast (divisão real)
    double media_pontos_com_cast = (double)pontos_totais / jogos; // Resultado com casas decimais
    double taxa_vitorias_com_cast = ((double)vitorias * 100) / jogos; // Resultado com casas decimais

    // Imprime os resultados
    printf("Média de pontos por jogo (sem cast): %d\n", media_pontos_sem_cast);
    printf("Taxa de vitórias (sem cast): %d%%\n", taxa_vitorias_sem_cast);
    printf("Média de pontos por jogo (com cast): %.2f\n", media_pontos_com_cast);
    printf("Taxa de vitórias (com cast): %.2f%%\n", taxa_vitorias_com_cast);

    return 0;
}
```

### Exercício 6 - Entrada/saída

Objetivo: praticar leitura de dados e impressão alinhada.

Lê nome do produto, quantidade e preço unitário, e apresenta:

um resumo de compra alinhado, com subtotal e total a 2 casas decimais.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Declara variáveis para nome do produto, quantidade e preço unitário.
2. Lê os dados com formatos adequados para cada tipo.
3. Calcula subtotal e total (se aplicável ao teu cenário).
4. Imprime um resumo em colunas alinhadas com `printf`.
5. Garante que valores monetários aparecem com 2 casas decimais.

> Resolução:

```c
#include <stdio.h>

int main() {
    char nome_produto[50]; // Nome do produto
    int quantidade;        // Quantidade comprada
    double preco_unitario; // Preço por unidade

    // Lê os dados do utilizador
    printf("Escreve o nome do produto: ");
    scanf("%49s", nome_produto); // Limita a leitura para evitar overflow
    printf("Escreve a quantidade: ");
    scanf("%d", &quantidade);
    printf("Escreve o preço unitário: ");
    scanf("%lf", &preco_unitario);

    // Calcula subtotal e total (sem impostos para simplicidade)
    double subtotal = quantidade * preco_unitario;

    // Imprime o resumo da compra alinhado
    printf("\nResumo da Compra:\n");
    printf("%-20s %10s %15s\n", "Produto", "Quantidade", "Preço Unitário");
    printf("%-20s %10d %15.2f\n", nome_produto, quantidade, preco_unitario);
    printf("\nSubtotal: %.2f euros\n", subtotal);

    return 0;
}
```

### Exercício 7 - Conversão de unidades

Objetivo: aplicar fórmulas de conversão com atenção ao tipo de dados.

Cria um mini conversor de meteorologia que lê:

temperatura em Celsius e velocidade do vento em km/h, mostrando Fahrenheit e m/s.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Declara variáveis para Celsius e velocidade em km/h.
2. Lê os dois valores introduzidos pelo utilizador.
3. Implementa a conversão de Celsius para Fahrenheit.
4. Implementa a conversão de km/h para m/s.
5. Mostra os resultados com unidades e formatação clara.

> Resolução:

```c
#include <stdio.h>

int main() {
    double temperatura_celsius; // Temperatura em Celsius
    double velocidade_kmh;      // Velocidade do vento em km/h

    // Lê os dados do utilizador
    printf("Escreve a temperatura em Celsius: ");
    scanf("%lf", &temperatura_celsius);
    printf("Escreve a velocidade do vento em km/h: ");
    scanf("%lf", &velocidade_kmh);

    // Converte Celsius para Fahrenheit
    double temperatura_fahrenheit = (temperatura_celsius * 9.0 / 5.0) + 32.0;

    // Converte km/h para m/s
    double velocidade_ms = velocidade_kmh / 3.6;

    // Imprime os resultados
    printf("\nTemperatura: %.2f °C = %.2f °F\n", temperatura_celsius, temperatura_fahrenheit);
    printf("Velocidade do vento: %.2f km/h = %.2f m/s\n", velocidade_kmh, velocidade_ms);

    return 0;
}
```

### Exercício 8 - Validação básica

Objetivo: validar limites antes de aceitar um valor como válido.

Lê a percentagem de bateria de um dispositivo (0 a 100) e:

valida o valor, emitindo erro claro se estiver fora do intervalo.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Lê a percentagem de bateria para uma variável numérica.
2. Define explicitamente o intervalo válido: 0 a 100.
3. Cria uma condição para detetar valores fora do intervalo.
4. Se inválido, apresenta mensagem de erro objetiva.
5. Se válido, mostra confirmação com o valor lido.

> Resolução:

```c

#include <stdio.h>

int main() {
    double percentagem_bateria; // Percentagem de bateria

    // Lê a percentagem de bateria do utilizador
    printf("Escreve a percentagem de bateria (0-100): ");
    scanf("%lf", &percentagem_bateria);

    // Valida o valor lido
    if (percentagem_bateria < 0.0 || percentagem_bateria > 100.0) {
        printf("Erro: A percentagem de bateria deve estar entre 0 e 100.\n");
    } else {
        printf("Percentagem de bateria válida: %.2f%%\n", percentagem_bateria);
    }

    return 0;
}
```

### Exercício 9 - Formatação

Objetivo: melhorar legibilidade de output em formato de tabela.

Mostra um placar com 3 jogadores contendo:

nome, pontos e precisão (%), com colunas alinhadas em `printf`.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Define dados de 3 jogadores (nome, pontos e precisão).
2. Planeia a largura de cada coluna antes de imprimir.
3. Imprime cabeçalho do placar.
4. Imprime as 3 linhas com especificadores de largura em `printf`.
5. Revê alinhamento visual no terminal e ajusta larguras se necessário.

> Resolução:

```c

#include <stdio.h>

int main() {
    // Dados dos jogadores
    char nome_jogadores[3][20] = {"Alice", "Bob", "Charlie"};
    int pontos[3] = {1500, 1200, 1800};
    double precisao[3] = {85.5, 78.2, 92.3};

    // Imprime o placar com colunas alinhadas
    printf("%-20s %10s %15s\n", "Nome", "Pontos", "Precisão (%)");
    printf("--------------------------------------------------\n");
    for (int i = 0; i < 3; i++) {
        printf("%-20s %10d %15.2f\n", nome_jogadores[i], pontos[i], precisao[i]);
    }

    return 0;
}
```

### Exercício 10 - Diagnóstico

Objetivo: diagnosticar e corrigir erros clássicos de formatação e leitura.

Analisa um trecho com erros em `%d`, `%f`, `%lf` e no uso de `&` no `scanf`,

depois corrige e justifica tecnicamente cada ajuste.

Requisitos:

- Identifica primeiro o comportamento errado ou o erro produzido.
- Explica a causa antes de apresentar a correção.
- Corrige apenas o necessário para resolver o problema indicado.
- Confirma a solução com compilação, execução ou análise manual adequada.

Passo a passo:

1. Prepara um pequeno trecho com erros propositados de `%d`, `%f`, `%lf` e `&`.
2. Compila com avisos ativos (`-Wall -Wextra`) para localizar problemas.
3. Corrige cada linha um erro de cada vez.
4. Em cada correção, escreve uma frase com o motivo técnico.
5. Recompila até não existirem avisos relacionados com formatos.

> Resolução:

```c

#include <stdio.h>

int main() {
    int idade; // Correção: tipo deve ser int para idade
    double altura; // Correção: tipo deve ser double para altura
    char nome[50]; // Correção: tipo deve ser char array para nome

    // Lê os dados do utilizador
    printf("Escreve a tua idade: ");
    scanf("%d", &idade); // Correção: %d para int e uso de & para variável

    printf("Escreve a tua altura em metros: ");
    scanf("%lf", &altura); // Correção: %lf para double e uso de & para variável

    printf("Escreve o teu nome: ");
    scanf("%49s", nome); // Correção: %s para string e limite de leitura

    // Imprime os dados lidos
    printf("\nIdade: %d anos\n", idade);
    printf("Altura: %.2f metros\n", altura);
    printf("Nome: %s\n", nome);

    return 0;
}
```

### Exercício 11 - Mini programa

Objetivo: integrar entrada, cálculo e apresentação num mini projeto.

Desenvolve um simulador de consumo elétrico doméstico que lê:

potência (W), horas de uso por dia e preço por kWh, e estima consumo e custo mensais.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Lê potência (W), horas por dia e preço por kWh.
2. Converte potência para kW antes de calcular energia.
3. Calcula consumo diário e depois consumo mensal.
4. Calcula custo mensal estimado com base no preço por kWh.
5. Apresenta um resumo final com unidades e casas decimais adequadas.

> Resolução:

```c

#include <stdio.h>

int main() {
    double potencia_watts; // Potência em watts
    double horas_por_dia; // Horas de uso por dia
    double preco_kwh;     // Preço por kWh

    // Lê os dados do utilizador
    printf("Escreve a potência do aparelho em watts: ");
    scanf("%lf", &potencia_watts);
    printf("Escreve as horas de uso por dia: ");
    scanf("%lf", &horas_por_dia);
    printf("Escreve o preço por kWh: ");
    scanf("%lf", &preco_kwh);

    // Converte potência para kW
    double potencia_kw = potencia_watts / 1000.0;

    // Calcula consumo diário e mensal
    double consumo_diario_kwh = potencia_kw * horas_por_dia;
    double consumo_mensal_kwh = consumo_diario_kwh * 30; // Aproximando 30 dias

    // Calcula custo mensal
    double custo_mensal = consumo_mensal_kwh * preco_kwh;

    // Apresenta o resumo final
    printf("\nConsumo diário: %.2f kWh\n", consumo_diario_kwh);
    printf("Consumo mensal: %.2f kWh\n", consumo_mensal_kwh);
    printf("Custo mensal estimado: %.2f euros\n", custo_mensal);

    return 0;
}
```

---

<a id="exercicios-07a"></a>

## 07A · Entrada/Saída Formatada (`printf`/`scanf`) e Endereços (`&` e `*`)

Fonte: [07a_entrada_saida_formatada_printf_scanf_e_enderecos.md](./07a_entrada_saida_formatada_printf_scanf_e_enderecos.md)

Ordem recomendada: resolver por sequência, do 12 ao 21.

### Exercício 12 - `printf` básico sem input

Objetivo: consolidar impressão formatada sem leitura de dados.

Cria um programa que declara `int`, `double`, `char` e `char nome[]` e imprime os 4 valores com os especificadores corretos.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Escolhe valores simples para cada variável (`int`, `double`, `char`, `string`).
2. Declara as variáveis com nomes claros.
3. Escreve uma linha de `printf` para cada tipo, usando `%d`, `%.2f`, `%c` e `%s`.
4. Compila e verifica se o output aparece na ordem esperada.
5. Ajusta os textos de apresentação para ficarem legíveis.

> Resolução:

```c
#include <stdio.h>

int main() {
    // Cada variável usa um tipo diferente para treinar os especificadores do printf.
    int idade = 16;
    double altura = 1.72;
    char turma = 'A';
    char nome[] = "Ana";

    // Cada printf usa o especificador adequado ao tipo da variável.
    printf("Idade: %d\n", idade);
    printf("Altura: %.2f\n", altura);
    printf("Turma: %c\n", turma);
    printf("Nome: %s\n", nome);

    return 0;
}
```

### Exercício 13 - Percentagens e casas decimais no `printf`

Objetivo: praticar formatação de números reais e impressão do símbolo `%`.

Cria um programa que apresenta um mini estado de bateria com nome do dispositivo, carga atual e meta de carregamento.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Declara variáveis para nome do dispositivo, carga atual e meta (em percentagem).
2. Atribui valores de teste realistas às variáveis.
3. Imprime o nome com `%s` e as percentagens com precisão fixa (por exemplo, 1 casa decimal).
4. Mostra o símbolo de percentagem corretamente usando `%%`.
5. Revê o output final para confirmar legibilidade e consistência das casas decimais.

> Resolução:

```c
#include <stdio.h>

int main() {
    // Valores fixos de teste para não ser necessário ler input neste exercício.
    char dispositivo[] = "Telemovel";
    double carga_atual = 63.5;
    double meta_carregamento = 90.0;

    // O símbolo %% imprime uma percentagem literal no ecrã.
    printf("Dispositivo: %s\n", dispositivo);
    printf("Carga atual: %.1f%%\n", carga_atual);
    printf("Meta de carregamento: %.1f%%\n", meta_carregamento);

    return 0;
}
```

### Exercício 14 - Leitura de um inteiro

Objetivo: ler e validar um valor inteiro com segurança.

Lê um `int` com `scanf`, valida o retorno e imprime o valor lido apenas quando a leitura for válida.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Declara uma variável `int` para guardar o valor.
2. Pede o número ao utilizador com um `printf` curto.
3. Usa `scanf` e guarda o valor devolvido (número de campos lidos).
4. Se o retorno for `1`, imprime o número lido.
5. Se o retorno for diferente de `1`, mostra mensagem de erro clara.

> Resolução:

```c
#include <stdio.h>

int main() {
    int numero;
    int lidos; // Guarda quantos valores o scanf conseguiu ler corretamente.

    printf("Escreve um numero inteiro: ");
    lidos = scanf("%d", &numero);

    // Se scanf devolver 1, significa que leu exatamente um inteiro.
    if (lidos == 1) {
        printf("Numero lido: %d\n", numero);
    } else {
        printf("Erro: valor invalido.\n");
    }

    return 0;
}
```

### Exercício 15 - Leitura de `double`

Objetivo: usar formato correto para leitura e impressão de `double`.

Lê um `double` com `scanf("%lf", ...)`, valida a leitura e imprime o resultado com 3 casas decimais.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Declara uma variável `double`.
2. Mostra uma mensagem a pedir um valor decimal.
3. Lê com `scanf("%lf", &variavel)` e verifica o retorno.
4. Em caso válido, imprime com `%.3f`.
5. Em caso inválido, apresenta erro sem continuar cálculos.

> Resolução:

```c
#include <stdio.h>

int main() {
    double valor;
    int lidos; // Permite confirmar se a leitura foi bem-sucedida.

    printf("Escreve um valor decimal: ");
    lidos = scanf("%lf", &valor);

    // Para ler double com scanf usa-se %lf.
    if (lidos == 1) {
        printf("Valor lido: %.3f\n", valor);
    } else {
        printf("Erro: valor invalido.\n");
    }

    return 0;
}
```

### Exercício 16 - Valor e endereço

Objetivo: distinguir valor armazenado de endereço em memória.

Lê um inteiro e imprime o valor (`%d`) e o endereço (`%p`, com cast para `(void *)`).

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Declara um `int` e lê o valor com `scanf`.
2. Verifica se a leitura foi bem-sucedida.
3. Imprime o valor com `%d`.
4. Imprime o endereço com `%p`, convertendo para `(void *)`.
5. Compara visualmente valor e endereço para reforçar a diferença.

> Resolução:

```c
#include <stdio.h>

int main() {
    int numero;
    int lidos;

    printf("Escreve um numero inteiro: ");
    lidos = scanf("%d", &numero);

    if (lidos == 1) {
        // O valor é o conteúdo guardado na variável.
        printf("Valor: %d\n", numero);
        // O endereço indica onde a variável está guardada na memória.
        printf("Endereco: %p\n", (void *)&numero);
    } else {
        printf("Erro: valor invalido.\n");
    }

    return 0;
}
```

### Exercício 17 - Dois inteiros na mesma linha

Objetivo: ler múltiplos campos numa única chamada de `scanf`.

Lê `a` e `b` na mesma linha com `scanf("%d %d", &a, &b)` e valida se foram lidos os 2 valores.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Declara duas variáveis `int` (`a` e `b`).
2. Mostra instrução para o utilizador inserir os dois valores na mesma linha.
3. Faz a leitura numa única chamada `scanf`.
4. Verifica se o retorno é `2`.
5. Se válido, imprime os dois valores; se inválido, mostra erro.

> Resolução:

```c
#include <stdio.h>

int main() {
    int a, b;
    int lidos;

    printf("Escreve dois numeros inteiros: ");
    // A mesma chamada scanf pode ler mais do que um valor.
    lidos = scanf("%d %d", &a, &b);

    // Neste caso, o valor esperado é 2 porque queremos ler dois inteiros.
    if (lidos == 2) {
        printf("Primeiro numero: %d\n", a);
        printf("Segundo numero: %d\n", b);
    } else {
        printf("Erro: tens de escrever dois numeros inteiros.\n");
    }

    return 0;
}
```

### Exercício 18 - Leitura de `char` após número

Objetivo: evitar erro comum de leitura de `char` após `int`.

Lê primeiro um número e depois uma opção (`A`, `B` ou `C`), usando `" %c"` para ignorar whitespace pendente.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Declara um `int` e um `char`.
2. Lê o número e valida retorno.
3. Lê a opção com `scanf(" %c", &opcao)`.
4. Confirma se a opção está no conjunto esperado (`A`, `B`, `C`).
5. Imprime resumo final com número e opção escolhida.

> Resolução:

```c
#include <stdio.h>

int main() {
    int numero;
    char opcao;

    printf("Escreve um numero: ");
    // Primeiro validamos o número, porque o programa depende dele.
    if (scanf("%d", &numero) != 1) {
        printf("Erro: numero invalido.\n");
        return 1;
    }

    printf("Escolhe uma opcao (A, B ou C): ");
    // O espaço antes de %c ignora ENTERs ou espaços deixados no input.
    if (scanf(" %c", &opcao) != 1) {
        printf("Erro: opcao invalida.\n");
        return 1;
    }

    // Só aceitamos as opções definidas no enunciado.
    if (opcao == 'A' || opcao == 'B' || opcao == 'C') {
        printf("Numero: %d\n", numero);
        printf("Opcao escolhida: %c\n", opcao);
    } else {
        printf("Erro: a opcao deve ser A, B ou C.\n");
    }

    return 0;
}
```

### Exercício 19 - Palavra com limite de tamanho

Objetivo: prevenir overflow em leitura de string com `scanf`.

Lê uma palavra para `char codigo[20]` usando limite no especificador (`%19s`) e imprime o resultado.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Declara o array `char codigo[20]`.
2. Pede ao utilizador um código sem espaços.
3. Lê com `scanf("%19s", codigo)`.
4. Verifica se a leitura retornou `1`.
5. Imprime o valor lido e testa com palavras curtas e longas.

> Resolução:

```c
#include <stdio.h>

int main() {
    char codigo[20];

    printf("Escreve um codigo sem espacos: ");

    // %19s impede que sejam guardados mais de 19 caracteres no array.
    // O último espaço fica reservado para o caractere final '\0'.
    if (scanf("%19s", codigo) == 1) {
        printf("Codigo lido: %s\n", codigo);
    } else {
        printf("Erro: nao foi possivel ler o codigo.\n");
    }

    return 0;
}
```

### Exercício 20 - Frase completa com `fgets`

Objetivo: ler linha completa com espaços e limpar newline final.

Lê uma frase para `char frase[80]` com `fgets`, remove `\n` final (quando existir) e imprime o texto limpo.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Declara `char frase[80]`.
2. Pede uma frase completa ao utilizador.
3. Lê com `fgets(frase, sizeof(frase), stdin)`.
4. Procura `\n` no fim e substitui por `\0` quando necessário.
5. Imprime a frase final entre delimitadores visuais para confirmar limpeza.

> Resolução:

```c
#include <stdio.h>

int main() {
    char frase[80];
    int i = 0; // Índice usado para percorrer a string caractere a caractere.

    printf("Escreve uma frase: ");

    // fgets lê a linha completa, incluindo espaços.
    if (fgets(frase, sizeof(frase), stdin) != NULL) {
        while (frase[i] != '\0') {
            // Se encontrarmos o ENTER final, substituímos por fim de string.
            if (frase[i] == '\n') {
                frase[i] = '\0';
            }
            i++;
        }

        printf("Frase: [%s]\n", frase);
    } else {
        printf("Erro: nao foi possivel ler a frase.\n");
    }

    return 0;
}
```

### Exercício 21 - Mini ficha (integração)

Objetivo: integrar leitura e apresentação de vários tipos no mesmo programa.

Cria uma mini ficha de aluno que lê: número (`int`), média (`double`), turma (`char`) e nome completo (`fgets`).

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Declara todas as variáveis necessárias com tipos corretos.
2. Lê número, média e turma com `scanf`, validando cada retorno.
3. Garante limpeza de input antes de ler o nome completo.
4. Lê o nome com `fgets` e remove `\n` final se existir.
5. Imprime um resumo final alinhado, claro e consistente.

> Resolução:

```c
#include <stdio.h>

int main() {
    int numero;
    double media;
    char turma;
    char nome[80];
    int i = 0;

    // Cada leitura com scanf é validada antes de continuar.
    printf("Numero do aluno: ");
    if (scanf("%d", &numero) != 1) {
        printf("Erro: numero invalido.\n");
        return 1;
    }

    printf("Media: ");
    if (scanf("%lf", &media) != 1) {
        printf("Erro: media invalida.\n");
        return 1;
    }

    printf("Turma: ");
    if (scanf(" %c", &turma) != 1) {
        printf("Erro: turma invalida.\n");
        return 1;
    }

    getchar(); // Limpa o '\n' deixado pelo scanf anterior

    printf("Nome completo: ");
    // fgets é usado para permitir nomes com espaços.
    if (fgets(nome, sizeof(nome), stdin) == NULL) {
        printf("Erro: nome invalido.\n");
        return 1;
    }

    // Remove o ENTER final, caso exista.
    while (nome[i] != '\0') {
        if (nome[i] == '\n') {
            nome[i] = '\0';
        }
        i++;
    }

    printf("\nResumo do aluno\n");
    printf("%-15s %d\n", "Numero:", numero);
    printf("%-15s %.2f\n", "Media:", media);
    printf("%-15s %c\n", "Turma:", turma);
    printf("%-15s %s\n", "Nome:", nome);

    return 0;
}
```

---

<a id="exercicios-08"></a>

## 08 · Operadores em C

Fonte: [08_operadores_em_c.md](./08_operadores_em_c.md)

### Exercício 22 - Aritmética básica

Objetivo: praticar aritmética básica aplicando os conceitos de operadores em C.

Escreve programa que lê dois inteiros e mostra soma, diferença, produto, quociente e resto.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

> Resolução:

```c
#include <stdio.h>

int main() {
    int a, b;

    printf("Escreve dois numeros inteiros: ");
    // Validamos se foram realmente lidos dois inteiros.
    if (scanf("%d %d", &a, &b) != 2) {
        printf("Erro: valores invalidos.\n");
        return 1;
    }

    // Operações aritméticas básicas entre os dois valores.
    printf("Soma: %d\n", a + b);
    printf("Diferenca: %d\n", a - b);
    printf("Produto: %d\n", a * b);

    // Divisão e resto só são possíveis se o divisor não for zero.
    if (b != 0) {
        printf("Quociente: %d\n", a / b);
        printf("Resto: %d\n", a % b);
    } else {
        printf("Nao e possivel dividir por zero.\n");
    }

    return 0;
}
```

### Exercício 23 - Divisão inteira vs real

Objetivo: praticar divisão inteira vs real aplicando os conceitos de operadores em C.

Demonstra com 8 exemplos a diferença entre divisão inteira e divisão real.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

> Resolução:

```c
#include <stdio.h>

int main() {
    // Cada par de inteiros permite comparar divisão inteira e real.
    int a1 = 5, b1 = 2;
    int a2 = 7, b2 = 3;
    int a3 = 10, b3 = 4;
    int a4 = 9, b4 = 2;

    printf("Divisao inteira:\n");
    printf("%d / %d = %d\n", a1, b1, a1 / b1);
    printf("%d / %d = %d\n", a2, b2, a2 / b2);
    printf("%d / %d = %d\n", a3, b3, a3 / b3);
    printf("%d / %d = %d\n", a4, b4, a4 / b4);

    printf("\nDivisao real:\n");
    // O cast para double força a divisão a produzir casas decimais.
    printf("%d / %d = %.2f\n", a1, b1, (double)a1 / b1);
    printf("%d / %d = %.2f\n", a2, b2, (double)a2 / b2);
    printf("%d / %d = %.2f\n", a3, b3, (double)a3 / b3);
    printf("%d / %d = %.2f\n", a4, b4, (double)a4 / b4);

    return 0;
}
```

### Exercício 24 - Atribuição composta

Objetivo: praticar atribuição composta aplicando os conceitos de operadores em C.

Reescreve 10 atribuições simples usando operadores compostos.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

> Resolução:

```c
#include <stdio.h>

int main() {
    // Valores iniciais simples para observar o efeito das atribuições compostas.
    int a = 10;
    int b = 20;
    int c = 30;
    int d = 40;
    int e = 50;

    // Cada operador composto altera a própria variável.
    a += 5;  // a = a + 5
    b -= 3;  // b = b - 3
    c *= 2;  // c = c * 2
    d /= 4;  // d = d / 4
    e %= 6;  // e = e % 6

    a += 10; // a = a + 10
    b -= 7;  // b = b - 7
    c *= 3;  // c = c * 3
    d /= 2;  // d = d / 2
    e %= 2;  // e = e % 2

    printf("a = %d\n", a);
    printf("b = %d\n", b);
    printf("c = %d\n", c);
    printf("d = %d\n", d);
    printf("e = %d\n", e);

    return 0;
}
```

### Exercício 25 - Comparações

Objetivo: praticar comparações aplicando os conceitos de operadores em C.

Para 12 pares de valores, imprime resultados de todos os operadores relacionais.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 26 - Lógica booleana

Objetivo: praticar lógica booleana aplicando os conceitos de operadores em C.

Implementa validador: idade >= 18 e nota >= 10.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 27 - Intervalos

Objetivo: praticar intervalos aplicando os conceitos de operadores em C.

Verifica se número está no intervalo fechado [1, 100].

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

> Resolução:

```c
#include <stdio.h>

int main() {
    int numero;

    printf("Escreve um numero: ");
    // Antes de testar o intervalo, confirmamos se foi lido um inteiro.
    if (scanf("%d", &numero) != 1) {
        printf("Erro: numero invalido.\n");
        return 1;
    }

    // O intervalo fechado inclui os limites 1 e 100.
    if (numero >= 1 && numero <= 100) {
        printf("O numero esta no intervalo [1, 100].\n");
    } else {
        printf("O numero esta fora do intervalo [1, 100].\n");
    }

    return 0;
}
```

### Exercício 28 - Incremento

Objetivo: praticar incremento aplicando os conceitos de operadores em C.

Cria programa com contador e demonstra pré/pós incremento.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

> Resolução:

```c
#include <stdio.h>

int main() {
    int contador = 5;
    int resultado;

    printf("Valor inicial: %d\n", contador);

    // Pós-incremento: primeiro usa o valor, depois incrementa.
    resultado = contador++;
    printf("Pos-incremento: resultado = %d, contador = %d\n", resultado, contador);

    // Pré-incremento: primeiro incrementa, depois usa o novo valor.
    resultado = ++contador;
    printf("Pre-incremento: resultado = %d, contador = %d\n", resultado, contador);

    return 0;
}
```

### Exercício 29 - Precedência

Objetivo: praticar precedência aplicando os conceitos de operadores em C.

Calcula e compara resultados de 10 expressões com e sem parênteses.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

> Resolução:

```c
#include <stdio.h>

int main() {
    // Os pares de expressões mostram como os parênteses podem mudar o resultado.
    printf("1) 2 + 3 * 4 = %d\n", 2 + 3 * 4);
    printf("   (2 + 3) * 4 = %d\n", (2 + 3) * 4);

    printf("2) 10 - 6 / 2 = %d\n", 10 - 6 / 2);
    printf("   (10 - 6) / 2 = %d\n", (10 - 6) / 2);

    printf("3) 8 + 2 > 5 = %d\n", 8 + 2 > 5);
    printf("   8 + (2 > 5) = %d\n", 8 + (2 > 5));

    printf("4) 1 || 0 && 0 = %d\n", 1 || 0 && 0);
    printf("   (1 || 0) && 0 = %d\n", (1 || 0) && 0);

    printf("5) 20 / 5 * 2 = %d\n", 20 / 5 * 2);
    printf("   20 / (5 * 2) = %d\n", 20 / (5 * 2));

    return 0;
}
```

### Exercício 30 - Refatoração

Objetivo: praticar refatoração aplicando os conceitos de operadores em C.

Recebes 6 condições complexas; reescreve em forma mais legível.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 31 - Mini calculadora

Objetivo: praticar mini calculadora aplicando os conceitos de operadores em C.

Implementa mini calculadora para `+`, `-`, `*`, `/`, `%`.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

> Resolução:

```c
#include <stdio.h>

int main() {
    int a, b;
    char operador;

    printf("Escreve uma operacao (ex.: 10 + 2): ");
    // Lê operando, operador e segundo operando na mesma linha.
    if (scanf("%d %c %d", &a, &operador, &b) != 3) {
        printf("Erro: operacao invalida.\n");
        return 1;
    }

    // Cada ramo trata um operador possível.
    if (operador == '+') {
        printf("Resultado: %d\n", a + b);
    } else if (operador == '-') {
        printf("Resultado: %d\n", a - b);
    } else if (operador == '*') {
        printf("Resultado: %d\n", a * b);
    } else if (operador == '/') {
        // Não se pode dividir por zero.
        if (b != 0) {
            printf("Resultado: %d\n", a / b);
        } else {
            printf("Erro: divisao por zero.\n");
        }
    } else if (operador == '%') {
        // O operador % também não pode ter divisor zero.
        if (b != 0) {
            printf("Resultado: %d\n", a % b);
        } else {
            printf("Erro: resto por zero.\n");
        }
    } else {
        printf("Erro: operador desconhecido.\n");
    }

    return 0;
}
```

### Exercício 32 - Diagnóstico

Objetivo: identificar problemas, explicar a causa e aplicar uma correção tecnicamente correta.

Encontra e corrige erros de operadores num código fornecido pelo professor.

Requisitos:

- Identifica primeiro o comportamento errado ou o erro produzido.
- Explica a causa antes de apresentar a correção.
- Corrige apenas o necessário para resolver o problema indicado.
- Confirma a solução com compilação, execução ou análise manual adequada.

Passo a passo:

1. Reproduz ou lê atentamente o erro apresentado.
2. Localiza a linha ou bloco responsável pelo problema.
3. Explica a causa usando os conceitos de C envolvidos.
4. Aplica a correção mínima necessária.
5. Volta a testar ou reler o código para confirmar que o problema ficou resolvido.

> Resolução:

Exemplo de correções comuns:

```c
#include <stdio.h>

int main() {
    int idade = 18;
    int nota = 12;
    int total = 7;
    int quantidade = 2;
    double media;

    // Correto: usa == para comparar.
    if (idade == 18) {
        printf("Idade igual a 18\n");
    }

    // Correto: usa && para exigir as duas condições.
    if (idade >= 18 && nota >= 10) {
        printf("Aluno valido\n");
    }

    // Correto: faz cast para evitar divisao inteira.
    media = (double)total / quantidade;
    printf("Media: %.2f\n", media);

    // Correto: usa parenteses para deixar a intencao clara.
    if ((nota >= 10) && (nota <= 20)) {
        printf("Nota dentro do intervalo\n");
    }

    return 0;
}
```

### Exercício 33 - Reflexão

Objetivo: consolidar os conceitos de operadores em C através de uma explicação escrita e justificada.

Explica por que compreender operadores evita muitos bugs lógicos.

Requisitos:

- Não escrevas um programa completo, exceto se precisares de pequenos exemplos para justificar uma ideia.
- A resposta deve usar linguagem técnica correta e frases claras.
- Justifica cada escolha com base no problema e não apenas no nome do conceito.
- Inclui pelo menos um exemplo ou situação prática quando isso ajudar a explicação.

Passo a passo:

1. Lê a situação proposta e identifica os conceitos principais envolvidos.
2. Organiza a resposta em pontos curtos ou pequenos parágrafos.
3. Justifica cada escolha com base no tipo de problema apresentado.
4. Acrescenta um exemplo simples quando isso tornar a explicação mais clara.
5. Revê a resposta para garantir que não ficou vaga ou apenas decorada.

---

<a id="exercicios-09"></a>

## 09 · Estruturas de Controlo em C

Fonte: [09_estruturas_de_controlo_em_c.md](./09_estruturas_de_controlo_em_c.md)

### Exercício 34 - Classificação

Objetivo: praticar decisões encadeadas com `if`, `else if` e `else`.

Cria um programa que lê a nota final de um aluno, entre 0 e 20, e apresenta uma classificação textual em quatro níveis.

Usa os seguintes níveis:

- `Insuficiente`: nota menor que 10
- `Suficiente`: nota entre 10 e 13
- `Bom`: nota entre 14 e 17
- `Muito Bom`: nota entre 18 e 20

Requisitos:

- O programa deve pedir a nota ao utilizador.
- A classificação deve ser feita com uma estrutura `if/else if/else`.
- Assume, nesta fase, que o utilizador introduz uma nota válida entre 0 e 20.
- O output deve mostrar a nota lida e a respetiva classificação.

Passo a passo:

1. Declara uma variável para guardar a nota.
2. Lê a nota introduzida pelo utilizador.
3. Identifica primeiro os intervalos de classificação em papel.
4. Implementa os testes do intervalo mais baixo para o mais alto, ou ao contrário, mas sem sobreposições.
5. Mostra uma mensagem final clara com a classificação obtida.

> Resolução:

```c
#include <stdio.h>

int main() {
    int nota;

    printf("Escreve a nota final (0 a 20): ");
    scanf("%d", &nota);

    // Testamos os intervalos por ordem crescente.
    if (nota < 10) {
        printf("Nota: %d - Classificacao: Insuficiente\n", nota);
    } else if (nota <= 13) {
        // Aqui já sabemos que a nota é pelo menos 10.
        printf("Nota: %d - Classificacao: Suficiente\n", nota);
    } else if (nota <= 17) {
        // Aqui já sabemos que a nota é pelo menos 14.
        printf("Nota: %d - Classificacao: Bom\n", nota);
    } else {
        // Como assumimos nota válida, resta o intervalo 18 a 20.
        printf("Nota: %d - Classificacao: Muito Bom\n", nota);
    }

    return 0;
}
```

### Exercício 35 - Menu

Objetivo: usar `switch` para escolher uma operação a partir de uma opção do utilizador.

Cria uma mini calculadora com menu para quatro operações matemáticas: soma, subtração, multiplicação e divisão.

O programa deve apresentar um menu semelhante a:

- `1` - Somar
- `2` - Subtrair
- `3` - Multiplicar
- `4` - Dividir

Requisitos:

- O utilizador deve escolher a operação através de um número.
- O programa deve ler dois valores numéricos.
- A escolha da operação deve ser feita com `switch`.
- Deve existir um caso `default` para opções inválidas.
- Na divisão, não permitas divisão por zero.

Passo a passo:

1. Mostra o menu antes de pedir a opção.
2. Lê a opção escolhida.
3. Lê os dois operandos necessários para o cálculo.
4. Cria um `switch` com um `case` para cada operação.
5. Trata a opção inválida no `default` e a divisão por zero no caso da divisão.

> Resolução:

```c
#include <stdio.h>

int main() {
    int opcao;
    double num1, num2, resultado;

    // Mostra o menu
    printf("Escolhe a operação:\n");
    printf("1 - Somar\n");
    printf("2 - Subtrair\n");
    printf("3 - Multiplicar\n");
    printf("4 - Dividir\n");
    printf("Opção: ");
    scanf("%d", &opcao);

    // Lê os operandos
    printf("Escreve o primeiro número: ");
    scanf("%lf", &num1);
    printf("Escreve o segundo número: ");
    scanf("%lf", &num2);

    // Processa a opção escolhida
    switch (opcao) {
        case 1:
            resultado = num1 + num2;
            printf("Resultado: %.2f\n", resultado);
            break;
        case 2:
            resultado = num1 - num2;
            printf("Resultado: %.2f\n", resultado);
            break;
        case 3:
            resultado = num1 * num2;
            printf("Resultado: %.2f\n", resultado);
            break;
        case 4:
            if (num2 != 0) {
                resultado = num1 / num2;
                printf("Resultado: %.2f\n", resultado);
            } else {
                printf("Erro: Divisão por zero não é permitida.\n");
            }
            break;
        default:
            printf("Opção inválida. Por favor, escolhe entre 1 e 4.\n");
            break;
    }

    return 0;
}
```

### Exercício 36 - Contagem

Objetivo: controlar uma repetição com `while` e aplicar regras simples dentro do ciclo.

Cria um programa que percorre os números de 1 a 50 e imprime apenas os que respeitam uma regra escolhida pelo utilizador.

Antes da contagem, o programa deve perguntar que tipo de números mostrar:

- `1` - todos os números
- `2` - apenas números pares
- `3` - apenas números ímpares
- `4` - apenas múltiplos de 5

Requisitos:

- A contagem principal deve ser feita com `while`.
- O contador deve começar em 1 e terminar em 50.
- O programa deve usar condições dentro do ciclo para decidir se imprime cada número.
- Se a opção for inválida, o programa deve mostrar uma mensagem de erro.

Passo a passo:

1. Declara uma variável para a opção e outra para o contador.
2. Mostra o menu de filtros e lê a escolha do utilizador.
3. Inicializa o contador com o primeiro valor da contagem.
4. Dentro do `while`, verifica se o número atual cumpre a regra escolhida.
5. No fim de cada repetição, atualiza sempre o contador para evitar um ciclo infinito.

> Resolução:

```c
#include <stdio.h>

int main() {
    int opcao;
    int contador = 1;

    // Mostra o menu de opções
    printf("Escolhe o tipo de números a mostrar:\n");
    printf("1 - Todos os números\n");
    printf("2 - Apenas números pares\n");
    printf("3 - Apenas números ímpares\n");
    printf("4 - Apenas múltiplos de 5\n");
    printf("Opção: ");
    scanf("%d", &opcao);

    // Verifica se a opção é válida antes de iniciar a contagem
    if (opcao < 1 || opcao > 4) {
        printf("Opção inválida. Por favor, escolhe entre 1 e 4.\n");
        return 1;
    }

    // Contagem de 1 a 50
    while (contador <= 50) {
        if (opcao == 1) {
            // Mostra todos os números
            printf("%d ", contador);
        } else if (opcao == 2 && contador % 2 == 0) {
            // Mostra apenas números pares
            printf("%d ", contador);
        } else if (opcao == 3 && contador % 2 != 0) {
            // Mostra apenas números ímpares
            printf("%d ", contador);
        } else if (opcao == 4 && contador % 5 == 0) {
            // Mostra apenas múltiplos de 5
            printf("%d ", contador);
        }
        contador++; // Atualiza o contador para evitar ciclo infinito
    }
    printf("\n"); // Nova linha após a contagem

    return 0;
}
```

### Exercício 37 - Soma acumulada

Objetivo: usar um ciclo com sentinela e acumular valores ao longo da execução.

Cria um programa que lê números inteiros introduzidos pelo utilizador até ser introduzido o valor `0`.

O valor `0` serve apenas para terminar a leitura e não deve entrar na soma.

Requisitos:

- O programa deve manter uma variável acumuladora para a soma.
- O programa deve contar quantos números foram efetivamente somados.
- No final, deve mostrar a soma total e a quantidade de números introduzidos antes do `0`.
- A leitura deve continuar enquanto o valor introduzido for diferente de `0`.

Passo a passo:

1. Cria uma variável para o número lido.
2. Cria uma variável para a soma acumulada, iniciada a zero.
3. Cria uma variável para contar quantos números válidos foram introduzidos.
4. Lê números repetidamente até surgir o valor sentinela `0`.
5. Depois do ciclo, apresenta o total acumulado e o número de entradas usadas.

> Resolução:

```c
#include <stdio.h>

int main() {
    int numero;
    int soma = 0;
    int contador = 0;

    printf("Escreve números inteiros (0 para terminar):\n");

    while (1) {
        scanf("%d", &numero);
        if (numero == 0) {
            break; // Termina o ciclo quando o valor é 0
        }
        soma += numero; // Acumula a soma
        contador++; // Conta quantos números foram introduzidos
    }

    printf("Soma total: %d\n", soma);
    printf("Quantidade de números introduzidos: %d\n", contador);

    return 0;
}
```

### Exercício 38 - Tabuada

Objetivo: usar `for` quando o número de repetições é conhecido antecipadamente.

Cria um programa que lê um número inteiro e imprime a sua tabuada de 1 a 10.

Exemplo de comportamento esperado, sem precisares de copiar este formato exatamente:

`7 x 1 = 7`

`7 x 2 = 14`

Requisitos:

- O programa deve pedir ao utilizador o número da tabuada.
- A repetição deve ser feita com `for`.
- A variável de controlo deve representar o multiplicador.
- O output deve ser organizado e fácil de ler.

Passo a passo:

1. Declara uma variável para o número escolhido pelo utilizador.
2. Lê esse número.
3. Cria um ciclo `for` que percorra os multiplicadores de 1 a 10.
4. Em cada iteração, calcula o produto entre o número e o multiplicador.
5. Imprime cada linha da tabuada no formato mais legível possível.

> Resolução:

```c

#include <stdio.h>

int main() {
    int numero;

    printf("Escreve um número para ver a tabuada: ");
    scanf("%d", &numero);

    printf("Tabuada de %d:\n", numero);
    for (int i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", numero, i, numero * i);
    }

    return 0;
}
```

### Exercício 39 - Adivinhação

Objetivo: combinar repetição, condições e controlo de tentativas num pequeno jogo.

Cria um jogo em que o utilizador tenta adivinhar um número secreto definido no programa.

O número secreto pode estar fixo no código, por exemplo entre 1 e 100. O jogador deve ter um número máximo de tentativas.

Requisitos:

- Define um número secreto numa variável.
- Define um limite máximo de tentativas.
- A cada tentativa, o utilizador introduz um palpite.
- O programa deve indicar se o palpite é demasiado baixo, demasiado alto ou correto.
- O jogo termina quando o utilizador acerta ou quando esgota as tentativas.
- No final, mostra uma mensagem de vitória ou derrota.

Passo a passo:

1. Decide o valor do número secreto e o número máximo de tentativas.
2. Cria variáveis para o palpite, o número de tentativas e o estado do jogo.
3. Enquanto ainda houver tentativas e o jogador não tiver acertado, pede um novo palpite.
4. Compara o palpite com o número secreto usando `if/else`.
5. Atualiza a contagem de tentativas e apresenta o resultado final quando o ciclo terminar.

> Nota: Se quiseres usar um número secreto aleatório, podes usar a função `rand()` da biblioteca `<stdlib.h>`, mas isso é opcional para este exercício.

> Resolução com rand():

```c

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int numero_secreto, palpite;
    int tentativas = 0;
    const int MAX_TENTATIVAS = 5;

    // Inicializa o gerador de números aleatórios
    srand(time(NULL)); // Usa o tempo atual como semente para garantir números diferentes a cada execução
    numero_secreto = rand() % 100 + 1; // Número entre 1 e 100

    printf("Bem-vindo ao jogo de adivinhação!\n");
    printf("Tenta adivinhar o número secreto entre 1 e 100.\n");
    printf("Tens %d tentativas.\n", MAX_TENTATIVAS);

    while (tentativas < MAX_TENTATIVAS) {
        printf("Tentativa %d: ", tentativas + 1);
        scanf("%d", &palpite);

        if (palpite < numero_secreto) {
            printf("Demasiado baixo!\n");
        } else if (palpite > numero_secreto) {
            printf("Demasiado alto!\n");
        } else {
            printf("Parabéns! Adivinhaste o número secreto!\n");
            return 0; // Termina o programa com vitória
        }
        tentativas++;
    }

    printf("Fim do jogo! O número secreto era: %d\n", numero_secreto);
    return 0; // Termina o programa com derrota
}
```

### Exercício 40 - `break` e `continue`

Objetivo: perceber quando `continue` salta uma iteração e quando `break` termina um ciclo.

Cria um programa que percorre números de 1 até 100, mas com duas regras especiais:

- os múltiplos de 3 não devem ser impressos;
- a contagem deve terminar imediatamente quando chegar a um valor limite escolhido pelo utilizador.

Requisitos:

- O valor limite deve ser lido no início do programa.
- Usa `continue` para saltar os múltiplos de 3.
- Usa `break` para terminar o ciclo quando o limite for atingido.
- O programa deve validar de forma simples se o limite está entre 1 e 100.

Passo a passo:

1. Lê o valor limite.
2. Antes do ciclo, confirma se o limite está dentro do intervalo permitido.
3. Cria um ciclo que percorra os valores de 1 a 100.
4. Dentro do ciclo, verifica primeiro se chegou ao valor limite.
5. Depois, verifica se o número é múltiplo de 3 e decide se deve saltar a impressão.

> Resolução:

```c
#include <stdio.h>

int main() {
    int limite;

    printf("Escreve o valor limite (1 a 100): ");
    scanf("%d", &limite);

    // Valida o limite
    if (limite < 1 || limite > 100) {
        printf("Valor limite inválido. Por favor, escolhe entre 1 e 100.\n");
        return 1;
    }

    printf("Números de 1 a %d, excluindo múltiplos de 3:\n", limite);
    for (int i = 1; i <= 100; i++) {
        if (i == limite) {
            break; // Termina o ciclo quando chega ao limite
        }
        if (i % 3 == 0) {
            continue; // Salta os múltiplos de 3
        }
        printf("%d ", i);
    }
    printf("\n"); // Nova linha após a contagem

    return 0;
}
```

### Exercício 41 - Matriz

Objetivo: praticar ciclos encadeados para percorrer uma matriz.

Cria um programa que guarda valores inteiros numa matriz 4x4 e calcula estatísticas simples sobre os seus elementos.

O programa deve calcular:

- a soma de todos os elementos;
- a quantidade de números pares;
- o maior valor existente na matriz.

Requisitos:

- Usa uma matriz 4x4 de inteiros.
- Podes preencher a matriz com valores fixos no código ou pedir os valores ao utilizador.
- O percurso da matriz deve ser feito com dois ciclos encadeados.
- Não uses 16 instruções separadas para aceder manualmente a cada posição.

Passo a passo:

1. Declara uma matriz 4x4.
2. Decide se vais inicializar a matriz diretamente ou preenchê-la com leitura do utilizador.
3. Cria um ciclo para percorrer as linhas.
4. Dentro dele, cria outro ciclo para percorrer as colunas.
5. Em cada posição, atualiza a soma, verifica se o valor é par e compara com o maior valor encontrado até ao momento.

### Exercício 42 - Validação

Objetivo: repetir a leitura até o utilizador introduzir um valor válido.

Cria um programa que pede uma nota entre 0 e 20 e só aceita o valor quando este estiver dentro do intervalo permitido.

Enquanto a nota for inválida, o programa deve mostrar uma mensagem de erro e voltar a pedir a nota.

Requisitos:

- A nota deve ser lida como valor numérico.
- O intervalo válido é de 0 a 20, inclusive.
- A repetição deve continuar enquanto a nota estiver fora do intervalo.
- Quando a nota for válida, o programa deve mostrar uma mensagem de confirmação.

Passo a passo:

1. Declara uma variável para guardar a nota.
2. Lê a primeira tentativa do utilizador.
3. Cria uma condição que identifique notas menores que 0 ou maiores que 20.
4. Enquanto a condição indicar erro, mostra uma mensagem e volta a ler.
5. Quando o ciclo terminar, apresenta a nota aceite.

### Exercício 43 - Menu persistente

Objetivo: usar `do while` quando o menu deve aparecer pelo menos uma vez.

Cria um programa com um menu persistente de gestão de notas.

O menu deve ter as seguintes opções:

- `1` - Inserir nota
- `2` - Mostrar última nota inserida
- `3` - Classificar última nota
- `0` - Sair

Requisitos:

- O menu deve aparecer pelo menos uma vez.
- A repetição deve ser feita com `do while`.
- O programa só deve terminar quando o utilizador escolher `0`.
- Se ainda não existir nota inserida, as opções 2 e 3 devem informar o utilizador.
- A opção inválida deve ser tratada com uma mensagem adequada.

Passo a passo:

1. Cria uma variável para a opção do menu.
2. Cria uma variável para guardar a última nota e outra para indicar se já existe nota.
3. Dentro do `do`, mostra o menu e lê a opção.
4. Usa `switch` ou `if/else` para tratar cada opção.
5. Mantém o ciclo ativo enquanto a opção escolhida for diferente de `0`.

### Exercício 44 - Simulação de saldo

Objetivo: integrar menu, validação, repetição e decisões num programa mais próximo de um caso real.

Cria uma simulação simples de saldo bancário. O utilizador começa com um saldo inicial e pode escolher operações através de um menu.

O menu deve incluir:

- `1` - Consultar saldo
- `2` - Depositar dinheiro
- `3` - Levantar dinheiro
- `0` - Terminar

Requisitos:

- O saldo inicial deve ser pedido ao utilizador.
- O menu deve repetir até o utilizador escolher sair.
- Um depósito só deve ser aceite se o valor for positivo.
- Um levantamento só deve ser aceite se o valor for positivo e não ultrapassar o saldo disponível.
- O programa deve mostrar mensagens claras para operações aceites e recusadas.

Passo a passo:

1. Lê e guarda o saldo inicial.
2. Cria um ciclo de menu que continue até à opção `0`.
3. Para cada opção, decide que dados adicionais precisas de pedir.
4. Valida os valores antes de alterar o saldo.
5. Atualiza o saldo apenas quando a operação for válida.

### Exercício 45 - Reflexão

Objetivo: escolher a estrutura de repetição adequada a diferentes problemas.

Para cada situação abaixo, indica se usarias `for`, `while` ou `do while` e justifica a escolha em duas ou três frases:

1. Imprimir os números de 1 a 100.
2. Pedir uma palavra-passe até estar correta.
3. Mostrar um menu que deve aparecer pelo menos uma vez.
4. Ler temperaturas até ser introduzido o valor `-999`.
5. Percorrer todas as posições de um array com tamanho conhecido.
6. Repetir uma pergunta enquanto o utilizador responder `S`.

Requisitos:

- Não escrevas código completo.
- Justifica com base no tipo de problema, não apenas no nome da estrutura.
- Refere se o número de repetições é conhecido, desconhecido ou se o ciclo tem de executar pelo menos uma vez.

Passo a passo:

1. Lê cada situação e identifica o que controla a repetição.
2. Decide se sabes antecipadamente o número de repetições.
3. Verifica se a ação precisa de acontecer antes do primeiro teste.
4. Escolhe a estrutura mais adequada.
5. Escreve uma justificação curta e técnica para cada caso.

---

<a id="exercicios-10"></a>

## 10 · Subprogramas: Funções, Variáveis Locais/Globais e Parâmetros

Fonte: [10_subprogramas_funcoes_e_parametros.md](./10_subprogramas_funcoes_e_parametros.md)

### Exercício 46 - Funções básicas

Objetivo: praticar funções básicas aplicando os conceitos de funções, escopo e parâmetros.

Cria funções para somar, subtrair, multiplicar e dividir.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

> Resolução:

```c
#include <stdio.h>
// Função para somar dois números
double somar(double a, double b) {
    return a + b;
}
// Função para subtrair dois números
double subtrair(double a, double b) {
    return a - b;
}
// Função para multiplicar dois números
double multiplicar(double a, double b) {
    return a * b;
}
// Função para dividir dois números, com validação de divisor zero
double dividir(double a, double b) {
    if (b != 0) {
        return a / b;
    } else {
        printf("Erro: divisão por zero não é permitida.\n");
        return 0; // Retorna zero ou outro valor para indicar erro
    }
}

int main() {
    double num1, num2;

    printf("Escreve o primeiro número: ");
    scanf("%lf", &num1);
    printf("Escreve o segundo número: ");
    scanf("%lf", &num2);

    printf("Soma: %.2f\n", somar(num1, num2));
    printf("Subtração: %.2f\n", subtrair(num1, num2));
    printf("Multiplicação: %.2f\n", multiplicar(num1, num2));
    printf("Divisão: %.2f\n", dividir(num1, num2));

    return 0;
}
```

### Exercício 47 - Retorno

Objetivo: praticar retorno aplicando os conceitos de funções, escopo e parâmetros.

Cria função que devolve maior de dois inteiros.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

> Resolução:

```c

#include <stdio.h>

// Função para encontrar o maior de dois inteiros
int maior(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

int main() {
    int num1, num2;

    printf("Escreve o primeiro número inteiro: ");
    scanf("%d", &num1);
    printf("Escreve o segundo número inteiro: ");
    scanf("%d", &num2);

    int resultado = maior(num1, num2);
    printf("O maior número é: %d\n", resultado);

    return 0;
}
```

### Exercício 48 - `void`

Objetivo: praticar `void` aplicando os conceitos de funções, escopo e parâmetros.

Cria procedimento que imprime linha separadora no ecrã.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

> Resolução:

```c
#include <stdio.h>

// Procedimento para imprimir uma linha separadora
void imprimirSeparador() {
    printf("------------------------------\n");
}

int main() {
    printf("Primeira seção do programa\n");
    imprimirSeparador(); // Chama o procedimento para imprimir a linha separadora
    printf("Segunda seção do programa\n");

    return 0;
}
```

### Exercício 49 - Locais e globais

Objetivo: praticar locais e globais aplicando os conceitos de funções, escopo e parâmetros.

Constrói exemplo com uma variável global e duas locais.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

> Resolução:

```c

#include <stdio.h>

// Variável global para contar o número de chamadas
int contadorChamadas = 0;
// Função que incrementa o contador e imprime o valor atual
void contarChamadas() {
    contadorChamadas++; // Incrementa a variável global
    printf("Número de chamadas: %d\n", contadorChamadas);
}

int main() {
    int contadorLocal = 0; // Variável local para contar chamadas dentro do main

    printf("Contador local antes de chamar a função: %d\n", contadorLocal);
    contarChamadas(); // Chama a função que incrementa o contador global
    contarChamadas(); // Chama novamente para mostrar o efeito acumulado
    printf("Contador local depois de chamar a função: %d\n", contadorLocal);

    return 0;
}
```

### Exercício 50 - Passagem por valor

Objetivo: praticar passagem por valor aplicando os conceitos de funções, escopo e parâmetros.

Demonstra, com programa curto, que variável original não é alterada.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

> Resolução:

```c

#include <stdio.h>

// Função que tenta alterar o valor de um inteiro passado por valor
void alterarValor(int x) {
    x = 100; // Tenta alterar o valor de x, mas isso não afeta a variável original
    printf("Valor dentro da função: %d\n", x);
}

int main() {
    int numero = 50; // Variável original
    printf("Valor antes de chamar a função: %d\n", numero);
    alterarValor(numero); // Passa a variável por valor
    printf("Valor depois de chamar a função: %d\n", numero); // O valor original permanece inalterado

    return 0;
}
```

### Exercício 51 - Passagem por ponteiro

Objetivo: praticar passagem por ponteiro aplicando os conceitos de funções, escopo e parâmetros.

Cria função para trocar dois inteiros.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

> Resolução:

```c

#include <stdio.h>

// Função para trocar dois inteiros usando passagem por ponteiro
void trocar(int *a, int *b) {
    int temp = *a; // Guarda o valor de a em temp
    *a = *b; // Atribui o valor de b a a
    *b = temp; // Atribui o valor guardado em temp a b
}

int main() {
    int num1, num2;

    printf("Escreve o primeiro número inteiro: ");
    scanf("%d", &num1);
    printf("Escreve o segundo número inteiro: ");
    scanf("%d", &num2);

    printf("Antes da troca: num1 = %d, num2 = %d\n", num1, num2);
    trocar(&num1, &num2); // Passa os endereços de num1 e num2 para a função
    printf("Depois da troca: num1 = %d, num2 = %d\n", num1, num2); // Os valores foram trocados

    return 0;
}
```

### Exercício 52 - Validação de parâmetros

Objetivo: reforçar validação, segurança e tratamento explícito de casos inválidos.

Cria função de divisão que trate divisor zero.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

> Resolução:

```c
#include <stdio.h>
// Função para dividir dois números, com validação de divisor zero
double dividir(double a, double b) {
    if (b != 0) {
        return a / b;
    } else {
        printf("Erro: divisão por zero não é permitida.\n");
        return 0; // Retorna zero ou outro valor para indicar erro
    }
}

int main() {
    double num1, num2;

    printf("Escreve o primeiro número: ");
    scanf("%lf", &num1);
    printf("Escreve o segundo número: ");
    scanf("%lf", &num2);

    double resultado = dividir(num1, num2);
    if (num2 != 0) { // Verifica se a divisão foi bem-sucedida antes de imprimir
        printf("Resultado da divisão: %.2f\n", resultado);
    }

    return 0;
}
```

### Exercício 53 - Modularização

Objetivo: organizar responsabilidades e tornar a solução mais modular, legível e sustentável.

Separa projeto em `main.c`, `operacoes.c`, `operacoes.h`.

Requisitos:

- Separa responsabilidades em funções, ficheiros ou tipos quando isso fizer sentido.
- Mantém nomes claros para funções, parâmetros e ficheiros.
- Evita duplicação de código e dependências desnecessárias.
- Garante que a solução continua fácil de compilar e testar.

Passo a passo:

1. Identifica as responsabilidades principais da solução.
2. Decide que funções, tipos ou ficheiros devem existir.
3. Define interfaces claras antes de escrever a implementação completa.
4. Implementa cada parte mantendo baixo acoplamento entre componentes.
5. Compila e testa o conjunto para confirmar que a organização funciona.

### Exercício 54 - Contador de chamadas

Objetivo: praticar contador de chamadas aplicando os conceitos de funções, escopo e parâmetros.

Usa variável global para contar quantas vezes função foi chamada.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 55 - Refatoração

Objetivo: praticar refatoração aplicando os conceitos de funções, escopo e parâmetros.

Transforma programa monolítico em pelo menos 5 funções.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 56 - Mini biblioteca

Objetivo: praticar mini biblioteca aplicando os conceitos de funções, escopo e parâmetros.

Cria conjunto de funções para manipular notas de alunos.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 57 - Reflexão

Objetivo: consolidar os conceitos de funções, escopo e parâmetros através de uma explicação escrita e justificada.

Explica quando usar retorno e quando usar parâmetro por ponteiro.

Requisitos:

- Não escrevas um programa completo, exceto se precisares de pequenos exemplos para justificar uma ideia.
- A resposta deve usar linguagem técnica correta e frases claras.
- Justifica cada escolha com base no problema e não apenas no nome do conceito.
- Inclui pelo menos um exemplo ou situação prática quando isso ajudar a explicação.

Passo a passo:

1. Lê a situação proposta e identifica os conceitos principais envolvidos.
2. Organiza a resposta em pontos curtos ou pequenos parágrafos.
3. Justifica cada escolha com base no tipo de problema apresentado.
4. Acrescenta um exemplo simples quando isso tornar a explicação mais clara.
5. Revê a resposta para garantir que não ficou vaga ou apenas decorada.

---

<a id="exercicios-11"></a>

## 11 · Funcionalidades de um Editor de Texto

Fonte: [11_funcionalidades_editor_de_texto.md](./11_funcionalidades_editor_de_texto.md)

### Exercício 58 - Configuração base

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Configura editor com linha, coluna e indentação de 4 espaços.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 59 - Atalhos

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Lista e pratica 12 atalhos úteis para programação C.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 60 - Pesquisa global

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Localiza todas as ocorrências de uma função num projeto com vários ficheiros.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 61 - Substituição segura

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Renomeia variável em projeto sem quebrar outras partes.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 62 - Navegação

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Usa "go to definition" para navegar entre `.h` e `.c`.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 63 - Formatação

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Aplica formatação consistente a um ficheiro propositalmente desorganizado.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 64 - Terminal

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Compila e executa programa apenas com terminal integrado.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 65 - Tarefa automática

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Cria tarefa de build no editor para um projeto C.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 66 - Debug inicial

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Configura breakpoint e observa valor de uma variável por iteração.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 67 - Refatoração assistida

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Extrai bloco de código para função com apoio do editor.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 68 - Produtividade

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Mede tempo de tarefa com e sem atalhos; compara resultados.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 69 - Reflexão

Objetivo: consolidar os conceitos de funcionalidades do editor de texto através de uma explicação escrita e justificada.

Explica como editor bem usado melhora aprendizagem para iniciantes.

Requisitos:

- Não escrevas um programa completo, exceto se precisares de pequenos exemplos para justificar uma ideia.
- A resposta deve usar linguagem técnica correta e frases claras.
- Justifica cada escolha com base no problema e não apenas no nome do conceito.
- Inclui pelo menos um exemplo ou situação prática quando isso ajudar a explicação.

Passo a passo:

1. Lê a situação proposta e identifica os conceitos principais envolvidos.
2. Organiza a resposta em pontos curtos ou pequenos parágrafos.
3. Justifica cada escolha com base no tipo de problema apresentado.
4. Acrescenta um exemplo simples quando isso tornar a explicação mais clara.
5. Revê a resposta para garantir que não ficou vaga ou apenas decorada.

---

<a id="exercicios-12"></a>

## 12 · Estruturas de Dados Estáticas: Strings, Arrays e Matrizes

Fonte: [12_estruturas_estaticas_strings_arrays_matrizes.md](./12_estruturas_estaticas_strings_arrays_matrizes.md)

### Exercício 70 - Vetor básico e ordem inversa

Objetivo: praticar declaração, preenchimento e percurso de um array de inteiros.

Lê 10 inteiros para um vetor e imprime-os na ordem inversa.

Requisitos:

- Usa uma constante para representar o tamanho do vetor.
- Guarda todos os valores num array antes de os imprimir.
- Usa um ciclo para ler os valores e outro ciclo para os imprimir pela ordem inversa.
- Não acedas a posições fora dos limites do array.
- O output deve deixar claro que a segunda listagem está em ordem inversa.

Passo a passo:

1. Define uma constante, por exemplo `TOTAL_NUMEROS`, com valor 10.
2. Declara um array de inteiros com esse tamanho.
3. Lê cada número para a posição correta do array.
4. Percorre o array do último índice até ao primeiro.
5. Testa com valores fáceis de verificar, como `1 2 3 4 5 6 7 8 9 10`.

> Resolução:

```c
#include <stdio.h>

#define TOTAL_NUMEROS 10

int main() {
    int numeros[TOTAL_NUMEROS];

    // Lê os números para o array
    printf("Escreve %d números inteiros:\n", TOTAL_NUMEROS);
    for (int i = 0; i < TOTAL_NUMEROS; i++) {
        scanf("%d", &numeros[i]);
    }

    // Imprime os números na ordem inversa
    printf("Números na ordem inversa:\n");
    for (int i = TOTAL_NUMEROS - 1; i >= 0; i--) {
        printf("%d ", numeros[i]);
    }
    printf("\n");

    return 0;
}
```

### Exercício 71 - Estatísticas

Objetivo: calcular informação simples a partir dos valores guardados num array.

Lê 20 valores inteiros para um vetor e calcula soma, média, máximo e mínimo.

Requisitos:

- Usa uma constante para o tamanho do vetor.
- Guarda os valores num array antes de calcular os resultados.
- Inicializa o máximo e o mínimo com o primeiro elemento do array, não com `0`.
- A média deve poder apresentar casas decimais.
- Mostra soma, média, máximo e mínimo com mensagens claras.

Passo a passo:

1. Lê todos os valores para o array.
2. Começa a soma em `0`.
3. Define máximo e mínimo com o valor da posição `0`.
4. Percorre o array e atualiza soma, máximo e mínimo.
5. Calcula a média com conversão para `double` ou `float`.
6. Testa também com valores negativos para confirmar que máximo e mínimo estão corretos.

### Exercício 72 - Pares e ímpares

Objetivo: praticar condições dentro do percurso de um array.

Lê 12 inteiros para um vetor, conta quantos são pares e quantos são ímpares, e mostra também os valores pares encontrados.

Requisitos:

- Usa o operador `%` para distinguir pares e ímpares.
- Não precisas de criar dois arrays separados; podes contar e mostrar durante o percurso.
- Mostra no final o total de pares e o total de ímpares.
- O programa deve funcionar também se todos os números forem pares ou todos forem ímpares.

Passo a passo:

1. Lê os 12 valores para um array.
2. Cria dois contadores: um para pares e outro para ímpares.
3. Percorre o array.
4. Se o valor for par, aumenta o contador de pares e mostra esse valor.
5. Caso contrário, aumenta o contador de ímpares.
6. Testa com uma lista mista e com uma lista só de números pares.

### Exercício 73 - Array passado para função

Objetivo: praticar passagem de arrays para funções, passando também o tamanho.

Cria uma função `calcular_soma` que receba um array de inteiros e o seu tamanho, devolvendo a soma dos elementos.

Requisitos:

- O programa principal deve ler 8 valores para um array.
- A função deve ter um parâmetro para o array e outro para o tamanho.
- A função não deve pedir valores ao utilizador nem imprimir resultados; apenas calcula e devolve a soma.
- O `main` deve chamar a função e mostrar o resultado.
- Usa nomes de variáveis que deixem claro o papel de cada elemento.

Passo a passo:

1. Escreve o protótipo da função antes do `main`.
2. No `main`, declara e preenche o array.
3. Chama `calcular_soma`.
4. Dentro da função, percorre o array com `for`.
5. Devolve a soma com `return`.
6. Testa com valores cuja soma seja fácil de confirmar.

### Exercício 74 - Pesquisa linear

Objetivo: procurar um valor dentro de um array usando pesquisa linear.

Lê 10 inteiros para um array. Depois lê um valor a pesquisar e indica se esse valor existe no array e em que posição aparece pela primeira vez.

Requisitos:

- Usa uma variável para indicar se o valor foi encontrado.
- Quando encontrares a primeira ocorrência, podes terminar a pesquisa.
- Se o valor não existir, mostra uma mensagem clara.
- A posição apresentada ao utilizador pode ser em formato humano, começando em 1, mas o índice interno continua a começar em 0.

Passo a passo:

1. Lê os valores do array.
2. Lê o valor a procurar.
3. Percorre o array desde a posição `0`.
4. Compara cada elemento com o valor procurado.
5. Guarda o índice quando encontrares o valor.
6. Testa um caso em que o valor existe e outro em que não existe.

> Resolução:

```c
#include <stdio.h>

#define TOTAL_NUMEROS 10

int main() {
    int numeros[TOTAL_NUMEROS];
    int valorProcurado;
    int encontrado = 0; // Variável para indicar se o valor foi encontrado
    int posicaoEncontrada = -1; // Variável para guardar a posição do valor encontrado

    // Lê os números para o array
    printf("Escreve %d números inteiros:\n", TOTAL_NUMEROS);
    for (int i = 0; i < TOTAL_NUMEROS; i++) {
        scanf("%d", &numeros[i]);
    }

    // Lê o valor a procurar
    printf("Escreve o valor a procurar: ");
    scanf("%d", &valorProcurado);

    // Pesquisa linear no array
    for (int i = 0; i < TOTAL_NUMEROS; i++) {
        if (numeros[i] == valorProcurado) {
            encontrado = 1;
            posicaoEncontrada = i; // Guarda a posição do valor encontrado
            break; // Termina a pesquisa após encontrar a primeira ocorrência
        }
    }

    // Mostra o resultado da pesquisa
    if (encontrado) {
        printf("Valor %d encontrado na posição %d.\n", valorProcurado, posicaoEncontrada + 1); // +1 para formato humano
    } else {
        printf("Valor %d não encontrado no array.\n", valorProcurado);
    }

    return 0;
}
```

### Exercício 75 - String com nome completo

Objetivo: praticar leitura segura de strings com espaços.

Lê o nome completo de uma pessoa e mostra quantos caracteres tem, sem contar o Enter final.

Requisitos:

- Usa um array de `char` com tamanho definido por constante.
- Usa `fgets` para permitir nomes com espaços.
- Remove o `\n` final, se existir.
- Usa `strlen` para calcular o comprimento da string.
- Não uses `gets`.

Passo a passo:

1. Inclui as bibliotecas necessárias.
2. Declara uma constante para o tamanho máximo do nome.
3. Lê o nome com `fgets`.
4. Remove o `\n` usando uma técnica segura, como `strcspn`. O `strcspn` retorna o índice do primeiro caractere encontrado que é `\n`, ou o tamanho da string se não encontrar. Substituir esse índice por `\0` remove o `\n`.
5. Calcula o comprimento com `strlen`.
6. Testa com um nome simples e com um nome composto.

> Resolução:

```c
#include <stdio.h>
#include <string.h>

#define MAX_NOME 100
int main() {
    char nome[MAX_NOME];

    printf("Escreve o nome completo: ");
    fgets(nome, MAX_NOME, stdin);

    // Remove o \n final, se existir
    nome[strcspn(nome, "\n")] = '\0';

    int comprimento = strlen(nome);
    printf("O nome tem %d caracteres.\n", comprimento);

    return 0;
}
```

Sem contra os espaços entre nomes:

```c
#include <stdio.h>
#include <string.h>

#define MAX_NOME 100
int main() {
    char nome[MAX_NOME];
    printf("Escreve o nome completo: ");
    fgets(nome, MAX_NOME, stdin);
    // Remove o \n final, se existir
    nome[strcspn(nome, "\n")] = '\0';
    int comprimento = 0;
    for (int i = 0; nome[i] != '\0'; i++) {
        if (nome[i] != ' ') {
            comprimento++;
        }
    }
    printf("O nome tem %d caracteres (sem contar os espaços).\n", comprimento);
    return 0;
}
```

### Exercício 76 - Comparação de strings

Objetivo: comparar o conteúdo de duas strings corretamente.

Lê duas palavras e indica se são iguais.

Requisitos:

- Usa arrays de `char` com tamanho definido por constante.
- Podes ler palavras com `scanf` usando largura máxima, por exemplo `%29s`, ou usar `fgets`.
- Compara as strings com `strcmp`.
- Não compares strings com `==`.
- Mostra mensagens diferentes para strings iguais e diferentes.

Passo a passo:

1. Lê a primeira palavra.
2. Lê a segunda palavra.
3. Usa `strcmp` para comparar as duas strings.
4. Verifica se o resultado da comparação é `0`.
5. Testa com duas palavras iguais e com duas palavras diferentes.

### Exercício 77 - Construção de nome completo

Objetivo: juntar strings respeitando a capacidade dos arrays.

Lê um primeiro nome e um apelido. Depois constrói e mostra o nome completo com um espaço entre eles.

Requisitos:

- Usa arrays de `char` para o primeiro nome, apelido e nome completo.
- Garante que o array do nome completo tem capacidade suficiente.
- Podes usar `strcpy` e `strcat`, desde que controles os tamanhos usados no exercício.
- O nome completo deve incluir exatamente um espaço entre o nome e o apelido.
- Não uses atribuição direta para copiar strings depois da declaração.

Passo a passo:

1. Define constantes para os tamanhos máximos.
2. Lê o primeiro nome e o apelido.
3. Copia o primeiro nome para o array do nome completo.
4. Acrescenta um espaço.
5. Acrescenta o apelido.
6. Mostra o resultado e testa com nomes curtos.

### Exercício 78 - Lista de nomes

Objetivo: praticar matriz de caracteres, ou seja, vários textos guardados numa só estrutura.

Lê nomes completos de 5 alunos e mostra a lista numerada no final.

Requisitos:

- Usa uma matriz de caracteres, por exemplo `char nomes[5][50]`.
- Usa constantes para o número de alunos e para o tamanho máximo de cada nome.
- Usa `fgets` para permitir nomes com espaços.
- Remove o `\n` final de cada nome.
- Mostra a lista com numeração de 1 a 5.

Passo a passo:

1. Declara a matriz de caracteres.
2. Usa um ciclo para ler cada nome.
3. Em cada leitura, remove o `\n` final.
4. Usa outro ciclo para mostrar os nomes.
5. Testa com nomes simples e nomes com espaços.

### Exercício 79 - Matriz 3x3: leitura, visualização e soma

Objetivo: praticar leitura e percurso completo de uma matriz.

Lê uma matriz 3x3 de inteiros, mostra-a em formato de tabela e calcula a soma de todos os elementos.

Requisitos:

- Usa constantes para o número de linhas e colunas.
- Usa dois ciclos `for` para ler os valores.
- Usa dois ciclos `for` para mostrar a matriz.
- Calcula a soma total dos elementos.
- O output deve manter a estrutura de linhas e colunas.

Passo a passo:

1. Declara a matriz.
2. Lê cada valor indicando linha e coluna ao utilizador.
3. Soma os valores durante a leitura ou num segundo percurso.
4. Mostra a matriz com quebras de linha no fim de cada linha.
5. Mostra a soma total.

### Exercício 80 - Matriz 3x3: diagonal, linhas e colunas

Objetivo: praticar acesso a posições específicas de uma matriz.

Lê uma matriz 3x3 de inteiros e calcula:

- a soma da diagonal principal;
- a soma de cada linha;
- a soma de cada coluna.

Requisitos:

- Usa dois ciclos para ler a matriz.
- Para a diagonal principal, usa posições em que linha e coluna têm o mesmo índice.
- Mostra a soma de cada linha de forma identificada.
- Mostra a soma de cada coluna de forma identificada.
- Mantém os limites corretos: índices de `0` a `2`.

Passo a passo:

1. Lê a matriz completa.
2. Calcula a soma da diagonal principal.
3. Percorre cada linha e calcula a sua soma.
4. Percorre cada coluna e calcula a sua soma.
5. Testa com uma matriz simples, como valores de 1 a 9.

### Exercício 81 - Desafio final: ordenação e reflexão

Objetivo: consolidar arrays através de um desafio um pouco mais exigente e de uma explicação escrita.

Lê 10 inteiros para um array, ordena-os por ordem crescente usando um método simples e explica, por palavras tuas, a diferença entre arrays estáticos e estruturas dinâmicas.

Requisitos:

- Usa um método simples de ordenação, como bubble sort ou selection sort.
- Não uses funções prontas de ordenação.
- Mostra o array antes e depois da ordenação.
- Na explicação escrita, refere tamanho fixo, memória reservada e limites do array.
- A parte de reflexão deve ter linguagem clara e pelo menos um exemplo prático.

Passo a passo:

1. Lê os 10 valores para o array.
2. Mostra o array original.
3. Aplica um algoritmo simples de ordenação.
4. Mostra o array ordenado.
5. Escreve uma explicação curta sobre quando um array estático é suficiente e quando uma estrutura dinâmica pode ser necessária.
6. Testa com valores repetidos, valores já ordenados e valores em ordem inversa.

---

<a id="exercicios-13"></a>

## 13 · Estruturas de Dados Compostas: `struct`, `union` e `enum`

Fonte: [13_estruturas_compostas_struct_union_enum.md](./13_estruturas_compostas_struct_union_enum.md)

Ordem recomendada: resolver por sequência, do 82 ao 93. Os exercícios 82 a 87 devem consolidar bem `struct` antes de avançares para `enum`, apontadores e `union`.

### Exercício 82 - `struct` básico

Objetivo: criar uma primeira `struct` e perceber que ela representa uma entidade com vários campos relacionados.

Cria uma `struct Livro` com título, autor, ano de publicação, preço e disponibilidade. Depois cria uma variável desse tipo com valores fixos e imprime todos os campos.

Requisitos:

- Usa `typedef struct` para poderes declarar variáveis apenas com `Livro`.
- Usa arrays de `char` para título e autor.
- Usa `int` para o ano, `double` ou `float` para o preço e `int` para a disponibilidade.
- Inicializa a variável diretamente na declaração.
- O output deve identificar cada campo pelo nome.

Passo a passo:

1. Define o tipo `Livro` antes do `main`.
2. Escolhe os campos: `titulo`, `autor`, `ano`, `preco` e `disponivel`.
3. No `main`, cria uma variável `Livro livro`.
4. Inicializa todos os campos com valores simples.
5. Mostra os campos usando o operador ponto (`.`).
6. Para a disponibilidade, mostra uma mensagem como "disponível" ou "indisponível".

### Exercício 83 - Leitura e impressão

Objetivo: preencher uma `struct` com dados introduzidos pelo utilizador.

Lê os dados de um livro e imprime uma ficha organizada no final.

Requisitos:

- Reutiliza uma `struct Livro` com título, autor, ano e preço.
- Lê título e autor com `fgets`, para permitir espaços.
- Remove o `\n` final das strings, se existir.
- Valida que o ano é positivo.
- Valida que o preço não é negativo.
- Mostra uma mensagem de erro clara se algum valor numérico for inválido.

Passo a passo:

1. Declara uma variável `Livro livro`.
2. Lê primeiro os campos de texto com `fgets`.
3. Remove o `\n` de cada campo de texto com `strcspn`.
4. Lê o ano e o preço com `scanf`.
5. Antes de imprimir a ficha, verifica se o ano e o preço são válidos.
6. Testa com um título com espaços, por exemplo `Os Maias`.

> Resolução:

```c
#include <stdio.h>
#include <string.h>

#define MAX_TITULO 100
#define MAX_AUTOR 50

typedef struct {
    char titulo[MAX_TITULO];
    char autor[MAX_AUTOR];
    int ano;
    double preco;
} Livro;

int main() {
    Livro livro;

    // Lê título e autor
    printf("Escreve o título do livro: ");
    fgets(livro.titulo, MAX_TITULO, stdin);
    livro.titulo[strcspn(livro.titulo, "\n")] = '\0'; // Remove o \n

    printf("Escreve o autor do livro: ");
    fgets(livro.autor, MAX_AUTOR, stdin);
    livro.autor[strcspn(livro.autor, "\n")] = '\0'; // Remove o \n

    // Lê ano e preço
    printf("Escreve o ano de publicação: ");
    scanf("%d", &livro.ano);
    printf("Escreve o preço do livro: ");
    scanf("%lf", &livro.preco);

    // Validações
    if (livro.ano <= 0) {
        printf("Ano inválido. O ano deve ser positivo.\n");
        return 1;
    }
    if (livro.preco < 0) {
        printf("Preço inválido. O preço não pode ser negativo.\n");
        return 1;
    }

    // Imprime a ficha do livro
    printf("\nFicha do Livro:\n");
    printf("Título: %s\n", livro.titulo);
    printf("Autor: %s\n", livro.autor);
    printf("Ano de Publicação: %d\n", livro.ano);
    printf("Preço: %.2lf\n", livro.preco);

    return 0;
}
```

### Exercício 84 - Array de structs

Objetivo: guardar vários registos do mesmo tipo num array de `struct`.

Cria um array com 5 livros e mostra apenas os livros publicados depois de 2020.

Requisitos:

- Usa uma constante para o número de livros.
- Podes inicializar os livros diretamente no código.
- Cada livro deve ter pelo menos título, autor, ano e preço.
- Percorre o array com um ciclo `for`.
- Mostra também quantos livros foram encontrados.
- Se nenhum livro cumprir a condição, mostra uma mensagem adequada.

Passo a passo:

1. Define `#define TOTAL_LIVROS 5`.
2. Declara `Livro livros[TOTAL_LIVROS]`.
3. Inicializa o array com dados fáceis de verificar.
4. Cria um contador para livros publicados depois de 2020.
5. Percorre o array e compara `livros[i].ano > 2020`.
6. Mostra título, autor e ano dos livros encontrados.

### Exercício 85 - Função que recebe uma `struct`

Objetivo: separar responsabilidades criando uma função que recebe uma `struct` por valor.

Define uma `struct Produto` com código, nome, preço e stock. Cria uma função `mostrar_produto` que recebe um `Produto` e imprime os seus dados.

Requisitos:

- A função deve receber um parâmetro do tipo `Produto`.
- A função não deve alterar o produto.
- O `main` deve criar pelo menos dois produtos e chamar a função para cada um.
- O stock deve ser inteiro e o preço deve permitir casas decimais.
- O output deve ficar em formato de ficha ou linha de relatório.

Passo a passo:

1. Define o tipo `Produto`.
2. Escreve o protótipo `void mostrar_produto(Produto produto);`.
3. No `main`, cria dois produtos com valores fixos.
4. Chama `mostrar_produto` para cada produto.
5. Implementa a função depois do `main`.
6. Confirma que todos os campos aparecem no output.

### Exercício 86 - Turma com array de `struct`

Objetivo: combinar arrays, strings e `struct` para representar uma pequena turma.

Cria uma `struct Aluno` com número, nome e média. Lê 5 alunos, calcula a média da turma e mostra os alunos com média positiva.

Requisitos:

- Usa uma constante para o número de alunos.
- Guarda todos os alunos num array de `Aluno`.
- O nome deve permitir espaços.
- A média de cada aluno deve estar entre 0 e 20.
- Se uma média for inválida, mostra erro e não uses esse valor no cálculo.
- Calcula a média da turma dividindo pelo número de médias válidas.
- Se nenhuma média for válida, mostra uma mensagem em vez de dividir por zero.
- Mostra a média da turma com duas casas decimais quando houver pelo menos uma média válida.

Passo a passo:

1. Define `#define TOTAL_ALUNOS 5`.
2. Declara `Aluno turma[TOTAL_ALUNOS]`.
3. Usa um ciclo para ler número, nome e média de cada aluno.
4. Remove o `\n` final dos nomes lidos com `fgets`.
5. Acumula a soma das médias válidas e conta quantas médias válidas existem.
6. No fim, mostra a média da turma e lista os alunos com média maior ou igual a 10.
7. Testa com uma turma em que pelo menos um aluno tem negativa.

### Exercício 87 - Pesquisa linear em array de `struct`

Objetivo: procurar um registo dentro de um array de `struct`.

Usa uma turma com alunos já inicializados no código. Lê um número de aluno e procura esse aluno no array.

Requisitos:

- Usa a mesma ideia da `struct Aluno`: número, nome e média.
- A pesquisa deve percorrer o array desde a posição `0`.
- Quando encontrares o aluno, podes parar a pesquisa.
- Se encontrares, mostra todos os dados do aluno.
- Se não encontrares, mostra uma mensagem clara.
- A posição mostrada ao utilizador pode começar em 1.

Passo a passo:

1. Inicializa um array com 5 alunos.
2. Lê o número a pesquisar.
3. Cria uma variável `encontrado` inicializada a `0`.
4. Percorre o array com `for`.
5. Compara `turma[i].numero` com o número pesquisado.
6. Guarda a posição quando encontrares o aluno.
7. Testa um número existente e um número inexistente.

### Exercício 88 - `enum` para valores com nome

Objetivo: usar `enum` para substituir números mágicos por nomes claros.

Define um `enum DiaSemana` com os dias úteis e cria um programa que lê um número de 1 a 5 e mostra o nome do dia correspondente.

Requisitos:

- O `enum` deve ter nomes como `SEGUNDA`, `TERCA`, `QUARTA`, `QUINTA`, `SEXTA`.
- Atribui valores explícitos ao `enum`, por exemplo `SEGUNDA = 1`, para coincidir com o input do utilizador.
- O número lido pelo utilizador deve ser validado.
- Se o número estiver fora de 1 a 5, mostra erro.
- Usa `switch` ou `if/else if` para mostrar o texto do dia.
- No código principal, evita usar números sem significado para representar dias.

Passo a passo:

1. Define o `enum DiaSemana`.
2. Lê um número entre 1 e 5.
3. Converte esse número para o valor correspondente do `enum`.
4. Mostra o dia usando os nomes do `enum`.
5. Testa com `1`, `5` e um valor inválido como `9`.

### Exercício 89 - `struct` com `enum`

Objetivo: representar o estado de uma entidade com `enum` dentro de uma `struct`.

Cria uma `struct Pedido` com código, nome do cliente, total e estado. O estado deve ser um `enum EstadoPedido` com `PENDENTE`, `ENVIADO` e `ENTREGUE`.

Requisitos:

- Usa `typedef enum` para o estado.
- Usa `typedef struct` para o pedido.
- Cria pelo menos 3 pedidos num array.
- Mostra apenas os pedidos que ainda não foram entregues.
- Ao imprimir o estado, mostra texto legível e não o valor numérico do `enum`.
- Não uses `0`, `1` e `2` diretamente no código principal para comparar estados.

Passo a passo:

1. Define `EstadoPedido`.
2. Define `Pedido`.
3. Inicializa um array com 3 pedidos.
4. Percorre o array.
5. Se o estado for diferente de `ENTREGUE`, mostra o pedido.
6. Cria uma função auxiliar, se quiseres, para converter o estado em texto.

### Exercício 90 - `struct` dentro de `struct`

Objetivo: modelar uma entidade composta por outra entidade.

Cria uma `struct Data` com dia, mês e ano. Depois cria uma `struct Aluno` que inclui número, nome, média e data de nascimento.

Requisitos:

- A `struct Aluno` deve ter um campo do tipo `Data`.
- Cria pelo menos um aluno com data de nascimento inicializada.
- Mostra a data no formato `dia/mes/ano`.
- Usa acesso encadeado aos campos, por exemplo `aluno.nascimento.dia`.
- Valida de forma simples que dia está entre 1 e 31 e mês entre 1 e 12.

Passo a passo:

1. Define primeiro a `struct Data`.
2. Define depois a `struct Aluno`.
3. Cria um aluno no `main`.
4. Imprime número, nome, média e data de nascimento.
5. Escreve uma condição simples para validar dia e mês.
6. Testa também uma data inválida para confirmar a mensagem de erro.

### Exercício 91 - Atualizar uma `struct` com ponteiro

Objetivo: perceber quando se usa `->` para alterar uma `struct` através de um apontador.

Cria uma `struct Produto` com código, nome, preço e stock. Depois cria uma função `atualizar_stock` que recebe um apontador para `Produto` e altera o stock.

Requisitos:

- A função deve ter um parâmetro `Produto *produto`.
- A função deve usar o operador `->`.
- O novo stock não pode ser negativo.
- Se o novo stock for inválido, a função não deve alterar o produto.
- O `main` deve mostrar o produto antes e depois da tentativa de atualização.

Passo a passo:

1. Define a `struct Produto`.
2. Escreve o protótipo `int atualizar_stock(Produto *produto, int novo_stock);`.
3. No `main`, cria um produto com stock inicial.
4. Chama a função passando `&produto`.
5. Dentro da função, valida `novo_stock`.
6. Se for válido, usa `produto->stock = novo_stock`.
7. Devolve `1` em caso de sucesso e `0` em caso de erro.

### Exercício 92 - `union` com indicação do tipo ativo

Objetivo: compreender que uma `union` guarda valores alternativos, mas só um campo deve ser considerado válido de cada vez.

Cria um tipo `Dado` que pode guardar um valor inteiro ou um valor real. Usa um `enum` para indicar qual dos campos da `union` está ativo.

Requisitos:

- Define um `enum TipoDado` com `DADO_INTEIRO` e `DADO_REAL`.
- Define uma `union Valor` com `int inteiro` e `float real`.
- Define uma `struct Dado` com dois campos: `tipo` e `valor`.
- Cria um exemplo de `Dado` inteiro e outro de `Dado` real.
- Ao imprimir, consulta primeiro o campo `tipo`.
- Não leias um campo da `union` diferente daquele indicado pelo `tipo`.

Passo a passo:

1. Define `TipoDado`.
2. Define `Valor`.
3. Define `Dado`.
4. Cria `Dado a` com tipo inteiro.
5. Cria `Dado b` com tipo real.
6. Escreve uma função `mostrar_dado(Dado dado)`.
7. Dentro da função, usa `if` ou `switch` para imprimir o campo correto da `union`.

### Exercício 93 - Reflexão

Objetivo: consolidar os conceitos de `struct`, `union` e `enum` através de uma explicação escrita e justificada.

Explica porque `struct`, `enum` e `union` não resolvem o mesmo problema.

Requisitos:

- Não escrevas um programa completo, exceto se precisares de pequenos exemplos para justificar uma ideia.
- A resposta deve usar linguagem técnica correta e frases claras.
- Justifica cada escolha com base no problema e não apenas no nome do conceito.
- Inclui pelo menos um exemplo ou situação prática quando isso ajudar a explicação.
- Refere explicitamente qual destes conceitos será mais comum nos teus primeiros programas em C.

Passo a passo:

1. Explica para que serve uma `struct`.
2. Explica para que serve um `enum`.
3. Explica para que serve uma `union`.
4. Dá um exemplo de problema real adequado a cada conceito.
5. Compara `struct` e `union`, destacando que na `struct` os campos coexistem e na `union` partilham memória.
6. Termina com uma conclusão curta sobre porque `struct` e `enum` aparecem mais cedo e com mais frequência em programas simples.

---

<a id="exercicios-14"></a>

## 14 · Estruturas de Dados Dinâmicas: Apontadores, Acesso e Manipulação

Fonte: [14_estruturas_dinamicas_apontadores.md](./14_estruturas_dinamicas_apontadores.md)

Ordem recomendada: resolver por sequência, do 94 ao 111. Antes de usar `malloc`, garante que sabes explicar a diferença entre valor, endereço e conteúdo apontado. Os exercícios 104 a 111 devem ser resolvidos por ordem, porque constroem gradualmente uma lista ligada.

### Exercício 94 - Endereços

Objetivo: distinguir valor de uma variável e endereço dessa variável.

Cria um programa com três variáveis (`int`, `double` e `char`), cria um apontador para cada uma e mostra os valores e os endereços guardados nesses apontadores.

Requisitos:

- Cria um apontador para cada variável.
- Usa `&` para guardar o endereço de cada variável no apontador correspondente.
- Usa `%p` para imprimir endereços.
- O output deve deixar claro o que é valor da variável e o que é endereço guardado no apontador.
- Não uses `malloc` neste exercício.
- Não alteres valores através dos apontadores neste exercício; isso fica para os exercícios seguintes.

Passo a passo:

1. Declara uma variável `int idade`, uma `double media` e uma `char letra`.
2. Atribui valores fixos às três variáveis.
3. Declara `int *p_idade`, `double *p_media` e `char *p_letra`.
4. Guarda em cada apontador o endereço da variável correspondente.
5. Imprime o valor de cada variável.
6. Imprime o endereço guardado em cada apontador com `%p`.
7. Executa o programa duas vezes e observa que os endereços podem mudar.

> Resolução:

```c

#include <stdio.h>
int main() {
    int idade = 25;
    double media = 15.5;
    char letra = 'A';

    int *p_idade = &idade;
    double *p_media = &media;
    char *p_letra = &letra;

    printf("Valor de idade: %d, Endereço de idade: %p\n", idade, (void *)p_idade);
    printf("Valor de media: %.2f, Endereço de media: %p\n", media, (void *)p_media);
    printf("Valor de letra: %c, Endereço de letra: %p\n", letra, (void *)p_letra);

    return 0;
}
```

Ao fazer cast para `(void *)` ao imprimir endereços, garantimos que o formato é consistente e evitamos warnings em alguns compiladores.
O cast é quando transformamos um tipo de dado em outro, e neste caso, estamos dizendo ao compilador para tratar o valor do apontador como um ponteiro genérico (`void *`), que é o tipo recomendado para imprimir endereços.

### Exercício 95 - Ponteiro básico

Objetivo: perceber quando um apontador é necessário para alterar uma variável original.

Cria duas funções: uma tenta aumentar uma idade recebendo `int`, e outra aumenta a idade recebendo `int *`.

Requisitos:

- A primeira função deve chamar-se `aniversario_errado` e receber `int idade`.
- A segunda função deve chamar-se `aniversario` e receber `int *idade`.
- Mostra a idade antes e depois de chamar cada função.
- Explica, num comentário curto, porque a primeira função não altera a variável original.
- Não uses variáveis globais.

Passo a passo:

1. Declara `int idade = 16;` no `main`.
2. Chama `aniversario_errado(idade)`.
3. Mostra que a idade continua igual.
4. Chama `aniversario(&idade)`.
5. Dentro de `aniversario`, usa `*idade = *idade + 1`.
6. Mostra que agora a idade original foi alterada.

> Resolução:

```c
#include <stdio.h>

void aniversario_errado(int idade) {
    // Esta função recebe uma cópia do valor de idade, então não altera a variável original.
    idade = idade + 1; // Aumenta a idade local, mas isso não afeta a variável no main.
}

void aniversario(int *idade) {
    // Esta função recebe um apontador para idade, então pode alterar a variável original.
    *idade = *idade + 1; // Aumenta a idade usando o conteúdo apontado, alterando a variável no main.
}

int main() {
    int idade = 16;

    printf("Idade antes do aniversário errado: %d\n", idade);
    aniversario_errado(idade);
    printf("Idade depois do aniversário errado: %d\n", idade); // Continua 16

    printf("Idade antes do aniversário correto: %d\n", idade);
    aniversario(&idade);
    printf("Idade depois do aniversário correto: %d\n", idade); // Agora é 17

    return 0;
}
```

### Exercício 96 - Troca de valores

Objetivo: usar dois apontadores para alterar duas variáveis originais.

Cria uma função `trocar` que recebe dois apontadores para `int` e troca os valores das variáveis originais.

Requisitos:

- A função deve ter a assinatura `void trocar(int *a, int *b)`.
- Usa uma variável temporária dentro da função.
- Mostra os valores antes e depois da troca.
- A função não deve ler input nem imprimir mensagens.
- O `main` é responsável por mostrar os resultados.

Passo a passo:

1. Declara dois inteiros no `main`, por exemplo `x = 10` e `y = 20`.
2. Mostra os valores iniciais.
3. Chama `trocar(&x, &y)`.
4. Dentro da função, guarda temporariamente `*a`.
5. Faz a troca usando `*a` e `*b`.
6. Mostra os valores finais no `main`.

> Resolução:

```c
#include <stdio.h>

void trocar(int *a, int *b) {
    int temp = *a; // Guarda o valor apontado por a
    *a = *b;       // Atribui o valor apontado por b a a
    *b = temp;     // Atribui o valor guardado em temp a b
}

int main() {
    int x = 10;
    int y = 20;

    printf("Antes da troca: x = %d, y = %d\n", x, y);
    trocar(&x, &y);
    printf("Depois da troca: x = %d, y = %d\n", x, y);

    return 0;
}
```

### Exercício 97 - Apontadores e arrays

Objetivo: perceber que arrays e apontadores estão relacionados em C.

Cria uma função `mostrar_array` que receba um array de inteiros e o seu tamanho, mostrando todos os elementos.

Requisitos:

- A função pode receber o array como `int valores[]` ou como `int *valores`.
- A função deve receber também o tamanho do array.
- Não acedas fora dos limites do array.
- No `main`, cria um array estático com 5 inteiros.
- Mostra também o endereço do primeiro elemento com `&valores[0]`.

Passo a passo:

1. Declara um array `int valores[5]`.
2. Escreve o protótipo de `mostrar_array`.
3. Chama a função passando o array e o tamanho.
4. Dentro da função, percorre o array com `for`.
5. Mostra cada posição e o respetivo valor.
6. Confirma que o ciclo usa `< tamanho`.

> Resolução:

```c
#include <stdio.h>

void mostrar_array(int valores[], int tamanho) {
    printf("Array: ");
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", valores[i]);
    }
    printf("\n");
}
int main() {
    int valores[5] = {10, 20, 30, 40, 50};
    printf("Endereço do primeiro elemento: %p\n", (void *)&valores[0]);
    mostrar_array(valores, 5);
    return 0;
}
```

Ou a mostrar o valor e o endereço de cada elemento na função:

```c

void mostrar_array(int valores[], int tamanho) {
    printf("Array:\n");
    for (int i = 0; i < tamanho; i++) {
        printf("Posição %d: valor = %d, endereço = %p\n", i, valores[i], (void *)&valores[i]);
    }
}
```

### Exercício 98 - Apontadores e arrays

Objetivo: perceber que o nome de um array é um apontador para o primeiro elemento.

Cria um programa que declare um array de inteiros e mostre o valor do primeiro elemento usando o nome do array e usando um apontador.

Requisitos:

- Declara um array `int numeros[5]` e inicializa-o com valores fixos.
- Declara um apontador `int *p_numeros` e atribui-lhe o endereço do primeiro elemento do array.
- Mostra o valor do primeiro elemento usando `numeros[0]` e usando `*p_numeros`.
- Mostra o endereço do primeiro elemento usando `&numeros[0]` e usando `p_numeros`.
- O output deve deixar claro que `numeros` e `p_numeros` estão relacionados.

Por exemplo, o output pode ser:

```
Valor do primeiro elemento usando numeros[0]: 10
Valor do primeiro elemento usando *p_numeros: 10
Endereço do primeiro elemento usando &numeros[0]: 0x7ffee3bc8a0
Endereço do primeiro elemento usando p_numeros: 0x7ffee3bc8a0
```

Passo a passo:

1. Declara `int numeros[5] = {10, 20, 30, 40, 50};`.
2. Declara `int *p_numeros = numeros;` ou `int *p_numeros = &numeros[0];`.
3. Imprime o valor do primeiro elemento usando `numeros[0]` e `*p_numeros`.
4. Imprime o endereço do primeiro elemento usando `&numeros[0]` e `p_numeros`.
5. Executa o programa e observa que os endereços são iguais.

### Exercício 99 - Vetor dinâmico com `malloc`

Objetivo: reservar memória durante a execução para guardar uma quantidade variável de valores.

Lê `n`, reserva dinamicamente um array de `n` inteiros, lê os valores e calcula soma e média.

Requisitos:

- Valida que `n` é maior do que zero.
- Usa `malloc(n * sizeof *valores)`.
- Verifica se `malloc` falhou.
- Não calcules a média se `n` for inválido.
- Liberta a memória antes de terminar.
- Mostra a média com duas casas decimais.

Passo a passo:

1. Lê `n`.
2. Se `n <= 0`, mostra erro e termina.
3. Reserva memória para `n` inteiros.
4. Lê os valores num ciclo.
5. Soma os valores.
6. Calcula a média com cast para `double`.
7. Mostra soma e média.
8. Faz `free(valores)` e `valores = NULL`.

> Resolução:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("Quantos valores queres ler? ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("Número inválido. O número deve ser maior que zero.\n");
        return 1;
    }

    int *valores = malloc(n * sizeof *valores);
    if (valores == NULL) {
        printf("Erro na reserva de memória.\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        printf("Escreve o valor %d: ", i + 1);
        scanf("%d", &valores[i]);
    }

    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += valores[i];
    }

    double media = (double)soma / n;
    printf("Soma: %d, Média: %.2lf\n", soma, media);

    free(valores);
    valores = NULL;

    return 0;
}
```

Pergunta: Porque é que estamos a criar arrays usando o `malloc`e não usando arrays estáticos? Em que situações é que um array dinâmico é necessário?

Resposta: Usamos `malloc` para criar arrays quando não sabemos de antemão quantos elementos vamos precisar, ou quando o número de elementos pode ser muito grande para ser alocado na stack. Arrays estáticos têm um tamanho fixo definido no momento da compilação, enquanto arrays dinâmicos permitem que reservemos memória durante a execução, o que é útil para lidar com dados cujo tamanho só é conhecido em tempo de execução. Por exemplo, se estivermos a ler uma lista de números do utilizador e não soubermos quantos números serão introduzidos, um array dinâmico é a escolha certa. Além disso, arrays dinâmicos podem ser redimensionados com `realloc`, oferecendo ainda mais flexibilidade.

### Exercício 100 - `calloc`

Objetivo: comparar `malloc` e `calloc` quanto à inicialização dos valores.

Reserva dinamicamente um array de 5 inteiros com `calloc` e mostra os valores antes de lhes atribuíres qualquer valor manualmente.

Requisitos:

- Usa `calloc(5, sizeof *valores)`.
- Verifica se `calloc` devolveu `NULL`.
- Mostra os 5 valores logo após a reserva.
- Depois altera os valores para `10`, `20`, `30`, `40` e `50`.
- Mostra novamente o array.
- Liberta a memória no fim.

Passo a passo:

1. Reserva o array com `calloc`.
2. Verifica se a reserva falhou.
3. Usa um ciclo para mostrar os valores iniciais.
4. Atribui valores manualmente a cada posição.
5. Usa outro ciclo para mostrar os novos valores.
6. Faz `free` e coloca o apontador a `NULL`.

> Resolução:

```c

#include <stdio.h>

int main() {
    int *valores = calloc(5, sizeof *valores);
    if (valores == NULL) {
        printf("Erro na reserva de memória.\n");
        return 1;
    }

    printf("Valores iniciais:\n");
    for (int i = 0; i < 5; i++) {
        printf("valores[%d] = %d\n", i, valores[i]);
    }

    // Atribui novos valores
    valores[0] = 10;
    valores[1] = 20;
    valores[2] = 30;
    valores[3] = 40;
    valores[4] = 50;

    printf("\nValores após atribuição:\n");
    for (int i = 0; i < 5; i++) {
        printf("valores[%d] = %d\n", i, valores[i]);
    }

    free(valores);
    valores = NULL;

    return 0;
}
```

### Exercício 101 - `realloc`

Objetivo: praticar redimensionamento seguro de memória dinâmica.

Começa com um array dinâmico de 5 inteiros, preenche-o com valores fixos, expande-o para 10 posições com `realloc` e preenche as novas posições.

Requisitos:

- Usa `malloc` para reservar as primeiras 5 posições.
- Verifica se `malloc` devolveu `NULL`.
- Usa um apontador temporário para guardar o resultado de `realloc`.
- Só atualizes o apontador original se `realloc` tiver sucesso.
- Mostra os 10 valores no final.
- Faz `free` no fim e coloca o apontador a `NULL`.

Passo a passo:

1. Define `tamanho = 5`.
2. Reserva memória com `malloc(tamanho * sizeof *valores)`.
3. Preenche as primeiras 5 posições.
4. Cria `novo_tamanho = 10`.
5. Faz `int *temporario = realloc(valores, novo_tamanho * sizeof *valores);`.
6. Se `temporario == NULL`, liberta `valores` e termina com erro.
7. Se funcionar, faz `valores = temporario`.
8. Preenche as posições de índice 5 a 9.
9. Mostra todos os valores e liberta a memória.

> Resolução:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int tamanho = 5;
    int *valores = malloc(tamanho * sizeof *valores);
    if (valores == NULL) {
        printf("Erro na reserva de memória.\n");
        return 1;
    }

    // Preenche as primeiras 5 posições
    for (int i = 0; i < tamanho; i++) {
        valores[i] = (i + 1) * 10; // 10, 20, 30, 40, 50
    }

    int novo_tamanho = 10;
    int *temporario = realloc(valores, novo_tamanho * sizeof *valores);
    if (temporario == NULL) {
        free(valores);
        printf("Erro no redimensionamento da memória.\n");
        return 1;
    }
    valores = temporario;

    // Preenche as novas posições
    for (int i = tamanho; i < novo_tamanho; i++) {
        valores[i] = (i + 1) * 10; // Continua a sequência: 60, 70, 80, 90, 100
    }

    // Mostra todos os valores
    printf("Valores no array redimensionado:\n");
    for (int i = 0; i < novo_tamanho; i++) {
        printf("valores[%d] = %d\n", i, valores[i]);
    }

    free(valores);
    valores = NULL;

    return 0;
}
```

### Exercício 102 - `struct` dinâmica

Objetivo: criar uma `struct` em memória dinâmica e aceder aos seus campos com `->`.

Define uma `struct Produto` com código, nome e preço. Reserva dinamicamente um produto, preenche os campos e mostra os dados.

Requisitos:

- Usa `Produto *produto = malloc(sizeof *produto);`.
- Verifica se `produto == NULL`.
- Usa `->` para preencher e mostrar os campos.
- Para o nome, usa uma string que saibas que cabe no array.
- Faz `free(produto)` no fim.
- Coloca `produto = NULL` depois de libertar.

Passo a passo:

1. Define o tipo `Produto`.
2. Reserva memória para um produto.
3. Verifica se a reserva falhou.
4. Preenche `codigo`, `nome` e `preco`.
5. Mostra os campos usando `produto->campo`.
6. Liberta a memória.

> Resolução:

```c

#include <stdio.h>

typedef struct {
    int codigo;
    char nome[50];
    float preco;
} Produto;

int main() {
    Produto *produto = malloc(sizeof *produto);
    if (produto == NULL) {
        printf("Erro na reserva de memória.\n");
        return 1;
    }

    produto->codigo = 123;
    snprintf(produto->nome, sizeof produto->nome, "Caneta Azul");
    produto->preco = 2.99;

    printf("Produto:\n");
    printf("Código: %d\n", produto->codigo);
    printf("Nome: %s\n", produto->nome);
    printf("Preço: %.2f\n", produto->preco);

    free(produto);
    produto = NULL;

    return 0;
}
```

### Exercício 103 - Array dinâmico de `struct`

Objetivo: combinar arrays dinâmicos com tipos compostos.

Lê o número de alunos de uma turma, reserva dinamicamente um array de `Aluno` e calcula a média da turma.

Requisitos:

- Define `struct Aluno` com número, nome e média.
- Valida que o número de alunos é maior que zero.
- Usa `malloc(total * sizeof *turma)`.
- Verifica se a reserva falhou.
- Para simplificar a leitura, podes usar nomes sem espaços com `scanf("%49s", turma[i].nome)`.
- Cada média deve estar entre 0 e 20.
- Liberta a memória antes de terminar.

Passo a passo:

1. Lê `total_alunos`.
2. Valida o valor.
3. Reserva memória para o array de alunos.
4. Lê os dados de cada aluno.
5. Soma apenas médias válidas.
6. Calcula a média da turma com base nas médias válidas.
7. Mostra a média ou uma mensagem se não houver médias válidas.
8. Faz `free(turma)`.

> Resolução:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int numero;
    char nome[50];
    float media;
} Aluno;

int main() {
    int total_alunos;
    printf("Quantos alunos tem a turma? ");
    scanf("%d", &total_alunos);

    if (total_alunos <= 0) {
        printf("Número de alunos inválido.\n");
        return 1;
    }

    Aluno *turma = malloc(total_alunos * sizeof *turma);
    if (turma == NULL) {
        printf("Erro na reserva de memória.\n");
        return 1;
    }

    float soma_medias = 0.0;
    int count_medias_validas = 0;

    for (int i = 0; i < total_alunos; i++) {
        printf("Aluno %d:\n", i + 1);
        printf("Número: ");
        scanf("%d", &turma[i].numero);
        printf("Nome: ");
        scanf("%49s", turma[i].nome);
        printf("Média: ");
        scanf("%f", &turma[i].media);

        if (turma[i].media >= 0 && turma[i].media <= 20) {
            soma_medias += turma[i].media;
            count_medias_validas++;
        } else {
            printf("Média inválida para o aluno %d. Ignorando esta média.\n", i + 1);
        }
    }

    if (count_medias_validas > 0) {
        float media_turma = soma_medias / count_medias_validas;
        printf("Média da turma: %.2f\n", media_turma);
    } else {
        printf("Não há médias válidas para calcular a média da turma.\n");
    }

    free(turma);
    turma = NULL;

    return 0;
}
```

### Exercício 104 - Lista ligada: nó único

Objetivo: perceber a estrutura mínima de um nó de lista ligada.

Define uma `struct No` com um valor inteiro e um apontador para o próximo nó. Cria dinamicamente um único nó, mostra o valor e liberta a memória.

Requisitos:

- Usa a forma `typedef struct No { ... } No;`.
- O campo `proximo` deve ser do tipo `struct No *`.
- Reserva memória para um nó com `malloc`.
- Define `proximo` como `NULL`.
- Mostra o valor do nó.
- Liberta o nó no fim.

Passo a passo:

1. Define a `struct No`.
2. Declara `No *no = malloc(sizeof *no);`.
3. Verifica se `no == NULL`.
4. Atribui um valor ao campo `valor`.
5. Atribui `NULL` ao campo `proximo`.
6. Mostra o valor.
7. Faz `free(no)` e `no = NULL`.

> Resolução:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *proximo;
} No;

int main() {
    No *no = malloc(sizeof *no);
    if (no == NULL) {
        printf("Erro na reserva de memória.\n");
        return 1;
    }

    no->valor = 10;
    no->proximo = NULL;

    printf("Valor do nó: %d\n", no->valor);

    free(no);
    no = NULL;

    return 0;
}
```

### Exercício 105 - Lista ligada com três nós

Objetivo: perceber como vários nós ficam ligados através do campo `proximo`.

Cria dinamicamente três nós com os valores `10`, `20` e `30`, liga-os manualmente e mostra a sequência completa.

Requisitos:

- Usa a mesma `struct No` do exercício anterior.
- Cada nó deve ser reservado com `malloc`.
- O primeiro nó deve apontar para o segundo.
- O segundo nó deve apontar para o terceiro.
- O terceiro nó deve apontar para `NULL`.
- Mostra a lista no formato `10 -> 20 -> 30 -> NULL`.
- Liberta os três nós no fim.

Passo a passo:

1. Define a `struct No`.
2. Cria três apontadores: `primeiro`, `segundo` e `terceiro`.
3. Reserva memória para cada nó.
4. Verifica se alguma reserva falhou.
5. Preenche os valores `10`, `20` e `30`.
6. Liga os nós através do campo `proximo`.
7. Mostra a sequência completa.
8. Liberta os três nós.

### Exercício 106 - Percorrer uma lista ligada

Objetivo: praticar o percurso de uma lista ligada até encontrar `NULL`.

Cria uma função `mostrar_lista` que recebe o início de uma lista ligada e mostra todos os valores.

Requisitos:

- A função deve ter a assinatura `void mostrar_lista(const No *inicio)`.
- A função não deve alterar a lista.
- Usa um apontador auxiliar chamado `atual`.
- O ciclo deve continuar enquanto `atual != NULL`.
- No fim, mostra `NULL` para indicar o fim da lista.
- Testa com uma lista vazia e com uma lista de três nós.

Passo a passo:

1. Define a `struct No`.
2. Cria a função `mostrar_lista`.
3. Dentro da função, começa com `const No *atual = inicio`.
4. Enquanto `atual` não for `NULL`, mostra `atual->valor`.
5. Avança com `atual = atual->proximo`.
6. Testa primeiro com `No *lista = NULL`.
7. Testa depois com uma lista de três nós.

### Exercício 107 - Contar nós

Objetivo: contar quantos elementos existem numa lista ligada.

Cria uma função `contar_nos` que recebe o início de uma lista ligada e devolve o número de nós existentes.

Requisitos:

- A função deve ter a assinatura `int contar_nos(const No *inicio)`.
- A função deve funcionar com uma lista vazia.
- Não uses variáveis globais.
- Não alteres os apontadores da lista original.
- Testa com listas de 0, 1 e 3 nós.

Passo a passo:

1. Declara uma variável `total` inicializada a `0`.
2. Usa um apontador auxiliar para percorrer a lista.
3. Sempre que encontrares um nó, incrementa `total`.
4. Avança para o próximo nó.
5. Quando chegares a `NULL`, devolve `total`.
6. Mostra o resultado no `main`.

### Exercício 108 - Procurar valor

Objetivo: procurar um valor percorrendo a lista nó a nó.

Cria uma função `contem_valor` que verifica se um determinado inteiro existe na lista ligada.

Requisitos:

- A função deve ter a assinatura `int contem_valor(const No *inicio, int valor)`.
- Devolve `1` se o valor existir.
- Devolve `0` se o valor não existir.
- O ciclo deve parar quando encontrar o valor ou chegar a `NULL`.
- Testa com um valor existente e com um valor inexistente.

Passo a passo:

1. Começa no primeiro nó da lista.
2. Enquanto o nó atual não for `NULL`, compara `atual->valor` com o valor procurado.
3. Se forem iguais, devolve `1`.
4. Se não forem iguais, avança para o próximo nó.
5. Se o ciclo terminar, devolve `0`.
6. No `main`, mostra uma mensagem clara com o resultado da procura.

### Exercício 109 - Inserir no início

Objetivo: perceber como atualizar o início de uma lista ligada.

Cria uma função `inserir_inicio` que cria um novo nó e o coloca no início da lista.

Requisitos:

- A função deve ter a assinatura `No *inserir_inicio(No *inicio, int valor)`.
- Reserva um novo nó com `malloc`.
- Verifica se `malloc` falhou.
- O novo nó deve apontar para o antigo início.
- A função deve devolver o novo início da lista.
- Testa inserindo os valores `30`, `20` e `10`, para obter `10 -> 20 -> 30 -> NULL`.

Passo a passo:

1. Reserva memória para o novo nó.
2. Se a reserva falhar, devolve o início antigo.
3. Preenche o campo `valor`.
4. Faz `novo->proximo = inicio`.
5. Devolve `novo`.
6. No `main`, atualiza a lista com `lista = inserir_inicio(lista, valor)`.

### Exercício 110 - Inserir no fim

Objetivo: inserir um novo nó depois do último elemento da lista.

Cria uma função `inserir_fim` que cria um novo nó e o coloca no fim da lista ligada.

Requisitos:

- A função deve ter a assinatura `No *inserir_fim(No *inicio, int valor)`.
- Se a lista estiver vazia, o novo nó passa a ser o início.
- Se a lista já tiver elementos, percorre até ao último nó.
- O último nó antigo deve apontar para o novo nó.
- O novo nó deve apontar para `NULL`.
- Testa inserindo os valores `10`, `20` e `30`, para obter `10 -> 20 -> 30 -> NULL`.

Passo a passo:

1. Reserva memória para o novo nó.
2. Preenche o valor e coloca `novo->proximo = NULL`.
3. Se `inicio == NULL`, devolve `novo`.
4. Caso contrário, percorre a lista até `atual->proximo == NULL`.
5. Liga o último nó ao novo nó.
6. Devolve o início original da lista.

### Exercício 111 - Libertar lista completa

Objetivo: libertar corretamente todos os nós de uma lista ligada.

Cria uma função `libertar_lista` que percorre a lista e liberta todos os nós criados dinamicamente.

Requisitos:

- A função deve ter a assinatura `void libertar_lista(No *inicio)`.
- Antes de libertar um nó, guarda o endereço do nó seguinte.
- Usa `free` em todos os nós.
- Não acedas a campos de um nó depois de fazer `free`.
- No `main`, coloca o apontador principal a `NULL` depois de chamar a função.
- Testa com uma lista vazia e com uma lista de vários nós.

Passo a passo:

1. Começa com `No *atual = inicio`.
2. Enquanto `atual != NULL`, guarda `No *seguinte = atual->proximo`.
3. Faz `free(atual)`.
4. Avança com `atual = seguinte`.
5. No `main`, chama `libertar_lista(lista)`.
6. Depois da chamada, faz `lista = NULL`.

---

<a id="exercicios-15"></a>

## 15 · Classes e Objetos (Contexto em C)

Fonte: [15_classes_e_objetos_contexto_c.md](./15_classes_e_objetos_contexto_c.md)

### Exercício 112 - Modelação

Objetivo: praticar modelação aplicando os conceitos de modelação de objetos em C.

Modela entidade `Aluno` como "objeto" em C (`struct` + funções).

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 113 - API mínima

Objetivo: organizar responsabilidades e tornar a solução mais modular, legível e sustentável.

Cria API para `Livro`: criar, atualizar estado e consultar dados.

Requisitos:

- Separa responsabilidades em funções, ficheiros ou tipos quando isso fizer sentido.
- Mantém nomes claros para funções, parâmetros e ficheiros.
- Evita duplicação de código e dependências desnecessárias.
- Garante que a solução continua fácil de compilar e testar.

Passo a passo:

1. Identifica as responsabilidades principais da solução.
2. Decide que funções, tipos ou ficheiros devem existir.
3. Define interfaces claras antes de escrever a implementação completa.
4. Implementa cada parte mantendo baixo acoplamento entre componentes.
5. Compila e testa o conjunto para confirmar que a organização funciona.

### Exercício 114 - Inicialização

Objetivo: praticar inicialização aplicando os conceitos de modelação de objetos em C.

Implementa função `init` para 3 tipos diferentes.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 115 - Encapsulamento

Objetivo: organizar responsabilidades e tornar a solução mais modular, legível e sustentável.

Reorganiza código para ocultar detalhes internos num `.c`.

Requisitos:

- Separa responsabilidades em funções, ficheiros ou tipos quando isso fizer sentido.
- Mantém nomes claros para funções, parâmetros e ficheiros.
- Evita duplicação de código e dependências desnecessárias.
- Garante que a solução continua fácil de compilar e testar.

Passo a passo:

1. Identifica as responsabilidades principais da solução.
2. Decide que funções, tipos ou ficheiros devem existir.
3. Define interfaces claras antes de escrever a implementação completa.
4. Implementa cada parte mantendo baixo acoplamento entre componentes.
5. Compila e testa o conjunto para confirmar que a organização funciona.

### Exercício 116 - Validação de regras

Objetivo: reforçar validação, segurança e tratamento explícito de casos inválidos.

Implementa função que recusa operações inválidas (ex.: saldo negativo).

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 117 - Modularização

Objetivo: organizar responsabilidades e tornar a solução mais modular, legível e sustentável.

Divide programa em `main.c`, `entidade.c`, `entidade.h`.

Requisitos:

- Separa responsabilidades em funções, ficheiros ou tipos quando isso fizer sentido.
- Mantém nomes claros para funções, parâmetros e ficheiros.
- Evita duplicação de código e dependências desnecessárias.
- Garante que a solução continua fácil de compilar e testar.

Passo a passo:

1. Identifica as responsabilidades principais da solução.
2. Decide que funções, tipos ou ficheiros devem existir.
3. Define interfaces claras antes de escrever a implementação completa.
4. Implementa cada parte mantendo baixo acoplamento entre componentes.
5. Compila e testa o conjunto para confirmar que a organização funciona.

### Exercício 118 - Const-correctness

Objetivo: praticar const-correctness aplicando os conceitos de modelação de objetos em C.

Cria funções de consulta que recebem ponteiro `const`.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 119 - Testes manuais

Objetivo: praticar testes manuais aplicando os conceitos de modelação de objetos em C.

Define 12 testes para validar API de uma entidade.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 120 - Refatoração

Objetivo: praticar refatoração aplicando os conceitos de modelação de objetos em C.

Converte programa monolítico num design baseado em "objetos" simulados.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 121 - Documentação

Objetivo: organizar responsabilidades e tornar a solução mais modular, legível e sustentável.

Escreve documentação de API para uma entidade criada por ti.

Requisitos:

- Separa responsabilidades em funções, ficheiros ou tipos quando isso fizer sentido.
- Mantém nomes claros para funções, parâmetros e ficheiros.
- Evita duplicação de código e dependências desnecessárias.
- Garante que a solução continua fácil de compilar e testar.

Passo a passo:

1. Identifica as responsabilidades principais da solução.
2. Decide que funções, tipos ou ficheiros devem existir.
3. Define interfaces claras antes de escrever a implementação completa.
4. Implementa cada parte mantendo baixo acoplamento entre componentes.
5. Compila e testa o conjunto para confirmar que a organização funciona.

### Exercício 122 - Evolução

Objetivo: organizar responsabilidades e tornar a solução mais modular, legível e sustentável.

Acrescenta novo comportamento mantendo compatibilidade da API.

Requisitos:

- Separa responsabilidades em funções, ficheiros ou tipos quando isso fizer sentido.
- Mantém nomes claros para funções, parâmetros e ficheiros.
- Evita duplicação de código e dependências desnecessárias.
- Garante que a solução continua fácil de compilar e testar.

Passo a passo:

1. Identifica as responsabilidades principais da solução.
2. Decide que funções, tipos ou ficheiros devem existir.
3. Define interfaces claras antes de escrever a implementação completa.
4. Implementa cada parte mantendo baixo acoplamento entre componentes.
5. Compila e testa o conjunto para confirmar que a organização funciona.

### Exercício 123 - Reflexão

Objetivo: consolidar os conceitos de modelação de objetos em C através de uma explicação escrita e justificada.

Explica semelhanças e diferenças entre este modelo em C e classes em OOP.

Requisitos:

- Não escrevas um programa completo, exceto se precisares de pequenos exemplos para justificar uma ideia.
- A resposta deve usar linguagem técnica correta e frases claras.
- Justifica cada escolha com base no problema e não apenas no nome do conceito.
- Inclui pelo menos um exemplo ou situação prática quando isso ajudar a explicação.

Passo a passo:

1. Lê a situação proposta e identifica os conceitos principais envolvidos.
2. Organiza a resposta em pontos curtos ou pequenos parágrafos.
3. Justifica cada escolha com base no tipo de problema apresentado.
4. Acrescenta um exemplo simples quando isso tornar a explicação mais clara.
5. Revê a resposta para garantir que não ficou vaga ou apenas decorada.

---

<a id="exercicios-16"></a>

## 16 · Herança e Polimorfismo (Contexto em C)

Fonte: [16_heranca_e_polimorfismo_contexto_c.md](./16_heranca_e_polimorfismo_contexto_c.md)

### Exercício 124 - Composição

Objetivo: praticar composição aplicando os conceitos de composição e polimorfismo em C.

Cria `struct Veiculo` e `struct Carro` reutilizando campos comuns.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 125 - Interface por função

Objetivo: praticar interface por função aplicando os conceitos de composição e polimorfismo em C.

Define interface de impressão para dois tipos diferentes.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 126 - Polimorfismo simples

Objetivo: praticar polimorfismo simples aplicando os conceitos de composição e polimorfismo em C.

Implementa duas funções de comportamento e seleciona em runtime.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 127 - Vetor de "objetos"

Objetivo: praticar vetor de "objetos" aplicando os conceitos de composição e polimorfismo em C.

Cria array de estruturas com ponteiro para função e executa comportamento.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 128 - Organização

Objetivo: organizar responsabilidades e tornar a solução mais modular, legível e sustentável.

Separa interface e implementação em ficheiros distintos.

Requisitos:

- Separa responsabilidades em funções, ficheiros ou tipos quando isso fizer sentido.
- Mantém nomes claros para funções, parâmetros e ficheiros.
- Evita duplicação de código e dependências desnecessárias.
- Garante que a solução continua fácil de compilar e testar.

Passo a passo:

1. Identifica as responsabilidades principais da solução.
2. Decide que funções, tipos ou ficheiros devem existir.
3. Define interfaces claras antes de escrever a implementação completa.
4. Implementa cada parte mantendo baixo acoplamento entre componentes.
5. Compila e testa o conjunto para confirmar que a organização funciona.

### Exercício 129 - Validação

Objetivo: reforçar validação, segurança e tratamento explícito de casos inválidos.

Evita chamada de ponteiro de função nulo com verificações.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 130 - Refatoração

Objetivo: praticar refatoração aplicando os conceitos de composição e polimorfismo em C.

Converte código com muitos `if` de tipo para abordagem polimórfica.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 131 - Testes

Objetivo: praticar testes aplicando os conceitos de composição e polimorfismo em C.

Define testes para validar interface comum entre tipos.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 132 - Limitações

Objetivo: consolidar os conceitos de composição e polimorfismo em C através de uma explicação escrita e justificada.

Escreve 6 limitações desta abordagem em comparação com C++.

Requisitos:

- Não escrevas um programa completo, exceto se precisares de pequenos exemplos para justificar uma ideia.
- A resposta deve usar linguagem técnica correta e frases claras.
- Justifica cada escolha com base no problema e não apenas no nome do conceito.
- Inclui pelo menos um exemplo ou situação prática quando isso ajudar a explicação.

Passo a passo:

1. Lê a situação proposta e identifica os conceitos principais envolvidos.
2. Organiza a resposta em pontos curtos ou pequenos parágrafos.
3. Justifica cada escolha com base no tipo de problema apresentado.
4. Acrescenta um exemplo simples quando isso tornar a explicação mais clara.
5. Revê a resposta para garantir que não ficou vaga ou apenas decorada.

### Exercício 133 - Expansão

Objetivo: praticar expansão aplicando os conceitos de composição e polimorfismo em C.

Adiciona um novo tipo à interface sem alterar código cliente principal.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 134 - Segurança

Objetivo: reforçar validação, segurança e tratamento explícito de casos inválidos.

Analisa código e identifica riscos com ponteiros para função.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 135 - Reflexão

Objetivo: consolidar os conceitos de composição e polimorfismo em C através de uma explicação escrita e justificada.

Explica como este módulo ajuda a entender OOP mesmo em C.

Requisitos:

- Não escrevas um programa completo, exceto se precisares de pequenos exemplos para justificar uma ideia.
- A resposta deve usar linguagem técnica correta e frases claras.
- Justifica cada escolha com base no problema e não apenas no nome do conceito.
- Inclui pelo menos um exemplo ou situação prática quando isso ajudar a explicação.

Passo a passo:

1. Lê a situação proposta e identifica os conceitos principais envolvidos.
2. Organiza a resposta em pontos curtos ou pequenos parágrafos.
3. Justifica cada escolha com base no tipo de problema apresentado.
4. Acrescenta um exemplo simples quando isso tornar a explicação mais clara.
5. Revê a resposta para garantir que não ficou vaga ou apenas decorada.

---

<a id="exercicios-17"></a>

## 17 · Exceções e Tratamento de Erros em C

Fonte: [17_excecoes_e_tratamento_de_erros_em_c.md](./17_excecoes_e_tratamento_de_erros_em_c.md)

### Exercício 136 - Divisão segura

Objetivo: reforçar validação, segurança e tratamento explícito de casos inválidos.

Implementa função de divisão com tratamento de divisor zero.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 137 - Entrada robusta

Objetivo: reforçar validação, segurança e tratamento explícito de casos inválidos.

Lê inteiro com validação de formato e intervalo.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 138 - Códigos de erro

Objetivo: praticar códigos de erro aplicando os conceitos de tratamento de erros em C.

Define tabela de códigos de erro para um mini projeto.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 139 - Ficheiros

Objetivo: praticar ficheiros aplicando os conceitos de tratamento de erros em C.

Abre ficheiro para leitura e trata todos os possíveis erros básicos.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 140 - Memória

Objetivo: praticar memória aplicando os conceitos de tratamento de erros em C.

Aloca vetor dinâmico com validação e mensagens de erro adequadas.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 141 - Propagação

Objetivo: praticar propagação aplicando os conceitos de tratamento de erros em C.

Cria cadeia de 3 funções que propagam erros até `main`.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 142 - Limpeza de recursos

Objetivo: reforçar validação, segurança e tratamento explícito de casos inválidos.

Garante que ficheiro e memória são libertados em qualquer caminho de erro.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 143 - Refatoração

Objetivo: praticar refatoração aplicando os conceitos de tratamento de erros em C.

Melhora um código sem tratamento de erros.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 144 - Diagnóstico

Objetivo: identificar problemas, explicar a causa e aplicar uma correção tecnicamente correta.

Usa `perror` e `errno` em 5 cenários distintos.

Requisitos:

- Identifica primeiro o comportamento errado ou o erro produzido.
- Explica a causa antes de apresentar a correção.
- Corrige apenas o necessário para resolver o problema indicado.
- Confirma a solução com compilação, execução ou análise manual adequada.

Passo a passo:

1. Reproduz ou lê atentamente o erro apresentado.
2. Localiza a linha ou bloco responsável pelo problema.
3. Explica a causa usando os conceitos de C envolvidos.
4. Aplica a correção mínima necessária.
5. Volta a testar ou reler o código para confirmar que o problema ficou resolvido.

### Exercício 145 - Testes de erro

Objetivo: praticar testes de erro aplicando os conceitos de tratamento de erros em C.

Define 15 testes focados apenas em cenários inválidos.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 146 - Mensagens de utilizador

Objetivo: praticar mensagens de utilizador aplicando os conceitos de tratamento de erros em C.

Reescreve mensagens técnicas para linguagem compreensível por utilizador final.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 147 - Reflexão

Objetivo: consolidar os conceitos de tratamento de erros em C através de uma explicação escrita e justificada.

Explica por que tratamento de erros faz parte da qualidade do software.

Requisitos:

- Não escrevas um programa completo, exceto se precisares de pequenos exemplos para justificar uma ideia.
- A resposta deve usar linguagem técnica correta e frases claras.
- Justifica cada escolha com base no problema e não apenas no nome do conceito.
- Inclui pelo menos um exemplo ou situação prática quando isso ajudar a explicação.

Passo a passo:

1. Lê a situação proposta e identifica os conceitos principais envolvidos.
2. Organiza a resposta em pontos curtos ou pequenos parágrafos.
3. Justifica cada escolha com base no tipo de problema apresentado.
4. Acrescenta um exemplo simples quando isso tornar a explicação mais clara.
5. Revê a resposta para garantir que não ficou vaga ou apenas decorada.

---

<a id="exercicios-18"></a>

## 18 · Ficheiros: Acesso e Manipulação em C

Fonte: [18_ficheiros_acesso_e_manipulacao_em_c.md](./18_ficheiros_acesso_e_manipulacao_em_c.md)

### Exercício 148 - Escrita simples

Objetivo: praticar escrita simples aplicando os conceitos de ficheiros em C.

Cria programa que grava 5 linhas num ficheiro texto.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 149 - Leitura simples

Objetivo: praticar leitura simples aplicando os conceitos de ficheiros em C.

Lê ficheiro linha a linha e imprime no ecrã.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 150 - Cópia de ficheiro

Objetivo: praticar cópia de ficheiro aplicando os conceitos de ficheiros em C.

Implementa cópia de um ficheiro texto para outro.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 151 - Contagem

Objetivo: praticar contagem aplicando os conceitos de ficheiros em C.

Conta número de linhas e caracteres de um ficheiro.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 152 - Registos

Objetivo: praticar registos aplicando os conceitos de ficheiros em C.

Guarda registos de alunos no formato `nome;nota`.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 153 - Pesquisa

Objetivo: praticar pesquisa aplicando os conceitos de ficheiros em C.

Lê ficheiro e procura registo por nome.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 154 - Acrescentar dados

Objetivo: praticar acrescentar dados aplicando os conceitos de ficheiros em C.

Abre ficheiro em modo append e adiciona novos registos.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 155 - Binário básico

Objetivo: praticar binário básico aplicando os conceitos de ficheiros em C.

Grava e lê array de inteiros em ficheiro binário.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 156 - Validação de I/O

Objetivo: reforçar validação, segurança e tratamento explícito de casos inválidos.

Melhora programa com tratamento de erro em cada operação de ficheiro.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 157 - Navegação

Objetivo: praticar navegação aplicando os conceitos de ficheiros em C.

Usa `fseek` e `ftell` para descobrir tamanho de ficheiro.

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 158 - Projeto curto

Objetivo: praticar projeto curto aplicando os conceitos de ficheiros em C.

Cria mini agenda persistente em ficheiro (inserir/listar).

Requisitos:

- A solução deve cumprir exatamente o comportamento pedido no enunciado.
- Usa os conceitos principais do módulo em que o exercício está inserido.
- Escolhe tipos de dados e nomes de variáveis adequados ao problema.
- Valida entradas do utilizador sempre que o exercício envolver leitura de dados.
- O output deve ser claro, organizado e fácil de verificar.

Passo a passo:

1. Identifica os dados de entrada, o processamento necessário e o resultado esperado.
2. Declara as variáveis com tipos apropriados e nomes significativos.
3. Implementa a lógica principal usando a estrutura ou conceito pedido.
4. Acrescenta validações simples para entradas ou casos especiais relevantes.
5. Compila, executa e testa com valores normais e pelo menos um caso limite.

### Exercício 159 - Reflexão

Objetivo: consolidar os conceitos de ficheiros em C através de uma explicação escrita e justificada.

Explica diferenças práticas entre guardar dados em texto e em binário.

Requisitos:

- Não escrevas um programa completo, exceto se precisares de pequenos exemplos para justificar uma ideia.
- A resposta deve usar linguagem técnica correta e frases claras.
- Justifica cada escolha com base no problema e não apenas no nome do conceito.
- Inclui pelo menos um exemplo ou situação prática quando isso ajudar a explicação.

Passo a passo:

1. Lê a situação proposta e identifica os conceitos principais envolvidos.
2. Organiza a resposta em pontos curtos ou pequenos parágrafos.
3. Justifica cada escolha com base no tipo de problema apresentado.
4. Acrescenta um exemplo simples quando isso tornar a explicação mais clara.
5. Revê a resposta para garantir que não ficou vaga ou apenas decorada.

---

<a id="exercicios-19"></a>

## 19 · Funcionalidades de Editor de Texto (Produtividade e Debug)

Fonte: [19_editor_texto_produtividade_e_debug.md](./19_editor_texto_produtividade_e_debug.md)

### Exercício 160 - Atalhos avançados

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Seleciona 15 atalhos do editor e aplica em tarefa real.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 161 - Pipeline local

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Configura build + run num único comando/tarefa no editor.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 162 - Debug guiado

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Coloca breakpoints em função com ciclo e analisa evolução de variáveis.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 163 - Rastreio de bug

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Recebe programa com erro lógico e usa debugger para localizar causa.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 164 - Navegação

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Num projeto com 8+ ficheiros, localiza rapidamente função e todas as referências.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 165 - Refatoração

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Renomeia função globalmente sem quebrar build.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 166 - Extração

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Extrai bloco repetido para função reutilizável.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 167 - Qualidade

Objetivo: consolidar os conceitos de produtividade, organização e debug no editor através de uma explicação escrita e justificada.

Cria checklist final de 12 pontos antes de entregar projeto.

Requisitos:

- Não escrevas um programa completo, exceto se precisares de pequenos exemplos para justificar uma ideia.
- A resposta deve usar linguagem técnica correta e frases claras.
- Justifica cada escolha com base no problema e não apenas no nome do conceito.
- Inclui pelo menos um exemplo ou situação prática quando isso ajudar a explicação.

Passo a passo:

1. Lê a situação proposta e identifica os conceitos principais envolvidos.
2. Organiza a resposta em pontos curtos ou pequenos parágrafos.
3. Justifica cada escolha com base no tipo de problema apresentado.
4. Acrescenta um exemplo simples quando isso tornar a explicação mais clara.
5. Revê a resposta para garantir que não ficou vaga ou apenas decorada.

### Exercício 168 - Métricas pessoais

Objetivo: consolidar os conceitos de produtividade, organização e debug no editor através de uma explicação escrita e justificada.

Regista tempo gasto em tarefa antes e depois de configurar automações.

Requisitos:

- Não escrevas um programa completo, exceto se precisares de pequenos exemplos para justificar uma ideia.
- A resposta deve usar linguagem técnica correta e frases claras.
- Justifica cada escolha com base no problema e não apenas no nome do conceito.
- Inclui pelo menos um exemplo ou situação prática quando isso ajudar a explicação.

Passo a passo:

1. Lê a situação proposta e identifica os conceitos principais envolvidos.
2. Organiza a resposta em pontos curtos ou pequenos parágrafos.
3. Justifica cada escolha com base no tipo de problema apresentado.
4. Acrescenta um exemplo simples quando isso tornar a explicação mais clara.
5. Revê a resposta para garantir que não ficou vaga ou apenas decorada.

### Exercício 169 - Organização

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Reorganiza projeto desestruturado em pastas claras (`src`, `include`, `bin`).

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 170 - Simulação de revisão

Objetivo: praticar uma funcionalidade de editor no contexto de programação em C.

Faz revisão de código de colega usando ferramentas do editor.

Requisitos:

- A atividade deve ser feita num ficheiro ou projeto C realista.
- Regista os passos principais ou configurações aplicadas.
- Confirma o resultado no editor, no terminal ou no debugger, conforme o exercício.
- Evita alterações globais sem verificar antes o impacto no projeto.

Passo a passo:

1. Abre um ficheiro ou projeto adequado para a atividade.
2. Executa a funcionalidade pedida no editor, terminal integrado ou debugger.
3. Observa o resultado e confirma se corresponde ao objetivo do exercício.
4. Corrige configurações ou passos caso o resultado não seja o esperado.
5. Regista uma conclusão curta sobre o que a funcionalidade permite fazer.

### Exercício 171 - Reflexão

Objetivo: consolidar os conceitos de produtividade, organização e debug no editor através de uma explicação escrita e justificada.

Explica como domínio de editor influencia qualidade e aprendizagem em C.

Requisitos:

- Não escrevas um programa completo, exceto se precisares de pequenos exemplos para justificar uma ideia.
- A resposta deve usar linguagem técnica correta e frases claras.
- Justifica cada escolha com base no problema e não apenas no nome do conceito.
- Inclui pelo menos um exemplo ou situação prática quando isso ajudar a explicação.

Passo a passo:

1. Lê a situação proposta e identifica os conceitos principais envolvidos.
2. Organiza a resposta em pontos curtos ou pequenos parágrafos.
3. Justifica cada escolha com base no tipo de problema apresentado.
4. Acrescenta um exemplo simples quando isso tornar a explicação mais clara.
5. Revê a resposta para garantir que não ficou vaga ou apenas decorada.

![Footer](../Images/Footer.png)
