#---------------------------------
# Desktop app No. 1
#---------------------------------

# se importa la libreria tkinter con todas sus funciones 
from tkinter import *
from tkinter import messagebox
#----------------------------
# funciones de la app
#----------------------------

# SUMAR 
def calcular():
    messagebox.showinfo("MINICALCULADORA 1.0", "LAS OPERACIONES HAN SIDO REALIZADAS")
    s = int(x.get()) + int(y.get())
    r = int(x.get()) - int(y.get())
    m = int(x.get()) * int(y.get())
    d = int(x.get()) / int(y.get())
    de = int(x.get()) // int(y.get())
    mod = int(x.get()) % int(y.get())
    p = int(x.get()) ** int(y.get())
    t_resultados.insert(INSERT, f"{int(x.get())} + {int(y.get())} = {s}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} - {int(y.get())} = {r}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} * {int(y.get())} = {m}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} / {int(y.get())} = {d}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} // {int(y.get())} = {de}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} % {int(y.get())} = {mod}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} ** {int(y.get())} = {p}")

#borrar
def borrar():
    messagebox.showinfo("minicalculadora 1.0", "Los datos serán borrados")
    x.set("")
    y.set("")
    t_resultados.delete("1.0","end")

#salir
def salir():
    messagebox.showinfo("minicalculadora 1.0", "La app se va a cerrar")
    ventana_principal.destroy()

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# TAMAÑO DE LA VENTANA 
ventana_principal.geometry("500x500")

# TITULO DE VENTANA
ventana_principal.title("minicalculadora 1.0")

# DESHABILITAR BOTON DE MAXIMIZAR
ventana_principal.resizable(False, False)

# COLOR DE FONDO DE LA VENTANA 
ventana_principal.config(bg="green")

#----------------------------
# variables globales
#----------------------------
x = StringVar()
y = StringVar() 

#-------------------------
# FRAMA ENTRADA DATOS
#-------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

# LOGO DE LA APP 
logo = PhotoImage(file="IMG/descarga.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=0,y=10)

# etiqueta para el valor de x 
lb_x = Label(frame_entrada, text = "X = ")
lb_x.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_x.place(x=240, y=60)

# caja de texto para valor x
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_x.focus_set()
entry_x.place(x=290,y=60)

# etiqueta para el valor de y
lb_x = Label(frame_entrada, text = "Y = ")
lb_x.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_x.place(x=240, y=120)

# caja de texto para valor y
entry_y = Entry(frame_entrada, textvariable=y)
entry_y.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_y.focus_set()
entry_y.place(x=290,y=120)

# TITULO DE APP 
titulo = Label(frame_entrada, text="minicalculadora 1.0")
titulo.config(bg="green", fg="white", font=("Helvetica", 16))
titulo.place(x=240,y=10)



#-------------------------
# FRAMA OPERACIONES
#-------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

# boton para sumar 
bl_sumar = Button(frame_operaciones,text="Calcular", command=calcular)
bl_sumar.place(x=45, y=35, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones, text="Salir", command=salir)
bt_salir.place(x=335, y=35, width=100, height=30)

#-------------------------
# FRAMA RESULTADOS
#-------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

# are del texto de los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier, 20"))
t_resultados.place(x=10,y=10,width=460,height=160)

# run 
# SE EJECUTA EL METODO MAINLOOP() DE LA CLASE TK() A TRAVES DE LA INSTANCIA DE LA INTANCIA ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de le que el usuario haga (click en un boton, escribir, etc). Cada accion del usuario se conoce como unn evento. El método mainloop() es un bucle infinito.
ventana_principal.mainloop()