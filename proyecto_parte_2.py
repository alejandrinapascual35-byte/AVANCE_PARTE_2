#La voutique se llama "MUNDO BELLO" y es olo de esmaltes 
usuarios={}
contraseña_correcta="Boutique1928"
while True:
    codigo=input("Ingrese el codigo de acceso: ")
    if codigo==contraseña_correcta:
        print("Acceso concedido.!Bienvenido a MUNDO BELLO")
        break
    else:
        print("el codigo es incorrecto. Intente de nuevo...")
while True:
    print("  ")
    print(" ____MENU PRINCIPAL___")
    print("1. Registrarse")
    print("2. Iniciar sesion")
    print("3. Salir")
    print("  ")
    opcion=input("Elige una opcion: ")
    if opcion == "1":
        usuario = input ("Ingrese un usuario: ").strip()
        if usuario in usuarios :
            print("Ese usuario ya existe. Intente de nuevo..")
        else:
            contraseña=input("Ingrese una contraseña: ")
            usuarios[usuario]=contraseña
            print("Usuario registrado")
            print(" ")
            print("Venta de esmaltes ")
            inventario=int(input("Ingrese cantidad del inventario: "))
            print("  ")
            print(" ____MENU PRINCIPAL____")
            print("1. Registrar venta")
            print("2. Ver inventario")
            print("3. Salir")
            print("  ")
            op=input("Elige una opcion: ")
            if op== "1":
                cantidad=int(input("Ingresa la cantidad vendida: "))
                if cantidad < 0 :
                    print("No debes vender la cantidad negativa ")
                elif cantidad > inventario :
                    print("No hay suficiente inventario. Inventario actual: ",inventario)
                else:
                    inventario-=cantidad #resta la venta al inventario
                    print("Venta registrada. Nuevo inventario: ", inventario)
            elif op=="2" :
                print("Inventario actual: ",inventario)
            elif op=="3" :
                print("Saliendo del sisitema...")
                break
    elif opcion=="2":
        usuario=input("Usuario: ")
        contraseña=input("Contraseña: ")

        if usuario in usuarios and usuarios[usuario]==contraseña :
            print(f"Inicio sesion exitosamente.¡Bienvenido a MUNDO BELLO..!")
            while True:
                print("  ")
                print("____MENU PRINCIPAL____")
                print("1. Registrar venta")
                print("2. Ver inventario")
                print("3. Salir")
                print("  ")
                opc=input("elige una opcion: ")
                if opc== "1":
                    
                    cantidad=(input("Ingresa la cantidad vendida: "))
                        
                    print("No debes vender la cantidad negativa ")
                    if cantidad > inventario :
                        print("No hay suficiente inventario. Inventario actual: ",inventario)
                    else:
                        inventario-=cantidad #resta la venta al inventario
                        print("Venta registrada. Nuevo inventario: ", inventario)
                    
                elif opc=="2" :
                    print("Inventario actual: ",inventario)
                elif opc=="3" :
                    print("Saliendo del sisitema...")
                break

        else:
            print("Usuario o contraseña incorrecta. Intenta de nuevo")

    elif opcion=="3" :
        print("Saliendo del sistema...")
        break