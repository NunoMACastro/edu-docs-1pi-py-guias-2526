# Avaliação do Projeto

## Grupo

Domingos e Enzo

## Projeto

Quiz Python

## Enquadramento da avaliação

Esta avaliação teve em conta que se trata de um trabalho de alunos do 10.º ano e do primeiro projeto deste tipo. O objetivo não é avaliar como se fosse um projeto profissional, mas sim perceber o que já foi conseguido, o que está bem encaminhado e o que ainda precisa de ser melhorado.

Neste caso, foi também considerado um ponto adicional importante: a possível utilização intensiva de IA, algo que, segundo a indicação do professor, estava expressamente proibido. Esse aspeto pesa negativamente na avaliação global, independentemente de o resultado final parecer mais polido.

## 1. Visão geral

O projeto apresenta-se como um quiz em terminal, com:

- menu principal;
- seleção de categoria;
- seleção de dificuldade;
- perguntas aleatórias;
- pontuação;
- ranking Top 10;
- separação em vários ficheiros (`main.py`, `logica_jogo.py`, `utils.py`);
- ficheiro JSON com perguntas.

Do ponto de vista funcional, o projeto está relativamente bem estruturado e aproxima-se bastante do que era pedido no enunciado. Há uma arquitetura simples, mas coerente, e existe preocupação com validação de entradas, filtragem de perguntas e gravação de resultados.

## 2. Nível de implementação

### O que está implementado

- menu principal com jogar, ranking e sair;
- pedido de nome do utilizador;
- escolha de categoria;
- escolha de dificuldade;
- leitura de perguntas a partir de `perguntas.json`;
- filtragem por categoria e dificuldade;
- escolha aleatória de perguntas;
- validação de respostas;
- feedback com explicação;
- gravação de pontuações em `pontuacoes.json`;
- visualização de Top 10.

### Estado global

O projeto está num nível de implementação bom para o contexto escolar. A maior parte do MVP pedido no enunciado está presente e existe também algum nível de polimento.

### Limitação importante

Mesmo assim, há detalhes que mostram que o projeto não está totalmente alinhado com o enunciado:

- o jogo usa 5 perguntas por sessão e não parece oferecer re-jogar logo no fim da partida;
- o resumo final mostra a pontuação, mas não apresenta claramente o número de certas, erradas e percentagem de acerto.

Ou seja, o projeto está bem encaminhado, mas não fecha tudo o que era pedido da melhor forma.

## 3. Pontos positivos

### 3.1 Estrutura organizada

A divisão entre `main.py`, `logica_jogo.py` e `utils.py` é clara e adequada. Para um primeiro projeto, esta separação mostra noção de organização e responsabilidade por ficheiros.

### 3.2 Validação de entradas

As funções `validar_numero()` e `validar_texto()` mostram preocupação com robustez. O programa tenta impedir entradas vazias ou inválidas, o que é um ponto positivo.

### 3.3 Modelo de dados coerente

O ficheiro `perguntas.json` usa uma estrutura consistente:

- `id`
- `pergunta`
- `opcoes`
- `resposta`
- `categoria`
- `dificuldade`
- `explicacao`

Isto está bem alinhado com o que o enunciado pedia e facilita o funcionamento do jogo.

### 3.4 Conteúdo relativamente rico

O ficheiro de perguntas contém um conjunto grande e variado de perguntas, distribuídas por categorias e dificuldades. Isso valoriza o projeto e mostra atenção ao conteúdo.

## 4. Problemas encontrados

### 4.1 Resumo final incompleto

O enunciado pedia claramente:

- pontuação total;
- número de certas e erradas;
- percentagem de acerto.

No entanto, o código mostra apenas a pontuação final sobre o número total de perguntas. Faltam os restantes indicadores, que eram parte importante do MVP.

### 4.2 Falta de re-jogar no fim

O enunciado pedia que, no fim, o utilizador pudesse jogar outra vez sem reiniciar o programa. Aqui, o fluxo volta ao menu principal, o que resolve parcialmente a necessidade, mas não existe uma opção explícita de “jogar novamente” logo após o resumo final.

### 4.3 Pequenas inconsistências de linguagem

O projeto mistura várias convenções:

- README em francês e português;
- nomes e mensagens em português do Brasil, português europeu e estilo mais neutro;
- planeamento com linguagem mais formal do que o resto do projeto.

Isto não impede o funcionamento, mas cria alguma falta de unidade.

### 4.4 Código correto, mas algo “limpo demais” para o contexto

O projeto tem uma estrutura muito arrumada e um estilo bastante uniforme. Em si isso é positivo. No entanto, no contexto indicado pelo professor, isso também levanta dúvidas sobre a autoria real do trabalho, sobretudo quando comparado com a maturidade geral esperada num primeiro projeto de 10.º ano.

## 5. Qualidade do código

### Avaliação geral

**Qualidade do código: boa.**

### O que está bem

- funções pequenas e com objetivo claro;
- responsabilidades separadas;
- lógica simples e legível;
- uso adequado de listas, dicionários e JSON;
- validações básicas bem colocadas.

### O que precisa de melhorar

- o resumo final devia ser mais completo;
- faltam alguns indicadores pedidos no enunciado;
- o jogo podia ter uma função dedicada para uma pergunta, em vez de manter parte do fluxo diretamente no `main.py`;
- a limpeza e consistência do código contrastam com a naturalidade do processo de aprendizagem esperado, o que reforça a necessidade de verificar autoria.

No plano puramente técnico, é um dos projetos mais organizados até agora.

## 6. Qualidade da documentação e comentários

