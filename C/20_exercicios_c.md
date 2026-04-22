# C (10.º Ano) - 20 · Exercícios

---

## Índice de exercícios por módulo

1. 07 · Dados, Variáveis, Declarações, Expressões, Constantes e Tipos
2. 07A · Entrada/Saída Formatada (`printf`/`scanf`) e Endereços (`&` e `*`)
3. 08 · Operadores em C
4. 09 · Estruturas de Controlo em C
5. 10 · Subprogramas: Funções, Variáveis Locais/Globais e Parâmetros
6. 11 · Funcionalidades de um Editor de Texto
7. 12 · Estruturas de Dados Estáticas: Strings, Arrays e Matrizes
8. 13 · Estruturas de Dados Compostas: `struct`, `union` e `enum`
9. 14 · Estruturas de Dados Dinâmicas: Apontadores, Acesso e Manipulação
10. 15 · Classes e Objetos (Contexto em C)
11. 16 · Herança e Polimorfismo (Contexto em C)
12. 17 · Exceções e Tratamento de Erros em C
13. 18 · Ficheiros: Acesso e Manipulação em C
14. 19 · Funcionalidades de Editor de Texto (Produtividade e Debug)

---

## 07 · Dados, Variáveis, Declarações, Expressões, Constantes e Tipos

Fonte: [07_dados_variaveis_constantes_tipos.md](./07_dados_variaveis_constantes_tipos.md)

### Exercício 1 - Declarações

Objetivo: treinar declaração de variáveis com nomes claros e tipos corretos.

Cria um programa que declara variáveis para os seguintes campos de uma ficha digital de aluno:

Número, nome, turma, idade, média e faltas (%).

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
    printf("Digite o nome do produto: ");
    scanf("%49s", nome_produto); // Limita a leitura para evitar overflow
    printf("Digite a quantidade: ");
    scanf("%d", &quantidade);
    printf("Digite o preço unitário: ");
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
    printf("Digite a temperatura em Celsius: ");
    scanf("%lf", &temperatura_celsius);
    printf("Digite a velocidade do vento em km/h: ");
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
    printf("Digite a percentagem de bateria (0-100): ");
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
    printf("Digite sua idade: ");
    scanf("%d", &idade); // Correção: %d para int e uso de & para variável

    printf("Digite sua altura em metros: ");
    scanf("%lf", &altura); // Correção: %lf para double e uso de & para variável

    printf("Digite seu nome: ");
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
    printf("Digite a potência do aparelho em watts: ");
    scanf("%lf", &potencia_watts);
    printf("Digite as horas de uso por dia: ");
    scanf("%lf", &horas_por_dia);
    printf("Digite o preço por kWh: ");
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

## 07A · Entrada/Saída Formatada (`printf`/`scanf`) e Endereços (`&` e `*`)

Fonte: [07a_entrada_saida_formatada_printf_scanf_e_enderecos.md](./07a_entrada_saida_formatada_printf_scanf_e_enderecos.md)

Ordem recomendada: resolver por sequência, do 12 ao 21.

### Exercício 12 - `printf` básico sem input

Objetivo: consolidar impressão formatada sem leitura de dados.

Cria um programa que declara `int`, `double`, `char` e `char nome[]` e imprime os 4 valores com os especificadores corretos.

Passo a passo:

1. Escolhe valores simples para cada variável (`int`, `double`, `char`, `string`).
2. Declara as variáveis com nomes claros.
3. Escreve uma linha de `printf` para cada tipo, usando `%d`, `%.2f`, `%c` e `%s`.
4. Compila e verifica se o output aparece na ordem esperada.
5. Ajusta os textos de apresentação para ficarem legíveis.

### Exercício 13 - Percentagens e casas decimais no `printf`

Objetivo: praticar formatação de números reais e impressão do símbolo `%`.

Cria um programa que apresenta um mini estado de bateria com nome do dispositivo, carga atual e meta de carregamento.

Passo a passo:

1. Declara variáveis para nome do dispositivo, carga atual e meta (em percentagem).
2. Atribui valores de teste realistas às variáveis.
3. Imprime o nome com `%s` e as percentagens com precisão fixa (por exemplo, 1 casa decimal).
4. Mostra o símbolo de percentagem corretamente usando `%%`.
5. Revê o output final para confirmar legibilidade e consistência das casas decimais.

