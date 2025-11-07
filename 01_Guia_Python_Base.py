# =============================================================================
# RESUMO DETALHADO — PYTHON (10.º ANO) · Ficheiro de Consulta
# Como usar:
# - Lê as notas (comentários) e observa o código logo abaixo de cada bloco.
# =============================================================================

# =============================================================================
# 1) VARIÁVEIS
# -----------------------------------------------------------------------------
# - “Etiquetas” para valores em memória; Python infere o tipo (tipagem dinâmica).
# - snake_case para nomes; CONSTANTES em MAIÚSCULAS (por convenção).
# - Reatribuição pode mudar o tipo do valor guardado.
# =============================================================================

idade = 16                               # int (inteiro)
altura = 1.72                            # float (decimal)
nome = "Ana"                             # str (texto)
aprovado = True                          # bool (booleano)
idade = "dezasseis"                      # reatribuição; agora 'idade' guarda uma string


# =============================================================================
# 2) TIPOS DE DADOS
# -----------------------------------------------------------------------------
# int, float, bool, str, list, dict, NoneType.
# Conversões: int("10"), float("2.5"), str(123), bool(0)->False, bool("x")->True.
# Coleções vazias contam como False: "", [], {}, 0, 0.0, None.
# =============================================================================

valores = [10, 3.14, True, "texto", [1, 2], {"nome": "Ana"}, None]  # coleção com vários tipos
tipos = [type(v).__name__ for v in valores]                         # compreens. de lista: nome do tipo de cada v


# =============================================================================
# 3) STRINGS — CONCEITOS E MÉTODOS
# -----------------------------------------------------------------------------
# - Strings são IMUTÁVEIS; usa slicing/métodos para gerar novas strings.
# - Métodos úteis: lower, upper, strip, replace, find, count, split, join,
#   startswith, endswith, isdigit, isalpha, isalnum.
# =============================================================================

s = "  Olá, Mundo  "                      # string com espaços à esquerda/direita
s_strip = s.strip()                        # remove espaços do início e fim -> "Olá, Mundo"
tem_mundo = "Mundo" in s                   # operador 'in': verifica se "Mundo" aparece em s (True/False)
s_upper = "abc".upper()                    # coloca a string "abc" em maiúsculas -> "ABC"
palavras = "um dois três".split()          # divide por espaços -> ["um","dois","três"]
reconstruida = "-".join(["a", "b", "c"])   # junta elementos com '-' -> "a-b-c"
invertida = "Programação"[::-1]            # slicing com passo -1: string invertida
primeiro_char = "Python"[0]                # indexação: primeiro caractere -> "P"
ult_char = "Python"[-1]                    # índice negativo: último caractere -> "n"
fatia = "Programação"[2:7]                 # slicing do índice 2 ao 6 -> "ogram"


# =============================================================================
# 4) ENTRADA E SAÍDA (print e input)
# -----------------------------------------------------------------------------
# - print(*valores, sep=" ", end="\n") imprime valores; f-strings ajudam na formatação.
# - input(prompt) devolve SEMPRE string; converte para int/float se precisares.
# =============================================================================

curso = "PI 10.º"                                                        # string simples
media_exemplo = 14.356                                                   # valor decimal
print("Bem-vindo ao curso de", curso)                                 # exemplo de print simples
print(f"Média do curso: {media_exemplo:.2f}")                       # print com f-string e formatação (2 casas decimais)

# Para testar input localmente, descomenta as linhas seguintes e executa:
# nome_user = input("Como te chamas? ")               # lê texto do utilizador (string)
# idade_txt = input("Idade? ")                        # lê outra string; convém validar antes de converter

nome = input("Como te chamas? ")                     # lê nome (string)
idade = int(input("Idade? "))                          # lê idade e converte para inteiro

# Temos que converter para um número porque input() devolve sempre string


