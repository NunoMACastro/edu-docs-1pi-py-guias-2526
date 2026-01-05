# Python (10.º Ano) - 09 · Módulos e Organização de Projetos

> **Objetivo deste ficheiro**  
> Ensinar como organizar código em ficheiros diferentes, reutilizar funções com `import`, e criar projetos simples mais limpos e fáceis de manter.

---

## 1) O que é um módulo e porquê usar?

Em Python, **um módulo é um ficheiro `.py`** com código. Esse código pode ter:

-   funções;
-   variáveis;
-   constantes;
-   pequenas listas/dicionários úteis;
-   até código de teste.

A ideia é **separar responsabilidades**. Em vez de ter tudo num único ficheiro:

-   um ficheiro pode tratar **cálculos**;
-   outro pode tratar **leitura/escrita de ficheiros**;
-   outro pode ter o **programa principal** (menu, `input`, `print`).

Vantagens:

-   o código fica **mais organizado**;
-   é mais fácil **reutilizar funções**;
-   é mais simples **corrigir erros**;
-   consegues **testar** partes isoladas.

---

## 2) Como criar um módulo

### Exemplo simples

Cria um ficheiro chamado `math_utils.py`:

```python
# math_utils.py

def soma(a, b):
    return a + b

def media(valores):
    if len(valores) == 0:
        return 0
    return sum(valores) / len(valores)
```

Agora, noutro ficheiro (por exemplo `main.py`), podes usar essas funções:

```python
# main.py
import math_utils

print(math_utils.soma(3, 5))
print(math_utils.media([10, 12, 14]))
```

Observa:

-   o `import math_utils` lê o ficheiro `math_utils.py`;
-   para usar funções, escreves `math_utils.nome_da_funcao`.

---

## 3) Diferentes formas de import

### 3.1 `import modulo`

É a forma mais segura e clara:

```python
import math_utils

total = math_utils.soma(10, 20)
```

Vantagem: sabes sempre **de onde vem** cada função.

---

### 3.2 `from modulo import funcao`

Importa apenas o que queres:

```python
from math_utils import soma

print(soma(10, 20))
```

Vantagem: código mais curto.  
Desvantagem: se houver muitas funções com o mesmo nome, pode causar confusão.

---

### 3.3 `from modulo import *` (evitar)

```python
from math_utils import *
```

Isto coloca **todas** as funções no teu ficheiro. É rápido, mas perigoso:

-   pode esconder nomes iguais;
-   fica menos claro o que foi importado.

Regra prática: **evita** `import *` em projetos reais.

---

### 3.4 `import modulo as apelido`

```python
import math_utils as mu

print(mu.soma(5, 7))
```

Útil para encurtar nomes longos.  
Exemplo real: `import random as rd`.

---

### 3.5 Quando usar cada forma?

| Forma de import        | Quando usar                                       |
| ---------------------- | ------------------------------------------------- |
| `import modulo`        | Projetos maiores, para clareza.                   |
| `from modulo import f` | Quando usas poucas funções e queres código curto. |
| `import modulo as a`   | Módulos com nomes longos ou usados muitas vezes.  |
| `from modulo import *` | Evitar, a menos que seja para testes rápidos.     |

---

## 4) O que acontece quando um módulo é importado?

Quando usas `import`, o Python **executa o ficheiro uma vez**, de cima para baixo.  
Por isso, se o módulo tiver `print` ou código solto, isso vai correr no import.

Exemplo:

```python
# exemplo_modulo.py
print("A correr no import...")

def mensagem():
    print("Olá!")
```

Se fizeres:

```python
import exemplo_modulo
```

Vai aparecer no ecrã:

```
A correr no import...
```

**Conclusão:** deixa só funções/constantes no módulo.  
Se precisares de testes, usa `if __name__ == "__main__":`.

---

## 5) `if __name__ == "__main__":`

Cada ficheiro Python tem uma variável especial chamada `__name__`.

-   Quando o ficheiro é executado diretamente, `__name__` é `"__main__"`.
-   Quando o ficheiro é importado, `__name__` tem o nome do módulo.

Isto permite colocar **testes simples** no fim do módulo, sem que eles corram no `import`.

Exemplo:

```python
# math_utils.py

def soma(a, b):
    return a + b

if __name__ == "__main__":
    # Testes rápidos
    print(soma(2, 3))
```

Quando importares `math_utils`, o teste **não** corre.  
Quando executares `python math_utils.py`, o teste **corre**.

---

## 6) Criar módulos próprios para um projeto

### Exemplo de projeto simples

```
projeto_turma/
├── main.py
├── alunos.py
└── ficheiros.py
```

#### `alunos.py`

```python
def calcula_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def tem_negativas(notas):
    for nota in notas:
        if nota < 10:
            return True
    return False
```

#### `ficheiros.py`

```python
import json

def guardar_alunos(alunos, nome_ficheiro):
    with open(nome_ficheiro, "w", encoding="utf-8") as f:
        json.dump(alunos, f, ensure_ascii=False, indent=4)

def ler_alunos(nome_ficheiro):
    with open(nome_ficheiro, "r", encoding="utf-8") as f:
        return json.load(f)
```

