from tkinter import *
from tkinter import filedialog
import tkinter
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil
import tkinter.messagebox

#Funciones

def select_path():
    #permite seleccionar al usuario un directorio desde el explorador
    path_field.delete(0, 100)
    path = filedialog.askdirectory() 
    path_field.insert(0,path)

def download_file():
    #get user path
    get_link = link_field.get()
    
    if get_link == "":
        print('Ingrese el Link de la Multimedia!')
        tkinter.messagebox.showinfo('ATENCIÓN', 'Ingrese el Link de la Multimedia..!')
    else:
        #get selected path
        user_path = path_label.cget("text")
        screen.title('Descargando... Espere un Momento')
        #Download Video
        mp4_video = YouTube(get_link).streams.get_highest_resolution().download()

        vid_clip = VideoFileClip(mp4_video)
        vid_clip.close()
        #move file to selected directory
        shutil.move(mp4_video, user_path)
        screen.title('Descarga Completada! Descargue otro Archivo...')
        link_field.delete(first=0, last=100) #limpia el contenido de la caja de texto

def download_audio():
    #get user path
    get_link = link_field.get()

    if get_link == "":
        print('Ingrese el Link de la Multimedia!')
        tkinter.messagebox.showinfo('ATENCIÓN', 'Ingrese el Link de la Multimedia..!')
    else:
        #get selected path
        user_path = path_label.cget("text")
        screen.title('Descargando... Espere un Momento')
        #Download Audio
        mp3_audio = YouTube(get_link).streams.get_audio_only().download()
        shutil.move(mp3_audio, user_path)
        screen.title('Descarga Completada! Descargue otro Archivo...')
        link_field.delete(first=0, last=100) #limpia el contenido de la caja de texto



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

# Campo de enlace
link_field = Entry(screen, width=50)
link_label = Label(screen, text='Ingresa enlace de Descarga: ', font=('Arial', 15))

# Ruta donde guarda el video
path_label = Label(screen, text='Seleccionar Ruta para Descargar', font=('Arial', 15))
select_btn = Button(screen, text='Seleccionar', command=select_path)
path_field = Entry(screen, width=40)  #campo de ruta

#boton de descarga de video
download_btn = Button(screen, text='Descargar Video', command=download_file)

#boton de descarga de audio
download_mp3 = Button(screen, text='Descargar Audio', command=download_audio)

#añadir widgets a la ventana
canvas.create_window(250, 190, window=link_label)  # Etiqueta de enlace
canvas.create_window(250, 220, window=link_field)  # Campo de enlace
canvas.create_window(250, 280,window=path_label)   # Etiqueta de la ruta
canvas.create_window(220, 310, window=path_field)  # Campo de la ruta
canvas.create_window(390, 310,window=select_btn)   # Boton Seleccionar Ruta
canvas.create_window(190, 390, window=download_btn)# Boton dascarga Video
canvas.create_window(310, 390, window=download_mp3)# Boton descarga Auido


screen.mainloop()