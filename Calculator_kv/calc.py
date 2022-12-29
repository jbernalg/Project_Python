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
        else:
            self.ids.calc_input.text = f'{prior}{button}'


    # funcion para volver la entrada negativa o positiva
    def pos_neg(self):
        # variable que contenga lo que haya en la entrada
        prior = self.ids.calc_input.text

        # verificar si esta el signo negativo
        if '-' in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'


    # funcion para remover el ultimo caracter de la entrada
    def remove(self):
        # variable que contenga lo que haya en la entrada
        prior = self.ids.calc_input.text
        
        # eliminar ultimo caracter
        prior = prior[:-1]

        # mostrar en la caja de texto el cambio
        self.ids.calc_input.text = prior


    # funcion decimal
    def dot(self):
        # variable que contenga lo que haya en la entrada
        prior = self.ids.calc_input.text

        # dividimos el contenido de la caja de texto por el signo +
        num_list = prior.split('+')

        if '+' in prior and '.' not in num_list[-1]:
            # añadir el punto decimal al final del texto
            self.ids.calc_input.text = f'{prior}.'
        elif '.' in prior:
            pass
        else:
            # añadir el punto decimal al final del texto
            self.ids.calc_input.text = f'{prior}.'


    # funcion mostrar signo matematico en la entrada
    def math_sign(self, sign):
        # variable que contenga lo que haya en la entrada
        prior = self.ids.calc_input.text
        
        # asignar el signo mas en la entrada 
        self.ids.calc_input.text = f'{prior}{sign}'

    
    # funcion operacion
    def equals(self):
        # variable que contenga lo que haya en la entrada
        prior = self.ids.calc_input.text

        # suma
        if '+' in prior:
            #lista de numeros dividos por el signo +
            num_list = prior.split('+')
            
            # variable con el resultado de la operacion
            answer = 0.0

            #sumar elementos de la lista con un ciclo for
            for number in num_list:
                answer = answer + float(number)

            # imprimir el resultado en la caja de texto
            self.ids.calc_input.text = f'{answer}'

        # multiplicacion
        if '*' in prior:
            #lista de numeros dividos por el signo *
            num_list = prior.split('*')
            
            # variable con el resultado de la operacion
            answer = 1.0

            # multiplica los elementos de la lista con un ciclo for
            for number in num_list:
                answer = answer * float(number)

            # imprimir el resultado en la caja de texto
            self.ids.calc_input.text = f'{answer}'

        # resta
        if '-' in prior:
            #lista de numeros dividos por el signo -
            num_list = prior.split('-')
            print(num_list)
            
            # variable con el resultado de la operacion
            answer = float(num_list[0])

            # restar elementos de la lista con un ciclo for
            for i in range (len(num_list) - 1):
                answer = answer - float(num_list[i + 1]) 
            # imprimir el resultado en la caja de texto
            self.ids.calc_input.text = f'{answer}'

        # division
        if '/' in prior:
            #lista de numeros dividos por el signo /
            num_list = prior.split('/')
            print(num_list)
            
            # variable con el resultado de la operacion
            answer = int(num_list[0])

            # dividir elementos de la lista con un ciclo for
            for i in range (len(num_list) - 1):
                answer = answer / int(num_list[i + 1]) 
            # imprimir el resultado en la caja de texto
            self.ids.calc_input.text = f'{answer}'

    


if __name__ == '__main__':
    calculatorApp().run()
