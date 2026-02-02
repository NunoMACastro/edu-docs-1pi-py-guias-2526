# Projeto Final (10.º PI) — Jogo de Perguntas (Quiz) em Python

**Duração:** 2–3 semanas  
**Grupos:** 3 alunos  
**Tipo:** Aplicação de consola (terminal)

---

## 1) Contexto e objetivo

Vais desenvolver um **jogo de perguntas** (um quiz) em Python, executado no terminal.

O foco do projeto não é só “fazer funcionar”. É treinar aquilo que mais custa no início:

- passar de um **enunciado** para um **plano**
- desenhar uma **estrutura de dados** coerente
- dividir o problema em **funções** e **módulos**
- validar entradas e tornar o programa **robusto**

---

## 2) O que vais construir (visão geral)

Uma aplicação com:

- um **menu**
- um modo de **jogo** (responder a perguntas e somar pontos)
- um sistema simples de **pontuação**
- leitura de perguntas a partir de um ficheiro **`perguntas.json`**

> O programa deve ser “amigável” no terminal: mensagens claras, opções numeradas, validação de inputs e resultados bem apresentados.

---

## 3) Regras e restrições

### Obrigatório

- Python 3.x
- Sem bibliotecas externas (só biblioteca standard: `json`, `random`, `time`, etc.)
- Usar **funções** (não pode ser um ficheiro gigante com tudo no `main`)
- Validar entradas do utilizador (não assumir que o utilizador escreve “bem”)
- Ler as perguntas a partir de um ficheiro JSON

### Permitido / recomendado

- Usar listas e dicionários como “base de dados em memória”
- Organizar o projeto em **módulos** (mais do que 1 ficheiro `.py`)
- Guardar pontuações num ficheiro (ex.: `pontuacoes.json`) para manter histórico

---

## 4) Ficheiro de perguntas (JSON)

Devem criar um ficheiro JSON com perguntas para o jogo. Depois de terem uma estrutura para o ficheiro, podem pedir a um agente de IA (ex.: ChatGPT) para gerar perguntas automaticamente.

### Estrutura do JSON (schema esperado)

O ficheiro terá uma **lista de perguntas**, e cada pergunta terá que guardar campos semelhantes a estes:

- `id` (int ou str)
- `pergunta` (str)
- `opcoes` (lista de strings)
- `resposta` (int **ou** str — dependendo do ficheiro fornecido)
- `categoria` (str) - Se for aplicável
- `dificuldade` (str: `"facil"`, `"media"`, `"dificil"`) — opcional
- `explicacao` (str) — opcional (para mostrar no fim)

**Nota importante:** O campo `resposta` pode ser:

- um **índice** (ex.: `1` significa a opção nº2, se estiveres a usar índice 0)
- ou o **texto** da opção correta

---

## 5) Funcionalidades

### 5.1 — MVP (obrigatório)

Estas funcionalidades têm de existir e estar a funcionar bem:

1. **Carregar perguntas**

- Ler `perguntas.json`
- Validar o básico: existe, não está vazio, cada pergunta tem `pergunta` e `opcoes`

2. **Menu principal**

- (1) Jogar
- (2) Regras / ajuda
- (3) Sair  
  (Podes adicionar mais opções, mas estas são obrigatórias.)

3. **Modo de jogo**

- Escolher **N perguntas aleatórias** (ex.: 5, 10 ou configurável)
- Para cada pergunta:
    - mostrar enunciado e opções numeradas
    - pedir resposta do utilizador
    - validar input (não pode crashar com letras, vazio, números fora do intervalo)
    - dizer se acertou/errou
    - atualizar pontuação

4. **Resumo final**

- Pontuação total
- Nº de certas / erradas
- Percentagem de acerto

5. **Re-jogar**

- No fim, permitir jogar outra vez sem reiniciar o programa

---

### 5.2 — Nível 2

Escolhe pelo menos **2** destas melhorias:

A) **Categorias e/ou dificuldade**

- Antes de jogar, permitir escolher categoria e/ou dificuldade
- Se o utilizador escolher “todas”, o jogo usa tudo

B) **Evitar repetição**

- Garantir que numa sessão as perguntas **não repetem**
- (Extra) evitar repetição em várias sessões enquanto houver perguntas novas

C) **Pontuações guardadas**

- Pedir um nome/nickname no início
- Guardar o resultado num ficheiro (ex.: `pontuacoes.json`)
- No menu, ter uma opção para ver o **Top 10**

D) **Explicação**

- Se existir `explicacao` na pergunta, mostrar no fim (ou após responder)

---

### 5.3 — Nível 3 (bónus)

Escolhe **1** se já tiveres o MVP + Nível 2 sólidos:

A) **Modo contra-relógio**

- O jogador tem X segundos por pergunta (ex.: 10–15)
- Se passar o tempo, conta como errada (ou sem pontos)

B) **Pontuação por dificuldade**

- Perguntas fáceis valem 1 ponto, médias 2, difíceis 3

C) **Modo “Campeonato”**

- Melhor de 3 rondas, soma total e vencedor (se tiverem 2 jogadores alternados)

---

## 6) Planificação inicial (obrigatória antes de programar)

Antes de escreverem código “a sério”, o grupo tem de entregar um ficheiro chamado:

- **`PLANIFICACAO.md`**

Este ficheiro vale para a nota e serve para desbloquear o projeto.

### O que o `PLANIFICACAO.md` tem de ter

