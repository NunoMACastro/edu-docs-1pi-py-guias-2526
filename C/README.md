# C · 10.º Ano (Programador de Informática)

> Este README descreve apenas a pasta `C`. Para visão geral do repositório, consulta o [README.md](../README.md) da raiz.

Materiais de apoio em **Markdown** para introdução e consolidação de programação em **C**, alinhados ao programa da disciplina e escritos com foco pedagógico para alunos em fase inicial.

Cada módulo inclui:

- explicação teórica detalhada em linguagem clara;
- exemplos práticos em C;
- alertas de erros comuns;
- secção de **exercícios apenas com enunciado** (sem resolução);
- secção de changelog.

---

## Índice

- [Estrutura da pasta](#estrutura-da-pasta)
- [Módulos e objetivos](#módulos-e-objetivos)
- [Nota sobre POO e exceções em C](#nota-sobre-poo-e-exceções-em-c)
- [Rota de estudo recomendada](#rota-de-estudo-recomendada)
- [Como usar estes materiais](#como-usar-estes-materiais)

---

## Estrutura da pasta

```text
.
├── 01_ciclo_de_vida_do_software.md
├── 02_pensamento_computacional_principios.md
├── 03_algoritmos_principios.md
├── 04_metodologias_de_desenvolvimento.md
├── 05_ambiente_de_desenvolvimento_c.md
├── 06_linguagem_estruturada_em_c.md
├── 07_dados_variaveis_constantes_tipos.md
├── 07a_entrada_saida_formatada_printf_scanf_e_enderecos.md
├── 08_operadores_em_c.md
├── 09_estruturas_de_controlo_em_c.md
├── 10_subprogramas_funcoes_e_parametros.md
├── 11_funcionalidades_editor_de_texto.md
├── 12_estruturas_estaticas_strings_arrays_matrizes.md
├── 13_estruturas_compostas_struct_union_enum.md
├── 14_estruturas_dinamicas_apontadores.md
├── 15_classes_e_objetos_contexto_c.md
├── 16_heranca_e_polimorfismo_contexto_c.md
├── 17_excecoes_e_tratamento_de_erros_em_c.md
├── 18_ficheiros_acesso_e_manipulacao_em_c.md
├── 19_editor_texto_produtividade_e_debug.md
└── README.md
```

---

## Módulos e objetivos

1. [Ciclo de vida do software](./01_ciclo_de_vida_do_software.md)  
   Objetivo: perceber as fases de desenvolvimento e manutenção de software.

2. [Pensamento computacional - princípios](./02_pensamento_computacional_principios.md)  
   Objetivo: decompor problemas e construir soluções antes de codificar.

3. [Algoritmos - princípios](./03_algoritmos_principios.md)  
   Objetivo: criar algoritmos corretos, claros e testáveis.

4. [Metodologias de desenvolvimento](./04_metodologias_de_desenvolvimento.md)  
   Objetivo: organizar trabalho com abordagens adequadas a projetos escolares.

5. [Ambiente de desenvolvimento em C](./05_ambiente_de_desenvolvimento_c.md)  
   Objetivo: configurar editor, compilador e fluxo de build/debug.

6. [Linguagem estruturada em C](./06_linguagem_estruturada_em_c.md)  
   Objetivo: dominar estrutura de programa e controlo de fluxo base.

7. [Dados, variáveis, constantes e tipos](./07_dados_variaveis_constantes_tipos.md)  
   Objetivo: usar tipos simples e expressões corretamente.

8. [Entrada/saída formatada: `printf`, `scanf`, `&` e `*`](./07a_entrada_saida_formatada_printf_scanf_e_enderecos.md)  
   Objetivo: dominar I/O formatada com validação e compreender o uso de endereços.

9. [Operadores em C](./08_operadores_em_c.md)  
   Objetivo: aplicar operadores aritméticos, relacionais, lógicos e de atribuição.

10. [Estruturas de controlo](./09_estruturas_de_controlo_em_c.md)  
   Objetivo: usar decisões e ciclos com segurança.

11. [Subprogramas (funções e parâmetros)](./10_subprogramas_funcoes_e_parametros.md)  
    Objetivo: modularizar código e compreender escopo e passagem por parâmetros.

12. [Funcionalidades de editor de texto](./11_funcionalidades_editor_de_texto.md)  
    Objetivo: melhorar produtividade básica no editor.

13. [Estruturas estáticas: strings, arrays e matrizes](./12_estruturas_estaticas_strings_arrays_matrizes.md)  
    Objetivo: manipular dados estáticos com segurança.

14. [Estruturas compostas: `struct`, `union`, `enum`](./13_estruturas_compostas_struct_union_enum.md)  
    Objetivo: representar dados complexos e estados.

15. [Estruturas dinâmicas e apontadores](./14_estruturas_dinamicas_apontadores.md)  
    Objetivo: gerir memória dinâmica e ponteiros com disciplina.

16. [Classes e objetos (contexto em C)](./15_classes_e_objetos_contexto_c.md)  
    Objetivo: aplicar equivalente de modelação orientada a objetos em C.

17. [Herança e polimorfismo (contexto em C)](./16_heranca_e_polimorfismo_contexto_c.md)  
    Objetivo: compreender e simular estes conceitos em C.

18. [Exceções e tratamento de erros em C](./17_excecoes_e_tratamento_de_erros_em_c.md)  
    Objetivo: implementar tratamento de erro robusto sem `try/catch`.

19. [Ficheiros: acesso e manipulação](./18_ficheiros_acesso_e_manipulacao_em_c.md)  
    Objetivo: persistir dados em ficheiros texto/binário com validação.

20. [Editor de texto: produtividade e debug](./19_editor_texto_produtividade_e_debug.md)  
    Objetivo: consolidar práticas avançadas de depuração e manutenção.

---

## Nota sobre POO e exceções em C

A linguagem C **não possui** classes, herança, polimorfismo e exceções como C++/Java/Python.

Nestes materiais:

- "classes/objetos" são explicados via `struct` + funções + organização de API;
- "herança/polimorfismo" são explicados via composição e ponteiros para função;
- "exceções" são abordadas com códigos de retorno, validação, `errno` e mensagens de erro.

---

## Rota de estudo recomendada

1. `01` a `05` (base de engenharia e ambiente)
2. `06`, `07` e `07a` (núcleo da linguagem C + I/O formatada com endereços)
3. `08` a `10` (operadores, controlo e funções)
4. `11` + `19` (produtividade e debug no editor)
5. `12` a `14` (dados em memória: estáticos e dinâmicos)
6. `15` a `17` (conceitos avançados em contexto C e robustez)
7. `18` (ficheiros e persistência; recomendado após base sólida de input/output)

---

## Como usar estes materiais

1. Estuda a teoria com calma.
2. Reproduz exemplos no teu computador.
3. Faz os exercícios por ordem.
4. Marca dúvidas para discutir em aula.
5. Revê módulos anteriores antes de temas mais avançados.

---

## Changelog

- **2026-02-23**: reestruturação completa da pasta `C` para versão detalhada e pedagógica.
- **2026-02-23**: todos os módulos atualizados com exercícios sem resolução (apenas enunciados).
- **2026-04-15**: adicionado módulo `07a` para aprofundar `printf`/`scanf`, `&` e `*`, com atualização da rota de estudo.
