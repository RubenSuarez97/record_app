import tkinter as tk
from tkinter import messagebox
from tkinter import *

#-------Ventana Principal------------------------------------------------

ventana = tk.Tk()
ventana.title("Regitro de actividades")
ventana.geometry("2999x697")



#-------Widgets---------------------------------------------------------

titulo = tk.Label(ventana, text="Registro de Actividades", font=("roboto", 15))
descripcion = tk.Entry()

#------Widgets Packs----------------------------------------------------

titulo.pack()
descripcion.pack()


# crear entrada del usuario





#-------Bucle principal------------------------------------------------
ventana.mainloop()