# =============================================================================
# 5) F-STRINGS (INTERPOLAÇÃO E FORMATAÇÃO)
# -----------------------------------------------------------------------------
# - f"texto {expressao}" insere variáveis/expressões dentro da string.
# - Exemplos de formatação: {x:.2f}, {n:03d}, {p:.1%}, {txt:^10}.
# =============================================================================

nota = 17.375                              # valor decimal a formatar
aluno = "Beatriz"                          # nome do aluno
resumo = f"Aluno: {aluno} | Nota: {nota:.2f}"  # interpolação + 2 casas decimais -> "Aluno: Beatriz | Nota: 17.38"


# =============================================================================
# 6) COMENTÁRIOS
# -----------------------------------------------------------------------------
# - Comentários de linha começam por "#": explicam o “porquê/como”.
# - Docstrings (strings multilinha) podem documentar módulos (não usadas aqui).
# =============================================================================

linha_explicativa = "Linha neutra para manter a secção coesa"  # não tem efeito especial; apenas exemplo


# =============================================================================
# 7) OPERADORES — DETALHE
# -----------------------------------------------------------------------------
# Aritméticos: +  -  *  /  //  %  **    (divisão real, divisão inteira, resto, potência)
# Concatenar/Repetir: "a"+"b" -> "ab"; "ha"*3 -> "hahaha" ; [1,2]+[3]->[1,2,3]; [0]*4->[0,0,0,0]
# Comparação: ==  !=  >  >=  <  <=    (podem ser encadeadas: 1 < x <= 10)
# Lógicos (curto-circuito): and, or, not
#   - and devolve o primeiro “falso” ou o último operando (se todos verdadeiros)
#   - or devolve o primeiro “verdadeiro” ou o último operando (se todos falsos)
# Pertinência: in, not in       ("pi" in "python", 2 in [1,2,3], "k" in {"k":1})
# Identidade: is, is not        (útil com None: if x is None:)
# Atribuições compostas: +=, -=, *=, /=, //=, %=, **=
# Precedência (alta → baixa): ** > * / // % > + - > comparações > not > and > or
# Pitfalls: 0.1 + 0.2 != 0.3 exatamente (usar round para apresentação); "/" dá float, "//" é inteira.
# =============================================================================

a = 7                                     # inteiro para exemplos
b = 3                                     # outro inteiro
soma = a + b                              # 7 + 3 -> 10
diferenca = a - b                         # 7 - 3 -> 4
produto = a * b                           # 7 * 3 -> 21
div_real = a / b                          # 7 / 3 -> 2.333... (float)
div_inteira = a // b                      # 7 // 3 -> 2 (descarta casas decimais)
resto = a % b                             # 7 % 3 -> 1 (resto da divisão inteira)
potencia = a ** b                         # 7 ** 3 -> 343 (potência)

concat_str = "Py" + "thon"                # concatenação de strings -> "Python"
rep_str = "ha" * 3                        # repetição -> "hahaha"
concat_lista = [1, 2] + [3]               # concatenação de listas -> [1,2,3]
rep_lista = [0] * 4                       # repetição de elementos -> [0,0,0,0]

igual = (a == b)                          # False (7 não é igual a 3)
diferente = (a != b)                      # True
maior = (a > b)                           # True
entre_1e10 = 1 < a <= 10                  # encadeamento de comparações -> True

expr_and1 = (0 and 5)                     # 0 (and devolve o primeiro falso)
expr_and2 = (3 and 4)                     # 4 (ambos “truthy”; devolve o último)
expr_or1 = (0 or 5)                       # 5 (or devolve o primeiro verdadeiro)
expr_or2 = ("" or "abc")                  # "abc" (string vazia é falso, "abc" é verdadeiro)

em_string = ("pi" in "python")            # False ("pi" não ocorre em "python")
em_lista = (2 in [1, 2, 3])               # True (2 está na lista)
em_dict_chaves = ("nome" in {"nome": "Ana", "idade": 16})  # True (verifica em CHAVES do dict)

