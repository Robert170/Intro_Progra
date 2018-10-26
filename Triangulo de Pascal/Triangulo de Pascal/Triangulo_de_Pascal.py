import math

def Triangulo():

    print("Triangulo de Pascal")
    Piso=int(input("Numeros de pisos que quieres que tenga tu triangulo:"))
    
    ListPascal=[1]
    ListValor=[1]
    Long=len(ListPascal)

    if(Piso==0):
        ListPascal.clear()
        print(ListPascal)

    elif(Piso==1):
        print(ListPascal)


    else:
        for Veces in range(0,Piso):

            Largo=len(ListValor)
            print(ListPascal)

            for Valor in range(0,Largo):
                ListValor=ListPascal.copy()
                if(Largo>=Piso):
                    return

                if(Largo==1):
                    ListPascal.append(1)
                    ListValor=ListPascal.copy()

                if(Largo==2):
                    Resultado=ListValor[Valor]+ListValor[Valor]
                    ListPascal.pop()
                    ListPascal.append(Resultado)
                    ListPascal.append(1)
                    ListValor=ListPascal.copy()
                    Largo=len(ListValor)
                    print(ListPascal)
                    if(Largo>=Piso):
                        return

                if(Largo>=3 and Piso>=4):
                    Largo=4
                    if(Largo>3):
                       
                        for Num in range(1,Piso):
                            Long=len(ListValor)

                            ListPascal=[1]


                            for Est in range(0,Long-1):
                                
                                Resultado=ListValor[Est]+ListValor[Est+1]
                                ListPascal.append(Resultado)
                                if(Long>=Piso):
                                    return
                                
                            ListPascal.append(1)
                            print(ListPascal)
                            Long=len(ListPascal)
                            ListValor=ListPascal.copy()
                     
  
if (__name__ == '__main__'):
	Triangulo()			



    
