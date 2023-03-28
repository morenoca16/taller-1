from Reto1 import Persona
class inicio:

    def __init__(self):
        self.usuario1 = Persona("", "", "", "", 0, 0, 0, "")
        self.usuario2 = Persona("", "", "", "", 0, 0, 0, "")

    def a(self):
        print('ingrese los datos del usuario 1')
        self.usuario1.registrarPersona()

        print('Datos del usuario 1')
        self.usuario1.mostrarPersonas()

        if self.usuario1.calcularIMC()<20 :
            print('El IMC del usuario 1 esta debajo del ideal')
        elif 20<= self.usuario1.calcularIMC() <=25 :
            print('El IMC del usuario 1 es el ideal')
        else:
            print('El IMC del usuario 1 esta encima del ideal')
        self.usuario1.calcularIMC()

        print(self.usuario1.CalcularMayorEdad)

        print('ingrese los datos del usuario 2')
        self.usuario2.registrarPersona()

        print('Datos del usuario 2')
        self.usuario2.mostrarPersonas()

        if self.usuario2.calcularIMC()<20 :
            print('El IMC del usuario 2 esta debajo del ideal')
        elif 20<= self.usuario2.calcularIMC() <=25 :
            print('El IMC del usuario 2 es el ideal')
        else:
            print('El IMC del usuario 2 esta encima del ideal')
        self.usuario2.calcularIMC()

        print(self.usuario2.CalcularMayorEdad)
inicio = inicio()
inicio.a()