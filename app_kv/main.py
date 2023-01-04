from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class SayHello(App):
    # crear ventana de la app
    def build(self):
        self.window = GridLayout()
        return self.window


# correr la app
if __name__ == '__main__':
    SayHello().run()