import customtkinter

# apariencia de la app
customtkinter.set_appearance_mode('dark')

# color del tema
customtkinter.set_default_color_theme('dark-blue')

#--------------- inicializacion de la app --------------------
root = customtkinter.CTk()

# dimensiones
root.geometry('500x350')

# funcion inicio de sesion
def login():
    print('Prueba')

# frame donde iran los botones
frame = customtkinter.CTkFrame(master=root)

# relleno del frame
frame.pack(pady=20, padx=60, fill='both', expand=True)

# agregar una etiqueta al frame
label = customtkinter.CTkLabel(master=frame, 
                               text='Inicio de Sesion', font=('Roboto', 24))

# relleno de la etiqueta
label.pack(pady=12, padx=10)

# entradas de texto
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Username')
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text='Password', show='*')
entry2.pack(pady=12, padx=10)

# boton inicio de sesion
button = customtkinter.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

# casilla de verificacion
checkbox = customtkinter.CTkCheckBox(master=frame, text='Recordarme')
checkbox.pack(pady=12, padx=10)

# bucle del punto raiz
root.mainloop()