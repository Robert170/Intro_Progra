List = [0,1,2,4,8,12]

print(List)

#Append es una funcion para agregar un elemento al final de la lista
List.append(7)
List.append(10)
List.append(5)

print(List)

#pop sin argumentos elimina el ultimo elemento de la lista 
List.pop()

print(List)

#pop con argumento elimina el elemento que se encuentra en el indice indicado
List.pop(3)

print(List)

#inserta el numero que desees en la posicion que indiques, el primer numero es la posisicion
# y el segundo el numero a insertar
List.insert(0,16)

print(List)

print("El tercer elemnto de mi lista es:", List[2])

for Elemento in List:
	if(Elemento == 10):
		print("El elemento 10 esta en la posicion:",List.index(Elemento))