# Avaliação do Projeto

## Grupo

Mateus Bitar, Davi e Diogo

## Projeto

Jogo de Perguntas em Python

## Enquadramento da avaliação

Esta avaliação teve em conta que se trata de um trabalho de alunos do 10.º ano e do primeiro projeto deste tipo. O objetivo não é avaliar como se fosse um projeto profissional, mas sim perceber o que já foi conseguido, o que está bem encaminhado e o que ainda precisa de ser melhorado.

## 1. Visão geral

O grupo desenvolveu um jogo de perguntas em terminal com:

- menu principal;
- escolha de dificuldade;
- leitura de perguntas a partir de JSON;
- seleção aleatória de 10 perguntas;
- consulta de pontuações;
- ficheiros separados por responsabilidade.

A ideia do projeto está alinhada com o enunciado e percebe-se claramente a intenção de organizar o programa em módulos. Há também um volume interessante de perguntas no ficheiro JSON, o que mostra trabalho real na preparação de conteúdos.

Ao mesmo tempo, a implementação final revela problemas importantes de execução, de acabamento e de robustez. Ou seja, o grupo conseguiu avançar na construção do projeto, mas a versão entregue ainda parece mais uma base de trabalho do que um produto final estável.

## 2. Nível de implementação

### O que está implementado ou tentado

- menu com opções principais;
- ajuda/regras;
- escolha de dificuldade;
- carregamento de perguntas de um ficheiro JSON;
- sorteio aleatório de 10 perguntas;
- top de pontuações;
- separação em vários ficheiros Python;
- ficheiro de pontuações.

### Estado global

O projeto está num nível intermédio. Existe bastante estrutura, existem dados, existe lógica pensada e há tentativa de cumprir várias partes do enunciado. No entanto, o estado real do código mostra que faltam partes essenciais para o jogo estar verdadeiramente fechado.

### Avaliação do nível de implementação

**Nível de implementação: razoável, mas incompleto e pouco consolidado.**

O grupo conseguiu construir uma boa base, mas há demasiados sinais de código inacabado, testes insuficientes e problemas de execução para considerar que o projeto ficou totalmente concluído.

## 3. Pontos positivos

### 3.1 Organização por ficheiros

O projeto foi dividido em ficheiros com funções diferentes:

- `files.py` para leitura e escrita;
- `logica.py` para a lógica principal;
- `menu.py` para interação com o utilizador;
- `sucesso.py` para testes de mensagens finais.

Para um primeiro projeto, esta tentativa de separação é positiva e mostra que o grupo não fez tudo num único ficheiro.

### 3.2 Quantidade de perguntas

O ficheiro `perguntas.json` tem um conjunto grande de perguntas, distribuídas por categorias e dificuldades. Isso é um ponto forte porque torna o jogo mais rico e mais interessante.

### 3.3 Uso de conceitos importantes

O grupo aplicou vários conteúdos relevantes:

- listas e dicionários;
- leitura de JSON;
- ordenação com `sorted`;
- aleatoriedade com `random.sample`;
- menus e ciclos;
- tratamento de alguns erros com `try/except`.

Isto mostra aprendizagem real e aplicação dos conteúdos dados em aula.

## 4. Problemas encontrados

### 4.1 Problemas sérios de formatação e sintaxe

O maior problema deste projeto é que vários ficheiros surgem praticamente todos numa linha ou com formatação muito degradada. Isso dificulta muito a leitura e levanta dúvidas sobre o estado real da execução.

Há também vários indícios de erros de sintaxe ou de escrita:

- `guardar_pontuacuao` tem o nome mal escrito;
- mensagens de texto aparecem partidas a meio;
- há caracteres de barra invertida e decoração de terminal mal organizados;
- a função `mostrar_pergunta` aparece definida dentro de outra parte do menu e parece ficar incompleta;
- no fim de `menu.py` há uma chamada direta a `mostrar_menu()` sem proteção do arranque do programa.

Mesmo que parte disto possa vir de má formatação do repositório, a entrega final deveria estar limpa e legível.

### 4.2 Lógica do jogo incompleta

O projeto consegue escolher dificuldade e sortear perguntas, mas a parte mais importante do jogo, que é mostrar cada pergunta, receber resposta, validar e somar pontos de forma clara, não está bem fechada no código entregue.

No relatório em PDF, o próprio grupo diz que o programa funciona “com ausência do MVP”, o que é uma admissão importante: o núcleo obrigatório do projeto não está totalmente concluído.

### 4.3 Separação de responsabilidades ainda fraca

Apesar da existência de módulos, ainda há mistura entre interface e lógica:

- a escolha da dificuldade está dentro de `logica.py`, quando devia ser controlada pelo menu;
- há imports feitos dentro de menus e dependências muito diretas entre ficheiros;
- a navegação do programa não parece estar centralizada de forma clara.

Ou seja, houve tentativa de modularização, mas ainda sem grande consistência.

### 4.4 Robustez limitada