x_ident = None                            # sentinel “sem valor”
e_none = (x_ident is None)                # True (is verifica identidade/mesmo objeto)

x_atrib = 10                              # valor inicial
x_atrib += 5                              # 15 (adição e atribuição)
x_atrib *= 2                              # 30 (multiplicação e atribuição)

prec_sem = 2 + 3 * 4                      # 14 (multiplicação antes da adição)
prec_com = (2 + 3) * 4                    # 20 (parênteses alteram a precedência)

soma_fp = 0.1 + 0.2                       # 0.30000000000000004 (limitações de ponto flutuante)
soma_fp_arred = round(soma_fp, 2)         # 0.3 (arredondado para apresentação)


# =============================================================================
# 8) ESTRUTURAS DE SELEÇÃO — if / elif / else
# -----------------------------------------------------------------------------
# - Escolha de caminhos com base em condições.
# - Valores “vazios” (0, "", [], {}, None) contam como False.
# =============================================================================

nota_exame = 15                           # valor para classificar
if nota_exame >= 18:                      # testa primeiro intervalo [18..20]
    conceito = "Excelente"                # ramo do if
elif nota_exame >= 14:                    # se falhar o if, testa [14..17]
    conceito = "Bom"                      # ramo do elif
elif nota_exame >= 10:                    # tenta [10..13]
    conceito = "Suficiente"               # ramo do elif
else:                                     # restante (<10)
    conceito = "Insuficiente"             # ramo do else

tem_nome = ""                             # string vazia é False em contexto booleano
tem_nome_msg = "Tem nome" if tem_nome else "String vazia é False"  # expressão condicional (ternário)


# =============================================================================
# 9) ESTRUTURAS DE REPETIÇÃO — while e for
# -----------------------------------------------------------------------------
# - while repete enquanto a condição for verdadeira (garante atualização/saída).
# - for percorre elementos de uma sequência (string, lista, range).
# - enumerate(seq) devolve pares (índice, valor).
# =============================================================================

i = 1                                     # contador para while
while i <= 3:                             # repete para i=1,2,3
    i = i + 1                             # atualiza i em cada iteração

texto_demo = "ABC"                        # string a percorrer
chars = []                                # lista onde vamos guardar os caracteres
for ch in texto_demo:                     # percorre cada caractere de "ABC"
    chars.append(ch)                      # adiciona 'A', depois 'B', depois 'C'

lista_demo = ["Ana", "Bruno", "Carla"]    # lista de nomes
indices_e_nomes = []                      # lista de pares (índice, nome)
for idx, nome_lista in enumerate(lista_demo):  # enumerate dá (índice, valor)
    indices_e_nomes.append((idx, nome_lista))  # guarda o par (0,"Ana"), (1,"Bruno"), (2,"Carla")


# =============================================================================
# 10) range() — GERADOR NUMÉRICO
# -----------------------------------------------------------------------------
# - range(fim)           → 0..fim-1
# - range(inicio, fim)   → inicio..fim-1
# - range(inicio, fim, passo) (passo pode ser negativo)
# - Usa range(len(lista)) para percorrer por índice quando precisares.
# =============================================================================

r1 = list(range(5))                       # [0,1,2,3,4]
r2 = list(range(2, 7))                    # [2,3,4,5,6]
r3 = list(range(10, 0, -2))               # [10,8,6,4,2]

nomes = ["Ana", "Bruno", "Carla"]         # lista para percorrer por índice
pares_indice_valor = []                   # vamos guardar (índice, valor)
for i_idx in range(len(nomes)):           # percorre índices 0..len(nomes)-1
    pares_indice_valor.append((i_idx, nomes[i_idx]))  # anexa (índice, elemento)

