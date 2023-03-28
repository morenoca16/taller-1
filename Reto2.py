from Reto2 import Persona

class empleado(Persona):
    # atributos
    def __init__(self,cargo,valHora,horasTra,depa):
        self.cargo=cargo
        self.valHora=valHora
        self.horasTra=horasTra
        self.depa=depa
        self.pagoEmpleado=self.calcularHorarios()

    def __init__(self):
        self.empleado1 = empleado("", "", "", "", 0, 0, 0, "","",0,0,"",0)

    # metodos
    def pedirDatos(self):
        self.tipoDoc=input('ingrese el tipo de documento del empleado: ')
        self.documento=input('ingrese el numero: ')
        self.nombre=input('ingrese el nombre: ')
        self.apellido=input('ingrese el apellido: ')
        self.peso=float(input('ingrese su peso en kg: '))
        self.estatura=float(input('ingrese su altura en mts: '))
        self.edad=int(input('ingrese su edad: '))
        self.sexo=input('indique su sexo: ')
        self.cargo=input('indique el cargo del empleado: ')
        self.valHora=float(input('ingrese cuanto va a pagarle al empleado por hora: '))
        self.horasTraba=float(input('ingrese las horas que trabajo el empleado: '))
        self.depar=input('indique el departamento del empleado: ')

    def calcularHorarios(self):
        valTotal = self.valHora * self.horasTraba
        reteica = valTotal * 0.00966
        honorarios = valTotal - reteica
        return honorarios
    
    def mostrarEmpleado(self):
        print(f'\n {self.tipoDoc} \n{self.nombre} \n{self.apellido} \n{self.cargo} \n{self.horasTraba} \n{self.valHora} \n{self.pagoEmpleado}')