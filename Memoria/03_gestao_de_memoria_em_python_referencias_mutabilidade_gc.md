# Memória (10.º Ano) - 03 · Gestão de Memória em Python: Referências, Mutabilidade e Garbage Collection

> **Objetivo deste ficheiro**  
> Compreender, de forma realmente clara, como Python gere memória: o que é uma referência, o que muda entre objetos mutáveis e imutáveis, e como funciona o Garbage Collector.

---

**Pré-requisitos:** [`04_heap_stack_frames_e_execucao_python.md`](04_heap_stack_frames_e_execucao_python.md)

## Índice

- [1. Ideia principal: Python gere memória automaticamente](#1-ideia-principal-python-gere-memória-automaticamente)
- [2. Variável não é "caixa de valor" em Python](#2-variável-não-é-caixa-de-valor-em-python)
- [3. Referências na prática](#3-referências-na-prática)
- [4. Mutável vs imutável](#4-mutável-vs-imutável)
- [5. Cópia, alias e efeitos laterais](#5-cópia-alias-e-efeitos-laterais)
- [6. Contagem de referências](#6-contagem-de-referências)
- [7. Garbage Collection e ciclos](#7-garbage-collection-e-ciclos)
- [8. Memory leaks: o que é e como evitar](#8-memory-leaks-o-que-é-e-como-evitar)
- [9. Boas práticas para alunos](#9-boas-práticas-para-alunos)
- [10. Resumo final](#10-resumo-final)
- [11. Changelog](#11-changelog)

---

## 1. Ideia principal: Python gere memória automaticamente

Em linguagens como C, o programador costuma gerir memória de forma manual (alocar/libertar).  
Em Python, a gestão é automática na maioria dos casos.

Isto significa:

- quando precisas de objetos, Python cria-os;
- quando objetos deixam de ser necessários, Python remove-os.

Essa remoção automática acontece através de mecanismos como:

- contagem de referências;
- garbage collection (incluindo deteção de ciclos).

---

## 2. O que é, na realidade uma variável em Python?

Em Python, uma variável é **um nome que aponta para um objeto na memória**.
Pensa num "rótulo" que referencia um objeto. Exemplo: `python x = 10 ` Aqui, `x` é um nome que aponta para o objeto inteiro `10` na memória.

### Consequência importante

Quando fazes:

```python
y = x
```

`y` não cria obrigatoriamente um novo objeto com o mesmo conteúdo.  
Na prática inicial, `y` passa a apontar para o mesmo objeto que `x`.

---

## 3. Referências na prática

Podemos observar referências com `id()`:

```python
x = [1, 2, 3]
y = x

print(id(x))
print(id(y))
```

Se os `id` forem iguais, significa que `x` e `y` referem o mesmo objeto.

### Igualdade (`==`) vs identidade (`is`)

Este ponto evita muitos erros:

- `==` compara conteúdo/valor lógico;
- `is` compara identidade (se é exatamente o mesmo objeto).

Exemplo:

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True (conteúdo igual)
print(a is b)  # False (objetos diferentes)
```

Usa `is` principalmente para `None`.

---

## 4. Mutável vs imutável

Este é um dos conceitos mais importantes em Python.

### Imutáveis

Objetos imutáveis **não podem ser alterados no local** depois de criados.

Exemplos típicos:

- `int`
- `float`
- `str`
- `tuple`
- `bool`
- `bytes`

Se "alterares" um imutável, Python cria novo objeto.

```python
x = 10
y = x
y = 20

print(x)  # 10
print(y)  # 20
```

### Mutáveis

Objetos mutáveis **podem ser alterados no mesmo local de memória**.

Exemplos típicos:

- `list`
- `dict`
- `set`
- objetos de classes personalizadas (na maioria dos casos)

```python
a = [1, 2, 3]
b = a
b.append(4)

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
```

Porquê? Porque `a` e `b` apontam para a mesma lista mutável.

---

## 5. Cópia, alias e efeitos laterais

### Alias

Quando duas variáveis apontam para o mesmo objeto, tens um alias.

Isso é útil, mas pode causar surpresas.

### Cópia superficial (`copy`)

```python
import copy

lista1 = [[1, 2], [3, 4]]
lista2 = copy.copy(lista1)
```

- Cria nova lista externa;
- elementos internos ainda podem ser referências partilhadas.

### Cópia profunda (`deepcopy`)

```python
import copy

lista1 = [[1, 2], [3, 4]]
lista2 = copy.deepcopy(lista1)
```

- Cria cópia completa, incluindo objetos internos;
- alterações em `lista2` não afetam `lista1`.

---

## 6. Contagem de referências

Python mantém uma contagem de quantas referências apontam para cada objeto.

Ideia simplificada:

- se o objeto tem referências ativas, continua em memória;
- se a contagem chega a zero, o objeto pode ser removido.

Exemplo conceptual:

1. `x = [1, 2]` -> objeto lista criado;
2. `y = x` -> mais uma referência;
3. `del x` -> ainda sobra `y`;
4. `del y` -> sem referências, objeto torna-se elegível para limpeza.

### 6.2 Quando é que a contagem de referências aumenta?

A contagem de referências de um objeto aumenta sempre que **mais alguma coisa passa a apontar para ele**, por exemplo:

1. **Atribuição a uma variável**

```python
a = [1, 2, 3]   # a aponta para a lista
b = a           # b passa a apontar para a MESMA lista -> refcount sobe
```

2. **Guardar dentro de outra estrutura (container)**

```python
lista = []
x = [10, 20]

lista.append(x)  # agora a lista também aponta para x -> refcount sobe
```

3. **Passar como argumento para uma função**

```python
def f(obj):
    pass

x = [1, 2]
f(x)  # durante a chamada, a função cria uma referência extra (parâmetro)
```

> Importante: o parâmetro da função é também um nome que aponta para o objeto.

### 6.3 Quando é que a contagem de referências diminui?

Diminui quando **uma referência deixa de existir**, por exemplo:

1. **Reatribuição (o nome passa a apontar para outra coisa)**

```python
x = [1, 2]
x = [9, 9]   # o nome x deixou de apontar para a primeira lista -> refcount desce
# Neste momento a lista [1, 2] tem refcount 0 (se não houver mais referências) e pode ser removida.
```

2. **`del` (remover o nome)**

```python
x = [1, 2]
del x        # o nome x desaparece -> refcount desce
```

3. **Fim de uma função (o frame desaparece)**

```python
def criar():
    temp = [1, 2, 3]  # temp é uma referência local
    # quando a função termina, temp desaparece -> refcount desce
```

---

## Nota sobre `sys.getrefcount`

Existe forma de observar contagem de referências com `sys.getrefcount`,  
mas para iniciantes não é obrigatório agora.  
Mais importante é entender a lógica de vida dos objetos.

---

## 7. Garbage Collection e ciclos

O Garbage Collection é um mecanismo que automatiza a gestão de memória.

Cenários em que o GC atua:

1. Objetos órfãos (sem referências):
    - Quando um objeto fica com zero referências a apontar para ele, o GC pode libertar a memória associada a esse objeto.
      Por exemplo:

    ```python
        def f(): temp = [1, 2, 3]
        f()
    ```

    Depois de `f()` terminar, a lista `[1, 2, 3]` fica órfã (sem referências) e pode ser removida. O GC é responsável por identificar e limpar esses objetos órfãos.

2. Ciclos de referência:
    - O GC também é responsável por detectar e limpar ciclos de referência, onde um grupo de objetos se referenciam mutuamente mas não são acessíveis a partir do programa.
      Por exemplo:
    ```python
        a = [] a.append(a)
        # cria um ciclo de referência
    ```
    Aqui temos uma lista `a` que contém uma referência para si mesma. Mesmo que façamos `del a`, o objeto lista ainda tem uma referência para si mesmo, então o refcount não chega a zero. O GC entra em ação para identificar e limpar esse ciclo de referência.

### 7.1 “Órfão” vs “Inacessível” (distinção útil)

- **Órfão (sem referências)**: refcount chega a 0.
- **Inacessível (unreachable)**: o teu programa já não tem como chegar ao objeto a partir de “raízes” (nomes globais, frames ativos…), mas pode haver referências internas em ciclo.

A contagem de referências resolve muito, mas **não resolve ciclos**.

### 7.2 O que o Garbage Collector faz, em termos simples?

O Garbage Collector (GC) entra para resolver isto:

- procura grupos de objetos que se referenciam entre si
- mas que já não são alcançáveis a partir do teu programa
- e liberta-os

Mentalmente:

> GC procura “ilhas” de objetos que já não estão ligados ao “continente” (o código em execução).

---

## 8. Memory leaks: o que é e como evitar

Um memory leak acontece quando um programa mantém referências a objetos que já não são necessários, impedindo que o Garbage Collector os limpe.
Em Python, leaks graves são menos comuns do que em gestão manual, mas podem acontecer.

Exemplos:

- guardar objetos indefinidamente em listas globais;
- criar caches sem limite;
- manter referências sem necessidade;
- abrir recursos e não libertar (ex.: ficheiros, sockets).

### Dica prática

Quando possível:

- limita o tamanho de estruturas em memória;
- reutiliza dados com critério;
- fecha recursos com `with` (ficheiros);
- evita manter referências "esquecidas".

---

## 9. Boas práticas para alunos

1. Usa nomes claros para variáveis (`lista_alunos`, `notas_turma`).
2. Evita criar aliases sem necessidade.
3. Quando precisares de independência entre listas, copia explicitamente.
4. Distingue sempre:
    - "mudar variável para novo objeto";
    - "mudar objeto existente".
5. Não uses `is` para comparar conteúdos de strings/listas; usa `==`.
6. Usa `is` principalmente para `None`.

### Bónus de compreensão: inteiros pequenos e otimizações

Em muitas execuções de CPython, inteiros pequenos (tipicamente entre `-5` e `256`) podem ser reutilizados internamente.

Isto é uma otimização de implementação (não regra pedagógica para escrever lógica).

Conclusão prática:

- não escrevas código a depender desse detalhe;
- usa `==` para comparar valores;
- usa `is` para identidade (`None`).

---

## 10. Resumo final

- Python gere memória automaticamente.
- Variáveis em Python apontam para objetos.
- Objetos imutáveis tendem a gerar novo objeto quando "alterados".
- Objetos mutáveis podem ser alterados no mesmo local.
- Contagem de referências + Garbage Collector garantem limpeza.
- Compreender referências evita muitos erros com listas e dicionários.

### Ligação com o módulo 06

No Python, estes mecanismos aparecem em alto nível (confortáveis para programar).  
No nível do sistema, o processo continua a depender de CPU, sistema operativo e instruções de máquina.

Para essa visão completa, consulta:

- `Memoria/06_do_codigo_a_execucao_real_so_cpu_isa.md`

---

**A seguir:** [`05_estruturas_dinamicas_e_complexidade.md`](05_estruturas_dinamicas_e_complexidade.md)

---

## 11. Changelog

- **2026-02-04**: versão inicial do módulo 03.
