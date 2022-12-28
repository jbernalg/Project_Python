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
    pass

if __name__ == '__main__':
    calculatorApp().run()
