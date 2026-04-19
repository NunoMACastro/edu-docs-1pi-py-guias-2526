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

Cria a "ficha digital" de um aluno: número, nome, turma, idade, média atual e percentagem de faltas. Declara variáveis com tipos adequados e nomes claros.

### Exercício 2 - Tipos corretos

Dado um sistema de bicicletas partilhadas, escolhe tipos para: id da bicicleta, quilómetros totais, custo por minuto, estado (disponível/ocupada) e nível de bateria. Justifica cada escolha.

### Exercício 3 - Constantes

Define constantes para: limite de velocidade de trotinete elétrica, preço fixo de desbloqueio e taxa por minuto. Usa `const` e/ou `#define` de forma consistente.

### Exercício 4 - Expressões

Num simulador de treino, calcula calorias estimadas com base em tempo (min), peso (kg) e fator de intensidade. Escreve as expressões em C e prevê os resultados para dois casos de teste.

### Exercício 5 - Casting

Num painel de estatísticas, calcula média de pontos por jogo e taxa de vitórias. Mostra o resultado sem cast e com cast, explicando a diferença no valor apresentado.

### Exercício 6 - Entrada/saída

Lê nome do produto, quantidade e preço unitário. Imprime um resumo de compra alinhado com subtotal e total com 2 casas decimais.

### Exercício 7 - Conversão de unidades

Cria um mini conversor de meteorologia: lê temperatura em Celsius e velocidade do vento em km/h, depois mostra Fahrenheit e m/s com formatação adequada.

### Exercício 8 - Validação básica

Lê a percentagem de bateria de um dispositivo (0 a 100) e valida o valor. Se estiver fora do intervalo, imprime mensagem de erro clara.

### Exercício 9 - Formatação

Mostra um "placar" com 3 jogadores: nome, pontos e precisão (%) com colunas alinhadas em `printf`.

### Exercício 10 - Diagnóstico

Analisa um trecho com erros de tipos e formatos (`%d`, `%f`, `%lf`, uso de `&` no `scanf`) e corrige cada linha, explicando o motivo técnico.

### Exercício 11 - Mini programa

Desenvolve um simulador de consumo elétrico doméstico: lê potência (W), horas de uso por dia e preço por kWh; calcula consumo mensal e custo estimado.

### Exercício 12 - Reflexão

Escreve uma reflexão curta: em que situações um `int` pode causar erro silencioso e quando `float`/`double` é realmente necessário?

---

## 07A · Entrada/Saída Formatada (`printf`/`scanf`) e Endereços (`&` e `*`)

Fonte: [07a_entrada_saida_formatada_printf_scanf_e_enderecos.md](./07a_entrada_saida_formatada_printf_scanf_e_enderecos.md)

Ordem recomendada: resolver por sequência, do 1 ao 10.

### Exercício 1 - `printf` básico sem input

Declara `int`, `double`, `char` e `char nome[]`, e imprime tudo com formatos corretos (`%d`, `%.2f`, `%c`, `%s`).

### Exercício 2 - Largura e precisão

Imprime 3 valores numéricos em colunas alinhadas, usando largura fixa e 2 casas decimais.

### Exercício 3 - Leitura de um inteiro

Lê um `int` com `scanf`, valida retorno (`== 1`) e imprime valor lido.

### Exercício 4 - Leitura de `double`

Lê um `double` com `scanf("%lf", ...)`, valida retorno e imprime com 3 casas decimais.

### Exercício 5 - Valor e endereço

Lê um inteiro e imprime:

- o valor (`%d`);
- o endereço (`%p` com cast para `(void *)`).

### Exercício 6 - Dois inteiros na mesma linha

Lê `a` e `b` com `scanf("%d %d", &a, &b)` e valida se foram lidos 2 campos.

### Exercício 7 - Leitura de `char` após número

Lê primeiro um número e depois uma opção (`A`, `B` ou `C`), usando `" %c"` para evitar leitura do `\n`.

### Exercício 8 - Palavra com limite de tamanho

Lê uma palavra para `char codigo[20]` usando `scanf("%19s", codigo)` e imprime o resultado.

### Exercício 9 - Frase completa com `fgets`

Lê uma linha completa para `char frase[80]` com `fgets`, remove o `\n` final (se existir) e imprime a frase.

### Exercício 10 - Mini ficha (integração)

