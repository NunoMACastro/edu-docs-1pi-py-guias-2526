# C - 04 · Metodologias de Desenvolvimento de Software

> **Objetivo deste ficheiro**  
> Escolher e aplicar metodologias de trabalho de forma prática, realista e eficiente em projetos de C.

---

## Índice

- [0. Como estudar este módulo](#0-como-estudar-este-módulo)
- [1. Resultados de aprendizagem](#1-resultados-de-aprendizagem)
- [2. Porque precisamos de metodologia?](#2-porque-precisamos-de-metodologia)
- [3. Níveis de decisão em desenvolvimento (explicação detalhada)](#3-níveis-de-decisão-em-desenvolvimento-explicação-detalhada)
- [4. Nível 1 · Modelos de ciclo de vida (Cascata e Iterativo)](#4-nível-1--modelos-de-ciclo-de-vida-cascata-e-iterativo)
- [5. Modelo em cascata (Nível 1)](#5-modelo-em-cascata-nível-1)
- [6. Modelo iterativo/incremental (Nível 1)](#6-modelo-iterativoincremental-nível-1)
- [7. Nível 2 · Abordagem Ágil (princípios)](#7-nível-2--abordagem-ágil-princípios)
- [8. Nível 3 · Scrum e Kanban (framework e método)](#8-nível-3--scrum-e-kanban-framework-e-método)
- [9. Como escolher e combinar níveis no projeto](#9-como-escolher-e-combinar-níveis-no-projeto)
- [10. Nível 4 · Ferramentas e artefactos mínimos](#10-nível-4--ferramentas-e-artefactos-mínimos)
- [11. Métricas simples para acompanhar progresso](#11-métricas-simples-para-acompanhar-progresso)
- [12. Exemplo guiado completo: agenda de contactos em C](#12-exemplo-guiado-completo-agenda-de-contactos-em-c)
- [13. Erros comuns de metodologia](#13-erros-comuns-de-metodologia)
- [14. Mini-laboratório de gestão ágil](#14-mini-laboratório-de-gestão-ágil)
- [15. Exercícios (sem resolução)](#15-exercícios-sem-resolução)
- [16. Rubrica de autoavaliação](#16-rubrica-de-autoavaliação)
- [17. Checklist de execução metodológica](#17-checklist-de-execução-metodológica)
- [18. Changelog](#18-changelog)

---

## 0. Como estudar este módulo

1. Lê primeiro diferenças entre cascata, iterativo e ágil.
2. Distingue explicitamente os 4 níveis (modelo, abordagem, framework/método, ferramentas).
3. Tenta mapear essas diferenças num projeto que já tenhas feito.
4. Executa o exemplo guiado como se fosse um projeto real.
5. Usa a rubrica para avaliar se a metodologia foi realmente aplicada.

---

## 1. Resultados de aprendizagem

No final deste módulo deves conseguir:

- explicar vantagens e limitações das principais abordagens;
- distinguir modelo de ciclo de vida, abordagem, framework/método e ferramenta;
- escolher metodologia adequada ao contexto do projeto;
- criar backlog, prioridades e plano iterativo;
- usar quadro Kanban com critérios claros de transição;
- conduzir reuniões curtas de acompanhamento;
- monitorizar progresso com métricas simples;
- ajustar plano com base em risco e feedback.

---

## 2. Porque precisamos de metodologia?

Sem metodologia, surgem padrões de falha:

- tarefas esquecidas;
- retrabalho frequente;
- conflitos de equipa por falta de alinhamento;
- atrasos no fim do projeto;
- entrega sem qualidade técnica.

Metodologia não é burocracia.

Metodologia é:

- estrutura para decidir prioridades;
- mecanismo de coordenação da equipa;
- proteção contra improviso descontrolado.

---

## 3. Níveis de decisão em desenvolvimento

Antes de escolher "uma metodologia", tens de perceber que existem níveis diferentes de decisão.

Se misturares níveis, o projeto fica confuso: discute-se Scrum vs Cascata como se fossem alternativas diretas, quando não são do mesmo tipo.

### 3.1 Nível 1 · Modelo de ciclo de vida (macroestrutura)

O modelo de ciclo de vida define a estrutura macro do trabalho ao longo do tempo.

Responde a perguntas como:

- "vamos fazer por fases sequenciais ou por iterações?"
- "quando validamos com utilizadores?"
- "como distribuímos risco ao longo do projeto?"

Exemplos neste módulo: Cascata e Iterativo/Incremental.

### 3.2 Nível 2 · Abordagem (princípios de decisão)

A abordagem define como a equipa pensa e decide no dia a dia.

Responde a perguntas como:

- "mudança é exceção ou parte normal do processo?"
- "priorizamos plano fechado ou adaptação contínua?"
- "qual o peso do feedback frequente?"

Exemplo neste módulo: Ágil (como conjunto de princípios, não como um único processo fechado).

### 3.3 Nível 3 · Framework/método operacional (ritmo e gestão do fluxo)

Este nível traduz princípios em rotinas operacionais concretas.

Responde a perguntas como:

- "que eventos fazemos por semana?"
- "como gerimos prioridades e bloqueios?"
- "como limitamos trabalho em progresso?"

Exemplos neste módulo: Scrum (framework com papéis/eventos/artefactos) e Kanban (método de gestão de fluxo).

### 3.4 Nível 4 · Ferramentas e artefactos (instrumentos práticos)

Ferramentas e artefactos suportam os níveis anteriores, mas não os substituem.

Responde a perguntas como:

- "onde registamos trabalho e prioridades?"
- "como visualizamos o estado das tarefas?"
- "como definimos 'concluído'?"

Exemplos neste módulo: backlog, quadro Kanban, definição de concluído, métricas e registo de riscos.

### 3.5 Mapa rápido

| Elemento                | Classificação correta               |
| ----------------------- | ----------------------------------- |
| Cascata                 | Nível 1 · Modelo de ciclo de vida   |
| Iterativo/Incremental   | Nível 1 · Modelo de ciclo de vida   |
| Ágil                    | Nível 2 · Abordagem                 |
| Scrum                   | Nível 3 · Framework operacional     |
| Kanban                  | Nível 3 · Método de gestão de fluxo |
| Quadro Kanban / Backlog | Nível 4 · Ferramenta/artefacto      |

Não existe combinação perfeita para todos os contextos.

Existe combinação de níveis mais adequada para cada projeto.

---

## 4. Nível 1 · Modelos de ciclo de vida (Cascata e Iterativo)

Explicação detalhada do Nível 1:

- define a arquitetura temporal do projeto do início ao fim;
- influencia previsibilidade, gestão de risco e forma de validação;
- deve ser decidido cedo, porque afeta prazos, planeamento e pontos de controlo.

---

## 5. Modelo em cascata (Nível 1)

Fluxo típico:

1. requisitos;
2. análise;
3. implementação;
4. testes;
5. entrega.

Como funciona na prática (passo a passo):

1. no início, a equipa tenta fechar requisitos com o máximo de detalhe;
2. depois transforma esses requisitos em análise técnica e desenho de solução;
3. a implementação acontece com foco em concluir o escopo planeado;
4. a validação mais pesada acontece perto do fim (testes integrados);
5. só depois vem a entrega formal.

Isto cria "portas" entre fases: normalmente só avanças quando a fase anterior é dada como concluída.

Gestão de mudança no cascata:

- mudança tardia custa mais, porque pode obrigar a rever documentação, código e testes já fechados;
- por isso, pedidos novos costumam passar por controlo formal de alteração (impacto em prazo/custo/escopo).

Vantagens:

- previsível;
- simples de explicar;
- documentação clara por fase.

Limitações:

- baixa flexibilidade a mudanças tardias;
- feedback do utilizador chega tarde;
- risco de descobrir problemas críticos no fim.

Quando usar:

- projeto pequeno, requisitos fixos e prazo curto.

Sinal de boa aplicação:

- requisitos estáveis desde cedo;
- poucas alterações a meio;
- documentação de fase realmente usada para decisão.

---

## 6. Modelo iterativo/incremental (Nível 1)

Ideia principal:

- construir em partes funcionais (incrementos);
- melhorar por ciclos.

Diferença-chave:

- `iteração` = ciclo de trabalho com planeamento -> execução -> teste -> revisão;
- `incremento` = parte funcional entregue no fim da iteração.

Em cada iteração:

- planear;
- implementar subset;
- testar;
- rever e ajustar.

Como funciona na prática (ritmo real):

1. escolhes um conjunto pequeno de funcionalidades prioritárias;
2. implementas apenas esse conjunto com qualidade mínima de entrega;
3. mostras resultado, recolhes feedback técnico/funcional;
4. ajustas prioridades do backlog para a próxima iteração.

Assim, em vez de "apostar tudo no fim", vais reduzindo risco em ciclos curtos.

Gestão de mudança no iterativo:

- mudança entra naturalmente entre iterações;
- cada novo pedido é priorizado com os restantes;
- o plano é atualizado sem perder visibilidade do que já foi concluído.

Vantagens:

- erro aparece cedo;
- entrega valor parcial rapidamente;
- facilita gestão de risco.

Quando usar:

- projetos de 2 a 6 semanas com evolução gradual.

Risco comum quando mal aplicado:

- abrir demasiadas tarefas por iteração e não fechar nada com qualidade.

---

## 7. Nível 2 · Abordagem Ágil (princípios)

Explicação detalhada do Nível 2:

- define princípios de decisão, não um roteiro único obrigatório;
- orienta como a equipa reage a mudança, incerteza e feedback;
- pode ser combinada com diferentes modelos de ciclo de vida no Nível 1.

Nesta perspetiva, "Ágil" não concorre diretamente com "Scrum" ou "Kanban".  
Ágil é a orientação de base; Scrum e Kanban são formas de operacionalizar essa orientação.

Princípios práticos:

- entregas frequentes;
- comunicação curta e constante;
- adaptação ao feedback do utilizador;
- foco no essencial antes do extra.

Aplicação prática:

- quadro de tarefas atualizado;
- revisões semanais;
- objetivos pequenos e alcançáveis.

---

## 8. Nível 3 · Scrum e Kanban (framework e método)

Explicação detalhada do Nível 3:

- define o mecanismo de execução semanal/diário;
- transforma princípios em cadência, regras de trabalho e pontos de inspeção;
- pode variar sem mudar o Nível 1 (por exemplo, manter iterativo e trocar Scrum por Kanban).

### 8.1 Scrum (framework)

Elementos simplificados:

- backlog: lista priorizada de trabalho;
- sprint: ciclo curto (de 1 dia a 1 semana recomendado);
- daily curta: reunião rápida para sincronizar e identificar bloqueios;
- review: demonstrar o que funciona;
- retro: decidir melhorias de processo.

Risco comum:

- falar muito e produzir pouco.
- muitas reuniões por sprint sem foco em decisão.

Solução:

- foco em bloqueios e decisões concretas.

### 8.2 Kanban (método de gestão de fluxo)

Colunas mínimas:

- por fazer;
- em progresso;
- em revisão/teste;
- concluído.

Regras de ouro:

- limite de tarefas em progresso (`WIP`) por elemento;
- mover cartão apenas quando critério estiver cumprido;
- não "mascarar" tarefa incompleta como concluída.

Critério de "concluído" recomendado:

- implementado;
- compilado sem erros;
- testado nos casos essenciais;
- documentado minimamente.

Exemplo de ferramentas que usam Kanban:

- Trello;
- Jira;
- GitHub Projects.

---

## 9. Como escolher e combinar níveis no projeto

Regra prática:

1. decidir Nível 1 (macroestrutura do ciclo de vida);
2. definir Nível 2 (princípios de decisão);
3. escolher Nível 3 (framework/método de execução);
4. configurar Nível 4 (ferramentas e artefactos de suporte).

Matriz prática de decisão:

| Contexto                    | Combinação recomendada                                            |
| --------------------------- | ----------------------------------------------------------------- |
| requisitos muito estáveis   | N1: cascata simplificada + N4: checklist forte                    |
| prazo curto com risco médio | N1: iterativo + N3: Kanban + N4: métricas semanais                |
| mudanças frequentes         | N1: iterativo + N2: ágil + N3: Scrum ou Kanban                    |
| equipa inexperiente         | N1: iterativo simples + N3: Kanban com poucas regras + N4: básico |

Estratégia híbrida:

- planeamento inicial estilo cascata;
- execução iterativa;
- acompanhamento com Kanban.

---

## 10. Nível 4 · Ferramentas e artefactos mínimos

Explicação detalhada do Nível 4:

- é o nível mais visível no dia a dia, mas também o mais confundido com "metodologia";
- ferramentas não definem processo sozinhas: um quadro sem regras não melhora execução;
- artefactos servem para dar evidência e controlo ao que foi decidido nos níveis 1, 2 e 3.

Para um projeto com gestão séria, cria no mínimo:

- backlog priorizado;
- plano de sprint/iteração;
- quadro Kanban atualizado;
- definição de "concluído";
- registo de riscos;
- resumo de revisão semanal.

Sem estes artefactos:

- dificilmente consegues provar controlo de projeto.

---

## 11. Métricas simples para acompanhar progresso

Métricas úteis para este nível:

- tarefas concluídas por semana;
- tarefas em atraso;
- número de bugs abertos/fechados;
- percentagem de funcionalidades essenciais concluídas;
- cumprimento dos objetivos da sprint.

O que não fazer:

- usar métricas para "culpar" colegas.

O que fazer:

- usar métricas para decidir prioridades e remover bloqueios.

---

## 12. Exemplo guiado completo: agenda de contactos em C

### 12.1 Objetivo

Aplicação para inserir, listar e pesquisar contactos.

### 12.2 Backlog inicial

1. criar contacto;
2. listar contactos;
3. pesquisar por nome;
4. editar contacto;
5. guardar em ficheiro;
6. carregar de ficheiro;
7. validação de input;
8. documentação de uso.

### 12.3 Planeamento em 3 iterações

Iteração 1:

- criar/listar;
- menu funcional;
- testes básicos.

Iteração 2:

- pesquisa/edição;
- validações;
- mais testes.

Iteração 3:

- persistência em ficheiro;
- correções finais;
- README e entrega.

### 12.4 Quadro Kanban inicial

- por fazer: 8 tarefas;
- em progresso: 2;
- revisão/teste: 0;
- concluído: 0.

### 12.5 Eventos semanais

- segunda: planeamento (20 min);
- quarta: checkpoint rápido (10 min);
- sexta: review + retro (20 min).

### 12.6 Resultados esperados

- melhoria contínua por iteração;
- menos surpresas no fim;
- entrega com controlo real de qualidade.

---

## 13. Erros comuns de metodologia

1. copiar termos ágeis sem aplicar práticas;
2. fazer backlog e nunca atualizar;
3. começar muitas tarefas ao mesmo tempo;
4. não reservar tempo para testes;
5. ignorar bloqueios até ao fim;
6. não fechar tarefas com critérios objetivos;
7. não fazer retro e repetir os mesmos erros.

Correção prática:

- reduzir WIP;
- reunião curta focada em decisão;
- revisão semanal obrigatória.

---

## 14. Mini-laboratório de gestão ágil

Objetivo: executar microprojeto em 60 a 90 min com método.

Problema sugerido:

- "sistema simples de notas em C".

Passos:

1. definir backlog com 12 tarefas;
2. priorizar em essencial/importante/opcional;
3. planear sprint de 1 semana (simulada);
4. criar quadro Kanban;
5. definir critérios de "concluído";
6. simular daily (3 perguntas);
7. fazer review do incremento entregue;
8. escrever retro com 3 melhorias.

Entrega:

- documento de gestão + evidência de incremento funcional.

---

## 15. Exercícios (sem resolução)

### Exercício 1 - Comparação técnica

Compara cascata, iterativo e ágil em 8 critérios.

### Exercício 2 - Escolha de metodologia

Para 5 cenários diferentes, escolhe combinação de níveis (N1, N2, N3, N4) e justifica.

### Exercício 3 - Backlog

Cria backlog de 20 itens para "gestão de biblioteca".

### Exercício 4 - Priorização

Classifica backlog em alta/média/baixa prioridade.

### Exercício 5 - Planeamento de iterações

Divide backlog em 3 iterações com objetivos claros.

### Exercício 6 - Kanban com WIP

Monta quadro Kanban e define limite de tarefas em progresso.

### Exercício 7 - Critérios de aceitação

Escreve critérios de aceitação para 6 tarefas.

### Exercício 8 - Riscos

Lista 10 riscos e medidas preventivas.

### Exercício 9 - Reuniões

Cria roteiro de reunião semanal de 10 min com foco em decisão.

### Exercício 10 - Métricas

Define dashboard simples para acompanhar evolução do projeto.

### Exercício 11 - Gestão de mudança

Pedido novo a meio da sprint: descreve como integrar sem desorganizar.

### Exercício 12 - Diagnóstico

Recebes projeto atrasado e sem método. Propõe plano de recuperação.

### Exercício 13 - Simulação Scrum

Executa sprint curta com equipa e regista eventos.

### Exercício 14 - Retro orientada

Escreve retro com "manter", "melhorar", "parar".

### Exercício 15 - Reflexão

Responde: "Porque metodologia também é competência técnica?".

---

## 16. Rubrica de autoavaliação

Pontua de 1 a 5:

- consigo escolher metodologia para contexto real;
- consigo manter backlog atualizado e útil;
- consigo planear iteração com objetivos mensuráveis;
- consigo usar Kanban com disciplina;
- consigo identificar e gerir riscos;
- consigo medir progresso com indicadores simples;
- consigo adaptar plano com base em feedback.

Interpretação:

- 7 a 16: base frágil;
- 17 a 27: base funcional;
- 28 a 35: base sólida.

---

## 17. Checklist de execução metodológica

Antes da entrega do projeto:

- metodologia escolhida está justificada;
- backlog foi priorizado e atualizado;
- tarefas concluídas seguem critério objetivo;
- há registo de riscos e bloqueios;
- foram feitas revisões periódicas;
- testes foram integrados no plano;
- documentação de processo está presente.

Se faltarem 2 ou mais itens, o processo ainda está incompleto.

---

## 18. Changelog

- **2026-04-14**: reestruturação por níveis (modelo, abordagem, framework/método, ferramentas) para evitar mistura de conceitos.
- **2026-04-12**: expansão completa do módulo com matriz de decisão, artefactos, métricas, laboratório e avaliação.
- **2026-02-23**: reescrita detalhada do módulo com foco pedagógico e exercícios sem resolução.
