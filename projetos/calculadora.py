#usando o flet faremos uma calculadora
#terá introdução a GUI 
#pratica de logica
#interatividade real
#desing moderno
#base para apps maiores

import flet as ft #pega as coisas do app
#função do app
def main(page: ft.Page):
    page.window.center()
    page.title="calculadora do demonio"
    page.window_height=450
    page.window_widht=270
    page.window.always_on_top=True
    page.window.resizable=True
    page.update()
#entrada de valores
    def entradas(e:ft.KeyboardEvent):
        print(e.key)
        if e.shift:
            match e.key:
                case "5":
                    return"%"
                case "8":
                    return"*"
                case "=":
                    return"+"
                case "-":
                    return"-"
                case "Enter":
                    return"="
                case ",":
                    return"."
        else:
            if e.key.isnumeric():
                return e.key
            match e.key:
                case ",":
                    return"."
                case "Numpad Multiply":
                    return"*"
                case "Numpad Add":
                    return"+"
                case "Numpad Subtract":
                    return"-"
                case "Numpad Divide":
                    return"/"
                case "Numpad Decimal":
                    return"."
                case "Numpad 1":
                    return"1"
                case "Numpad 2":
                    return"2"
                case "Numpad 3":
                    return"3"
                case "Numpad 4":
                    return"4"
                case "Numpad 5":
                    return"5"
                case "Numpad 6":
                    return"6"
                case "Numpad 7":
                    return"7"
                case "Numpad 8":
                    return"8" 
                case "Numpad 9":
                    return"9" 
                case "Numpad 0":
                    return"0" 
                case "Enter":
                    return"="
                case "-":
                    return"-"
                case "=":
                    return"="
                case"Backspace":
                    return"<"
    def tcinput(e):
        nonlocal novo, operador, num1
        data = entradas(e)  # Certifique-se que esta função está definida
    
        if not hasattr(resul, 'value'):  # Verifica se resul tem a propriedade value
            resul.value = "0"
    
        if data == "AC":
            resul.value = "0"
            operador = " "
            novo = True
            num1 = -1
        elif data == ".":
            if resul.value == "0" or novo:
                resul.value = "0."
                novo = False
            elif "." not in resul.value:
                resul.value += data
        elif data == "<":
            if len(resul.value) > 1:
                resul.value = resul.value[:-1]
            else:
                resul.value = "0"
                num1 = -1
                novo = True
        elif data == "+/-":
            if resul.value != "0":
                if "-" in resul.value:
                    resul.value = resul.value.replace("-", "")
                else:
                    resul.value = "-" + resul.value
        elif data.isdigit():  # Substitui valor(data) por verificação de dígito
            if resul.value == "0" or novo or operador == "=":
                resul.value = data
                novo = False
                if operador == "=":
                    operador = " "
            else:
                resul.value += data
    
        resul.update()  # Certifique-se que resul tem este método
#calculo
    def calc(num1,num2,operador):
        num1=format(num1)
        num2=format(num2)
        if operador=="+":
            resultado=num1+num2
            return format(resultado)
        elif operador=="-":
            resultado=num1-num2
            return format(resultado)
        elif operador=="*":
            resultado=num1*num2
            return format(resultado)
        elif operador=="%":
            resultado=(num1%100)*num2
            return format(resultado)
        elif operador=="/":
            if num2!=0:
                resultado=num1/num2
                return format(resultado)
            else:
                return 0
#interação
    def click(c):
        nonlocal novo, operador, num1  # Certifique-se que estas variáveis foram declaradas como nonlocal
    
        data = c.control.text
    
    # Função auxiliar para verificar se é número
        def is_number(n):
            try:
                float(n)
                return True
            except ValueError:
                return False
    
        if data == "AC":
        # Reset completo
            resul.value = "0"
            operador = ''
            novo = True
            num1 = None  # Melhor usar None do que -1 para indicar ausência de valor
    
        elif data == '.':
        # Tratamento do ponto decimal
            if novo:
                resul.value = "0."
                novo = False
            elif '.' not in resul.value:
                resul.value += data
    
        elif data == '<':
        # Backspace
            if len(resul.value) > 1:
                resul.value = resul.value[:-1]
            else:
                resul.value = "0"
                novo = True
    
        elif data == '+/-':
        # Troca de sinal
            if resul.value != "0":
                if '-' in resul.value:
                    resul.value = resul.value.replace('-', '')
                else:
                    resul.value = '-' + resul.value
    
        elif is_number(data):
        # Dígitos numéricos
            if resul.value == "0" or novo or operador == '=':
                resul.value = data
                novo = False
                if operador == '=':
                    operador = ''
            else:
                resul.value += data
    
        elif data in '+-*/':
        # Operadores
            if num1 is None:
                num1 = float(resul.value)
                operador = data
                novo = True
            else:
            # Calcula o resultado parcial se já houver uma operação pendente
                if operador:
                    resul.value = str(calc(num1, float(resul.value), operador))
                num1 = float(resul.value)
                operador = data
                novo = True
    
        elif data == '=':
        #  Cálculo final
            if num1 is not None and operador:
                resul.value = str(calc(num1, float(resul.value), operador))
            num1 = None
            operador = ''
            novo = True
    
        resul.update()  # Atualiza a interface

# Função de cálculo (precisa ser definida)
    def calc(val1, val2, operador):
        if operador == '+':
            return val1 + val2
        elif operador == '-':
            return val1 - val2
        elif operador == '*':
            return val1 * val2
        elif operador == '/':
            return val1 / val2 if val2 != 0 else float('nan')  # Trata divisão por zero
        return val2  # Retorna o segundo valor se não houver operador válido

    def valor(dt,i=False):
        if i:
            if dt in ('+','-','*','/','%','='):
                return True
        else:
            if dt in ('1','2','3','4','5','6','7','8','9','0'):
                return True
        return False
    def format(data):
        data = float(data)
        if data %1 ==0:
            return int(data)
        else:
            return float(data)