# =============================================================================
# 11) BLOCOS DE CÓDIGO E INDENTAÇÃO
# -----------------------------------------------------------------------------
# - Em Python, os blocos iniciam-se com ":" e são definidos pela INDENTAÇÃO.
# - Usa 4 espaços por nível de indentação (PEP 8). Não misturar tabs com espaços.
# - As linhas ao mesmo nível de indentação pertencem ao mesmo bloco.
# - Exemplos de blocos: if/elif/else, while, for.
# - Parênteses permitem partir linhas longas sem "\": soma = (a + b + c + d)
# =============================================================================

x = 12                                   # variável simples para exemplificar um if/else
if x > 10:                               # começa um bloco; a condição é avaliada como True/False
    mensagem = "maior que 10"            # linha INDENTADA (4 espaços) pertence ao bloco do if
else:                                     # ramo alternativo do bloco caso a condição seja False
    mensagem = "10 ou menos"             # também INDENTADA (4 espaços), dentro do bloco do else

contador = 0                             # contador para exemplificar um while
while contador < 3:                      # enquanto a condição for True, o corpo repete
    contador = contador + 1              # ATUALIZA o contador (evita ciclos infinitos)

nomes_demo = ["Ana", "Bruno", "Carla"]   # lista para percorrer com for
for pessoa in nomes_demo:                # for cria um bloco; percorre elemento a elemento
    saudacao = "Olá, " + pessoa          # linha INDENTADA pertence ao bloco do for



# =============================================================================
# 12) LISTAS — CRIAÇÃO, ACESSO E MÉTODOS
# -----------------------------------------------------------------------------
# - Listas são coleções ordenadas de elementos (qualquer tipo).
# - Cada elemento de uma lista tem um índice (0..n-1); índices negativos contam do fim (-1 é o último).
# - Podemos aceder, modificar, adicionar e remover elementos usando índices.
# - Por exemplo: print(l[0]) acede e mostra ao primeiro elemento.
# - Mutáveis; suportam indexação e slicing.
# - Métodos: append, extend, insert, pop, remove, clear, count, index, sort, reverse.
# - Funções: len, sum, min, max, sorted (esta não altera a original).
# - Cópia: l.copy() ou l[:] para não partilhar referência (shallow copy).
# =============================================================================

l = [3, 1, 4]                             # cria uma lista

print(l[0])                                # mostra o primeiro elemento (indice 0) -> 3
print(l[-1])                               # mostra o último elemento -> 4



l.append(1)                               # adiciona 1 no fim -> [3,1,4,1]
l.insert(1, 7)                            # coloca 7 no índice 1 -> [3,7,1,4,1,5,9]
ultimo = l.pop()                          # remove/devolve o último (9)
l.remove(1)                               # remove a PRIMEIRA ocorrência de 1 -> [3,7,4,1,5]
conta_uns = l.count(1)                    # conta quantos '1' há -> 1
idx_sete = l.index(7)                     # devolve o índice do 7 -> 1
l.sort()                                  # ordena in-place (crescente)
l.reverse()                               # inverte a ordem in-place

nums = [10, 20, 5, 15]                    # outra lista
len_nums = len(nums)                      # número de elementos -> 4
sum_nums = sum(nums)                      # soma -> 50
min_nums = min(nums)                      # mínimo -> 5
max_nums = max(nums)                      # máximo -> 20
nums_ordenados = sorted(nums)             # devolve NOVA lista ordenada (não altera nums)

# Percorrer lista com for
numeros = [2, 4, 6, 8]                     # lista de números
quadrados = []                             # lista onde guardaremos os quadrados
for n in numeros:                         # percorre cada número n na lista
    # o n vai ser cada um dos elementos: 2, depois 4, depois 6, depois 8
    quadrados.append(n ** 2)              # calcula o quadrado e adiciona à lista
# Agora, quadrados = [4, 16, 36, 64]


# =============================================================================
# 13) DICIONÁRIOS — CRIAÇÃO, ACESSO E MÉTODOS
# -----------------------------------------------------------------------------
# - Dicionários são coleções de pares chave:valor (sem ordem garantida).
# - Pares chave:valor; iteráveis por chaves/valores/pares (keys/values/items).
# - Acesso seguro: d.get("k", valor_por_defeito).
# - Alterar: atribuição direta ou update; remover: pop, del, popitem.
# =============================================================================

