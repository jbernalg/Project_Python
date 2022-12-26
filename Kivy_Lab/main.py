from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.properties import StringProperty

# definiendo la clase del boton click
class WidgetsExample(GridLayout):
    # creamos un contador
    count = 1
    # creamos un objeto de tipo StringProperty con el texto de la etiqueta
    my_text = StringProperty('1')
    
    # creamos una funcion para dar funcionalidad al boton
    def on_button_click(self):
        print('Boton presionado')
        self.count += 1
        self.my_text = str(self.count)
        

# diseño de pila
class StackLayoutExample(StackLayout):
    # constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # cambiar de orientacion
        #self.orientation = 'lr-bt'
        
        for i in range(0, 100):
            #diferentes tamaños para los botones
            #size = dp(100) + i*10
            size = dp(100)
            #crear boton
            b = Button(text=str(i+1),
                       size_hint=(None, None),
                       size=(size, size))
            #añadir boton
            self.add_widget(b)

# diseño de cuadricula
# class GridLayoutExample(GridLayout):
#     pass

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
