# Python (10.º Ano) — 04 · Funções do Básico ao “Quase Avançado”

> **Objetivo deste ficheiro**  
> Perceber bem o que são funções em Python, como as definir e usar, e dar um primeiro contacto com ideias um bocadinho mais avançadas.

---

## 0. Guia para não te perderes

É aqui que muitos alunos começam a “desligar”, por isso vamos organizar assim:

-   Secções marcadas como **[ESSENCIAL]** → é o que precisas MESMO para testes e para programar no dia a dia.
-   Secções marcadas como **[EXTRA]** → são assuntos um pouco mais avançados; lê se estiveres confortável, caso contrário podes voltar mais tarde.

Se te sentires perdido:

1. Foca-te nas secções **[ESSENCIAL]**.
2. Faz os exemplos e **os exercícios** dessas partes.
3. Só depois, se der, explora o resto.

---

## 1. Porque usar funções? · [ESSENCIAL]

Antes de falarmos de sintaxe, pensa no problema:

-   Sem funções, tens um ficheiro `.py` enorme, com código repetido por todo o lado.
-   Se quiseres mudar a lógica, tens de ir a todos os sítios copiar/colar correções.
-   Fica difícil testar, difícil explicar, difícil manter.

Uma **função** é um “bloco de código com nome” que:

-   recebe dados de entrada (**parâmetros**),
-   faz alguma coisa (cálculos, decisões, etc.),
-   e normalmente devolve um resultado com `return`.

Vantagens:

-   **Evitar repetição**: em vez de copiares código, chamas a função várias vezes.
-   **Organizar o código**: cada função faz uma tarefa bem definida.
-   **Facilitar testes**: é mais fácil testar uma função de cada vez.

Pensa numa função como uma **máquina**:

-   metes valores na entrada,
-   ela faz o trabalho,
-   devolve um resultado pela saída.

---

## 2. Definir e chamar funções · [ESSENCIAL]

### 2.1. Sintaxe básica do `def`

```python
def nome_da_funcao(param1, param2):
    # corpo da função (bloco indentado)
    ...
    return resultado
```

-   `def` → palavra reservada para definir a função.
-   `nome_da_funcao` → deve explicar o que a função faz (em `snake_case`).
-   Dentro dos parênteses vão os parâmetros (podem ser zero ou mais).
-   O corpo está **indentado** (4 espaços).
-   `return` devolve o resultado e termina a função.

### 2.2. Exemplo 1 — função muito simples

```python
def ola_mundo():
    print("Olá, Mundo!")
```

Chamar a função:

```python
ola_mundo()   # executa o código da função
```

### 2.3. Exemplo 2 — soma de dois números

```python
def soma(a, b):
    resultado = a + b
    return resultado

x = soma(3, 5)      # x fica 8
print(x)
```

### 2.4. Exemplo 3 — saudação

```python
def saudacao(nome):
    texto = f"Olá, {nome}!"
    return texto

frase = saudacao("Ana")
print(frase)   # "Olá, Ana!"
```

---

## 3. `print` vs `return` · [ESSENCIAL]

Isto é um ponto onde muita gente se confunde.

-   `print(...)` → serve para **mostrar** algo no ecrã (apresentação).
-   `return ...` → serve para **devolver** um valor ao sítio onde a função foi chamada (lógica).

Uma função que **só faz `print`** é difícil de reutilizar noutras funções.  
Uma função que **devolve com `return`** pode ser usada em contas, condições, etc.

### 3.1. Mesmo exemplo, duas versões

Versão “preso ao ecrã”:

```python
def mostrar_soma(a, b):
    print(a + b)    # não devolve nada, só mostra
```

Versão reutilizável (melhor):

```python
def soma(a, b):
    return a + b

resultado = soma(3, 5)
print("Resultado =", resultado)    # agora decidimos aqui se mostramos ou não
```

Regra prática:

-   Dentro das funções mais “lógicas”, prefere usar `return`.
-   Deixa o `print` para a “camada” que fala com o utilizador.

---

## 4. Parâmetros e argumentos · [ESSENCIAL]

### 4.1. Parâmetros vs argumentos

-   **Parâmetros** → os “lugares” definidos na função:

    ```python
    def soma(a, b):  # a e b são parâmetros
        return a + b
    ```

-   **Argumentos** → os valores reais que passas quando chamas a função:

    ```python
    soma(3, 5)       # 3 e 5 são argumentos
    ```

