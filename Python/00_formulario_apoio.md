# Formulário de Apoio · Python (10.º Ano)

> Ficha de consulta rápida para testes.

---

## 1) Entrada/Saída e Conversões

```python
# Ler texto (str)
s = input("Texto: ").strip()

# Converter para número
n_int = int(input("Inteiro: ").strip())
n_float = float(input("Real: ").strip())

# Normalizar texto
t_lower = s.lower()
t_upper = s.upper()

# f-string
msg = f"{s} -> {n_int} / {n_float:.2f}"
```

-   `type(valor)` para confirmar o tipo.
-   `bool(...)` interpreta `0`, `""`, `[]`, `{}`, `None` como `False`.

---

## 2) Operadores essenciais

-   **Aritméticos**: `+ - * / // % **`
-   **Comparação**: `== != > >= < <=`
-   **Lógicos**: `and`, `or`, `not`
-   **Pertinência**: `item in seq`, `item not in seq`
-   **Identidade**: `is`, `is not` (especialmente com `None`)
-   **Atribuições compostas**: `+=`, `-=`, `*=`, ...

Lembra-te de encadear comparações: `1 < x <= 10`.

---

## 3) Condicionais (`if / elif / else`)

```python
if condicao_principal:
    ...
elif outra_condicao:
    ...
else:
    ...

# Intervalos
if 5 <= nota <= 15:
    ...

# Ternário
status = "maior" if idade >= 18 else "menor"
```

Cuida da indentação (4 espaços).

---

## 4) Ciclo `for` e `range`

```python
# range(inicio_inclusivo, fim_exclusivo, passo)
for i in range(0, 5):
    ...  # 0,1,2,3,4

for par in range(2, 11, 2):
    ...  # 2,4,6,8,10

for item in sequencia:
    ...  # strings, listas, etc.
```

Útil para somatórios, contagens, percorrer coleções.

---

## 5) Ciclo `while` e validação

```python
valor = int(input("0-20: "))
while valor < 0 or valor > 20:
    print("Inválido.")
    valor = int(input("0-20: "))
```

-   Ideal para repetir até uma condição deixar de ser verdadeira.
-   Controla variáveis de estado para evitar ciclos infinitos.

---

## 6) Listas (criação e métodos)

```python
nums = [10, 20, 30]
nums.append(40)
nums.insert(1, 15)
ultimo = nums.pop()      # remove final
nums.remove(15)          # primeira ocorrência
nums.sort()              # altera lista
ordenada = sorted(nums)  # cópia ordenada
```

-   Índices positivos e negativos (`lista[-1]`).
-   Funções úteis: `len`, `sum`, `min`, `max`.
-   Padrões: acumulação, filtragem, transformação, procurar mínimo/máximo manualmente.

---

## 7) Dicionários

```python
pessoa = {"nome": "Ana", "idade": 16}
pessoa["cidade"] = "Lisboa"
idade = pessoa.get("idade", 0)
for chave, valor in pessoa.items():
    ...
```

-   Chaves normalmente `str`, valores de qualquer tipo.
-   Métodos: `keys`, `values`, `items`, `pop`.
-   Uso de `in` verifica chaves.

---

## 8) Estruturas aninhadas e padrões (listas/dicionários)

-   Lista de listas (matriz): `matriz[linha][coluna]`.
-   Dicionário de listas (turma → alunos).
-   Dicionário de dicionários (aluno → disciplina → nota).
-   Lista de dicionários (coleções de registos).

Padrões frequentes:

-   Ciclos aninhados para percorrer matrizes e coleções complexas.
-   Contagens condicionais (negativas, aprovados, etc.).
-   Procura de elementos por nome/título ignorando maiúsculas (`valor.lower()`).

---

## 9) Funções (`def`, parâmetros, `return`)

```python
def nome_funcao(param1, param2=valor):
    if condicao_especial:
        return ...
    resultado = param1 + param2
    return resultado

# Chamada
valor = nome_funcao(arg1, param2=arg2)
```

-   Prefere `return` para reutilizar resultados.
-   Pode devolver múltiplos valores através de tuplos: `return quociente, resto`.
-   Parâmetros: posicionais, nomeados, valores por defeito.

---

## 10) Funções avançadas (conceitos essenciais)

-   `*args` e `**kwargs` para argumentos variáveis.
-   Atenção à mutabilidade: alterar listas/dicionários passados por referência; evita valores por defeito mutáveis (usa `None` + inicialização interna).
-   `lambda` e funções de ordem superior (`map`, `filter`, `sorted(key=...)`) aparecem como curiosidade; aplica somente se confortável.
-   Scope: variáveis locais vs globais (`global`, `nonlocal` apenas quando indispensável).

---

## 11) Slicing e List Comprehensions

```python
seq = [0, 1, 2, 3, 4, 5]
fat1 = seq[1:4]      # índices 1..3
fat2 = seq[:3]       # início até índice 2
fat3 = seq[::2]      # passo 2
invertida = seq[::-1]

dobros = [x * 2 for x in seq]
pares = [x for x in seq if x % 2 == 0]
rotulo = ["par" if x % 2 == 0 else "ímpar" for x in seq]
```

-   Também funciona com strings (`texto[a:b]`).
-   Comprehensions substituem ciclos simples de construção de listas; evita efeitos secundários dentro delas.

---

## 12) Ficheiros de texto (`.txt`)

```python
# Escrever
with open("dados.txt", "w", encoding="utf-8") as f:
    f.write("linha 1\n")

# Ler linha a linha
with open("dados.txt", "r", encoding="utf-8") as f:
    for linha in f:
        conteudo = linha.rstrip("\n")
        ...
```

-   Modos: `"r"`, `"w"`, `"a"`.
-   `with` garante fecho automático do ficheiro.

---

## 13) JSON (`json.dump` / `json.load`)

```python
import json

dados = {"nome": "Ana", "idades": [16, 17]}
with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

with open("dados.json", "r", encoding="utf-8") as f:
    info = json.load(f)
```

-   Estruturas típicas: listas de dicionários, dicionário de listas.
-   Mantém separação entre lógica (funções que tratam `info`) e I/O (funções que leem/escrevem).

---

## 14) CSV “manual”

```python
registos = [
    {"nome": "Ana", "idade": 16, "nota": 15},
    ...
]

with open("alunos.csv", "w", encoding="utf-8") as f:
    f.write("nome;idade;nota\n")
    for reg in registos:
        linha = f"{reg['nome']};{reg['idade']};{reg['nota']}\n"
        f.write(linha)

with open("alunos.csv", "r", encoding="utf-8") as f:
    cabecalho = f.readline()
    for linha in f:
        nome, idade, nota = linha.strip().split(";")
        idade = int(idade)
        nota = int(nota)
        ...
```

-   Atenção à conversão de tipos após `split`.
-   `newline=""` recomendado quando usares `csv` module (opcional para esta ficha).

---

## 15) Planeamento + testes rápidos (revisão `00`)

-   Identifica **entradas**, **processamento** e **saídas** antes de escrever código.
-   Divide problemas em funções pequenas (lógica vs interface).
-   Usa padrões aprendidos (acumulação, contagem, filtragem, transformação).
-   Valida dados antes de guardar ou escrever em ficheiros.
-   Faz testes rápidos com `assert` ou `print` temporários para confirmar cada parte.
-   Mantém registos (JSON/CSV) atualizados e consistentes ao longo da execução.

Boa preparação!
