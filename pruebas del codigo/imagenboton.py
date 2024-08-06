import tkinter as tk
from tkinter import PhotoImage, messagebox

def button_clicked():
    messagebox.showinfo("Notificación", "El botón fue presionado")

root = tk.Tk()
root.title("Botón con imagen en Tkinter")

# Asegúrate de que la ruta y el nombre del archivo de imagen sean correctos
button_image = PhotoImage(file=r"C:\Users\Acer\Downloads\codigo de registro de vida\boton clacular IMC.png")

image_button = tk.Button(root, image=button_image, command=button_clicked, borderwidth=0)
image_button.pack(pady=28)

root.mainloop()
