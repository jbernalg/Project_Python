from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout


# diseño de anclado
class AnchorLayoutExample(AnchorLayout):
    pass

# diseño de caja para la app
class BoxLayoutExample(BoxLayout):
    pass
    '''
    # constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # cambiar orientacion de los botones
        self.orientation = 'vertical'

        #botones
        b1 = Button(text='new button')
        b2 = Button(text='new button 2')
        b3 = Button(text='new button 3')

        # agregar botones al diseño de caja
        # el orden de agregar los botones es importante
        self.add_widget(b2)
        self.add_widget(b1)
        self.add_widget(b3)
    '''

# interfaz principal de la app
class MainWidget(Widget):
    pass


# clase que inicia la app
class TheLabApp(App):
    pass


# linea para correr la app
TheLabApp().run()
