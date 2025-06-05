
def hora_forma(*args):
    hora=hora_padrao[:2]
    if hora_padrao[2]==":":
        minuto=hora_padrao[2:]
    else:
        new_hora=hora_padrao.replace(hora_padrao[2], ":")
        minuto=new_hora[2:]
    if int(hora) > 12 and int(hora)<24:
        if minuto < 59 or minuto>00:
            hora_formatado=hora+minuto
        
        
    match hora_formatado[:1]:
        case 13:
            hora_formatado=hora_formatado.replace([1],horastuple[0])
        case 14:
            hora_formatado=hora_formatado.replace([1],horastuple[1])
        case 15:
            hora_formatado=hora_formatado.replace([1],horastuple[2])
        case 16:
            hora_formatado=hora_formatado.replace([1],horastuple[3])
        case 17:
            hora_formatado=hora_formatado.replace([1],horastuple[4])
        case 18:
            hora_formatado=hora_formatado.replace([1],horastuple[5])
        case 19:
            hora_formatado=hora_formatado.replace([1],horastuple[6])
        case 20:
            hora_formatado=hora_formatado.replace(hora_formatado[1],horastuple[7])
        case 21:
            hora_formatado=hora_formatado.replace(hora_formatado[1],horastuple[8])
        case 22:
            hora_formatado=hora_formatado.replace(hora_formatado[1],horastuple[9])
        case 23:
            hora_formatado=hora_formatado.replace(hora_formatado[1],horastuple[10])
        case 12:
            hora_formatado=hora_formatado.replace(hora_formatado[1],horastuple[-1])
        
    return f"{hora_formatado}"

horastuple=(1,2,3,4,5,6,7,8,9,10,11,12)
hora_padrao=input("digite a hora:")
print(hora_forma())