Cria um programa que lê e imprime:

- número do aluno (`int`);
- média (`double`);
- turma (`char`);
- nome completo (`fgets`).

Regras:

- validar retornos de `scanf`;
- usar formato correto em cada tipo;
- imprimir resumo final alinhado e legível.

---

## 08 · Operadores em C

Fonte: [08_operadores_em_c.md](./08_operadores_em_c.md)

### Exercício 1 - Aritmética básica

Escreve programa que lê dois inteiros e mostra soma, diferença, produto, quociente e resto.

### Exercício 2 - Divisão inteira vs real

Demonstra com 8 exemplos a diferença entre divisão inteira e divisão real.

### Exercício 3 - Atribuição composta

Reescreve 10 atribuições simples usando operadores compostos.

### Exercício 4 - Comparações

Para 12 pares de valores, imprime resultados de todos os operadores relacionais.

### Exercício 5 - Lógica booleana

Implementa validador: idade >= 18 e nota >= 10.

### Exercício 6 - Intervalos

Verifica se número está no intervalo fechado [1, 100].

### Exercício 7 - Incremento

Cria programa com contador e demonstra pré/pós incremento.

### Exercício 8 - Precedência

Calcula e compara resultados de 10 expressões com e sem parênteses.

### Exercício 9 - Refatoração

Recebes 6 condições complexas; reescreve em forma mais legível.

### Exercício 10 - Mini calculadora

Implementa mini calculadora para `+`, `-`, `*`, `/`, `%`.

### Exercício 11 - Diagnóstico

Encontra e corrige erros de operadores num código fornecido pelo professor.

### Exercício 12 - Reflexão

Explica por que compreender operadores evita muitos bugs lógicos.

---

## 09 · Estruturas de Controlo em C

Fonte: [09_estruturas_de_controlo_em_c.md](./09_estruturas_de_controlo_em_c.md)

### Exercício 1 - Classificação

Lê nota e classifica em 4 níveis usando `if/else if/else`.

### Exercício 2 - Menu

Cria menu com `switch` para 4 operações matemáticas.

### Exercício 3 - Contagem

Imprime números de 1 a 50 com `while`.

### Exercício 4 - Soma acumulada

Lê números até aparecer 0 e mostra soma total.

### Exercício 5 - Tabuada

Mostra tabuada de um número com `for`.

### Exercício 6 - Adivinhação

Cria jogo de adivinhar número com limite de tentativas.

### Exercício 7 - `break` e `continue`

Faz exemplo que salta múltiplos de 3 e termina em valor específico.

### Exercício 8 - Matriz

Percorre matriz 4x4 e calcula soma dos elementos.

### Exercício 9 - Validação

Repete pedido de nota enquanto valor estiver fora de 0-20.

### Exercício 10 - Menu persistente

Menu com `do while` que só termina quando utilizador escolhe sair.

### Exercício 11 - Conversão

Converte um algoritmo textual com repetição para C.

### Exercício 12 - Reflexão

Explica quando escolher `for`, `while` e `do while`.

---

## 10 · Subprogramas: Funções, Variáveis Locais/Globais e Parâmetros

Fonte: [10_subprogramas_funcoes_e_parametros.md](./10_subprogramas_funcoes_e_parametros.md)

### Exercício 1 - Funções básicas

Cria funções para somar, subtrair, multiplicar e dividir.

### Exercício 2 - Retorno

Cria função que devolve maior de dois inteiros.

### Exercício 3 - `void`

Cria procedimento que imprime linha separadora no ecrã.

### Exercício 4 - Locais e globais

Constrói exemplo com uma variável global e duas locais.

### Exercício 5 - Passagem por valor

Demonstra, com programa curto, que variável original não é alterada.

### Exercício 6 - Passagem por ponteiro

Cria função para trocar dois inteiros.

### Exercício 7 - Validação de parâmetros

Cria função de divisão que trate divisor zero.

### Exercício 8 - Modularização

Separa projeto em `main.c`, `operacoes.c`, `operacoes.h`.

### Exercício 9 - Contador de chamadas

Usa variável global para contar quantas vezes função foi chamada.

### Exercício 10 - Refatoração

Transforma programa monolítico em pelo menos 5 funções.

### Exercício 11 - Mini biblioteca

Cria conjunto de funções para manipular notas de alunos.

