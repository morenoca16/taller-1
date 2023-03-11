pres=100
pres1=0
seguir="s"
apuesta=0
count=0
gana=0
pierde=0

for i in range(1,6,1):

    while seguir=="S" or seguir=="s":
        seguir=input("Desea seguir apostando:  \n ingrese s/S \n para salir n")
        if seguir=="s" or seguir=="S":
            apuesta=int(input("Ingrese apuesta" ))
            pres=pres-apuesta
            print("Su gasto fue de: ", apuesta, "Le quedan del presupuesto: ", pres)
        else:
          print("Salio del reporte")
          print("Su apuesta fue de: ", apuesta, "Le quedan del presupuesto: ", pres)
          print("Supero el # de registros", )
            
        num1=int(input("ingrese 0 para sello y 1 para cara:"))
        if num1==0:
          print("Sello")
        else:
          print("Cara")
        import random
        num2=random.randint(0,1)
        if num2==0:
          print("Máquina arrojo Sello")
        else:
          print("Máquina arrojo Cara")
        if num1==num2:
          gana=apuesta*2
          pres=pres+gana
          count=count+1
          print("Gano, se le sumará a la apuesta", gana)
        else:
          pierde=pres-apuesta
          count=count+1
          print("Perdío, se le restara a la apuesta", apuesta)
