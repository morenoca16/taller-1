#1.Crear clase
class Persona:
    tipoDoc=" "
    documento=0
    nombre=" "
    apellido=" "
    peso=0
    estatura=0.5
    edad=0
    sexo=" "
#7.Método constructor
    def __init__(self, tipoDoc, documento, nombre, apellido, peso, estatura, edad, sexo):
        self.tipoDoc=tipoDoc
        self.documento=documento
        self.nombre=nombre
        self.apellido=apellido
        self.peso=peso
        self.estatura=estatura
        self.edad=edad
        self.sexo=sexo
    def registrarPersona(self):
        self.tipoDoc=input("Ingrese tipo de documento: ")
        self.documento=int(input("Ingresar número de documento: "))
        self.nombre=input("Ingrese el nombre de la persona: ")
        self.apellido=input("Ingrese el apellido de la persona: ")
        self.peso=int(input("Ingrese el peso: "))
        self.estatura=int(input("Ingresar la estatura: "))
        self.edad=int(input("Ingresar la edad: "))
        self.sexo=input("Ingresar sexo: ")

#7.Definir método con parámetros luego del contructor
    def mostrarPersonas(self):
        print(f'Tipo de documento: {self.tipoDoc} \nNumero de documento: {self.documento} \nNombre: {self.nombre}\nApellido: {self.apellido}\nPeso: {self.peso}\nEstatura: {self.estatura}\nEdad: {self.edad}\nSexo: {self.sexo}')
      
    def calcularIMC(self):
      pesoActual=self.peso/(self.estatura**2)
      print(f'el ususario {self.nombre} {self.apellido} \nidentificado con el tipo de documento: {self.tipoDoc} \n tiene un peso de {pesoActual}')
      return pesoActual
    def CalcularMayorEdad(self):
      if self.edad>=18:
        print('El usuario ya es mayor de edad')
      else:
        print('El usuario aun no es mayor de edad')

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