### Exercício 12 - Reflexão

Explica quando usar retorno e quando usar parâmetro por ponteiro.

---

## 11 · Funcionalidades de um Editor de Texto

Fonte: [11_funcionalidades_editor_de_texto.md](./11_funcionalidades_editor_de_texto.md)

### Exercício 1 - Configuração base

Configura editor com linha, coluna e indentação de 4 espaços.

### Exercício 2 - Atalhos

Lista e pratica 12 atalhos úteis para programação C.

### Exercício 3 - Pesquisa global

Localiza todas as ocorrências de uma função num projeto com vários ficheiros.

### Exercício 4 - Substituição segura

Renomeia variável em projeto sem quebrar outras partes.

### Exercício 5 - Navegação

Usa "go to definition" para navegar entre `.h` e `.c`.

### Exercício 6 - Formatação

Aplica formatação consistente a um ficheiro propositalmente desorganizado.

### Exercício 7 - Terminal

Compila e executa programa apenas com terminal integrado.

### Exercício 8 - Tarefa automática

Cria tarefa de build no editor para um projeto C.

### Exercício 9 - Debug inicial

Configura breakpoint e observa valor de uma variável por iteração.

### Exercício 10 - Refatoração assistida

Extrai bloco de código para função com apoio do editor.

### Exercício 11 - Produtividade

Mede tempo de tarefa com e sem atalhos; compara resultados.

### Exercício 12 - Reflexão

Explica como editor bem usado melhora aprendizagem para iniciantes.

---

## 12 · Estruturas de Dados Estáticas: Strings, Arrays e Matrizes

Fonte: [12_estruturas_estaticas_strings_arrays_matrizes.md](./12_estruturas_estaticas_strings_arrays_matrizes.md)

### Exercício 1 - Vetor básico

Lê 10 inteiros para um vetor e imprime-os na ordem inversa.

### Exercício 2 - Estatísticas

Num vetor de 20 valores, calcula soma, média, máximo e mínimo.

### Exercício 3 - Pares e ímpares

Conta quantos elementos pares e ímpares existem no vetor.

### Exercício 4 - Pesquisa

Implementa pesquisa linear de um valor num array.

### Exercício 5 - Strings

Lê nome completo e imprime quantidade de caracteres.

### Exercício 6 - Comparação de strings

Lê duas palavras e indica se são iguais.

### Exercício 7 - Concatenação

Lê nome e apelido e constrói nome completo.

### Exercício 8 - Matriz 3x3

Lê matriz 3x3 e calcula soma da diagonal principal.

### Exercício 9 - Matriz e condição

Conta quantos valores de matriz 4x4 são maiores que 10.

### Exercício 10 - Ordenação simples

Ordena vetor de 10 elementos por método simples à tua escolha.

### Exercício 11 - Segurança

Reescreve programa de leitura de nomes para evitar overflow.

### Exercício 12 - Reflexão

Explica diferenças práticas entre arrays e estruturas dinâmicas.

---

## 13 · Estruturas de Dados Compostas: `struct`, `union` e `enum`

Fonte: [13_estruturas_compostas_struct_union_enum.md](./13_estruturas_compostas_struct_union_enum.md)

### Exercício 1 - `struct` básico

Cria `struct Livro` com título, autor, ano e disponibilidade.

### Exercício 2 - Leitura e impressão

Lê dados de 3 livros e imprime relatório.

### Exercício 3 - Array de structs

Cria array de 20 alunos e calcula média da turma.

### Exercício 4 - Pesquisa

Procura aluno por número dentro de array de structs.

### Exercício 5 - Atualização

Atualiza estado de um registo (ativo/inativo).

### Exercício 6 - `enum`

Define `enum` para dias da semana e usa em programa simples.

### Exercício 7 - `union`

Cria `union` para representar valor numérico em formatos diferentes.

### Exercício 8 - `struct` com `enum`

Combina `struct Pedido` com `enum EstadoPedido`.

### Exercício 9 - Ponteiros

Manipula `struct` através de ponteiro e operador `->`.

### Exercício 10 - Modularização

Move definições para ficheiro `.h` e implementação para `.c`.

### Exercício 11 - Validação

Valida campos de registo antes de guardar.

### Exercício 12 - Reflexão

Explica porque estruturas compostas tornam o código mais próximo de problemas reais.

