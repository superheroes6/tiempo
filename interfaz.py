import gradio as gr
from lista_climas import ListaDeListas
import random
import tkinter as tk
from tkinter import messagebox

estructura = ListaDeListas()
estructura.agregar_letra('Madrid', ['Soleado', 'Nublado', 'Tormentoso'])
estructura.agregar_letra('Barcelona', ['Lluvioso', 'Soleado'])
estructura.agregar_letra('Valencia', ['Nublado', 'Lluvioso'])
estructura.agregar_letra('Sevilla', ['Soleado', 'Nublado'])
estructura.agregar_letra('Bilbao', ['Lluvioso', 'Nublado'])

def clima_interfaz(ciudad, hora):
    return estructura.consultar_clima(ciudad, hora)

def generar_clima(ciudad):
    resultado = f"Clima para {ciudad}:\n\n"
    for hora in range(24):
        temperatura = random.randint(-10, 40)
        condicion = random.choice(["Soleado", "Nublado", "Lluvioso", "Tormentoso", "Nevado"])
        resultado += f"{hora:02d}:00 - {temperatura}°C, {condicion}\n"
    return resultado

def generar_clima_para_hora(ciudad, hora):
    if 6 <= hora < 12:
        condicion = random.choice(["Soleado", "Nublado", "Lluvioso"])
        temperatura = random.randint(10, 25)
    elif 12 <= hora < 18:
        condicion = random.choice(["Soleado", "Nublado", "Lluvioso", "Tormentoso"])
        temperatura = random.randint(20, 35)
    elif 18 <= hora < 24:
        condicion = random.choice(["Nublado", "Lluvioso", "Tormentoso"])
        temperatura = random.randint(15, 25)
        condicion = random.choice(["Nublado", "Nevado", "Lluvioso"])
        temperatura = random.randint(-5, 10)
    return f"A las {hora:02d}:00 en {ciudad}, el clima será {condicion} con una temperatura de {temperatura}°C."

def mostrar_clima():
    ciudad = entrada_ciudad.get().strip().upper()
    hora_str = entrada_hora.get().strip()

    if not ciudad:
        messagebox.showerror("Error", "Por favor, ingrese el nombre de una ciudad.")
        return

    if not hora_str.isdigit() or not (0 <= int(hora_str) < 24):
        messagebox.showerror("Error", "Por favor, ingrese una hora válida (0-23).")
        return

    hora = int(hora_str)
    clima = estructura.consultar_clima(ciudad, hora)
    resultado_texto.delete(1.0, tk.END)
    resultado_texto.insert(tk.END, clima)

def lanzar_interfaz():
    global entrada_ciudad, entrada_hora, resultado_texto

    ventana = tk.Tk()
    ventana.title("Clima Dinámico")

    tk.Label(ventana, text="Ingrese el nombre de la ciudad (Madrid, Barcelona, Valencia, Sevilla, Bilbao):").pack(pady=5)
    entrada_ciudad = tk.Entry(ventana, width=30)
    entrada_ciudad.pack(pady=5)

    tk.Label(ventana, text="Ingrese la hora (0-23):").pack(pady=5)
    entrada_hora = tk.Entry(ventana, width=5)
    entrada_hora.pack(pady=5)

    tk.Button(ventana, text="Mostrar Clima", command=mostrar_clima).pack(pady=10)

    resultado_texto = tk.Text(ventana, width=50, height=10)
    resultado_texto.pack(pady=5)

    ventana.mainloop()
