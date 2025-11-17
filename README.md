## Índice

-   [Estrutura do repositório](#estrutura-do-reposit%C3%B3rio)
-   [`01_introducao_variaveis_tipos_strings_io.md`](#01introducaovariaveistiposstringsiomd)
-   [`02_operadores_e_controlo_de_fluxo_if_ciclos.md`](#02operadoresecontrolodefluxoifciclosmd)
-   [`03_listas_dicionarios_estruturas_aninhadas.md`](#03listasdicionariosestruturasaninhadasmd)
-   [`04_funcoes_do_basico_ao_avancado.md`](#04funcoesdobasicoaoavancadomd)
-   [`05_algoritmos_e_padroes_de_programacao.md`](#05algoritmosepadroesdeprogramacaomd)
-   [Como usar estes materiais](#como-usar-estes-materiais)
-   [Pré-requisitos e ambiente de trabalho](#pr%C3%A9-requisitos-e-ambiente-de-trabalho)

# Python · 10.º Ano (Programador de Informática)

Materiais de apoio em formato **Markdown** para introdução à programação em Python, pensados para alunos do **10.º ano - Curso Profissional de Programador de Informática (PI)**.

O objetivo deste repositório é ter um conjunto de **apontamentos estruturados + exercícios graduais**, que os alunos possam usar como:

-   ficha de consulta durante as aulas;
-   material de estudo para testes;
-   base para pequenos projetos.

Cada ficheiro foca um conjunto de temas e termina com:

-   uma secção de **Exercícios** (10–12 exercícios, do mais simples ao mais desafiante);
-   uma secção de **Changelog**, para registar alterações.

---

## Estrutura do repositório

```text
.
├── 01_introducao_variaveis_tipos_strings_io.md
├── 02_operadores_e_controlo_de_fluxo_if_ciclos.md
├── 03_listas_dicionarios_estruturas_aninhadas.md
├── 04_funcoes_do_basico_ao_avancado.md
├── 05_algoritmos_e_padroes_de_programacao.md
└── README.md
```

### `01_introducao_variaveis_tipos_strings_io.md`

**Objetivo:** dar o primeiro contacto com Python e com a ideia de “programa”.

Conteúdos principais:

-   o que é um programa e como o Python executa o código;
-   variáveis e tipos básicos: `int`, `float`, `str`, `bool`, `None`;
-   convenções de nomes (`snake_case`, maiúsculas para constantes);
-   operações básicas com números e strings;
-   métodos de strings mais usados (`lower`, `upper`, `strip`, `replace`, `split`, `join`, etc.);
-   entrada e saída:
    -   `print` (incluindo _f-strings_);
    -   `input` e conversão de tipos (`int`, `float`);
-   noções de comentário e leitura de código.

Inclui exemplos muito simples e exercícios iniciais focados em:

-   declaração de variáveis;
-   pequenas contas;
-   manipulação de strings;
-   uso de `input`/`print`.

---

### `02_operadores_e_controlo_de_fluxo_if_ciclos.md`

**Objetivo:** introduzir o “motor” da lógica de programação: **operadores**, **decisões** e **repetições**.

Conteúdos principais:

-   operadores aritméticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`
    -   diferença entre `/` (divisão real) e `//` (divisão inteira);
    -   exemplos com resto (`%`) e potência (`**`);
-   operadores de comparação: `==`, `!=`, `>`, `>=`, `<`, `<=`
    -   encadeamento de comparações: `1 < x <= 10`;
-   operadores lógicos: `and`, `or`, `not`
    -   tabelas verdade simples;
    -   ideia intuitiva de _short-circuit_;
-   `in` / `not in` (strings, listas, dicionários) e `is` / `is not` (sobretudo com `None`);
-   atribuições compostas: `+=`, `-=`, `*=`, etc.;
-   **truthiness**: o que conta como `False` (`0`, `0.0`, `""`, `[]`, `{}`, `None`);
-   estruturas de seleção:
    -   `if`, `elif`, `else`;
    -   exemplos com classificação de notas (0–20);
    -   `if` aninhado;
    -   expressão condicional (“ternário”) como curiosidade;
-   estruturas de repetição:
    -   `while`: repetir enquanto a condição for verdadeira, cuidado com ciclos infinitos;
    -   `for` sobre strings, listas e `range`;
-   `range()`:
    -   `range(fim)`, `range(inicio, fim)`, `range(inicio, fim, passo)` (inclui passo negativo);
-   blocos de código e indentação:
    -   regra dos 4 espaços;
    -   como o Python usa indentação em vez de `{}`.

Exercícios focados em:

-   classificação de notas;
-   verificar se um número está dentro de um intervalo;
-   contagem decrescente (com `for` e `while`);
-   somatório de 1 até `n`;
-   tabuada;
-   jogo de adivinhar número com limite de tentativas.

---

### `03_listas_dicionarios_estruturas_aninhadas.md`

**Objetivo:** consolidar o armazenamento de coleções de dados e treinar uma forma de pensar mais estruturada.

Conteúdos principais:

-   **listas**:
    -   criação, acesso por índice (positivo e negativo);
    -   alteração de elementos;
    -   métodos: `append`, `insert`, `pop`, `remove`, `clear`, `count`, `index`, `sort`, `reverse`;
    -   funções: `len`, `sum`, `min`, `max`, `sorted`;
    -   percorrer listas com `for` (por elemento e por índice);
    -   padrões clássicos:
        -   construir nova lista;
        -   filtrar valores;
        -   calcular média;
        -   encontrar mínimo/máximo sem `min`/`max`;
    -   pequena introdução a **compreensões de lista** (como curiosidade);
-   **dicionários**:
    -   ideia chave→valor;
    -   criação, acesso, atualização, inserção e remoção;
    -   métodos: `keys`, `values`, `items`, `get`;
    -   verificar existência de chaves com `in`;
    -   exemplos aplicados (preços de frutas, dados de uma pessoa);
-   **estruturas aninhadas**:
    -   lista de listas (matriz);
    -   dicionário de listas (turmas e alunos);
    -   dicionário de dicionários (aluno → disciplina → nota);
    -   lista de dicionários (livros, alunos, etc.);
    -   percorrer com ciclos aninhados;

Inclui exemplos aplicados como:

-   mini “base de dados” de livros;
-   turmas com alunos e notas;
-   temperaturas médias mensais de uma cidade.

Exercícios focados em:

-   criar e percorrer listas;
-   separar pares/ímpares;
-   contar positivos/negativos;
-   manipular dicionários simples;
-   trabalhar com estruturas aninhadas (matriz, turmas, notas, livros).

---

### `04_funcoes_do_basico_ao_avancado.md`

**Objetivo:** construir um módulo sólido sobre **funções**, desde o `def` básico até ideias de ordem superior, com as partes **essenciais** bem destacadas e os tópicos mais avançados claramente marcados como **extra**.

O ficheiro está organizado com etiquetas:

-   **[ESSENCIAL]** – obrigatório para dominar a base de Python;
-   **[EXTRA]** – curiosidade / temas mais avançados (podem ser vistos mais tarde).

Conteúdos principais:

-   porque usar funções:
    -   evitar repetição;
    -   organizar o código;
    -   facilitar testes;
-   definir e chamar funções (`def`):
    -   exemplos básicos (`ola_mundo`, `soma`, `saudacao`);
    -   diferença entre `print` dentro da função e `return`;
-   parâmetros e argumentos:
    -   posicionais vs nomeados;
    -   valores por defeito;
    -   boas práticas para nomes de funções e parâmetros;
-   `return`:
    -   ausência de `return` → `None`;
    -   devolver um valor;
    -   devolver vários valores via **tuplos** (ex.: divisão que devolve quociente e resto);
    -   **saída antecipada** (casos especiais);
-   scope (espaço de nomes):
    -   variáveis locais;
    -   noção de global (como coisa a evitar na maior parte dos casos);
    -   `nonlocal` como curiosidade (exemplo `cria_contador`);
-   mutabilidade e passagem de argumentos:
    -   imutáveis (`int`, `float`, `str`, `tuple`);
    -   mutáveis (`list`, `dict`);
    -   funções que alteram listas recebidas;
    -   perigo de _defaults_ mutáveis (`acumulador_errado` vs `acumulador_correto`);
-   **[EXTRA]** funções de ordem superior e `lambda`:
    -   funções como valores;
    -   `aplicar(func, valor)`;
    -   `map`, `filter`, `sorted(key=...)` vs compreensões de lista;
-   **[EXTRA]** `*args` e `**kwargs`:
    -   funções “elásticas” (`media(*nums)`, `configurar(**opcoes)`);
    -   desempacotar listas e dicionários ao chamar;
-   **[EXTRA]** docstrings e anotações de tipo:
    -   exemplo `normalizar_textos`;
    -   referência rápida a `typing` (`list[str]`, `Sequence[str]`);
-   **[EXTRA]** recursão:
    -   ideia de função que chama a si própria;
    -   caso base e passo recursivo;
    -   exemplo `fatorial`, `conta_decrescente`;
    -   aviso sobre limites e sobre quando preferir `while`/`for`;
-   boas práticas:
    -   funções curtas, uma responsabilidade;
    -   `if __name__ == "__main__":` para demos e pequenos testes;
    -   uso de `assert` para testes rápidos.

Exercícios focados em:

-   escrever funções simples (`ola_mundo`, `soma`, contagem de letras);
-   funções com listas (contar pares/ímpares, média, somatório);
-   funções com dicionários (contar alunos por turma, encontrar a pessoa mais velha, médias por aluno);
-   desafios com `*args` e recursão simples.

---

### `05_algoritmos_e_padroes_de_programacao.md`

**Objetivo:**  
Deixar de ser apenas “truques de Python” e começar a pensar como **programador**, usando o que já se aprendeu (variáveis, listas, dicionários, funções) para resolver problemas completos: analisar o enunciado, planear a solução e só depois escrever código.

Conteúdos principais:

-   como atacar um problema de programação:
    -   identificar **entradas**, **processamento** e **saídas**;
    -   fazer exemplos à mão antes de programar;
    -   escrever um plano em português (pseudocódigo) antes do código;
-   padrões clássicos com **listas**:
    -   leitura de valores para uma lista (input em ciclo + `append`);
    -   padrão de **acumulação** (somatórios, médias);
    -   padrão de **contagem condicional** (contar positivos, pares, aprovados, etc.);
    -   busca de **mínimo/máximo manual** (sem `min`/`max`);
    -   padrão de **filtragem** (nova lista com elementos que cumprem uma condição);
    -   padrão de **transformação** (nova lista com valores transformados);
-   padrões com **dicionários**:
    -   “mini base de dados” em memória (nome → idade, produto → preço, etc.);
    -   procura de chaves (`if chave in dicionario`);
    -   contagem de frequências (quantas vezes aparece cada palavra/letra);
    -   dicionário de listas (turma → lista de alunos);
-   juntar tudo em **funções**:
    -   separar funções “puras” (com `return`) da parte de `input`/`print`;
    -   decompor problemas maiores em funções pequenas (média de alunos, melhor aluno, reprovados, etc.);
-   erros típicos e **debugging básico**:
    -   esquecer `return`, confundir `=` com `==`, erros em `range`, mutabilidade;
    -   uso de `print` intermédios e `assert` para testar.

Exercícios focados em:

-   consolidar padrões com listas e dicionários;
-   aplicar estratégias de decomposição em funções;
-   analisar enunciados em português antes de escrever código;
-   desafios com estruturas aninhadas e pequenos “mini-projetos” guiados.

---

## Como usar estes materiais

1. Segue a **ordem dos ficheiros** (01 → 02 → 03 → 04).
2. Em cada ficheiro:
    - lê primeiro a teoria e os exemplos;
    - copia alguns exemplos para um ficheiro `.py` e experimenta alterá-los;
    - tenta resolver todos os exercícios, pela ordem apresentada;
    - marca as partes com **[EXTRA]** para rever mais tarde se sentires dificuldades.
3. Usa os apontamentos como apoio ao estudo para testes e projetos.

---

## Pré-requisitos e ambiente de trabalho

-   Python 3.x instalado (idealmente uma versão recente, ex.: 3.11/3.12).
-   Editor recomendado: **VS Code** ou IDE online com:
    -   extensão **Python**;
    -   (opcional) ferramenta de execução integrada (Run/Debug).

Para correr um exemplo:

1. Criar um ficheiro, por exemplo `exemplo.py`;
2. Copiar o código do ficheiro `.md` para o `.py`;
3. Guardar;
4. Executar com:
    - `python exemplo.py` no terminal, ou
    - botão de _Run_ do editor.

---
