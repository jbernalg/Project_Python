from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.app import App


class SayHello(App):
    # crear ventana de la app
    def build(self):
        self.window = GridLayout()
        # numero de columnas
        self.window.cols = 1
        # margenes
        self.window.size_hint = (0.6, 0.7)
        # posicion de la ventana
        self.window.pos_hint = {'center_x':0.5, 'center_y':0.5}

        # añadir  image widgets
        self.window.add_widget(Image(source='logo.png'))
        
        # añadir label widget
        self.greeting = Label(
            text='Cual es tu nombre?',
            font_size = 18,
            color= '#00FFCE'
            )
        self.window.add_widget(self.greeting)

        # añadir widget entrada de texto 
        self.user = TextInput(
            multiline=False,
            padding_y= (20, 20),
            size_hint = (1, .5)
            )
        self.window.add_widget(self.user)

        # añadir widget boton
        self.boton = Button(
            text='SALUDAR',
            size_hint = (1, .5),
            bold = True,
            background_color = '#00FFCE',
            background_normal = ''
            )
        self.boton.bind(on_press=self.callback)
        self.window.add_widget(self.boton)

        return self.window

    # funcion devolver saludo
    def callback(self, instance):
        self.greeting.text = 'Hola '+ self.user.text + '!'

       



# correr la app
if __name__ == '__main__':
    SayHello().run()