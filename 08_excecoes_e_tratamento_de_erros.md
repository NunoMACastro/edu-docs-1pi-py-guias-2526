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

> Podemos pedir repetidamente numeros ao utilizador enquanto o que ele introduzir produzir erros:

```python

while True:
    try:
        numerador = float(input("Numerador: "))
        denominador = float(input("Denominador: "))
        resultado = numerador / denominador
    except ZeroDivisionError:
        print("Não é possível dividir por zero. Tenta outra vez.")
    except ValueError:
        print("Por favor escreve números válidos. Tenta outra vez.")
    else:
        # Só chega aqui se NÃO tiver havido erro
        print("Resultado:", resultado)
        break  # sai do ciclo se tudo correu bem
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

## 6. `else` e `finally` · [EXTRA]

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

> Porquê usar o `finally` e não colocar o código fora do `try`/`except`?
> Porque se houver um erro no `try`, o código fora do `try`/`except` **não é executado**.

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

Outro exemplo, mas mais util:

```python
def define_maioridade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa.")
    elif idade >= 18:
        return True
    else:
        return False
```

Deteção do erro:

```python
try:
    idade = int(input("Idade: "))
    maior = define_maioridade(idade)
    if maior:
        print("És maior de idade.")
    else:
        print("És menor de idade.")
except ValueError as e:
    print("Erro:", e)
```

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

## 9. Padrões comuns de exceções

-   **Exemplo usando as mensagens de erro**:

    ```python
    try:
        numero = int(input("Número inteiro: "))
        print("10 / número =", 10 / numero)
    except Exception as e:
        print("Ocorreu um erro:", e)
    ```

-   **Leitura segura de inteiro**:

    ```python
    try:
        numero = int(input("Número inteiro: "))
    except ValueError:
        print("Isso não é um inteiro.")
    ```

-   **Divisão segura**:

    ```python
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Não podes dividir por zero.")
    ```

-   **Leitura de ficheiro com tratamento de erro**:

    ```python
    try:
        with open("dados.txt", "r", encoding="utf-8") as f:
            conteudo = f.read()
    except FileNotFoundError:
        print("Ficheiro não encontrado.")
    else:
        print(conteudo)
    ```

-   **Conversão segura de lista de strings para inteiros**:

    ```python
    strings = ["10", "20", "abc", "30"]
    numeros = []
    for s in strings:
        try:
            n = int(s)
            numeros.append(n)
        except ValueError:
            print(f"Ignorando valor inválido: {s}")
    ```

---

## 10. Lista de erros comuns em Python

-   `SyntaxError` → erro de sintaxe (o programa não arranca).
-   `NameError` → variável não definida.
-   `TypeError` → operação com tipos incompatíveis.
-   `ValueError` → valor inválido (ex.: converter string para número).
-   `IndexError` → índice fora dos limites de uma lista.
-   `KeyError` → chave inexistente num dicionário.
-   `ZeroDivisionError` → divisão por zero.
-   `FileNotFoundError` → ficheiro não encontrado.
-   `IOError` / `OSError` → erros de entrada/saída (ficheiros, discos, etc.).
-   `ImportError` → erro ao importar um módulo.
-   `AttributeError` → atributo ou método inexistente num objeto.
-   `IndentationError` → erro de indentação (espaços/tabs incorretos).

---

## 11. Exercícios - Exceções e Tratamento de Erros

### Exercício 1 - Leitura segura de inteiro · [BÁSICO]

Escreve um programa que:

-   pede um número inteiro ao utilizador;
-   usa `try`/`except` para:
    -   mostrar o quadrado do número, **se estiver tudo bem**;
    -   mostrar uma mensagem amigável **se o utilizador escrever algo inválido** (por exemplo, `abc`).

> Resolução:

```python
try:
    numero = int(input("Número inteiro: "))
    print("Número ao quadrado:", numero ** 2)
except ValueError:
    print("Isso não é um inteiro válido.")
```

---

### Exercício 2 - Repetir até ser válido · [BÁSICO]

Melhora o exercício anterior:

-   usa um ciclo `while True` para pedir um número inteiro;
-   se a conversão com `int` correr bem, sai do ciclo (`break`) e mostra o resultado;
-   se der `ValueError`, mostra uma mensagem e volta a pedir o número.

> Resolução:

```python
while True:
    try:
        numero = int(input("Número inteiro: "))
        break  # sai do ciclo se tudo correr bem
    except ValueError:
        print("Isso não é um inteiro válido. Tenta outra vez.")

print("Número ao quadrado:", numero ** 2)
```

---

### Exercício 3 - Divisão segura · [BÁSICO]

Escreve um programa que:

-   pede dois números (numerador e denominador);
-   tenta fazer a divisão;
-   trata separadamente:
    -   `ValueError` (se o utilizador escrever algo que não seja número),
    -   `ZeroDivisionError` (se o denominador for zero).

Mostra mensagens diferentes em cada caso.

> Resolução:

```python
try:
    numerador = float(input("Numerador: "))
    denominador = float(input("Denominador: "))
    resultado = numerador / denominador
    print("Resultado:", resultado)
