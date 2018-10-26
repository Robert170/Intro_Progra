import random
import os

print("Vamos a jugar a el ahorcado")


ListPalabra=[]
ListOculta=[]
Vidas=6

def Main():

	Archivo=open("sowpods.txt", "r")

	ListPalabra = Archivo.readlines()
	Palabra=random.choice(ListPalabra)
	print(Palabra)
	Archivo.close()



if (__name__ == '__main__'):
	Main()			



	