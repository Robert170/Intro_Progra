
def Año():

	Name=(input("introduce nombre:"))
	Age=int(input("introduce tu edad:"))

	print("Hola",Name)
	Year=2018

	while Age<=100:
		Year=Year+1
		Age=Age+1

		if Age==100:
			print("Vas cumplir 100 años en:",Year)

if (__name__ == '__main__'):
	Año()		
