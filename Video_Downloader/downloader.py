import glob
from msilib.schema import ComboBox
from tkinter import *
from tkinter import filedialog
import tkinter
from tkinter.ttk import Combobox
from moviepy import *
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
from pytube import YouTube
import shutil
import tkinter.messagebox
import webbrowser
import os

# Funciones

# Verifica si el link es valido
def verify_link(string):
    try:
        YouTube(link_field.get()).check_availability()
        if string == 'video':
            download_file()
        else:
            download_audio()
    except Exception:
        tkinter.messagebox.showinfo('ERROR EN EL LINK', 'Ingrese un Link Válido')
        link_field.delete(first=0, last=100)
        

# Redirecciona a la pagina Principal de Youtube
def search_multi():
    webbrowser.open('https://www.youtube.com')


# Selecciona la ruta local donde guarda el archivo
def select_path():
    #permite seleccionar al usuario un directorio desde el explorador
    path = filedialog.askdirectory() 
    path_field.delete(0, 100)   #elimina la ruta anterior
    path_field.insert(0,path)


# descarga video
def download_file():
    #get user path
    get_link = link_field.get()
    
    #get selected path
    user_path =  path_field.get()
    screen.title('Descargando... Espere un Momento')
        
    #Download Video
    if list_resol.get() == 'Alta':
        mp4_video = YouTube(get_link).streams.get_highest_resolution().download()    
    else:
        mp4_video = YouTube(get_link).streams.get_lowest_resolution().download() 
        
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Descarga Completada! Descargue otro Archivo...')
    link_field.delete(first=0, last=100) #limpia el contenido de la caja de texto


# Descarga audio
def download_audio():
    #get user path
    get_link = link_field.get()

    #get selected path
    user_path = path_field.get()
    screen.title('Descargando... Espere un Momento')
    
    #Download Audio
    mp4_audio = YouTube(get_link).streams.get_audio_only().download(user_path)
    mp3_audio = AudioFileClip(mp4_audio)
    mp3_audio.write_audiofile(mp3_audio.filename.replace('.mp4', '.mp3'))

    #shutil.move()
    screen.title('Descarga Completada! Descargue otro Archivo...')
    link_field.delete(first=0, last=100) #limpia el contenido de la caja de texto

#-------------------------Main---------------------------------------------------

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

# Busqueda en youTube
search_label = Label(screen, text='Buscar Multimedia en YouTube', font=('Arial Rounded MT Bold', 14))
search_btn = Button(screen, text='Buscar', command=search_multi)

# Enlace
link_field = Entry(screen, width=40)
link_label = Label(screen, text='Ingresa enlace de Descarga', font=('Arial Rounded MT Bold', 14))

# Ruta donde guarda el video
path_label = Label(screen, text='Seleccionar Ruta para Descargar', font=('Arial Rounded MT Bold', 14))
select_btn = Button(screen, text='Seleccionar', command=select_path)
path_field = Entry(screen, width=40)  #campo de ruta

# boton de descarga de video
download_btn = Button(screen,
                text='Descargar Video',
                command=lambda: verify_link('video'), 
                font=('Arial Black',11), 
                foreground= 'red')

# boton de descarga de audio
download_mp3 = Button(screen, 
                text='Descargar Audio', 
                command=lambda: verify_link('audio'), 
                font=('Arial Black',11), 
                foreground= 'blue')

# Lista Resolucion video
list_resol = Combobox(state='readonly' ,values=['Alta', 'Baja'], width=6)
list_resol.set('Alta')
resol_label = Label(screen, text='Resolución', font=('Arial', 10))

#añadir widgets a la ventana
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
canvas.create_window(340, 420, window=download_mp3)# Boton descarga Auido



screen.mainloop()