
# este codigo es un juego de señales de transito el cual consiste en mostrar una imagen y preguntar como se llama la señal, tienes 4 opciones de respuesta


import tkinter as tk
from tkinter import PhotoImage

# Lista de preguntas y respuestas
preguntas = [
    {
        "pregunta": "¿Qué significa esta señal?",
        "imagen": r"C:\PROCESAMIENTO DE DATOS PARA IA\PROYECTOS PERSONALES\dos_sentidos.png",
        "opciones": ["1) Prohibido girar a la derecha", "2) dos sentidos", "3) Prohibido adelantar", "4) Prohibido detenerse"],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Cuál es el límite de velocidad en esta señal?",
        "imagen": r"C:\PROCESAMIENTO DE DATOS PARA IA\PROYECTOS PERSONALES\glorieta.png",
        "opciones": ["1) giro en circulo", "2) retorno", "3) peligro", "4) remolino"],
        "respuesta_correcta": 3
    }
    
    # Puedes agregar más preguntas aquí
]

class JuegoPreguntas:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Preguntas de Normas de Tránsito")
        self.puntaje = 0
        self.pregunta_actual = 0

        self.pregunta_label = tk.Label(root, text="", wraplength=400)
        self.pregunta_label.pack(pady=20)

        self.imagen_label = tk.Label(root)
        self.imagen_label.pack(pady=10)

        self.opciones = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", value=i, variable=tk.IntVar(), command=self.evaluar_respuesta)
            rb.pack(anchor="w")
            self.opciones.append(rb)

        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        pregunta = preguntas[self.pregunta_actual]
        self.pregunta_label.config(text=pregunta["pregunta"])

        imagen = PhotoImage(file=pregunta["imagen"])
        self.imagen_label.config(image=imagen)
        self.imagen_label.image = imagen

        for i, opcion in enumerate(pregunta["opciones"]):
            self.opciones[i].config(text=opcion)

    def evaluar_respuesta(self):
        respuesta_seleccionada = int(self.root.children.get(self.opciones[0].cget("variable")).get())
        if respuesta_seleccionada == preguntas[self.pregunta_actual]["respuesta_correcta"]:
            self.puntaje += 1
            print("¡Correcto!")
        else:
            print("Incorrecto.")

        self.pregunta_actual += 1
        if self.pregunta_actual < len(preguntas):
            self.mostrar_pregunta()
        else:
            self.mostrar_puntaje_final()

    def mostrar_puntaje_final(self):
        self.pregunta_label.config(text=f"Tu puntaje final es: {self.puntaje} de {len(preguntas)}")
        self.imagen_label.config(image="")
        for rb in self.opciones:
            rb.pack_forget()

# Iniciar el juego
root = tk.Tk()
app = JuegoPreguntas(root)
root.mainloop()
