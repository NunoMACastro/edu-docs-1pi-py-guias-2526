![Header](../../Images/Header.png)

# Avaliação do Projeto

## Grupo

Afonso: 17
Rodrigo Poça: 13
Mateus: 16

## Projeto

Jogo de Perguntas em Python

## Enquadramento da avaliação

Esta avaliação foi feita com base em:

- enunciado do projeto (`Python/11_projeto_final_python.md`);
- código do repositório (`main.py`, `menu.py`, `logica.py`, `files.py`, `perguntas.json`, `pontuacoes.json`);
- documentação entregue (`PLANIFICACAO.md`, `RELATORIO.md`, `README.MD`);
- testes de execução feitos durante a revisão.

## 1. Resultado geral

O projeto cumpre a maior parte do MVP e implementa melhorias relevantes (dificuldade, Top 10 e pontuação por dificuldade). O programa compila e executa no ambiente testado.

## 2. Evidências de funcionalidades concluídas

### 2.1 Estrutura por módulos

Está implementada separação por ficheiros:

- `main.py` arranca o programa;
- `menu.py` trata menu e fluxo principal;
- `logica.py` trata dificuldade, pontuação e top;
- `files.py` trata leitura e escrita de JSON.

### 2.2 MVP

Critérios do MVP confirmados no código:

- menu principal com jogar, ajuda e sair (`menu.py`, função `mostrar_menu`);
- perguntas lidas de `perguntas.json` (`files.py`, função `importar_perguntas`);
- seleção aleatória de perguntas sem repetição na sessão (`logica.py`, `random.sample`);
- jogo com pontuação acumulada (`menu.py` + `logica.py`, função `somar_pontuacao`);
- resumo final com pontuação, certas, erradas e percentagem (`menu.py`, função `sucesso`);
- opção de re-jogar sem reiniciar o programa (`menu.py`, pergunta "Pretende voltar a jogar? (S/N)").

### 2.3 Melhorias (Nível 2 e além)

Funcionalidades extra confirmadas:

- escolha de dificuldade (`logica.py`, função `escolher_dificuldade`);
- histórico de pontuações em `pontuacoes.json` (`files.py`, função `guardar_pontuacuao`);
- visualização de Top 10 (`logica.py`, função `mostrar_top10` + menu opção 2);
- pontuação por dificuldade (5/10/20 pontos em `somar_pontuacao`).

### 2.4 Dados de perguntas

`perguntas.json` contém:

- 50 perguntas no total;
- 5 categorias com 10 perguntas cada;
- dificuldades distribuídas por Fácil, Médio e Difícil;
- campos essenciais usados pelo programa (`pergunta`, `Opções`, `Resposta_correta`, `Categoria`, `Dificuldade`).

## 3. Problemas encontrados (objetivos)

### 3.1 Validação de resposta incompleta

Em `menu.py` (`mostrar_pergunta`), a validação aceita qualquer número `<= 4`. Isto permite valores `0` e negativos.

Impacto:

- entradas fora do intervalo 1..4 são aceites como se fossem respostas válidas.

### 3.2 Validação do conteúdo de perguntas incompleta

O enunciado pede validação básica da estrutura das perguntas. Em `files.py` (`importar_perguntas`) o ficheiro é carregado, mas não existe validação dos campos obrigatórios por pergunta.

Impacto:

- com JSON mal formado, o erro só aparece mais tarde durante o jogo.

### 3.3 Tratamento de erro de ficheiro pode falhar no fluxo seguinte

Quando há `FileNotFoundError` ou `JSONDecodeError`, `importar_perguntas` e `importar_pontuacao` apenas imprimem mensagem e não devolvem estrutura segura.

Impacto:

- funções seguintes podem receber `None` e gerar erro em tempo de execução.

### 3.4 Inconsistência entre plano e implementação

No `PLANIFICACAO.md` aparecem funções planeadas como `sortear_perguntas_facil`, `sortear_perguntas_medio`, `realizar_pergunta` e `mostrar_pontuacao`. No código final essas funções não existem com esses nomes ou responsabilidades.

Impacto:

- documentação de planeamento não corresponde totalmente à implementação final.

### 3.5 Nomes e assinatura de função com erro ortográfico

A função `guardar_pontuacuao` está com nome mal escrito e recebe parâmetro `f` que não é usado (`files.py`).

Impacto:

- reduz clareza do código e pode gerar confusão na manutenção.

### 3.6 Compatibilidade de versão Python

Em `menu.py`, a string `f"... {question["Resposta_correta"]+1}"` funciona em Python 3.12+.

Impacto:

- em versões mais antigas pode causar erro de sintaxe.

## 4. Testes de execução feitos nesta revisão

Testes realizados:

- compilação dos ficheiros com `python -m py_compile`: passou;
- execução do fluxo "entrar no menu e sair": passou;
- execução de uma ronda completa de jogo com 10 perguntas e re-jogar: passou;
- consulta de pontuações após jogo: passou.

## 5. Qualidade do código

### Pontos fortes

- estrutura modular clara;
- funcionalidades principais implementadas;
- lógica de jogo e pontuação funcional;
- uso correto de JSON e `random.sample`.

### Pontos a melhorar

- validação de inputs mais rigorosa (intervalo e casos inválidos);
- validação estrutural dos dados lidos do JSON;
- alinhamento entre documentação e implementação final;
- uniformização de nomes de funções.

## 6. Qualidade da documentação

Documentos entregues e úteis:

- `README.MD`;
- `PLANIFICACAO.md`;
- `RELATORIO.md`.

Observações objetivas:

- há explicação da organização e das funções;
- o plano contém tabela de responsabilidades;
- parte do plano não coincide totalmente com as funções finais do código.

## 7. Avaliação final resumida

### Síntese

O grupo entregou um projeto funcional, com MVP amplamente cumprido e com melhorias relevantes para o contexto do 10.º ano. O trabalho mostra organização por módulos, dados bem estruturados e execução real do jogo.

Os pontos de melhoria estão concentrados na robustez (validação de entradas e dados) e na consistência entre planificação e implementação final.

### Classificação qualitativa sugerida

**Projeto bom, funcional e com extras relevantes, com melhorias necessárias na robustez e na consistência documental.**

### Feedback curto

Conseguiram entregar um jogo funcional com várias partes importantes do enunciado e extras úteis. O próximo passo é reforçar a robustez: validar melhor respostas e ficheiros, e manter a documentação totalmente alinhada com o código final.

![Footer](../../Images/Footer.png)
