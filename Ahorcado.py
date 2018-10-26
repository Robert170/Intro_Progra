import random
import sys
import os

print("Vamos a jugar a el ahorcado""\n")

ListPalabra=[]
ListAcertijo=[]
ListOculta=[]
Palabra=""
Intentos=0

def Main():

	Intentos=6

	print("Tienes 6 Intentos")

	Archivo=open("sowpods.txt", "r")
	ListPalabra = Archivo.readlines()
	Palabra=random.choice(ListPalabra)
	Archivo.close()
	ListAcertijo=list(Palabra)

	for Elemento in ListAcertijo:
		ListOculta.append("_")
	print(ListOculta)

	while (Intentos>=-1):

		Letra=input("Escribe una letra en MAYUSCULAS:")

		if(Letra not in ListAcertijo):
			Intentos=Intentos-1
			print("Te equivocaste ahora te quedan",Intentos,"Intentos""\n")

		if(Letra in ListAcertijo):
			for X, Elemento in enumerate(ListAcertijo):
				if Elemento==Letra:
					ListOculta[X]=Letra
			print(ListOculta,"\n")


		if(Intentos==0):
			print("Perdiste, la palabra era:",Palabra)
			break

		elif(ListAcertijo==ListOculta):
			print("Felicidades ganaste")
			break

	Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
	
	if (Continuar=="SI"):
		os.system("cls")
		ListOculta.clear()
		Main()

	elif(Continuar=="NO"):
		print("Grcias por jugar")
		sys.exit()



if (__name__ == '__main__'):
	Main()			
