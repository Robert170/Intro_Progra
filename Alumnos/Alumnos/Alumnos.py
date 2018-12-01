
class Alumno:
	def __init__(self, Estudiante : str, Calificacion : float, Grado : str):
		self.Nombre= Estudiante
		self.Promedio= Calificacion
		self.Grupo= Grado
#Diccionario. update
			
def Main():
#Incio del programa y acamodo de los alumnos por grupo	
	#Abrir archivo para obtener datos
	Datos=[]
	Grupo= dict()
	with open("alumnos.txt", "r") as f:
		while f:
			Linea=f.readline()
			Lista=Linea.split()
			if(Lista==[]):
				break
			Datos.append(Alumno(Lista[0], Lista[1], Lista[2]))
#[-1] sirve para acceder al ultomo elemento de una lista
			if(Datos[-1].Grupo in Grupo):
				Grupo[Datos[-1].Grupo].append(Datos[-1])
			else:
				Grupo[Datos[-1].Grupo]=[]
				Grupo[Datos[-1].Grupo].append(Datos[-1])
#Ciclo para crear y llenar los grupos
	for Llave in Grupo: 
			with open(Llave+".txt", "w") as f:
				Valor=Grupo[Llave]
				for Variables in Valor:
					f.writelines(Variables.Nombre+" ")
					f.writelines(Variables.Promedio+" ")
					f.writelines(Variables.Grupo+"\n")

		

	Menu_Principal(Grupo)	

def Menu_Principal(Grupo):
#Inicio del menu principal
	print("Si quieres ver algun grupo pulse: 1","\n")
	print("Si quieres ordenar un archivo de una forma especifica pulse: 2","\n")
	print("Si quiere agregar un nuevo alumno pulse: 3","\n")
	Dato=input("¿Que quieres hacer? ")


	if(Dato=="1"):
		Revisar(Grupo)

	elif(Dato=="2"):
		Ordenar(Grupo)
	
	elif(Dato=="3"):
		Ingresar(Grupo)

	else:
		print("---Por favor elija una de las opciones que se le dan---","\n")
		Menu_Principal(Grupo)

def Revisar(Grupo):
#Funcion para mostrar el contenido de los archivos
	Eleccion=input("Escriba el grupo, ejemplo 2018A, que desea ver: ")
	Eleccion=Eleccion.upper()
	#Si la eleccion esta en el mapa/diccionario entrara en la condicion e imprimira a los alumnos del archivo
	if(Eleccion in Grupo):
		with open(Eleccion+".txt", "r") as f:
			while f:
				Estudiante=f.readline()
				print(Estudiante)
				if(Estudiante==""):
					break
	#Si no se encuentra saltara el mensaje y llamara de nuevo a la funcion 
	elif(Eleccion not in Grupo):
		print("-----Ese grupo no existe----","\n")
		Revisar(Grupo)

	

	print("¿Quieres ver otro grupo? pulse 1","\n")
	print("¿Quieres regresar al menu principal? pulse 2","\n")
	print("Si quiere salir presione otra tecla","\n")
	Opcion=input("¿Que quiere hacer? ")

	if(Opcion=="1"):
		Revisar(Grupo)
		
	elif(Opcion=="2"):
		Menu_Principal(Grupo)

	else:
		return

