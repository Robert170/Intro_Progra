import random
import os

def Marcador():
    with open("Marcador.txt","w") as f:
        global Jugador1Puntaje
        global Jugador2Puntaje
        global MaquinaPuntaje
        global EmpatePuntaje
        f.write("Jugador1""\n")
        f.write(str(Jugador1Puntaje)+"\n")
        f.write("Jugador2""\n")
        f.write(str(Jugador2Puntaje)+"\n")
        f.write("Maquina""\n")
        f.write(str(MaquinaPuntaje)+"\n")
        f.write("Empate""\n")
        f.write(str(EmpatePuntaje))


def Main():
    myline = ""
    global Jugador1Puntaje
    global Jugador2Puntaje
    global MaquinaPuntaje
    global EmpatePuntaje
    with open("Marcador.txt") as f:
        myline = f.readline()
        while myline:
            if ("Jugador1" in myline):
                myline=f.readline()
                Jugador1Puntaje=int()
            elif ("Jugador2" in myline):
                myline=f.readline()
                Jugador1Puntaje=int()
            elif ("Maquina" in myline):
                myline=f.readline()
                Jugador1Puntaje=int()
            elif ("Empate" in myline):
                myline=f.readline()
                Jugador1Puntaje=int()
            myline=f.readline()

                     
    print("Vamos a jugar al juego del gato""\n")
    print("Para seleccionar el modo 1 jugador presione 1")
    print("Para seleccionar el modo 2 jugadores presione 2""\n")
    Eleccion=input("¿Qué quiere hacer?:")	
    
    if(Eleccion=="1"):
        Uno()

    elif(Eleccion=="2"):
        Dos()

    else:
        print("---Por favor elija una de las opciones que se la dan------""\n")	
        Main()
       
