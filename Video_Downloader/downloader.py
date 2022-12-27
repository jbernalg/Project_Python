from msilib.schema import ComboBox
from tkinter import *
from tkinter import filedialog
import tkinter
from tkinter.ttk import Combobox
from moviepy import *
import tkinter.messagebox
import utils


#-------------------------Main---------------------------------------------------
def run():
    screen = Tk()  #pantalla de la app
    title = screen.title('Descarga Videos de Youtube') # titulo de la app
    canvas = Canvas(screen, width=500, height=500)  # medidas del lienzo de la app
    canvas.pack()

    #logo
    path = utils.resource_path('logo_youtube.png')
    logo_img = PhotoImage(file=path)
    #redimensionar imagen
    logo_img = logo_img.subsample(2, 2)
    #agregar la imagen al lienzo
    canvas.create_image(250, 80, image=logo_img)

    # Busqueda en youTube
    search_label = Label(screen, text='Buscar Multimedia en YouTube', font=('Arial Rounded MT Bold', 14))
    search_btn = Button(screen, text='Buscar', command= lambda: utils.search_multi())

    # Enlace
    link_field = Entry(screen, width=40)
    link_label = Label(screen, text='Ingresa enlace de Descarga', font=('Arial Rounded MT Bold', 14))

    # Ruta donde guarda el video
    path_label = Label(screen, text='Seleccionar Ruta para Descargar', font=('Arial Rounded MT Bold', 14))
    path_field = Entry(screen, width=40)  #campo de ruta
    select_btn = Button(screen, text='Seleccionar', command=lambda: utils.select_path(path_field))


    # boton de descarga de video
    download_btn = Button(screen,
                    text='Descargar Video',
                    command=lambda: utils.verify_link(
                                'video',
                                link_field = link_field,
                                path_field = path_field,
                                screen = screen,
                                list_resol = list_resol), 
                    font=('Arial Black',11), 
                    foreground= 'red')

    # boton de descarga de audio
    download_mp3 = Button(screen, 
                    text='Descargar Audio', 
                    command=lambda: utils.verify_link(
                                'audio', 
                                link_field = link_field, 
                                path_field = path_field, 
                                screen = screen, 
                                list_resol = list_resol), 
                    font=('Arial Black',11), 
                    foreground= 'blue')


    # Lista Resolucion video
    list_resol = Combobox(state='readonly' ,values=['Alta', 'Baja'], width=6)
    list_resol.set('Alta')
    resol_label = Label(screen, text='Resolución', font=('Arial', 10))

    #añadir elementos a la interfaz
    canvas.create_window(230, 170, window=search_label)# Etiqueta de busqueda
    canvas.create_window(400, 170, window=search_btn)  # Boton de busqueda
    canvas.create_window(220, 240, window=link_label)  # Etiqueta de enlace
    canvas.create_window(215, 270, window=link_field)  # Campo de enlace
    canvas.create_window(390, 270, window=list_resol)  # Lista resolucion
    canvas.create_window(390, 250, window=resol_label) # Etiqueta resolucion
    canvas.create_window(242, 330,window=path_label)   # Etiqueta de la ruta
    canvas.create_window(215, 360, window=path_field)  # Campo de la ruta
    canvas.create_window(390, 360,window=select_btn)   # Boton Seleccionar Ruta
    canvas.create_window(160, 420, window=download_btn)# Boton dascarga Video
    canvas.create_window(340, 420, window=download_mp3)# Boton descarga Audio

    screen.mainloop()

if __name__ == '__main__':
    run()