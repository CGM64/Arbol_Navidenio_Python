import os

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

os.system("clear")

print("\t\tCharly GM Systems\n\n")
tamanio = int(input("  Ingrese el tamaño del árbol: "))

os.system("clear")

#Ramas
for i in range(tamanio):
	if(tamanio <= 25):
		if i == 0:
			print(YELLOW + "  " * (tamanio - i)+"*" * (2 * i + 1))
		
		if i >= 2:
			print(GREEN + "  " * (tamanio - i)+"*" * (2 * i + 1))
	elif(tamanio > 25):
		if i == 0:
			print(YELLOW + "  " * (tamanio - i)+"*" * (2 * i + 1))
		
		if i >= 2:
			print(GREEN + "  " * (tamanio - i)+"*" * (2 * i + 1))

#Tronco
for j in range(tamanio):
	print(MAGENTA + " " * (tamanio + tamanio) + "|  " * 2)

print(RED + "\n\t¡Felices fiestas te desea Charly GM!")

print(RESET)