def Uno():
    Nombre1=input("Escriba su nombre J1:")
    J1=1
    Pc=0
    ListSuperior=["-","-","-"]
    ListCentral=["-","-","-"]
    ListInferior=["-","-","-"]
    ListLetra=["A","B","C"]
    List1=[1]
    List2=[2]
    List3=[3]
    global Jugador1Puntaje
    global MaquinaPuntaje
    global EmpatePuntaje

    #Ganar Horizontal en X o O
    ListR1=["X","X","X"]
    ListR2=["O","O","O"]

    #Ganar Vertical a la izquierda solo X
    ListR3=["X","O","-"]
    ListR4=["X","-","O"]
    ListR5=["X","O","X"]
    ListR6=["X","X","O"]
    ListR7=["X","-","-"]
    ListR8=["X","O","O"]
    ListR9=["X","-","X"]
    ListR10=["X","X","-"]

    #Ganar Vertical en el centro solo X
    ListR11=["-","X","-"]
    ListR12=["O","X","-"]
    ListR13=["-","X","O"]
    ListR14=["O","X","O"]
    ListR15=["X","X","-"]
    ListR16=["-","X","X"]
    ListR17=["X","X","O"]
    ListR18=["O","X","X"]

    #Ganar Vertical a la derecha solo X
    ListR19=["-","-","X"]
    ListR20=["-","O","X"]
    ListR21=["O","-","X"]
    ListR22=["O","O","X"]
    ListR23=["X","-","X"]
    ListR24=["-","X","X"]
    ListR25=["O","X","X"]
    ListR26=["X","O","X"]

    #Ganar Vertical a la izquierda solo O
    ListR3a=["O","X","-"]
    ListR4a=["O","-","X"]
    ListR5a=["O","X","O"]
    ListR6a=["O","O","X"]
    ListR7a=["O","-","-"]
    ListR8a=["O","X","X"]
    ListR9a=["O","-","O"]
    ListR10a=["O","O","-"]

    #Ganar Vertical en el centro solo O
    ListR11a=["-","O","-"]
    ListR12a=["X","O","-"]
    ListR13a=["-","O","X"]
    ListR14a=["X","O","X"]
    ListR15a=["O","O","-"]
    ListR16a=["-","O","O"]
    ListR17a=["O","O","X"]
    ListR18a=["X","O","O"]

    #Ganar Vertical a la derecha solo O
    ListR19a=["-","-","O"]
    ListR20a=["-","X","O"]
    ListR21a=["X","-","O"]
    ListR22a=["X","X","O"]
    ListR23a=["O","-","O"]
    ListR24a=["-","O","O"]
    ListR25a=["X","O","O"]
    ListR26a=["O","X","O"]





    ListJugada=[]
    ListPc=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
    Turno=0
    Num=1


    print(ListLetra,"\n")
    print(ListSuperior,List1)
    print(ListCentral,List2)
    print(ListInferior,List3)

    while Num>=0:
        while (J1==1):
            print("Turno de",Nombre1)
            Jugada=input("Escribe una coordenada, ejemplo A1, si escribe una coordenada no existente pierdes turno:")
            Jugada=Jugada.upper()


            if (Jugada in ListJugada):
                print("Esa jugada ya se puso elige otra, si eliges otra jugada que ya se uso pierdes turno""\n")
                Jugada=input("Escribe una coordenada, ejemplo A1:")
                Jugada=Jugada.upper()

            if(Jugada in ListJugada):
                 print("Turno perdido, sigue la computadora")
                 Pc=1
                 break


            if(Jugada not in ListJugada):

                if(Jugada=="A1"):
                    ListSuperior[0]="X"

                elif(Jugada=="A2"):
                    ListCentral[0]="X"
        
                elif(Jugada=="A3"):
                    ListInferior[0]="X"

                elif(Jugada=="B1"):
                    ListSuperior[1]="X"

                elif(Jugada=="B2"):
                    ListCentral[1]="X"
        
                elif(Jugada=="B3"):
                    ListInferior[1]="X"

                elif(Jugada=="C1"):
                    ListSuperior[2]="X"

                elif(Jugada=="C2"):
                    ListCentral[2]="X"
        
                elif(Jugada=="C3"):
                    ListInferior[2]="X"

                else:
                    print("Turno perdido, sigue la computadora")
                    Pc=1
                    break

            print(ListLetra,"\n")
            print(ListSuperior,List1)
            print(ListCentral,List2)
            print(ListInferior,List3)
            
            J1=0
            Pc=1
            Turno=Turno+1
            ListJugada.append(Jugada)
            ListPc.remove(Jugada)

            if(ListSuperior==ListR1):
                print(Nombre1,"gano")
                Jugador1Puntaje=Jugador1Puntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if (Continuar=="SI"):
                    os.system("cls")
                    Main()
            
                elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return


            if(ListCentral==ListR1):
                 print(Nombre1,"gano")
                 Jugador1Puntaje=Jugador1Puntaje+1
                 Marcador()
                 Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                 Continuar=Continuar.upper()
                 if(Continuar=="SI"):
                     os.system("cls")
                     Main()

                 elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return
             

            if(ListInferior==ListR1):
                 print(Nombre1,"gano")
                 Jugador1Puntaje=Jugador1Puntaje+1
                 Marcador()
                 Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                 Continuar=Continuar.upper()
                 if(Continuar=="SI"):
                    os.system("cls")
                    Main()

                 elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return


            if((ListSuperior==ListR3 or ListSuperior==ListR4 or ListSuperior==ListR5 or ListSuperior==ListR6 or ListSuperior==ListR7 or ListSuperior==ListR8 or ListSuperior==ListR9 or ListSuperior==ListR10) and (ListCentral==ListR3 or ListCentral==ListR4 or ListCentral==ListR5 or ListCentral==ListR6 or ListCentral==ListR7 or ListCentral==ListR8 or ListCentral==ListR9 or ListCentral==ListR10) and (ListInferior==ListR3 or ListInferior==ListR4 or ListInferior==ListR5 or ListInferior==ListR6 or ListInferior==ListR7 or ListInferior==ListR8 or ListInferior==ListR9 or ListInferior==ListR10)): 
               print(Nombre1,"gano")
               Jugador1Puntaje=Jugador1Puntaje+1
               Marcador()
               Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
               Continuar=Continuar.upper()
               if(Continuar=="SI"):
                   os.system("cls")
                   Main()

               elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return

            if((ListSuperior==ListR11 or ListSuperior==ListR12 or ListSuperior==ListR13 or ListSuperior==ListR14 or ListSuperior==ListR15 or ListSuperior==ListR16 or ListSuperior==ListR17 or ListSuperior==ListR18) and (ListCentral==ListR11 or ListCentral==ListR12 or ListCentral==ListR13 or ListCentral==ListR14 or ListCentral==ListR15 or ListCentral==ListR16 or ListCentral==ListR17 or ListCentral==ListR18) and (ListInferior==ListR11 or ListInferior==ListR12 or ListInferior==ListR13 or ListInferior==ListR14 or ListInferior==ListR15 or ListInferior==ListR16 or ListInferior==ListR17 or ListInferior==ListR18)):
                 print(Nombre1,"gano")
                 Jugador1Puntaje=Jugador1Puntaje+1
                 Marcador()
                 Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                 Continuar=Continuar.upper()
                 if(Continuar=="SI"):
                     os.system("cls")
                     Main()

                 elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return

            if((ListSuperior==ListR19 or ListSuperior==ListR20 or ListSuperior==ListR21 or ListSuperior==ListR22 or ListSuperior==ListR23 or ListSuperior==ListR24 or ListSuperior==ListR25 or ListSuperior==ListR26) and (ListCentral==ListR19 or ListCentral==ListR20 or ListCentral==ListR21 or ListCentral==ListR22 or ListCentral==ListR23 or ListCentral==ListR24 or ListCentral==ListR25 or ListCentral==ListR26) and (ListInferior==ListR19 or ListInferior==ListR20 or ListInferior==ListR21 or ListInferior==ListR22 or ListInferior==ListR23 or ListInferior==ListR24 or ListInferior==ListR25 or ListInferior==ListR26)):
                print(Nombre1,"gano")
                Jugador1Puntaje=Jugador1Puntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if(Continuar=="SI"):
                    os.system("cls")
                    Main()

                elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return

            if((ListSuperior==ListR19 or ListSuperior==ListR20 or ListSuperior==ListR21 or ListSuperior==ListR22 or ListSuperior==ListR23 or ListSuperior==ListR24 or ListSuperior==ListR25 or ListSuperior==ListR26) and (ListCentral==ListR11 or ListCentral==ListR12 or ListCentral==ListR13 or ListCentral==ListR14 or ListCentral==ListR15 or ListCentral==ListR16 or ListCentral==ListR17 or ListCentral==ListR18) and (ListInferior==ListR3 or ListInferior==ListR4 or ListInferior==ListR5 or ListInferior==ListR6 or ListInferior==ListR7 or ListInferior==ListR8 or ListInferior==ListR9 or ListInferior==ListR10)):
                print(Nombre1,"gano")
                Jugador1Puntaje=Jugador1Puntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if(Continuar=="SI"):
                    os.system("cls")
                    Main()

                elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return

            if((ListSuperior==ListR3 or ListSuperior==ListR4 or ListSuperior==ListR5 or ListSuperior==ListR6 or ListSuperior==ListR7 or ListSuperior==ListR8 or ListSuperior==ListR9 or ListSuperior==ListR10) and (ListCentral==ListR11 or ListCentral==ListR12 or ListCentral==ListR13 or ListCentral==ListR14 or ListCentral==ListR15 or ListCentral==ListR16 or ListCentral==ListR17 or ListCentral==ListR18) and (ListInferior==ListR19 or ListInferior==ListR20 or ListInferior==ListR21 or ListInferior==ListR22 or ListInferior==ListR23 or ListInferior==ListR24 or ListInferior==ListR25 or ListInferior==ListR26)):
                print(Nombre1,"gano")
                Jugador1Puntaje=Jugador1Puntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if(Continuar=="SI"):
                    os.system("cls")
                    Main()

                elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return
                   
            if(Turno==9):
                print("Es un empate")
                EmpatePuntaje=EmpatePuntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if (Continuar=="SI"):
                    os.system("cls")
                    Main()
            
                elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return

        while (Pc==1):
            print("Turno de la computadora")
            Jugada=random.choice(ListPc)

            if(Jugada=="A1"):
                ListSuperior[0]="O"

            if(Jugada=="A2"):
                ListCentral[0]="O"
        
            if(Jugada=="A3"):
                ListInferior[0]="O"

            if(Jugada=="B1"):
                ListSuperior[1]="O"

            if(Jugada=="B2"):
                ListCentral[1]="O"
        
            if(Jugada=="B3"):
                ListInferior[1]="O"

            if(Jugada=="C1"):
                ListSuperior[2]="O"

            if(Jugada=="C2"):
                ListCentral[2]="O"
        
            if(Jugada=="C3"):
                ListInferior[2]="O"

            print(ListLetra,"\n")
            print(ListSuperior,List1)
            print(ListCentral,List2)
            print(ListInferior,List3)

            J1=1
            Pc=0
            Turno=Turno+1
            ListJugada.append(Jugada)
            ListPc.remove(Jugada)
            

            if(ListSuperior==ListR2):
                print("La computadora gano")
                MaquinaPuntaje=MaquinaPuntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if(Continuar=="SI"):
                    os.system("cls")
                    Main()
                elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return

            if(ListCentral==ListR2):
                 print("La computadora gano")
                 MaquinaPuntaje=MaquinaPuntaje+1
                 Marcador()
                 Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                 Continuar=Continuar.upper()
                 if(Continuar=="SI"):
                    os.system("cls")
                    Main()
                 elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return

            if(ListInferior==ListR2):
                 print("La computadora gano")
                 MaquinaPuntaje=MaquinaPuntaje+1
                 Marcador()
                 Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                 Continuar=Continuar.upper()
                 if(Continuar=="SI"):
                    os.system("cls")
                    Main()
                 elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return

            if((ListSuperior==ListR3a or ListSuperior==ListR4a or ListSuperior==ListR5a or ListSuperior==ListR6a or ListSuperior==ListR7a or ListSuperior==ListR8a or ListSuperior==ListR9a or ListSuperior==ListR10a) and (ListCentral==ListR3a or ListCentral==ListR4a or ListCentral==ListR5a or ListCentral==ListR6a or ListCentral==ListR7a or ListCentral==ListR8a or ListCentral==ListR9a or ListCentral==ListR10a) and (ListInferior==ListR3a or ListInferior==ListR4a or ListInferior==ListR5a or ListInferior==ListR6a or ListInferior==ListR7a or ListInferior==ListR8a or ListInferior==ListR9a or ListInferior==ListR10a)): 
               print("La computadora gano")
               MaquinaPuntaje=MaquinaPuntaje+1
               Marcador()
               Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
               Continuar=Continuar.upper()
               if(Continuar=="SI"):
                   os.system("cls")
                   Main()

               elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return

            if((ListSuperior==ListR11a or ListSuperior==ListR12a or ListSuperior==ListR13a or ListSuperior==ListR14a or ListSuperior==ListR15a or ListSuperior==ListR16a or ListSuperior==ListR17a or ListSuperior==ListR18a) and (ListCentral==ListR11a or ListCentral==ListR12a or ListCentral==ListR13a or ListCentral==ListR14a or ListCentral==ListR15a or ListCentral==ListR16a or ListCentral==ListR17a or ListCentral==ListR18a) and (ListInferior==ListR11a or ListInferior==ListR12a or ListInferior==ListR13a or ListInferior==ListR14a or ListInferior==ListR15a or ListInferior==ListR16a or ListInferior==ListR17a or ListInferior==ListR18a)):
                 print("La computadora gano")
                 MaquinaPuntaje=MaquinaPuntaje+1
                 Marcador()
                 Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                 Continuar=Continuar.upper()
                 if(Continuar=="SI"):
                    os.system("cls")
                    Main()
                 elif(Continuar=="SI"):
                     print("Grcias por jugar")
                     return
                

            if((ListSuperior==ListR19a or ListSuperior==ListR20a or ListSuperior==ListR21a or ListSuperior==ListR22a or ListSuperior==ListR23a or ListSuperior==ListR24a or ListSuperior==ListR25a or ListSuperior==ListR26a) and (ListCentral==ListR19a or ListCentral==ListR20a or ListCentral==ListR21a or ListCentral==ListR22a or ListCentral==ListR23a or ListCentral==ListR24a or ListCentral==ListR25a or ListCentral==ListR26a) and (ListInferior==ListR19a or ListInferior==ListR20a or ListInferior==ListR21a or ListInferior==ListR22a or ListInferior==ListR23a or ListInferior==ListR24a or ListInferior==ListR25a or ListInferior==ListR26a)):
                print("La computadora gano")
                MaquinaPuntaje=MaquinaPuntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if(Continuar=="SI"):
                    os.system("cls")
                    Main()

                elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return

            if((ListSuperior==ListR19a or ListSuperior==ListR20a or ListSuperior==ListR21a or ListSuperior==ListR22a or ListSuperior==ListR23a or ListSuperior==ListR24a or ListSuperior==ListR25a or ListSuperior==ListR26a) and (ListCentral==ListR11a or ListCentral==ListR12a or ListCentral==ListR13a or ListCentral==ListR14a or ListCentral==ListR15a or ListCentral==ListR16a or ListCentral==ListR17a or ListCentral==ListR18a) and (ListInferior==ListR3a or ListInferior==ListR4a or ListInferior==ListR5a or ListInferior==ListR6a or ListInferior==ListR7a or ListInferior==ListR8a or ListInferior==ListR9a or ListInferior==ListR10a)):
                print("La computadora gano")
                MaquinaPuntaje=MaquinaPuntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if(Continuar=="SI"):
                    os.system("cls")
                    Main()

                elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return

            if((ListSuperior==ListR3a or ListSuperior==ListR4a or ListSuperior==ListR5a or ListSuperior==ListR6a or ListSuperior==ListR7a or ListSuperior==ListR8a or ListSuperior==ListR9a or ListSuperior==ListR10a) and (ListCentral==ListR11a or ListCentral==ListR12a or ListCentral==ListR13a or ListCentral==ListR14a or ListCentral==ListR15a or ListCentral==ListR16a or ListCentral==ListR17a or ListCentral==ListR18a) and (ListInferior==ListR19a or ListInferior==ListR20a or ListInferior==ListR21a or ListInferior==ListR22a or ListInferior==ListR23a or ListInferior==ListR24a or ListInferior==ListR25a or ListInferior==ListR26a)):
                print("La computadora gano")
                MaquinaPuntaje=MaquinaPuntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if(Continuar=="SI"):
                    os.system("cls")
                    Main()

                elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return

            if(Turno==9):
                print("Es un empate")
                EmpatePuntaje=EmpatePuntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if (Continuar=="SI"):
                    os.system("cls")
                    Main()
            
                elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return



