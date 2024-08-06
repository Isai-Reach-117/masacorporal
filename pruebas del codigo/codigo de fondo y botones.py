import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.colorchooser import askcolor
from PIL import ImageTk, Image
import csv

def calculate_bmi():
    try:
        peso = float(entry_weight.get())
        altura = float(entry_height.get())
        edad = int(entry_age.get())
        sexo = sex_var.get()
        
        if (peso <= 0) or (altura <= 0) or (edad <= 0):
            raise ValueError("Peso, altura y edad deben ser mayores que cero")
        
        if sexo == "Hombre":
            ks = 1.0
        elif sexo == "Mujer":
            ks = 1.1
        else:
            raise ValueError("Sexo inválido")
        
        ka = 1 + 0.01 * (edad - 25)
        imc = (peso / (altura ** 2)) * ks * ka
        
        if imc < 18.5:
            nivel_obesidad = "Bajo peso"
        elif 18.5 <= imc < 24.9:
            nivel_obesidad = "Normal"
        elif 25 <= imc < 29.9:
            nivel_obesidad = "Sobrepeso"
        elif 30 <= imc < 34.9:
            nivel_obesidad = "Obesidad I"
        elif 35 <= imc < 39.9:
            nivel_obesidad = "Obesidad II"
        else:
            nivel_obesidad = "Obesidad III"
        
        label_result['text'] = f"IMC: {imc:.2f} ({nivel_obesidad})"
    except Exception as e:
        messagebox.showerror("Error en la entrada", str(e))

def save_data():
    try:
        nombre = entry_name.get()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        
        peso = float(entry_weight.get())
        altura = float(entry_height.get())
        edad = int(entry_age.get())
        sexo = sex_var.get()
        
        if (peso <= 0) or (altura <= 0) or (edad <= 0):
            raise ValueError("Peso, altura y edad deben ser mayores que cero")
        
        imc_text = label_result['text']
        if "IMC:" not in imc_text:
            raise ValueError("IMC no calculado")
        
        imc = imc_text.split(": ")[1]
        
        with open(f"{nombre}.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre", "Peso (kg)", "Altura (m)", "Edad", "Sexo", "IMC"])
            writer.writerow([nombre, peso, altura, edad, sexo, imc])
        
        messagebox.showinfo("Éxito", "Datos guardados correctamente")
    except Exception as e:
        messagebox.showerror("Error al guardar", str(e))

def inicio():
    root.title("Bienvenida a Centro de Salud Uptex")
    
    # Limpiar pantalla anterior
    for widget in root.winfo_children():
        widget.destroy()
    
    # Crear un marco para el inicio
    frame_inicio = tk.Frame(root, padx=20, pady=20)
    frame_inicio.pack(expand=True)
    
    # Cargar la imagen
    image_path = r"C:\Users\Acer\Downloads\codigo de registro de vida\boton de entrada.png"
    image = Image.open(image_path)
    image = image.resize((250, 250), Image.LANCZOS)  # Ajustar tamaño según necesidad
    photo = ImageTk.PhotoImage(image)
    
    # Mostrar la imagen como botón
    btn_image = tk.Button(frame_inicio, image=photo, command=ir_a_datos, bd=0, cursor="hand2")
    btn_image.image = photo  # Mantener referencia a la imagen
    btn_image.pack(pady=20)
    
    # Etiqueta de bienvenida
    tk.Label(frame_inicio, text="¡Bienvenido a Centro de Salud Uptex!", font=("Arial", 16)).pack(pady=20)

