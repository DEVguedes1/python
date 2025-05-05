# . Dada uma lista com elementos repetidos, crie uma nova lista que contenha apenas os elementos únicos,
#  mantendo a ordem original.
lista_repetida=[45,15,47,86,15,86,86,45,47]
lista_normal=[]
for n in lista_repetida:
    if n not in lista_normal:
        lista_normal.append(n)
print(lista_normal)

# #  A partir de uma lista de inteiros, crie outra contendo apenas os quadrados dos números pares.
lista_inteiros=[48,26,59,88,15,47,12,35]
quadrados=[]
for p in lista_inteiros:
    if p % 2 == 0:
        quadrado=p**2
        quadrados.append(quadrado)
print(quadrados)

#  Escreva uma função que receba uma lista de números do usuário
#  e retorne o segundo maior valor da lista sem usar max() duas vezes.
num_user=list()
for _ in range(5):

    try:
        valor=int(input("digite um numero aqui =>"))
        num_user.append(valor)
       
    except ValueError:
       print("apenas numeros")
    
num_user.sort()
print(num_user[-2])

# Crie duas listas, que podem ter o mesmo tamanho ou tamanhos diferentes e,
#  a partir delas, cria uma terceira lista intercalando os valores.
p1lista=[458,15,2478,3694,125,12]
p2lista=[15,468,7615,48]

conj_de_listas= p1lista+p2lista
print(conj_de_listas)

# Transforme uma lista de listas em uma lista única.
lista = [[1, 2], [3, 4], [5]]
ultima_lista=lista[0]+lista[1]+lista[2]
print(ultima_lista)

# Receba uma lista com as notas dos alunos de uma turma. 
# Crie uma nova lista contendo apenas as notas dos alunos aprovados (nota ≥ 7) e calcule a média das notas aprovadas.
ListaDeNota=[]
for _ in range(4):
    try:
        nota=int(input("digite um numero aqui =>"))
        ListaDeNota.append(nota)
    except ValueError:
       print("apenas numeros")
passou=[]
reprovados=[]
for nota in ListaDeNota:
    if nota >=7:
        passou.append(nota)
    else:
        reprovados.append(nota<7)
print(passou)

# Cada atleta faz 5 saltos, armazenados em uma lista. Escreva um programa que leia os 5 saltos de um atleta, 
# descarte o melhor e o pior, e calcule a média dos 3 saltos restantes.
totalsaltos=[]
for _ in range(5):
    try:
        saltos=int(input("salto do atleta =>"))
        totalsaltos.append(saltos)
    except ValueError:
       print("formato inválido")
saltordem=totalsaltos.copy()
saltordem.sort()
saltordem.pop(-1)
saltordem.pop(0)
saltomedia=sum(saltordem)/len(saltordem)
print(saltordem,"media:",saltomedia)

# Dadas duas listas A e B, escreva uma função que verifique se B aparece como uma sublista contínua dentro de A.
listaprincipal=list()
for _ in range(5):
    try:
        num1=int(input("digite um numero aqui =>"))
        listaprincipal.append(num1)
    except ValueError:
       print("apenas numeros")
valorverificar = []
contador = 0
while contador < 5:
    entrada = input("Digite o número a pesquisar aqui (ou X para sair) => ")
    if entrada.upper() == 'X':
        print("Saindo do programa...")
        break
    try:
        num2 = int(entrada)
        valorverificar.append(num2)
        contador += 1
        print("Pressione X para sair")
    except ValueError:
        print("Apenas números são permitidos!")
if len(valorverificar) == 0:
    print("segunda lista não é sublista de lista principal (segunda lista é vazia)")
elif len(valorverificar) > len(listaprincipal):
    print("segunda lista não é sublista de lista principal (segunda lista é maior que lista principal)")
else:
    encontrou = False
    for i in range(len(listaprincipal) - len(valorverificar) + 1):
        todos_iguais = True
        for j in range(len(valorverificar)):
            if listaprincipal[i + j] != valorverificar[j]:
                todos_iguais = False
                break
        if todos_iguais:
            encontrou = True
            break
    if encontrou:
        print(True)
    else:
        print(False)

# Dada uma lista de produtos comprados por um usuário (strings) e uma lista de produtos populares,
# escreva uma função que retorne os produtos populares que o usuário ainda não comprou, como sugestão.
comprados = ["Arroz 5kg", "Feijão 1kg", "Açúcar 1kg", "Sal 1kg"]
populares = [
    "Arroz 5kg", "Feijão 1kg", "Óleo de Soja 900ml", 
    "Café 500g", "Leite em Pó 400g", "Macarrão 500g",
    "Açúcar 1kg", "Sabão em Pó 1kg"
]
sugestoes = []
for produto in populares:
    if produto not in comprados:
        sugestoes.append(produto)
print("=== SUGESTÕES DE PRODUTOS POPULARES ===")
print("Você ainda não comprou estes itens populares:")
for i, item in enumerate(sugestoes, 1):
    print(f"{i}. {item}")
print(f"\nTotal de sugestões: {len(sugestoes)}")
  