def Dos():
    Nombre1=input("Escriba su nombre J1:")
    Nombre2=input("Escriba su nombre J2:")
    J1=1
    J2=0
    ListSuperior=["-","-","-"]
    ListCentral=["-","-","-"]
    ListInferior=["-","-","-"]
    ListLetra=["A","B","C"]
    List1=[1]
    List2=[2]
    List3=[3]
    global Jugador1Puntaje
    global Jugador2Puntaje
    global EmpatePuntaje
    #Ganar Horizontal en X o O
    ListR1=["X","X","X"]
    ListR2=["O","O","O"]

    #Ganar Vertical a la izquierda solo X
    ListR3=["X","O","-"]
    ListR4=["X","-","O"]
    ListR5=["X","O","X"]
    ListR6=["X","X","O"]
    ListR7=["X","-","-"]
    ListR8=["X","O","O"]
    ListR9=["X","-","X"]
    ListR10=["X","X","-"]

    #Ganar Vertical en el centro solo X
    ListR11=["-","X","-"]
    ListR12=["O","X","-"]
    ListR13=["-","X","O"]
    ListR14=["O","X","O"]
    ListR15=["X","X","-"]
    ListR16=["-","X","X"]
    ListR17=["X","X","O"]
    ListR18=["O","X","X"]

    #Ganar Vertical a la derecha solo X
    ListR19=["-","-","X"]
    ListR20=["-","O","X"]
    ListR21=["O","-","X"]
    ListR22=["O","O","X"]
    ListR23=["X","-","X"]
    ListR24=["-","X","X"]
    ListR25=["O","X","X"]
    ListR26=["X","O","X"]

    #Ganar Vertical a la izquierda solo O
    ListR3a=["O","X","-"]
    ListR4a=["O","-","X"]
    ListR5a=["O","X","O"]
    ListR6a=["O","O","X"]
    ListR7a=["O","-","-"]
    ListR8a=["O","X","X"]
    ListR9a=["O","-","O"]
    ListR10a=["O","O","-"]

    #Ganar Vertical en el centro solo O
    ListR11a=["-","O","-"]
    ListR12a=["X","O","-"]
    ListR13a=["-","O","X"]
    ListR14a=["X","O","X"]
    ListR15a=["O","O","-"]
    ListR16a=["-","O","O"]
    ListR17a=["O","O","X"]
    ListR18a=["X","O","O"]

    #Ganar Vertical a la derecha solo O
    ListR19a=["-","-","O"]
    ListR20a=["-","X","O"]
    ListR21a=["X","-","O"]
    ListR22a=["X","X","O"]
    ListR23a=["O","-","O"]
    ListR24a=["-","O","O"]
    ListR25a=["X","O","O"]
    ListR26a=["O","X","O"]





    ListJugada=[]
    Turno=0
    Num=1


    print(ListLetra,"\n")
    print(ListSuperior,List1)
    print(ListCentral,List2)
    print(ListInferior,List3)

    while Num>=0:
        while (J1==1):
            print("Turno de",Nombre1)
            Jugada=input("Escribe una coordenada, ejemplo A1, si eliges una coordenada no existente pierdes turno:")
            Jugada=Jugada.upper()

            if (Jugada in ListJugada):
                print("Esa jugada ya se puso elige otra, si eliges otra jugada que ya se uso pierdes turno""\n")
                Jugada=input("Escribe una coordenada, ejemplo A1:")
                Jugada=Jugada.upper()

            if(Jugada in ListJugada):
                 print("Turno perdido, sigue",Nombre2)
                 J2=1
                 break

            if(Jugada not in ListJugada):

                if(Jugada=="A1"):
                    ListSuperior[0]="X"

                elif(Jugada=="A2"):
                    ListCentral[0]="X"
        
                elif(Jugada=="A3"):
                    ListInferior[0]="X"

                elif(Jugada=="B1"):
                    ListSuperior[1]="X"

                elif(Jugada=="B2"):
                    ListCentral[1]="X"
        
                elif(Jugada=="B3"):
                    ListInferior[1]="X"

                elif(Jugada=="C1"):
                    ListSuperior[2]="X"

                elif(Jugada=="C2"):
                    ListCentral[2]="X"
        
                elif(Jugada=="C3"):
                    ListInferior[2]="X"
            
                else:
                    print("Turno perdido, sigue",Nombre2)
                    J2=1
                    break

            print(ListLetra,"\n")
            print(ListSuperior,List1)
            print(ListCentral,List2)
            print(ListInferior,List3)
            
            J1=0
            J2=1
            Turno=Turno+1
            ListJugada.append(Jugada)


            if(ListSuperior==ListR1):
                print(Nombre1,"gano")
                Jugador1Puntaje=Jugador1Puntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if (Continuar=="SI"):
                    os.system("cls")
                    Main()
            
                elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return


            if(ListCentral==ListR1):
                 print(Nombre1,"gano")
                 Jugador1Puntaje=Jugador1Puntaje+1
                 Marcador()
                 Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                 Continuar=Continuar.upper()
                 if(Continuar=="SI"):
                     os.system("cls")
                     Main()

                 elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return
             

            if(ListInferior==ListR1):
                 print(Nombre1,"gano")
                 Jugador1Puntaje=Jugador1Puntaje+1
                 Marcador()
                 Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                 Continuar=Continuar.upper()
                 if(Continuar=="SI"):
                    os.system("cls")
                    Main()

                 elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return

            if((ListSuperior==ListR3 or ListSuperior==ListR4 or ListSuperior==ListR5 or ListSuperior==ListR6 or ListSuperior==ListR7 or ListSuperior==ListR8 or ListSuperior==ListR9 or ListSuperior==ListR10) and (ListCentral==ListR3 or ListCentral==ListR4 or ListCentral==ListR5 or ListCentral==ListR6 or ListCentral==ListR7 or ListCentral==ListR8 or ListCentral==ListR9 or ListCentral==ListR10) and (ListInferior==ListR3 or ListInferior==ListR4 or ListInferior==ListR5 or ListInferior==ListR6 or ListInferior==ListR7 or ListInferior==ListR8 or ListInferior==ListR9 or ListInferior==ListR10)): 
               print(Nombre1,"gano")
               Jugador1Puntaje=Jugador1Puntaje+1
               Marcador()
               Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
               Continuar=Continuar.upper()
               if(Continuar=="SI"):
                   os.system("cls")
                   Main()

               elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return

            if((ListSuperior==ListR11 or ListSuperior==ListR12 or ListSuperior==ListR13 or ListSuperior==ListR14 or ListSuperior==ListR15 or ListSuperior==ListR16 or ListSuperior==ListR17 or ListSuperior==ListR18) and (ListCentral==ListR11 or ListCentral==ListR12 or ListCentral==ListR13 or ListCentral==ListR14 or ListCentral==ListR15 or ListCentral==ListR16 or ListCentral==ListR17 or ListCentral==ListR18) and (ListInferior==ListR11 or ListInferior==ListR12 or ListInferior==ListR13 or ListInferior==ListR14 or ListInferior==ListR15 or ListInferior==ListR16 or ListInferior==ListR17 or ListInferior==ListR18)):
                 print(Nombre1,"gano")
                 Jugador1Puntaje=Jugador1Puntaje+1
                 Marcador()
                 Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                 Continuar=Continuar.upper()
                 if(Continuar=="SI"):
                     os.system("cls")
                     Main()

                 elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return

            if((ListSuperior==ListR19 or ListSuperior==ListR20 or ListSuperior==ListR21 or ListSuperior==ListR22 or ListSuperior==ListR23 or ListSuperior==ListR24 or ListSuperior==ListR25 or ListSuperior==ListR26) and (ListCentral==ListR19 or ListCentral==ListR20 or ListCentral==ListR21 or ListCentral==ListR22 or ListCentral==ListR23 or ListCentral==ListR24 or ListCentral==ListR25 or ListCentral==ListR26) and (ListInferior==ListR19 or ListInferior==ListR20 or ListInferior==ListR21 or ListInferior==ListR22 or ListInferior==ListR23 or ListInferior==ListR24 or ListInferior==ListR25 or ListInferior==ListR26)):
                print(Nombre1,"gano")
                Jugador1Puntaje=Jugador1Puntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if(Continuar=="SI"):
                    os.system("cls")
                    Main()

                elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return

            if((ListSuperior==ListR19 or ListSuperior==ListR20 or ListSuperior==ListR21 or ListSuperior==ListR22 or ListSuperior==ListR23 or ListSuperior==ListR24 or ListSuperior==ListR25 or ListSuperior==ListR26) and (ListCentral==ListR11 or ListCentral==ListR12 or ListCentral==ListR13 or ListCentral==ListR14 or ListCentral==ListR15 or ListCentral==ListR16 or ListCentral==ListR17 or ListCentral==ListR18) and (ListInferior==ListR3 or ListInferior==ListR4 or ListInferior==ListR5 or ListInferior==ListR6 or ListInferior==ListR7 or ListInferior==ListR8 or ListInferior==ListR9 or ListInferior==ListR10)):
                print(Nombre1,"gano")
                Jugador1Puntaje=Jugador1Puntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if(Continuar=="SI"):
                    os.system("cls")
                    Main()

                elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return

            if((ListSuperior==ListR3 or ListSuperior==ListR4 or ListSuperior==ListR5 or ListSuperior==ListR6 or ListSuperior==ListR7 or ListSuperior==ListR8 or ListSuperior==ListR9 or ListSuperior==ListR10) and (ListCentral==ListR11 or ListCentral==ListR12 or ListCentral==ListR13 or ListCentral==ListR14 or ListCentral==ListR15 or ListCentral==ListR16 or ListCentral==ListR17 or ListCentral==ListR18) and (ListInferior==ListR19 or ListInferior==ListR20 or ListInferior==ListR21 or ListInferior==ListR22 or ListInferior==ListR23 or ListInferior==ListR24 or ListInferior==ListR25 or ListInferior==ListR26)):
                print(Nombre1,"gano")
                Jugador1Puntaje=Jugador1Puntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if(Continuar=="SI"):
                    os.system("cls")
                    Main()

                elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return

            if(Turno==9):
                print("Es un empate")
                EmpatePuntaje=EmpatePuntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if (Continuar=="SI"):
                    os.system("cls")
                    Main()
            
                elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return
                   

        while (J2==1):
            print("Turno de",Nombre2)
            Jugada=input("Escribe una coordenada, ejemplo A1, si eliges una coordenada no existente pierdes turno:")     
            Jugada=Jugada.upper()

            if (Jugada in ListJugada):
                print("Esa jugada ya se puso elige otra, si eliges otra jugada que ya se uso pierdes turno""\n")
                Jugada=input("Escribe una coordenada, ejemplo A1:")
                Jugada=Jugada.upper()

            if(Jugada in ListJugada):
                 print("Turno perdido, sigue",Nombre1)
                 J1=1
                 break

            if(Jugada not in ListJugada):
                if(Jugada=="A1"):
                    ListSuperior[0]="O"

                elif(Jugada=="A2"):
                    ListCentral[0]="O"
        
                elif(Jugada=="A3"):
                    ListInferior[0]="O"

                elif(Jugada=="B1"):
                    ListSuperior[1]="O"

                elif(Jugada=="B2"):
                    ListCentral[1]="O"
        
                elif(Jugada=="B3"):
                    ListInferior[1]="O"

                elif(Jugada=="C1"):
                    ListSuperior[2]="O"

                elif(Jugada=="C2"):
                    ListCentral[2]="O"
        
                elif(Jugada=="C3"):
                    ListInferior[2]="O"

                else:
                    print("Turno perdido, sigue", Nombre1)
                    J1=1
                    break

            print(ListLetra,"\n")
            print(ListSuperior,List1)
            print(ListCentral,List2)
            print(ListInferior,List3)

            J1=1
            J2=0
            Turno=Turno+1
            ListJugada.append(Jugada)

            if(ListSuperior==ListR2):
                print(Nombre2,"gano")
                Jugador2Puntaje=Jugador2Puntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if(Continuar=="SI"):
                    os.system("cls")
                    Main()
                elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return

            if(ListCentral==ListR2):
                 print(Nombre2,"gano")
                 Jugador2Puntaje=Jugador2Puntaje+1
                 Marcador()
                 Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                 Continuar=Continuar.upper()
                 if(Continuar=="SI"):
                    os.system("cls")
                    Main()
                 elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return

            if(ListInferior==ListR2):
                 print(Nombre2,"gano")
                 Jugador2Puntaje=Jugador2Puntaje+1
                 Marcador()
                 Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                 Continuar=Continuar.upper()
                 if(Continuar=="SI"):
                    os.system("cls")
                    Main()
                 elif(Continuar=="NO"):
                    print("Garcias por jugar")
                    return

            if((ListSuperior==ListR3a or ListSuperior==ListR4a or ListSuperior==ListR5a or ListSuperior==ListR6a or ListSuperior==ListR7a or ListSuperior==ListR8a or ListSuperior==ListR9a or ListSuperior==ListR10a) and (ListCentral==ListR3a or ListCentral==ListR4a or ListCentral==ListR5a or ListCentral==ListR6a or ListCentral==ListR7a or ListCentral==ListR8a or ListCentral==ListR9a or ListCentral==ListR10a) and (ListInferior==ListR3a or ListInferior==ListR4a or ListInferior==ListR5a or ListInferior==ListR6a or ListInferior==ListR7a or ListInferior==ListR8a or ListInferior==ListR9a or ListInferior==ListR10a)): 
               print(Nombre2,"gano")
               Jugador2Puntaje=Jugador2Puntaje+1
               Marcador()
               Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
               Continuar=Continuar.upper()
               if(Continuar=="SI"):
                   os.system("cls")
                   Main()

               elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return

            if((ListSuperior==ListR11a or ListSuperior==ListR12a or ListSuperior==ListR13a or ListSuperior==ListR14a or ListSuperior==ListR15a or ListSuperior==ListR16a or ListSuperior==ListR17a or ListSuperior==ListR18a) and (ListCentral==ListR11a or ListCentral==ListR12a or ListCentral==ListR13a or ListCentral==ListR14a or ListCentral==ListR15a or ListCentral==ListR16a or ListCentral==ListR17a or ListCentral==ListR18a) and (ListInferior==ListR11a or ListInferior==ListR12a or ListInferior==ListR13a or ListInferior==ListR14a or ListInferior==ListR15a or ListInferior==ListR16a or ListInferior==ListR17a or ListInferior==ListR18a)):
                 print(Nombre2,"gano")
                 Jugador2Puntaje=Jugador2Puntaje+1
                 Marcador()
                 Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                 Continuar=Continuar.upper()
                 if(Continuar=="SI"):
                    os.system("cls")
                    Main()
                 elif(Continuar=="SI"):
                     print("Gracias por jugar")
                     return
                

            if((ListSuperior==ListR19a or ListSuperior==ListR20a or ListSuperior==ListR21a or ListSuperior==ListR22a or ListSuperior==ListR23a or ListSuperior==ListR24a or ListSuperior==ListR25a or ListSuperior==ListR26a) and (ListCentral==ListR19a or ListCentral==ListR20a or ListCentral==ListR21a or ListCentral==ListR22a or ListCentral==ListR23a or ListCentral==ListR24a or ListCentral==ListR25a or ListCentral==ListR26a) and (ListInferior==ListR19a or ListInferior==ListR20a or ListInferior==ListR21a or ListInferior==ListR22a or ListInferior==ListR23a or ListInferior==ListR24a or ListInferior==ListR25a or ListInferior==ListR26a)):
                print(Nombre2,"gano")
                Jugador2Puntaje=Jugador2Puntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if(Continuar=="SI"):
                    os.system("cls")
                    Main()

                elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return

            if((ListSuperior==ListR19a or ListSuperior==ListR20a or ListSuperior==ListR21a or ListSuperior==ListR22a or ListSuperior==ListR23a or ListSuperior==ListR24a or ListSuperior==ListR25a or ListSuperior==ListR26a) and (ListCentral==ListR11a or ListCentral==ListR12a or ListCentral==ListR13a or ListCentral==ListR14a or ListCentral==ListR15a or ListCentral==ListR16a or ListCentral==ListR17a or ListCentral==ListR18a) and (ListInferior==ListR3a or ListInferior==ListR4a or ListInferior==ListR5a or ListInferior==ListR6a or ListInferior==ListR7a or ListInferior==ListR8a or ListInferior==ListR9a or ListInferior==ListR10a)):
                print(Nombre2,"gano")
                Jugador2Puntaje=Jugador2Puntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if(Continuar=="SI"):
                    os.system("cls")
                    Main()

                elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return

            if((ListSuperior==ListR3a or ListSuperior==ListR4a or ListSuperior==ListR5a or ListSuperior==ListR6a or ListSuperior==ListR7a or ListSuperior==ListR8a or ListSuperior==ListR9a or ListSuperior==ListR10a) and (ListCentral==ListR11a or ListCentral==ListR12a or ListCentral==ListR13a or ListCentral==ListR14a or ListCentral==ListR15a or ListCentral==ListR16a or ListCentral==ListR17a or ListCentral==ListR18a) and (ListInferior==ListR19a or ListInferior==ListR20a or ListInferior==ListR21a or ListInferior==ListR22a or ListInferior==ListR23a or ListInferior==ListR24a or ListInferior==ListR25a or ListInferior==ListR26a)):
                print(Nombre2,"gano")
                Jugador2Puntaje=Jugador2Puntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if(Continuar=="SI"):
                    os.system("cls")
                    Main()

                elif(Continuar=="NO"):
                    print("Gracias por jugar")
                    return

            if(Turno==9):
                print("Es un empate")
                EmpatePuntaje=EmpatePuntaje+1
                Marcador()
                Continuar=input("¿Quieres volver a intentarlo? SI/NO:")
                Continuar=Continuar.upper()
                if (Continuar=="SI"):
                    os.system("cls")
                    Main()
            
                elif(Continuar=="NO"):
                    print("Grcias por jugar")
                    return
                
             


if (__name__ == '__main__'):
    Jugador1Puntaje=0
    Jugador2Puntaje=0
    MaquinaPuntaje=0
    EmpatePuntaje=0
    Main()			