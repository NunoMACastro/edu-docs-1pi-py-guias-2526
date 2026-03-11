# Teste de Avaliação - Memória e Execução de Programas (10.º Ano)

**Nome:** **\*\***\*\***\*\***\_\_\_\_**\*\***\*\***\*\***  
**Turma:** \***\*\_\_\*\***  
**Data:** \_**\_ / \_\_** / **\_\_**  
**Duração sugerida:** 60-75 minutos

## Instruções

- Lê todas as perguntas com atenção.
- Nas perguntas de escolha múltipla, assinala apenas **uma** opção.
- Mostra os passos nas conversões para binário.
- Nas perguntas de desenvolvimento, responde de forma clara e com vocabulário técnico correto.

---

## Parte A - Escolha múltipla (15 perguntas)

1. Qual é a principal função da memória **cache**?
    - A) Guardar dados de forma permanente como um SSD
    - B) Guardar instruções frequentes perto da CPU para acelerar acessos
    - C) Substituir a RAM durante falhas de energia
    - D) Guardar apenas ficheiros multimédia

2. A memória RAM é considerada:
    - A) Não volátil e lenta
    - B) Volátil e de acesso rápido
    - C) Não volátil e apenas de leitura
    - D) Volátil e apenas para backup

3. A ROM é usada principalmente para:
    - A) Armazenar programas temporários do utilizador
    - B) Guardar firmware/instruções de arranque
    - C) Aumentar a frequência do processador
    - D) Substituir a cache L1

4. Um **byte** corresponde a:
    - A) 2 bits
    - B) 4 bits
    - C) 8 bits
    - D) 16 bits

5. No ciclo de execução da CPU, a sequência correta é:
    - A) Execute -> Fetch -> Decode
    - B) Decode -> Execute -> Fetch
    - C) Fetch -> Decode -> Execute
    - D) Fetch -> Execute -> Decode

6. O que representa um endereço de memória?
    - A) O valor decimal de uma variável
    - B) A posição onde um dado/instrução está armazenado
    - C) O nome da variável no código
    - D) O tipo de dado (int, str, list)

7. Em Python, uma variável guarda principalmente:
    - A) Sempre o valor físico em RAM
    - B) Uma referência para um objeto
    - C) Apenas números inteiros
    - D) Um endereço IP

8. Em termos gerais, objetos como listas e dicionários em Python são alocados sobretudo na:
    - A) ROM
    - B) Stack de chamadas
    - C) Heap
    - D) Cache L1

9. Qual sequência descreve melhor o modelo de execução do Python?
    - A) Código-fonte (.py) -> código de máquina direto -> execução
    - B) Código-fonte (.py) -> bytecode -> PVM/interpretador -> CPU
    - C) Código-fonte (.py) -> ROM -> cache -> SSD
    - D) Código-fonte (.py) -> BIOS -> execução sem sistema operativo

10. Em Python, `==` e `is` comparam respetivamente:
    - A) Identidade e valor
    - B) Tipo e tamanho
    - C) Valor e identidade
    - D) Endereço físico e valor lógico

11. Qual afirmação sobre mutabilidade está correta?
    - A) `list` é imutável
    - B) `tuple` é mutável
    - C) `str` é mutável
    - D) `dict` é mutável

12. Em termos gerais, a **stack** de execução guarda sobretudo:
    - A) Ficheiros do sistema operativo
    - B) Frames de chamadas de função
    - C) Vídeo em streaming
    - D) Dados permanentes do utilizador

13. O `__pycache__` em Python está relacionado com:
    - A) Cópias de segurança automáticas de projetos
    - B) Ficheiros de bytecode para acelerar execuções
    - C) Logs de erros do sistema operativo
    - D) Imagens temporárias da interface gráfica

14. Um processo e uma thread diferem porque:
    - A) Processo e thread são exatamente o mesmo conceito
    - B) Processo tem espaço de memória próprio; threads partilham o processo
    - C) Thread é sempre mais lenta que processo
    - D) Processo existe apenas em Python

15. O Garbage Collector em Python é particularmente útil para:
    - A) Aumentar a frequência da CPU
    - B) Converter decimal para binário
    - C) Libertar objetos inacessíveis, incluindo ciclos
    - D) Criar variáveis globais automaticamente

---

## Parte B - Conversão de números para binário (5 perguntas)

Converte os seguintes números **decimais** para binário:

16. 19 = **\*\*\*\***\_\_\_\_**\*\*\*\*** (base 2)

17. 42 = **\*\*\*\***\_\_\_\_**\*\*\*\*** (base 2)

18. 77 = **\*\*\*\***\_\_\_\_**\*\*\*\*** (base 2)

19. 100 = **\*\*\*\***\_\_\_\_**\*\*\*\*** (base 2)

20. 255 = **\*\*\*\***\_\_\_\_**\*\*\*\*** (base 2)

---

## Parte C - Desenvolvimento (3 perguntas)

21. Explica a diferença entre um objeto "órfão" e um objeto "inacessível" em Python e descreve como o Garbage Collector atua nesses casos.

22. Em Python, explica o que pode acontecer quando duas variáveis referenciam a mesma lista (alias). Usa um pequeno exemplo e descreve os possíveis efeitos laterais.

23. Descreve o caminho de execução de um programa desde o código-fonte até à execução no CPU, incluindo pelo menos: sistema operativo, loader, processo, instruções e ciclo fetch-decode-execute.

24. Desenvolve, da forma mais detalhada que conseguires, todo o processo de utilização da RAM por parte de um programa. Tópicos obrigatórios: alocação de memória, stack vs heap, referências, e libertação de memória.

---

## Chave de Respostas

### Parte A - Escolha múltipla

1. B
2. B
3. B
4. C
5. C
6. B
7. B
8. C
9. B
10. C
11. D
12. B
13. B
14. B
15. C

### Parte B - Conversões

16. 19 = `10011`
17. 42 = `101010`
18. 77 = `1001101`
19. 100 = `1100100`
20. 255 = `11111111`
