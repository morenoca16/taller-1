import random
compra = float (input ('Ingresa el valor de la compra: '))
if compra>50000:
  print("Aplica dctos")
  descuento=0
  bolita=random.randint(1, 4)
  if bolita==1:
    descuento=compra
    print ('Bolita blanca su compra es gratis')
  if bolita==2:
    descuento=compra*0.1
    print ('Bolita roja obtienes 10% de dcto en tu compra.')
  if bolita==3:
    descuento=compra*0.30
    print ('Bolita azul obtienes 30% de dcto en tu compra.')
  if bolita==4:
     descuento=compra*0.50
     print ('Bolita amarilla obtienes 50% de dcto en tu compra.')
     pagar=compra-descuento
     print ('Valor a pagar: ', pagar)
     print ('Valor de descuento: ', descuento)
else:
  print("Dcto aplica para compras superiores a 50 mil")