#variaveis
    novo = True
    operador = ''
    num1 = -1

    page.on_keyboard_event=tcinput
#butoes construção
    botoes_ac = [

        {"Valor": 'AC', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_500, "Forma": 2, "Comando": click},
        {"Valor": '%', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_500, "Forma": 2, "Comando": click},
        {"Valor": '<', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_500, "Forma": 2, "Comando": click},
        {"Valor": '+/-', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_500, "Forma": 2, "Comando": click}

    ]

    botoes_79 = [

        {"Valor": '7', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '8', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '9', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '/', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_ACCENT_400, "Comando": click},
    ]
    
    botoes_46 = [

        {"Valor": '4', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '5', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '6', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '*', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_ACCENT_400, "Comando": click},
    ]

    botoes_13 = [

        {"Valor": '1', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '2', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '3', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '-', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_ACCENT_400, "Comando": click},
    ]

    botoes_0 = [

        {"Valor": '.', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '0', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '=', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_500, "Comando": click},
        {"Valor": '+', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_ACCENT_400, "Comando": click},
    ]

        #Botões
    bts_ac = [ft.Container(
        content = ft.FloatingActionButton(text=bts_ac['Valor'], foreground_color=bts_ac['Cor'],
                                           bgcolor=bts_ac['Cor_de_fundo'], aspect_ratio=bts_ac['Forma'], on_click=bts_ac['Comando']),
        width=55,
        height=55,
        alignment=ft.alignment.center,
    )   for bts_ac in botoes_ac]

    bts_79 = [ft.Container(
        content=ft.FloatingActionButton(text=bts_79['Valor'], foreground_color=bts_79['Cor'],
                                         bgcolor=bts_79['Cor_de_fundo'], on_click=bts_79['Comando']),
        width=55,
        height=55,
    )   for bts_79 in botoes_79]

    bts_46 = [ft.Container(
        content=ft.FloatingActionButton(text=bts_46['Valor'], foreground_color=bts_46['Cor'],
                                         bgcolor=bts_46['Cor_de_fundo'], on_click=bts_46['Comando']),
        width=55,
        height=55,
    )   for bts_46 in botoes_46]

    bts_13 = [ft.Container(
        content=ft.FloatingActionButton(text=bts_13['Valor'], foreground_color=bts_13['Cor'],
                                         bgcolor=bts_13['Cor_de_fundo'], on_click=bts_13['Comando']),
        width=55,
        height=55,
    )   for bts_13 in botoes_13]

    bts_0 = [ft.Container(
        content=ft.FloatingActionButton(text=bts_0['Valor'], foreground_color=bts_0['Cor'],
                                         bgcolor=bts_0['Cor_de_fundo'], on_click=bts_0['Comando']),
        width=55,
        height=55,
    )   for bts_0 in botoes_0]

#botões desing
    bts_ac = [ft.Container(
        content = ft.FloatingActionButton(text=bts_ac['Valor'], foreground_color=bts_ac['Cor'],
                                           bgcolor=bts_ac['Cor_de_fundo'], aspect_ratio=bts_ac['Forma'], on_click=bts_ac['Comando']),
        width=55,
        height=55,
        alignment=ft.alignment.center,
    )   for bts_ac in botoes_ac]

    bts_79 = [ft.Container(
        content=ft.FloatingActionButton(text=bts_79['Valor'], foreground_color=bts_79['Cor'],
                                         bgcolor=bts_79['Cor_de_fundo'], on_click=bts_79['Comando']),
        width=55,
        height=55,
    )   for bts_79 in botoes_79]

    bts_46 = [ft.Container(
        content=ft.FloatingActionButton(text=bts_46['Valor'], foreground_color=bts_46['Cor'],
                                         bgcolor=bts_46['Cor_de_fundo'], on_click=bts_46['Comando']),
        width=55,
        height=55,
    )   for bts_46 in botoes_46]

    bts_13 = [ft.Container(
        content=ft.FloatingActionButton(text=bts_13['Valor'], foreground_color=bts_13['Cor'],
                                         bgcolor=bts_13['Cor_de_fundo'], on_click=bts_13['Comando']),
        width=55,
        height=55,
    )   for bts_13 in botoes_13]

    bts_0 = [ft.Container(
        content=ft.FloatingActionButton(text=bts_0['Valor'], foreground_color=bts_0['Cor'],
                                         bgcolor=bts_0['Cor_de_fundo'], on_click=bts_0['Comando']),
        width=55,
        height=55,
    )   for bts_0 in botoes_0]
#txt
    resul = ft.Text(
        value='0',
        size=40
    )
#linhas
    display = ft.Row(
        width=270,
        height=80,
        controls=[resul],
        alignment='end',
    )

    l_ac = ft.Row(
        controls=bts_ac,
        alignment=ft.alignment.center,
        spacing=5,
        height=30
    )
    
    l_79 = ft.Row(
        controls=bts_79,
        alignment=ft.alignment.center,
        spacing=5
    )
    
    l_46 = ft.Row(
        controls=bts_46,
        alignment=ft.alignment.center,
        spacing=5
    )
    
    l_13 = ft.Row(
        controls=bts_13,
        alignment=ft.alignment.center,
        spacing=5
    )
    
    l_0 = ft.Row(
        controls=bts_0,
        alignment=ft.alignment.center,
        spacing=5
    )


    page.add(display,l_ac,l_79,l_46,l_13, l_0)

ft.app(target=main)