def ir_a_datos():
    root.title("Ingreso de Datos")
    
    # Limpiar pantalla anterior
    for widget in root.winfo_children():
        widget.destroy()
    
    frame_datos = tk.Frame(root, padx=20, pady=20)
    frame_datos.pack(expand=True)

    tk.Label(frame_datos, text="Ingrese sus datos:", font=("Arial", 14)).grid(row=0, column=0, columnspan=3, pady=10)
    
    tk.Label(frame_datos, text="Nombre:").grid(row=1, column=0, sticky="e")
    global entry_name
    entry_name = tk.Entry(frame_datos)
    entry_name.grid(row=1, column=1, columnspan=2, sticky="w")
    
    tk.Label(frame_datos, text="Peso (kg):").grid(row=2, column=0, sticky="e")
    global entry_weight
    entry_weight = tk.Entry(frame_datos)
    entry_weight.grid(row=2, column=1, columnspan=2, sticky="w")
    
    tk.Label(frame_datos, text="Altura (m):").grid(row=3, column=0, sticky="e")
    global entry_height
    entry_height = tk.Entry(frame_datos)
    entry_height.grid(row=3, column=1, columnspan=2, sticky="w")
    
    tk.Label(frame_datos, text="Edad:").grid(row=4, column=0, sticky="e")
    global entry_age
    entry_age = tk.Entry(frame_datos)
    entry_age.grid(row=4, column=1, columnspan=2, sticky="w")
    
    tk.Label(frame_datos, text="Sexo:").grid(row=5, column=0, sticky="e")
    global sex_var
    sex_var = tk.StringVar(value="Hombre")
    tk.Radiobutton(frame_datos, text="Hombre", variable=sex_var, value="Hombre").grid(row=5, column=1, sticky="w")
    tk.Radiobutton(frame_datos, text="Mujer", variable=sex_var, value="Mujer").grid(row=5, column=2, sticky="w")
    
    # Cargar y ajustar las imágenes para los nuevos botones
    calculate_image_path = r"C:\Users\Acer\Downloads\codigo de registro de vida\boton clacular IMC.png"
    save_image_path = r"C:\Users\Acer\Downloads\codigo de registro de vida\boton de guardar.png"
    back_image_path = r"C:\Users\Acer\Downloads\codigo de registro de vida\boton de regrso.png"
    question_image_path = r"C:\Users\Acer\Downloads\codigo de registro de vida\boton de pregunta.png"
    
    calculate_image = Image.open(calculate_image_path)
    calculate_image = calculate_image.resize((75, 75), Image.LANCZOS)
    calculate_photo = ImageTk.PhotoImage(calculate_image)
    
    save_image = Image.open(save_image_path)
    save_image = save_image.resize((75, 75), Image.LANCZOS)
    save_photo = ImageTk.PhotoImage(save_image)
    
    back_image = Image.open(back_image_path)
    back_image = back_image.resize((90, 50), Image.LANCZOS)
    back_photo = ImageTk.PhotoImage(back_image)
    
    question_image = Image.open(question_image_path)
    question_image = question_image.resize((100, 60), Image.LANCZOS)
    question_photo = ImageTk.PhotoImage(question_image)
    
    button_calculate = tk.Button(frame_datos, image=calculate_photo, command=calculate_bmi, bd=0, cursor="hand2")
    button_calculate.image = calculate_photo  # Mantener referencia a la imagen
    button_calculate.grid(row=6, column=0, columnspan=2, pady=10)
    
    button_save = tk.Button(frame_datos, image=save_photo, command=save_data, bd=0, cursor="hand2")
    button_save.image = save_photo  # Mantener referencia a la imagen
    button_save.grid(row=6, column=2, columnspan=2, pady=10)
    
    global label_result
    label_result = tk.Label(frame_datos, text="IMC: ", font=("Arial", 14))
    label_result.grid(row=7, column=0, columnspan=4, pady=10)
    
    button_back = tk.Button(frame_datos, image=back_photo, command=inicio, bd=0, cursor="hand2")
    button_back.image = back_photo  # Mantener referencia a la imagen
    button_back.grid(row=8, column=0, columnspan=2, pady=10)
    
    button_question = tk.Button(frame_datos, image=question_photo, command=mostrar_explicacion, bd=0, cursor="hand2")
    button_question.image = question_photo  # Mantener referencia a la imagen
    button_question.grid(row=8, column=2, columnspan=2, pady=10)

