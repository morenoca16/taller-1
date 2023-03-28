nums=[]
n= int(input("Cuantos números ingresarás"))
i=0
for i in range(0,n):
    val=float(input("Valor número: "))
    nums.append(val)
    i=i+1
    prom=sum(nums)/ len (nums)
    nums.append(val)
    promedio=i/len(nums)
print('el promedio que dio fue: ',promedio)
if prom<3.0:
    print=("Reprobaste")
elif prom <=4.0:
    print=("Reprobaste")
elif prom >4.0:
    print=("Aprobaste con buenos resultados")
else:
    print("Opción es invalida")