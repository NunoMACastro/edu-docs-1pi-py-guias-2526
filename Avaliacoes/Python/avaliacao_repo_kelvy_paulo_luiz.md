# Avaliação do Projeto

## Grupo

Kelvy, Paulo e Luiz

## Projeto

Jogo de Perguntas em Python

## Enquadramento da avaliação

Esta avaliação teve em conta que se trata de um trabalho de alunos do 10.º ano e do primeiro projeto deste tipo. O objetivo não é avaliar como se fosse um projeto profissional, mas sim perceber o que já foi conseguido, o que está bem encaminhado e o que ainda precisa de ser melhorado.

Neste caso, também pesa o facto de o grupo não ter entregue relatório técnico nem documentação minimamente desenvolvida, o que limita bastante a explicação do trabalho e daquilo que foi realmente pensado ou testado.

## 1. Visão geral

O projeto tenta implementar um quiz em terminal com:

- menu principal;
- escolha de nível de dificuldade;
- perguntas carregadas de ficheiros JSON;
- pontuação acumulada;
- ecrãs simples de ajuda e fim de jogo.

A base existe e percebe-se claramente a intenção do grupo. No entanto, a implementação está bastante simples e ainda longe de uma versão realmente sólida ou completa.

## 2. Nível de implementação

### O que está implementado

- menu principal;
- opção de jogar;
- opção de ajuda/regras;
- opção de sair;
- escolha entre nível fácil, médio e difícil;
- carregamento de perguntas a partir de três ficheiros JSON;
- soma de pontos quando a resposta está correta;
- mensagem final de fim de jogo.

### Estado global

O projeto está num nível básico de implementação. Existe um fluxo mínimo de jogo, mas faltam várias partes importantes pedidas no enunciado.

### Avaliação do nível de implementação

**Nível de implementação: básico e incompleto.**

O grupo conseguiu criar uma estrutura mínima que permite jogar, mas ainda está muito distante de um quiz completo e robusto.

## 3. Pontos positivos

### 3.1 Há separação por ficheiros

O projeto tem pelo menos uma separação básica entre:

- `main.py`;
- `menu.py`;
- `logica.py`;
- ficheiros JSON com perguntas.

Para um primeiro projeto, esta divisão já é um ponto positivo.

### 3.2 Uso de JSON

As perguntas estão guardadas em ficheiros JSON separados por dificuldade, o que mostra que o grupo compreendeu uma das partes centrais do enunciado: ler dados de um ficheiro externo em vez de escrever tudo diretamente no código.

### 3.3 Ideia de pontuação por dificuldade

Os ficheiros têm pontuações diferentes conforme o nível e a pergunta. Isso mostra tentativa de enriquecer o jogo para além do mais básico.

## 4. Problemas encontrados

### 4.1 Falta muita coisa do MVP

O enunciado pedia, entre outras coisas:

- resumo final com pontuação, certas, erradas e percentagem;
- possibilidade de re-jogar sem reiniciar o programa;
- validação robusta de inputs;
- menu amigável;
- tratamento de erros sem crashes.

Neste projeto, várias dessas partes estão ausentes ou apenas muito parcialmente presentes.

### 4.2 Validação de inputs muito fraca

Este é um dos maiores problemas do projeto.

Por exemplo:

- `menu_principal()` faz `int(input(...))` diretamente, sem `try/except`;
- `mostra_pergunta()` também faz `int(input(...))` diretamente;
- se o utilizador escrever uma letra em vez de número, o programa pode crashar.

Ou seja, a robustez pedida no enunciado não está garantida.

### 4.3 Código principal demasiado direto

O `main.py` corre logo o ciclo principal sem estar protegido por uma função `main()` ou por `if __name__ == "__main__":`. Isso não é o mais grave do mundo num primeiro projeto, mas mostra uma estrutura ainda muito inicial.

### 4.4 Funções pouco aproveitadas

Há funções importadas que praticamente não são usadas ou que ficam mal integradas:

- `ajuda` é importada, mas as regras acabam por ser escritas diretamente no `main.py`;
- `calcular_pontos()` existe em `logica.py`, mas depois a soma é feita manualmente no `main.py`.

Isto mostra falta de coerência entre o que foi criado e o que realmente é utilizado.

### 4.5 Sem ranking nem pontuações guardadas

O enunciado recomendava fortemente histórico de pontuações e Top 10 como melhoria relevante. Neste projeto, isso não aparece implementado. A função `mostra_pontos()` apenas mostra os pontos atuais da sessão, sem guardar histórico.

