# 1. Faça um programa em Python que gerencie notas de alunos em uma disciplina,
# utilizando uma tupla imutável como base de armazenamento. O menu deve conter:

# 1. Adicionar Nota (10 pontos)
# 2. Listar Notas (20 pontos)
# 3. Média das Notas (10 pontos)
# 4. Maior e Menor Nota (10 pontos)
# 5. Notas Acima da Média (20 pontos)
# 6. Buscar Nota Específica (10 pontos)
# 7. Remover Nota (10 pontos)
# 8. Sair

# O programa deve armazenar as notas como float.

# Use uma lista temporária para simular a mutabilidade da tupla (adicionar/remover elementos) e 
# reconverta a estrutura a cada operação.

# Ao listar as notas, imprima uma a uma.

# A busca por nota (opção 6) deve indicar se a nota informada existe e sua posição.

# A opção 5 deve calcular a média e exibir somente as notas estritamente acima dela.

notas_tuple=()
while True:
    print("="*50)
    print("""
1. Adicionar Nota (10 pontos)
2. Listar Notas (20 pontos)
3. Média das Notas (10 pontos)
4. Maior e Menor Nota (10 pontos)
5. Notas Acima da Média (20 pontos)
6. Buscar Nota Específica (10 pontos)   
7. Remover Nota (10 pontos)
8. Sair""")
    action=int(input("=>"))

    if action == 1:
            try:
                notas=float(input(f"\ndigite a nota:"))
                notas_temp=list(notas_tuple)
                notas_temp.append(notas)
                notas_tuple=tuple(notas_temp)
            except ValueError:
                print("ERRO: apenas numeros") 
    elif action == 2:
        if len(notas_tuple)==0:
            print("vazio")
        else:
            print("-"*50)
            print("NOTAS")
            print("-"*50)
            i = 0
            while i < len(notas_tuple):
                print(f"Nota {i+1}: {notas_tuple[i]:.2f}")
                i += 1
    elif action == 3:
        if len(notas_tuple)==0 or len(notas_tuple)==1:
            print("quantidade insuficiente")
        else:
            media=sum(notas_tuple)/len(notas_tuple)
            print("="*50)
            print("MÉDIA DAS NOTAS")
            print("-"*50)
            print(f"{media:.2f}")
    elif action == 4:
        if len(notas_tuple)>1:
            maior=max(notas_tuple)
            menor=min(notas_tuple)
            print(f"maior nota:{maior:.2f}")
            print(f"menor nota:{menor:.2f}")
        else:
            print("quantidade insuficiente")
    elif action == 5:
        if not notas_tuple:
            print("vazio")
        else:
            media=sum(notas_tuple)/len(notas_tuple)
            maiores_media=[]
            for n in notas_tuple:
                if n >media:
                    maiores_media.append(n)
                else:
                    for nota in maiores_media:
                        print(f"{nota:.2f}")
    elif action == 6:
        if not notas_tuple:
            print("vazio")
        else:
            try:
                busca = float(input("procure a nota: "))
                posicoes = []
                for i, nota in enumerate(notas_tuple, 1):
                    if nota == busca:
                        posicoes.append(i)
                if posicoes:
                    print(f"Nota {busca:.2f} encontrada na posição:", end=" ")
                    for idx, pos in enumerate(posicoes):
                        if idx == len(posicoes) - 1: 
                            print(pos)
                        else:
                            print(pos, end=", ")
                else:
                    print(f"Nota {busca:.2f} não encontrada.")
            except ValueError:
                print("Erro: Por favor, digite um número válido.")
    elif action == 7:
        if not notas_tuple:
            print("vazio")
        else:
            try:
                nota_excluida=float(input(f"\ndigite a nota:"))
                if nota_excluida in notas_tuple:
                    notas_temp=list(notas_tuple)
                    notas_temp.remove(notas)
                    notas_tuple=tuple(notas_temp)
                    print(f"Nota {nota_excluida:.2f} removida!")
            except ValueError:
                print("ERRO: apenas numeros") 
    elif action == 8:
        print("saindo...")
        break
    else :
        print("forma invalida!!")