#### `main.py`

```python
from alunos import calcula_media, tem_negativas
from ficheiros import guardar_alunos, ler_alunos

def mostrar_relatorio(alunos):
    for aluno in alunos:
        notas = aluno["notas"]
        media = calcula_media(notas)
        negativas = tem_negativas(notas)
        estado = "OK" if not negativas else "Com negativas"
        print(f"{aluno['nome']} - media: {media:.1f} - {estado}")

alunos = [
    {"nome": "Ana", "notas": [12, 15, 10]},
    {"nome": "Bruno", "notas": [9, 8, 10]},
]

mostrar_relatorio(alunos)
guardar_alunos(alunos, "alunos.json")
```

Notas pedagógicas:

-   `main.py` só tem **input/print** e fluxo principal.
-   `alunos.py` tem **logica** (funções de calculo).
-   `ficheiros.py` tem **I/O**.

---

### 6.1) Organização de pastas

Para projetos maiores, podes organizar módulos em pastas:

```projeto_grande/
├── main.py
├── utils/
│   ├── __init__.py
│   ├── alunos.py
│   └── ficheiros.py
└── data/
    └── alunos.json
```

Depois, importas com:

```python
from utils.alunos import calcula_media
```

Deves sempre ser consistente na organização e coerente com os nomes.

---

## 7) Boas praticas ao criar módulos

-   escolhe nomes claros e simples (`alunos.py`, `ficheiros.py`, `utils.py`);
-   evita letras maiusculas e espaços;
-   não escrevas código solto que execute automaticamente;
-   coloca testes simples no `if __name__ == "__main__":`;
-   separa **logica** de **I/O**.

---

## 8) Bibliotecas da linguagem (módulos prontos)

Python vem com muitas bibliotecas. Alguns exemplos uteis:

-   `random` → números aleatorios;
-   `math` → funções matematicas;
-   `datetime` → datas e horas;
-   `os` e `os.path` → caminhos e pastas.

Exemplo rápido com `random`:

```python
import random

numero = random.randint(1, 10)
print(numero)
```

---

## 9) Exercícios

### Exercício 1 - Primeiro módulo

1. Cria um ficheiro `mensagens.py` com duas funções:
    - `ola(nome)` que devolve `"Olá, <nome>!"`;
    - `adeus(nome)` que devolve `"Até logo, <nome>!"`.
2. Cria um ficheiro `main.py` que importa o módulo e usa as duas funções.

---

### Exercício 2 - Módulo de operações

Cria um ficheiro `operacoes.py` com:

-   `soma(a, b)`
-   `subtrai(a, b)`
-   `multiplica(a, b)`
-   `divide(a, b)` (se `b == 0`, devolve `None`)

Depois cria `main.py` para testar cada função.

---

### Exercício 3 - Separar lógica e I/O

1. Cria um módulo `texto.py` com uma função `conta_vogais(texto)`.
2. No `main.py`, pede uma frase ao utilizador e mostra quantas vogais existem.

---

### Exercício 4 - Projeto com dois módulos

Cria um pequeno projeto:

-   `alunos.py` com funções para calcular media e contar negativas;
-   `main.py` com uma lista de alunos e a impressao do relatorio.

---

### Exercício 5 - Módulo de ficheiros JSON

1. Cria `dados.py` com funções `guardar(alunos, ficheiro)` e `ler(ficheiro)`.
2. No `main.py`, guarda uma lista de alunos e depois le novamente.

---

### Exercício 6 - Import com `as`

1. Cria um módulo `numeros.py` com função `dobros(lista)` que devolve nova lista.
2. Importa com um apelido: `import numeros as n`.
3. Usa `n.dobros(...)`.

---

### Exercício 7 - `__main__`

Num módulo chamado `teste_modulo.py`:

-   cria uma função `quadrado(n)`;
-   no fim, adiciona um bloco `if __name__ == "__main__":` com testes.

Depois:

-   executa `python teste_modulo.py` e confirma que os testes correm;
-   cria `main.py` que importa `teste_modulo` e usa `quadrado` sem correr os testes.

---

### Exercício 8 - Módulo com constantes

1. Cria `config.py` com:
    - `ESCOLA = "EPM"`
    - `ANO = 2025`
2. No `main.py`, imprime uma frase a usar essas constantes.

---

### Exercício 9 - Módulo com listas/dicionarios

Cria `dados_alunos.py` com uma lista de alunos e notas.  
No `main.py`, importa essa lista e calcula a media geral.

---

### Exercício 10 - Mini projeto organizado

Cria um projeto com 3 ficheiros:

-   `menu.py` (mostra opcoes e valida escolha);
-   `logica.py` (funções que tratam tarefas);
-   `main.py` (junta tudo e executa).

Objetivo: um mini gestor de tarefas simples (adicionar, listar, remover).

---

## 10) Changelog

-   `2025-02-XX` · Criacao inicial do ficheiro com introducao a modulos, imports e organizacao de projetos.
