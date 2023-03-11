import random
dado1=random.randint(1,6) 
print("Dado 1: " , dado1)
dado2=random.randint(1,6)
print("Dado 2: ",dado2)

if dado1==1 and dado2==1:
    print("SACASTE PAR DE 1:¡GANASTE!")
elif dado1+dado2==3:
    print("SACASTE SUMATORIA DE 3: ¡GANASTE!")
elif dado1+dado2==11:
    print("SACASTE SUMATORIA DE 11: ¡GANASTE!")
elif dado1+dado2==2:
    print("SACASTE SUMATORIA DE 2: ¡GANASTE!")
elif dado1+dado2==12:
    print("SACASTE SUMATORIA DE 12: ¡GANASTE!")
elif dado1+dado2==7:
    print("SACASTE SUMATORIA DE 7: ¡GANASTE!")
else:
    print("LOS SIENTO ¡PERDISTE!")