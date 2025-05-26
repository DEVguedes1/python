# Resolução dos Exercícios sem usar funções (def)

## Exercício 1
nomes = ["Ana", "Bruno", "Amanda", "Bia", "Carlos"]
grupos = {}
for nome in nomes:
    inicial = nome[0].upper()  # Pega a primeira letra em maiúscula
    if inicial not in grupos:
        grupos[inicial] = []  # Cria nova lista se a letra não existir
    grupos[inicial].append(nome)  # Adiciona o nome ao grupo

resultado = []
letras_vistas = set()
for nome in nomes:
    inicial = nome[0].upper()
    if inicial not in letras_vistas:
        letras_vistas.add(inicial)
        resultado.append(tuple(grupos[inicial]))  # Converte lista para tupla

print(resultado)  # [("Ana", "Amanda"), ("Bruno", "Bia"), ("Carlos")]


# grupos = {}: Cria um dicionário vazio para armazenar os grupos.
# Loop for nome in nomes: Percorre cada nome na lista.
# inicial = nome[0].upper(): Pega a primeira letra do nome em maiúscula.
# if inicial not in grupos: Verifica se a letra já existe no dicionário.
# grupos[inicial].append(nome): Adiciona o nome ao grupo correspondente.
# letras_vistas: Conjunto para controlar letras já processadas.
# Segundo loop for nome in nomes: Garante a ordem de aparição.
# resultado.append(tuple(grupos[inicial])): Converte cada lista de nomes em tupla.

## Exercício 2
palavras = ["pé", "de", "péde", "bola", "futebol", "fute", "bol"]
conjunto_palavras = set(palavras)  # Para busca mais rápida
resultado = []

for palavra in palavras:
    for i in range(1, len(palavra)):
        parte1 = palavra[:i]
        parte2 = palavra[i:]
        if parte1 in conjunto_palavras and parte2 in conjunto_palavras:
            resultado.append(palavra)
            break  # Para não adicionar a mesma palavra várias vezes

print(resultado)  # ["péde", "futebol"]

# conjunto_palavras = set(palavras): Converte para conjunto para busca eficiente.
# Loop duplo:
# for palavra in palavras: Percorre cada palavra.
# for i in range(1, len(palavra)): Divide a palavra em todas as combinações possíveis.
# parte1 e parte2: Divide a palavra em duas partes.
# if parte1 in conjunto_palavras...: Verifica se ambas partes existem na lista original

## Exercício 3
frase = "hoje o dia está bonito e o dia está claro"
palavras = frase.split()
palavras_vistas = []
resultado = []

for palavra in palavras:
    if palavra in palavras_vistas:
        resultado.append(palavra + "*")
    else:
        resultado.append(palavra)
        palavras_vistas.append(palavra)

print(" ".join(resultado))  # "hoje o dia está* bonito e o dia* está* claro"

# palavras = frase.split(): Divide a frase em palavras.
# palavras_vistas = []: Lista para rastrear palavras já encontradas.
# Loop for palavra in palavras:
# Se a palavra já foi vista, adiciona *.
# Senão, adiciona à lista de palavras vistas.

## Exercício 4
lista = ["123.456.789-00", "111.222.333-44", "1234.567.890-12", "abc.def.ghi-jk"]
cpfs_validos = []

for item in lista:
    if len(item) == 14 and item[3] == '.' and item[7] == '.' and item[11] == '-':
        numeros = item.replace('.', '').replace('-', '')
        if numeros.isdigit() and len(numeros) == 11:
            cpfs_validos.append(item)

print(cpfs_validos)  # ["123.456.789-00", "111.222.333-44"]

# Verificação de formato:
# len(item) == 14: Tamanho correto.
# item[3] == '.': Verifica pontos e hífen nas posições certas.
# numeros = item.replace(...): Remove caracteres não numéricos.
# numeros.isdigit(): Confirma que só há dígitos.

