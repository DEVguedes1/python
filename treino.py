# Questão 1 – Inverter String
# Enunciado:
# Dada uma string qualquer, inverta a ordem dos caracteres e retorne o resultado.

# O que precisa ser feito:
# Você precisa percorrer a string de trás para frente e construir uma nova string com os caracteres invertidos.

str_padrao= input("uma palavra:")

str_padrao=list(str_padrao)
str_padrao.reverse()
str_mod="".join(str_padrao)
print(str_mod)

# Questão 2 – Contar Vogais
# Enunciado:
# Dada uma string, conte quantas vogais (a, e, i, o, u – tanto maiúsculas quanto minúsculas) ela possui.

# O que precisa ser feito:
# Você deve percorrer todos os caracteres da string e verificar se cada um deles é uma vogal.
# Se for, incremente um contador.

vogais="aAeEiIoOuU"
cont=0
entrada=input("digite uma palavra:")
for i in entrada:
    if i in vogais:
        cont+=1
print(f"tem {cont} vogais na palavra")