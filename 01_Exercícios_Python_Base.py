# Exercícios de preparação para o teste de Python - 1º Teste 2025/2026
#
# Matéria abrangida:
# - Variáveis e operadores
# - Strings
# - Tipos de dados básicos: int, float, str, bool
# - Estruturas de seleção: if, elif, else
# - Estruturas de repetição: for, while
# - Listas e operações com listas
# - Dicionários e operações com dicionários
# - Estruturas aninhadas: listas de listas, dicionários de listas, dicionários de dicionários, listas de dicionários

# 1) Pede um número ao utilizador e, caso ele seja positivo, diz se é par.

# Resolução:
num = int(input("Introduza um número: "))
if num > 0:
    if num % 2 == 0:
        print("O número é positivo e par.")
    else:
        print("O número é positivo e ímpar.")


#2) Pede 3 números ao utilizador e, sem usar o min(), diz qual o menor.

# Resolução:
n1 = float(input("Introduza o primeiro número: "))
n2 = float(input("Introduza o segundo número: "))
n3 = float(input("Introduza o terceiro número: "))

menor = n1  # Assume que o primeiro é o menor
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print("O menor número é:", menor)

# Outra forma:

if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3
print("O menor número é:", menor)


#3) Lê um número nota (0–20) e imprime "Excelente" (≥18), "Bom" (14–17), "Suficiente" (10–13), "Insuficiente" (<10) usando if/else.

# Resolução:

nota = int(input("Introduza a nota (0-20): "))

if nota < 0 or nota > 20:
    print("Nota inválida. Introduza um valor entre 0 e 20.")
else:
    if nota >= 18:
        print("Excelente")
    elif nota >= 14:
        print("Bom")
    elif nota >= 10:
        print("Suficiente")
    else:
        print("Insuficiente")

#4) Pede um número ao utilizador e, caso ele seja maior do que 1, faz uma contagem decrescente desse número até 0.

# Resolução:
num = int(input("Introduza um número maior que 1: "))
if num > 1:
    for i in range(num, -1, -1):
        print(i)
else:
    print("Número inválido. Deve ser maior que 1.")

# Com o while:
num = int(input("Introduza um número maior que 1: "))
if num > 1:
    while num >= 0:
        print(num)
        num -= 1
else:
    print("Número inválido. Deve ser maior que 1.")

#5) Usa for para somar os números de 1 a 100. Repete com while.

# Resolução com for:
soma = 0
for i in range(1, 101):
    soma += i
print("A soma dos números de 1 a 100 é:", soma) 

# Resolução com while:
soma = 0
i = 1
while i <= 100:
    soma += i
    i += 1
print("A soma dos números de 1 a 100 é:", soma)

#6) Pede um número ao utilizador e diz a tabuada do 1 até 10 desse número.

# Resolução:
num = int(input("Introduza um número para ver a tabuada: "))
print(f"Tabuada do {num}:")
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")

#7) Cria uma lista com 5 números pedidos ao utilizador. Depois diz quais são positivos, negativos ou zero.

# Resolução:
numeros = []
for _ in range(5):
    n = float(input("Introduza um número: "))
    numeros.append(n)

# Análise dos números para positivos, negativos ou zero
for num in numeros:
    if num > 0:
        print(f"{num} é positivo.")
    elif num < 0:
        print(f"{num} é negativo.")
    else:
        print("O número é zero.")

#8) Cria uma lista com números à tua escolha. Depois mostra a lista, mostra o primeiro e o último elemento da lista.

# Resolução:
numeros = [10, -5, 0, 23, -8, 42]  # Lista de números à escolha
print("Lista completa:", numeros)
print("Primeiro elemento:", numeros[0])
print("Último elemento:", numeros[-1])  

#9) Pede 10 números ao utilizador e coloca-os numa lista. Sem usar o min e o max, calcula qual o maior e qual o menor número da lista.

# Resolução:
numeros = []
for _ in range(10):
    n = float(input("Introduza um número: "))
    numeros.append(n)

# Cálculo do maior e do menor número    
maior = numeros[0]
menor = numeros[0]
for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

#10) Pede uma string ao utilizador e depois conta quantas vogais tem a string.

# Resolução:
texto = input("Introduza uma string: ")
vogais = "aeiouAEIOU"
contador = 0
for char in texto:
    if char in vogais:
        contador += 1

#11) Cria um dicionário com as chaves nome, idade, profissao. Preenche os valores com dados à tua escolha. 
# Depois mostra a informação do dicionário de forma organizada.

# Resolução:
pessoa = {
    "nome": "Ana Silva",
    "idade": 28,
    "profissao": "Engenheira"
}  
print("Informação da Pessoa:")
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']} anos")
print(f"Profissão: {pessoa['profissao']}")

