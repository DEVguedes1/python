#jogo da velha usando tkinter
#treino de python e GUI
from tkinter import *
import random
from PIL import Image,ImageDraw, ImageTk

useriicial= 1
jogadores=1
quad=[0,0,0,0,0,0,0,0,0]

tela=Tk()
tela.title("game of the older")
tela.resizable(False,False)

