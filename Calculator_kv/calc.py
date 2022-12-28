from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window # configura el tamaño de la app

# configurar tamaño de la app
Window.size = (500, 700)

# clase de la app
class calculatorApp(App):
    pass

if __name__ == '__main__':
    calculatorApp().run()
