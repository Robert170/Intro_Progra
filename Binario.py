
print("Programa para convertir un numero decimal a binario y visevrsa" "\n")

def Menu():

	print("Si quiere convertir un numero decimal a binario presione 1")
	print("Si quiere convertir un numero binario a decimal presione 2""\n")
	Eleccion=input("¿Qué quiere hacer?:")	

	if(Eleccion=="1"):
		Binario()

	elif(Eleccion=="2"):
		Decimal()

	else:
		print("---Por favor elija una de las opciones que se la dan------""\n")	
		Menu()
	

def Binario():

	Num=int(input("introduce el numero que quieras combertirlo a binario:"))
	ListBinario=[]

	for Elemento in range(0,Num):

		if(Num%2==0):
			Num=Num/2
			Resultado=0
			ListBinario.insert(0,Resultado)

		elif(Num%2!=0):
			Num=Num/2-0.5
			Resultado=1
			ListBinario.insert(0,Resultado)

		if(Num==0):
			break	

	print(ListBinario)		

def Decimal():
	Bin=input("introduce el numero binario que quieras combertirlo a decimal:")
	
	Resultado=0
	Potencia=0
	Valor=0

	for Elemento in reversed(Bin):

		if(Elemento=="1"):
			Valor=2**Potencia
			Resultado=Valor+Resultado
			Potencia=Potencia+1

		else:
			Valor=Valor+0
			Potencia=Potencia+1

			

	print(Resultado)	




if (__name__ == '__main__'):
	Menu()			