#Funcion para ingresar nuevo alumno
def Ingresar(Grupo):
	Datos=[]
	Nombre=input("Introdusca el nombre del alumno:")
	if(Nombre==""):
		print("Por favor llene todo o que se le pida")
		Ingresar(Grupo)
	if(Nombre!=""):
		Nombre=Nombre.capitalize()
		Promedio=input("Escriba la calificacion:")
		try:
			Promedio=float(Promedio)
		except:
			print("Porfavor llene correctamente todos los campos y empiece de nuevo")
			Ingresar(Grupo)
		if(Promedio>10):
			print("Escriba una calificacion real")
			Promedio=input("Escriba la calificacion:")
			try:
				Promedio=float(Promedio)
			except:
				print("Porfavor llene correctamente todos los campos y empiece de nuevo")
				Ingresar(Grupo)
			if(Promedio>10):
				print("Empiece de nuevo")
				Ingresar(Grupo)
	Key=input("Ingrese el grupo:")
	if(Key==""):
		print("Por favor llene todo lo que se le pida y empiece de nuevo")
		Ingresar(Grupo)
	Key=Key.upper()
	ListNuevo=[]
	ListNuevo.append(Nombre)
	ListNuevo.append(str(Promedio))
	ListNuevo.append(Key)
	Datos.append(Alumno(ListNuevo[0], ListNuevo[1], ListNuevo[2]))
	
	if(Datos[-1].Grupo in Grupo):
		Grupo[Datos[-1].Grupo].append(Datos[-1])
		with open("alumnos.txt", "a") as f:
			Valor=Grupo[Datos[-1].Grupo]
			f.writelines("\n")
			f.writelines(Valor[-1].Nombre+" ")
			f.writelines(Valor[-1].Promedio)
			f.writelines(" ")
			f.writelines(Valor[-1].Grupo)
		with open(Key+".txt", "a") as f:
			Valor=Grupo[Datos[-1].Grupo]
			f.writelines(Valor[-1].Nombre+" ")
			f.writelines(Valor[-1].Promedio)
			f.writelines(" ")
			f.writelines(Valor[-1].Grupo)
				
	else:
		Grupo[Datos[-1].Grupo]=[]
		Grupo[Datos[-1].Grupo].append(Datos[-1])
		with open("alumnos.txt", "a") as f:
			Valor=Grupo[Datos[-1].Grupo]
			for Variables in Valor:
				f.writelines("\n")
				f.writelines(Variables.Nombre+" ")
				f.writelines(Variables.Promedio)
				f.writelines(" ")
				f.writelines(Variables.Grupo)

	
	print("¿Quieres agregar otro alumno? pulse 1","\n")
	print("¿Quieres regresar al menu principal? pulse 2","\n")
	print("Si quiere salir presino otra tecla","\n")
	Opcion=input("¿Que quiere hacer?" )

	if(Opcion=="1"):
		Ingresar(Grupo)
		
	elif(Opcion=="2"):
		Menu_Principal(Grupo)

	else:
		return


#Funcion para ordenar de forma alfabetica o por promedio un grupo
def Ordenar(Grupo):
	print("¿Quieres ordenar un grupo de manera alfabetica? presione 1","\n")
	print("¿Quieres ordenarlo por calificaciones del mayor al menor? presione 2","\n")
	Eleccion=input("¿Que quiere hacer? ")
	
#Aqui se ordena de forma alffabetica
	if(Eleccion=="1"):	
		Opcion=input("¿Que grupo queries ordenar? ")
		Opcion=Opcion.upper()
		if(Opcion in Grupo):
			Lista_alumno=[]
			Estudiantes=Grupo[Opcion]
			Respaldo=Grupo[Opcion]
			for Elementos in Estudiantes:
				Valor=Elementos.Nombre
				Lista_alumno.append(Valor)
			#Metodo burbuja para ordenar los nombres
			for Repeticion in range(0,len(Lista_alumno)):
				for Dato in range(Repeticion):
					if (Lista_alumno[Dato]>Lista_alumno[Dato+1]):
						G=Lista_alumno[Dato]
						Lista_alumno[Dato]=Lista_alumno[Dato+1]
						Lista_alumno[Dato+1]=G
			for Repeticion in range(0,len(Lista_alumno)):
				for Dato in range(Repeticion):
					if (Lista_alumno[Dato]>Lista_alumno[Dato+1]):
						G=Lista_alumno[Dato]
						Lista_alumno[Dato]=Lista_alumno[Dato+1]
						Lista_alumno[Dato+1]=G
			for Repeticion in range(0,len(Lista_alumno)):
				for Dato in range(Repeticion):
					if (Lista_alumno[Dato]>Lista_alumno[Dato+1]):
						G=Lista_alumno[Dato]
						Lista_alumno[Dato]=Lista_alumno[Dato+1]
						Lista_alumno[Dato+1]=G

		#Abrir archivo, ingresar los alumnos de manera ordenada 
			with open(Opcion+".txt", "w") as f:
				for i in range(0,len(Lista_alumno)):
					for j in range(len(Estudiantes)):
						if(Lista_alumno[i]==Estudiantes[j].Nombre):
							f.writelines(Estudiantes[j].Nombre+" ")
							f.writelines(Estudiantes[j].Promedio+" ")
							f.writelines(Estudiantes[j].Grupo+"\n")
							Grupo[Opcion].remove(Estudiantes[j])
							break
		#Llenar el mapa grupo que fue vaciado previamente
			with open(Opcion+".txt", "r") as f:
				Datos=[]
				while f:
					Linea=f.readline()
					Lista=Linea.split()
					if(Lista==[]):
						break
					Datos.append(Alumno(Lista[0], Lista[1], Lista[2]))
					if(Datos[-1].Grupo in Grupo):
						Grupo[Datos[-1].Grupo].append(Datos[-1])

			
		elif(Opcion not in Grupo):
			print("-----Ese grupo no existe----","\n")
			Ordenar(Grupo)
