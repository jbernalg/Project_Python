# librerias
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfReader, PdfWriter

# Seleccionar PDF
def seleccionar_pdf():
    ruta = filedialog.askopenfilename(
        filetypes=[("PDF files", ".pdf")]
    )
    if ruta:
        entrada_pdf.set(ruta)

# Cortar PDF
def cortar_pdf():
    try:
        archivo = entrada_pdf.get()
        inicio = int(pagina_inicio.get())
        fin = int(pagina_fin.get())

        reader = PdfReader(archivo)
        writer = PdfWriter()

        total_paginas = len(reader.pages)

        if inicio < 1 or fin > total_paginas or inicio > fin:
            messagebox.showerror('Error', 'Rango de paginas invalido')
            return
        
        for i in range(inicio-1, fin):
            writer.add_page(reader.pages[i])

        guardar = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", '.pdf')]
        )

        if guardar:
            with open(guardar, 'wb') as salida:
                writer.write(salida)
            messagebox.showinfo('Exito', 'PDF creado correctamente')
    
    except Exception as e:
        messagebox.showerror('Error', str(e))


# Ventana principal
ventana = tk.Tk()
ventana.title('Cortador de PDF')
ventana.geometry("400x200")

entrada_pdf = tk.StringVar()

# Seleccionar archivo
tk.Label(ventana, text='PDF:').pack(pady=5)
tk.Entry(ventana, textvariable=entrada_pdf, width=40).pack()
tk.Button(ventana, text='Seleccionar PDF', command=seleccionar_pdf).pack(pady=5)

# Pagina de inicio
tk.Label(ventana, text='Pagina Inicio').pack()
pagina_inicio = tk.Entry(ventana)
pagina_inicio.pack()

# Pagina fin
tk.Label(ventana, text="Pagina Fin").pack()
pagina_fin = tk.Entry(ventana)
pagina_fin.pack() 

# boton cortar
tk.Button(ventana, text='Crear PDF', command=cortar_pdf).pack(pady=10)

ventana.mainloop()