def mostrar_explicacion():
    root.title("Explicación del IMC")
    
    # Limpiar pantalla anterior
    for widget in root.winfo_children():
        widget.destroy()
    
    frame_explicacion = tk.Frame(root, padx=20, pady=20)
    frame_explicacion.pack(expand=True)
    
    tk.Label(frame_explicacion, text="Explicación del nivel de IMC", font=("Arial", 16)).pack(pady=20)
    
    explanation_text = (
        "El Índice de Masa Corporal (IMC) es una medida que se utiliza para determinar si una persona tiene un peso saludable "
        "en relación con su altura. A continuación, se describen los diferentes niveles de IMC y las recomendaciones para cada uno:\n\n"
        "1. Bajo peso (IMC < 18.5):\n"
        "   - Las personas con bajo peso pueden tener un sistema inmunológico debilitado y estar en riesgo de desnutrición.\n"
        "   - Recomendaciones: Consumir una dieta equilibrada y rica en nutrientes, y consultar a un profesional de la salud.\n\n"
        "2. Normal (IMC 18.5 - 24.9):\n"
        "   - Indica un peso saludable y menor riesgo de enfermedades relacionadas con el peso.\n"
        "   - Recomendaciones: Mantener una dieta equilibrada y una rutina regular de ejercicio físico.\n\n"
        "3. Sobrepeso (IMC 25 - 29.9):\n"
        "   - Aumenta el riesgo de enfermedades cardiovasculares, diabetes tipo 2 y otros problemas de salud.\n"
        "   - Recomendaciones: Adoptar hábitos alimenticios saludables y aumentar la actividad física.\n\n"
        "4. Obesidad I (IMC 30 - 34.9):\n"
        "   - Mayor riesgo de enfermedades crónicas y problemas de salud.\n"
        "   - Recomendaciones: Seguir una dieta balanceada, hacer ejercicio regularmente y buscar orientación médica.\n\n"
        "5. Obesidad II (IMC 35 - 39.9):\n"
        "   - Riesgo significativamente alto de enfermedades graves y complicaciones de salud.\n"
        "   - Recomendaciones: Implementar cambios en el estilo de vida bajo supervisión médica y considerar intervenciones especializadas.\n\n"
        "6. Obesidad III (IMC ≥ 40):\n"
        "   - Riesgo muy alto de problemas de salud graves y potencialmente mortales.\n"
        "   - Recomendaciones: Buscar atención médica inmediata y considerar tratamientos especializados.\n"
    )
    
    text_widget = scrolledtext.ScrolledText(frame_explicacion, wrap=tk.WORD, width=80, height=20, font=("Arial", 12))
    text_widget.insert(tk.END, explanation_text)
    text_widget.config(state=tk.DISABLED)
    text_widget.pack(pady=20)
    
    # Cargar y ajustar la imagen para el botón "Regresar"
    back_image_path = r"C:\Users\Acer\Downloads\codigo de registro de vida\boton de regresar 2.png"
    back_image = Image.open(back_image_path)
    back_image = back_image.resize((90, 50), Image.LANCZOS)
    back_photo = ImageTk.PhotoImage(back_image)
    
    button_back = tk.Button(frame_explicacion, image=back_photo, command=ir_a_datos, bd=0, cursor="hand2")
    button_back.image = back_photo  # Mantener referencia a la imagen
    button_back.pack()

def change_background_color():
    color = askcolor(title="Seleccionar color de fondo")[1]
    if color:
        root.configure(background=color)

root = tk.Tk()
root.title("Bienvenida a Centro de Salud Uptex")

# Establecer fondo de pantalla
background_image = Image.open(r"C:\Users\Acer\Downloads\codigo de registro de vida\fondo de pantalla.jpg")
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.geometry("800x600")

# Menú para cambiar el color de fondo
menubar = tk.Menu(root)
root.config(menu=menubar)
options_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Opciones", menu=options_menu)
options_menu.add_command(label="Cambiar color de fondo", command=change_background_color)

inicio()

root.mainloop()