---

## 14 · Estruturas de Dados Dinâmicas: Apontadores, Acesso e Manipulação

Fonte: [14_estruturas_dinamicas_apontadores.md](./14_estruturas_dinamicas_apontadores.md)

### Exercício 1 - Endereços

Cria programa que mostra valor e endereço de 3 variáveis.

### Exercício 2 - Ponteiro básico

Usa ponteiro para alterar valor de uma variável inteira.

### Exercício 3 - Vetor dinâmico

Aloca vetor de `n` inteiros e calcula soma dos elementos.

### Exercício 4 - `calloc`

Repete exercício 3 usando `calloc` e compara comportamento inicial.

### Exercício 5 - `realloc`

Começa com 5 elementos e expande para 10 com `realloc`.

### Exercício 6 - Struct dinâmica

Aloca dinamicamente uma `struct Aluno` e preenche campos.

### Exercício 7 - Array de structs dinâmico

Aloca turma com tamanho informado pelo utilizador.

### Exercício 8 - Lista ligada (nó único)

Cria nó, atribui valor, imprime e liberta memória.

### Exercício 9 - Lista ligada (vários nós)

Insere 5 nós no fim e percorre para imprimir.

### Exercício 10 - Gestão de memória

Faz auditoria de um código e identifica pontos de leak.

### Exercício 11 - Segurança

Corrige um exemplo com risco de use-after-free.

### Exercício 12 - Reflexão

Explica por que gestão manual de memória exige disciplina técnica.

---

## 15 · Classes e Objetos (Contexto em C)

Fonte: [15_classes_e_objetos_contexto_c.md](./15_classes_e_objetos_contexto_c.md)

### Exercício 1 - Modelação

Modela entidade `Aluno` como "objeto" em C (`struct` + funções).

### Exercício 2 - API mínima

Cria API para `Livro`: criar, atualizar estado e consultar dados.

### Exercício 3 - Inicialização

Implementa função `init` para 3 tipos diferentes.

### Exercício 4 - Encapsulamento

Reorganiza código para ocultar detalhes internos num `.c`.

### Exercício 5 - Validação de regras

Implementa função que recusa operações inválidas (ex.: saldo negativo).

### Exercício 6 - Modularização

Divide programa em `main.c`, `entidade.c`, `entidade.h`.

### Exercício 7 - Const-correctness

Cria funções de consulta que recebem ponteiro `const`.

### Exercício 8 - Testes manuais

Define 12 testes para validar API de uma entidade.

### Exercício 9 - Refatoração

Converte programa monolítico num design baseado em "objetos" simulados.

### Exercício 10 - Documentação

Escreve documentação de API para uma entidade criada por ti.

### Exercício 11 - Evolução

Acrescenta novo comportamento mantendo compatibilidade da API.

### Exercício 12 - Reflexão

Explica semelhanças e diferenças entre este modelo em C e classes em OOP.

---

## 16 · Herança e Polimorfismo (Contexto em C)

Fonte: [16_heranca_e_polimorfismo_contexto_c.md](./16_heranca_e_polimorfismo_contexto_c.md)

### Exercício 1 - Composição

Cria `struct Veiculo` e `struct Carro` reutilizando campos comuns.

### Exercício 2 - Interface por função

Define interface de impressão para dois tipos diferentes.

### Exercício 3 - Polimorfismo simples

Implementa duas funções de comportamento e seleciona em runtime.

### Exercício 4 - Vetor de "objetos"

Cria array de estruturas com ponteiro para função e executa comportamento.

### Exercício 5 - Organização

Separa interface e implementação em ficheiros distintos.

### Exercício 6 - Validação

Evita chamada de ponteiro de função nulo com verificações.

### Exercício 7 - Refatoração

Converte código com muitos `if` de tipo para abordagem polimórfica.

### Exercício 8 - Testes

Define testes para validar interface comum entre tipos.

### Exercício 9 - Limitações

Escreve 6 limitações desta abordagem em comparação com C++.

### Exercício 10 - Expansão

Adiciona um novo tipo à interface sem alterar código cliente principal.

### Exercício 11 - Segurança

Analisa código e identifica riscos com ponteiros para função.

### Exercício 12 - Reflexão

Explica como este módulo ajuda a entender OOP mesmo em C.

---

