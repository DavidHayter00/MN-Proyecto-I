from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

def clear_frame():
    for widgets in root.winfo_children():
        widgets.destroy()

def create_menu():
    my_menu = Menu(root)
    root.config(menu=my_menu)

    doolitle_menu = Menu(my_menu)
    roots_menu = Menu(my_menu)
    my_menu.add_command(label = "Presentacion", command= intro)
    my_menu.add_cascade(label = "Metodo Doolitle", menu= doolitle_menu)
    doolitle_menu.add_command(label= "Matriz Principal", command= doo.matrix_p)
    doolitle_menu.add_command(label= "Matrices Triangulares Superior e Inferior", command= doo.matrix_lu)
    doolitle_menu.add_command(label= "Resultado del Sistema de Ecuaciones", command= doo.result)
    my_menu.add_cascade(label = "Metodos para Calcular Raices", menu= roots_menu)
    roots_menu.add_command(label = "Insertar Funcion Polinomica", command= roots.insert_function)
    roots_menu.add_command(label = "Metodo Cerrado Biseccion", command= roots.bisec)
    roots_menu.add_command(label = "Metodo Abierto de la Secante", command= roots.secante)
    my_menu.add_command(label= "Salir", command= root.destroy)

def intro():
    clear_frame()
    create_menu()

    title = Label(root, text= "Bienvenido", font= titlefont)
    title.grid(padx= 15, pady= 15)

    topic = Label(root, text= "Este programa realiza Sistemas de Ecuaciones Algebraicas Lineales \ny Raices Reales de Funciones Algebraicas. Hecho por:", font= normalfont)
    topic.grid()

    names = Label(root, text= "- David Torres  8-963-282\n- Mark Bryan 20-14-7194", font= normalfont)
    names.grid()

class Doolittle:
    def __init__(self, A, B, L, U):
        self.A = A
        self.B = B
        self.L = L
        self.U = U

    def matrix_p(self):
        clear_frame()
        create_menu()

        if self.A ==  [[0, 0, 0],[0, 0, 0],[0, 0, 0]] and self.B == [[0],[0],[0]]: 
            entry_1_1 = Entry(root, width= 5)
            entry_1_1.grid(row=0, column=0)
            entry_1_1.insert(0, self.A[0][0])

            entry_1_2 = Entry(root, width= 5)
            entry_1_2.grid(row=0, column=1)
            entry_1_2.insert(0, self.A[0][1])

            entry_1_3 = Entry(root, width= 5)
            entry_1_3.grid(row=0, column=2)
            entry_1_3.insert(0, self.A[0][2])

            entry_2_1 = Entry(root, width= 5)
            entry_2_1.grid(row=1, column=0)
            entry_2_1.insert(0, self.A[1][0])

            entry_2_2 = Entry(root, width= 5)
            entry_2_2.grid(row=1, column=1)
            entry_2_2.insert(0, self.A[1][1])

            entry_2_3 = Entry(root, width= 5)
            entry_2_3.grid(row=1, column=2)
            entry_2_3.insert(0, self.A[1][2])

            entry_3_1 = Entry(root, width= 5)
            entry_3_1.grid(row=2, column=0)
            entry_3_1.insert(0, self.A[2][0])

            entry_3_2 = Entry(root, width= 5)
            entry_3_2.grid(row=2, column=1)
            entry_3_2.insert(0, self.A[2][1])

            entry_3_3 = Entry(root, width= 5)
            entry_3_3.grid(row=2, column=2)
            entry_3_3.insert(0, self.A[2][2])

            entry_b1 = Entry(root, width= 5)
            entry_b1.grid(row=0, column=3)
            entry_b1.insert(0, self.B[0])

            entry_b2 = Entry(root, width= 5)
            entry_b2.grid(row=1, column=3)
            entry_b2.insert(0, self.B[1])

            entry_b3 = Entry(root, width= 5)
            entry_b3.grid(row=2, column=3)
            entry_b3.insert(0, self.B[2])

            button_p = Button(root, text= "Insertar", command= lambda: doo.regis_matrix(entry_1_1.get(), entry_1_2.get(), entry_1_3.get(), entry_2_1.get(), entry_2_2.get(), entry_2_3.get(), entry_3_1.get(), entry_3_2.get(), entry_3_3.get(), entry_b1.get(), entry_b2.get(), entry_b3.get()))
            button_p.grid()
        else:
            doo.calculate_matrix(self.A[0][0], self.A[0][1], self.A[0][2], self.A[1][0], self.A[1][1], self.A[1][2], self.A[2][0], self.A[2][1], self.A[2][2])

    def regis_matrix(self, pos_1_1, pos_1_2, pos_1_3, pos_2_1, pos_2_2, pos_2_3, pos_3_1, pos_3_2, pos_3_3, pos_1, pos_2,pos_3):
        self.A[0][0] = int(pos_1_1)
        self.A[0][1] = int(pos_1_2)
        self.A[0][2] = int(pos_1_3)
        self.A[1][0] = int(pos_2_1)
        self.A[1][1] = int(pos_2_2)
        self.A[1][2] = int(pos_2_3)
        self.A[2][0] = int(pos_3_1)
        self.A[2][1] = int(pos_3_2)
        self.A[2][2] = int(pos_3_3)

        self.B[0] = int(pos_1)
        self.B[1] = int(pos_2)
        self.B[2] = int(pos_3)

        n = 3
        self.L = [[0 for x in range(n)]
                 for y in range(n)]
        self.U = [[0 for x in range(n)]
                 for y in range(n)]

        for i in range(n):
            for k in range(i, n):
                sum = 0
                for j in range(i):
                    sum += (self.L[i][j] * self.U[j][k])
                self.U[i][k] = self.A[i][k] - sum
        
            for k in range(i, n):
                if (i == k):
                    self.L[i][i] = 1 
                else:
                    sum = 0
                    for j in range(i):
                        sum += (self.L[k][j] * self.U[j][i])
                    self.L[k][i] = int((self.A[k][i] - sum) / self.U[i][i])

        clear_frame()
        create_menu()
        
        print(self.A, self.B)

    def matrix_lu(self):
        clear_frame()
        create_menu()

        n=3

        print("Lower Triangular\t\tUpper Triangular")

        for i in range(n):
            for j in range(n):
                print(self.L[i][j], end="\t")
            print("", end="\t")

            for j in range(n):
                print(self.U[i][j], end="\t")
            print("")
    
            
    def result(self):
        x = []
        y = []
        
        y.append(self.B[0])
        print(self.B[1])
        y.append(self.B[1] - (self.L[1][0] * y[0]))
        y.append(self.B[2] - (self.L[2][0] * y[0]) - (self.L[2][1] * y[1]))

        x.append(y[2] / self.U[2][2])
        x.append((y[1] - (self.U[1][2] * x[0])) / self.U[1][1])
        x.append((y[0] - (self.U[0][1] * x[1]) - (self.U[0][2] * x[0])) / self.U[0][0])

        clear_frame()
        create_menu()

        print(y,x)