#### 1) Modelo de dados (muito importante)

- Como vão representar:
    - as perguntas em memória (lista? Dicionários? Uma combinação de ambos?)
    - a pontuação (inteiro? dicionário com certas/erradas?)
    - as pontuações guardadas (lista de dicionários em `pontuacoes.json`?)
- Incluir **2 exemplos reais** (pequenos) das estruturas.

#### 2) Entradas / Processamento / Saídas

Uma tabela ou lista com:

- entradas (o que o utilizador escreve / o que vem do JSON)
- processamento (o que o programa calcula/decide)
- saídas (o que mostra no terminal / o que guarda em ficheiro)

#### 3) Lista de funções (com responsabilidades)

Exemplos do género:

- `carregar_perguntas(...)` — lê JSON e devolve lista
- `mostrar_menu(...)` — imprime opções e devolve escolha válida
- `fazer_pergunta(...)` — mostra pergunta, pede resposta, devolve se acertou

(Os nomes e a divisão são decididos por vocês — mas têm de justificar.)

Exemplo de tabela com as funções:

| Função               | Descrição                                 | Responsabilidade |
| -------------------- | ----------------------------------------- | ---------------- |
| `carregar_perguntas` | Leitura do ficheiro JSON com as perguntas | João             |
| `mostrar_menu`       | Mostra o menu e lê escolha do utilizador  | Maria            |

#### 4) Fluxo do programa

Um fluxograma simples (pode ser em texto ou diagrama) ou passos numerados que expliquem:

- o que acontece desde o início até ao fim
- como o menu liga ao jogo, como o jogo termina, etc.
- como são tratadas entradas inválidas
- como se escolhe jogar outra vez ou sair

##### Exemplo prático de fluxo

1. Ao arrancar, limpar o ecrã e mostrar o menu principal.
2. Ler a escolha do utilizador; se for inválida, repetir até obter um número válido.
3. Se a escolha for “jogar”, carregar perguntas, iniciar o ciclo de perguntas (mostrar enunciado, validar resposta, atualizar pontuação) e, no final, apresentar o resumo e perguntar se quer jogar outra vez.
4. Se a escolha for ......
5. Se for sair ......

#### 5) Estrutura de ficheiros / módulos (decidida por vocês)

Não existe uma estrutura “certa”. Mas é obrigatório:

- usar **mais do que 1 ficheiro `.py`**
- justificar a divisão: o que fica em cada ficheiro e porquê

#### 6) Plano de testes (manual)

Criar uma lista de testes do tipo:

- “Se escrever ‘a’ em vez de número, o programa não crasha e volta a pedir”
- “Se escolher uma opção fora do intervalo, dá erro e repete”
- ...

Escrever pelo menos 7 testes diferentes que cubram as funcionalidades principais e as validações.

##### Teste de exemplo

- Entrada inválida: o utilizador digita “a” em vez de um número no menu. O programa deteta o erro, mostra uma mensagem de aviso e volta a pedir uma escolha sem fechar.

#### 7) Mini-revisões antes de começar a programar

- Revisão 1: o modelo de dados está descrito com dois exemplos e todos os membros compreendem como as perguntas/pontuações são guardadas?
- Revisão 2: a lista de funções está completa, com responsabilidades atribuídas e dependências assinaladas?
- Revisão 3: o fluxo e o plano de testes foram revistos antes de começar a implementar?

---

## 7) Organização do trabalho

### Fase 1

- Entregar `PLANIFICACAO.md`
- Fazer protótipo do menu + carregar JSON

### Fase 2

- Implementar o modo de jogo completo (MVP)
- Validar inputs e melhorar mensagens
- Começar Nível 2 (categorias/pontuações/etc.)

### Fase 3

- Terminar Nível 2
- Fazer testes, corrigir bugs
- Melhorar apresentação no terminal
- (Opcional) 1 funcionalidade Nível 3

---

## 8) Critérios de avaliação

- **10%** Planificação (`PLANIFICACAO.md`) bem feita e coerente
- **35%** MVP completo e funcional
- **25%** Qualidade do código: funções, organização por módulos, legibilidade
- **10%** Robustez: validações, erros tratados sem crashes
- **10%** Nível 2 e polimento
- **10%** Nível 3 ou extras interessantes

---

## 9) Entrega final

Entregar o link do repositório GitHub com:

- ficheiros `.py` do projeto
- `perguntas.json` (o fornecido, sem alterações “à sorte”)
- (se aplicável) `pontuacoes.json`
- `PLANIFICACAO.md`
- `README.md` pequeno com:
    - como executar
    - funcionalidades implementadas
    - extras feitos

---

## 10) Notas finais (dicas práticas)

- Comecem pelo **fluxo** (menu → jogar → resumo). Só depois polir.
- Se estiverem bloqueados, voltem ao modelo de dados: “como vou guardar isto?”
- Façam o programa funcionar com 3 perguntas, depois escalam para o ficheiro todo.
- Guardem sempre uma versão que “funciona” antes de adicionar extras.

---

### Checkpoint rápido (para o professor validar)

No fim da Fase 1, o grupo deve conseguir:

- abrir o JSON e mostrar quantas perguntas carregou
- ter um menu que aceita escolhas válidas
- conseguir mostrar uma pergunta e ler uma resposta

---

### Entrega do projeto final

Todos os ficheiros e o md de planificação devem ser entregues via Guithub até à data definida pelo professor.
