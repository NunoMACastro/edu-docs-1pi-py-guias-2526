# Guia Completo de Markdown (10º ao 12º Ano)

> **Objetivo:**  
> Ensinar Markdown de forma simples e completa, com exemplos práticos.  
> Útil para relatórios, fichas, README de projetos e documentação.

---

## 1. Conceitos Fundamentais

| Termo               | Explicação                                                            |
| ------------------- | --------------------------------------------------------------------- |
| **Markdown**        | Linguagem de marcação simples para formatar texto de forma rápida.    |
| **Renderização**    | Conversão do texto Markdown para HTML ou para a versão “formatada”.   |
| **GFM**             | GitHub Flavored Markdown: versão com extras (tabelas, tarefas, etc.). |
| **README.md**       | Ficheiro principal de explicação de um projeto.                       |
| **Código inline**   | Pequenos trechos de código dentro de uma frase, com `crases`.         |
| **Bloco de código** | Trecho de código com várias linhas, entre três crases ```             |
| **Heading**         | Título ou subtítulo (feito com #).                                    |

---

## 2. Estrutura Básica

Um documento Markdown é **texto normal** com símbolos para formatar.

Exemplo mínimo:

```md
# Título

Este é um parágrafo com **negrito** e _itálico_.
```

> Regra simples: **usa linhas em branco** para separar parágrafos.

---

## 3. Títulos (Headings)

```md
# Título 1

## Título 2

### Título 3

#### Título 4
```

> Usa títulos por ordem: não saltes do `#` para `###` sem razão.

---

## 4. Ênfase e Texto

| Formatação        | Markdown       | Resultado (visual) |
| ----------------- | -------------- | ------------------ |
| Negrito           | `**texto**`    | **texto**          |
| Itálico           | `*texto*`      | _texto_            |
| Negrito + Itálico | `***texto***`  | **_texto_**        |
| Riscado (GFM)     | `~~texto~~`    | ~~texto~~          |
| Código inline     | `` `codigo` `` | `codigo`           |

---

## 5. Listas

### 5.1) Lista não ordenada

```md
- Item A
- Item B
- Item C
```

### 5.2) Lista ordenada

```md
1. Passo um
2. Passo dois
3. Passo tres
```

### 5.3) Lista de tarefas (GFM)

```md
- [x] Feito
- [ ] Por fazer
```

> Dica: uma lista é ótima para instruções ou materiais.

---

## 6. Links e Imagens

### Link

```md
[Texto do link](https://exemplo.com)
```

### Imagem

```md
![Texto alternativo](caminho/da-imagem.png)
```

> O texto alternativo ajuda na acessibilidade e quando a imagem não carrega.

---

## 7. Código

### 7.1) Código inline

```md
Usa o comando `git status` para ver alterações.
```

### 7.2) Bloco de código

````md
```python
print("Ola, Markdown!")
```
````

> Especificar a linguagem melhora a cor (syntax highlighting).

---

## 8. Citações

```md
> Esta é uma citação importante.
```

> Pode ser usada para notas, definições ou fontes.

---

## 9. Tabelas (GFM)

```md
| Comando | Funcao           |
| ------- | ---------------- |
| `cd`    | Mudar de pasta   |
| `ls`    | Listar ficheiros |
```

> Usa `|` para separar colunas e `---` para a linha do cabeçalho.

---

## 10. Separadores

```md
---
```

Cria uma linha horizontal para separar secções.

---

## 11. Quebras de Linha

Duas formas:

```md
Linha 1 (dois espacos no fim)  
Linha 2
```

ou

```md
Linha 1<br>
Linha 2
```

---

## 12. Escapar Caracteres

Se precisares de mostrar símbolos Markdown sem formatar:

```md
\*não é itálico\*
\# não é título
```

---

## 13. HTML no Markdown (quando necessário)

Markdown permite HTML simples:

```md
<details>
<summary>Mostrar mais</summary>
Texto escondido aqui.
</details>
```

> Útil para conteúdos extra sem poluir a página.

---

## 14. Markdown no GitHub vs. Outros Editores

- GitHub usa **GFM**, com **tabelas**, **checklists** e **riscado**.
- VSCode, Obsidian e outros podem ter pequenas diferenças no render.
- Se algo não funcionar, testa no local onde vais publicar.

---

## 15. Erros Comuns (e como evitar)

- **Esquecer linha em branco** entre parágrafos → texto fica junto.
- **Misturar níveis de títulos** sem lógica → má leitura.
- **Links quebrados** → confirma URLs e caminhos.
- **Ficheiros grandes** sem secções → usa títulos e separadores.

---

## 16. Estrutura Recomendada para um README

```md
# Nome do Projeto

## Objetivo

## Como usar

## Tecnologias

## Autor
```

> Um README claro facilita a avaliação e a colaboração.

---

## 17. Mini-Exercicios

1. Cria um documento com um título, dois subtítulos e um parágrafo.
2. Faz uma lista de tarefas de uma semana de estudo.
3. Cria uma tabela com 3 comandos de terminal e a sua função.
4. Escreve um README simples para um projeto escolar.

---

## 18. Resumo Rapido (Cheat Sheet)

```md
# Titulo 1

## Titulo 2

**negrito** _italico_ `codigo`

- lista

1. lista numerada
   [link](https://exemplo.com)
   ![imagem](caminho.png)
    > citacao
```

---

## 19. Ajuda

- Documentacao oficial: pesquisa por "Markdown Guide".
- VSCode: extensao de Preview para ver o resultado.
- GitHub: cria um `README.md` e usa o Preview.

---

## 20. Fluxo Recomendado para Alunos

```md
1. Cria o ficheiro `README.md`
2. Usa titulos para organizar
3. Escreve por secoes curtas
4. Revê o Preview
```
