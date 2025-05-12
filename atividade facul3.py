# 2. Crie um programa em Python que controle os preços de produtos em uma loja virtual,
# usando uma tupla para armazenar os preços. O menu deve conter:

# 1. Cadastrar Preço de Produto (10 pontos)
# 2. Listar Todos os Preços (20 pontos)
# 3. Valor Total em Estoque (10 pontos)
# 4. Preço Médio (10 pontos)
# 5. Produto Mais Barato e Mais Caro (20 pontos)
# 6. Contar Preços Abaixo de X (10 pontos)
# 7. Remover um Preço (10 pontos)
# 8. Sair

# Os valores devem ser do tipo float, representando o preço de cada item.

# Na opção 6, o usuário informa um valor X, e o sistema deve contar quantos preços estão abaixo dele.

# A opção 7 deve pedir um valor exato e removê-lo, se existir (caso contrário, mostrar mensagem de erro).

# Sempre que um dado for alterado, a tupla original deve ser atualizada com a nova versão imutável da lista temporária.


precos = []

while True:
    print("\n=== MENU DE OPÇÕES ===")
    print("1. Adicionar preço")
    print("2. Ver todos os preços")
    print("3. Calcular valor total")
    print("4. Calcular preço médio")
    print("5. Mostrar menor e maior preço")
    print("6. Contar preços abaixo de um valor")
    print("7. Remover preço")
    print("8. Sair")
    
    opcao = input("Escolha uma opção (1-8): ")
    if opcao == '1':
        try:
            novo_preco = float(input("Digite o preço do produto: "))
            precos.append(novo_preco)
            print(f"Preço R${novo_preco:.2f} adicionado com sucesso!")
        except:
            print("Erro: Digite um valor numérico válido")
    elif opcao == '2':
        if len(precos) == 0:
            print("Nenhum preço cadastrado ainda.")
        else:
            print("\nLISTA DE PREÇOS:")
            for i, preco in enumerate(precos, 1):
                print(f"{i}. R${preco:.2f}")
    elif opcao == '3':
        total = sum(precos)
        print(f"Valor total em estoque: R${total:.2f}")
    elif opcao == '4':
        if len(precos) > 0:
            media = sum(precos) / len(precos)
            print(f"Preço médio: R${media:.2f}")
        else:
            print("Não há preços cadastrados para calcular a média.")
    elif opcao == '5':
        if len(precos) > 0:
            print(f"Produto mais barato: R${min(precos):.2f}")
            print(f"Produto mais caro: R${max(precos):.2f}")
        else:
            print("Não há preços cadastrados.")
    elif opcao == '6':
        if len(precos) > 0:
            try:
                valor = float(input("Digite o valor de comparação: "))
                quantidade = len([p for p in precos if p < valor])
                print(f"Existem {quantidade} preços abaixo de R${valor:.2f}")
            except:
                print("Valor inválido! Digite um número.")
        else:
            print("Não há preços cadastrados.")
    elif opcao == '7':
        if len(precos) > 0:
            try:
                remover = float(input("Digite o preço exato que deseja remover: "))
                if remover in precos:
                    precos.remove(remover)
                    print(f"Preço R${remover:.2f} removido com sucesso!")
                else:
                    print("Este preço não existe na lista.")
            except:
                print("Valor inválido! Digite um número.")
        else:
            print("Não há preços para remover.")
    elif opcao == '8':
        print("Obrigado por usar o programa! Até mais!")
        break
    else:
        print("Opção inválida! Digite um número de 1 a 8.")
    precos_tuple = tuple(precos)