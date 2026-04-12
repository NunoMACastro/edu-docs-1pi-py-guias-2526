# C - 04 · Metodologias de Desenvolvimento de Software

> **Objetivo deste ficheiro**  
> Escolher e aplicar metodologias de trabalho de forma prática, realista e eficiente em projetos de C.

---

## Índice

- [0. Como estudar este módulo](#0-como-estudar-este-módulo)
- [1. Resultados de aprendizagem](#1-resultados-de-aprendizagem)
- [2. Porque precisamos de metodologia?](#2-porque-precisamos-de-metodologia)
- [3. Panorama das abordagens](#3-panorama-das-abordagens)
- [4. Modelo em cascata](#4-modelo-em-cascata)
- [5. Modelo iterativo/incremental](#5-modelo-iterativoincremental)
- [6. Metodologias ágeis (visão introdutória)](#6-metodologias-ágeis-visão-introdutória)
- [7. Scrum](#7-scrum)
- [8. Kanban na prática](#8-kanban-na-prática)
- [9. Como escolher metodologia para o projeto](#9-como-escolher-metodologia-para-o-projeto)
- [10. Artefactos mínimos de gestão de projeto](#10-artefactos-mínimos-de-gestão-de-projeto)
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
2. Tenta mapear essas diferenças num projeto que já tenhas feito.
3. Executa o exemplo guiado como se fosse um projeto real.
4. Usa a rubrica para avaliar se a metodologia foi realmente aplicada.

---

## 1. Resultados de aprendizagem

No final deste módulo deves conseguir:

- explicar vantagens e limitações das principais abordagens;
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

## 3. Panorama das abordagens

### 3.1 Cascata

- sequência de fases mais rígida;
- boa quando requisitos estão estáveis.

### 3.2 Iterativo/incremental

- ciclos curtos com entregas parciais;
- bom para aprendizagem progressiva.

### 3.3 Ágil

- adaptação contínua;
- feedback frequente;
- foco em valor entregue.

Não existe metodologia perfeita para todos os contextos.

Existe metodologia mais adequada para cada projeto.

---

## 4. Modelo em cascata

Fluxo típico:

1. requisitos;
2. análise;
3. implementação;
4. testes;
5. entrega.

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

---

## 5. Modelo iterativo/incremental

Ideia principal:

- construir em partes funcionais (incrementos);
- melhorar por ciclos.

Em cada iteração:

- planear;
- implementar subset;
- testar;
- rever e ajustar.

Vantagens:

- erro aparece cedo;
- entrega valor parcial rapidamente;
- facilita gestão de risco.

Quando usar:

- projetos de 2 a 6 semanas com evolução gradual.

---

## 6. Metodologias ágeis (visão introdutória)

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

## 7. Scrum

Elementos simplificados:

- backlog: lista priorizada de trabalho;
- sprint: ciclo curto (1 semana recomendado);
- daily curta: 3 perguntas em 5 min;
- review: demonstrar o que funciona;
- retro: decidir melhorias de processo.

Perguntas da daily:

- o que fiz desde a última reunião?
- o que vou fazer até à próxima?
- que bloqueio tenho?

Risco comum:

- falar muito e produzir pouco.

Solução:

- foco em bloqueios e decisões concretas.

---

## 8. Kanban na prática

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

---

## 9. Como escolher metodologia para o projeto

Matriz prática de decisão:

| Contexto                    | Abordagem recomendada        |
| --------------------------- | ---------------------------- |
| requisitos muito estáveis   | cascata simplificada         |
| prazo curto com risco médio | iterativo + Kanban           |
| mudanças frequentes         | ágil com sprints curtos      |
| equipa inexperiente         | iterativo com regras simples |

Estratégia híbrida (frequente e saudável):

- planeamento inicial estilo cascata;
- execução iterativa;
- acompanhamento com Kanban.

---

## 10. Artefactos mínimos de gestão de projeto

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

Para 5 cenários diferentes, escolhe abordagem e justifica.

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

- **2026-04-12**: expansão completa do módulo com matriz de decisão, artefactos, métricas, laboratório e avaliação.
- **2026-02-23**: reescrita detalhada do módulo com foco pedagógico e exercícios sem resolução.
