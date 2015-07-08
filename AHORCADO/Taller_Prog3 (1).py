import platform,os, sys, time,csv,contextlib

cPalabraIni=''
cLetraEntro=''
iLetraLargo=0
iIntenfalla=0
bloop=True
lst_Espacio=[]
lst_Entrada=[]
Lst_ImagenA= ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

def Clear():
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')

def Print_Menu(cPalabraIni, lst_Espacio):
	Clear()
#	print(cPalabraIni)
	Imprima_Espacios(lst_Espacio)
	print(30 * "-" , "AHORCADO" , 30 * "-")
	print("1. Introducir Palabra ")
	print("2. Jugar")
	print("0. Salir")
	print(68 * "-")
	return 
	
def Bienvenida():
	Clear()
	print(30 * "-" , "AHORCADO" , 30 * "-")
	print("Listo para un ahorcado?")
	print("Te explico brevemente las reglas:")
	print(68 * "-")
	print("Este es un juego de 2 personas, si.. 2 personas.")
	print("La primera persona ingresa una palabra, y la segunda tiene que adivinar.") 
	print("El resto es igual a cualquier otro ahorcado.") 
	print(68 * "-")
	print("---DIVIERTANSE---")
	time.sleep(0)

def Imprima_Espacios(lst_Espacio):
	print(lst_Espacio)

def Captura(cPalabraIni,lst_Espacio):
	cPalabraIni = str.upper(str(input('Ingrese la palabra: ')))
	for i in range(len(cPalabraIni)):		
		lst_Espacio.append('_')
	return (cPalabraIni, lst_Espacio)

def Jugar(cPalabraIni,lst_Entrada,lst_Espacio,iIntenfalla):
#	while iIntentos!=0:
	cLetraEntro = str.upper(str(input('Ingrese la Letra: ')))
	if len(cLetraEntro) != 1:
		print('Solo puede digitar una letra.')
	else:
		if cLetraEntro not in cPalabraIni:
			iIntenfalla=iIntenfalla+1
			print(Lst_ImagenA[iIntenfalla])
		else:
#			print(cPalabraIni)
#			print(len(cPalabraIni))
			for j in range(len(cPalabraIni)):
				if cPalabraIni[j]==cLetraEntro:
					lst_Espacio[j]=cLetraEntro
#					print(j)
#					print(cPalabraIni[j])
		
#		Imprima_Espacios(lst_Espacio)
		if lst_Espacio == cPalabraIni:
			print('Se acabo el juego! Ganaste')
	time.sleep(2)
	return (lst_Entrada,lst_Espacio,iIntenfalla)
	
iChoice = 0    
Bienvenida()
cPalabraIni=''
cLetraEntro=''
while bloop:
	Print_Menu(cPalabraIni, lst_Espacio)
	print(Lst_ImagenA[iIntenfalla])
	iChoice = int(input('Enter su seleccion [0-2]: '))
	if iChoice == 1:
		cPalabraIni,lst_Espacio=Captura(cPalabraIni,lst_Espacio)
	elif iChoice == 2:
		lst_Entrada, lst_Espacio,iIntenfalla= Jugar(cPalabraIni,lst_Entrada,lst_Espacio,iIntenfalla)
		print(Lst_ImagenA[iIntenfalla])
	elif iChoice == 0:
		break

