# Teste de Avaliação - Gestão de Memória em Python (10.º Ano) - Versão 2

**Nome:** **************__**************  
**Turma:** ****__****  
**Data:** _**_ / __** / **__**  
**Duração sugerida:** 60-75 minutos

## Instruções

- Lê todas as perguntas com atenção.
- Nas perguntas de escolha múltipla, assinala apenas **uma** opção.
- Na parte de código, justifica brevemente quando pedido.
- Nas perguntas de desenvolvimento, usa vocabulário técnico correto.

---

## Parte A - Escolha múltipla (15 perguntas)

1. Em CPython, ao executar um ficheiro `.py`, o primeiro passo relevante é:
    - A) Converter diretamente para instruções nativas da CPU
    - B) Compilar para bytecode da máquina virtual Python
    - C) Guardar automaticamente em ROM
    - D) Criar uma thread por cada função

2. O diretório `__pycache__` serve principalmente para:
    - A) Guardar cópias de segurança do projeto
    - B) Guardar ficheiros de bytecode (`.pyc`) para reutilização
    - C) Guardar logs do sistema operativo
    - D) Guardar código de máquina da ISA

3. Quando uma função é chamada, em termos de execução:
    - A) É criada uma stack frame para essa chamada
    - B) Todos os objetos são movidos para ROM
    - C) O código-fonte é apagado da memória
    - D) O processo principal termina

4. Em Python, os objetos (ex.: listas e dicionários) vivem tipicamente na:
    - A) Stack de chamadas
    - B) Heap
    - C) Cache L1
    - D) ROM

5. O que está mais associado à stack de execução em Python?
    - A) Objetos dinâmicos de longa duração
    - B) Frames das chamadas de função
    - C) Ficheiros no disco
    - D) Código binário persistente

6. Numa atribuição `b = a` (com `a` a referir uma lista), o que acontece?
    - A) É sempre criada cópia profunda
    - B) `b` passa a referenciar o mesmo objeto que `a`
    - C) `a` deixa de existir
    - D) A lista passa para ROM

7. Qual afirmação sobre `==` e `is` está correta?
    - A) Ambos comparam identidade
    - B) `==` compara valor; `is` compara identidade
    - C) `is` compara valor; `==` compara tipo
    - D) Ambos comparam tipo

8. A contagem de referências de um objeto aumenta quando:
    - A) Uma nova variável passa a referenciar esse objeto
    - B) O programa entra numa função
    - C) O objeto é impresso com `print`
    - D) O objeto é convertido para `str`

9. A contagem de referências de um objeto diminui quando:
    - A) O objeto é comparado com `==`
    - B) Uma referência é removida (ex.: `del nome`)
    - C) O objeto é lido numa expressão
    - D) O programa compila bytecode

10. O Garbage Collector (GC) em Python é especialmente importante para:
    - A) Limpar cache L1 da CPU
    - B) Recolher ciclos de objetos que ficaram inacessíveis
    - C) Converter bytecode em código-fonte
    - D) Gerir permissões do sistema operativo

11. Dois objetos podem ter o mesmo valor e identidades diferentes?
    - A) Não, nunca
    - B) Sim, isso é possível
    - C) Só em listas, nunca em strings
    - D) Só quando existe erro de sintaxe

12. Num cenário de alias com lista mutável, ao fazer `a.append(5)`:
    - A) Só `a` vê a alteração
    - B) Todas as variáveis que referenciam a mesma lista veem a alteração
    - C) Python bloqueia a operação
    - D) A lista passa a imutável

13. Um `RecursionError` está normalmente ligado a:
    - A) Falta de espaço em disco
    - B) Excesso de chamadas recursivas e profundidade de stack
    - C) Falha de compilação da ISA
    - D) Erro de ROM

14. Qual opção representa melhor o percurso de execução em Python?
    - A) `.py` -> bytecode -> PVM -> instruções no CPU
    - B) `.py` -> ROM -> cache -> CPU
    - C) `.py` -> SSD -> CPU sem interpretação
    - D) `.py` -> BIOS -> GC -> CPU

15. Sobre “objeto órfão” e “objeto inacessível”:
    - A) São sempre conceitos opostos
    - B) Um objeto inacessível pode ser considerado órfão em linguagem informal
    - C) Um objeto com muitas referências é órfão
    - D) Ambos significam “objeto em ROM”

---

## Parte B - Leitura de código (5 perguntas)

16. Considera:

```python
a = [1, 2]
b = a
b.append(3)
print(a, b)
```

Qual é a saída?
- A) `[1, 2] [1, 2, 3]`
- B) `[1, 2, 3] [1, 2, 3]`
- C) `[1, 2] [1, 2]`
- D) Erro de execução

17. Considera:

```python
a = [10, 20]
b = a.copy()
b.append(30)
print(a, b)
```

Qual é a saída?
- A) `[10, 20, 30] [10, 20, 30]`
- B) `[10, 20] [10, 20, 30]`
- C) `[10, 20] [10, 20]`
- D) Erro de sintaxe

18. Considera:

```python
def altera(lista):
    lista.append(99)

nums = [1, 2]
altera(nums)
print(nums)
```

Qual é a saída?
- A) `[1, 2]`
- B) `[99]`
- C) `[1, 2, 99]`
- D) Erro porque argumentos são sempre copiados

19. Considera:

```python
x = [1, [2, 3]]
y = x.copy()
y[1].append(4)
print(x, y)
```

Qual é a melhor interpretação?
- A) `x` e `y` ficam totalmente independentes
- B) A lista interna é partilhada e ambos refletem o `append(4)`
- C) `copy()` faz cópia profunda automática
- D) Código inválido por listas aninhadas

20. Considera:

```python
class N:
    pass

a = N()
b = N()
a.outro = b
b.outro = a
del a
del b
```

Após o último `del`, a afirmação mais correta é:
- A) Os objetos ficam sempre em memória para sempre
- B) A contagem de referências pode não chegar a zero de imediato por causa do ciclo
- C) O código remove obrigatoriamente os objetos sem GC
- D) O ciclo impede qualquer execução do programa

---

## Parte C - Desenvolvimento (3 perguntas)

21. Explica o caminho de execução de um programa Python, desde o ficheiro `.py` até à execução no CPU, incluindo: compilação para bytecode, PVM/interpretador e ciclo fetch-decode-execute.

22. Explica, com exemplo, a diferença entre stack (frames de chamadas) e heap (objetos), e como referências ligam estas duas partes no raciocínio em Python.

23. Explica como funcionam contagem de referências e Garbage Collector em conjunto em Python, incluindo o caso de ciclos de referência.

---

## Gabarito (Professor)

### Parte A - Escolha múltipla

1. B
2. B
3. A
4. B
5. B
6. B
7. B
8. A
9. B
10. B
11. B
12. B
13. B
14. A
15. B

### Parte B - Leitura de código

16. B
17. B
18. C
19. B
20. B
