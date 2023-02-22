num1=int(input("ingrese 0 para sello y 1 para cara: "))

if num1==0:
    print("Cara")
else:
    print("Sello")

import random
num2=random.randint(0,1)

if num2==0:
    print("Máquina arrojo Cara")
else:
    print("Máquina arrojo Sello")

if num1==num2:
     print("Gano")
else:
    print("Perdío")