### Exercício 14 - Leitura de um inteiro

Objetivo: ler e validar um valor inteiro com segurança.

Lê um `int` com `scanf`, valida o retorno e imprime o valor lido apenas quando a leitura for válida.

Passo a passo:

1. Declara uma variável `int` para guardar o valor.
2. Pede o número ao utilizador com um `printf` curto.
3. Usa `scanf` e guarda o valor devolvido (número de campos lidos).
4. Se o retorno for `1`, imprime o número lido.
5. Se o retorno for diferente de `1`, mostra mensagem de erro clara.

### Exercício 15 - Leitura de `double`

Objetivo: usar formato correto para leitura e impressão de `double`.

Lê um `double` com `scanf("%lf", ...)`, valida a leitura e imprime o resultado com 3 casas decimais.

Passo a passo:

1. Declara uma variável `double`.
2. Mostra uma mensagem a pedir um valor decimal.
3. Lê com `scanf("%lf", &variavel)` e verifica o retorno.
4. Em caso válido, imprime com `%.3f`.
5. Em caso inválido, apresenta erro sem continuar cálculos.

### Exercício 16 - Valor e endereço

Objetivo: distinguir valor armazenado de endereço em memória.

Lê um inteiro e imprime o valor (`%d`) e o endereço (`%p`, com cast para `(void *)`).

Passo a passo:

1. Declara um `int` e lê o valor com `scanf`.
2. Verifica se a leitura foi bem-sucedida.
3. Imprime o valor com `%d`.
4. Imprime o endereço com `%p`, convertendo para `(void *)`.
5. Compara visualmente valor e endereço para reforçar a diferença.

### Exercício 17 - Dois inteiros na mesma linha

Objetivo: ler múltiplos campos numa única chamada de `scanf`.

Lê `a` e `b` na mesma linha com `scanf("%d %d", &a, &b)` e valida se foram lidos os 2 valores.

Passo a passo:

1. Declara duas variáveis `int` (`a` e `b`).
2. Mostra instrução para o utilizador inserir os dois valores na mesma linha.
3. Faz a leitura numa única chamada `scanf`.
4. Verifica se o retorno é `2`.
5. Se válido, imprime os dois valores; se inválido, mostra erro.

### Exercício 18 - Leitura de `char` após número

Objetivo: evitar erro comum de leitura de `char` após `int`.

Lê primeiro um número e depois uma opção (`A`, `B` ou `C`), usando `" %c"` para ignorar whitespace pendente.

Passo a passo:

1. Declara um `int` e um `char`.
2. Lê o número e valida retorno.
3. Lê a opção com `scanf(" %c", &opcao)`.
4. Confirma se a opção está no conjunto esperado (`A`, `B`, `C`).
5. Imprime resumo final com número e opção escolhida.

### Exercício 19 - Palavra com limite de tamanho

Objetivo: prevenir overflow em leitura de string com `scanf`.

Lê uma palavra para `char codigo[20]` usando limite no especificador (`%19s`) e imprime o resultado.

Passo a passo:

1. Declara o array `char codigo[20]`.
2. Pede ao utilizador um código sem espaços.
3. Lê com `scanf("%19s", codigo)`.
4. Verifica se a leitura retornou `1`.
5. Imprime o valor lido e testa com palavras curtas e longas.

### Exercício 20 - Frase completa com `fgets`

Objetivo: ler linha completa com espaços e limpar newline final.

Lê uma frase para `char frase[80]` com `fgets`, remove `\n` final (quando existir) e imprime o texto limpo.

Passo a passo:

1. Declara `char frase[80]`.
2. Pede uma frase completa ao utilizador.
3. Lê com `fgets(frase, sizeof(frase), stdin)`.
4. Procura `\n` no fim e substitui por `\0` quando necessário.
5. Imprime a frase final entre delimitadores visuais para confirmar limpeza.

### Exercício 21 - Mini ficha (integração)

Objetivo: integrar leitura e apresentação de vários tipos no mesmo programa.

Cria uma mini ficha de aluno que lê: número (`int`), média (`double`), turma (`char`) e nome completo (`fgets`).

Passo a passo:

1. Declara todas as variáveis necessárias com tipos corretos.
2. Lê número, média e turma com `scanf`, validando cada retorno.
3. Garante limpeza de input antes de ler o nome completo.
4. Lê o nome com `fgets` e remove `\n` final se existir.
5. Imprime um resumo final alinhado, claro e consistente.

---

## 08 · Operadores em C

Fonte: [08_operadores_em_c.md](./08_operadores_em_c.md)

### Exercício 22 - Aritmética básica

Escreve programa que lê dois inteiros e mostra soma, diferença, produto, quociente e resto.

### Exercício 23 - Divisão inteira vs real

Demonstra com 8 exemplos a diferença entre divisão inteira e divisão real.

### Exercício 24 - Atribuição composta

Reescreve 10 atribuições simples usando operadores compostos.

### Exercício 25 - Comparações

Para 12 pares de valores, imprime resultados de todos os operadores relacionais.

### Exercício 26 - Lógica booleana

Implementa validador: idade >= 18 e nota >= 10.

### Exercício 27 - Intervalos

Verifica se número está no intervalo fechado [1, 100].

### Exercício 28 - Incremento

Cria programa com contador e demonstra pré/pós incremento.

### Exercício 29 - Precedência

Calcula e compara resultados de 10 expressões com e sem parênteses.

### Exercício 30 - Refatoração

Recebes 6 condições complexas; reescreve em forma mais legível.

### Exercício 31 - Mini calculadora

Implementa mini calculadora para `+`, `-`, `*`, `/`, `%`.

### Exercício 32 - Diagnóstico

Encontra e corrige erros de operadores num código fornecido pelo professor.

### Exercício 33 - Reflexão

Explica por que compreender operadores evita muitos bugs lógicos.

---

## 09 · Estruturas de Controlo em C

Fonte: [09_estruturas_de_controlo_em_c.md](./09_estruturas_de_controlo_em_c.md)

### Exercício 34 - Classificação

Lê nota e classifica em 4 níveis usando `if/else if/else`.

### Exercício 35 - Menu

Cria menu com `switch` para 4 operações matemáticas.

### Exercício 36 - Contagem

Imprime números de 1 a 50 com `while`.

### Exercício 37 - Soma acumulada

Lê números até aparecer 0 e mostra soma total.

### Exercício 38 - Tabuada

Mostra tabuada de um número com `for`.

### Exercício 39 - Adivinhação

Cria jogo de adivinhar número com limite de tentativas.

### Exercício 40 - `break` e `continue`

Faz exemplo que salta múltiplos de 3 e termina em valor específico.

### Exercício 41 - Matriz

Percorre matriz 4x4 e calcula soma dos elementos.

### Exercício 42 - Validação

Repete pedido de nota enquanto valor estiver fora de 0-20.

### Exercício 43 - Menu persistente

Menu com `do while` que só termina quando utilizador escolhe sair.

### Exercício 44 - Conversão

Converte um algoritmo textual com repetição para C.

### Exercício 45 - Reflexão

Explica quando escolher `for`, `while` e `do while`.

---

## 10 · Subprogramas: Funções, Variáveis Locais/Globais e Parâmetros

Fonte: [10_subprogramas_funcoes_e_parametros.md](./10_subprogramas_funcoes_e_parametros.md)

### Exercício 46 - Funções básicas

Cria funções para somar, subtrair, multiplicar e dividir.

### Exercício 47 - Retorno

Cria função que devolve maior de dois inteiros.

### Exercício 48 - `void`

Cria procedimento que imprime linha separadora no ecrã.

### Exercício 49 - Locais e globais

Constrói exemplo com uma variável global e duas locais.

### Exercício 50 - Passagem por valor

Demonstra, com programa curto, que variável original não é alterada.

### Exercício 51 - Passagem por ponteiro

Cria função para trocar dois inteiros.

### Exercício 52 - Validação de parâmetros

Cria função de divisão que trate divisor zero.

### Exercício 53 - Modularização

Separa projeto em `main.c`, `operacoes.c`, `operacoes.h`.

### Exercício 54 - Contador de chamadas

Usa variável global para contar quantas vezes função foi chamada.

### Exercício 55 - Refatoração

Transforma programa monolítico em pelo menos 5 funções.

### Exercício 56 - Mini biblioteca

Cria conjunto de funções para manipular notas de alunos.

### Exercício 57 - Reflexão

