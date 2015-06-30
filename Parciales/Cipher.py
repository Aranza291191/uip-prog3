Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
Texto {}
Cifrado {}
servicio cifrado {}

Escoger: 0

while Escoger != 4 :

	#Menu para que el cliente pueda elegir
	print ("***Servicio de Cifrado de Mensaje de Correo Electrónico***")
	print ("1. Introducir Texto")
	print ("2. Cifrar Texto")
	print ("3. Descrifrar Texto")
	print ("4. Imprimir Texto En Pantalla") 
	print ("5. Salir")

	Escoger = input ("Opcion a Escoger: ")

	if Escoger == "1" :
		texto = input ("Ingresar Texto : ")

	
	#Cifra el texto
	elif Escoger == "2" :
		print ("El Texto a Cifrar Es: ")
		Cifrado = (texto + 1)

	#Descifra el texto
	elif Escoger == "3" :
		print ("El Texto a Descrifrar Es: ")
		Descifrado = (texto - 1)

	#Imprime El Texto
	elif Escoger == "4" :
		print ("Texto" + str(ServicioCifrado)+ texto)


	#Cierra El Programa
	elif Escoger = "5" :

	os.system ("cls")
