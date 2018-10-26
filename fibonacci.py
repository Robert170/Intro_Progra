print("Secuencia Fibonacci")

def Fibonacci():
	Numero1=0
	Numero2=1

	for Valor in range(0,10):
		if(Valor==0):
			Numero2=0

		if(Valor==1):
			Numero2=1

		if(Valor==2):
			Numero1=0		

		Resultado=Numero1+Numero2
		Numero1=Numero2
		Numero2=Resultado
		
		print(Resultado)

if (__name__ == '__main__'):
	Fibonacci()				
	print("Fin de la Secuencia Fibonacci")
