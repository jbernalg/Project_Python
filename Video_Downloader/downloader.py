from msilib.schema import ComboBox
from tkinter import *
from tkinter import filedialog
import tkinter
from tkinter.ttk import Combobox
from moviepy import *
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
from pytube import YouTube
import tkinter.messagebox
import utils

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



#-------------------------Main---------------------------------------------------

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