class Root_Methods:
    def __init__(self, a, b ,c):
        self.a = a
        self.b = b
        self.c = c

    def insert_function(self):
        clear_frame()
        create_menu()
        
        entry_a = Entry(root, width= 5)
        entry_a.grid()
        entry_a.insert(0, self.a)

        entry_b = Entry(root, width= 5)
        entry_b.grid()
        entry_b.insert(0, self.b)

        entry_c = Entry(root, width= 5)
        entry_c.grid()
        entry_c.insert(0, self.c)

        button_r = Button(root, text= "Insertar", command= lambda: roots.register_coe(entry_a.get(), entry_b.get(), entry_c.get()))
        button_r.grid()

    def register_coe(self, coe_a, coe_b, coe_c):
        self.a = coe_a
        self.b = coe_b
        self.c = coe_c
        messagebox.showinfo("Mensaje", ("Se leyeron los coeficientes correctamente su ecuacion resultante\n",self.a,"x^2", self.b, "x", self.c))
        intro()

    def bisec(self):
        top = Toplevel()
        top.title("Insertar Intervalos")

        inte_a = Entry(top, width= 5)
        inte_a.grid()
        inte_a.insert(0, "a")
        
        inte_b = Entry(top, width= 5)
        inte_b.grid()
        inte_b.insert(0, "b")

        button_r = Button(top, text= "Insertar", command= lambda: roots.resul_bisec(inte_a.get(), inte_b.get()))
        button_r.grid()

        top.mainloop()
    
    def resul_bisec(self, int_a, int_b):
        print(self.a*(int_a ** 2) + self.b*(int_a) + self.c) * (self.a*(int_b ** 2) + self.b*(int_b) + self.c)
        #if ((self.a(int_a)**2 + self.b(int_a) + self.c) * (self.a(int_b)**2 + self.b(int_b) + self.c)) < 0:
        
    def secante():
        pass

root = Tk()
root.title("Proyecto 1")
root.geometry("450x300")

titlefont = Font(family= "Georgia", size= 42, slant="italic")
normalfont = Font(family= "Geogia", size= 10)

doo = Doolittle([[0, 0, 0],[0, 0, 0],[0, 0, 0]], [[0],[0],[0]], [], [])
roots = Root_Methods(0,0,0)

intro()

root.mainloop()

