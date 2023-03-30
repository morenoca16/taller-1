class Persona:
    def __init__(self):
        self.tipoDoc = ""
        self.documento = ""
        self.nombre = ""
        self.apellido = ""
        self.peso = 0.0
        self.estatura = 0.0
        self.edad = 0
        self.sexo = ""

    def pedirDatos(self):
        self.tipoDoc = input("Ingrese Tipo de documento: ")
        self.documento = input("Ingrese Número de documento: ")
        self.nombre = input("Ingrese Nombre: ")
        self.apellido = input("Ingrese Apellido: ")
        self.peso = float(input("Ingrese Peso (kilogramosg): "))
        self.estatura = float(input("Ingrese Estatura (metros): "))
        self.edad = int(input("Ingrese edad: "))
        self.sexo = input("Escoja el Sexo de la persona (M/F): ").upper()

    def mostrarDatos(self):
        print(f'Tipo de documento: {self.tipoDoc} \nNumero de documento: {self.documento} \nNombre: {self.nombre}\nApellido: {self.apellido}\nPeso: {self.peso}\nEstatura: {self.estatura}\nEdad: {self.edad}\nSexo: {self.sexo}')

    def calcularImc(self):
        pesoActual = self.peso / (self.estatura ** 2)
        if pesoActual < 20:
            print("El peso de la persona está por debajo de lo ideal")
        elif pesoActual >= 20 and pesoActual <= 25:
            print("El peso de la persona es ideal")
        else:
            print("La persona tiene sobrepeso")

    def mayorEdad(self):
        if self.edad >= 18:
            print("La persona es mayor de edad")
        else:
            print("La persona es menor de edad")