d = {                                     # cria dicionário com duas chaves
    "nome": "Ana", 
    "idade": 16
}         

# get - aceder com valor por defeito
nome_d = d.get("nome", "Desconhecido")    # acede a "nome" -> "Ana"
curso_d = d.get("curso", "Não definido")  # tenta aceder a "curso", não existe -> devolve "Não definido"


d["idade"] = 17                           # atualiza valor da chave "idade"
cidade_removida = d.pop("cidade")         # remove e devolve o valor em "cidade"
chaves = list(d.keys())                   # lista das chaves atuais
valores_d = list(d.values())              # lista dos valores atuais
pares = list(d.items())                   # lista de pares (chave, valor)

# Dicionário de exemplo: chaves são frutas; valores são preços em euros
precos = {"maçã": 0.79, "banana": 0.35, "pera": 1.05, "uva": 2.40}

# 1) Iterar pelas CHAVES (keys)
for fruta in precos.keys():                 # percorre cada chave do dicionário
    preco = precos[fruta]                   # acede ao valor correspondente à chave "fruta"
    print(fruta, "->", preco)               # imprime "maçã -> 0.79", etc.

# Nota: "for fruta in precos:" é equivalente a "for fruta in precos.keys():"
for fruta in precos:                         # forma curta, percorre chaves
    print("Chave:", fruta)                   # imprime apenas a chave

# 2) Iterar pelos VALORES (values)
total = 0.0                                  # acumulador para somar preços
for valor in precos.values():                # percorre apenas os valores do dicionário
    total += valor                           # acumula cada preço no total
media = total / len(precos)                  # calcula a média dos preços
print("Média:", round(media, 2))             # mostra a média arredondada a 2 casas

# 3) Iterar por PARES (items)
for fruta, valor in precos.items():          # percorre (chave, valor)
    print(f"{fruta} custa {valor:.2f} euros")  # imprime com formatação

# 4) Verificar existência de chave (membership)
existe_banana = ("banana" in precos.keys())  # True se "banana" for uma chave
# Dica: também funciona "banana" in precos (é o mesmo que in precos.keys())
existe_uva = ("uva" in precos)               # True se "uva" for chave

# 6) Filtrar usando keys() (ex.: Mostrar frutas com preço >= 1.00)
caras = []                                   # lista para guardar chaves filtradas
for fruta in precos.keys():                  # percorre chaves
    if precos[fruta] >= 1.00:                # testa condição no valor associado
        caras.append(fruta)                  # adiciona a fruta se cumprir
print("Caras:", caras)                       # ex.: ["pera","uva"]


# =============================================================================
# 14) ESTRUTURAS DE DADOS ANINHADAS
# -----------------------------------------------------------------------------
# - Lista de listas (matriz), dicionário de listas, lista de dicionários,
#   dicionário de dicionários.
# - Itera com loops aninhados e/ou enumerate conforme a estrutura.
# =============================================================================


# Lista de listas (matriz)
##################################
matriz = [                                # lista de listas (3x3)
    [1, 2, 3],                            # 1.ª linha
    [4, 5, 6],                            # 2.ª linha
    [7, 8, 9],                            # 3.ª linha
]
elem_2a_linha_3a_col = matriz[1][2]       # acesso por índice duplo -> 6
linhas = []                               
for linha in matriz:                      # percorre cada sublista
    linhas.append(linha)                  # acumula a linha (só para exemplo)

# Adicionar nova linha
nova_linha = [10, 11, 12]                 # nova linha a adicionar
matriz.append(nova_linha)                  # adiciona ao fim da matriz


# Dicionário com listas
##################################

turmas = {                                # dicionário de listas
    "10A": ["Ana", "Bruno", "Carla"],
    "10B": ["Diogo", "Eva", "Fábio"],
}
alunos_10A = turmas["10A"]                # acede à lista de alunos da turma 10A