## 17 · Exceções e Tratamento de Erros em C

Fonte: [17_excecoes_e_tratamento_de_erros_em_c.md](./17_excecoes_e_tratamento_de_erros_em_c.md)

### Exercício 1 - Divisão segura

Implementa função de divisão com tratamento de divisor zero.

### Exercício 2 - Entrada robusta

Lê inteiro com validação de formato e intervalo.

### Exercício 3 - Códigos de erro

Define tabela de códigos de erro para um mini projeto.

### Exercício 4 - Ficheiros

Abre ficheiro para leitura e trata todos os possíveis erros básicos.

### Exercício 5 - Memória

Aloca vetor dinâmico com validação e mensagens de erro adequadas.

### Exercício 6 - Propagação

Cria cadeia de 3 funções que propagam erros até `main`.

### Exercício 7 - Limpeza de recursos

Garante que ficheiro e memória são libertados em qualquer caminho de erro.

### Exercício 8 - Refatoração

Melhora um código sem tratamento de erros.

### Exercício 9 - Diagnóstico

Usa `perror` e `errno` em 5 cenários distintos.

### Exercício 10 - Testes de erro

Define 15 testes focados apenas em cenários inválidos.

### Exercício 11 - Mensagens de utilizador

Reescreve mensagens técnicas para linguagem compreensível por utilizador final.

### Exercício 12 - Reflexão

Explica por que tratamento de erros faz parte da qualidade do software.

---

## 18 · Ficheiros: Acesso e Manipulação em C

Fonte: [18_ficheiros_acesso_e_manipulacao_em_c.md](./18_ficheiros_acesso_e_manipulacao_em_c.md)

### Exercício 1 - Escrita simples

Cria programa que grava 5 linhas num ficheiro texto.

### Exercício 2 - Leitura simples

Lê ficheiro linha a linha e imprime no ecrã.

### Exercício 3 - Cópia de ficheiro

Implementa cópia de um ficheiro texto para outro.

### Exercício 4 - Contagem

Conta número de linhas e caracteres de um ficheiro.

### Exercício 5 - Registos

Guarda registos de alunos no formato `nome;nota`.

### Exercício 6 - Pesquisa

Lê ficheiro e procura registo por nome.

### Exercício 7 - Acrescentar dados

Abre ficheiro em modo append e adiciona novos registos.

### Exercício 8 - Binário básico

Grava e lê array de inteiros em ficheiro binário.

### Exercício 9 - Validação de I/O

Melhora programa com tratamento de erro em cada operação de ficheiro.

### Exercício 10 - Navegação

Usa `fseek` e `ftell` para descobrir tamanho de ficheiro.

### Exercício 11 - Projeto curto

Cria mini agenda persistente em ficheiro (inserir/listar).

### Exercício 12 - Reflexão

Explica diferenças práticas entre guardar dados em texto e em binário.

---

## 19 · Funcionalidades de Editor de Texto (Produtividade e Debug)

Fonte: [19_editor_texto_produtividade_e_debug.md](./19_editor_texto_produtividade_e_debug.md)

### Exercício 1 - Atalhos avançados

Seleciona 15 atalhos do editor e aplica em tarefa real.

### Exercício 2 - Pipeline local

Configura build + run num único comando/tarefa no editor.

### Exercício 3 - Debug guiado

Coloca breakpoints em função com ciclo e analisa evolução de variáveis.

### Exercício 4 - Rastreio de bug

Recebe programa com erro lógico e usa debugger para localizar causa.

### Exercício 5 - Navegação

Num projeto com 8+ ficheiros, localiza rapidamente função e todas as referências.

### Exercício 6 - Refatoração

Renomeia função globalmente sem quebrar build.

### Exercício 7 - Extração

Extrai bloco repetido para função reutilizável.

### Exercício 8 - Qualidade

Cria checklist final de 12 pontos antes de entregar projeto.

### Exercício 9 - Métricas pessoais

Regista tempo gasto em tarefa antes e depois de configurar automações.

### Exercício 10 - Organização

Reorganiza projeto desestruturado em pastas claras (`src`, `include`, `bin`).

### Exercício 11 - Simulação de revisão

Faz revisão de código de colega usando ferramentas do editor.

### Exercício 12 - Reflexão

Explica como domínio de editor influencia qualidade e aprendizagem em C.

---
