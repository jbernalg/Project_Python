from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window # configura el tamaño de la app

# configurar tamaño de la app
Window.size = (400, 600)

# clase de la app
class calculatorApp(App):
    pass

# clase con el diseño de la app
class mylayout(Widget):
    
    # funcion limpiar entrada
    def clear(self):
        self.ids.calc_input.text = '0'

    # funcion presionar boton
    def button_press(self, button):
        # variable que contenga lo que haya en la entrada
        prior = self.ids.calc_input.text

        # determinar si el 0 esta en la entrada
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'

if __name__ == '__main__':
    calculatorApp().run()
