import tkinter as tk
from tkinter import messagebox
from tkinter import *

#-------Ventana Principal------------------------------------------------

ventana = tk.Tk()
ventana.title("Regitro de actividades")
#ventana.geometry("2999x697")
ventana.state("zoomed")


#-------Widgets Frames----------------------------------------------------

frame_avtividad = tk.Frame(ventana, bd=2, relief= GROOVE, highlightbackground="gray86")
nueva_actividad = tk.Label(frame_avtividad, text="Nueva Actividad", font=("Arial", 10), fg="black", padx=5, pady=5)


#------Widgets Labels----------------------------------------------------
text_descripcion = tk.Label(frame_avtividad, text="Descripción: ", font=("Arial", 10), fg="black", padx=5, pady=5)


#------Entrada del usuario---------------------------------------- 
descripcion = tk.Entry(frame_avtividad, width=40, font=("Arial", 10), fg="black", bg="white", relief="solid", bd=1, highlightbackground="gray42", )


#------Widgets Packs----------------------------------------------------
frame_avtividad.pack(padx=20, pady=20, fill=tk.X, side=tk.TOP)
nueva_actividad.place(x=10, y =-10)
descripcion.pack(padx=200, pady=25, anchor="nw",  expand=True)
text_descripcion.place(x=10, y=20, anchor="nw")


#-------Bucle principal------------------------------------------------
ventana.mainloop()