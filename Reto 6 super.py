import random
count=0
total=0
descuento=0
for i in range(1,3,1):
    #Aquí instruciones que voy a repetir
    price=int(input("Ingrese el precio del producto" ))
    cantidad=int(input("Ingrese la cantidad del producto" ))
    count=count+1
    sub=price*cantidad
    total=total+sub
print("Total a pagar", total)


bolita=random.randint(1, 4)
if bolita==1:
    descuento=total
    print ('Bolita blanca su compra es gratis')
if bolita==2:
    descuento=total*0.1
    print ('Bolita roja obtienes 10% de dcto en tu compra.')
if bolita==3:
    descuento=total*0.30
    print ('Bolita azul obtienes 30% de dcto en tu compra.')
if bolita==4:
    descuento=total*0.50
    print ('Bolita amarilla obtienes 30% de dcto en tu compra.')
pagar=total-descuento
print ('Valor a pagar: ', pagar)
print ('Valor de descuento: ', descuento)

pago=int(input("ingrese con cuanto paga"))
cambio=pago-pagar

print("Su cambio es: ", cambio)
