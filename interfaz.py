import gradio as gr
from lista_climas import ListaDeListas

estructura = ListaDeListas()
estructura.agregar_letra('A', ['sol', 'nube', 'tormenta'])
estructura.agregar_letra('G', ['lluvia', 'sol'])
estructura.agregar_letra('L', ['nube', 'lluvia'])
estructura.agregar_letra('O', ['sol', 'nube'])
estructura.agregar_letra('Y', ['lluvia', 'nube'])

def clima_interfaz(ciudad, hora):
    return estructura.consultar_clima(ciudad, hora)

def lanzar_interfaz():
    interface = gr.Interface(
        fn=clima_interfaz,
        inputs=[
            gr.Dropdown(choices=['A', 'G', 'L', 'O', 'Y'], label="Ciudad"),
            gr.Slider(minimum=0, maximum=4, step=1, label="Hora (posición)")
        ],
        outputs="text",
        title="Consulta de Clima",
        description="Selecciona una ciudad y una hora para ver el clima correspondiente."
    )
    interface.launch()