# Percorrer dicionário de listas
for turma, alunos in turmas.items():      # percorre (chave, valor) Cada turma vai para a variável 'turma', a lista de alunos para 'alunos'
    print(f"Turma {turma}:")               # imprime o nome da turma
    for aluno in alunos:                   # percorre a lista de alunos
        print(" -", aluno)                 # imprime cada aluno

# Inserir novo aluno na turma 10B
turmas["10B"].append("Gabriela")          # adiciona "Gabriela" à lista da turma 10B

# Inserir nova turma
turmas["10C"] = ["Helena", "Igor"]        # cria nova entrada no dicionário


# Dicionário de dicionários
##################################

notas = {                                 # dicionário de dicionários
    "Ana": {"Matemática": 18, "Português": 16},
    "Bruno": {"Matemática": 14, "Português": 15},
}
nota_ana_matematica = notas["Ana"]["Matemática"]  # acede à nota de Matemática da Ana -> 18

# Percorrer dicionário de dicionários
for aluno, disciplinas in notas.items():   # percorre (aluno, dicionário de disciplinas)
    print(f"Notas de {aluno}:")            # imprime o nome do aluno
    # A variável 'disciplinas' é um dicionário com pares (disciplina, nota)
    # Vamos usar novo for para percorrer esse dicionário interno
    for disciplina, nota in disciplinas.items():  # percorre (disciplina, nota)
        print(f" - {disciplina}: {nota}")  # imprime cada disciplina e nota 

# Adicionar nova nota
notas["Ana"]["Inglês"] = 17                # adiciona nova disciplina e nota para Ana
notas["Bruno"]["Inglês"] = 14               # adiciona nova disciplina e nota para Bruno

# Adicionar novo aluno
notas["Carla"] = {"Matemática": 19, "Português": 18}  # cria nova entrada para Carla

# Calcular média de um aluno

aluno_alvo = input("Nome do aluno para média? ")  # lê nome do aluno
soma_notas = 0                            # acumulador para a soma das notas
num_disciplinas = 0                       # contador de disciplinas
for disciplina, nota in notas[aluno_alvo].items():  # percorre as disciplinas e notas do aluno
    soma_notas += nota                     # acumula a nota
    num_disciplinas += 1                  # incrementa o contador
media_aluno = soma_notas / num_disciplinas  # calcula a média
print(f"Média de {aluno_alvo}: {media_aluno:.2f}")  

# Lista de dicionários
##################################

alunos = [                                # lista de dicionários
    {"nome": "Ana", "idade": 16},
    {"nome": "Bruno", "idade": 17},
]
idade_bruno = alunos[1]["idade"]          # acede à idade do segundo aluno -> 17

# Percorrer lista de dicionários
for aluno in alunos:                      # percorre cada dicionário na lista
    nome_aluno = aluno["nome"]            # acede ao nome
    idade_aluno = aluno["idade"]          # acede à idade
    print(f"{nome_aluno} tem {idade_aluno} anos")  # imprime informação do aluno

# Adicionar novo aluno
novo_aluno = {"nome": "Carla", "idade": 16}  # cria novo dicionário
alunos.append(novo_aluno)                 # adiciona à lista    



# =============================================================================
# 15) BOAS PRÁTICAS RÁPIDAS
# -----------------------------------------------------------------------------
# - Usa 4 espaços por indentação; não misturar tabs com espaços.
# - Nomeia variáveis de forma clara (snake_case).
# - Comenta o “porquê” (intenção) mais do que o óbvio.
# - Valida input antes de converter para int/float.
# - Evita duplicação; procura padrões e extrai passos (mais tarde com funções).
# - Atenção à mutabilidade: listas/dicionários (mutáveis) vs strings/ints (imutáveis).
# - Testa com exemplos pequenos e vai aumentando a complexidade.
# =============================================================================
