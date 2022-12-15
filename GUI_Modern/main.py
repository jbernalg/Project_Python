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

# configuracion del frame
frame.pack(pady=20, padx=60, fill='both', expand=True)