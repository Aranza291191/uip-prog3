import os
Nombre={}
Nummero={}
MiDirectorio = {}

Escoger = 0

while  Escoger != 5 :

    print ("***Mi Directorio Telefonico***")
    print ("1. Imprimir Numeros de Telefono: ")
    print ("2. Agregar Numeros de Telefono: ")
    print ("3. Quitar Numeros de Telefono: ")
    print ("4. Buscar Numeros de Telefono: ")
    print ("5. Salir")

    Escoger = input ("Opcion a Escoger: ")

    if Escoger == "1" : 
        print ("Numero" + str (MiDirectorio)+Nombre)

    elif Escoger == "2" :
	Nombre = input ("Ingresar Nombre: ")
	Numero = (input ("Ingresar Numero:"))
	MiDirectorio [Nombre] = Numero

    elif Escoger == "3" :
	Nombre = input ("Ingresar Nombre a Eliminar: ")
	del MiDiccionario [Nombre]

    elif Escoger == "4" :
	 Nombre = input ("Ingresar El Numero a Buscar: ")
	 print (Numero + str(MiDirectorio[Nombre])+Nomvre)


    elif Escoger = "5" :

os.system ("cls")
