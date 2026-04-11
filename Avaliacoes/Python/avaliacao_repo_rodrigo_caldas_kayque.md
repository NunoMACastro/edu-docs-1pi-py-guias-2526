# Avaliação do Projeto

## Grupo

Rodrigo Caldas e Kayque

## Projeto

Jogo de Perguntas em Python

## Enquadramento da avaliação

Esta avaliação teve em conta que se trata de um trabalho de alunos do 10.º ano e do primeiro projeto deste tipo. O objetivo não é avaliar como se fosse um projeto profissional, mas sim perceber o que já foi conseguido, o que está bem encaminhado e o que ainda precisa de ser melhorado.

## 1. Visão geral

O grupo desenvolveu um projeto de quiz em terminal com uma ideia bastante ambiciosa para um primeiro trabalho. Em vez de criar apenas um modo de jogo, tentou construir três modos diferentes:

- modo clássico;
- modo verdadeiro ou falso;
- modo bomba.

Além disso, o projeto inclui:

- pontuações separadas por modo;
- menus para navegar entre as várias partes;
- leitura de perguntas a partir de ficheiros JSON;
- pontuação diferente conforme a dificuldade.

Isto mostra ambição, criatividade e vontade de ir além do mínimo pedido.

## 2. Nível de implementação

### O que está implementado ou tentado

- menu principal;
- menu de escolha do modo de jogo;
- menu de visualização de pontuações;
- três tipos de quiz;
- leitura de perguntas a partir de vários ficheiros JSON;
- registo de pontuações por nome;
- sistema de pontuação por dificuldade;
- regras do jogo;
- perguntas aleatórias sem repetição dentro da sessão.

### Estado global

O projeto está num nível intermédio-alto em termos de ideias e quantidade de funcionalidades. Há bastante conteúdo e percebe-se claramente que houve trabalho real.

No entanto, a implementação final tem problemas importantes de robustez e pelo menos um erro de sintaxe sério que coloca em causa a execução direta do programa na forma em que foi entregue.

### Avaliação do nível de implementação

**Nível de implementação: bom nas ideias e nas funcionalidades tentadas, mas irregular na execução final.**

Ou seja, o grupo fez bastante, mas a entrega final ainda não está tão sólida como podia.

## 3. Pontos positivos

### 3.1 Ambição acima da média

Para um primeiro projeto, o grupo tentou fazer bastante mais do que o mínimo:

- vários modos de jogo;
- vários ficheiros de perguntas;
- vários ficheiros de pontuação;
- menus separados;
- regras detalhadas;
- pontuação por dificuldade.

Isto é claramente um ponto forte.

### 3.2 Boa quantidade de conteúdo

Os ficheiros JSON têm muitas perguntas. O modo clássico tem 50 perguntas, o modo bomba também tem 50 e o modo verdadeiro ou falso também tem 50. Isto enriquece bastante o projeto e mostra investimento no conteúdo do jogo.

### 3.3 Separação por responsabilidade

O grupo tentou separar o projeto em ficheiros com papéis diferentes:

- `main.py` para o fluxo principal;
- `menu.py` para os menus;
- `logica.py` para funções de apoio e da jogabilidade;
- ficheiros JSON para dados.

Esta divisão é uma boa decisão para o nível de escolaridade em causa.

### 3.4 Uso de conceitos certos

Foram usados vários conceitos adequados:

- listas e dicionários;
- ficheiros JSON;
- ciclos;
- funções;
- aleatoriedade;
- validação básica;
- pontuação acumulada.

As escolhas estão bem alinhadas com o que se espera num primeiro projeto de Python.

## 4. Problemas encontrados

### 4.1 Erro de sintaxe importante

Em `logica.py`, na função `mostrar_regras()`, existe uma `f-string` com aspas internas que, na forma em que está escrita, tem forte probabilidade de causar erro de sintaxe:

```python
print(f"se escrever {"1"} e apertar enter vai para o menu jogar,")
```

Isto é um problema importante porque pode impedir o programa de arrancar corretamente.

### 4.2 `main.py` tem demasiado código direto

O `main.py` concentra quase todo o fluxo do programa:

- pede o nome;
- controla os menus;
- escolhe modos;
- percorre perguntas;
- soma pontos;
- guarda pontuação;
- trata vários erros.

Funciona como um grande bloco principal, mas para um projeto organizado seria melhor dividir mais em funções. Neste momento, o ficheiro está grande e mais difícil de ler e manter.

### 4.3 Pouca reutilização

O código dos três modos de jogo é bastante repetido. A estrutura de:

- carregar perguntas;
- criar lista aleatória;
- percorrer perguntas;
- calcular pontos;
- guardar pontuação;

aparece várias vezes com pequenas mudanças. Isto faz com que o programa funcione, mas aumenta a repetição e dificulta correções futuras.

### 4.4 Falta de contadores de certas e erradas no resumo

O enunciado pedia claramente resumo final com:

- pontuação total;
- número de certas e erradas;
- percentagem de acerto.

Neste projeto, o foco está muito na pontuação, mas o resumo final não parece incluir esses dados de forma clara no fluxo principal. Isso significa que uma parte importante do MVP não está fechada da melhor forma.

### 4.5 Algumas validações ainda são limitadas

Há esforço de tratamento de erros, mas ainda com limitações:

