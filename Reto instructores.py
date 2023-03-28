instructores2503816 ={}

while True:
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")

  
    opcion = int(input("¿Qué opción deseas realizar?: "))
    if opcion == 1:
        nombre = input("Nombre del instructor: ")
        if nombre in instructores2503816:
            print(f"Materia: {instructores2503816[nombre]['materia']}")
            print(f"Teléfono: {instructores2503816[nombre]['telefono']}")
            opcion = input("Pulsa 's' si quieres modificar datos. Otra tecla para continuar.")
            if opcion == "s":
               materia= input("Ingrese materia: ")
               instructores2503816[nombre]=materia
               telefono= input("Ingrese número de télefono: ")
               instructores2503816[nombre]=telefono
        else:
          materia= input("Ingrese materia: ")
          telefono= input("Ingrese número de télefono: ")
          instructores2503816[nombre] = {'materia': materia, 'telefono': telefono}
          print("Intructor añadido")
    elif opcion == 2:
        texto = input("Nombre del instructor a buscar:")
        print("Se encontraron los siguientes resultados:")    
        for nombre, info in instructores2503816.items():
            if nombre.startswith(texto):
                print(f"{nombre}: {info['materia']}, {info['telefono']}")
        else:
          print("Ingrese opción 1 para añadir el instructor")
      
    elif opcion == 3:
        nombre = input("Nombre del instructor a eliminar:")    
        if nombre in instructores2503816:
            opcion = input("Pulsa 's' si quieres borrarlo!!!. Otra tecla para continuar.")
            if opcion == "s":
                del instructores2503816 [nombre]
                print(f"{nombre} ha sido eliminado de la lista.")
        else:
            print("No existe en la lista")
    elif opcion == 4:
        for nombre, info in instructores2503816.items():
            print(f"{nombre}: {info['materia']}, {info['telefono']}")
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")