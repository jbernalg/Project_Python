from email.mime import image
from select import select
from tkinter import *
from tkinter import filedialog

screen = Tk()  #pantalla de la app
title = screen.title('Descarga Videos de Youtube') # titulo de la app
canvas = Canvas(screen, width=500, height=500)  # medidas del lienzo de la app
canvas.pack()

#logo
logo_img = PhotoImage(file='logo_youtube.png')
#redimensionar image
logo_img = logo_img.subsample(2, 2)

#agregar la imagen al lienzo
canvas.create_image(250, 80, image=logo_img)

#campo de enlace
link_field = Entry(screen, width=50)
link_label = Label(screen, text='Ingresa enlace de Descarga: ', font=('Arial', 15))

#seleccione ruta donde guarda el video
path_label = Label(screen, text='Seleccionar Ruta para Descargar', font=('Arial', 15))
select_btn = Button(screen, text='Seleccionar')

#añadir widgets a la ventana
canvas.create_window(250, 190, window=link_label)
canvas.create_window(250, 220, window=link_field)
canvas.create_window(250, 280,window=path_label)
canvas.create_window(250, 330,window=select_btn)

#boton de descarga
download_btn = Button(screen, text='Download File')

#añadir boton a la ventana
canvas.create_window(250, 390,window=download_btn)

screen.mainloop()