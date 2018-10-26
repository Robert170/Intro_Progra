
def Divisores():

	Div=[]

	Resultado=0
	NumDiv=int(input("introduce el numero que quieras saber sus divisores:"))
	for Valor in range (1,NumDiv):

		if(NumDiv%Valor==0):
		
			Div.append(Valor)

	Div.append(NumDiv)

	print(Div)	

if (__name__ == '__main__'):
	Divisores()			
	print("Estos son sus numeros divisores")
			
