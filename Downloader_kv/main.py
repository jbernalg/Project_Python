import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
import webbrowser
from pytube import YouTube
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import os
from kivy.properties import StringProperty

Window.size = (400, 600)

class downloaderApp(App):
    pass

class layoutapp(Widget):
    title_media = StringProperty('')
    duration_media = StringProperty('')
    
    # ir a youtube
    def go_youtube(self):
        webbrowser.open('https://www.youtube.com')


    # Descargar audio
    def download_audio(self):

        # ventana emergente
        popup = Popup(title='Error en el Link',
                            content=Label(text='Ingrese un link correcto'),
                            size_hint=(.5, .2))

        #get user path
        get_link = self.ids.text_link.text
        try:
            YouTube(get_link).check_availability()
            
            #Download Audio
            mp4_audio = YouTube(get_link).streams.get_audio_only().download()
            mp3_audio = AudioFileClip(mp4_audio)
            mp3_audio.write_audiofile(mp3_audio.filename.replace('.mp4', '.mp3'))

            os.remove(mp3_audio.filename)

            # limpia el contenido de la caja de texto
            self.ids.text_link.text = ''
        except Exception:
            popup.open()


    # Descargar Video
    def download_video(self):

        # ventana emergente
        popup = Popup(title='Error en el Link',
                            content=Label(text='Ingrese un link correcto'),
                            size_hint=(.5, .2))


        #get user path
        get_link = self.ids.text_link.text

        try:        
            YouTube(get_link).check_availability()
            #Download Video
            mp4_video = YouTube(get_link).streams.get_highest_resolution().download()            
            vid_clip = VideoFileClip(mp4_video)
            vid_clip.close()
            
            #limpia el contenido de la caja de texto
            self.ids.text_link.text = ''
        except Exception:
            popup.open()

    
    # informacion del multimedia
    def info_media(self):
        get_link = self.ids.text_link.text

        if get_link != '':
            yt = YouTube(get_link)
            title = yt.title
            self.title_media = f'Titulo: {title}'

            duration = yt.length
            duration = duration/60
            self.duration_media = f'Duracion: {duration} minutos'



if __name__ == '__main__':
    downloaderApp().run()