Explica quando usar retorno e quando usar parâmetro por ponteiro.

---

## 11 · Funcionalidades de um Editor de Texto

Fonte: [11_funcionalidades_editor_de_texto.md](./11_funcionalidades_editor_de_texto.md)

### Exercício 58 - Configuração base

Configura editor com linha, coluna e indentação de 4 espaços.

### Exercício 59 - Atalhos

Lista e pratica 12 atalhos úteis para programação C.

### Exercício 60 - Pesquisa global

Localiza todas as ocorrências de uma função num projeto com vários ficheiros.

### Exercício 61 - Substituição segura

Renomeia variável em projeto sem quebrar outras partes.

### Exercício 62 - Navegação

Usa "go to definition" para navegar entre `.h` e `.c`.

### Exercício 63 - Formatação

Aplica formatação consistente a um ficheiro propositalmente desorganizado.

### Exercício 64 - Terminal

Compila e executa programa apenas com terminal integrado.

### Exercício 65 - Tarefa automática

Cria tarefa de build no editor para um projeto C.

### Exercício 66 - Debug inicial

Configura breakpoint e observa valor de uma variável por iteração.

### Exercício 67 - Refatoração assistida

Extrai bloco de código para função com apoio do editor.

### Exercício 68 - Produtividade

Mede tempo de tarefa com e sem atalhos; compara resultados.

### Exercício 69 - Reflexão

Explica como editor bem usado melhora aprendizagem para iniciantes.

---

## 12 · Estruturas de Dados Estáticas: Strings, Arrays e Matrizes

Fonte: [12_estruturas_estaticas_strings_arrays_matrizes.md](./12_estruturas_estaticas_strings_arrays_matrizes.md)

### Exercício 70 - Vetor básico

Lê 10 inteiros para um vetor e imprime-os na ordem inversa.

### Exercício 71 - Estatísticas

Num vetor de 20 valores, calcula soma, média, máximo e mínimo.

### Exercício 72 - Pares e ímpares

Conta quantos elementos pares e ímpares existem no vetor.

### Exercício 73 - Pesquisa

Implementa pesquisa linear de um valor num array.

### Exercício 74 - Strings

Lê nome completo e imprime quantidade de caracteres.

### Exercício 75 - Comparação de strings

Lê duas palavras e indica se são iguais.

### Exercício 76 - Concatenação

Lê nome e apelido e constrói nome completo.

### Exercício 77 - Matriz 3x3

Lê matriz 3x3 e calcula soma da diagonal principal.

### Exercício 78 - Matriz e condição

Conta quantos valores de matriz 4x4 são maiores que 10.

### Exercício 79 - Ordenação simples

Ordena vetor de 10 elementos por método simples à tua escolha.

### Exercício 80 - Segurança

Reescreve programa de leitura de nomes para evitar overflow.

### Exercício 81 - Reflexão

Explica diferenças práticas entre arrays e estruturas dinâmicas.

---

## 13 · Estruturas de Dados Compostas: `struct`, `union` e `enum`

Fonte: [13_estruturas_compostas_struct_union_enum.md](./13_estruturas_compostas_struct_union_enum.md)

### Exercício 82 - `struct` básico

Cria `struct Livro` com título, autor, ano e disponibilidade.

### Exercício 83 - Leitura e impressão

Lê dados de 3 livros e imprime relatório.

### Exercício 84 - Array de structs

Cria array de 20 alunos e calcula média da turma.

### Exercício 85 - Pesquisa

Procura aluno por número dentro de array de structs.

### Exercício 86 - Atualização

Atualiza estado de um registo (ativo/inativo).

### Exercício 87 - `enum`

Define `enum` para dias da semana e usa em programa simples.

### Exercício 88 - `union`

Cria `union` para representar valor numérico em formatos diferentes.

### Exercício 89 - `struct` com `enum`

Combina `struct Pedido` com `enum EstadoPedido`.

### Exercício 90 - Ponteiros

Manipula `struct` através de ponteiro e operador `->`.

### Exercício 91 - Modularização

Move definições para ficheiro `.h` e implementação para `.c`.

### Exercício 92 - Validação

Valida campos de registo antes de guardar.

### Exercício 93 - Reflexão

Explica porque estruturas compostas tornam o código mais próximo de problemas reais.

---

