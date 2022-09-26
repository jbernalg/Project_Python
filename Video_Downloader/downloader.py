from tkinter import *
from tkinter import filedialog

screen = Tk()  #pantalla de la app
title = screen.title('Descarga Videos de Youtube') # titulo de la app
canvas = Canvas(screen, width=500, height=500)  # medidas del lienzo de la app
canvas.pack()

screen.mainloop()