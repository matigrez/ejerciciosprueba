

def mostrar_menu():
    print ("\n---INGRESO DE USUARIOS---")
    print ("1. Ingresar usuario ")
    print ("2. Buscar usuario ")
    print ("3. Eliminar usuario ")
    print ("4. Salir")

def agregar_usuario(usuario):
    nombre = input("Ingrese nombre del usuario: ").strip()
    if nombre in usuario:
        print("Ingrese un nombre correcto ")    
    if nombre.isdigit () or nombre == "":
        print ("[ERROR]Ingrese un valor correcto")
        return
    while True:
        sexo = input("Ingrese sexo del usuario: ").strip().upper()
        if sexo != "F" and sexo != "M":
            print ("[Error] Ingrese un valor correcto ")
            continue
        else:
            break
    while True:
        contraseña = input("Ingrese una contraseña: ")
        if len(contraseña) < 8:
            print("[ERROR] ingrese un valor correcto.")
            continue
        if "" in contraseña:
            rint("[ERROR] ingrese un valor correcto.")
            continue
        tiene_numero = False
        tiene_letra = False

        for caracter in contraseña:
            if caracter.isdigit():
                tiene_numero = True
            if caracter.isalpha():
                tiene_letra = True

        if tiene_numero and tiene_letra:
            print("Contraseña aceptada")
            usuario[nombre] = [sexo],[contraseña]
            break

        else:
            print("[ERROR] Ingrese valor correcto")
            

    nuevo_usuario = {"nombre": nombre, "sexo": sexo, "contraseña": contraseña}
    print (f"\n Usuario {nombre} creado correctamente")
    return nuevo_usuario
def buscar_usuario(usuario):
    buscar = input("Ingrese el nombre del Usuario ")
    if buscar in usuario:
        print(f"el sexo del usuario {usuario[buscar[0]]} y la contraseña del ususario {ususario[buscar[1]]}")
    else: 
        print("usuario no encontrado.")

def eliminar_usuario(usuario):
    eliminar = input("ingrese nombre del usuario a eliminar.")
    if eliminar in usuario:
        del usuario{eliminar}
        print ("usuario eliminado")
    else:
        print("no se pudo eliminar al usuario")























usuario = {}    
while True:
    mostrar_menu()
    try:
        menu = int(input("Ingrese una opcion: "))
        break
    except ValueError:
            print("Ingreese una opcion correcta")
    if menu == 1:
        agregar_usuario(usuario)
    elif menu == 2:
        buscar_usuario(usuario)
    elif menu == 3:
        eliminar_usuario(usuario)
    elif menu == 4:
        print("Programa terminado.")
        break