#Aqui se ordena de por promedios
	elif(Eleccion=="2"):
		Opcion=input("¿Que grupo queries ordenar? ")
		Opcion=Opcion.upper()
		if(Opcion in Grupo):
			Lista_promedio=[]
			Lista_promedio2=[]
			Estudiantes=Grupo[Opcion]
			Respaldo=Grupo[Opcion]
			for Elementos in Estudiantes:
				Valor=Elementos.Promedio
				Lista_promedio.append(float(Valor))
			#Metodo burbuja para ordenar los nombres
			for Repeticion in range(0,len(Lista_promedio)):
				for Dato in range(Repeticion):
					if (Lista_promedio[Dato]<Lista_promedio[Dato+1]):
						G=Lista_promedio[Dato]
						Lista_promedio[Dato]=Lista_promedio[Dato+1]
						Lista_promedio[Dato+1]=G
			for Repeticion in range(0,len(Lista_promedio)):
				for Dato in range(Repeticion):
					if (Lista_promedio[Dato]<Lista_promedio[Dato+1]):
						G=Lista_promedio[Dato]
						Lista_promedio[Dato]=Lista_promedio[Dato+1]
						Lista_promedio[Dato+1]=G
			for Repeticion in range(0,len(Lista_promedio)):
				for Dato in range(Repeticion):
					if (Lista_promedio[Dato]<Lista_promedio[Dato+1]):
						G=Lista_promedio[Dato]
						Lista_promedio[Dato]=Lista_promedio[Dato+1]
						Lista_promedio[Dato+1]=G

			for Elementos in Lista_promedio:
				Lista_promedio2.append(str(Elementos))

		#Abrir archivo, ingresar los alumnos de manera ordenada 
			with open(Opcion+".txt", "w") as f:
				for i in range(0,len(Lista_promedio2)):
					for j in range(len(Estudiantes)):
						if(Lista_promedio2[i]==Estudiantes[j].Promedio):
							f.writelines(Estudiantes[j].Nombre+" ")
							f.writelines(Estudiantes[j].Promedio+" ")
							f.writelines(Estudiantes[j].Grupo+"\n")
							Grupo[Opcion].remove(Estudiantes[j])
							break
		#Llenar el mapa grupo que fue vaciado previamente
			with open(Opcion+".txt", "r") as f:
				Datos=[]
				while f:
					Linea=f.readline()
					Lista=Linea.split()
					if(Lista==[]):
						break
					Datos.append(Alumno(Lista[0], Lista[1], Lista[2]))
					if(Datos[-1].Grupo in Grupo):
						Grupo[Datos[-1].Grupo].append(Datos[-1])


		elif(Opcion not in Grupo):
			print("-----Ese grupo no existe----","\n")
			Ordenar(Grupo)
	
	else:
		print("---Por favor elija una de las opciones que se le dan---","\n")
		Ordenar(Grupo)

	print("¿Quieres ordenar otro grupo? pulse 1","\n")
	print("¿Quieres regresar al menu principal? pulse 2","\n")
	print("Si quiere salir presino otra tecla","\n")
	Opcion=input("¿Que quiere hacer?" )

	if(Opcion=="1"):
		OOrdenar(Grupo)
		
	elif(Opcion=="2"):
		Menu_Principal(Grupo)

	else:
		return

#mandar a llamar la funcion principal
if __name__== "__main__":
	Main()