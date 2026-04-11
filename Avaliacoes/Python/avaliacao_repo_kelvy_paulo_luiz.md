# Avaliação do Projeto

## Grupo

Kelvy, Paulo e Luiz

## Projeto

Jogo de Perguntas em Python

## Enquadramento da avaliação

Esta avaliação foi feita com base em:

- enunciado do projeto (`Python/11_projeto_final_python.md`);
- código do repositório (`main.py`, `menu.py`, `logica.py`);
- dados (`perguntas_facil.json`, `perguntas_medias.json`, `perguntas_dificil.json`);
- documentação entregue (`README.md`, `PLANIFICACAO.md`);
- testes de execução feitos durante a revisão.

## 1. Resultado geral

O projeto tem uma base funcional mínima: menu principal, escolha de nível, perguntas em JSON e soma de pontos. No entanto, o MVP obrigatório está incompleto e a robustez de inputs é baixa.

## 2. Evidências de funcionalidades concluídas

### 2.1 Estrutura por ficheiros

Foram usados ficheiros separados para:

- fluxo principal (`main.py`);
- interação no terminal (`menu.py`);
- leitura de JSON (`logica.py`);
- dados por dificuldade em ficheiros JSON.

### 2.2 Funcionalidades confirmadas

Foi confirmado no código e em execução:

- menu com jogar, regras/ajuda e sair;
- escolha de nível fácil/médio/difícil;
- carregamento de perguntas por ficheiro JSON de dificuldade;
- apresentação de perguntas e respostas com 4 opções;
- soma de pontos quando a resposta está correta;
- mensagem de fim de jogo e pontuação atual.

### 2.3 Dados das perguntas

Foi confirmado:

- `perguntas_facil.json`: 10 perguntas;
- `perguntas_medias.json`: 9 perguntas;
- `perguntas_dificil.json`: 11 perguntas.

## 3. Problemas encontrados (objetivos)

### 3.1 Robustez de input insuficiente

`menu_principal()` e `mostra_pergunta()` usam `int(input(...))` sem tratamento local.

Evidência em execução:

- ao introduzir `a` no menu principal, o programa termina com `ValueError`.

Impacto:

- o programa pode crashar com entradas inválidas simples.

### 3.2 MVP incompleto no resumo final

No fim da ronda, o programa mostra apenas pontuação acumulada.

Impacto:

- faltam número de certas, número de erradas e percentagem de acerto, que são requisitos obrigatórios.

### 3.3 Sem histórico de pontuações e sem Top 10

O projeto não grava resultados em `pontuacoes.json` nem apresenta ranking.

Impacto:

- não cumpre uma melhoria importante do enunciado e não permite acompanhar evolução dos jogadores.

### 3.4 Sem perguntas aleatórias

No fluxo de jogo, as perguntas são percorridas na ordem em que aparecem no JSON (`for pergunta in perguntas`), sem baralhamento.

Impacto:

- não cumpre o requisito de perguntas aleatórias por sessão.

### 3.5 Coerência parcial entre funções e uso real

A função `ajuda()` é importada em `main.py`, mas a opção de regras imprime texto diretamente no `main.py` em vez de chamar `ajuda()`.

Impacto:

- há lógica duplicada e funções pouco aproveitadas.

### 3.6 Gestão de pontuação entre partidas

`acumulacao_pontos` é global ao ciclo principal e mantém valor entre partidas.

Impacto:

- a pontuação pode acumular entre jogos diferentes, em vez de reiniciar por ronda.

### 3.7 Inconsistência nos dados de pontuação por dificuldade

Distribuição observada:

- fácil: todas as perguntas valem 10;
- médio: todas as perguntas valem 20;
- difícil: valores mistos (20, 30, 40, 50).

Impacto:

- falta consistência de regra de pontuação entre níveis.

## 4. Testes de execução feitos nesta revisão

Testes realizados:

- compilação com `python -m py_compile`: passou;
- execução com opção 3 (sair): passou;
- execução de uma ronda completa no nível fácil: passou;
- teste de input inválido no menu (`a`): falhou com `ValueError`.

## 5. Qualidade do código

### Pontos fortes

- estrutura simples e fácil de seguir;
- uso correto de JSON para perguntas;
- funções com nomes compreensíveis.

### Pontos a melhorar

- validação robusta de input em todos os pontos de entrada;
- completar requisitos do MVP no resumo final;
- implementar perguntas aleatórias, histórico e ranking;
- reduzir duplicação de lógica e melhorar integração das funções.

## 6. Qualidade da documentação

### O que foi entregue

- `README.md` com conteúdo muito curto;
- `PLANIFICACAO.md` com descrição inicial simples.

### O que falta

- relatório técnico (não encontrado no repositório);
- documentação de execução detalhada;
- plano de testes com resultados reais.

## 7. Avaliação final resumida

### Síntese

O grupo conseguiu montar um quiz básico funcional com níveis e pontuação. Isso demonstra entendimento inicial do problema.

No entanto, faltam componentes centrais do MVP e da robustez esperada: validação de inputs, resumo final completo, perguntas aleatórias e sistema de pontuações persistentes.

### Classificação qualitativa sugerida

**Projeto básico funcional, mas incompleto nos requisitos obrigatórios e com robustez insuficiente.**

### Feedback curto

A base do jogo existe e isso é um bom começo. O próximo passo é fechar os requisitos essenciais: impedir crashes com input inválido, mostrar resumo final completo, baralhar perguntas e guardar pontuações para ranking.
