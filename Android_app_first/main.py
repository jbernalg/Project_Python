import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

# version compatible con android del tlfn
kivy.require('1.9.0')

# clase principal
class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    # funcion para generar numeros aleatorios
    def generate_number(self):
        self.random_label.text = str(random.randint(0, 1000))


# clase con el nombre de la app
class appAleatorio(App):

    def build(self):
        return MyRoot()

appaleatorio = appAleatorio()
appaleatorio.run()