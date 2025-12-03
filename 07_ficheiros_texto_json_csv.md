# Python (10.º Ano) - 07 · Ficheiros de Texto, JSON e CSV

> **Objetivo deste ficheiro**  
> Aprender a ler e escrever ficheiros simples em Python (texto, JSON e CSV) para guardar e voltar a usar dados entre execuções do programa.

---

## Índice

-   [0. Como usar este ficheiro](#0-como-usar-este-ficheiro)
-   [1. Introdução: porque usar ficheiros?](#1-introdução-porque-usar-ficheiros)
-   [2. Ficheiros JSON (`.json`)](#2-ficheiros-json-json)
-   [3. Ficheiros de texto (`.txt`)](#3-ficheiros-de-texto-txt)
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

## 2. Ficheiros JSON (`.json`)

### 2.1. O que é JSON? · [ESSENCIAL]

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

Json é muito usado para trocar dados entre programas (APIs, bases de dados, etc.). Faz parte do backbone da web moderna uma vez que grande parte dos serviços web usam JSON para comunicar.

Python tem um módulo para trabalhar com JSON: `import json`.

#### 2.1.1. Importar o módulo JSON

Antes de usar funções de JSON, temos de importar o módulo:

```python
import json
```

Um módulo (que vamos ver mais à frente) é um conjunto de funções e variáveis pré-definidas que podemos usar no nosso código.
A partir do momento em que fazemos `import json`, podemos usar as funções do módulo `json` com o prefixo `json.`.

---

### 2.2. Guardar dados em JSON com `json.dump` · [ESSENCIAL]

Imagina que temos uma lista com números:

```python
numeros = [10, 20, 30, 40]
```

Agora queriamos guardar essa lista num ficheiro JSON.
Para isso vamos usar uma nova estrutura, o `with`.

O `with`cria um contexto para abrir o ficheiro e garantir que ele é fechado no final do bloco.

Depois usamos a função `open` para abrir o ficheiro em modo de escrita (`"w"`).

```python
import json

numeros = [10, 20, 30, 40]

with open("numeros.json", "w") as f:
    json.dump(numeros, f)
```

Isto cria um ficheiro `numeros.json` com o seguinte conteúdo:

```json
[10, 20, 30, 40]
```

Outro exemplo, com um dicionário.
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
Repara que agora temos mais argumentos em `json.dump` e no `open`. Ambas as funções aceitam vários parâmetros opcionais para controlar o comportamento da interação com o ficheiro.

-   `encoding="utf-8"` → para suportar acentos.
-   `json.dump(dados, ficheiro, ...)` escreve os dados em formato JSON.
-   `ensure_ascii=False` → permite acentos no ficheiro.
-   `indent=4` → “bonito” (indentado) e fácil de ler.

Abre depois `aluno.json` no editor e observa a estrutura.

> O que é o utf-8?
> UTF-8 é um padrão de codificação de caracteres que permite representar praticamente todos os caracteres usados em línguas humanas. Usar UTF-8 garante que acentos, símbolos e caracteres especiais são armazenados corretamente em ficheiros de texto.
> Basicamente é um mapa que diz ao computador como transformar os bits (0s e 1s) em letras e símbolos que nós entendemos.
> Por exemplo:
>
> -   A letra "a" minúscula é representada pelo byte 01100001 em UTF-8.
> -   A letra "á" (com acento) é representada por dois bytes: 11000011 10100001.
>     Usar UTF-8 é importante para evitar problemas com caracteres estranhos ou ilegíveis, especialmente quando trabalhamos com línguas que usam acentos ou símbolos especiais.

> O que é ASCII?
> ASCII (American Standard Code for Information Interchange) é um padrão de codificação de caracteres que representa letras, números e símbolos básicos usando 7 bits (128 caracteres). É limitado a caracteres em inglês sem acentos ou símbolos especiais.
> Por exemplo:
>
> -   A letra "A" maiúscula é representada pelo byte 01000001 em ASCII.
> -   O número "0" é representado pelo byte 00110000.
>     ASCII é simples e eficiente, mas não suporta caracteres acentuados ou símbolos usados em outras línguas. Por isso, para textos com acentos ou caracteres especiais, usamos UTF-8, que é mais abrangente.

> Então porque usamos os dois? Um no `open` e outro no `json.dump`?
> Usamos `encoding="utf-8"` no `open` para garantir que o ficheiro é lido e escrito corretamente com acentos e caracteres especiais. Já o `ensure_ascii=False` no `json.dump` diz ao Python para não converter caracteres não-ASCII em sequências de escape (como `\u00e1` para "á"), permitindo que os acentos sejam escritos diretamente no ficheiro JSON. Assim, garantimos que tanto a leitura/escrita do ficheiro quanto o formato JSON suportam corretamente os caracteres especiais.

### 2.3. Ler dados de JSON com `json.load` · [ESSENCIAL]

Agora vamos ler o mesmo ficheiro e trabalhar com os dados em Python:

```python
import json

with open("aluno.json", "r", encoding="utf-8") as f:
    aluno = json.load(f)   # volta a ser um dicionário Python em "aluno"

# A partir daqui podemos usar "aluno" como um dicionário normal

print("Nome:", aluno["nome"])
print("Notas:", aluno["notas"])
media = sum(aluno["notas"]) / len(aluno["notas"])
print("Média:", media)
```

Repara:

-   `json.load(f)` → lê do ficheiro e devolve um dicionário/lista normal de Python.
-   Depois podemos usar `[]`, `for`, etc., como em qualquer estrutura.

---

### 2.4. Lista de vários registos em JSON · [ESSENCIAL]

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

### 2.5. Modos de abertura de ficheiros · [ESSENCIAL]

Ao abrir ficheiros (independentemente do tipo de ficheiro), usamos diferentes modos:

-   `"r"` → ler (read) → ficheiro deve existir;
-   `"w"` → escrever (write) → cria ou apaga o conteúdo antigo. O conteúdo antigo é perdido;
-   `"a"` → acrescentar (append) → cria se não existir, acrescenta no fim sem apagar o conteúdo antigo.
-   `"x"` → criar (create) → cria o ficheiro vazio, dá erro se já existir.
-   `"b"` → binário (binary) → usado para ficheiros não-texto (imagens, som, etc.). Não vamos usar aqui.

Podemos combinar modos, por exemplo:

-   `"rb"` → ler em binário;
-   `"wb"` → escrever em binário;
-   `"ab"` → acrescentar em binário.

---

## 3. Ficheiros de texto (`.txt`)

### 3.1. Abrir um ficheiro com `open` e `with` · [ESSENCIAL]

Em Python podemos usar ficheiros de texto. Ficheiros de texto são ficheiros simples que contêm apenas texto legível (sem formatação especial).
Normalmente têm a extensão `.txt`, mas podem ter outras extensões também.

Sintaxe básica (forma recomendada):

```python
with open("exemplo.txt", "w", encoding="utf-8") as f:
    f.write("Olá, ficheiro!\n")
```

Notas:

> Todas as regras da abertura de ficheiros em JSON também se aplicam aqui (modos, encoding, etc.).

---

### 3.2. Escrever várias linhas num ficheiro de texto · [ESSENCIAL]

Exemplo: pedir 3 frases ao utilizador e guardá-las num ficheiro.

```python
with open("frases.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        frase = input(f"Frase {i + 1}: ")
        f.write(frase + "\n")
```

Depois abre `frases.txt` no editor e confirma o conteúdo.

---

### 3.3. Ler um ficheiro de texto linha a linha · [ESSENCIAL]

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

### 3.4. Ler ficheiro inteiro de uma vez · [EXTRA]

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

### Exercício 1 - Lista de números em JSON · [BÁSICO]

Cria um programa que:

-   Gere uma lista com 100 números inteiros aleatórios entre 1 e 1000;
-   Guarde essa lista num ficheiro `numeros.json` usando `json.dump`.

---

### Exercício 2 - Ler lista de números de JSON · [BÁSICO]

Cria um programa que:

-   Leia o ficheiro `numeros.json` do exercício anterior usando `json.load`;
-   Calcule e mostre:

    -   o maior número;
    -   o menor número;
    -   a média dos números.

-   Depois, pede ao utilizador um número e verifica se está no ficheiro.

---

### Exercício 3 - Diário simples (`.json`) · [BÁSICO]

Cria um programa que:

-   pede ao utilizador que escreva uma frase (mensagem do dia);
-   acrescenta essa frase no fim do ficheiro `diario.json` (usa uma lista);
-   no fim, mostra uma mensagem a indicar que a frase foi guardada.

Corre o programa 2–3 vezes e verifica se o ficheiro foi sendo atualizado.

---

### Exercício 4 - Ler o diário · [BÁSICO]

Escreve um programa que:

-   lê o ficheiro `diario.json`;
-   mostra todas as frases numeradas (1:, 2:, 3:, ...).

---

### Exercício 5 - Usando funções, dicionários e JSON · [INTERMÉDIO]

Escreve um programa que:

-   define uma função `adicionar_tarefa(titulo, descricao)` que:
    -   lê o ficheiro `tarefas.json` (se existir);
    -   acrescenta uma nova tarefa (dicionário com `titulo` e `descricao`) a uma lista de tarefas;
    -   guarda a lista atualizada de tarefas no ficheiro;
-   define uma função `mostrar_tarefas()` que:
    -   lê o ficheiro `tarefas.json`;
    -   mostra todas as tarefas numeradas;
-   no programa principal, cria um menu de navegação simples com 3 opções:

    -   adicionar tarefa;
    -   mostrar tarefas;
    -   sair.

---

### Exercício 6 - Gestão de contactos · [INTERMÉDIO]

Escreve um programa que:

-   define uma função `adicionar_contacto(nome, telefone)` que:
    -   lê o ficheiro `contactos.json` (se existir);
    -   acrescenta um novo contacto (dicionário com `nome` e `telefone`) a uma lista de contactos;
    -   guarda a lista atualizada de contactos no ficheiro;
-   define uma função `mostrar_contactos()` que:
    -   lê o ficheiro `contactos.json`;
    -   mostra todos os contactos numerados;
-   no programa principal, cria um menu de navegação simples com 4 opções:
    -   adicionar contacto;
    -   mostrar contactos;
    -   procurar contacto por nome;
    -   sair.

---

### Exercício 7 - Gestão de notas · [DESAFIO]

Escreve um programa que:

-   define uma função `adicionar_nota(aluno, disciplina, nota)` que:
    -   lê o ficheiro `notas.json` (se existir);
    -   acrescenta uma nova nota (dicionário com `aluno`, `disciplina` e `nota`) a uma lista de notas;
    -   guarda a lista atualizada de notas no ficheiro;
-   define uma função `mostrar_notas()` que:
    -   lê o ficheiro `notas.json`;
    -   mostra todas as notas numeradas;
-   define uma função `calcular_media(aluno)` que:
    -   lê o ficheiro `notas.json`;
    -   calcula e retorna a média das notas do aluno especificado;
-   no programa principal, cria um menu de navegação simples com 5 opções:
    -   adicionar nota;
    -   mostrar notas;
    -   calcular média de um aluno;
    -   mostrar aluno com melhor média;
    -   sair.

---

## 7. Changelog

-   **2025-11-26 · v1.0**
    -   Criação inicial do ficheiro com introdução a ficheiros de texto, JSON e CSV.
