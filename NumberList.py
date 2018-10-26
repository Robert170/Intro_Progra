
NumberList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(NumberList)

NumberList2 = []

for Elemento in NumberList:
	if(Elemento < 5):
		print(Elemento)	
		NumberList2.append(Elemento)	
		
print(NumberList2)

NumLimt=int(input("introduce el numero limite:"))

NumberList3=[]

for Elemento in NumberList:
	if(Elemento < NumLimt):
		NumberList3.append(Elemento)	
		
print(NumberList3)
	
def Fibonacci():
	ListFibo=[]
	Numero1=0
	Numero2=1
	NumFibo=int(input("introduce hasta que numero quieres que se haga la sucecion fibonacci:"))
	for Valor in range(0,NumFibo):

		if(Valor==0):
			Numero2=0

		if(Valor==1):
			Numero2=1

		if(Valor==2):
			Numero1=0		

		Resultado=Numero1+Numero2
		Numero1=Numero2
		Numero2=Resultado

		ListFibo.append(Resultado)
		
	print(ListFibo)

if (__name__ == '__main__'):
	Fibonacci()		
	print("Lista Fibonacci terminada")
			
