competidor=[]
tiempo=[]
Ncompetidores=int(input("Cuantos competidores son?: "))
for i in range(0,Ncompetidores):
  Nomcompe=input("Ingrese nombre: ")
  competidor.append(Nomcompe)
for i in range(0,Ncompetidores):
  tiempoCompetidor= float(input("Ingresar tiempo competidor: "))
  tiempo.append(tiempoCompetidor)
print("Tiempos: ", competidor, tiempo) 

tiemin = min(tiempo)
ganador = ""

for i in range(len(competidor)):
    print(f"\n{competidor[i]}: {tiempo[i]} segundo/s\n")
    if tiempo[i] == tiemin:
        ganador = competidor[i]

print(f"El/La ganador/a es {ganador} con un tiempo de {tiemin} segundo/s \n ")