### 4.2. Argumentos posicionais

A ordem importa:

```python
def potencia(base, expoente):
    return base ** expoente

print(potencia(2, 3))   # 2 ** 3 = 8
print(potencia(3, 2))   # 3 ** 2 = 9 (diferente!)
```

### 4.3. Argumentos nomeados (keywords)

Podes indicar explicitamente o nome:

```python
print(potencia(base=2, expoente=3))      # 8
print(potencia(expoente=3, base=2))      # 8 (ordem já não interessa)
```

Isto torna o código mais claro, especialmente quando há muitos parâmetros.

### 4.4. Valores por defeito

Permitem tornar certos parâmetros **opcionais**.

```python
def potencia(base, expoente=2):   # por defeito, expoente = 2
    return base ** expoente

print(potencia(3))            # 3 ** 2 = 9
print(potencia(2, 5))         # 2 ** 5 = 32
```

Outro exemplo (saudação com prefixo):

```python
def saudacao(nome, prefixo="Olá"):
    return f"{prefixo}, {nome}!"

print(saudacao("Ana"))                         # usa "Olá"
print(saudacao("Bruno", prefixo="Bem-vindo"))  # usa "Bem-vindo"
```

### 4.5. Boas práticas para nomes de funções

-   Funções → **verbos** em `snake_case`:
    -   `calcular_media`, `contar_vogais`, `obter_idade`.
-   Parâmetros → nomes claros que indiquem o que representam:
    -   `lista_numeros`, `nome_aluno`, `notas`.

---

## 5. `return` em detalhe · [ESSENCIAL]

### 5.1. Se não houver `return`.

Se uma função não tiver `return` explícito, devolve automaticamente `None`.

```python
def ola_mundo():
    print("Olá, Mundo!")

resultado = ola_mundo()
print(resultado)   # None
```

### 5.2. Devolver um valor

Já vimos vários exemplos:

```python
def quadrado(n):
    return n ** 2
```

### 5.3. Devolver vários valores (tuplos)

Não podemos devolver **dois** valores em separado, mas podemos devolver um **tuplo** com dois (ou mais) elementos.

Exemplo: quociente e resto de uma divisão inteira:

```python
def dividir(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto   # isto é um tuplo (quociente, resto)

q, r = dividir(17, 5)        # desempacotar
print("Quociente:", q)
print("Resto:", r)
```

### 5.4. Saída antecipada (casos especiais)

Podemos sair da função mais cedo com `return`.

```python
def safe_div(a, b):
    if b == 0:
        return None   # caso especial: não dá para dividir

    return a / b

print(safe_div(10, 2))   # 5.0
print(safe_div(10, 0))   # None
```

---

## 6. Scope (espaço de nomes) · [ESSENCIAL (noção básica)]

“Scope” é o **sítio onde uma variável “vive”**.

### 6.1. Variáveis locais

Variáveis criadas dentro da função são **locais**: só existem lá dentro.

```python
def saudacao(nome):
    mensagem = f"Olá, {nome}!"   # mensagem é local
    return mensagem

print(saudacao("Ana"))
# print(mensagem)   # ERRO: mensagem não existe aqui fora
```

### 6.2. Variáveis globais (cuidado!)

Variáveis definidas fora de qualquer função são globais.  
É **possível** alterá-las com a palavra `global`, mas não é boa prática abusar disto.

```python
total_global = 0

def acumular_no_global(valor):
    global total_global
    total_global += valor    # altera a variável global

acumular_no_global(5)
acumular_no_global(7)
print(total_global)          # 12
```

Regra prática:  
Prefere devolver valores com `return` e passá-los como argumentos a outras funções, em vez de andar a mexer em globais.

### 6.3. `nonlocal` (curiosidade) · [EXTRA]

Para funções **dentro de funções**:

```python
def cria_contador(inicio=0):
    contador = inicio

    def proximo():
        nonlocal contador   # usa a variável da função “de fora”
        contador += 1
        return contador

    return proximo

novo_id = cria_contador(100)
print(novo_id())   # 101
print(novo_id())   # 102
```

Isto chama-se uma **closure**; é útil, mas não é essencial no 10.º ano.

---

## 7. Mutabilidade e passagem de argumentos · [ESSENCIAL]

Quando passamos uma variável a uma função, o comportamento depende do tipo:

-   Tipos **imutáveis** → `int`, `float`, `str`, `tuple`, etc.
    -   Não podem ser alterados “por dentro”.
