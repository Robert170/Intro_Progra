
print("Triangulo de Pascal")
Piso=int(input("Numeros de pisos que quieres que tenga tu triangulo:"))

def Triangulo():
    
    ListPascal=[]
    ListValor=[]
    ListValor2=[]
    Elemento=1
    Suma=0
    
    if(Piso==1):
        ListPascal.append(Elemento)
        print(ListPascal)

    if(Piso==2):
        ListPascal.append(Elemento)
        print(ListPascal)
        ListPascal.append(Elemento)
        print(ListPascal)

    if(Piso==3):
        ListPascal.append(Elemento)
        print(ListPascal)
        ListPascal.append(Elemento)
        print(ListPascal)
        Elemento=Elemento+1
        ListPascal.insert(1,Elemento)
        print(ListPascal)

    if(Piso==4):
        ListPascal.append(Elemento)
        print(ListPascal)
        ListPascal.append(Elemento)
        print(ListPascal)
        Elemento=Elemento+1
        ListPascal.insert(1,Elemento)
        print(ListPascal)
        Elemento=Elemento+1
        ListPascal.pop(1)
        ListPascal.insert(1,Elemento)
        ListPascal.insert(1,Elemento)
        print(ListPascal)

    if(Piso>=5):
        ListPascal.append(Elemento)
        print(ListPascal)

        ListPascal.append(Elemento)
        print(ListPascal)

        Elemento=Elemento+1
        ListPascal.insert(1,Elemento)
        print(ListPascal)

        Elemento=Elemento+1
        ListPascal.pop(1)
        ListPascal.insert(1,Elemento)
        ListPascal.insert(1,Elemento)
        print(ListPascal)

        for Veces in range((Piso)-1,Piso):
            ListValor=ListPascal[0:2]
            ListValor2=ListPascal[1:3]
            for X in ListValor:
                Suma=Suma+X
            ListValor.clear()
            ListValor.append(Suma)
            ListPascal.remove(Elemento)
            ListPascal.insert(1,ListValor[0])
            ListPascal.remove(Elemento)
            ListPascal.insert(1,ListValor[0])
            for X in ListValor2:
                Suma=Suma+X
            ListValor2.clear()
            ListValor2.append(Suma)
            ListPascal.insert(2,ListValor2[0])
            print(ListPascal)

        





if (__name__ == '__main__'):
	Triangulo()			



    