### README

O README é muito polido, bilingue e com linguagem bastante formal. Apresenta:

- objetivos do projeto;
- estado do desenvolvimento;
- instalação e execução;
- visão geral da equipa.

### PLANIFICACAO

O ficheiro de planificação também está bastante organizado:

- modelo de dados;
- entradas/processamento/saídas;
- lista de funções;
- fluxo;
- estrutura de ficheiros;
- plano de testes.

À primeira vista, isto é positivo.

### Limitações

No entanto, há dois problemas aqui:

- parte da documentação parece mais “modelo de documentação” do que documentação natural feita por alunos em início de aprendizagem;
- o plano fala em três estudantes (“Estudante A”, “Estudante B”, “Estudante C”), mas o grupo indicado tem apenas dois elementos.

Esse detalhe é importante, porque sugere que o documento pode ter sido adaptado de um modelo externo e não escrito de raiz especificamente para este grupo.

### Comentários no código

O código tem poucos comentários, mas como as funções são curtas isso não é grave.

### Avaliação

**Documentação: boa na forma, mas com fortes sinais de artificialidade.**

## 7. Uso de IA ou ajuda externa

Este é o ponto mais importante neste caso.

Não posso afirmar com certeza absoluta, só pelo código, que o projeto foi gerado intensivamente por IA. Isso seria uma acusação demasiado forte sem prova direta. Mas há vários indícios consistentes que apontam para ajuda externa significativa:

- README muito polido, bilingue e com estilo quase promocional;
- planificação com estrutura muito “modelo pronto”;
- inconsistência entre o número de membros do grupo e a tabela de responsabilidades;
- link explícito no fim da planificação para um guia externo de como criar ficheiros README;
- estilo do código e da documentação bastante acima do nível expectável para partes específicas, mas sem correspondência completa com todos os requisitos do enunciado.

Isto sugere fortemente que houve, no mínimo, apoio externo relevante na produção do projeto e da documentação.

### Como isso pesa na avaliação

Se o uso de IA era proibido, então este aspeto deve pesar negativamente de forma clara. Mesmo que o projeto funcione bem, a avaliação não pode olhar apenas para o resultado final. Tem também de olhar para:

- autenticidade do trabalho;
- correspondência entre o nível demonstrado e o processo de aprendizagem esperado;
- cumprimento das regras dadas pelo professor.

Neste caso, eu consideraria que a qualidade técnica do projeto é razoavelmente boa, mas a confiança na autoria fica enfraquecida. Isso deve baixar a avaliação global.

## 8. Extras implementados

O projeto inclui alguns aspetos que vão um pouco além do mínimo:

- escolha de categoria;
- dificuldade;
- explicação após resposta;
- Top 10 com histórico de pontuações.

São extras úteis e bem escolhidos.

## 9. Nível das soluções encontradas

As soluções técnicas são adequadas:

- JSON para perguntas e ranking;
- filtragem por categoria e dificuldade;
- validação reutilizável em `utils.py`;
- ordenação de pontuações com `sort`.

Nada aqui é excessivamente complexo, mas está bem montado.

O principal problema não é a solução técnica em si. É a credibilidade do processo de construção do trabalho.

## 10. Coerência do projeto

O projeto é coerente:

- o menu liga bem ao jogo;
- o jogo usa uma estrutura de dados estável;
- o ranking reutiliza a pontuação gravada;
- a planificação bate relativamente certo com a organização do código.

É um projeto com unidade e com aspeto cuidado.

## 11. Outros pontos importantes

### 11.1 É um projeto funcionalmente bom

Do ponto de vista do que aparece no repositório, o projeto está acima da média em organização e clareza.

### 11.2 A questão ética pesa muito

Mas, neste caso, a análise não pode ser apenas técnica. Se a utilização de IA estava proibida, então um projeto com fortes sinais de apoio externo perde valor pedagógico. O objetivo não era só entregar algo “bonito” ou “arrumado”. Era aprender e demonstrar trabalho próprio.

### 11.3 Nem tudo o que parece polido está necessariamente dominado

Uma boa forma de confirmar isso, em contexto de avaliação, seria pedir aos alunos para explicarem oralmente:

- por que dividiram o projeto nestes ficheiros;
- como funciona a filtragem das perguntas;
- como é guardada a pontuação;
- por que o resumo final não mostra certas/erradas/percentagem;
- por que a planificação menciona três estudantes.

Se conseguirem justificar tudo com segurança, a suspeita diminui. Se não conseguirem, isso reforça bastante a ideia de uso indevido de IA.

## 12. Avaliação final resumida

### Síntese

Tecnicamente, este é um projeto bom para o nível do 10.º ano: organizado, funcional, coerente e com vários pontos positivos na estrutura e validação.

No entanto, os sinais de apoio externo ou uso intensivo de IA são suficientemente fortes para que isso pese negativamente na avaliação. Como o uso de IA era proibido, este fator não pode ser ignorado. Assim, o projeto deve ser visto com duas camadas:

- qualidade técnica razoavelmente boa;
- fiabilidade pedagógica enfraquecida.

### Classificação qualitativa sugerida

**Projeto tecnicamente bom, mas com fortes indícios de ajuda externa/IA, o que prejudica a avaliação global.**

### Feedback curto para os alunos

O projeto está bem organizado e funcional, mas a avaliação não depende só do resultado final. Também conta a autenticidade do trabalho e o respeito pelas regras dadas. Quando um trabalho apresenta fortes sinais de apoio externo não autorizado, isso tira valor ao que foi entregue, mesmo que a base técnica seja boa.
