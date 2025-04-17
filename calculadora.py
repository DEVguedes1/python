#usando o flet faremos uma calculadora
#terá introdução a GUI 
#pratica de logica
#interatividade real
#desing moderno
#base para apps maiores

import flet as ft #pega as coisas do app
from flet import colors #pega a função de cor
from decimal import Decimal

botao1 = [
    {"op":"AC","fonte":colors.BLACK,"fundo":colors.BLUE_100},
    {"op":"+/-","fonte":colors.BLACK,"fundo":colors.BLUE_100},
    {"op":"%","fonte":colors.BLACK,"fundo":colors.BLUE_100},
    {"op":"/","fonte":colors.WHITE,"fundo":colors.ORANGE},
    {"op":"7","fonte":colors.WHITE,"fundo":colors.WHITE24},
    {"op":"8","fonte":colors.WHITE,"fundo":colors.WHITE24},
    {"op":"9","fonte":colors.WHITE,"fundo":colors.WHITE24},
    {"op":"*","fonte":colors.WHITE,"fundo":colors.ORANGE},
    {"op":"4","fonte":colors.WHITE,"fundo":colors.WHITE24},
    {"op":"5","fonte":colors.WHITE,"fundo":colors.WHITE24},
    {"op":"6","fonte":colors.WHITE,"fundo":colors.WHITE24},
    {"op":"-","fonte":colors.WHITE,"fundo":colors.ORANGE},
    {"op":"1","fonte":colors.WHITE,"fundo":colors.WHITE24},
    {"op":"2","fonte":colors.WHITE,"fundo":colors.WHITE24},
    {"op":"3","fonte":colors.WHITE,"fundo":colors.WHITE24},
    {"op":"+","fonte":colors.WHITE,"fundo":colors.ORANGE},
    {"op":"0","fonte":colors.WHITE,"fundo":colors.WHITE24},
    {"op":",","fonte":colors.WHITE,"fundo":colors.WHITE24},
    {"op":"=","fonte":colors.WHITE,"fundo":colors.ORANGE},
    ]

def main(page:ft.Page):
    page.title = "calculadora"
    page.window_resizable = False#agua
    page.bgcolor = colors.GREY_300 #cor de fundo
    page.window_wight = 280
    page.window_height = 300
    page.window_always_on_top = True

    #resultado= ft.Text(value= '0' , color= colors.WHITE , size= 20)
    #tela onde ficara os numeros
    resultado = ft.TextField(
        value="0",
        border_color="#FFFFFF",
        color="#FFFFFF",
        read_only=True,
        text_size=30
    )

    def calculate(op,valor_atual):

        try:
            value=eval(valor_atual)
            if op == "%":
                value/=100
            elif op == "+/-":
                value = -value
        except:
            return "error"
        digits= min(abs(Decimal(value).as_tuple().exponent ), 5)
        return format(value, f".{digits}f")

    def select(e):
        value_atual = resultado.value if resultado.value not in ("0","error") else " "
        value = e.control.content.value
        if value.isdigit():
            value = value_atual + value
        elif value == 'AC':
            value = '0'
        else:
            if value_atual and value_atual[-1] in ('/','*','+', '-','.'):
                value_atual = value_atual[:-1]
                value = value_atual + value
            if value[-1] in ('=' , '%' , '+/-'):
                value = calculate(operador = value[-1], value_atual = value_atual)

        resultado.value = value
        resultado.update()

    display = ft.Row(
        width=250,
        controls=[resultado],
        alignment="end"
    )

    botao=[ft.Container(
        content=ft.Text(value=botao["op"],color=botao["fonte"]),
        bgcolor=botao["fundo"]if "fundo" in botao else botao.get("fundo", colors.BLUE_100),
        on_click=select,
        border_radius=100,
        height=50,
        width=50,
        alignment=ft.alignment.center
    )for botao in botao1]
    #hora de por os botões na tela

    keyboard=ft.Row(
        width=250,
        wrap=True,
        controls=botao,
        alignment="end"
    )
    page.add(display,keyboard)


ft.app(target=main)