## Exercício 5
frases = ["Organização Mundial da Saúde", "Banco Central"]
siglas = []

for frase in frases:
    palavras = frase.split()
    sigla = ''.join([palavra[0].upper() for palavra in palavras])
    siglas.append(sigla)

print(siglas)  # ["OMS", "BC"]

# frase.split(): Divide a frase em palavras.
# [palavra[0].upper()...]: Pega a primeira letra de cada palavra em maiúscula.
# ''.join(...): Junta as iniciais para formar a sigla.

## Exercício 6
palavras = ["casa", "arara", "bola", "python", "dado"]
vogais = {'a', 'e', 'i', 'o', 'u'}
resultado = []

for palavra in palavras:
    valida = True
    for i in range(len(palavra)-1):
        atual = palavra[i].lower()
        prox = palavra[i+1].lower()
        # Verifica se ambas são vogais ou ambas consoantes
        if (atual in vogais and prox in vogais) or (atual not in vogais and prox not in vogais):
            valida = False
            break
    if valida:
        resultado.append(palavra)

print(resultado)  # ["bola", "python", "dado"]

# vogais = {'a', 'e', 'i', 'o', 'u'}: Conjunto de vogais.
# Loop duplo:
# Verifica se caracteres adjacentes são ambos vogais ou consoantes.
# Se sim, marca a palavra como inválida.

## Exercício 7

strings = ["abc", "123", "a1b2", "!@#", "abc123"]
apenas_letras = []
apenas_numeros = []
alfanumericos = []

for item in strings:
    if item.isalpha():
        apenas_letras.append(item)
    elif item.isdigit():
        apenas_numeros.append(item)
    elif item.isalnum():
        alfanumericos.append(item)

print(apenas_letras)  # ["abc"]
print(apenas_numeros)  # ["123"]
print(alfanumericos)   # ["a1b2", "abc123"]

# isalpha(), isdigit(), isalnum():
# isalpha(): Verifica se tem apenas letras.
# isdigit(): Verifica se tem apenas números.
# isalnum(): Verifica se tem letras e números (sem símbolos).

## Exercício 8

frase = "vida longa ao rei"
palavras = frase.split()
resultado = []

for palavra in palavras:
    if len(palavra) % 2 == 0:
        resultado.append(palavra[::-1])  # Inverte a palavra
    else:
        resultado.append(palavra)

print(" ".join(resultado))  # "adiv agnol ao ier"

# len(palavra) % 2 == 0: Verifica se o comprimento é par.
# palavra[::-1]: Inverte a palavra usando slicing.

## Exercício 9
texto = "o rato roeu a roupa do rei de roma e o rato roeu tudo"
palavras = texto.lower().split()
unicas = []
repetidas = []

for palavra in palavras:
    if palavra in unicas:
        if palavra not in repetidas:
            repetidas.append(palavra)
    else:
        unicas.append(palavra)

print(repetidas)  # ["o", "rato", "roeu"]

# palavras = texto.lower().split(): Padroniza para minúsculas e divide.
# Duas listas:
# unicas: Armazena palavras vistas pela primeira vez.
# repetidas: Armazena palavras repetidas (sem duplicatas).

## Exercício 10

frase1 = "A vida é bela"
frase2 = "a vida é dura mas bela"
palavras1 = frase1.lower().split()
palavras2 = frase2.lower().split()

menor = min(len(palavras1), len(palavras2))
iguais = 0

for p1 in palavras1:
    if p1 in palavras2:
        iguais += 1

porcentagem = (iguais / menor) * 100
print(f"Similaridade: {porcentagem:.0f}%")  # Similaridade: 75%

# palavras1 e palavras2: Divide as frases em palavras (minúsculas).
# menor = min(...): Pega o tamanho da menor frase para cálculo.
# Contagem de palavras iguais:
# Incrementa iguais se uma palavra da frase1 existe na frase2.
# Cálculo da porcentagem: (iguais / menor) * 100.