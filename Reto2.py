from Reto1 import Persona

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.cargo = ""
        self.valorhora = 0.0
        self.horastrabajadas = 0
        self.departamento = ""

    def pedirDatos(self):
        super().pedirDatos()
        self.cargo = input("Cargo: ")
        self.valorhora = float(input("Valor por hora: "))
        self.horastrabajadas = int(input("Horas trabajadas: "))
        self.departamento = input("Departamento: ")
        print("\n")

    def calcularHonorarios(self):
        total = self.valorhora * self.horastrabajadas
        reteica = total * 0.00966
        honorarios = total - reteica
        return honorarios

    def imprimirEmpleado(self):
        print(f'Tipo de documento: {self.tipoDoc} \nNumero de documento: {self.documento} \nNombre: {self.nombre}\nApellido: {self.apellido}\ncargo: {self.cargo}\nHoras trabajadas: {self.horastrabajadas}\nValor por hora: {self.valorhora}\nTotal a pagar: {self.calcularHonorarios()}')
        
empleado = Empleado()
empleado.pedirDatos()
empleado.imprimirEmpleado()