## 14 · Estruturas de Dados Dinâmicas: Apontadores, Acesso e Manipulação

Fonte: [14_estruturas_dinamicas_apontadores.md](./14_estruturas_dinamicas_apontadores.md)

### Exercício 94 - Endereços

Cria programa que mostra valor e endereço de 3 variáveis.

### Exercício 95 - Ponteiro básico

Usa ponteiro para alterar valor de uma variável inteira.

### Exercício 96 - Vetor dinâmico

Aloca vetor de `n` inteiros e calcula soma dos elementos.

### Exercício 97 - `calloc`

Repete exercício 3 usando `calloc` e compara comportamento inicial.

### Exercício 98 - `realloc`

Começa com 5 elementos e expande para 10 com `realloc`.

### Exercício 99 - Struct dinâmica

Aloca dinamicamente uma `struct Aluno` e preenche campos.

### Exercício 100 - Array de structs dinâmico

Aloca turma com tamanho informado pelo utilizador.

### Exercício 101 - Lista ligada (nó único)

Cria nó, atribui valor, imprime e liberta memória.

### Exercício 102 - Lista ligada (vários nós)

Insere 5 nós no fim e percorre para imprimir.

### Exercício 103 - Gestão de memória

Faz auditoria de um código e identifica pontos de leak.

### Exercício 104 - Segurança

Corrige um exemplo com risco de use-after-free.

### Exercício 105 - Reflexão

Explica por que gestão manual de memória exige disciplina técnica.

---

## 15 · Classes e Objetos (Contexto em C)

Fonte: [15_classes_e_objetos_contexto_c.md](./15_classes_e_objetos_contexto_c.md)

### Exercício 106 - Modelação

Modela entidade `Aluno` como "objeto" em C (`struct` + funções).

### Exercício 107 - API mínima

Cria API para `Livro`: criar, atualizar estado e consultar dados.

### Exercício 108 - Inicialização

Implementa função `init` para 3 tipos diferentes.

### Exercício 109 - Encapsulamento

Reorganiza código para ocultar detalhes internos num `.c`.

### Exercício 110 - Validação de regras

Implementa função que recusa operações inválidas (ex.: saldo negativo).

### Exercício 111 - Modularização

Divide programa em `main.c`, `entidade.c`, `entidade.h`.

### Exercício 112 - Const-correctness

Cria funções de consulta que recebem ponteiro `const`.

### Exercício 113 - Testes manuais

Define 12 testes para validar API de uma entidade.

### Exercício 114 - Refatoração

Converte programa monolítico num design baseado em "objetos" simulados.

### Exercício 115 - Documentação

Escreve documentação de API para uma entidade criada por ti.

### Exercício 116 - Evolução

Acrescenta novo comportamento mantendo compatibilidade da API.

### Exercício 117 - Reflexão

Explica semelhanças e diferenças entre este modelo em C e classes em OOP.

---

## 16 · Herança e Polimorfismo (Contexto em C)

Fonte: [16_heranca_e_polimorfismo_contexto_c.md](./16_heranca_e_polimorfismo_contexto_c.md)

### Exercício 118 - Composição

Cria `struct Veiculo` e `struct Carro` reutilizando campos comuns.

### Exercício 119 - Interface por função

Define interface de impressão para dois tipos diferentes.

### Exercício 120 - Polimorfismo simples

Implementa duas funções de comportamento e seleciona em runtime.

### Exercício 121 - Vetor de "objetos"

Cria array de estruturas com ponteiro para função e executa comportamento.

### Exercício 122 - Organização

Separa interface e implementação em ficheiros distintos.

### Exercício 123 - Validação

Evita chamada de ponteiro de função nulo com verificações.

### Exercício 124 - Refatoração

Converte código com muitos `if` de tipo para abordagem polimórfica.

### Exercício 125 - Testes

Define testes para validar interface comum entre tipos.

### Exercício 126 - Limitações

Escreve 6 limitações desta abordagem em comparação com C++.

### Exercício 127 - Expansão

Adiciona um novo tipo à interface sem alterar código cliente principal.

### Exercício 128 - Segurança

Analisa código e identifica riscos com ponteiros para função.

### Exercício 129 - Reflexão

Explica como este módulo ajuda a entender OOP mesmo em C.

---

## 17 · Exceções e Tratamento de Erros em C

