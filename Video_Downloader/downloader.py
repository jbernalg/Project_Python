from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

#Funciones

def select_path():
    #permite seleccionar al usuario un directorio desde el explorador
    path = filedialog.askdirectory() 
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
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

def download_audio():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Descargando... Espere un Momento')
    #Download Audio
    mp3_audio = YouTube(get_link).streams.get_audio_only().download()
    shutil.move(mp3_audio, user_path)
    screen.title('Descarga Completada! Descargue otro Archivo...')
    link_label = Label(screen, text='Ingresa enlace de Descarga: ', font=('Arial', 15))



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
select_btn = Button(screen, text='Seleccionar', command=select_path)

#añadir widgets a la ventana
canvas.create_window(250, 190, window=link_label)
canvas.create_window(250, 220, window=link_field)
canvas.create_window(250, 280,window=path_label)
canvas.create_window(250, 330,window=select_btn)

#boton de descarga de video
download_btn = Button(screen, text='Descargar Video', command=download_file)
#boton de descarga a la ventana
canvas.create_window(190, 390, window=download_btn)

#boton de descarga de audio
download_mp3 = Button(screen, text='Descargar Audio', command=download_audio)
#boton de descarga de audio a la ventana
canvas.create_window(310, 390, window=download_mp3)

screen.mainloop()