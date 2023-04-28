#---------------------------------
# Desktop app No. 1
#---------------------------------

# se importa la libreria tkinter con todas sus funciones 
from tkinter import *

#----------------------------
# funciones de la app
#----------------------------

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# TAMAÑO DE LA VENTANA 
ventana_principal.geometry("500x500")

# TITULO DE VENTANA
ventana_principal.title("SUMA ENTEROS 1.0")

# DESHABILITAR BOTON DE MAXIMIZAR
ventana_principal.resizable(False, False)

# COLOR DE FONDO DE LA VENTANA 
ventana_principal.config(bg="green")

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


# TITULO DE APP 
titulo = Label(frame_entrada, text="suma_enteros_1.0")
titulo.config(bg="green", fg="white", font=("Helvetica", 16))
titulo.place(x=240,y=10)



#-------------------------
# FRAMA OPERACIONES
#-------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

#-------------------------
# FRAMA RESULTADOS
#-------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

# run 
# SE EJECUTA EL METODO MAINLOOP() DE LA CLASE TK() A TRAVES DE LA INSTANCIA DE LA INTANCIA ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de le que el usuario haga (click en un boton, escribir, etc). Cada accion del usuario se conoce como unn evento. El método mainloop() es un bucle infinito.
ventana_principal.mainloop()