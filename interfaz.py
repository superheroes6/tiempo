import tkinter as tk
from tkinter import messagebox, ttk
from lista_climas import ListaDeListas

estructura = ListaDeListas()
estructura.agregar_letra('Madrid', ['Soleado', 'Nublado', 'Tormentoso'])
estructura.agregar_letra('Barcelona', ['Lluvioso', 'Soleado'])
estructura.agregar_letra('Valencia', ['Nublado', 'Lluvioso'])
estructura.agregar_letra('Sevilla', ['Soleado', 'Nublado'])
estructura.agregar_letra('Bilbao', ['Lluvioso', 'Nublado'])

def mostrar_clima():
    ciudad = seleccion_ciudad.get()
    hora_str = entrada_hora.get().strip()

    if not ciudad:
        messagebox.showerror("Error", "Por favor, seleccione una ciudad.")
        return

    if not hora_str.isdigit() or not (0 <= int(hora_str) < 24):
        messagebox.showerror("Error", "Por favor, ingrese una hora válida (0-23).")
        return

    hora = int(hora_str)
    clima = estructura.consultar_clima(ciudad, hora)
    resultado_texto.delete(1.0, tk.END)
    resultado_texto.insert(tk.END, clima)

def lanzar_interfaz():
    global seleccion_ciudad, entrada_hora, resultado_texto

    ventana = tk.Tk()
    ventana.title("Clima Dinámico")
    ventana.geometry("600x400")
    ventana.configure(bg="#87CEEB")

    titulo = tk.Label(
        ventana,
        text="Consulta del Clima",
        font=("Helvetica", 20, "bold"),
        bg="#87CEEB",
        fg="white"
    )
    titulo.pack(pady=10)

    decoracion = tk.Label(
        ventana,
        text="☀️🌧️⛅❄️🌩️",
        font=("Helvetica", 30),
        bg="#87CEEB",
        fg="white"
    )
    decoracion.pack(pady=10)

    frame_centro = tk.Frame(ventana, bg="#87CEEB")
    frame_centro.pack(pady=10)

    tk.Label(
        frame_centro,
        text="Seleccione una ciudad:",
        font=("Helvetica", 12),
        bg="#87CEEB",
        fg="white"
    ).grid(row=0, column=0, padx=10, pady=5, sticky="e")
    seleccion_ciudad = ttk.Combobox(
        frame_centro,
        values=["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"],
        state="readonly",
        font=("Helvetica", 10)
    )
    seleccion_ciudad.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    tk.Label(
        frame_centro,
        text="Ingrese la hora (0-23):",
        font=("Helvetica", 12),
        bg="#87CEEB",
        fg="white"
    ).grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entrada_hora = tk.Entry(frame_centro, width=5, font=("Helvetica", 10))
    entrada_hora.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    boton = tk.Button(
        ventana,
        text="Mostrar Clima",
        command=mostrar_clima,
        font=("Helvetica", 12, "bold"),
        bg="#4682B4",
        fg="white",
        activebackground="#5F9EA0",
        activeforeground="white"
    )
    boton.pack(pady=10)

    resultado_texto = tk.Text(
        ventana,
        width=60,
        height=10,
        font=("Helvetica", 10),
        bg="#F0F8FF",
        fg="black"
    )
    resultado_texto.pack(pady=10)

    ventana.mainloop()