Existe algum tratamento de erros com `try/except`, o que é positivo. Mesmo assim:

- a validação do nome do utilizador é fraca;
- não se vê um fluxo sólido de recuperação de erro em várias partes;
- o jogo depende bastante de o utilizador introduzir valores certos;
- não fica claro que todas as perguntas/respostas estejam mesmo ligadas ao cálculo de pontuação.

### 4.5 Código de teste misturado com o projeto

O ficheiro `sucesso.py` parece mais um teste manual de rankings do que uma parte integrada do jogo. Isso não é necessariamente mau como experiência, mas não devia aparecer como se fosse parte normal da entrega final sem explicação clara.

## 5. Qualidade do código

### Avaliação geral

**Qualidade do código: média-baixa.**

### O que está bem

- há divisão por funções e módulos;
- o grupo tentou usar nomes que indicam intenção;
- há aplicação de estruturas de dados adequadas;
- o JSON está suficientemente rico para suportar o jogo.

### O que precisa de melhorar

- legibilidade muito fraca em vários ficheiros;
- falta de consistência nos nomes;
- funções incompletas ou mal integradas;
- pouco acabamento final;
- sinais de falta de revisão antes da entrega.

A principal sensação ao ler o código é que houve trabalho, mas faltou uma última fase de organizar, limpar e testar.

## 6. Qualidade da documentação e comentários

### Relatório

O grupo entregou relatório, o que é positivo. O relatório explica:

- quem fez parte do grupo;
- a ideia geral do projeto;
- os ficheiros;
- as funções;
- a distribuição de tarefas.

Isto ajuda a perceber a intenção e a estrutura do trabalho.

### Limitações

No entanto, a documentação apresenta alguns problemas:

- linguagem pouco cuidada em vários pontos;
- explicações algo vagas;
- admite que falta o MVP, mas não explica com clareza o que ficou por fazer;
- não mostra um plano de testes sólido;
- não evidencia bem as dificuldades técnicas encontradas.

### Comentários no código

Os comentários existem, mas são poucos e em muitos casos não compensam a fraca legibilidade do código.

### Avaliação

**Documentação e comentários: razoáveis, mas abaixo do desejável para uma entrega final.**

## 7. Extras implementados

O grupo tentou ir além do mínimo com:

- dificuldades;
- top de pontuações;
- várias categorias;
- grande conjunto de perguntas;
- teste de ranks no ficheiro `sucesso.py`.

Isto deve ser valorizado, porque mostra vontade de enriquecer o projeto.

O problema é que os extras acabam por não compensar a falta de solidez da parte principal do jogo.

## 8. Nível das soluções encontradas

As soluções escolhidas são adequadas ao nível de um primeiro projeto:

- JSON para guardar perguntas;
- `random.sample` para evitar repetições numa sessão;
- `sorted` para o top;
- menu por opções numéricas.

São escolhas corretas e apropriadas ao contexto.

Portanto, o problema não está nas ideias. Está sobretudo na execução, integração e revisão final.

## 9. Coerência do projeto

O projeto é coerente na intenção:

- entrar no menu;
- escolher dificuldade;
- carregar perguntas;
- jogar;
- ver pontuações.

Essa linha existe.

Mas a coerência prática falha porque algumas partes essenciais não estão verdadeiramente fechadas no código. Há distância entre o que o relatório diz que o projeto faz e aquilo que se consegue confirmar com segurança ao ler a implementação.

## 10. Outros pontos importantes

### 10.1 Boa base de dados de perguntas

O conjunto de perguntas é um dos pontos mais fortes do trabalho. Mostra esforço e torna o jogo mais completo.

### 10.2 Falta de acabamento

O projeto precisava claramente de mais uma fase de polimento:

- rever sintaxe;
- corrigir formatação;
- testar o fluxo completo;
- confirmar que todas as opções do menu levam a funcionalidades realmente concluídas.

### 10.3 Potencial de melhoria

Este projeto não está longe de poder melhorar bastante. Com revisão, simplificação e fecho da lógica do jogo, podia subir de forma clara.

## 11. Avaliação final resumida

### Síntese

O grupo mostrou empenho, criou uma boa base de perguntas e organizou o projeto em vários ficheiros, o que é bastante positivo para um primeiro trabalho. Também tentou implementar extras interessantes e usou conceitos importantes da disciplina.

No entanto, a entrega final ainda tem problemas relevantes de legibilidade, robustez e completude. O mais importante é que a parte central do jogo não transmite segurança suficiente como MVP concluído.

### Classificação qualitativa sugerida

**Projeto com boa base e bom esforço, mas ainda incompleto e com falta de revisão final.**

### Feedback curto para os alunos

Mostraram boas ideias e perceberam bem a estrutura geral do problema. O que vos falta agora é aprender a fechar melhor um projeto: deixar o código limpo, garantir que o jogo principal está mesmo concluído, testar o fluxo inteiro e rever a apresentação final. A base está lá, mas precisa de mais solidez.
