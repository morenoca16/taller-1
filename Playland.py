edad=int(input("Ingresa tu edad en años: "))
if 0<=edad<=4:
    print("El cliente ingresa gratis")
elif 4<edad<18:
    print("El cliente paga: $20.000")
elif 18<=edad<=60:
    print("El cliente paga: $15.000")
elif edad>60:
    print("El cliente paga: $3.000")
