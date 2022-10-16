from tkinter import *
from tkinter.font import Font

def clear_frame():
    for widgets in frame.winfo_children():
      widgets.destroy()

def create_menu():
    my_menu = Menu(frame)
    root.config(menu=my_menu)

    doolitle_menu = Menu(my_menu)
    roots_menu = Menu(my_menu)
    my_menu.add_command(label = "Presentacion", command= intro)
    my_menu.add_cascade(label = "Metodo Doolitle", menu= doolitle_menu)
    doolitle_menu.add_command(label= "Matriz Principal", command= matrix_p)
    doolitle_menu.add_command(label= "Matriz Triangular Inferior", command= matrix_ti)
    doolitle_menu.add_command(label= "Matriz Triangular Superior", command= matrix_ts)
    doolitle_menu.add_command(label= "Resultado del sistema de ecuaciones", command= outcome)
    my_menu.add_cascade(label = "Metodos para Calcular Raices", menu= roots_menu)
    roots_menu.add_command(label = "Insertar Funcion Polinomica", command= insert_function)
    roots_menu.add_command(label = "Metodo Cerrado Biseccion", command= bisec)
    roots_menu.add_command(label = "Metodo Abierto de la Secante", command= secante)
    my_menu.add_command(label= "Salir", command= root.destroy)

def intro():
    clear_frame()
    create_menu()

    title = Label(frame, text= "Bienvenido", font= titlefont)
    title.pack()

    topic = Label(frame, text= "Este programa realiza Sistemas de Ecuaciones Algebraicas Lineales \ny Raices Reales de Funciones Algebraicas. Hecho por:",
        font= normalfont)
    topic.pack()

    names = Label(frame, text= "- David Torres  8-963-282\n- Mark Bryan 20-14-7194", font= normalfont)
    names.pack()

def matrix_p():
    A = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    B = [[0],
         [0],
         [0]]
    
    clear_frame()
    create_menu()

    entry_1_1 = Entry(frame, width= 5)
    entry_1_1.pack()

    entry_1_2 = Entry(frame, width= 5)
    entry_1_2.pack()

    entry_1_3 = Entry(frame, width= 5)
    entry_1_3.pack()

    entry_2_1 = Entry(frame, width= 5)
    entry_2_1.pack()

    entry_2_2 = Entry(frame, width= 5)
    entry_2_2.pack()

    entry_2_3 = Entry(frame, width= 5)
    entry_2_3.pack()

    entry_3_1 = Entry(frame, width= 5)
    entry_3_1.pack()

    entry_3_2 = Entry(frame, width= 5)
    entry_3_2.pack()

    entry_3_3 = Entry(frame, width= 5)
    entry_3_3.pack()

    button_p = Button(frame, text= "Registrar", command= get_matrix)
    button_p.pack()

def matrix_ti():
    pass

def matrix_ts():
    pass

def outcome():
    pass
def insert_function():
    pass

def bisec(): 
    pass

def secante():
    pass

root = Tk()
root.title("Proyecto 1")
root.geometry("530x300")

frame = Frame(root)
frame.pack()

titlefont = Font(family= "Georgia", size= 42, slant="italic")
normalfont = Font(family= "Geogia", size= 10)

create_menu()
intro()

root.mainloop()