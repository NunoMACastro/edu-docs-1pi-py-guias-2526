# Python (10.º Ano) - 07 · Ficheiros de Texto, JSON e CSV

> **Objetivo deste ficheiro**  
> Aprender a ler e escrever ficheiros simples em Python (texto, JSON e CSV) para guardar e voltar a usar dados entre execuções do programa.

---

## Índice

-   [0. Como usar este ficheiro](#0-como-usar-este-ficheiro)
-   [1. Introdução: porque usar ficheiros?](#1-introdução-porque-usar-ficheiros)
-   [2. Ficheiros de texto (`.txt`)](#2-ficheiros-de-texto-txt)
-   [3. Ficheiros JSON (`.json`)](#3-ficheiros-json-json)
-   [4. Ficheiros CSV (`.csv`)](#4-ficheiros-csv-csv)
-   [5. Boas práticas com ficheiros](#5-boas-práticas-com-ficheiros)
-   [6. Exercícios - Ficheiros de Texto, JSON e CSV](#6-exercícios---ficheiros-de-texto-json-e-csv)
-   [7. Changelog](#7-changelog)

---

## 0. Como usar este ficheiro

1. Garante que sabes:
    - variáveis, tipos básicos e `input`/`print` (`01_introducao_variaveis_tipos_strings_io.md`);
    - `if`, ciclos `for`/`while` (`02_operadores_e_controlo_de_fluxo_if_ciclos.md`);
    - listas e dicionários (`03_listas_dicionarios_estruturas_aninhadas.md`);
    - funções simples (`04_funcoes_do_basico_ao_avancado.md`).
2. Lê as secções pela ordem: texto → JSON → CSV.
3. Testa todos os exemplos num ficheiro `.py`:
    - observa que ficheiros são criados na mesma pasta;
    - abre os ficheiros no editor para veres o “resultado”.
4. No fim, resolve os **exercícios**.  
   Começa pelos ficheiros de texto, depois JSON, e por fim CSV.

---

## 1. Introdução: porque usar ficheiros?

Até agora, os programas:

-   liam dados com `input`;
-   faziam contas / processamento;
-   mostravam resultados com `print`;
-   quando o programa terminava, **tudo se perdia**.

Com **ficheiros**, podemos:

-   guardar dados para usar **noutra execução** do programa;
-   ler informação que outra pessoa / programa escreveu;
-   trocar dados com outros programas (por exemplo, Excel).

Tipos de ficheiros que vamos ver:

-   **texto (`.txt`)** → linhas de texto normal;
-   **JSON (`.json`)** → estrutura de dados (dicionários/listas) em formato de texto;
-   **CSV (`.csv`)** → tabela simples (linhas / colunas), muito usado em folhas de cálculo.

---

## 2. Ficheiros de texto (`.txt`)

### 2.1. Abrir um ficheiro com `open` e `with` · [ESSENCIAL]

Em Python usamos a função `open` para trabalhar com ficheiros.

Sintaxe básica (forma recomendada):

```python
with open("exemplo.txt", "w", encoding="utf-8") as f:
    f.write("Olá, ficheiro!\n")
```

Explicação:

-   `"exemplo.txt"` → nome do ficheiro (cria se não existir).
-   `"w"` → modo de abertura:
    -   `"w"` → escrever (apaga o conteúdo antigo, se existir);
    -   `"a"` → acrescentar no fim (sem apagar);
    -   `"r"` → ler (dá erro se o ficheiro não existir).
-   `encoding="utf-8"` → garante que caracteres como `á`, `ç`, etc. funcionam bem.
-   `with ... as f:` → garante que o ficheiro é **fechado** no fim do bloco.

### 2.2. Escrever várias linhas num ficheiro de texto · [ESSENCIAL]

Exemplo: pedir 3 frases ao utilizador e guardá-las num ficheiro.

```python
with open("frases.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        frase = input(f"Frase {i + 1}: ")
        f.write(frase + "\n")
```

Depois abre `frases.txt` no editor e confirma o conteúdo.

### 2.3. Ler um ficheiro de texto linha a linha · [ESSENCIAL]

Exemplo: ler o ficheiro `frases.txt` e mostrar as linhas numeradas.

```python
with open("frases.txt", "r", encoding="utf-8") as f:
    for numero_linha, linha in enumerate(f, start=1):
        linha = linha.rstrip("\n")   # remove a quebra de linha do fim
        print(f"{numero_linha}: {linha}")
```

Notas:

-   O próprio ficheiro pode ser percorrido com `for`, linha a linha.
-   `enumerate` dá-nos o número da linha e o texto da linha.

### 2.4. Ler ficheiro inteiro de uma vez · [EXTRA]

Às vezes é útil ler tudo para uma string ou lista:

```python
with open("frases.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()       # string com TODO o ficheiro

print(conteudo)
```

Ou:

```python
with open("frases.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()    # lista de strings (linhas)

print(linhas)
```

Para ficheiros grandes, é mais eficiente ler **linha a linha** com `for`.

---

## 3. Ficheiros JSON (`.json`)

### 3.1. O que é JSON? · [ESSENCIAL]

JSON é um formato de texto para guardar **estruturas de dados**:

-   dicionários (`{ ... }`) → pares chave/valor;
-   listas (`[ ... ]`);
-   números, strings, `true`/`false` (em Python → `True`/`False`), `null` (Python → `None`).

Exemplo de JSON no ficheiro `aluno.json`:

```json
{
    "nome": "Ana",
    "idade": 16,
    "notas": [14, 15, 12],
    "aprovado": true
}
```

Python tem um módulo para trabalhar com JSON: `import json`.

### 3.2. Guardar dados em JSON com `json.dump` · [ESSENCIAL]

Vamos guardar um dicionário num ficheiro `aluno.json`:

```python
import json

aluno = {
    "nome": "Ana",
    "idade": 16,
    "notas": [14, 15, 12],
    "aprovado": True,
}

with open("aluno.json", "w", encoding="utf-8") as f:
    json.dump(aluno, f, ensure_ascii=False, indent=4)
```

Notas:

-   `json.dump(dados, ficheiro, ...)` escreve os dados em formato JSON.
-   `ensure_ascii=False` → permite acentos no ficheiro.
-   `indent=4` → “bonito” (indentado) e fácil de ler.

Abre depois `aluno.json` no editor e observa a estrutura.

### 3.3. Ler dados de JSON com `json.load` · [ESSENCIAL]

Agora vamos ler o mesmo ficheiro e trabalhar com os dados em Python:

```python
import json

with open("aluno.json", "r", encoding="utf-8") as f:
    aluno = json.load(f)   # volta a ser um dicionário Python

print("Nome:", aluno["nome"])
print("Notas:", aluno["notas"])
media = sum(aluno["notas"]) / len(aluno["notas"])
print("Média:", media)
```

Repara:

-   `json.load(f)` → lê do ficheiro e devolve um dicionário/lista normal de Python.
-   Depois podemos usar `[]`, `for`, etc., como em qualquer estrutura.

### 3.4. Lista de vários registos em JSON · [ESSENCIAL]

É muito comum guardar **uma lista de dicionários**:

```python
import json

alunos = [
    {"nome": "Ana", "idade": 16, "nota": 15},
    {"nome": "Bruno", "idade": 17, "nota": 12},
    {"nome": "Carla", "idade": 16, "nota": 18},
]

with open("alunos.json", "w", encoding="utf-8") as f:
    json.dump(alunos, f, ensure_ascii=False, indent=4)
```

Depois:

```python
import json

with open("alunos.json", "r", encoding="utf-8") as f:
    alunos = json.load(f)

for aluno in alunos:
    print(aluno["nome"], "-", aluno["nota"])
```

Isto é útil para pequenos sistemas de gestão (alunos, produtos, etc.).

---

## 4. Ficheiros CSV (`.csv`)

### 4.1. O que é um CSV? · [ESSENCIAL]

CSV significa **Comma-Separated Values** (valores separados por vírgulas).

-   É um formato de texto para guardar **tabelas** (linhas e colunas).
-   Cada linha é um registo (por exemplo, um aluno).
-   As colunas são separadas por vírgulas ou ponto e vírgula.

Exemplo de `alunos.csv`:

```text
nome;idade;nota
Ana;16;15
Bruno;17;12
Carla;16;18
```

### 4.2. Escrever CSV “à mão” · [ESSENCIAL]

Sem usar módulos, podemos escrever linhas de texto separadas por `;`:

```python
with open("alunos.csv", "w", encoding="utf-8") as f:
    f.write("nome;idade;nota\n")  # cabeçalho

    alunos = [
        {"nome": "Ana", "idade": 16, "nota": 15},
        {"nome": "Bruno", "idade": 17, "nota": 12},
        {"nome": "Carla", "idade": 16, "nota": 18},
    ]

    for aluno in alunos:
        linha = f"{aluno['nome']};{aluno['idade']};{aluno['nota']}\n"
        f.write(linha)
```

Depois podes abrir `alunos.csv` no Excel / LibreOffice / Google Sheets.

### 4.3. Ler CSV “à mão” · [ESSENCIAL]

Vamos ler `alunos.csv` e calcular a média das notas:

```python
with open("alunos.csv", "r", encoding="utf-8") as f:
    cabecalho = f.readline()   # lê a primeira linha e ignora

    soma_notas = 0
    contador = 0

    for linha in f:
        linha = linha.strip()          # tira \n
        nome, idade_str, nota_str = linha.split(";")

        idade = int(idade_str)
        nota = int(nota_str)

        soma_notas += nota
        contador += 1

media = soma_notas / contador
print("Média das notas:", media)
```

Notas:

-   `split(";")` → divide a linha em partes (lista de strings).
-   É importante converter `idade` e `nota` para `int`.

### 4.4. Usar o módulo `csv` (curiosidade / EXTRA)

Python tem um módulo `csv` que ajuda a tratar casos mais chatos (vírgulas dentro de textos, etc.).  
Como curiosidade:

```python
import csv

with open("alunos.csv", "r", encoding="utf-8", newline="") as f:
    leitor = csv.DictReader(f, delimiter=";")
    for linha in leitor:
        print(linha["nome"], "-", linha["nota"])
```

Para o 10.º ano, podes ficar confortável primeiro com a versão “à mão”.

---

## 5. Boas práticas com ficheiros

-   Usa sempre `with open(...)` para garantir que o ficheiro é fechado.
-   Usa `encoding="utf-8"` para evitar problemas com acentos.
-   Se o ficheiro for grande, **lê linha a linha** com um ciclo `for`.
-   Escolhe nomes de ficheiros claros: `alunos.txt`, `produtos.csv`, etc.
-   Guarda ficheiros de dados **junto do teu script** enquanto estás a aprender (para simplificar caminhos).

---

## 6. Exercícios - Ficheiros de Texto, JSON e CSV

### Exercício 1 - Diário simples (`.txt`) · [BÁSICO]

Cria um programa que:

-   pede ao utilizador que escreva uma frase (mensagem do dia);
-   acrescenta essa frase no fim do ficheiro `diario.txt` (uma frase por linha);
-   no fim, mostra uma mensagem a indicar que a frase foi guardada.

Corre o programa 2–3 vezes e verifica se o ficheiro foi sendo atualizado.

---

### Exercício 2 - Ler o diário · [BÁSICO]

Escreve um programa que:

-   lê o ficheiro `diario.txt`;
-   mostra todas as linhas numeradas (1:, 2:, 3:, ...).

Se o ficheiro ainda não existir, corre primeiro o exercício 1.

---

### Exercício 3 - Contar linhas e caracteres · [BÁSICO]

Escreve um programa que:

-   pede o nome de um ficheiro de texto ao utilizador (por exemplo, `frases.txt`);
-   lê o ficheiro;
-   mostra:
    -   quantas linhas tem;
    -   quantos caracteres (sem contar com as quebras de linha `\n`).

---

### Exercício 4 - Guardar aluno em JSON · [BÁSICO]

Escreve um programa que:

-   pede ao utilizador:
    -   nome do aluno;
    -   idade;
    -   3 notas (podes pedir uma a uma);
-   cria um dicionário com estes dados;
-   guarda o dicionário num ficheiro `aluno.json` usando `json.dump` (indentado).

Depois, abre `aluno.json` no editor e confirma se está correto.

---

### Exercício 5 - Ler aluno de JSON · [BÁSICO]

Escreve um programa que:

-   lê o ficheiro `aluno.json` (do exercício anterior);
-   mostra o nome e idade;
-   calcula e mostra a média das notas;
-   escreve “Aprovado” se a média for ≥ 10; caso contrário, “Reprovado”.

---

### Exercício 6 - Lista de alunos em JSON · [INTERMÉDIO]

Escreve um programa que:

-   permite registar vários alunos;
-   em cada iteração:
    -   pede nome (ou uma string vazia para terminar);
    -   pede nota (inteira);
    -   guarda num dicionário `{"nome": ..., "nota": ...}`;
    -   acrescenta o dicionário a uma lista;
-   no fim, guarda a lista completa em `alunos.json`.

Depois, faz um segundo programa que lê `alunos.json` e:

-   mostra todos os nomes e notas;
-   indica a média da turma.

---

### Exercício 7 - Exportar lista de alunos para CSV · [INTERMÉDIO]

Usando uma lista de dicionários (por exemplo, a do exercício 6), escreve um programa que:

-   pede o nome do ficheiro CSV a criar (por exemplo, `alunos_exportados.csv`);
-   escreve o cabeçalho `nome;nota`;
-   escreve uma linha por cada aluno;
-   no fim, mostra uma mensagem a indicar quantos alunos foram guardados.

Abre o CSV num programa de folha de cálculo e verifica os dados.

---

### Exercício 8 - Ler CSV de produtos · [INTERMÉDIO]

Imagina um ficheiro `produtos.csv` com o seguinte conteúdo:

```text
nome;preco
Caneta;1.20
Caderno;2.50
Lápis;0.80
```

Escreve um programa que:

-   lê o ficheiro `produtos.csv`;
-   mostra o nome e preço de cada produto;
-   calcula o total (soma dos preços de todos os produtos).

---

### Exercício 9 (Desafio) - Fusão de ficheiros TXT → JSON · [DESAFIO]

Imagina que tens vários ficheiros de texto com nomes de alunos, um por linha:

-   `turma_a.txt`
-   `turma_b.txt`

Escreve um programa que:

-   lê todos os nomes de `turma_a.txt` e `turma_b.txt`;
-   cria uma lista com dicionários do tipo `{"turma": "A", "nome": ...}` e `{"turma": "B", "nome": ...}`;
-   guarda essa lista num ficheiro `alunos_todas_as_turmas.json`.

---

### Exercício 10 (Desafio) - Estatísticas a partir de CSV · [DESAFIO]

Supondo que tens um ficheiro `notas.csv` com:

```text
nome;nota
Ana;15
Bruno;8
Carla;18
```

Escreve um programa que:

-   lê o ficheiro;
-   conta quantos alunos estão:
    -   aprovados (nota ≥ 10),
    -   reprovados (nota < 10);
-   mostra a média da turma;
-   mostra o nome do aluno com melhor nota.

---

## 7. Changelog

-   **2025-11-26 · v1.0**
    -   Criação inicial do ficheiro com introdução a ficheiros de texto, JSON e CSV.