### 4.6 Sem resumo final completo

No fim do jogo, o programa mostra os pontos, mas não mostra:

- número de certas;
- número de erradas;
- percentagem de acerto.

Isto é uma falha importante relativamente ao que foi pedido.

### 4.7 Sem sorteio aleatório

As perguntas parecem ser apresentadas pela ordem em que estão nos ficheiros JSON. O enunciado pedia perguntas aleatórias, e isso aqui não se vê implementado.

### 4.8 Inconsistências nos dados

Os ficheiros JSON têm alguns problemas:

- `perguntas_medias.json` tem apenas 9 perguntas, enquanto os outros têm 10 ou mais;
- o ficheiro difícil mistura perguntas com pontuações 20, 30, 40 e 50 sem explicação clara;
- há pequenas gralhas e escolhas pouco consistentes nas perguntas.

Nada disto impede totalmente o funcionamento, mas mostra pouca revisão.

## 5. Qualidade do código

### Avaliação geral

**Qualidade do código: baixa.**

### O que está bem

- o código é curto e relativamente simples de seguir;
- existem funções com nomes compreensíveis;
- a intenção geral percebe-se.

### O que precisa de melhorar

- falta validação segura;
- há pouca reutilização real das funções;
- a lógica está muito simplificada;
- existem decisões pouco coerentes entre ficheiros;
- o programa ainda está mais próximo de protótipo do que de entrega final.

## 6. Qualidade da documentação e comentários

### Documentação

A documentação é praticamente inexistente.

O `README.md` contém apenas:

- título do projeto;
- uma linha a dizer “Projeto de Python”.

Isto é claramente insuficiente para uma entrega final. O grupo também não entregou relatório técnico, o que enfraquece bastante o trabalho.

### Comentários

Há poucos comentários, e os que existem são muito básicos.

### Avaliação

**Documentação e comentários: muito fracos.**

## 7. Extras implementados

Não se observam extras relevantes para além da separação por dificuldade e da atribuição de pontos.

Não há:

- Top 10;
- explicação após a resposta;
- categorias;
- modo extra;
- histórico de pontuações;
- apresentação mais cuidada.

## 8. Nível das soluções encontradas

As soluções são muito básicas. Isso não é necessariamente negativo num primeiro projeto, mas aqui a simplicidade veio acompanhada de muitas falhas importantes.

O grupo conseguiu montar um esqueleto de quiz, mas ainda não conseguiu transformá-lo num projeto completo.

## 9. Coerência do projeto

O projeto tem alguma coerência na ideia geral:

- escolher nível;
- responder a perguntas;
- acumular pontos.

Mas a coerência técnica é fraca:

- funções criadas mas não usadas corretamente;
- ajuda escrita num sítio diferente da função de ajuda;
- lógica de pontuação duplicada;
- ausência de várias partes essenciais do fluxo.

## 10. Outros pontos importantes

### 10.1 Parece um projeto ainda muito inicial

A sensação geral é que este trabalho ficou numa fase intermédia, sem ter passado por uma fase séria de revisão e fecho.

### 10.2 Faltou polimento final

Mesmo sem fazer grandes extras, o grupo podia ter melhorado bastante apenas com:

- validação correta de inputs;
- resumo final mais completo;
- melhor README;
- mais cuidado na integração das funções;
- sorteio aleatório das perguntas.

### 10.3 A base existe, mas ainda é curta

Não é um projeto vazio. Há trabalho feito. Mas é claramente um dos trabalhos mais frágeis do conjunto.

## 11. Avaliação final resumida

### Síntese

O grupo conseguiu construir uma base mínima de quiz com níveis, perguntas em JSON e acumulação de pontos. Isso mostra algum entendimento dos objetivos principais do projeto.

No entanto, a entrega ficou muito incompleta. Faltam várias partes importantes do MVP, a validação de inputs é fraca, a documentação é praticamente inexistente e o projeto não transmite robustez.

### Classificação qualitativa sugerida

**Projeto fraco, com base mínima funcional, mas muito incompleto e pouco polido.**

### Feedback curto para os alunos

Conseguiram montar uma base inicial do jogo, o que já mostra algum trabalho. Mas era preciso ir mais longe no acabamento: validar melhor os inputs, completar o resumo final, organizar melhor as funções e documentar o projeto. A ideia existe, mas a entrega final ficou demasiado curta.
