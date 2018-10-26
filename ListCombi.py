Lista1=[1,1,2,3,5,8,13,21,34,55,89]
Lista2=[1,2,3,4,5,6,7,8,9,10,11,12,13]
Lista3=[]

print(Lista1)
print(Lista2)
print("Vamos a hacer una nueva lista usando los elementos que se repitenen las listas anteriores")

def Combinacion():

	for Elemento in Lista1:
		if(Elemento not in Lista3 and Elemento in Lista2):
			Lista3.append(Elemento)

	print(Lista3)

if (__name__ == '__main__'):
	Combinacion()	 	
	print("Lista ya combinada")
			
	
	
		