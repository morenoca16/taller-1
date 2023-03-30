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
        self.sexo = input("Ingrese Sexo: ")

    def mostrarDatos(self):
        print(f'Tipo de documento: {self.tipoDoc} \nNumero de documento: {self.documento} \nNombre: {self.nombre}\nApellido: {self.apellido}\nPeso: {self.peso}\nEstatura: {self.estatura}\nEdad: {self.edad}\nSexo: {self.sexo}')

    def calcularImc(self):
        pesoActual = self.peso / (self.estatura ** 2)
        if pesoActual < 20:
            print("El peso está por debajo de lo ideal")
        elif pesoActual >= 20 and pesoActual <= 25:
            print("El peso es ideal")
        else:
            print("Tiene sobrepeso")

    def mayorEdad(self):
        if self.edad >= 18:
            print("Mayor de edad")
        else:
            print("Menor de edad")

'''class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # atributo privado
        self._edad = edad  # atributo privado
    def get_nombre(self):
        
       
return self._nombre  # método público
    def set_nombre(self, nombre):
        
       
self._nombre = nombre  # método público
    def get_edad(self):
        return self._edad  # método público
    def set_edad(self, edad):
        self._edad = edad  # método público'''
