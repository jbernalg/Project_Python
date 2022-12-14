from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle


# clase canvas 1
class CanvasExample1(Widget):
    pass

# clase canvas 2
class CanvasExample2(Widget):
    pass

# clase canvas 3
class CanvasExample3(Widget):
    pass

# clase elementos creado desde main
class CanvasExample4(Widget):
    # constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # llamar al canvas
        with self.canvas:
            Color(0, 1, 0)
            Line(points=(100, 100, 400, 500), width = 3) # linea
            Color(0, 0, 1)
            Line(circle = (400, 200, 120), width = 2) # circulo de lineas
            Line(rectangle = (700, 400, 150, 100), width = 5) # rectangulo de lineas
            Rectangle(pos=(700, 200), size=(150, 100)) # rectangulo relleno
            


# clase con elementos del diseño
class WidgetsExample(GridLayout):
    # creamos un contador
    count = 1
    # creamos un objeto de tipo StringProperty con el texto de la etiqueta
    my_text = StringProperty('1')
    # variable que almacena el estado del toggle button
    count_enabled = BooleanProperty(False)
    # variable de tipo StringProperty con el texto de la etiqueta slider
    slider_value_text = StringProperty('50')
    # variable de tipo StringProperty con el texto de la etiqueta entrada
    text_input_str = StringProperty('bienvenidos')

    # funcion para llevar contabilidad de click
    def on_button_click(self):
        print('Boton presionado')

        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)

    # funcion para cambiar de estado
    def on_toggle_button_state(self, widget):
        # mostrar el estado en consola
        print('toggle state: ' + widget.state)
        
        # cambiar el texto del boton al cambiar de estado
        if widget.state == 'normal':
            widget.text = 'OFF'
            # cambiar el estado de count_enable
            self.count_enabled = False
        else:
            widget.text = 'ON'
            # cambiar el estado de count_enable
            self.count_enabled = True

    # funcion que permite mostrar en consola el estado del switch    
    def on_switch_active(self, widget):
        # mostrar en consola el estado de switch
        print('switch: ' + str(widget.active))


    # funcion que permite mostrar en consola el valor del slider
    def on_slider_value(self, widget):
        print('Slider: '+ str(int(widget.value)))
        self.slider_value_text = str(int(widget.value))
    

    # validar el texto de la etiqueta de entrada
    def on_text_validate(self, widget):
        self.text_input_str = widget.text


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