Fonte: [17_excecoes_e_tratamento_de_erros_em_c.md](./17_excecoes_e_tratamento_de_erros_em_c.md)

### Exercício 130 - Divisão segura

Implementa função de divisão com tratamento de divisor zero.

### Exercício 131 - Entrada robusta

Lê inteiro com validação de formato e intervalo.

### Exercício 132 - Códigos de erro

Define tabela de códigos de erro para um mini projeto.

### Exercício 133 - Ficheiros

Abre ficheiro para leitura e trata todos os possíveis erros básicos.

### Exercício 134 - Memória

Aloca vetor dinâmico com validação e mensagens de erro adequadas.

### Exercício 135 - Propagação

Cria cadeia de 3 funções que propagam erros até `main`.

### Exercício 136 - Limpeza de recursos

Garante que ficheiro e memória são libertados em qualquer caminho de erro.

### Exercício 137 - Refatoração

Melhora um código sem tratamento de erros.

### Exercício 138 - Diagnóstico

Usa `perror` e `errno` em 5 cenários distintos.

### Exercício 139 - Testes de erro

Define 15 testes focados apenas em cenários inválidos.

### Exercício 140 - Mensagens de utilizador

Reescreve mensagens técnicas para linguagem compreensível por utilizador final.

### Exercício 141 - Reflexão

Explica por que tratamento de erros faz parte da qualidade do software.

---

## 18 · Ficheiros: Acesso e Manipulação em C

Fonte: [18_ficheiros_acesso_e_manipulacao_em_c.md](./18_ficheiros_acesso_e_manipulacao_em_c.md)

### Exercício 142 - Escrita simples

Cria programa que grava 5 linhas num ficheiro texto.

### Exercício 143 - Leitura simples

Lê ficheiro linha a linha e imprime no ecrã.

### Exercício 144 - Cópia de ficheiro

Implementa cópia de um ficheiro texto para outro.

### Exercício 145 - Contagem

Conta número de linhas e caracteres de um ficheiro.

### Exercício 146 - Registos

Guarda registos de alunos no formato `nome;nota`.

### Exercício 147 - Pesquisa

Lê ficheiro e procura registo por nome.

### Exercício 148 - Acrescentar dados

Abre ficheiro em modo append e adiciona novos registos.

### Exercício 149 - Binário básico

Grava e lê array de inteiros em ficheiro binário.

### Exercício 150 - Validação de I/O

Melhora programa com tratamento de erro em cada operação de ficheiro.

### Exercício 151 - Navegação

Usa `fseek` e `ftell` para descobrir tamanho de ficheiro.

### Exercício 152 - Projeto curto

Cria mini agenda persistente em ficheiro (inserir/listar).

### Exercício 153 - Reflexão

Explica diferenças práticas entre guardar dados em texto e em binário.

---

## 19 · Funcionalidades de Editor de Texto (Produtividade e Debug)

Fonte: [19_editor_texto_produtividade_e_debug.md](./19_editor_texto_produtividade_e_debug.md)

### Exercício 154 - Atalhos avançados

Seleciona 15 atalhos do editor e aplica em tarefa real.

### Exercício 155 - Pipeline local

Configura build + run num único comando/tarefa no editor.

### Exercício 156 - Debug guiado

Coloca breakpoints em função com ciclo e analisa evolução de variáveis.

### Exercício 157 - Rastreio de bug

Recebe programa com erro lógico e usa debugger para localizar causa.

### Exercício 158 - Navegação

Num projeto com 8+ ficheiros, localiza rapidamente função e todas as referências.

### Exercício 159 - Refatoração

Renomeia função globalmente sem quebrar build.

### Exercício 160 - Extração

Extrai bloco repetido para função reutilizável.

### Exercício 161 - Qualidade

Cria checklist final de 12 pontos antes de entregar projeto.

### Exercício 162 - Métricas pessoais

Regista tempo gasto em tarefa antes e depois de configurar automações.

### Exercício 163 - Organização

Reorganiza projeto desestruturado em pastas claras (`src`, `include`, `bin`).

### Exercício 164 - Simulação de revisão

Faz revisão de código de colega usando ferramentas do editor.

### Exercício 165 - Reflexão

Explica como domínio de editor influencia qualidade e aprendizagem em C.

---
