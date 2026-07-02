![Header](../Images/Header.png)

# C (10.º Ano) - Exercícios

---

## Índice de exercícios por módulo

1. [07 · Dados, Variáveis, Declarações, Expressões, Constantes e Tipos](#exercicios-07)
2. [07A · Entrada/Saída Formatada (`printf`/`scanf`) e Endereços (`&` e `*`)](#exercicios-07a)
3. [08 · Operadores em C](#exercicios-08)
4. [09 · Estruturas de Controlo em C](#exercicios-09)
5. [10 · Subprogramas: Funções, Variáveis Locais/Globais e Parâmetros](#exercicios-10)
6. [11 · Funcionalidades de um Editor de Texto](#exercicios-11)
7. [12 · Estruturas de Dados Estáticas: Strings, Arrays e Matrizes](#exercicios-12)
8. [13 · Estruturas de Dados Compostas: `struct`, `union` e constantes simples](#exercicios-13)
9. [14 · Estruturas de Dados Dinâmicas: Apontadores, Acesso e Manipulação](#exercicios-14)

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
    int estado;                // Estado da bicicleta: 0 para disponivel, 1 para ocupada
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

> Resolução:

```c
#include <stdio.h>

int main() {
    int pares[12][2] = {
        {5, 3}, {4, 4}, {2, 9}, {10, 1},
        {7, 8}, {0, 0}, {-3, 2}, {15, 15},
        {6, -1}, {20, 10}, {1, 100}, {-5, -9}
    };

    for (int i = 0; i < 12; i++) {
        int a = pares[i][0];
        int b = pares[i][1];

        printf("Par %d: a = %d, b = %d\n", i + 1, a, b);
        printf("a == b: %d\n", a == b);
        printf("a != b: %d\n", a != b);
        printf("a > b: %d\n", a > b);
        printf("a < b: %d\n", a < b);
        printf("a >= b: %d\n", a >= b);
        printf("a <= b: %d\n\n", a <= b);
    }

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

int main() {
    int idade;
    double nota;

    printf("Idade: ");
    if (scanf("%d", &idade) != 1) {
        printf("Erro: idade invalida.\n");
        return 1;
    }

    printf("Nota: ");
    if (scanf("%lf", &nota) != 1) {
        printf("Erro: nota invalida.\n");
        return 1;
    }

    if (idade >= 18 && nota >= 10) {
        printf("Valido: idade e nota cumprem os requisitos.\n");
    } else {
        printf("Invalido: e necessario ter idade >= 18 e nota >= 10.\n");
    }

    return 0;
}
```

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

> Resolução:

Exemplo de refatoração de condições:

```c
#include <stdio.h>

int main() {
    int idade = 19;
    double nota = 14.5;
    int faltas = 3;
    int tem_autorizacao = 1;
    int saldo = 25;
    int custo = 20;

    int idade_valida = idade >= 18;
    int nota_valida = nota >= 10 && nota <= 20;
    int poucas_faltas = faltas <= 5;
    int pode_comprar = saldo >= custo;
    int pode_entrar = idade_valida || tem_autorizacao;
    int aluno_aprovado = nota_valida && poucas_faltas;

    printf("Idade valida: %d\n", idade_valida);
    printf("Nota valida: %d\n", nota_valida);
    printf("Poucas faltas: %d\n", poucas_faltas);
    printf("Pode comprar: %d\n", pode_comprar);
    printf("Pode entrar: %d\n", pode_entrar);
    printf("Aluno aprovado: %d\n", aluno_aprovado);

    return 0;
}
```

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

> Resolução:

Compreender operadores evita bugs porque muitos erros em C não impedem o programa de compilar, mas alteram o resultado lógico.

Exemplos importantes:

- `=` atribui um valor; `==` compara dois valores.
- `&&` exige que duas condições sejam verdadeiras; `||` exige apenas uma.
- A divisão entre inteiros perde a parte decimal se não houver conversão para `double` ou `float`.
- A precedência dos operadores pode mudar o resultado se faltarem parênteses.

Exemplo:

```c
if (nota >= 10 && faltas <= 5) {
    printf("Aprovado\n");
}
```

Neste caso, o aluno só é aprovado se tiver nota suficiente e poucas faltas. Se fosse usado `||`, bastava uma das condições ser verdadeira, mudando a regra do problema.

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

> Resolução:

```c
#include <stdio.h>

int main() {
    int numero_secreto = 42;
    int palpite;
    int tentativas = 0;
    int acertou = 0;
    int max_tentativas = 5;

    printf("Adivinha o numero secreto entre 1 e 100.\n");

    while (tentativas < max_tentativas && !acertou) {
        printf("Tentativa %d de %d: ", tentativas + 1, max_tentativas);
        if (scanf("%d", &palpite) != 1) {
            printf("Valor invalido.\n");
            return 1;
        }

        tentativas++;

        if (palpite < numero_secreto) {
            printf("Demasiado baixo.\n");
        } else if (palpite > numero_secreto) {
            printf("Demasiado alto.\n");
        } else {
            acertou = 1;
        }
    }

    if (acertou) {
        printf("Vitoria! Acertaste em %d tentativas.\n", tentativas);
    } else {
        printf("Derrota. O numero secreto era %d.\n", numero_secreto);
    }

    return 0;
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

> Resolução:

```c
#include <stdio.h>

#define LINHAS 4
#define COLUNAS 4

int main() {
    int matriz[LINHAS][COLUNAS] = {
        {4, 7, 2, 9},
        {1, 8, 6, 3},
        {5, 10, 12, 0},
        {-2, 11, 14, 6}
    };
    int soma = 0;
    int pares = 0;
    int maior = matriz[0][0];

    for (int linha = 0; linha < LINHAS; linha++) {
        for (int coluna = 0; coluna < COLUNAS; coluna++) {
            int valor = matriz[linha][coluna];
            soma += valor;

            if (valor % 2 == 0) {
                pares++;
            }

            if (valor > maior) {
                maior = valor;
            }
        }
    }

    printf("Soma: %d\n", soma);
    printf("Quantidade de pares: %d\n", pares);
    printf("Maior valor: %d\n", maior);

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

int main() {
    double nota;

    printf("Nota (0 a 20): ");
    if (scanf("%lf", &nota) != 1) {
        printf("Erro: nota invalida.\n");
        return 1;
    }

    while (nota < 0 || nota > 20) {
        printf("Nota fora do intervalo.\n");
        printf("Nota (0 a 20): ");
        if (scanf("%lf", &nota) != 1) {
            printf("Erro: nota invalida.\n");
            return 1;
        }
    }

    printf("Nota aceite: %.2f\n", nota);

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

int main() {
    int opcao;
    double ultima_nota = 0;
    int existe_nota = 0;

    do {
        printf("\n1 - Inserir nota\n");
        printf("2 - Mostrar ultima nota\n");
        printf("3 - Classificar ultima nota\n");
        printf("0 - Sair\n");
        printf("Opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Nota: ");
                scanf("%lf", &ultima_nota);

                if (ultima_nota >= 0 && ultima_nota <= 20) {
                    existe_nota = 1;
                    printf("Nota guardada.\n");
                } else {
                    printf("Nota invalida.\n");
                }
                break;

            case 2:
                if (existe_nota) {
                    printf("Ultima nota: %.2f\n", ultima_nota);
                } else {
                    printf("Ainda nao existe nota.\n");
                }
                break;

            case 3:
                if (!existe_nota) {
                    printf("Ainda nao existe nota.\n");
                } else if (ultima_nota >= 10) {
                    printf("Classificacao: positiva.\n");
                } else {
                    printf("Classificacao: negativa.\n");
                }
                break;

            case 0:
                printf("A sair...\n");
                break;

            default:
                printf("Opcao invalida.\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

int main() {
    double saldo;
    double valor;
    int opcao;

    printf("Saldo inicial: ");
    if (scanf("%lf", &saldo) != 1 || saldo < 0) {
        printf("Saldo inicial invalido.\n");
        return 1;
    }

    do {
        printf("\n1 - Consultar saldo\n");
        printf("2 - Depositar dinheiro\n");
        printf("3 - Levantar dinheiro\n");
        printf("0 - Terminar\n");
        printf("Opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Saldo atual: %.2f euros\n", saldo);
                break;

            case 2:
                printf("Valor a depositar: ");
                scanf("%lf", &valor);

                if (valor > 0) {
                    saldo += valor;
                    printf("Deposito aceite.\n");
                } else {
                    printf("Deposito recusado.\n");
                }
                break;

            case 3:
                printf("Valor a levantar: ");
                scanf("%lf", &valor);

                if (valor > 0 && valor <= saldo) {
                    saldo -= valor;
                    printf("Levantamento aceite.\n");
                } else {
                    printf("Levantamento recusado.\n");
                }
                break;

            case 0:
                printf("Operacao terminada.\n");
                break;

            default:
                printf("Opcao invalida.\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
```

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

> Resolução:

1. Usaria `for`, porque o número de repetições é conhecido: de 1 a 100.
2. Usaria `while`, porque não se sabe quantas tentativas serão necessárias até a palavra-passe estar correta.
3. Usaria `do while`, porque o menu deve aparecer pelo menos uma vez antes de testar a opção.
4. Usaria `while`, porque a leitura termina quando aparece um valor especial (`-999`).
5. Usaria `for`, porque o tamanho do array é conhecido e queremos percorrer todas as posições.
6. Usaria `do while` se a pergunta tiver de ser feita pelo menos uma vez; usaria `while` se a resposta inicial já existir antes do ciclo.

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

> Resolução:

Exemplo de organização em três ficheiros.

`operacoes.h`:

```c
#ifndef OPERACOES_H
#define OPERACOES_H

int somar(int a, int b);
int subtrair(int a, int b);
int multiplicar(int a, int b);

#endif
```

`operacoes.c`:

```c
#include "operacoes.h"

int somar(int a, int b) {
    return a + b;
}

int subtrair(int a, int b) {
    return a - b;
}

int multiplicar(int a, int b) {
    return a * b;
}
```

`main.c`:

```c
#include <stdio.h>
#include "operacoes.h"

int main() {
    int a = 8;
    int b = 4;

    printf("Soma: %d\n", somar(a, b));
    printf("Subtracao: %d\n", subtrair(a, b));
    printf("Multiplicacao: %d\n", multiplicar(a, b));

    return 0;
}
```

Compilação:

```bash
cc main.c operacoes.c -o programa
```

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

> Resolução:

```c
#include <stdio.h>

int total_chamadas = 0;

void mostrar_mensagem() {
    total_chamadas++;
    printf("Funcao chamada. Total: %d\n", total_chamadas);
}

int main() {
    mostrar_mensagem();
    mostrar_mensagem();
    mostrar_mensagem();

    printf("A funcao foi chamada %d vezes.\n", total_chamadas);

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

double ler_numero() {
    double numero;

    printf("Numero: ");
    scanf("%lf", &numero);

    return numero;
}

char ler_operador() {
    char operador;

    printf("Operador (+, -, *, /): ");
    scanf(" %c", &operador);

    return operador;
}

double calcular(double a, double b, char operador) {
    if (operador == '+') {
        return a + b;
    }

    if (operador == '-') {
        return a - b;
    }

    if (operador == '*') {
        return a * b;
    }

    if (operador == '/' && b != 0) {
        return a / b;
    }

    return 0;
}

int operador_valido(char operador, double b) {
    if (operador == '+' || operador == '-' || operador == '*') {
        return 1;
    }

    if (operador == '/' && b != 0) {
        return 1;
    }

    return 0;
}

void mostrar_resultado(double resultado) {
    printf("Resultado: %.2f\n", resultado);
}

int main() {
    double a = ler_numero();
    double b = ler_numero();
    char operador = ler_operador();

    if (operador_valido(operador, b)) {
        mostrar_resultado(calcular(a, b, operador));
    } else {
        printf("Operacao invalida.\n");
    }

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

int nota_valida(double nota) {
    return nota >= 0 && nota <= 20;
}

double calcular_media(double a, double b, double c) {
    return (a + b + c) / 3.0;
}

int aluno_aprovado(double media) {
    return media >= 10;
}

void mostrar_resultado(double media) {
    printf("Media: %.2f\n", media);

    if (aluno_aprovado(media)) {
        printf("Resultado: aprovado\n");
    } else {
        printf("Resultado: reprovado\n");
    }
}

int main() {
    double nota1, nota2, nota3;

    printf("Nota 1: ");
    scanf("%lf", &nota1);
    printf("Nota 2: ");
    scanf("%lf", &nota2);
    printf("Nota 3: ");
    scanf("%lf", &nota3);

    if (!nota_valida(nota1) || !nota_valida(nota2) || !nota_valida(nota3)) {
        printf("Existe pelo menos uma nota invalida.\n");
        return 1;
    }

    mostrar_resultado(calcular_media(nota1, nota2, nota3));

    return 0;
}
```

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

> Resolução:

Usa-se `return` quando a função precisa de devolver um único resultado principal.

Exemplo:

```c
int dobro(int numero) {
    return numero * 2;
}
```

Usa-se parâmetro por ponteiro quando a função precisa de alterar uma variável que existe fora dela, ou quando precisa de devolver mais do que um resultado.

Exemplo:

```c
void trocar(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
```

Neste caso, se os parâmetros não fossem ponteiros, a função só alterava cópias locais. Com ponteiros, a função altera as variáveis originais.

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

> Resolução:

1. Abrir as definições do editor.
2. Ativar a visualização de linha e coluna na barra de estado.
3. Definir indentação com 4 espaços.
4. Criar ou abrir um ficheiro `main.c`.
5. Escrever um pequeno programa e confirmar que os blocos ficam alinhados com 4 espaços.

Conclusão: a linha, a coluna e a indentação ajudam a localizar erros e tornam o código mais legível.

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

> Resolução:

Atalhos praticados:

1. Guardar ficheiro.
2. Abrir ficheiro.
3. Fechar ficheiro.
4. Copiar linha.
5. Cortar linha.
6. Colar.
7. Desfazer.
8. Refazer.
9. Procurar texto.
10. Substituir texto.
11. Comentar linha.
12. Abrir terminal integrado.

Conclusão: os atalhos reduzem tarefas repetitivas e deixam mais atenção disponível para pensar no código.

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

> Resolução:

1. Abrir o projeto no editor.
2. Usar a pesquisa global.
3. Procurar o nome da função, por exemplo `calcular_media`.
4. Confirmar onde a função é declarada, implementada e chamada.
5. Abrir cada resultado e verificar se a ocorrência pertence mesmo à função procurada.

Conclusão: a pesquisa global permite perceber rapidamente onde uma função é usada num projeto.

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

> Resolução:

1. Escolher uma variável com nome pouco claro, por exemplo `n`.
2. Confirmar o seu escopo antes de renomear.
3. Usar a opção de renomear símbolo, se existir.
4. Se for usada substituição manual, confirmar cada ocorrência antes de substituir.
5. Compilar o programa depois da alteração.

Conclusão: renomear com cuidado evita alterar texto parecido que não pertence à mesma variável.

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

> Resolução:

1. Criar ou abrir um projeto com `main.c`, `operacoes.c` e `operacoes.h`.
2. No `main.c`, clicar numa chamada como `somar(a, b)`.
3. Usar "go to definition".
4. Confirmar que o editor abre a implementação da função em `operacoes.c` ou a declaração em `operacoes.h`.
5. Voltar ao ficheiro anterior usando o atalho de navegação do editor.

Conclusão: navegar entre `.h` e `.c` ajuda a perceber a ligação entre interface e implementação.

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

> Resolução:

1. Abrir um ficheiro C com indentação irregular.
2. Aplicar a opção de formatar documento.
3. Confirmar se os blocos `if`, `for`, `while` e funções ficaram alinhados.
4. Ajustar manualmente algum ponto que o formatador não tenha resolvido bem.
5. Compilar para garantir que a formatação não alterou a lógica.

Conclusão: a formatação torna o código mais fácil de ler, mas não substitui a revisão do programador.

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

> Resolução:

Comandos usados no terminal integrado:

```bash
cc main.c -o programa
./programa
```

Se o programa tiver avisos, compilar com:

```bash
cc -Wall -Wextra -pedantic main.c -o programa
```

Conclusão: o terminal integrado permite compilar, executar e corrigir erros sem sair do editor.

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

> Resolução:

1. Abrir a configuração de tarefas do editor.
2. Criar uma tarefa de build.
3. Definir o comando de compilação, por exemplo `cc main.c -o programa`.
4. Executar a tarefa.
5. Confirmar no terminal integrado se o executável foi criado.

Conclusão: uma tarefa de build evita repetir sempre o mesmo comando manualmente.

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

> Resolução:

1. Criar um programa com um ciclo `for`.
2. Colocar um breakpoint dentro do ciclo.
3. Iniciar o debug.
4. Observar o valor da variável de controlo a cada paragem.
5. Avançar passo a passo até perceber como o valor muda.

Conclusão: o breakpoint permite ver o programa a executar devagar e confirmar o valor real das variáveis.

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

> Resolução:

1. Escolher um bloco de código repetido, por exemplo cálculo de média.
2. Criar uma função com nome claro, como `calcular_media`.
3. Mover o bloco para dentro da função.
4. Substituir o bloco antigo por uma chamada à função.
5. Compilar e testar para confirmar que o resultado é o mesmo.

Conclusão: extrair uma função reduz repetição e dá nomes claros às responsabilidades do programa.

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

> Resolução:

Exemplo de registo:

```text
Tarefa: comentar 10 linhas e compilar o programa.
Sem atalhos: 3 minutos e 20 segundos.
Com atalhos: 1 minuto e 40 segundos.
Diferença: menos 1 minuto e 40 segundos.
```

Conclusão: atalhos simples podem reduzir o tempo gasto em tarefas repetitivas, especialmente em projetos maiores.

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

> Resolução:

Um editor bem usado melhora a aprendizagem porque reduz distrações técnicas e ajuda o aluno a perceber melhor o código.

Exemplos:

- a indentação mostra visualmente onde começa e termina cada bloco;
- a pesquisa ajuda a encontrar funções e variáveis rapidamente;
- o terminal integrado aproxima compilação, execução e correção;
- o debug permite observar variáveis passo a passo;
- a formatação torna os erros de estrutura mais fáceis de encontrar.

Para iniciantes, isto é importante porque muitos erros aparecem por distração: chavetas mal alinhadas, nomes trocados, ficheiros errados ou comandos de compilação repetidos incorretamente.

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

> Resolução:

```c
#include <stdio.h>

#define TOTAL 20

int main() {
    int valores[TOTAL];
    int soma = 0;
    int maximo;
    int minimo;
    double media;

    for (int i = 0; i < TOTAL; i++) {
        printf("Valor %d: ", i + 1);
        scanf("%d", &valores[i]);
    }

    maximo = valores[0];
    minimo = valores[0];

    for (int i = 0; i < TOTAL; i++) {
        soma += valores[i];

        if (valores[i] > maximo) {
            maximo = valores[i];
        }

        if (valores[i] < minimo) {
            minimo = valores[i];
        }
    }

    media = (double)soma / TOTAL;

    printf("Soma: %d\n", soma);
    printf("Media: %.2f\n", media);
    printf("Maximo: %d\n", maximo);
    printf("Minimo: %d\n", minimo);

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

#define TOTAL 12

int main() {
    int valores[TOTAL];
    int pares = 0;
    int impares = 0;

    for (int i = 0; i < TOTAL; i++) {
        printf("Valor %d: ", i + 1);
        scanf("%d", &valores[i]);
    }

    printf("Valores pares: ");

    for (int i = 0; i < TOTAL; i++) {
        if (valores[i] % 2 == 0) {
            pares++;
            printf("%d ", valores[i]);
        } else {
            impares++;
        }
    }

    printf("\nTotal de pares: %d\n", pares);
    printf("Total de impares: %d\n", impares);

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

#define TOTAL 8

int calcular_soma(int valores[], int tamanho);

int main() {
    int valores[TOTAL];
    int soma;

    for (int i = 0; i < TOTAL; i++) {
        printf("Valor %d: ", i + 1);
        scanf("%d", &valores[i]);
    }

    soma = calcular_soma(valores, TOTAL);
    printf("Soma: %d\n", soma);

    return 0;
}

int calcular_soma(int valores[], int tamanho) {
    int soma = 0;

    for (int i = 0; i < tamanho; i++) {
        soma += valores[i];
    }

    return soma;
}
```

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

> Resolução:

```c
#include <stdio.h>
#include <string.h>

#define TAMANHO 30

int main() {
    char palavra1[TAMANHO];
    char palavra2[TAMANHO];

    printf("Primeira palavra: ");
    scanf("%29s", palavra1);

    printf("Segunda palavra: ");
    scanf("%29s", palavra2);

    if (strcmp(palavra1, palavra2) == 0) {
        printf("As palavras sao iguais.\n");
    } else {
        printf("As palavras sao diferentes.\n");
    }

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>
#include <string.h>

#define TAM_NOME 30
#define TAM_COMPLETO 70

int main() {
    char primeiro_nome[TAM_NOME];
    char apelido[TAM_NOME];
    char nome_completo[TAM_COMPLETO];

    printf("Primeiro nome: ");
    scanf("%29s", primeiro_nome);

    printf("Apelido: ");
    scanf("%29s", apelido);

    strcpy(nome_completo, primeiro_nome);
    strcat(nome_completo, " ");
    strcat(nome_completo, apelido);

    printf("Nome completo: %s\n", nome_completo);

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>
#include <string.h>

#define TOTAL_ALUNOS 5
#define TAM_NOME 50

int main() {
    char nomes[TOTAL_ALUNOS][TAM_NOME];

    for (int i = 0; i < TOTAL_ALUNOS; i++) {
        printf("Nome do aluno %d: ", i + 1);
        fgets(nomes[i], TAM_NOME, stdin);
        nomes[i][strcspn(nomes[i], "\n")] = '\0';
    }

    printf("\nLista de alunos:\n");

    for (int i = 0; i < TOTAL_ALUNOS; i++) {
        printf("%d. %s\n", i + 1, nomes[i]);
    }

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

#define LINHAS 3
#define COLUNAS 3

int main() {
    int matriz[LINHAS][COLUNAS];
    int soma = 0;

    for (int linha = 0; linha < LINHAS; linha++) {
        for (int coluna = 0; coluna < COLUNAS; coluna++) {
            printf("Valor [%d][%d]: ", linha, coluna);
            scanf("%d", &matriz[linha][coluna]);
            soma += matriz[linha][coluna];
        }
    }

    printf("\nMatriz:\n");

    for (int linha = 0; linha < LINHAS; linha++) {
        for (int coluna = 0; coluna < COLUNAS; coluna++) {
            printf("%4d", matriz[linha][coluna]);
        }
        printf("\n");
    }

    printf("Soma total: %d\n", soma);

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

#define TAMANHO 3

int main() {
    int matriz[TAMANHO][TAMANHO];
    int soma_diagonal = 0;

    for (int linha = 0; linha < TAMANHO; linha++) {
        for (int coluna = 0; coluna < TAMANHO; coluna++) {
            printf("Valor [%d][%d]: ", linha, coluna);
            scanf("%d", &matriz[linha][coluna]);
        }
    }

    for (int i = 0; i < TAMANHO; i++) {
        soma_diagonal += matriz[i][i];
    }

    printf("Soma da diagonal principal: %d\n", soma_diagonal);

    for (int linha = 0; linha < TAMANHO; linha++) {
        int soma_linha = 0;

        for (int coluna = 0; coluna < TAMANHO; coluna++) {
            soma_linha += matriz[linha][coluna];
        }

        printf("Soma da linha %d: %d\n", linha + 1, soma_linha);
    }

    for (int coluna = 0; coluna < TAMANHO; coluna++) {
        int soma_coluna = 0;

        for (int linha = 0; linha < TAMANHO; linha++) {
            soma_coluna += matriz[linha][coluna];
        }

        printf("Soma da coluna %d: %d\n", coluna + 1, soma_coluna);
    }

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

#define TOTAL 10

int main() {
    int valores[TOTAL];

    for (int i = 0; i < TOTAL; i++) {
        printf("Valor %d: ", i + 1);
        scanf("%d", &valores[i]);
    }

    printf("Array original: ");
    for (int i = 0; i < TOTAL; i++) {
        printf("%d ", valores[i]);
    }
    printf("\n");

    for (int i = 0; i < TOTAL - 1; i++) {
        for (int j = 0; j < TOTAL - 1 - i; j++) {
            if (valores[j] > valores[j + 1]) {
                int temp = valores[j];
                valores[j] = valores[j + 1];
                valores[j + 1] = temp;
            }
        }
    }

    printf("Array ordenado: ");
    for (int i = 0; i < TOTAL; i++) {
        printf("%d ", valores[i]);
    }
    printf("\n");

    return 0;
}
```

Explicação:

Um array estático é suficiente quando sabemos, antes de executar o programa, quantos elementos precisamos de guardar. Por exemplo, uma matriz 3x3 ou um vetor com 10 notas.

Uma estrutura dinâmica é mais adequada quando o tamanho pode variar durante a execução. Por exemplo, se o utilizador indicar quantos valores quer inserir, podemos reservar memória com `malloc`.

---

<a id="exercicios-13"></a>

## 13 · Estruturas de Dados Compostas: `struct`, `union` e constantes simples

Fonte: [13_estruturas_compostas_struct_union_enum.md](./13_estruturas_compostas_struct_union_enum.md)

Ordem recomendada: resolver por sequência, do 82 ao 93. Os exercícios 82 a 87 devem consolidar bem `struct` antes de avançares para constantes com nome, apontadores e `union`.

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

> Resolução:

```c
#include <stdio.h>

typedef struct {
    char titulo[100];
    char autor[50];
    int ano;
    double preco;
    int disponivel;
} Livro;

int main() {
    Livro livro = {"Os Maias", "Eca de Queiros", 1888, 12.50, 1};

    printf("Titulo: %s\n", livro.titulo);
    printf("Autor: %s\n", livro.autor);
    printf("Ano: %d\n", livro.ano);
    printf("Preco: %.2f\n", livro.preco);

    if (livro.disponivel) {
        printf("Disponibilidade: disponivel\n");
    } else {
        printf("Disponibilidade: indisponivel\n");
    }

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

#define TOTAL_LIVROS 5

typedef struct {
    char titulo[100];
    char autor[50];
    int ano;
    double preco;
} Livro;

int main() {
    Livro livros[TOTAL_LIVROS] = {
        {"Livro A", "Autor A", 2019, 10.0},
        {"Livro B", "Autor B", 2021, 12.5},
        {"Livro C", "Autor C", 2023, 15.0},
        {"Livro D", "Autor D", 2020, 8.0},
        {"Livro E", "Autor E", 2024, 20.0}
    };
    int encontrados = 0;

    for (int i = 0; i < TOTAL_LIVROS; i++) {
        if (livros[i].ano > 2020) {
            printf("%s, %s, %d\n", livros[i].titulo, livros[i].autor, livros[i].ano);
            encontrados++;
        }
    }

    if (encontrados == 0) {
        printf("Nenhum livro encontrado.\n");
    } else {
        printf("Total encontrado: %d\n", encontrados);
    }

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

typedef struct {
    int codigo;
    char nome[50];
    double preco;
    int stock;
} Produto;

void mostrar_produto(Produto produto);

int main() {
    Produto p1 = {101, "Caneta", 1.20, 30};
    Produto p2 = {102, "Caderno", 2.50, 15};

    mostrar_produto(p1);
    mostrar_produto(p2);

    return 0;
}

void mostrar_produto(Produto produto) {
    printf("Codigo: %d | Nome: %s | Preco: %.2f | Stock: %d\n",
           produto.codigo, produto.nome, produto.preco, produto.stock);
}
```

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

> Resolução:

```c
#include <stdio.h>
#include <string.h>

#define TOTAL_ALUNOS 5

typedef struct {
    int numero;
    char nome[50];
    double media;
} Aluno;

int main() {
    Aluno turma[TOTAL_ALUNOS];
    double soma = 0;
    int validas = 0;

    for (int i = 0; i < TOTAL_ALUNOS; i++) {
        printf("Numero do aluno %d: ", i + 1);
        scanf("%d", &turma[i].numero);
        getchar();

        printf("Nome: ");
        fgets(turma[i].nome, sizeof turma[i].nome, stdin);
        turma[i].nome[strcspn(turma[i].nome, "\n")] = '\0';

        printf("Media: ");
        scanf("%lf", &turma[i].media);

        if (turma[i].media >= 0 && turma[i].media <= 20) {
            soma += turma[i].media;
            validas++;
        } else {
            printf("Media invalida. Este valor nao entra no calculo.\n");
        }
    }

    if (validas > 0) {
        printf("Media da turma: %.2f\n", soma / validas);
    } else {
        printf("Nao existem medias validas.\n");
    }

    printf("Alunos com media positiva:\n");
    for (int i = 0; i < TOTAL_ALUNOS; i++) {
        if (turma[i].media >= 10 && turma[i].media <= 20) {
            printf("%d - %s - %.2f\n", turma[i].numero, turma[i].nome, turma[i].media);
        }
    }

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

#define TOTAL_ALUNOS 5

typedef struct {
    int numero;
    char nome[50];
    double media;
} Aluno;

int main() {
    Aluno turma[TOTAL_ALUNOS] = {
        {101, "Ana", 16.5},
        {102, "Bruno", 9.5},
        {103, "Carla", 18.0},
        {104, "Diogo", 12.0},
        {105, "Eva", 14.5}
    };
    int numero;
    int encontrado = 0;
    int posicao = -1;

    printf("Numero a pesquisar: ");
    scanf("%d", &numero);

    for (int i = 0; i < TOTAL_ALUNOS; i++) {
        if (turma[i].numero == numero) {
            encontrado = 1;
            posicao = i;
            break;
        }
    }

    if (encontrado) {
        printf("Aluno encontrado na posicao %d.\n", posicao + 1);
        printf("%d - %s - %.2f\n",
               turma[posicao].numero, turma[posicao].nome, turma[posicao].media);
    } else {
        printf("Aluno nao encontrado.\n");
    }

    return 0;
}
```

### Exercício 88 - Constantes para valores com nome

Objetivo: usar constantes com nome para substituir números mágicos por nomes claros.

Define constantes para os dias úteis e cria um programa que lê um número de 1 a 5 e mostra o nome do dia correspondente.

Requisitos:

- As constantes devem ter nomes como `SEGUNDA`, `TERCA`, `QUARTA`, `QUINTA`, `SEXTA`.
- Usa valores explícitos, por exemplo `#define SEGUNDA 1`, para coincidir com o input do utilizador.
- O número lido pelo utilizador deve ser validado.
- Se o número estiver fora de 1 a 5, mostra erro.
- Usa `switch` ou `if/else if` para mostrar o texto do dia.
- No código principal, evita usar números sem significado para representar dias.

Passo a passo:

1. Define as constantes dos dias úteis.
2. Lê um número entre 1 e 5.
3. Guarda esse número numa variável.
4. Mostra o dia usando os nomes das constantes.
5. Testa com `1`, `5` e um valor inválido como `9`.

> Resolução:

```c
#include <stdio.h>

#define SEGUNDA 1
#define TERCA 2
#define QUARTA 3
#define QUINTA 4
#define SEXTA 5

int main(void) {
    int numero;
    int dia;

    printf("Dia util (1 a 5): ");
    scanf("%d", &numero);

    if (numero < SEGUNDA || numero > SEXTA) {
        printf("Dia invalido.\n");
        return 1;
    }

    dia = numero;

    switch (dia) {
        case SEGUNDA:
            printf("Segunda-feira\n");
            break;
        case TERCA:
            printf("Terca-feira\n");
            break;
        case QUARTA:
            printf("Quarta-feira\n");
            break;
        case QUINTA:
            printf("Quinta-feira\n");
            break;
        case SEXTA:
            printf("Sexta-feira\n");
            break;
    }

    return 0;
}
```

### Exercício 89 - `struct` com estado numérico

Objetivo: representar o estado de uma entidade com constantes dentro de uma `struct`.

Cria uma `struct Pedido` com código, nome do cliente, total e estado. O estado deve usar constantes como `PENDENTE`, `ENVIADO` e `ENTREGUE`.

Requisitos:

- Usa constantes com nome para o estado.
- Usa `typedef struct` para o pedido.
- Cria pelo menos 3 pedidos num array.
- Mostra apenas os pedidos que ainda não foram entregues.
- Ao imprimir o estado, mostra texto legível e não apenas o valor numérico.
- Não uses `0`, `1` e `2` diretamente no código principal para comparar estados.

Passo a passo:

1. Define as constantes `PENDENTE`, `ENVIADO` e `ENTREGUE`.
2. Define `Pedido`.
3. Inicializa um array com 3 pedidos.
4. Percorre o array.
5. Se o estado for diferente de `ENTREGUE`, mostra o pedido.
6. Cria uma função auxiliar, se quiseres, para converter o estado em texto.

> Resolução:

```c
#include <stdio.h>

#define TOTAL_PEDIDOS 3
#define PENDENTE 1
#define ENVIADO 2
#define ENTREGUE 3

typedef struct {
    int codigo;
    char cliente[50];
    double total;
    int estado;
} Pedido;

const char *estado_texto(int estado) {
    if (estado == PENDENTE) {
        return "pendente";
    }

    if (estado == ENVIADO) {
        return "enviado";
    }

    return "entregue";
}

int main(void) {
    Pedido pedidos[TOTAL_PEDIDOS] = {
        {1, "Ana", 25.0, PENDENTE},
        {2, "Bruno", 40.5, ENVIADO},
        {3, "Carla", 15.0, ENTREGUE}
    };

    for (int i = 0; i < TOTAL_PEDIDOS; i++) {
        if (pedidos[i].estado != ENTREGUE) {
            printf("%d - %s - %.2f - %s\n",
                   pedidos[i].codigo,
                   pedidos[i].cliente,
                   pedidos[i].total,
                   estado_texto(pedidos[i].estado));
        }
    }

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

typedef struct {
    int dia;
    int mes;
    int ano;
} Data;

typedef struct {
    int numero;
    char nome[50];
    double media;
    Data nascimento;
} Aluno;

int main() {
    Aluno aluno = {101, "Ana Silva", 15.5, {12, 5, 2008}};

    if (aluno.nascimento.dia < 1 || aluno.nascimento.dia > 31 ||
        aluno.nascimento.mes < 1 || aluno.nascimento.mes > 12) {
        printf("Data invalida.\n");
        return 1;
    }

    printf("Numero: %d\n", aluno.numero);
    printf("Nome: %s\n", aluno.nome);
    printf("Media: %.2f\n", aluno.media);
    printf("Nascimento: %d/%d/%d\n",
           aluno.nascimento.dia,
           aluno.nascimento.mes,
           aluno.nascimento.ano);

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>

typedef struct {
    int codigo;
    char nome[50];
    double preco;
    int stock;
} Produto;

int atualizar_stock(Produto *produto, int novo_stock);
void mostrar_produto(Produto produto);

int main() {
    Produto produto = {101, "Rato", 12.99, 5};

    mostrar_produto(produto);

    if (atualizar_stock(&produto, 10)) {
        printf("Stock atualizado.\n");
    } else {
        printf("Stock invalido.\n");
    }

    mostrar_produto(produto);

    if (!atualizar_stock(&produto, -3)) {
        printf("Tentativa invalida recusada.\n");
    }

    mostrar_produto(produto);

    return 0;
}

int atualizar_stock(Produto *produto, int novo_stock) {
    if (novo_stock < 0) {
        return 0;
    }

    produto->stock = novo_stock;
    return 1;
}

void mostrar_produto(Produto produto) {
    printf("%d - %s - %.2f - stock: %d\n",
           produto.codigo, produto.nome, produto.preco, produto.stock);
}
```

### Exercício 92 - `union` com indicação do tipo ativo

Objetivo: compreender que uma `union` guarda valores alternativos, mas só um campo deve ser considerado válido de cada vez.

Cria um tipo `Dado` que pode guardar um valor inteiro ou um valor real. Usa constantes para indicar qual dos campos da `union` está ativo.

Requisitos:

- Define constantes `DADO_INTEIRO` e `DADO_REAL`.
- Define uma `union Valor` com `int inteiro` e `float real`.
- Define uma `struct Dado` com dois campos: `tipo` e `valor`.
- Cria um exemplo de `Dado` inteiro e outro de `Dado` real.
- Ao imprimir, consulta primeiro o campo `tipo`.
- Não leias um campo da `union` diferente daquele indicado pelo `tipo`.

Passo a passo:

1. Define as constantes do tipo de dado.
2. Define `Valor`.
3. Define `Dado`.
4. Cria `Dado a` com tipo inteiro.
5. Cria `Dado b` com tipo real.
6. Escreve uma função `mostrar_dado(Dado dado)`.
7. Dentro da função, usa `if` ou `switch` para imprimir o campo correto da `union`.

> Resolução:

```c
#include <stdio.h>

#define DADO_INTEIRO 1
#define DADO_REAL 2

typedef union {
    int inteiro;
    float real;
} Valor;

typedef struct {
    int tipo;
    Valor valor;
} Dado;

void mostrar_dado(Dado dado);

int main(void) {
    Dado a;
    Dado b;

    a.tipo = DADO_INTEIRO;
    a.valor.inteiro = 10;

    b.tipo = DADO_REAL;
    b.valor.real = 12.5f;

    mostrar_dado(a);
    mostrar_dado(b);

    return 0;
}

void mostrar_dado(Dado dado) {
    if (dado.tipo == DADO_INTEIRO) {
        printf("Inteiro: %d\n", dado.valor.inteiro);
    } else {
        printf("Real: %.2f\n", dado.valor.real);
    }
}
```

### Exercício 93 - Reflexão

Objetivo: consolidar os conceitos de `struct`, `union` e constantes com nome através de uma explicação escrita e justificada.

Explica porque `struct`, constantes com nome e `union` não resolvem o mesmo problema.

Requisitos:

- Não escrevas um programa completo, exceto se precisares de pequenos exemplos para justificar uma ideia.
- A resposta deve usar linguagem técnica correta e frases claras.
- Justifica cada escolha com base no problema e não apenas no nome do conceito.
- Inclui pelo menos um exemplo ou situação prática quando isso ajudar a explicação.
- Refere explicitamente qual destes conceitos será mais comum nos teus primeiros programas em C.

Passo a passo:

1. Explica para que serve uma `struct`.
2. Explica para que servem constantes com nome.
3. Explica para que serve uma `union`.
4. Dá um exemplo de problema real adequado a cada conceito.
5. Compara `struct` e `union`, destacando que na `struct` os campos coexistem e na `union` partilham memória.
6. Termina com uma conclusão curta sobre porque `struct` e constantes simples aparecem mais cedo e com mais frequência em programas simples.

> Resolução:

`struct`, constantes com nomes e `union` resolvem problemas diferentes.

Uma `struct` agrupa vários dados que pertencem à mesma entidade. Por exemplo, um `Aluno` pode ter número, nome e média ao mesmo tempo. Todos estes campos existem em simultâneo.

Podemos usar constantes com nomes para representar estados. Por exemplo, `#define PENDENTE 1`, `#define ENVIADO 2` e `#define ENTREGUE 3`. Isto é mais claro do que escrever `1`, `2` e `3` diretamente no código.

Uma `union` permite guardar valores alternativos no mesmo espaço de memória. Por exemplo, um dado pode ser inteiro ou real, mas só um desses campos deve ser considerado válido de cada vez.

Nos primeiros programas em C, `struct` e constantes simples costumam ser suficientes para organizar dados e estados. `union` é mais específica e exige mais cuidado, porque os campos partilham memória.

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

> Resolução:

```c
#include <stdio.h>

int main() {
    int numeros[5] = {10, 20, 30, 40, 50};
    int *p_numeros = numeros;

    printf("Valor usando numeros[0]: %d\n", numeros[0]);
    printf("Valor usando *p_numeros: %d\n", *p_numeros);
    printf("Endereco usando &numeros[0]: %p\n", (void *)&numeros[0]);
    printf("Endereco usando p_numeros: %p\n", (void *)p_numeros);

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *proximo;
} No;

int main() {
    No *primeiro = malloc(sizeof *primeiro);
    No *segundo = malloc(sizeof *segundo);
    No *terceiro = malloc(sizeof *terceiro);

    if (primeiro == NULL || segundo == NULL || terceiro == NULL) {
        printf("Erro na reserva de memoria.\n");
        free(primeiro);
        free(segundo);
        free(terceiro);
        return 1;
    }

    primeiro->valor = 10;
    segundo->valor = 20;
    terceiro->valor = 30;

    primeiro->proximo = segundo;
    segundo->proximo = terceiro;
    terceiro->proximo = NULL;

    printf("%d -> %d -> %d -> NULL\n",
           primeiro->valor, segundo->valor, terceiro->valor);

    free(primeiro);
    free(segundo);
    free(terceiro);

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *proximo;
} No;

void mostrar_lista(const No *inicio) {
    const No *atual = inicio;

    while (atual != NULL) {
        printf("%d -> ", atual->valor);
        atual = atual->proximo;
    }

    printf("NULL\n");
}

int main() {
    No *lista = NULL;
    No *n1 = malloc(sizeof *n1);
    No *n2 = malloc(sizeof *n2);
    No *n3 = malloc(sizeof *n3);

    mostrar_lista(lista);

    if (n1 == NULL || n2 == NULL || n3 == NULL) {
        printf("Erro na reserva de memoria.\n");
        free(n1);
        free(n2);
        free(n3);
        return 1;
    }

    n1->valor = 10;
    n2->valor = 20;
    n3->valor = 30;

    n1->proximo = n2;
    n2->proximo = n3;
    n3->proximo = NULL;

    lista = n1;
    mostrar_lista(lista);

    free(n1);
    free(n2);
    free(n3);

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *proximo;
} No;

int contar_nos(const No *inicio) {
    int total = 0;
    const No *atual = inicio;

    while (atual != NULL) {
        total++;
        atual = atual->proximo;
    }

    return total;
}

int main() {
    No *n1 = malloc(sizeof *n1);
    No *n2 = malloc(sizeof *n2);
    No *n3 = malloc(sizeof *n3);

    if (n1 == NULL || n2 == NULL || n3 == NULL) {
        free(n1);
        free(n2);
        free(n3);
        return 1;
    }

    n1->valor = 10;
    n2->valor = 20;
    n3->valor = 30;
    n1->proximo = n2;
    n2->proximo = n3;
    n3->proximo = NULL;

    printf("Total de nos: %d\n", contar_nos(n1));

    free(n1);
    free(n2);
    free(n3);

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *proximo;
} No;

int contem_valor(const No *inicio, int valor) {
    const No *atual = inicio;

    while (atual != NULL) {
        if (atual->valor == valor) {
            return 1;
        }

        atual = atual->proximo;
    }

    return 0;
}

int main() {
    No *n1 = malloc(sizeof *n1);
    No *n2 = malloc(sizeof *n2);

    if (n1 == NULL || n2 == NULL) {
        free(n1);
        free(n2);
        return 1;
    }

    n1->valor = 10;
    n2->valor = 20;
    n1->proximo = n2;
    n2->proximo = NULL;

    if (contem_valor(n1, 20)) {
        printf("O valor 20 existe.\n");
    } else {
        printf("O valor 20 nao existe.\n");
    }

    if (contem_valor(n1, 99)) {
        printf("O valor 99 existe.\n");
    } else {
        printf("O valor 99 nao existe.\n");
    }

    free(n1);
    free(n2);

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *proximo;
} No;

No *inserir_inicio(No *inicio, int valor) {
    No *novo = malloc(sizeof *novo);

    if (novo == NULL) {
        return inicio;
    }

    novo->valor = valor;
    novo->proximo = inicio;

    return novo;
}

void mostrar_lista(const No *inicio) {
    const No *atual = inicio;

    while (atual != NULL) {
        printf("%d -> ", atual->valor);
        atual = atual->proximo;
    }

    printf("NULL\n");
}

void libertar_lista(No *inicio) {
    No *atual = inicio;

    while (atual != NULL) {
        No *seguinte = atual->proximo;
        free(atual);
        atual = seguinte;
    }
}

int main() {
    No *lista = NULL;

    lista = inserir_inicio(lista, 30);
    lista = inserir_inicio(lista, 20);
    lista = inserir_inicio(lista, 10);

    mostrar_lista(lista);
    libertar_lista(lista);
    lista = NULL;

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *proximo;
} No;

No *inserir_fim(No *inicio, int valor) {
    No *novo = malloc(sizeof *novo);

    if (novo == NULL) {
        return inicio;
    }

    novo->valor = valor;
    novo->proximo = NULL;

    if (inicio == NULL) {
        return novo;
    }

    No *atual = inicio;

    while (atual->proximo != NULL) {
        atual = atual->proximo;
    }

    atual->proximo = novo;

    return inicio;
}

void mostrar_lista(const No *inicio) {
    const No *atual = inicio;

    while (atual != NULL) {
        printf("%d -> ", atual->valor);
        atual = atual->proximo;
    }

    printf("NULL\n");
}

void libertar_lista(No *inicio) {
    No *atual = inicio;

    while (atual != NULL) {
        No *seguinte = atual->proximo;
        free(atual);
        atual = seguinte;
    }
}

int main() {
    No *lista = NULL;

    lista = inserir_fim(lista, 10);
    lista = inserir_fim(lista, 20);
    lista = inserir_fim(lista, 30);

    mostrar_lista(lista);
    libertar_lista(lista);
    lista = NULL;

    return 0;
}
```

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

> Resolução:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *proximo;
} No;

No *inserir_inicio(No *inicio, int valor) {
    No *novo = malloc(sizeof *novo);

    if (novo == NULL) {
        return inicio;
    }

    novo->valor = valor;
    novo->proximo = inicio;

    return novo;
}

void libertar_lista(No *inicio) {
    No *atual = inicio;

    while (atual != NULL) {
        No *seguinte = atual->proximo;
        free(atual);
        atual = seguinte;
    }
}

int main() {
    No *lista = NULL;

    lista = inserir_inicio(lista, 30);
    lista = inserir_inicio(lista, 20);
    lista = inserir_inicio(lista, 10);

    libertar_lista(lista);
    lista = NULL;

    printf("Lista libertada.\n");

    return 0;
}
```

### Exercício 112 - Inventário de equipamentos com lista ligada

Objetivo: aplicar listas ligadas a um problema, usando inserção, procura, remoção e libertação de memória.

Cria um programa que gere o inventário de equipamentos de uma sala ou laboratório. Cada equipamento deve ficar guardado num nó de uma lista ligada simples.

Requisitos:

- Define uma estrutura `Equipamento` com os campos `codigo`, `nome` e `estado`.
- Define uma estrutura `NoEquipamento` com os campos `equipamento` e `proximo`.
- Usa `char nome[50]` para guardar o nome do equipamento.
- Usa `char estado[20]` para guardar valores como `"disponivel"` ou `"avariado"`.
- Cria a função `Equipamento criar_equipamento(int codigo, const char nome[], const char estado[])`.
- Cria a função `NoEquipamento *criar_no_equipamento(Equipamento equipamento)`.
- Cria a função `NoEquipamento *inserir_fim(NoEquipamento *inicio, Equipamento equipamento)`.
- Cria a função `NoEquipamento *procurar_equipamento(NoEquipamento *inicio, int codigo)`.
- Cria a função `int existe_codigo(const NoEquipamento *inicio, int codigo)`.
- Cria a função `int atualizar_estado(NoEquipamento *inicio, int codigo, const char novo_estado[])`.
- Cria a função `NoEquipamento *remover_equipamento(NoEquipamento *inicio, int codigo)`.
- Cria a função `int contar_equipamentos(const NoEquipamento *inicio)`.
- Cria a função `void mostrar_inventario(const NoEquipamento *inicio)`.
- Cria a função `void libertar_inventario(NoEquipamento *inicio)`.
- Todas as reservas com `malloc` devem ser verificadas.
- Não permitas dois equipamentos com o mesmo código.
- A procura, atualização e remoção devem ser feitas pelo código do equipamento.
- A função `remover_equipamento` deve funcionar quando o equipamento está no primeiro nó, no meio da lista, no último nó ou não existe.
- No fim do programa, o inventário deve ser libertado e o apontador principal deve ficar com `NULL`.

Passo a passo:

1. Começa com `NoEquipamento *inventario = NULL`.
2. Cria três equipamentos com dados definidos no código.
3. Insere os três equipamentos no fim da lista.
4. Mostra o inventário completo pela ordem de inserção.
5. Tenta inserir um equipamento com código repetido e confirma que a lista não muda.
6. Procura um código existente e um código inexistente.
7. Atualiza o estado de um equipamento existente.
8. Tenta atualizar o estado de um equipamento inexistente.
9. Remove um equipamento que esteja no primeiro nó.
10. Remove um equipamento que esteja no meio ou no fim da lista.
11. Tenta remover um código inexistente.
12. Mostra o inventário depois de cada alteração.
13. Mostra o número final de equipamentos.
14. Liberta todos os nós e coloca `inventario = NULL`.

Exemplo de dados para teste:

```text
101 - Portatil - disponivel
102 - Monitor - avariado
103 - Teclado - disponivel
```

Testes obrigatórios:

- Mostrar o inventário quando ainda está vazio.
- Inserir equipamentos no fim da lista.
- Bloquear código repetido.
- Procurar equipamento existente.
- Procurar equipamento inexistente.
- Atualizar o estado de um equipamento existente.
- Tentar atualizar um código inexistente.
- Remover o primeiro equipamento da lista.
- Remover um equipamento do meio ou do fim.
- Tentar remover um equipamento inexistente.
- Contar corretamente os equipamentos existentes.
- Libertar todos os nós criados com `malloc`.

### Exercício 113 - Lista ligada de alunos

Objetivo: usar uma lista ligada para guardar dados compostos, combinando `struct`, strings, apontadores e memória dinâmica.

Cria um programa que gere uma lista ligada de alunos. Cada nó deve guardar os dados de um aluno e o endereço do próximo nó.

Requisitos:

- Define uma estrutura `Aluno` com `numero`, `nome` e `media`.
- Define uma estrutura `NoAluno` com os campos `aluno` e `proximo`.
- Usa `char nome[50]` para guardar o nome do aluno.
- Cria a função `Aluno criar_aluno(int numero, const char nome[], float media)`.
- Cria a função `NoAluno *criar_no_aluno(Aluno aluno)`.
- Cria a função `NoAluno *inserir_fim(NoAluno *inicio, Aluno aluno)`.
- Cria a função `const NoAluno *procurar_aluno(const NoAluno *inicio, int numero)`.
- Cria a função `NoAluno *remover_aluno(NoAluno *inicio, int numero)`.
- Cria a função `void mostrar_alunos(const NoAluno *inicio)`.
- Cria a função `void libertar_alunos(NoAluno *inicio)`.
- A procura e a remoção devem ser feitas pelo número do aluno.
- Usa apenas lista ligada simples.
- O programa não deve perder o início da lista durante o percurso.

Passo a passo:

1. Começa com `NoAluno *turma = NULL`.
2. Cria três alunos com dados definidos no código.
3. Insere os três alunos no fim da lista.
4. Mostra a lista completa.
5. Procura um aluno existente pelo número.
6. Procura um aluno inexistente pelo número.
7. Remove o primeiro aluno da lista.
8. Remove um aluno que esteja no meio ou no fim da lista.
9. Tenta remover um número inexistente.
10. Mostra a lista depois de cada remoção.
11. Liberta a lista completa.
12. Coloca `turma = NULL` no fim do `main`.

Exemplo de dados para teste:

```text
101 - Ana Silva - 16.5
102 - Bruno Costa - 13.0
103 - Carla Dias - 18.2
```

Critérios de verificação:

- A lista mostra todos os alunos pela ordem de inserção.
- A procura distingue corretamente alunos existentes e inexistentes.
- A remoção do primeiro aluno atualiza o início da lista.
- A remoção de um aluno do meio ou do fim mantém a lista bem ligada.
- Todos os nós criados com `malloc` são libertados com `free`.

### Exercício 114 - Gestor de tarefas com lista ligada e menu

Objetivo: criar um pequeno programa completo com menu, usando lista ligada como estrutura principal de dados.

Cria um gestor de tarefas em consola. Cada tarefa deve estar guardada num nó de uma lista ligada. O utilizador deve conseguir adicionar tarefas, listar tarefas, marcar tarefas como concluídas, remover tarefas e sair do programa.

Requisitos:

- Define constantes `POR_FAZER` e `CONCLUIDA`.
- Define uma estrutura `Tarefa` com `id`, `descricao` e `estado`.
- Define uma estrutura `NoTarefa` com os campos `tarefa` e `proximo`.
- Usa `char descricao[80]` para a descrição.
- Cria a função `Tarefa criar_tarefa(int id, const char descricao[])`.
- Cria a função `NoTarefa *criar_no_tarefa(Tarefa tarefa)`.
- Cria a função `NoTarefa *inserir_fim(NoTarefa *inicio, Tarefa tarefa)`.
- Cria a função `int existe_tarefa(const NoTarefa *inicio, int id)`.
- Cria a função `int marcar_concluida(NoTarefa *inicio, int id)`.
- Cria a função `NoTarefa *remover_tarefa(NoTarefa *inicio, int id)`.
- Cria a função `int contar_pendentes(const NoTarefa *inicio)`.
- Cria a função `void mostrar_tarefas(const NoTarefa *inicio)`.
- Cria a função `void libertar_tarefas(NoTarefa *inicio)`.
- Não permitas duas tarefas com o mesmo `id`.
- A opção de remover deve funcionar para o primeiro nó, para um nó do meio, para o último nó e para um `id` inexistente.
- Usa apenas lista ligada simples.

Menu obrigatório:

```text
1 - Adicionar tarefa
2 - Listar tarefas
3 - Marcar tarefa como concluída
4 - Remover tarefa
5 - Mostrar número de tarefas pendentes
0 - Sair
```

Passo a passo:

1. Começa com `NoTarefa *tarefas = NULL`.
2. Mostra o menu dentro de um ciclo `do while` ou `while`.
3. Na opção `1`, pede `id` e `descricao`.
4. Antes de inserir, verifica se o `id` já existe.
5. Na opção `2`, percorre a lista e mostra cada tarefa.
6. Na opção `3`, procura a tarefa pelo `id` e altera o estado para `CONCLUIDA`.
7. Na opção `4`, remove a tarefa pelo `id`.
8. Na opção `5`, conta apenas as tarefas com estado `POR_FAZER`.
9. Na opção `0`, liberta toda a lista antes de terminar.
10. Depois de libertar, coloca `tarefas = NULL`.

Testes obrigatórios:

- Listar tarefas quando a lista está vazia.
- Adicionar três tarefas.
- Tentar adicionar uma tarefa com `id` repetido.
- Marcar uma tarefa existente como concluída.
- Tentar marcar uma tarefa inexistente.
- Remover a primeira tarefa.
- Remover a última tarefa.
- Tentar remover uma tarefa inexistente.
- Confirmar que o número de tarefas pendentes fica correto.
- Sair do programa sem fugas de memória.

---

![Footer](../Images/Footer.png)
