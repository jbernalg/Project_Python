# librerias
from pytube import YouTube
from tkinter import *
from tkinter import filedialog
import tkinter
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
import webbrowser
import os
import sys

from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex

from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.gamma_corr import gamma_corr
from moviepy.video.fx.headblur import headblur
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.lum_contrast import lum_contrast
from moviepy.video.fx.make_loopable import make_loopable
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_color import mask_color
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.painting import painting
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.speedx import speedx
from moviepy.video.fx.supersample import supersample
from moviepy.video.fx.time_mirror import time_mirror
from moviepy.video.fx.time_symmetrize import time_symmetrize

# Verifica si el link es valido
def verify_link(string, link_field,path_field, screen,list_resol):
    try:
        YouTube(link_field.get()).check_availability()
        if string == 'video':
            download_file(link_field,path_field, screen, list_resol)
        else:
            download_audio(link_field, path_field, screen)
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


# Redirecciona a la pagina Principal de Youtube
def search_multi():
    webbrowser.open('https://www.youtube.com')


# Selecciona la ruta local donde guarda el archivo
def select_path(path_field):
    #permite seleccionar al usuario un directorio desde el explorador
    path = filedialog.askdirectory() 
    path_field.delete(0, 100)   #elimina la ruta anterior
    path_field.insert(0,path)


# Rutas relativas para los archivos de imagen
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)