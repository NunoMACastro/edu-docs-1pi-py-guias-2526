# Avaliação do Projeto

## Grupo

Domingos: 11
Enzo: 11

## Projeto

Quiz Python

## Enquadramento da avaliação

Esta avaliação foi feita com base em:

- enunciado do projeto (`Python/11_projeto_final_python.md`);
- código do repositório (`main.py`, `logica_jogo.py`, `utils.py`);
- dados (`perguntas.json`, `pontuacoes.json`);
- documentação (`README.md`, `PLANIFICACAO.md`, `PlanificationFR.md`);
- testes de execução feitos durante a revisão.

## 1. Resultado técnico geral

O projeto está funcional e bem organizado para o nível da turma. A estrutura por módulos está clara, o jogo executa sem crash nos testes realizados e inclui melhorias úteis (categoria, dificuldade, explicação e ranking).

## 2. Evidências de funcionalidades concluídas

### 2.1 Estrutura e organização

O projeto está dividido em:

- `main.py` para fluxo principal do jogo;
- `logica_jogo.py` para leitura, filtragem, gravação e ranking;
- `utils.py` para validação de entradas e utilitários.

### 2.2 Funcionalidades confirmadas

Foi confirmado no código e em execução:

- menu principal com iniciar partida, classificação e sair;
- pedido de nome do utilizador;
- escolha de categoria e dificuldade;
- seleção aleatória de perguntas (`random.shuffle`);
- validação numérica de respostas;
- feedback de correto/incorreto com explicação;
- gravação de resultados em `pontuacoes.json`;
- visualização de Top 10 ordenado por pontuação.

### 2.3 Dados do jogo

`perguntas.json` contém 80 perguntas com estrutura consistente:

- `id`, `pergunta`, `opcoes`, `resposta`, `categoria`, `dificuldade`, `explicacao`.

## 3. Problemas encontrados (objetivos)

### 3.1 Menu principal não cumpre totalmente o MVP obrigatório

No enunciado, o menu principal obrigatório inclui Regras/Ajuda como opção principal. No projeto atual, o menu principal tem:

- iniciar partida;
- ver classificação;
- sair.

Impacto:

- falta a opção obrigatória Regras/Ajuda no menu principal.

### 3.2 Resumo final incompleto

No fim da partida, o programa mostra `Pontuação: X / N`, mas não mostra explicitamente:

- número de certas;
- número de erradas;
- percentagem de acerto.

Impacto:

- o resumo final não cumpre totalmente os requisitos do MVP.

### 3.3 Validação estrutural de perguntas incompleta

`ler_json` trata ficheiro inexistente, mas não valida estrutura mínima de cada pergunta (campos obrigatórios e formato).

Impacto:

- se o JSON tiver estrutura inválida, o erro pode aparecer apenas durante o jogo.

### 3.4 Gestão de ficheiros pode ser mais robusta

`logica_jogo.py` abre ficheiros com `open()` sem `with` em alguns pontos.

Impacto:

- funciona, mas é menos robusto para manutenção e tratamento de exceções.

## 4. Conformidade com regra de uso de IA (proibido)

### 4.1 Evidências documentais observadas

Foram observados no repositório vários sinais consistentes de uso intensivo de conteúdo de modelo/template externo:

- `README.md` com estrutura de template genérico;
- comandos de instalação com placeholders (`ton-profil/quiz-master-python` e `teu-perfil/quiz-master-python`) em vez do repositório real;
- `PLANIFICACAO.md` com responsabilidades atribuídas a `Estudante A`, `Estudante B`, `Estudante C`, apesar de o grupo ter 2 alunos;
- referência explícita a guia externo para "como criar ficheiro .md" no fim da planificação.

Exemplos observados no repositório:

```bash
git clone https://github.com/ton-profil/quiz-master-python.git
cd quiz-master-python
```

```bash
git clone https://github.com/teu-perfil/quiz-master-python.git
cd quiz-master-python
```

```md
| `carregar_json` | ... | Estudante A |
| `validar_input` | ... | Estudante B |
| `gerar_quiz` | ... | Estudante C |
```

```md
link para ajudar a criar este ficheiro .md:
https://datascientist.fr/blog/guide-ultime-creer-fichiers-readme-md-efficaces-markdown
```

### 4.2 Impacto na avaliação

Como a utilização de IA foi expressamente proibida, este ponto deve pesar negativamente na avaliação global, independentemente da qualidade técnica do código.

## 5. Testes de execução feitos nesta revisão

Testes realizados:

- compilação com `python -m py_compile`: passou;
- execução do menu e saída: passou;
- execução de partida completa com 5 perguntas: passou;
- gravação e leitura de classificação: passou.

## 6. Qualidade do código

### Pontos fortes

- boa modularização;
- validação de input consistente para números e texto;
- lógica simples e legível;
- ranking funcional com ordenação.

### Pontos a melhorar

- cumprir todos os itens obrigatórios do MVP (regras no menu principal e resumo final completo);
- reforçar validação de dados lidos do JSON;
- uniformizar práticas de leitura/escrita de ficheiros.

## 7. Avaliação final resumida

### Síntese

Tecnicamente, o projeto está bem construído para o nível do 10.º ano e funciona nos testes realizados. Existem, no entanto, falhas concretas de cumprimento do MVP obrigatório.

Além disso, há indícios documentais fortes de uso intensivo de conteúdo gerado/assistido externamente. Como esse uso era proibido, este fator deve reduzir a avaliação final.

### Classificação qualitativa sugerida

**Projeto tecnicamente bom, com falhas pontuais de MVP e com incumprimento relevante da regra de uso de IA.**

### Feedback curto

O projeto está funcional e organizado, mas faltam alguns elementos obrigatórios do enunciado no menu e no resumo final. Também é essencial respeitar integralmente as regras do trabalho, incluindo a proibição de uso de IA quando essa regra é definida pelo professor.
