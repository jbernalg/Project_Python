# librerias
from pytube import YouTube
from tkinter import *
from tkinter import filedialog
import tkinter


# Verifica si el link es valido
def verify_link(string, link_field):
    try:
        YouTube(link_field.get()).check_availability()
        if string == 'video':
            download_file(link_field)
        else:
            download_audio(link_field)
    except Exception:
        tkinter.messagebox.showinfo('ERROR EN EL LINK', 'Ingrese un Link Válido')
        link_field.delete(first=0, last=100)


# descarga video
def download_file(link_field, path_field, screen):
    #get user path
    get_link = link_field.get()
    
    #get selected path
    user_path =  path_field.get()
    screen.title('Descargando... Espere un Momento')
        
    #Download Video
    if list_resol.get() == 'Alta':
        mp4_video = YouTube(get_link).streams.get_highest_resolution().download(user_path)    
    else:
        mp4_video = YouTube(get_link).streams.get_lowest_resolution().download(user_path) 
        
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    
    screen.title('Descarga Completada! Descargue otro Archivo...')
    link_field.delete(first=0, last=100) #limpia el contenido de la caja de texto