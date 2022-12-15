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
                    width=16, 
                    height=3)
height_label.place(x=30, y=60)

# Etiqueta texto altura
height_text_label = Label(app, 
                          text='Altura (cm)', 
                          font=('Roboto', 18, 'bold'), 
                          fg='#FFFFFF', 
                          bg='#181935' , 
                          width=10, 
                          height=1)
height_text_label.place(x=70, y=60)

# Etiqueta Peso
weight_label = Label(app, 
                    font=('Roboto', 18, 'bold'), 
                    fg='#FFFFFF', 
                    bg='#181935' , 
                    width=16, 
                    height=3)
weight_label.place(x=30, y=210)

# Etiqueta texto Peso
weight_text_label = Label(app, 
                          text='Peso (Kg)', 
                          font=('Roboto', 18, 'bold'), 
                          fg='#FFFFFF', 
                          bg='#181935' , 
                          width=10, 
                          height=1)
weight_text_label.place(x=72, y=217)

# variables de entrada
height = StringVar()
weight = StringVar()

# valores de las variables de entrada
height_value = IntVar()
weight_value = IntVar()

#---------- funciones para obtener los valores -----------
def get_height_value():
    return height_value.get()

def slider1(event):
    return height.set(get_height_value())

def get_weight_value():
    return weight_value.get()

def slider2(event):
    return weight.set(get_weight_value())

# entrada de la altura
height_entry = customtkinter.CTkEntry(app, 
                                      textvariable=height,
                                      bg_color='#181935',
                                      fg_color='#181833',
                                      border_width=1,
                                      font=('Arial',23, 'bold'))
height_entry.place(x=72, y=100)

# entrada del peso
weight_entry = customtkinter.CTkEntry(app, 
                                      textvariable=weight,
                                      bg_color='#181935',
                                      fg_color='#181833',
                                      border_width=1,
                                      font=('Arial',23, 'bold'))
weight_entry.place(x=72, y=258)



# control deslizante altura
height_slider = customtkinter.CTkSlider(app,
                                        variable=height_value,
                                        from_=0,
                                        to=300,
                                        width=230,
                                        bg_color='#181935',
                                        fg_color='#FFFFFF',
                                        button_hover_color='#bf0d97',
                                        command=slider1)
height_slider.place(x=30, y=160)

# control deslizante peso
weight_slider = customtkinter.CTkSlider(app,
                                        variable=weight_value,
                                        from_=0,
                                        to=500,
                                        width=230,
                                        bg_color='#181935',
                                        fg_color='#FFFFFF',
                                        button_hover_color='#bf0d97',
                                        command=slider2)
weight_slider.place(x=30, y=310)


# bucle para correr la app
app.mainloop()