# Ou usando um for:
print("Informação da Pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

#12) Lê um número e diz se está entre 5 e 15  (inclusive).

# Resolução:
num = int(input("Introduza um número: "))
if num >= 5 and num <= 15:
    print(f"O número {num} está entre 5 e 15 (inclusive).")
else:
    print(f"O número {num} não está entre 5 e 15.")

#13) Pede dois números e indica se têm o mesmo sinal  (ambos ≥0 ou ambos <0).

# Resolução:
num1 = int(input("Introduza o primeiro número: "))
num2 = int(input("Introduza o segundo número: "))

if (num1 >= 0 and num2 >= 0) or (num1 < 0 and num2 < 0):
    print("Os dois números têm o mesmo sinal.")
else:
    print("Os dois números têm sinais diferentes.")

#14) Pede um número ao utilizador e calcula o somatório dos números de 1 até esse número (ou seja, 1 + 2 + ... + n).

# Resolução:
num = int(input("Introduza um número positivo: "))
if num > 0:
    somatorio = 0
    for i in range(1, num + 1):
        somatorio += i
    print(f"O somatório dos números de 1 até {num} é: {somatorio}")
else:
    print("Número inválido. Deve ser positivo.")

#15) Pede um número ao utilizador e, caso ele seja positivo e par, faz uma contagem decrescente desse número até 0.

# Resolução:
num = int(input("Introduza um número positivo e par: "))

if num > 0 and num % 2 == 0:
    for i in range(num, -1, -1):
        print(i)
else:
    print("Número inválido. Deve ser positivo e par.")

#

#16) Pede o nome, a idade e o peso ao utilizador. Caso a idade for entre 18 e 65 e o peso for superior a 50 kg, diz que a pessoa pode ser 
# dadora de sangue; caso contrário, diz que não pode.

# Resolução:
nome = input("Introduza o seu nome: ")
idade = int(input("Introduza a sua idade: "))
peso = float(input("Introduza o seu peso (kg): "))

if idade >= 18 and idade <= 65 and peso > 50:
    print(f"{nome}, você pode ser dador(a) de sangue.")
else:
    print(f"{nome}, você não pode ser dador(a) de sangue.")

#17) Pede 10 números ao utilizador e coloca-os numa lista. Depois cria uma nova lista apenas com os números pares da lista original e 
# mostra essa nova lista.

# Resolução:
numeros = []
for _ in range(10):
    n = int(input("Introduza um número: "))
    numeros.append(n)

pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
print("Números pares da lista original:", pares)

#18) Gera um número aleatório; o utilizador tenta adivinhar e o programa diz "maior/menor" até acertar; conta as tentativas e 
# não permitas mais do que 5 tentativas.

# Resolução:
import random

numero_aleatorio = random.randint(1, 100)  # Número aleatório entre 1 e 100
tentativas = 0
max_tentativas = 5

while tentativas < max_tentativas:
    palpite = int(input("Adivinhe o número (entre 1 e 100): "))
    tentativas += 1

    if palpite < numero_aleatorio:
        print("Maior!")
    elif palpite > numero_aleatorio:
        print("Menor!")
    else:
        print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
        break
else:
    print(f"Você não conseguiu adivinhar o número. O número era {numero_aleatorio}.")

#19) Lê uma nota entra 0 e 200  e converte para escala 0-20  (arredonda ao inteiro mais próximo), depois imprime se passou ou não. 

#20) Considera o dicionário que mostra restaurantes num festival de comida.
#bancas = {
#    "TacoTron":   {"vendas": 184, "preco_medio": 6.5, "avaliacao": 4.6},
#    "Bao&Buns":   {"vendas": 149, "preco_medio": 7.0, "avaliacao": 4.8},
#    "PokeWave":   {"vendas": 132, "preco_medio": 9.0, "avaliacao": 4.2},
#    "PastelPower":{"vendas": 210, "preco_medio": 2.0, "avaliacao": 4.9},
#    "VeggieVolt": {"vendas": 98,  "preco_medio": 8.5, "avaliacao": 4.4}
#}

# 20.1) Diz qual o restaurante com melhor avaliação.

# Resolução:

bancas = {
    "TacoTron":   {"vendas": 184, "preco_medio": 6.5, "avaliacao": 4.6},
    "Bao&Buns":   {"vendas": 149, "preco_medio": 7.0, "avaliacao": 4.8},
    "PokeWave":   {"vendas": 132, "preco_medio": 9.0, "avaliacao": 4.2},
    "PastelPower":{"vendas": 210, "preco_medio": 2.0, "avaliacao": 4.9},
    "VeggieVolt": {"vendas": 98,  "preco_medio": 8.5, "avaliacao": 4.4}
}
melhor_restaurante = ""
melhor_avaliacao = 0.0

for restaurante, info in bancas.items():
    if info["avaliacao"] > melhor_avaliacao:
        melhor_avaliacao = info["avaliacao"]
        melhor_restaurante = restaurante

print(f"O restaurante com melhor avaliação é {melhor_restaurante} com uma avaliação de {melhor_avaliacao}.")


# 20.2) Diz qual o restaurante que fez mais dinheiro.

# Resolução:

mais_rentavel = ""
maior_lucro = 0.0

for restaurante, info in bancas.items():
    lucro = info["vendas"] * info["preco_medio"]
    if lucro > maior_lucro:
        maior_lucro = lucro
        mais_rentavel = restaurante

print(f"O restaurante que fez mais dinheiro é {mais_rentavel} com um lucro de {maior_lucro} euros.")


#21) Cria uma lista de listas (matriz) 3x3 com números à tua escolha. 
# Mostra a matriz linha a linha. 
# Adiciona uma nova linha à matriz e mostra a matriz atualizada.

# Resolução:

matriz = [                                # lista de listas (3x3)
    [1, 2, 3],                            # 1.ª linha
    [4, 5, 6],                            # 2.ª linha
    [7, 8, 9]                             # 3.ª linha
]

print("Matriz original:")
for linha in matriz:                      # percorre cada sublista
    print(linha)                          # mostra a linha

# Adicionar nova linha
nova_linha = [10, 11, 12]                 # nova linha a adicionar
matriz.append(nova_linha)                  # adiciona ao fim da matriz  

print("Matriz atualizada:")
for linha in matriz:
    print(linha)    

#22) Cria um programa que gere um lista de livros. Cada livro deve ter um título, um autor, um ano de publicação e um género.

#22.1)  Mostra todos os livros de forma organizada.

# Resolução:
livros = [
    {"título": "1984", "autor": "George Orwell", "ano": 1949, "género": "Distopia"},
    {"título": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954, "género": "Fantasia"},
    {"título": "Dom Quixote", "autor": "Miguel de Cervantes", "ano": 1605, "género": "Clássico"},
    {"título": "A Menina que Roubava Livros", "autor": "Markus Zusak", "ano": 2005, "género": "Ficção Histórica"}
]

# Mostra todos os livros de forma organizada
print("Lista de Livros:")
for livro in livros:
    print(f"Título: {livro['título']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Género: {livro['género']}")

# Ou, usando um loop aninhado:
print("Lista de Livros:")
for livro in livros:
    for chave, valor in livro.items():
        print(f"{chave}: {valor}")
    print()  # linha em branco entre livros


#22.2) Pede um livro ao utilizador e, caso ele exista na lista, mostra a sua informação completa; caso contrário, diz que o livro não foi encontrado.

# Resolução:
titulo_procurado = input("Introduza o título do livro que procura: ")
for livro in livros:
    if livro["título"].lower() == titulo_procurado.lower(): # o .lower() torna a comparação case-insensitive ou seja, não diferencia maiúsculas de minúsculas
        print(f"Livro encontrado: Título: {livro['título']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Género: {livro['género']}")
        break
else:
    print("Livro não encontrado na lista.")

#23) Cria um dicionário de listas onde as chaves são nomes de turmas (ex: "10A", "10B") e os valores são listas com nomes de alunos.
# Mostra a lista de alunos de cada turma.
# Adiciona uma nova turma com alunos e mostra o dicionário atualizado.

turmas = {                                # dicionário de listas
    "10A": ["Ana", "Bruno", "Carla"],
    "10B": ["David", "Eva", "Fábio"]
}
for turma, alunos in turmas.items():      # percorre cada par chave-valor
    print(f"Turma {turma}: {alunos}")      # mostra a turma e a lista de alunos 

# Inserir nova turma
turmas["10C"] = ["Helena", "Igor"]        # cria nova entrada no dicionário

print("Dicionário de turmas atualizado:")
for turma, alunos in turmas.items():
    print(f"Turma {turma}: {alunos}")


# 24) Cria um programa que, usando listas, gere as temperaturas médias mensais de uma cidade ao longo de um ano.
# O programa deve permitir:
# - Consultar a temperatura média de um mês específico.
# - Calcular a temperatura média anual.
# - Identificar o mês mais quente e o mês mais frio.

# Resolução:
temperaturas = [15.5, 16.0, 18.2, 20.1, 22.5, 25.0, 27.3, 26.8, 24.0, 20.5, 17.8, 15.2]  # Temperaturas médias mensais
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"] 

# Consultar a temperatura média de um mês específico
mes_procurado = int(input("Introduza o número do mês (1-12) para consultar a temperatura média: "))
if 1 <= mes_procurado <= 12:
    print(f"A temperatura média em {meses[mes_procurado - 1]} é {temperaturas[mes_procurado - 1]} °C.")
    # Colocamos mes_procurado - 1 porque as listas em Python são indexadas a partir do 0.
    # Se o uilizador introduzir 1 (Janeiro), queremos aceder ao índice 0 da lista, pois é aí que está a temperatura de Janeiro.
else:
    print("Mês inválido. Deve ser entre 1 e 12.")

# Calcular a temperatura média anual
media_anual = sum(temperaturas) / len(temperaturas)
print(f"A temperatura média anual é {media_anual:.2f} °C.")

# Identificar o mês mais quente e o mês mais frio
mes_mais_quente = temperaturas.index(max(temperaturas))
mes_mais_frio = temperaturas.index(min(temperaturas))
print(f"O mês mais quente é {meses[mes_mais_quente]} com {temperaturas[mes_mais_quente]} °C.")
print(f"O mês mais frio é {meses[mes_mais_frio]} com {temperaturas[mes_mais_frio]} °C.")

# Sem usar o max() e o min():
mais_quente = temperaturas[0]
mais_frio = temperaturas[0]
indice_quente = 0
indice_frio = 0
for i in range(len(temperaturas)):
    if temperaturas[i] > mais_quente:
        mais_quente = temperaturas[i]
        indice_quente = i
    if temperaturas[i] < mais_frio:
        mais_frio = temperaturas[i]
        indice_frio = i

print(f"O mês mais quente é {meses[indice_quente]} com {mais_quente} °C.")
print(f"O mês mais frio é {meses[indice_frio]} com {mais_frio} °C.")


#25) Expande o exercício anterior de forma a que o dicionário contenha a seguinte informação:
# - Chave: turma (ex: "10A")
# - Valor: dicionário com as chaves:
#   - "alunos": lista de dicionários em que cada dicionário representa um aluno com as chaves "nome" e "notas" (dicionário com 
#       disciplinas (chave) e respetivas notas (valor)).
#   - "professor": nome do professor da turma.

# Resolução:
turmas = {
    "10A": {
        "alunos": [
            {"nome": "Ana", "notas": {"Matemática": 18, "Português": 16}},
            {"nome": "Bruno", "notas": {"Matemática": 14, "Português": 15}},
            {"nome": "Carla", "notas": {"Matemática": 12, "Português": 14}}
        ],
        "professor": "Sr. Silva"
    },
    "10B": {
        "alunos": [
            {"nome": "David", "notas": {"Matemática": 10, "Português": 12}},
            {"nome": "Eva", "notas": {"Matemática": 9, "Português": 11}},
            {"nome": "Fábio", "notas": {"Matemática": 15, "Português": 14}}
        ],
        "professor": "Sra. Costa"
    }
}

# 23.1) Mostra a lista de alunos com as respetivas notas de cada turma.

# Resolução:
for turma, info in turmas.items():
    print(f"Turma {turma}:")
    for aluno in info["alunos"]:
        nome = aluno["nome"]
        notas = aluno["notas"]
        print(f"  Aluno: {nome}, Notas: {notas}")
    print()

# 23.2) Diz quantos alunos têm pelo menos uma negativa (nota < 10) em cada turma.

# Resolução:
for turma, info in turmas.items():
    count_negativas = 0
    for aluno in info["alunos"]:
        for nota in aluno["notas"].values():
            if nota < 10:
                count_negativas += 1
                break  # Conta o aluno apenas uma vez

    print(f"Turma {turma} tem {count_negativas} alunos com pelo menos uma negativa.") 

# 23.3) Diz qual o professor de cada turma.

# Resolução:
for turma, info in turmas.items():
    professor = info["professor"]
    print(f"O professor da turma {turma} é {professor}.")

# 23.4) Pede um nome de um aluno e diz em que turma está e quais as suas notas.

# Resolução:
nome_procurado = input("Introduza o nome do aluno que procura: ")
for turma, info in turmas.items():
    for aluno in info["alunos"]:
        if aluno["nome"].lower() == nome_procurado.lower():
            notas = aluno["notas"]
            print(f"O aluno {nome_procurado} está na turma {turma} com as seguintes notas: {notas}")
            break
    else:
        continue  # Continua se o aluno não foi encontrado nesta turma
    break  # Sai do loop se o aluno foi encontrado
