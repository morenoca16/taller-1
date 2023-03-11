num1=int(input("ingrese 1 para tijera, 2 para papel y 3 para piedra: "))
if num1==1:
    print("tijera")
elif num1==2:
    print("papel")
elif num1==3:
    print("papel")
else:
    print("ingrese número valido")

import random
num2=random.randint(1,3)

if num2==1:
    print("Máquina arrojo tijera")
elif num2==2:
    print("Máquina arrojo papel")
elif num2==3:
    print("Máquina arrojo piedral")

if num1==num2:
     print("Gano")
else:
    print("Perdío")