-   Tipos **mutáveis** → `list`, `dict`, `set`, etc.
    -   Podem ser alterados por métodos, como `append`, `pop`, etc.

### 7.1. Exemplo com tipos imutáveis

```python
def incrementa_numero(n):
    n = n + 1
    return n

x = 10
y = incrementa_numero(x)
print("x =", x)   # 10
print("y =", y)   # 11
```

A função não altera o valor de `x` fora da função.

### 7.2. Exemplo com listas (mutáveis)

```python
def adiciona_elemento(lista, elem):
    lista.append(elem)   # altera a lista recebida (mutação)

numeros = [1, 2]
adiciona_elemento(numeros, 3)
print(numeros)   # [1, 2, 3]
```

Aqui, a função altera a lista original, porque está a mexer no **objeto mutável** a que a variável aponta.

### 7.3. Perigo dos valores por defeito mutáveis

Exemplo **errado**:

```python
def acumulador_errado(valor, acc=[]):
    acc.append(valor)
    return acc

print(acumulador_errado(1))   # [1]
print(acumulador_errado(2))   # [1, 2]  (continuou a lista anterior!)
print(acumulador_errado(3))   # [1, 2, 3]
```

A lista `[]` é criada **uma vez** e reaproveitada em todas as chamadas sem `acc`.

Forma **correta**:

```python
def acumulador_correto(valor, acc=None):
    if acc is None:
        acc = []      # nova lista
    acc.append(valor)
    return acc

print(acumulador_correto(1))           # [1]
print(acumulador_correto(2))           # [2]
print(acumulador_correto(3, [10]))     # [10, 3]
```

Regra prática:  
Nunca uses listas ou dicionários como valores por defeito. Usa `None` e cria a lista dentro da função.

---

## 8. Funções de ordem superior e `lambda` · [EXTRA]

> Lê esta secção quando já te sentires seguro com as partes essenciais.

Em Python, funções são “cidadãos de 1.ª classe”:

-   podem ser guardadas em variáveis,
-   podem ser passadas como argumentos,
-   podem ser devolvidas por outras funções.

### 8.1. Função que recebe outra função

```python
def aplicar(func, valor):
    return func(valor)

def dobro(x):
    return 2 * x

print(aplicar(dobro, 7))   # 14
```

### 8.2. `lambda` (funções anónimas)

Uma `lambda` é uma forma curta de escrever funções simples:

```python
dobro_lambda = lambda x: x * 2
print(dobro_lambda(5))   # 10

print(aplicar(lambda x: x * 3, 4))   # 12
```

Usa com moderação; para funções mais complexas é preferível usar `def`.

### 8.3. `map`, `filter`, `sorted(key=...)` vs compreensões

```python
dados = [1, 2, 3, 4, 5]

# map
dobros = list(map(lambda x: x * 2, dados))      # [2, 4, 6, 8, 10]

# filter
pares = list(filter(lambda x: x % 2 == 0, dados))  # [2, 4]

# sorted com key
tuplos = [("a", 3), ("b", 1), ("c", 2)]
ordenado = sorted(tuplos, key=lambda t: t[1])   # ordena pelo 2.º elemento
```

Normalmente, para listas simples é mais legível usar **compreensões**:

```python
dobros_comp = [x * 2 for x in dados]
pares_comp = [x for x in dados if x % 2 == 0]
```

---

## 9. `*args` e `**kwargs` · [EXTRA]

Servem para criar funções com número variável de argumentos.

### 9.1. `*args` — vários argumentos posicionais

```python
def media(*nums):
    if not nums:
        return 0.0
    return sum(nums) / len(nums)

print(media(10, 12, 14))   # 12.0
print(media())             # 0.0
```

### 9.2. `**kwargs` — vários argumentos nomeados

```python
def configurar(**opcoes):
    return opcoes

cfg = configurar(debug=True, porta=8000)
print(cfg)   # {'debug': True, 'porta': 8000}
```

Desempacotar ao chamar:

```python
valores = [10, 20, 30]
opcoes = {"debug": False, "porta": 5000}

print(media(*valores))         # 20.0
print(configurar(**opcoes))    # {'debug': False, 'porta': 5000}
```

---

## 10. Docstrings e anotações de tipo · [EXTRA mas muito útil]

### 10.1. Docstrings

Uma **docstring** é uma string logo a seguir ao `def` que explica o que a função faz.

```python
def soma(a, b):
    """Devolve a soma de a e b."""
    return a + b
```

