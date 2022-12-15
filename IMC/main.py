import customtkinter
from tkinter import *
from utils import resource_path

# crear app
app = customtkinter.CTk()

# dimensiones de la app
app.geometry('300x500')

# titulo de la app
app.title('CALCULADORA IMC')

# agregar icono de la app
path = resource_path('./images/icon_peso.png')
image_icon = PhotoImage(file= path)
app.iconphoto(False, image_icon)

# color background a la app
app.config(bg='#020414')

# Etiqueta top titulo
top = Label(app, 
            text='Calculadora IMC', 
            font=('Roboto', 18, 'bold'), 
            fg='#FFFFFF', 
            bg='#181935' , 
            width=28, 
            height=1)
top.pack()

# Etiqueta altura
height_label = Label(app, 
                    font=('Roboto', 18, 'bold'), 
                    fg='#FFFFFF', 
                    bg='#181935' , 
                    width=17, 
                    height=4)
height_label.place(x=20, y=60)

# Etiqueta texto altura
height_text_label = Label(app, 
                          text='Altura (cm)', 
                          font=('Roboto', 18, 'bold'), 
                          fg='#FFFFFF', 
                          bg='#181935' , 
                          width=10, 
                          height=1)
height_text_label.place(x=75, y=60)

# Etiqueta Peso
weight_label = Label(app, 
                    font=('Roboto', 18, 'bold'), 
                    fg='#FFFFFF', 
                    bg='#181935' , 
                    width=17, 
                    height=4)
weight_label.place(x=20, y=210)

# Etiqueta texto Peso
weight_text_label = Label(app, 
                          text='Peso (Kg)', 
                          font=('Roboto', 18, 'bold'), 
                          fg='#FFFFFF', 
                          bg='#181935' , 
                          width=10, 
                          height=1)
weight_text_label.place(x=75, y=220)

# variables de entrada
height = StringVar

# entrada de la altura
height_entry = customtkinter.CTkEntry(app, 
                                      textvariable=height,
                                      bg_color='#')




# bucle para correr la app
app.mainloop()





