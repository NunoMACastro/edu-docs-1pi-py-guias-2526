# Avaliação do Projeto

## Grupo

Diogo: 14
Davi: 13
Mateus Bitar: 13

## Projeto

Jogo de Perguntas em Python

## Enquadramento da avaliação

Esta avaliação foi feita com base em:

- enunciado do projeto (`Python/11_projeto_final_python.md`);
- código do repositório (`menu.py`, `logica.py`, `files.py`, `sucesso.py`, `perguntas.json`, `pontuacoes.json`);
- documentação entregue no repositório (`RELATORIO.MD`);
- testes de execução feitos durante a revisão.

## 1. Resultado geral

O projeto tem uma base de dados de perguntas forte e já inclui menu, ajuda, dificuldade e Top 10. No entanto, o ciclo principal de jogo ainda não está concluído, por isso o MVP não está completo.

## 2. Evidências de funcionalidades concluídas

### 2.1 Estrutura por ficheiros

O projeto está dividido em vários ficheiros:

- `menu.py` para interação no terminal;
- `logica.py` para dificuldade e ordenação de pontuações;
- `files.py` para leitura e escrita de JSON;
- `sucesso.py` para testes de mensagens de rank.

### 2.2 Funcionalidades confirmadas

Foi possível confirmar:

- menu com opções Jogar, Pontuações, Regras/Ajuda e Sair (`menu.py`);
- menu de ajuda funcional (`menu.py`, função `mostrar_ajuda`);
- carregamento de perguntas de `perguntas.json` (`files.py`, `importar_perguntas`);
- sorteio de 10 perguntas por dificuldade com `random.sample` (`logica.py`, `escolher_dificuldade`);
- visualização de Top 10 com ordenação por pontuação (`logica.py`, `mostrar_top10` + menu opção 2).

### 2.3 Dados do jogo

`perguntas.json` contém:

- 50 perguntas no total;
- 5 categorias com 10 perguntas cada;
- dificuldades Fácil, Médio e Difícil;
- campos necessários para o jogo (`pergunta`, `Opções`, `Resposta_correta`, `Categoria`, `Dificuldade`).

## 3. Problemas encontrados (objetivos)

### 3.1 Modo de jogo incompleto

Na opção `1 | Jogar` em `menu.py`:

- o programa chama `escolher_dificuldade()`;
- define uma função interna `mostrar_pergunta()`;
- não executa ciclo de perguntas com validação de respostas e soma de pontos.

Impacto:

- a jogabilidade principal não está concluída.

### 3.2 Chamada de jogo no import de módulo

No fim de `logica.py` existe `escolher_dificuldade()` fora de função.

Impacto:

- ao abrir `menu.py`, o utilizador é forçado a escolher dificuldade antes de aparecer o menu principal.

### 3.3 Saída de debug no terminal

`escolher_dificuldade()` imprime a lista completa de dicionários das perguntas sorteadas (`print(perguntas_...)`).

Impacto:

- interface do jogo fica poluída e mostra dados internos que não deviam aparecer ao utilizador final.

### 3.4 MVP incompleto em critérios obrigatórios

Com base no enunciado, faltam partes obrigatórias:

- ronda de perguntas totalmente funcional;
- resumo final com pontuação total, certas, erradas e percentagem;
- fluxo de re-jogar no fim da partida com resultados da ronda.

### 3.5 Validação de utilizador insuficiente

Em `menu.py`, `utilizador = input(...)` é aceite sem validação (nome vazio é aceite).

Impacto:

- o menu pode apresentar “Olá . Bem vindo...”, o que mostra falta de validação mínima.

### 3.6 Mensagens e legibilidade

Existem vários `print` com sequências como `"\================================================/"`, gerando `SyntaxWarning` no Python atual. Existe também uma mensagem inadequada para contexto escolar na opção inválida.

Impacto:

- baixa qualidade de apresentação e experiência do utilizador.

### 3.7 Escrita de pontuações não integrada no fluxo do jogo

`files.py` tem `guardar_pontuacuao`, mas o fluxo principal de `menu.py` não regista resultados de uma ronda jogada, porque a ronda não está completa.

Impacto:

- histórico não reflete novas partidas reais.

### 3.8 Código de teste separado e não integrado

`sucesso.py` é um script de testes de rank isolado do jogo principal.

Impacto:

- não acrescenta funcionalidade ao fluxo final entregue.

## 4. Testes de execução feitos nesta revisão

Testes realizados:

- compilação com `python -m py_compile`: passou (com vários `SyntaxWarning` em `menu.py`);
- execução de `menu.py`: passou;
- fluxo menu opção 2 (Top 10): passou;
- fluxo menu opção 1 (Jogar): não inicia ronda completa de perguntas.

## 5. Qualidade do código

### Pontos fortes

- base de perguntas bem preenchida e estruturada;
- uso correto de JSON e `random.sample`;
- tentativa de modularização em vários ficheiros.

### Pontos a melhorar

- fechar o ciclo principal de jogo;
- remover execução automática de lógica no import;
- melhorar validações de input;
- remover prints de debug e rever mensagens do utilizador;
- alinhar scripts de teste com a entrega final.

## 6. Qualidade da documentação

O repositório inclui `RELATORIO.MD`, mas está muito curto para uma entrega final.

Pontos objetivos:

- não descreve com detalhe o estado real do MVP;
- não apresenta plano de testes manual com casos e resultados;
- não documenta claramente o que ficou por concluir.

## 7. Avaliação final resumida

### Síntese

O grupo demonstrou esforço na organização inicial e na preparação de conteúdo (perguntas e pontuações). As partes de menu, ajuda, dificuldade e Top 10 existem e funcionam.

A parte principal do projeto, que é jogar uma ronda completa com avaliação de respostas e resumo final, ainda não ficou concluída. Por esse motivo, o projeto fica abaixo do nível esperado para MVP fechado.

### Classificação qualitativa sugerida

**Projeto com boa base de conteúdo e organização inicial, mas com MVP incompleto na jogabilidade principal.**

### Feedback curto

A base do projeto está montada e as perguntas estão bem preparadas. O próximo passo é concluir o essencial: ronda completa de jogo, validação de respostas, soma de pontos e resumo final. Depois disso, devem fazer uma revisão final de mensagens, validações e documentação.