No REPL, podes usar `help(soma)` para ver a docstring.

### 10.2. Exemplo mais completo com tipos

```python
from typing import Sequence

def normalizar_textos(textos: Sequence[str]) -> list[str]:
    """
    Normaliza uma sequência de textos:
    - remove espaços nas pontas
    - converte para minúsculas
    - ignora strings vazias após trim

    :param textos: Sequência de strings de entrada.
    :return: Lista de strings normalizadas e não vazias.
    """
    resultado: list[str] = []
    for t in textos:
        t_norm = t.strip().lower()
        if t_norm:
            resultado.append(t_norm)
    return resultado
```

As **anotações de tipo** (`-> list[str]`, `textos: Sequence[str]`, etc.) não são obrigatórias, mas:

-   tornam o código mais legível,
-   ajudam o editor (VS Code, por exemplo) a dar melhores sugestões,
-   ajudam a apanhar certos erros.

---

## 11. Recursão · [EXTRA / AVANÇADO]

> Só deves ler esta secção quando já estiveres confortável com `while` e `for`.

Uma função é **recursiva** quando chama a si própria.

Estrutura típica:

-   **caso base** → quando parar (evitar recursão infinita),
-   **passo recursivo** → a função chama-se com um problema mais pequeno.

### 11.1. Exemplo: fatorial

O fatorial de `n` (`n!`) é:

-   `0! = 1`
-   `n! = n * (n-1)!` para `n > 0`

```python
def fatorial(n):
    if n < 0:
        raise ValueError("n deve ser >= 0")
    if n in (0, 1):   # caso base
        return 1
    return n * fatorial(n - 1)  # passo recursivo
```

### 11.2. Exemplo: lista decrescente

```python
def conta_decrescente(n):
    if n <= 1:
        return [1]
    return [n] + conta_decrescente(n - 1)

print(conta_decrescente(4))   # [4, 3, 2, 1]
```

Avisos:

-   Python tem um limite para profundidade de recursão; para contagens grandes, usa `while` ou `for`.
-   Recursão é útil em alguns problemas (árvores, divisão de problemas), mas no 10.º ano é mais importante saber bem `while` e `for`.

---

## 12. Boas práticas e pequenos testes · [ESSENCIAL (mentalidade)]

Algumas regras que te vão ajudar:

-   Funções **curtas** e com **uma responsabilidade** principal.
-   Nomes claros para funções e parâmetros.
-   Preferir `return` a `print` em funções de lógica.
-   Evitar alterar variáveis globais; passar valores como argumentos e devolver resultados.
-   Evitar defaults mutáveis (usar `None`).
-   Escrever pequenos **testes** com `assert`.

### 12.1. Bloco `if __name__ == "__main__":`

Costuma colocar-se no fim do ficheiro:

```python
def soma(a, b):
    return a + b

if __name__ == "__main__":
    # testes rápidos (só correm se este ficheiro for o "principal")
    assert soma(2, 3) == 5
    print("Tudo OK!")
```

-   Se importares este ficheiro noutro, o código dentro deste `if` não corre automaticamente.
-   É um bom sítio para pôr testes e demonstrações.

---

## 13. Exercícios (Funções do básico ao avançado)

> Começa pelos primeiros.  
> Os últimos podem ser um pouco mais desafiantes, especialmente se envolverem dicionários ou recursão.

### Exercício 1 — `ola_mundo` (a máquina mais simples)

Cria uma função `ola_mundo` que não recebe parâmetros e:

-   mostra no ecrã `"Olá, Mundo!"`.

Depois, chama essa função pelo menos duas vezes.

---

### Exercício 2 — Soma de dois números

Cria uma função `soma(a, b)` que:

-   recebe dois números como parâmetros,
-   devolve a soma,
-   não faz `print` dentro da função.

No programa principal, pede dois números ao utilizador, chama a função e mostra o resultado.

---

### Exercício 3 — Contar letras de um nome

Cria uma função `contar_letras(nome)` que:

-   recebe uma string `nome`,
-   devolve o número de letras (usa `len()`).

No programa principal, pede o nome ao utilizador e mostra:

```text
O nome <nome> tem <n> letras.
```

---

### Exercício 4 — Contar pares e ímpares numa lista

Cria uma função `contar_pares_impares(lista_numeros)` que:

-   recebe uma lista de inteiros,
-   devolve **dois** valores: número de pares e número de ímpares.

