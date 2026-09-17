![Header](../Images/Header.png)

# Python · 10.º Ano (Programador de Informática)

> Este README descreve apenas a pasta `Python`. Para uma visão geral do repositório, vê o [README.md](../README.md) na raiz.

Materiais de apoio em **Markdown** para introdução à programação em Python, alinhados ao programa da disciplina e escritos com foco pedagógico para alunos em fase inicial.

Cada módulo inclui:

- explicação teórica detalhada em linguagem clara;
- exemplos práticos em Python;
- alertas de erros comuns;
- secção de Exercícios (10–12, do mais simples ao mais desafiante);
- secção de changelog.

O ficheiro [`00_formulario_apoio.md`](./00_formulario_apoio.md) serve como ficha de consulta rápida, e os ficheiros [`00_exercicios_de_preparacao.md`](./00_exercicios_de_preparacao.md) e [`00_exercicios_de_recuperacao.md`](./00_exercicios_de_recuperacao.md) reúnem exercícios extra de consolidação/recuperação.

O percurso desta pasta está organizado em **11 módulos tutoriais**, **3 fichas de apoio** e **1 projeto final**.

---

## Índice

- [Estrutura do repositório](#estrutura-do-repositório)
- [Módulos e objetivos](#módulos-e-objetivos)
- [Pré-requisitos e ambiente de trabalho](#pré-requisitos-e-ambiente-de-trabalho)

---

## Estrutura do repositório

```text
.
├── 00_formulario_apoio.md
├── 00_exercicios_de_preparacao.md
├── 00_exercicios_de_recuperacao.md
├── 01_introducao_variaveis_tipos_strings_io.md
├── 02_operadores_e_controlo_de_fluxo_if_ciclos.md
├── 03_listas_dicionarios_estruturas_aninhadas.md
├── 04_funcoes_do_basico_ao_avancado.md
├── 05_algoritmos_e_padroes_de_programacao.md
├── 06_slicing_list_comprehensions.md
├── 07_ficheiros_texto_json_csv.md
├── 08_excecoes_e_tratamento_de_erros.md
├── 09_modulos_e_organizacao_de_projetos.md
├── 10_estruturas_e_algoritmos_classicos.md
├── 11_projeto_final_python.md
└── README.md
```

---

## Módulos e objetivos

1. [Introdução: variáveis, tipos, strings e I/O](./01_introducao_variaveis_tipos_strings_io.md)  
   Objetivo: dar o primeiro contacto com Python e com a ideia de "programa".

2. [Operadores e controlo de fluxo (if, ciclos)](./02_operadores_e_controlo_de_fluxo_if_ciclos.md)  
   Objetivo: introduzir operadores, decisões e repetições.

3. [Listas, dicionários e estruturas aninhadas](./03_listas_dicionarios_estruturas_aninhadas.md)  
   Objetivo: consolidar o armazenamento de coleções de dados e treinar um pensamento mais estruturado.

4. [Funções, do básico ao avançado](./04_funcoes_do_basico_ao_avancado.md)  
   Objetivo: construir um módulo sólido sobre funções, do `def` básico a ideias de ordem superior.

5. [Algoritmos e padrões de programação](./05_algoritmos_e_padroes_de_programacao.md)  
   Objetivo: resolver problemas completos, do enunciado ao código.

6. [Slicing e list comprehensions](./06_slicing_list_comprehensions.md)  
   Objetivo: aprofundar slicing e compreensões de lista.

7. [Ficheiros: texto, JSON e CSV](./07_ficheiros_texto_json_csv.md)  
   Objetivo: guardar e reutilizar dados entre execuções com formatos simples e práticos.

8. [Exceções e tratamento de erros](./08_excecoes_e_tratamento_de_erros.md)  
   Objetivo: ler tracebacks e tornar os programas mais robustos com `try`/`except`.

9. [Módulos e organização de projetos](./09_modulos_e_organizacao_de_projetos.md)  
   Objetivo: organizar código em vários ficheiros e reutilizar funções com `import`.

10. [Estruturas e algoritmos clássicos](./10_estruturas_e_algoritmos_classicos.md)  
    Objetivo: introduzir pesquisa linear, ordenação básica (bubble/selection) e noção de eficiência.

11. [Projeto final: quiz em consola](./11_projeto_final_python.md)  
    Objetivo: aplicar os módulos 01–10 na construção de um projeto completo, em grupo.

Exercícios extra de preparação/recuperação: [00_exercicios_de_preparacao.md](./00_exercicios_de_preparacao.md) e [00_exercicios_de_recuperacao.md](./00_exercicios_de_recuperacao.md)

Ficha de consulta rápida: [00_formulario_apoio.md](./00_formulario_apoio.md)

---

## Pré-requisitos e ambiente de trabalho

- Python 3.x instalado (idealmente uma versão recente, ex.: 3.11/3.12).
- Editor recomendado: **VS Code** ou IDE online com:
    - extensão **Python**;
    - (opcional) ferramenta de execução integrada (Run/Debug).

Para correr um exemplo:

1. Criar um ficheiro, por exemplo `exemplo.py`;
2. Copiar o código do ficheiro `.md` para o `.py`;
3. Guardar;
4. Executar com:
    - `python exemplo.py` no terminal, ou
    - botão de _Run_ do editor.

---

## Changelog

- **2026-09-17**: README reestruturado para alinhar com o formato do README de `C` (secções "Módulos e objetivos", "Rota de estudo recomendada" e "Changelog").

![Footer](../Images/Footer.png)
