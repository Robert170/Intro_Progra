
Valor=int(input("¿Que numero quieres multiplicar?"))
Veces=int(input("¿Porque numero lo quieres multiplicar?"))
Num=0
Suma=0

def Multiplicacion(Valor,Veces,Num,Suma):

	if(Num!=Veces):
		Suma=Suma+Valor
		Num=Num+1
		Multiplicacion(Valor,Veces,Num,Suma)

	elif(Num==Veces):
		print(Suma)
		return

if (__name__ == '__main__'):
	Multiplicacion(Valor,Veces,Num,Suma)	
