# librerias
from pytube import YouTube
from tkinter import *
from tkinter import filedialog
import tkinter
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
import os
import sys

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
def download_file(link_field, path_field, screen, list_resol):
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


# Descarga audio
def download_audio(link_field, path_field, screen):
    #get user path
    get_link = link_field.get()

    #get selected path
    user_path = path_field.get()
    screen.title('Descargando... Espere un Momento')
    
    #Download Audio
    mp4_audio = YouTube(get_link).streams.get_audio_only().download(user_path)
    mp3_audio = AudioFileClip(mp4_audio)
    mp3_audio.write_audiofile(mp3_audio.filename.replace('.mp4', '.mp3'))

    os.remove(mp3_audio.filename)

    screen.title('Descarga Completada! Descargue otro Archivo...')
    link_field.delete(first=0, last=100) #limpia el contenido de la caja de texto