- as opções do menu são tratadas quase sempre com `if/elif`, sem uma validação mais consistente;
- se o utilizador escrever respostas fora do esperado, algumas partes apenas consideram erro e seguem em frente;
- há muitos `input()` usados como pausa, o que pode tornar o programa menos fluido.

### 4.6 Registo de pontuação pode sobrescrever resultados

As pontuações são guardadas num dicionário com o nome do jogador como chave. Isso significa que, se a mesma pessoa jogar novamente, o novo valor substitui o anterior em vez de guardar histórico de várias partidas. Para um primeiro projeto não é grave, mas é uma limitação importante.

## 5. Qualidade do código

### Avaliação geral

**Qualidade do código: média.**

### O que está bem

- o código mostra lógica;
- as funções têm objetivos claros;
- existe estrutura modular;
- o projeto tem bastante conteúdo;
- os modos de jogo diferenciam-se de forma criativa.

### O que precisa de melhorar

- há repetição excessiva;
- o `main.py` está demasiado carregado;
- há pelo menos um erro de sintaxe sério;
- faltam mais funções pequenas para dividir melhor responsabilidades;
- alguns nomes e mensagens podiam estar mais consistentes.

No geral, não é um código fraco, mas ainda está pouco polido.

## 6. Qualidade da documentação e comentários

### Manual Técnico

O repositório inclui um `Manual_tecnico.md`, o que é positivo. O manual identifica:

- os ficheiros;
- os modos de jogo;
- várias funções;
- o objetivo de cada parte.

Isto ajuda a perceber o projeto e mostra preocupação em documentar.

### Limitações

Mesmo assim, a documentação ainda tem alguns problemas:

- está muito resumida em certos pontos;
- tem várias gralhas e frases pouco cuidadas;
- explica a intenção geral, mas não analisa muito o que ficou menos conseguido;
- o README é demasiado curto e quase não explica como executar o projeto.

### Comentários no código

Os comentários são poucos. Como o `main.py` é grande, mais comentários ou uma melhor divisão em funções teriam ajudado bastante.

### Avaliação

**Documentação e comentários: razoáveis.**
Existe documentação, o que é bom, mas ainda precisa de mais clareza e mais cuidado.

## 7. Extras implementados

Este é um dos pontos mais fortes do projeto.

Extras claros:

- modo verdadeiro ou falso;
- modo bomba;
- pontuações separadas por modo;
- regras detalhadas;
- sistema de pontuação por dificuldade.

Isto deve ser valorizado, porque mostra criatividade e vontade de enriquecer a experiência do utilizador.

## 8. Nível das soluções encontradas

As soluções são, em geral, boas para o nível do 10.º ano:

- usar JSON para perguntas;
- usar JSON para pontuações;
- usar `random.choice` e controlo manual para evitar repetição;
- adaptar a jogabilidade conforme o modo.

O grupo mostra que não ficou preso ao mínimo. Tentou criar mecânicas diferentes, o que é bastante positivo.

Ao mesmo tempo, algumas soluções ainda são pouco refinadas:

- muita lógica repetida;
- pouca abstração;
- resumo final incompleto;
- pontuações guardadas de forma limitada.

## 9. Coerência do projeto

O projeto é coerente na sua identidade:

- é claramente um quiz;
- tem menus bem definidos;
- os três modos fazem sentido;
- a dificuldade influencia os pontos;
- os ficheiros de dados estão bem alinhados com os modos.

Essa coerência geral é um ponto forte.

O que falha mais é a coerência técnica do acabamento:

- um erro de sintaxe pode comprometer o arranque;
- o resumo final não cobre tudo o que era pedido;
- a estrutura podia estar mais limpa.

## 10. Outros pontos importantes

### 10.1 Criatividade

O modo bomba é uma ideia engraçada e dá personalidade ao projeto. Isso é importante, porque mostra que o grupo não fez apenas uma cópia básica do enunciado.

### 10.2 Conteúdo bem preparado

Ter 50 perguntas em cada modo é um excelente sinal de esforço.

### 10.3 Falta de polimento final

Este projeto beneficiava muito de uma última fase de:

- corrigir erros de sintaxe;
- rever o resumo final;
- reduzir repetição;
- melhorar o README;
- testar tudo de ponta a ponta.

Com essa revisão, podia subir bastante de nível.

## 11. Avaliação final resumida

### Síntese

Este grupo apresentou um projeto criativo, ambicioso e com bastante trabalho visível. A quantidade de conteúdo, os vários modos de jogo e a tentativa de organizar o código por ficheiros mostram empenho e boas ideias.

Ao mesmo tempo, a execução final ainda tem falhas importantes, sobretudo a nível de robustez, repetição de código e acabamento técnico. A base é boa e está acima da média em ambição, mas ainda precisava de mais revisão para ficar realmente sólida.

### Classificação qualitativa sugerida

**Projeto bom e criativo, com extras interessantes, mas ainda com falhas de execução e de acabamento.**

### Feedback curto para os alunos

Fizeram um projeto com muita personalidade e com mais ambição do que seria normal num primeiro trabalho. Isso é muito positivo. O passo seguinte é aprender a transformar boas ideias em código mais limpo e mais estável: dividir melhor o `main.py`, evitar repetição, corrigir erros de sintaxe e fechar melhor o resumo final do jogo.
