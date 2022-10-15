from tkinter import *
from tkinter.font import Font

def intro():
    pass

def matriz_p():
    pass

def matriz_ti():
    pass

def matriz_ts():
    pass

def outcome():
    pass
def insert_function():
    pass

def bisec(): 
    pass

def secante():
    pass

def exit():
    quit()

root = Tk()
root.title("Proyecto 1")
root.geometry("530x300")

my_menu = Menu(root)
root.config(menu=my_menu)

titlefont = Font(family= "Georgia", size= 42, slant="italic")
normalfont = Font(family= "Geogia", size= 10)

doolitle_menu = Menu(my_menu)
roots_menu = Menu(my_menu)
my_menu.add_command(label = "Presentacion", command= intro)
my_menu.add_cascade(label = "Metodo Doolitle", menu= doolitle_menu)
doolitle_menu.add_command(label= "Matriz Principal", command= matriz_p)
doolitle_menu.add_command(label= "Matriz Triangular Inferior", command= matriz_ti)
doolitle_menu.add_command(label= "Matriz Triangular Superior", command= matriz_ts)
doolitle_menu.add_command(label= "Resultado del sistema de ecuaciones", command= outcome)
my_menu.add_cascade(label = "Metodos para Calcular Raices", menu= roots_menu)
roots_menu.add_command(label = "Insertar Funcion Polinomica", command= insert_function)
roots_menu.add_command(label = "Metodo Cerrado Biseccion", command= bisec)
roots_menu.add_command(label = "Metodo Abierto de la Secante", command= secante)
my_menu.add_command(label= "Salir", command= exit)

title = Label(text= "Bienvenido", font= titlefont)
title.pack()

topic = Label(text= "Este programa realiza Sistemas de Ecuaciones Algebraicas Lineales \ny Raices Reales de Funciones Algebraicas. Hecho por:",
        font= normalfont)
topic.pack()

names = Label(text= "- David Torres  8-963-282\n- Mark Bryan 20-14-7194", font= normalfont)
names.pack()

root.mainloop()