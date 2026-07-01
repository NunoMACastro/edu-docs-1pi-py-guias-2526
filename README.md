![Header](Images/Header.png)

# Material de Apoio — PI (10.º Ano)

Materiais de apoio em **Markdown** para Programação no **10.º ano (Curso Profissional de Técnico de Programação de Informática)**.

## Conteúdo

### Python

[Ver sub-readme](./Python/README.md)

Apontamentos e exercícios graduais, ficha de consulta e projeto final.

- [`Python/README.md`](./Python/README.md) — índice completo do percurso Python.
- [`Python/11_projeto_final_python.md`](./Python/11_projeto_final_python.md) — enunciado do projeto final.
- [`Python/00_exercicios_de_recuperacao.md`](./Python/00_exercicios_de_recuperacao.md) — exercícios extra de recuperação/consolidação.

### C

[Ver sub-readme](./C/README.md)

Percurso de C, de fundamentos até arrays, `struct`, `enum`, apontadores e estruturas dinâmicas.

- [`C/README.md`](./C/README.md) — índice completo dos **15 módulos**, exercícios e mini projeto.

### Memória e Execução

[Ver sub-readme](./Memoria/README.md)

Módulos sobre hardware base, RAM/ROM, execução Python, heap/stack e complexidade.

- [`Memoria/README.md`](./Memoria/README.md) — guia de estudo.
- [`Memoria/teste_memoria_10ano.md`](./Memoria/teste_memoria_10ano.md) — versão de teste.
- [`Memoria/teste_memoria_10ano_v2.md`](./Memoria/teste_memoria_10ano_v2.md) — versão alternativa.

### Git

- [`Git/git-guia.md`](./Git/git-guia.md) — guia prático com comandos e fluxo básico.
- [`Git/template-gitignore.md`](./Git/template-gitignore.md) — template `.gitignore` para projetos escolares.

### Vários

- [`Varios/terminal-consola-guia.md`](./Varios/terminal-consola-guia.md) — terminal/consola.
- [`Varios/markdown-guia.md`](./Varios/markdown-guia.md) — Markdown.

### Materiais de Professor

Documentos de avaliação e feedback pedagógico (não são fichas de aluno):

- [`Avaliacoes/Python/`](./Avaliacoes/Python/) — avaliações de repositórios/projetos.
- [`modulo_804_projeto_recuperacao.md`](./modulo_804_projeto_recuperacao.md) — proposta de trabalho de recuperação.

## Validação dos docs

Para validar consistência editorial/técnica do conteúdo PT base:

```bash
python3 scripts/validate_docs.py
```

O comando valida:

- paridade de code fences;
- links relativos quebrados;
- sintaxe de blocos `python`.

![Footer](Images/Footer.png)
