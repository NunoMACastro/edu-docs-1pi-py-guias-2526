# Avaliação do Projeto

## Grupo

Rodrigo Caldas e Kayque

## Projeto

Jogo de Perguntas em Python

## Enquadramento da avaliação

Esta avaliação foi feita com base em:

- enunciado do projeto (`Python/11_projeto_final_python.md`);
- código do repositório (`main.py`, `menu.py`, `logica.py`);
- dados (`perguntas.json`, `perguntas_bomba.json`, `verdadeiro_falso.json` e ficheiros de pontuação);
- documentação (`Manual_tecnico.md`, `PLANIFICACAO.MD`, `README.md`);
- testes de execução feitos durante a revisão.

## 1. Resultado geral

O projeto está funcional no ambiente testado e inclui vários extras relevantes para o nível da turma. O grupo implementou três modos de jogo e separou os dados por ficheiro.

O ponto principal a melhorar é o fecho do MVP obrigatório no fim de cada ronda, sobretudo no resumo final e no sistema de pontuações.

## 2. Evidências de funcionalidades concluídas

### 2.1 Estrutura e organização

O projeto usa vários ficheiros com responsabilidades diferentes:

- `main.py`: fluxo principal;
- `menu.py`: menus do terminal;
- `logica.py`: regras de jogo, pontuação e leitura de informação;
- ficheiros JSON separados por modo e pontuações.

### 2.2 Funcionalidades confirmadas

Foi possível confirmar no código e em execução:

- menu principal com jogar, pontuação, regras e sair;
- submenu para escolher modo de jogo;
- três modos implementados: clássico, verdadeiro/falso e bomba;
- perguntas aleatórias sem repetição na sessão (`random.choice` com controlo em lista);
- pontuação por dificuldade (fácil 1, médio 2, difícil 3);
- registo de pontuação por modo em ficheiros JSON separados;
- possibilidade de voltar ao menu e jogar novamente sem reiniciar o programa.

### 2.3 Dados de perguntas

Foram confirmados:

- `perguntas.json`: 50 perguntas;
- `perguntas_bomba.json`: 50 perguntas;
- `verdadeiro_falso.json`: 50 perguntas.

Cada modo tem quantidade suficiente para selecionar 15 perguntas aleatórias por ronda.

## 3. Problemas encontrados (objetivos)

### 3.1 Resumo final do MVP incompleto

No fim das rondas, o programa mostra apenas a pontuação final.

Impacto:

- não mostra número de certas, número de erradas e percentagem de acerto, que são requisitos explícitos do MVP.

### 3.2 Sistema de pontuações sem histórico por partida

A função `guardar_info` grava pontuação num dicionário com o nome como chave. Se o mesmo nome jogar outra vez, o valor anterior é substituído.

Impacto:

- não existe histórico de múltiplas partidas por jogador.

### 3.3 Ecrã de pontuação não mostra Top 10

`mostrar_info` apresenta todos os registos e destaca o maior valor, mas não calcula nem apresenta uma tabela Top 10 ordenada.

Impacto:

- a melhoria "Top 10" não está implementada no formato pedido no enunciado.

### 3.4 Robustez de erros com `except` genérico

No fluxo de pontuações em `main.py` existe `except:` genérico.

Impacto:

- dificulta perceber a causa real do erro e torna o comportamento menos previsível.

### 3.5 Legibilidade e manutenção

`main.py` concentra muitas responsabilidades no mesmo bloco.

Impacto:

- aumenta repetição de código entre modos e dificulta manutenção.

### 3.6 Documentação curta em partes críticas

Existe `Manual_tecnico.md`, mas o `README.md` está muito curto para orientar execução e objetivos do projeto.

Impacto:

- reduz clareza para quem lê o repositório pela primeira vez.

## 4. Testes de execução feitos nesta revisão

Testes realizados:

- compilação com `python -m py_compile`: passou no ambiente testado;
- execução do menu principal e saída: passou;
- execução de ronda de jogo (modo clássico): passou;
- consulta de pontuações por modo: passou.

Observação:

- no ambiente testado, o código compila e corre. Ainda assim, há pontos de melhoria de robustez e de fecho do MVP.

## 5. Qualidade do código

### Pontos fortes

- boa quantidade de funcionalidades para primeiro projeto;
- criatividade com três modos diferentes;
- separação de dados por ficheiros JSON;
- uso de lógica de pontuação por dificuldade.

### Pontos a melhorar

- reduzir repetição entre modos;
- dividir melhor o fluxo principal em funções menores;
- substituir `except` genérico por erros específicos;
- completar resumo final obrigatório do MVP.

## 6. Qualidade da documentação

### O que foi entregue

- `Manual_tecnico.md` com descrição de ficheiros e funções;
- `PLANIFICACAO.MD`;
- `README.md`.

### Pontos a melhorar

- `README.md` precisa de instruções mais claras de execução;
- documentação pode indicar com mais detalhe o que está concluído e o que ficou em falta.

## 7. Avaliação final resumida

### Síntese

O grupo apresentou um projeto funcional, com volume de conteúdo elevado e criatividade acima da média para o nível da turma. Os três modos de jogo são um ponto forte claro.

Para fechar melhor o trabalho, falta completar o resumo final do MVP e melhorar o sistema de pontuações para histórico e Top 10.

### Classificação qualitativa sugerida

**Projeto bom e criativo, com vários extras funcionais, mas com requisitos do MVP ainda por fechar no resumo final e no ranking.**

### Feedback curto

A base do projeto é forte e os três modos mostram empenho real. O próximo passo é consolidar o essencial: no fim de cada jogo, mostrar certas, erradas e percentagem, e melhorar a gestão das pontuações para histórico e Top 10.