except ValueError:
    print("Por favor escreve números válidos.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
```

---

### Exercício 4 - Leitura de ficheiro com mensagem amigável · [BÁSICO]

Escreve um programa que:

-   pede o nome de um ficheiro ao utilizador;
-   tenta abrir o ficheiro em modo leitura e mostrar o seu conteúdo;
-   se o ficheiro **não existir**, apanha `FileNotFoundError` e mostra uma mensagem clara (sem traceback).

Dica: liga com o que aprendeste em `07_ficheiros_texto_json_csv.md`.

> Resolução:

```python
nome_ficheiro = input("Nome do ficheiro: ")
try:
    with open(nome_ficheiro, "r", encoding="utf-8") as f:
        conteudo = f.read()
except FileNotFoundError:
    print("Não foi possível encontrar esse ficheiro.")
else:
    print("Conteúdo do ficheiro:")
    print(conteudo)
```

> Podemos também verificar se a extensão do ficheiro é `json`e se não for, lançar um `ValueError` com `raise`.
> Vamos usar o split para dividir o nome do ficheiro pelo ponto e verificar a última parte.:

```python
nome_ficheiro = input("Nome do ficheiro: ")
try:
    if nome_ficheiro.split('.')[-1] != 'json': # aqui usamos o índice -1 para obter a última parte após o ponto
        raise ValueError("O ficheiro tem de ser um .json")
    with open(nome_ficheiro, "r", encoding="utf-8") as f:
        conteudo = f.read()
except FileNotFoundError:
    print("Não foi possível encontrar esse ficheiro.")
except ValueError as ve:
    print("Erro:", ve)
else:
    print("Conteúdo do ficheiro:")
    print(conteudo)

```

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

> Resolução:

```python
linha = input("Escreve vários números separados por espaços: ")
partes = linha.split()
soma = 0

for p in partes:
    try:
        n = int(p)
        soma += n
    except ValueError:
        print(f"Ignorando valor inválido: {p}")
print("Soma dos números válidos:", soma)
```

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

> Resolução:

```python
import json

try:
    with open("aluno.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
except FileNotFoundError:
    print("Ficheiro aluno.json não encontrado.")
except json.JSONDecodeError:
    print("O conteúdo do ficheiro aluno.json é inválido.")
else:
    nome = dados["nome"]
    notas = dados["notas"]
    media = sum(notas) / len(notas) if notas else 0
    print(f"Aluno: {nome}")
    print(f"Média das notas: {media:.2f}")
```

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

> Resolução:

```python
while True:
    print("Menu:")
    print("1 - Dizer olá")
    print("2 - Mostrar a tabuada do 5")
    print("3 - Sair")
    try:
        opcao = int(input("Escolhe uma opção (1-3): "))
        if opcao == 1:
            print("Olá!")
        elif opcao == 2:
            print("Tabuada do 5:")
            for i in range(1, 11):
                print(f"5 x {i} = {5 * i}")
        elif opcao == 3:
            print("A sair...")
            break
        else:
            print("Opção inválida. Tenta outra vez.")
    except ValueError:
        print("Por favor escreve um número inteiro válido.")
```

---

### Exercício 8 (Desafio) - Calculadora básica com validação (usa \*args) · [DESAFIO]

Escreve uma função `calculadora(operacao, *numeros)` que:

-   recebe uma string `operacao` que pode ser `"soma"`, `"subtrai"`, `"multiplica"` ou `"divide"`;
-   recebe um número variável de argumentos `numeros` (pelo menos dois);
-   realiza a operação indicada em todos os números fornecidos;
-   usa `try`/`except` para tratar:
    -   `ValueError` se algum dos argumentos não for numérico;
    -   `ZeroDivisionError` se tentar dividir por zero (neste caso, devolve `None`);
    -   `TypeError` se a operação não for reconhecida (mostra uma mensagem clara).
    -   Cria um erro `ValueError` se forem fornecidos menos de dois números.

Exemplos de uso:

```python
print(calculadora("soma", 10, 5, 3))          # devolve 18
print(calculadora("subtrai", 10, 5, 3))       # devolve 2
print(calculadora("multiplica", 2, 3, 4))      # devolve 24
print(calculadora("divide", 10, 2, 0))         # devolve None (devido a divisão por zero)
print(calculadora("divide", 10, "a"))          # trata ValueError
print(calculadora("potencia", 2, 3))           # trata TypeError
print(calculadora("soma", 10))                  # trata ValueError (menos de dois números)
```

> Resolução:

```python
def calculadora(operacao, *numeros):
    if len(numeros) < 2:
        raise ValueError("Deves fornecer pelo menos dois números.")

    try:
        if operacao == "soma":
            return sum(numeros)
        elif operacao == "subtrai":
            resultado = numeros[0]
            for n in numeros[1:]:
                resultado -= n
            return resultado
        elif operacao == "multiplica":
            resultado = 1
            for n in numeros:
                resultado *= n
            return resultado
        elif operacao == "divide":
            resultado = numeros[0]
            for n in numeros[1:]:
                resultado /= n
            return resultado
        else:
            raise TypeError(f"Operação '{operacao}' não reconhecida.")
    except ValueError:
        print("Erro: todos os argumentos devem ser numéricos.")
    except ZeroDivisionError:
        print("Erro: divisão por zero detectada.")
    except TypeError as te:
        print(te)
        return None
```

---

### Exercício 9 (Desafio) - Estatísticas a partir de JSON · [DESAFIO]

Supondo um ficheiro `notas.json` com:

```json
{
    "alunos": [
        { "nome": "Ana", "notas": [14, 15, 12] },
        { "nome": "Bruno", "notas": [10, 9, 11] },
        { "nome": "Carla", "notas": [16, 18, 17] }
    ]
}
```

Escreve um programa que:

-   tenta ler o ficheiro `notas.json`;
-   se o ficheiro não existir, apanha `FileNotFoundError` e mostra uma mensagem;
-   se o conteúdo for inválido, apanha `json.JSONDecodeError` e mostra uma mensagem;
-   se tudo correr bem, calcula e mostra:
    -   a média de cada aluno;
    -   a média geral da turma;
    -   o nome do aluno com a maior média.

> Resolução:

```python
import json
try:
    with open("notas.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
except FileNotFoundError:
    print("Ficheiro notas.json não encontrado.")
except json.JSONDecodeError:
    print("O conteúdo do ficheiro notas.json é inválido.")
else:
    alunos = dados.get("alunos", [])
    if not alunos:
        print("Nenhum aluno encontrado.")
    else:
        soma_geral = 0
        total_notas = 0
        melhor_aluno = None
        melhor_media = -1

        for aluno in alunos:
            nome = aluno.get("nome", "Desconhecido")
            notas = aluno.get("notas", [])
            if notas:
                media = sum(notas) / len(notas)
                print(f"{nome}: Média = {media:.2f}")
                soma_geral += sum(notas)
                total_notas += len(notas)

                if media > melhor_media:
                    melhor_media = media
                    melhor_aluno = nome
            else:
                print(f"{nome}: Sem notas disponíveis.")

        if total_notas > 0:
            media_geral = soma_geral / total_notas
            print(f"Média geral da turma: {media_geral:.2f}")
            print(f"Melhor aluno: {melhor_aluno} com média {melhor_media:.2f}")
```

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

-   todas as entradas são guardadas em `diario.json`;
-   ao escolher “Escrever nova entrada”:
    -   pede a data (formato `YYYY-MM-DD`);
    -   pede o texto da entrada;
    -   guarda a entrada no ficheiro JSON (cria o ficheiro se não existir);
-   ao escolher “Ver entradas”:
    -   tenta ler o ficheiro `diario.json`;
    -   se o ficheiro não existir, mostra uma mensagem adequada;
    -   se o ficheiro existir, mostra todas as entradas com data e texto;
-   usa `try`/`except` para tratar erros de ficheiro e JSON inválido.

> Resolução:

```python
import json
import os # Para verificar se o ficheiro existe
DIARIO_FILE = "diario.json"

def carregar_diario():
    if not os.path.exists(DIARIO_FILE): # Verifica se o ficheiro existe
        return []
    try:
        with open(DIARIO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Erro: o ficheiro do diário está corrompido.")
        return []
def guardar_diario(entradas):
    with open(DIARIO_FILE, "w", encoding="utf-8") as f:
        json.dump(entradas, f, ensure_ascii=False, indent=4)
def escrever_entrada():
    data = input("Data (YYYY-MM-DD): ")
    texto = input("Texto da entrada: ")
    entradas = carregar_diario()
    entradas.append({"data": data, "texto": texto})
    guardar_diario(entradas)
    print("Entrada guardada.")
def ver_entradas():
    entradas = carregar_diario()
    if not entradas:
        print("Nenhuma entrada no diário.")
        return
    for entrada in entradas:
        print(f"{entrada['data']}: {entrada['texto']}")
def main():
    while True:
        print("Menu do Diário:")
        print("1 - Escrever nova entrada")
        print("2 - Ver entradas")
        print("3 - Sair")
        try:
            opcao = int(input("Escolhe uma opção (1-3): "))
            if opcao == 1:
                escrever_entrada()
            elif opcao == 2:
                ver_entradas()
            elif opcao == 3:
                print("A sair...")
                break
            else:
                print("Opção inválida. Tenta outra vez.")
        except ValueError:
            print("Por favor escreve um número inteiro válido.")
main()

---

## 10. Changelog

-   `2025-02-XX` · Criação inicial do ficheiro com introdução a exceções, leitura de mensagens de erro e `try`/`except` básico.
```
