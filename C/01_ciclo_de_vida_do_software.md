![Header](../Images/Header.png)

# C - 01 · Ciclo de Vida do Software

> **Objetivo deste ficheiro**  
> Compreender como um software nasce, evolui e se mantém, usando um processo técnico claro e aplicável a projetos em C.

---

## Índice

- [0. Como estudar este módulo](#0-como-estudar-este-módulo)
- [1. Resultados de aprendizagem](#1-resultados-de-aprendizagem)
- [2. O que é o ciclo de vida do software?](#2-o-que-é-o-ciclo-de-vida-do-software)
- [3. Porque o ciclo de vida é importante](#3-porque-o-ciclo-de-vida-é-importante)
- [4. Visão geral das fases](#4-visão-geral-das-fases)
- [5. Fase 1 - Requisitos](#5-fase-1---requisitos)
- [6. Fase 2 - Análise e planeamento](#6-fase-2---análise-e-planeamento)
- [7. Fase 3 - Desenho da solução](#7-fase-3---desenho-da-solução)
- [8. Fase 4 - Implementação (codificação)](#8-fase-4---implementação-codificação)
- [9. Fase 5 - Testes](#9-fase-5---testes)
- [10. Fase 6 - Entrega e operação](#10-fase-6---entrega-e-operação)
- [11. Fase 7 - Manutenção e evolução](#11-fase-7---manutenção-e-evolução)
- [12. Artefactos e documentação mínima por fase](#12-artefactos-e-documentação-mínima-por-fase)
- [13. Exemplo guiado completo: mini biblioteca](#13-exemplo-guiado-completo-mini-biblioteca)
- [14. Erros comuns de iniciantes](#14-erros-comuns-de-iniciantes)
- [15. Mini-laboratório de planeamento](#15-mini-laboratório-de-planeamento)
- [16. Rubrica de autoavaliação](#16-rubrica-de-autoavaliação)
- [17. Checklist final do módulo](#17-checklist-final-do-módulo)
- [18. Changelog](#18-changelog)

---

## 0. Como estudar este módulo

1. Lê as fases por ordem e tenta responder: "qual é a saída desta fase?".
2. Relaciona cada fase com trabalhos reais que já fizeste.
3. No exemplo guiado, identifica decisões boas e decisões arriscadas.
4. Faz primeiro o mini-laboratório e só depois a autoavaliação.

---

## 1. Resultados de aprendizagem

No fim deste módulo deves conseguir:

- explicar, com linguagem técnica correta, as 7 fases do ciclo de vida;
- distinguir requisitos funcionais, não funcionais e restrições;
- criar um planeamento simples (tarefas, prioridades e prazos);
- propor desenho inicial de solução (módulos, dados, interação);
- definir uma estratégia de testes com casos normais e limite;
- preparar entrega com documentação mínima;
- classificar pedidos de manutenção como corretiva, adaptativa, evolutiva ou preventiva.

---

## 2. O que é o ciclo de vida do software?

É o processo completo que vai da necessidade inicial até à manutenção do sistema em utilização.

Resumo simples:

- nasce de um problema real;
- passa por análise e construção;
- é validado por testes;
- é entregue a utilizadores;
- continua a ser melhorado.

Ideia-chave:

- software não termina quando "compila";
- termina quando resolve o problema com qualidade e continuidade.

---

## 3. Porque o ciclo de vida é importante

Sem processo, surgem problemas previsíveis:

- começar a programar sem objetivo claro;
- perder tempo com retrabalho;
- entregar algo que funciona "às vezes";
- não conseguir justificar decisões técnicas.

Com processo, mesmo em projetos pequenos:

- ganhas controlo sobre o trabalho;
- comunicas melhor com a equipa e com quem acompanha o projeto;
- detetas erros mais cedo;
- constróis hábitos profissionais desde cedo.

---

## 4. Visão geral das fases

Fluxo base de referência:

1. Requisitos
2. Análise e planeamento
3. Desenho da solução
4. Implementação
5. Testes
6. Entrega e operação
7. Manutenção e evolução

Importante:

- o fluxo parece linear, mas na prática há retornos;
- se um teste falha, voltas a implementação ou desenho;
- se surge pedido novo, voltas a requisitos.

---

## 5. Fase 1 - Requisitos

Pergunta central: **o que o sistema deve fazer e em que condições?**

### 5.1 Tipos de requisitos

- funcionais: funcionalidades observáveis;
- não funcionais: qualidade, desempenho, segurança, usabilidade;
- restrições: tecnologia, tempo, orçamento, regras do contexto.

### 5.2 Exemplos práticos (biblioteca)

Funcionais:

- registar livro;
- listar livros disponíveis;
- marcar empréstimo.

Não funcionais:

- operação básica em menos de 2 segundos;
- mensagens de erro claras para utilizador;
- dados guardados sem perda ao terminar.

Restrições:

- linguagem C;
- prazo de 3 semanas;
- execução em computadores disponíveis.

### 5.3 Critérios de qualidade de requisitos

Bons requisitos devem ser:

- claros;
- testáveis;
- sem ambiguidades;
- relevantes para objetivo.

Mau exemplo:

- "o programa deve ser bom".

Bom exemplo:

- "o programa deve permitir inserir até 500 registos".

---

## 6. Fase 2 - Análise e planeamento

Pergunta central: **como transformar requisitos em trabalho executável?**

### 6.1 Decisões típicas

- dividir projeto em módulos;
- identificar riscos técnicos e de tempo;
- priorizar tarefas essenciais;
- definir sequência de implementação.

### 6.2 Planeamento mínimo recomendado

- lista de tarefas;
- prioridade (alta, média, baixa);
- estimativa (horas/blocos de aula);
- responsável por tarefa;
- estado (`por fazer`, `em progresso`, `concluído`).

### 6.3 Gestão de risco simples

Exemplo de riscos:

- pouco domínio de ficheiros em C;
- faltas de elementos da equipa;
- subestimação do tempo de testes.

Mitigação:

- protótipo cedo;
- checkpoints semanais;
- reservar 20% do tempo para correções.

---

## 7. Fase 3 - Desenho da solução

Pergunta central: **como a solução será estruturada antes de codificar?**

### 7.1 Elementos de desenho para este nível

- modelo de dados (ex.: `struct Livro`);
- estrutura de ficheiros (`main.c`, `dados.c`, `menu.c`);
- pseudocódigo do fluxo principal;
- desenho de menus e interações.

### 7.2 Benefícios

- evita começar "às cegas";
- reduz decisões improvisadas durante codificação;
- facilita comunicação na equipa.

### 7.3 Saída esperada

No mínimo, deves produzir:

- desenho de módulos;
- lista de funções principais;
- representação E-P-S (Entrada, Processo, Saída) do programa.

---

## 8. Fase 4 - Implementação (codificação)

Pergunta central: **como transformar desenho em código funcional com controlo?**

### 8.1 Princípios de implementação

- começar por núcleo mínimo funcional;
- evoluir em incrementos pequenos;
- compilar frequentemente;
- corrigir warnings cedo;
- isolar funcionalidades por módulo.

### 8.2 Estratégia prática

Ordem sugerida:

1. estrutura base e menu;
2. inserção e listagem;
3. pesquisa e atualização;
4. persistência em ficheiro;
5. validações e melhorias.

### 8.3 Indicadores de progresso real

Sinal bom:

- funcionalidade completa + testada.

Sinal enganador:

- "escrevi muito código" sem validação.

---

## 9. Fase 5 - Testes

Pergunta central: **o software funciona corretamente em condições normais e difíceis?**

### 9.1 Tipos essenciais de teste

- caso normal;
- caso limite;
- caso inválido;
- regressão (algo que já funcionava continua a funcionar?).

### 9.2 Formato simples de caso de teste

- identificador: `T01`;
- entrada;
- resultado esperado;
- resultado obtido;
- estado: passou/falhou.

### 9.3 Erro frequente

Testar só "o melhor cenário" e ignorar entradas erradas.

---

## 10. Fase 6 - Entrega e operação

Pergunta central: **como disponibilizar o software de forma utilizável?**

Entrega mínima técnica:

- executável ou instruções de compilação;
- `README` com passos para correr;
- limitações conhecidas;
- versão identificada.

Operação inclui:

- uso real por utilizadores;
- recolha de feedback;
- registo de problemas.

---

## 11. Fase 7 - Manutenção e evolução

Pergunta central: **como manter valor após entrega?**

Tipos de manutenção:

- corretiva: corrigir bug;
- adaptativa: adaptar a novo ambiente;
- evolutiva: adicionar funcionalidade;
- preventiva: melhorar estrutura para evitar falhas futuras.

Exemplo rápido:

- crash ao procurar livro inexistente -> corretiva;
- mudança para novo formato de ficheiro -> adaptativa;
- filtro por autor -> evolutiva;
- refatorar função gigante em funções pequenas -> preventiva.

---

## 12. Artefactos e documentação mínima por fase

| Fase | Artefacto mínimo | Objetivo |
|---|---|---|
| Requisitos | lista de requisitos | definir "o quê" |
| Análise/planeamento | backlog + cronograma curto | definir "quando" e "quem" |
| Desenho | pseudocódigo + estrutura de módulos | definir "como" |
| Implementação | código compilável por incrementos | construir solução |
| Testes | tabela de casos de teste | validar comportamento |
| Entrega | README + versão | permitir uso sem ambiguidade |
| Manutenção | registo de issues/melhorias | evoluir com histórico |

Regra prática:

- sem artefacto mínimo, a fase está incompleta.

---

## 13. Exemplo guiado completo: mini biblioteca

### 13.1 Contexto

Objetivo: criar aplicação em C para gerir livros emprestados.

### 13.2 Aplicação fase a fase

Fase 1 (Requisitos):

- inserir livro;
- listar disponíveis;
- marcar empréstimo/devolução;
- guardar dados em ficheiro texto.

Fase 2 (Planeamento):

- semana 1: estrutura de dados + menu;
- semana 2: operações principais;
- semana 3: persistência, testes e documentação.

Fase 3 (Desenho):

- `struct Livro { titulo, autor, disponivel }`;
- módulos `menu`, `dados`, `ficheiro`;
- fluxo de menu em ciclo até sair.

Fase 4 (Implementação):

- primeiro versão mínima (inserir/listar);
- depois empréstimo/devolução;
- no fim leitura/escrita em ficheiro.

Fase 5 (Testes):

- lista vazia;
- livro duplicado;
- índice inválido;
- caracteres especiais no título.

Fase 6 (Entrega):

- README com compilação e execução;
- exemplos de utilização.

Fase 7 (Manutenção):

- nova funcionalidade: pesquisa por autor;
- correção: validação de índice no menu.

### 13.3 Aprendizagens do exemplo

- fases reduzem improviso;
- testes evitam regressões;
- documentação acelera suporte.

---

## 14. Erros comuns de iniciantes

1. começar a codificar antes de escrever requisitos;
2. confundir atividade com progresso (muito código sem validação);
3. deixar testes para o último dia;
4. não versionar alterações;
5. ignorar feedback de utilizadores e revisores;
6. entregar sem instruções;
7. não manter registo de bugs e melhorias.

Como evitar:

- ciclos curtos de planeamento e validação;
- checklist por fase;
- revisão semanal de estado real.

---

## 15. Mini-laboratório de planeamento

Objetivo: praticar o ciclo de vida num problema pequeno em 45 a 60 min.

Problema sugerido:

- "Sistema de registo de presenças".

Passos:

1. escrever 6 requisitos funcionais e 3 não funcionais;
2. criar backlog com 10 tarefas priorizadas;
3. desenhar módulos e funções principais;
4. definir 8 casos de teste;
5. preparar mini plano de entrega;
6. listar 4 melhorias de manutenção.

Entrega do laboratório:

- 1 documento curto (1 a 2 páginas) com todas as saídas.

---

## 16. Rubrica de autoavaliação

Pontua cada item de 1 (fraco) a 5 (forte):

- sei explicar cada fase com exemplo próprio;
- sei produzir artefactos mínimos por fase;
- consigo transformar requisitos em plano executável;
- consigo definir testes antes de terminar código;
- consigo preparar entrega técnica clara;
- consigo distinguir os 4 tipos de manutenção;
- consigo justificar decisões com critério técnico.

Interpretação:

- 7 a 16: base frágil (repetir laboratório);
- 17 a 27: base funcional (ganhar consistência);
- 28 a 35: base sólida (pronto para avançar).

---

## 17. Checklist final do módulo

Antes de fechar este módulo:

- escreveste requisitos claros e testáveis;
- montaste backlog com prioridade;
- definiste desenho inicial por módulos;
- registaste casos de teste;
- preparaste entrega com README;
- listaste manutenção futura com classificação correta.

Se falhar algum item, volta à fase correspondente e corrige.

---

## 18. Changelog

- **2026-04-12**: expansão completa do módulo com foco em profundidade, artefactos por fase, laboratório e avaliação.
- **2026-02-23**: reescrita completa do módulo com versão detalhada e foco pedagógico.

![Footer](../Images/Footer.png)
