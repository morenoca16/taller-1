from Reto1 import Persona

class Inicio:
    def __init__(self):
        self.persona = Persona()

    def ejecutar(self):
        self.persona.pedirDatos()
        self.persona.mostrarDatos()
        self.persona.calcularImc()
        self.persona.mayorEdad()

inicio = Inicio()
inicio.ejecutar()