No programa principal, cria uma lista de números (por exemplo, de 1 a 10) e mostra:

```text
Números pares: X, números ímpares: Y
```

---

### Exercício 5 — Média de uma lista de números

Cria uma função `calcular_media(lista_numeros)` que:

-   recebe uma lista de números,
-   devolve a média,
-   se a lista estiver vazia, devolve 0 (para evitar divisão por zero).

Testa a função com diferentes listas (incluindo uma lista vazia).

---

### Exercício 6 — Somatório de 1 até `n`

Cria uma função `somatorio(n)` que:

-   recebe um inteiro positivo `n`,
-   devolve `1 + 2 + ... + n`.

No programa principal, pede `n` ao utilizador, verifica se é positivo e:

-   se for, mostra o somatório;
-   se não, mostra uma mensagem de erro.

---

### Exercício 7 — String mais longa

Cria uma função `string_mais_longa(lista_strings)` que:

-   recebe uma lista de strings,
-   devolve a string com maior comprimento,
-   se a lista estiver vazia, devolve `None`.

Testa a função com várias listas (por exemplo, nomes de cidades, jogadores, etc.).

---

### Exercício 8 — Contar alunos por turma (dicionário simples + função)

Cria um dicionário `turmas` em que:

-   as chaves são nomes de turmas (ex.: `"10A"`, `"10B"`),
-   os valores são listas de nomes de alunos.

Depois, cria uma função `contar_alunos_por_turma(turmas)` que:

-   recebe este dicionário,
-   devolve um **novo dicionário** em que:
    -   as chaves são as mesmas turmas,
    -   os valores são o número de alunos em cada turma.

No programa principal, mostra algo do género:

```text
Turma 10A: 3 alunos
Turma 10B: 4 alunos
```

---

### Exercício 9 — Encontrar a pessoa mais velha

Cria uma função `mais_velho(pessoas)` que recebe um dicionário do tipo:

```python
pessoas = {
    "Ana": 16,
    "Bruno": 17,
    "Carla": 15
}
```

A função deve:

-   devolver o nome da pessoa mais velha,
-   se houver mais do que uma pessoa com a idade máxima, podes devolver uma delas (não faz mal).

Testa a função com diferentes dicionários.

---

### Exercício 10 — Média por aluno (função + dicionário aninhado)

Usa um dicionário semelhante a este:

```python
turma = {
    "alunos": [
        {"nome": "Ana", "notas": {"Matemática": 18, "Português": 16}},
        {"nome": "Bruno", "notas": {"Matemática": 14, "Português": 15}},
        {"nome": "Carla", "notas": {"Matemática": 12, "Português": 14}}
    ]
}
```

Cria uma função `media_aluno(aluno)` que:

-   recebe um dicionário com `"nome"` e `"notas"`,
-   devolve a média das notas desse aluno.

Depois, no programa principal, percorre a lista de alunos em `turma["alunos"]` e mostra:

```text
Ana -> média: X
Bruno -> média: Y
Carla -> média: Z
```

---

### Exercício 11 (Desafio) — Função com `*args`

Cria uma função `produto(*nums)` que:

-   recebe 0 ou mais números,
-   devolve o produto de todos (multiplicação),
-   se não receber nenhum número, devolve 1 (identidade da multiplicação).

Testa com:

-   `produto(2, 3)` → 6
-   `produto(2, 3, 4)` → 24
-   `produto()` → 1

---

### Exercício 12 (Desafio avançado) — Recursão simples

Cria uma função recursiva `conta_decrescente(n)` que:

-   recebe um inteiro `n >= 1`,
-   devolve uma lista `[n, n-1, ..., 1]`.

Exemplo:

```python
conta_decrescente(4)  # [4, 3, 2, 1]
```

Depois, compara com uma versão **não recursiva** usando `while` ou `for`.  
Reflete qual das versões achas mais fácil de ler.

---

## 14. Changelog

> Registo de alterações importantes a este ficheiro.

-   **2025-11-17 · v1.0**
    -   Criação inicial do documento.
    -   Secções essenciais: motivação para funções, definição e chamada, `print` vs `return`, parâmetros/argumentos, `return`, scope básico, mutabilidade, boas práticas e testes.
    -   Secções extra: funções de ordem superior, `lambda`, `*args`/`**kwargs`, docstrings e tipos, recursão.
    -   Adicionados 12 exercícios graduais (dos básicos aos desafios com recursão e estruturas aninhadas).
