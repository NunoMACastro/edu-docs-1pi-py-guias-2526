# Python (10.º Ano) - 08 · Exceções e Tratamento de Erros

> **Objetivo deste ficheiro**  
> Perceber porque acontecem erros em tempo de execução, aprender a ler mensagens de erro e usar `try`/`except` para tornar os programas mais robustos e amigáveis.

---

## Índice

-   [0. Como usar este ficheiro](#0-como-usar-este-ficheiro)
-   [1. Tipos de erros em Python · \[ESSENCIAL\]](#1-tipos-de-erros-em-python--essencial)
-   [2. Como ler mensagens de erro · \[ESSENCIAL\]](#2-como-ler-mensagens-de-erro--essencial)
-   [3. Introdução a `try`/`except` · \[ESSENCIAL\]](#3-introdução-a-tryexcept--essencial)
-   [4. Capturar exceções específicas · \[ESSENCIAL\]](#4-capturar-exceções-específicas--essencial)
-   [5. Várias cláusulas `except` e exceção genérica · \[EXTRA\]](#5-várias-cláusulas-except-e-exceção-genérica--extra)
-   [6. `else` e `finally` · \[EXTRA / curiosidade\]](#6-else-e-finally--extra--curiosidade)
-   [7. Lançar erros com `raise` (e `assert`) · \[EXTRA\]](#7-lançar-erros-com-raise-e-assert--extra)
-   [8. Boas práticas ao tratar erros](#8-boas-práticas-ao-tratar-erros)
-   [9. Exercícios - Exceções e Tratamento de Erros](#9-exercícios---exceções-e-tratamento-de-erros)
-   [10. Changelog](#10-changelog)

---

## 0. Como usar este ficheiro

1. Garante que estás minimamente confortável com:
    - tipos básicos (`int`, `float`, `str`, `bool`) e `input`/`print` (`01_introducao_variaveis_tipos_strings_io.md`);
    - `if`, `while`, `for`, `range` (`02_operadores_e_controlo_de_fluxo_if_ciclos.md`);
    - listas e dicionários (`03_listas_dicionarios_estruturas_aninhadas.md`);
    - funções básicas (`04_funcoes_do_basico_ao_avancado.md`);
    - ficheiros de texto/JSON/CSV (`07_ficheiros_texto_json_csv.md`).
2. Lê primeiro as secções marcadas como **[ESSENCIAL]**:
    - 1, 2, 3 e 4.
3. Só depois explora as secções marcadas como **[EXTRA]**:
    - 5, 6 e 7.
4. Usa o interpretador ou ficheiros `.py` para:
    - **provocar erros** de propósito,
    - ver as mensagens de erro e analisá-las,
    - reescrever o código com `try`/`except`.
5. No fim, resolve os **exercícios**, começando pelos básicos.

---

## 1. Tipos de erros em Python · [ESSENCIAL]

Quando algo corre mal, o Python pode mostrar vários tipos de erros (exceções).

### 1.1. Erros de sintaxe (`SyntaxError`)

São erros em que o Python **nem sequer consegue começar a correr** o programa.

Exemplo:

```python
if x > 0
    print("positivo")
```

Aqui falta o `:` no `if`.  
Se tentares correr, aparece algo do género:

```text
  File "exemplo.py", line 1
    if x > 0
            ^
SyntaxError: invalid syntax
```

Enquanto não corrigires estes erros, o programa não arranca.

### 1.2. Erros em tempo de execução (exceções)

São erros que acontecem **depois** do programa começar a correr.

Alguns exemplos clássicos:

-   `ZeroDivisionError` → divisão por zero:

    ```python
    x = 10 / 0
    ```

-   `NameError` → usar uma variável que não existe:

    ```python
    print(resultado)  # resultado nunca foi definido
    ```

-   `TypeError` → tipos incompatíveis:

    ```python
    total = "10" + 5   # string + inteiro → erro
    ```

-   `ValueError` → valor inválido na conversão:

    ```python
    numero = int("abc")    # "abc" não é um número
    ```

-   `IndexError` → índice fora dos limites de uma lista:

    ```python
    lista = [1, 2, 3]
    print(lista[5])        # não existe índice 5
    ```

-   `KeyError` → chave inexistente num dicionário:

    ```python
    aluno = {"nome": "Ana", "nota": 15}
    print(aluno["idade"])  # não existe "idade"
    ```

Vamos aprender a **ler** estas mensagens e depois a **tratá-las**.

---

## 2. Como ler mensagens de erro · [ESSENCIAL]

Quando acontece um erro em tempo de execução, o Python mostra um “rasto” (traceback).

Exemplo:

```python
numero = int(input("Número inteiro: "))
print(10 / numero)
```

Se o utilizador escrever `0`, aparece algo deste tipo:

```text
Traceback (most recent call last):
  File "exemplo.py", line 2, in <module>
    print(10 / numero)
ZeroDivisionError: division by zero
```

Coisas importantes para reparar:

1. **Ficheiro e linha**:
    - `File "exemplo.py", line 2` → onde o erro aconteceu.
2. **Código da linha**:
    - `print(10 / numero)` → o que estava a ser executado.
3. **Tipo de erro**:
    - `ZeroDivisionError` → categoria do problema.
4. **Mensagem**:
    - `division by zero` → descrição em inglês.

Quando estiveres a depurar (resolver problemas):

-   lê sempre a **última linha** do traceback (tipo de erro + mensagem);
-   vê **a linha de código** indicada;
-   tenta perceber **que valores** estavam a ser usados nessa linha.

---

## 3. Introdução a `try`/`except` · [ESSENCIAL]

O que acontece normalmente:

-   se houver um erro, o programa **pára** imediatamente;
-   o utilizador vê uma mensagem técnica (traço grande com inglês);
-   em programas reais, isso não é aceitável.

Com `try`/`except`, podemos **interceptar** certos erros e reagir de forma controlada.

### 3.1. Sintaxe básica

```python
try:
    # código que pode dar erro
    numero = int(input("Número inteiro: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except:
    # o que fazer se DEU erro
    print("Ups, algo correu mal.")
```

Funcionamento:

-   o Python entra no bloco `try` e executa as linhas normalmente;
-   se não houver erro → ignora o `except`;
-   se houver erro em alguma linha do `try`:
    -   pára aí,
    -   salta para dentro do bloco `except`,
    -   executa o código do `except` em vez de parar o programa.

**Atenção:**  
Neste exemplo o `except` é **genérico** (apanha qualquer erro).  
Mais à frente vamos ver porque isto deve ser usado com cuidado.

### 3.2. Exemplo: conversão segura com `int` · [ESSENCIAL]

Queremos pedir um inteiro, mas o utilizador pode escrever qualquer coisa.

```python
try:
    idade = int(input("Idade (em anos): "))
    print("Daqui a 10 anos terás", idade + 10, "anos.")
except ValueError:
    print("Por favor escreve um número inteiro válido.")
```

Aqui já estamos a capturar **um tipo de erro específico** (`ValueError`).  
É melhor do que apanhar “todos os erros” sem saber qual é.

---

## 4. Capturar exceções específicas · [ESSENCIAL]

É muito importante saber **que erro estamos à espera**.

### 4.1. `ValueError` ao converter `input` · [ESSENCIAL]

Padrão típico: ler número do utilizador.

```python
try:
    numero = int(input("Escreve um número inteiro: "))
    print("Número ao quadrado:", numero ** 2)
except ValueError:
    print("Isso não parece um número inteiro...")
```

Se o utilizador escrever `abc`, apanhamos o `ValueError` e mostramos uma mensagem amigável.

### 4.2. `ZeroDivisionError` em divisões · [ESSENCIAL]

Outro clássico: divisão por zero.

```python
try:
    numerador = float(input("Numerador: "))
    denominador = float(input("Denominador: "))
    resultado = numerador / denominador
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except ValueError:
    print("Por favor escreve números válidos.")
```

Repara que já temos **dois `except` diferentes**:

-   um para divisão por zero,
-   outro para conversão de strings para números.

### 4.3. `FileNotFoundError` ao abrir ficheiros · [ESSENCIAL]

Ligação com o ficheiro `07_ficheiros_texto_json_csv.md`.

```python
nome_ficheiro = input("Nome do ficheiro: ")

try:
    with open(nome_ficheiro, "r", encoding="utf-8") as f:
        conteudo = f.read()
except FileNotFoundError:
    print("Não foi possível encontrar esse ficheiro.")
else:
    # só chega aqui se NÃO tiver havido erro
    print("Conteúdo do ficheiro:")
    print(conteudo)
```

Aqui introduzimos também o `else` (vamos explicar melhor na secção 6).

---

## 5. Várias cláusulas `except` e exceção genérica · [EXTRA]

### 5.1. Vários `except` separados

Já vimos um exemplo com `ZeroDivisionError` e `ValueError`.  
Podemos organizar assim:

```python
try:
    numero = int(input("Número inteiro: "))
    print("10 / número =", 10 / numero)
except ValueError:
    print("Isso não é um inteiro.")
except ZeroDivisionError:
    print("Não podes dividir por zero.")
```

O primeiro `except` compatível com o erro é o que é usado.

### 5.2. Apanhar vários tipos de uma vez

Às vezes queremos reagir da mesma forma a vários tipos de erro.

```python
try:
    numero = int(input("Número inteiro: "))
    print("10 / número =", 10 / numero)
except (ValueError, ZeroDivisionError):
    print("Erro: escreve um inteiro diferente de zero.")
```

Repara nos parênteses à volta dos tipos de erro.

### 5.3. `except Exception` (quase todos os erros) · [cuidado!]

Podemos usar:

```python
try:
    # código
except Exception as e:
    print("Ocorreu um erro:", e)
```

Problemas:

-   pode esconder erros de programação (bugs) que deviam ser corrigidos;
-   se usares isto em todo o lado, ficas sem saber o que se passou.

Regra geral para quem está a aprender:

-   **prefere apanhar erros específicos** (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`, etc.);
-   usa `Exception` apenas em casos especiais e com muito cuidado.

---

## 6. `else` e `finally` · [EXTRA / curiosidade]

### 6.1. `else` depois de `try`/`except`

O bloco `else` é **opcional** e corre **apenas se não houver erro**.

```python
try:
    numero = int(input("Número inteiro: "))
except ValueError:
    print("Isso não é um inteiro.")
else:
    # só corre se NÃO tiver havido ValueError
    print("Número ao quadrado:", numero ** 2)
```

É útil para separar:

-   a parte que pode falhar (`try`),
-   da parte que só faz sentido se correu tudo bem (`else`).

### 6.2. `finally` (executa sempre)

O bloco `finally` também é **opcional** e corre **sempre**:

-   se houver erro,
-   se não houver erro.

Exemplo mais teórico (ficheiros já são bem tratados com `with`):

```python
f = open("dados.txt", "w", encoding="utf-8")

try:
    f.write("Alguns dados...\n")
    # mais código que pode dar erro
finally:
    f.close()   # garante que o ficheiro é fechado
```

Hoje em dia, quase sempre preferimos:

```python
with open("dados.txt", "w", encoding="utf-8") as f:
    f.write("Alguns dados...\n")
```

Porque o `with` já trata da parte de fechar o ficheiro.

---

## 7. Lançar erros com `raise` (e `assert`) · [EXTRA]

### 7.1. `raise` para indicar situações proibidas

Às vezes queremos **nós próprios** lançar um erro, para indicar que algo inesperado aconteceu.

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("O denominador não pode ser zero.")
    return a / b
```

Se alguém chamar `dividir(10, 0)`, é lançado um `ValueError` com a mensagem indicada.

Mais tarde, esse erro pode ser tratado com `try`/`except` noutro sítio do programa.

### 7.2. `assert` para verificações rápidas

Já foi falado em `05_algoritmos_e_padroes_de_programacao.md`, mas fica o resumo:

```python
def media(numeros):
    assert len(numeros) > 0, "Lista não pode ser vazia"
    return sum(numeros) / len(numeros)
```

-   Se a condição for `True`, o programa continua normalmente.
-   Se for `False`, é lançado um `AssertionError` com a mensagem.

`assert` é útil para testes rápidos e para garantir certas condições em funções.

---

## 8. Boas práticas ao tratar erros

-   Tenta perceber **porque** o erro acontece antes de usar `try`/`except`.
-   Não uses `except:` ou `except Exception:` em todo o lado “só para não dar erro”.
-   Prefere **capturar exceções específicas** (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`, etc.).
-   Mostra mensagens claras ao utilizador, de preferência em português simples.
-   Não “engulas” o erro sem fazer nada:
    -   evita `except: pass`.
-   Usa `try`/`except` para:
    -   validar `input` do utilizador;
    -   lidar com ficheiros que podem não existir;
    -   tratar dados vindos de fora do programa (JSON, CSV, etc.).

---

## 9. Exercícios - Exceções e Tratamento de Erros

### Exercício 1 - Leitura segura de inteiro · [BÁSICO]

Escreve um programa que:

-   pede um número inteiro ao utilizador;
-   usa `try`/`except` para:
    -   mostrar o quadrado do número, **se estiver tudo bem**;
    -   mostrar uma mensagem amigável **se o utilizador escrever algo inválido** (por exemplo, `abc`).

Sugestão: começa por provocar o erro sem `try`/`except`, depois acrescenta o tratamento.

---

### Exercício 2 - Repetir até ser válido · [BÁSICO]

Melhora o exercício anterior:

-   usa um ciclo `while True` para pedir um número inteiro;
-   se a conversão com `int` correr bem, sai do ciclo (`break`) e mostra o resultado;
-   se der `ValueError`, mostra uma mensagem e volta a pedir o número.

---

### Exercício 3 - Divisão segura · [BÁSICO]

Escreve um programa que:

-   pede dois números (numerador e denominador);
-   tenta fazer a divisão;
-   trata separadamente:
    -   `ValueError` (se o utilizador escrever algo que não seja número),
    -   `ZeroDivisionError` (se o denominador for zero).

Mostra mensagens diferentes em cada caso.

---

### Exercício 4 - Leitura de ficheiro com mensagem amigável · [BÁSICO]

Escreve um programa que:

-   pede o nome de um ficheiro ao utilizador;
-   tenta abrir o ficheiro em modo leitura e mostrar o seu conteúdo;
-   se o ficheiro **não existir**, apanha `FileNotFoundError` e mostra uma mensagem clara (sem traceback).

Dica: liga com o que aprendeste em `07_ficheiros_texto_json_csv.md`.

---

### Exercício 5 - Soma de números numa linha · [INTERMÉDIO]

Escreve um programa que:

-   pede ao utilizador uma linha com vários números separados por espaços, por exemplo:

    ```text
    10 5 -3 7
    ```

-   divide a linha em partes (`split`);
-   tenta converter cada parte para inteiro e somar todos os valores;
-   se alguma parte não for um número válido, apanha `ValueError` e:
    -   mostra uma mensagem a indicar qual foi o valor inválido;
    -   ignora esse valor e continua com os restantes.

---

### Exercício 6 - Leitura de JSON com tratamento de erros · [INTERMÉDIO]

Cria um ficheiro `aluno.json` parecido com:

```json
{
    "nome": "Ana",
    "idade": 16,
    "notas": [14, 15, 12]
}
```

Escreve um programa que:

-   tenta abrir e ler o ficheiro `aluno.json` com `json.load`;
-   se o ficheiro não existir, apanha `FileNotFoundError` e mostra uma mensagem;
-   se o ficheiro existir mas o conteúdo estiver estragado (JSON inválido), apanha `json.JSONDecodeError` e mostra uma mensagem adequada;
-   se tudo correr bem, mostra o nome do aluno e a média das notas.

---

### Exercício 7 - Menu com validação de opções · [INTERMÉDIO]

Escreve um pequeno programa com menu:

```text
1 - Dizer olá
2 - Mostrar a tabuada do 5
3 - Sair
```

Requisitos:

-   o programa pede ao utilizador uma opção;
-   usa `try`/`except` para garantir que a opção é um inteiro válido;
-   se a opção não existir (por exemplo, 10), mostra uma mensagem e volta a pedir;
-   só termina quando o utilizador escolher a opção 3.

---

### Exercício 8 (Desafio) - Função `dividir` robusta · [DESAFIO]

Cria uma função `dividir(a, b)` que:

-   verifica se `b` é zero;
-   se for zero, lança um `ValueError` com uma mensagem clara usando `raise`;
-   caso contrário, devolve o resultado da divisão.

Depois cria um programa que:

-   pede `a` e `b` ao utilizador;
-   chama `dividir(a, b)` dentro de um `try`;
-   trata o `ValueError` lançado pela função, mostrando uma mensagem amigável.

---

### Exercício 9 (Desafio) - Estatísticas robustas a partir de CSV · [DESAFIO]

Supondo um ficheiro `notas.csv` com:

```text
nome;nota
Ana;15
Bruno;abc
Carla;18
```

Escreve um programa que:

-   tenta abrir o ficheiro `notas.csv` (trata `FileNotFoundError`);
-   percorre cada linha (ignorando o cabeçalho);
-   tenta converter a nota para inteiro:
    -   se correr bem, usa essa nota;
    -   se der erro (`ValueError`), mostra uma mensagem a indicar o nome do aluno com nota inválida e ignora essa linha;
-   no fim, mostra:
    -   média das notas válidas;
    -   número de linhas ignoradas por erro.

---

### Exercício 10 (Desafio) - Diário com opções e tratamento de erros · [DESAFIO]

Junta o que aprendeste em ficheiros e exceções.  
Cria um programa que funcione como um “diário” simples:

```text
1 - Escrever nova entrada
2 - Ver entradas
3 - Sair
```

Requisitos:

-   todas as entradas são guardadas em `diario.txt` (uma por linha);
-   o programa usa `try`/`except` para:
    -   lidar com erros ao abrir/ler/escrever o ficheiro;
    -   validar a opção do menu (tem de ser 1, 2 ou 3);
-   se o ficheiro ainda não existir quando o utilizador escolher “Ver entradas”, mostra uma mensagem simpática (por exemplo, “Ainda não tens entradas no diário!”) em vez de um traceback.

---

## 10. Changelog

-   `2025-02-XX` · Criação inicial do ficheiro com introdução a exceções, leitura de mensagens de erro e `try`/`except` básico.
