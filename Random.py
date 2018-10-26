
import random
	
RanList1=[]

from random import shuffle
RanList1 = [[Valor] for Valor in range(0,25)]
shuffle(RanList1)

print(RanList1)
print("-----------------------------")

RanList2=[]

from random import shuffle
RanList2 = [[Valor] for Valor in range(0,40)]
shuffle(RanList2)

print(RanList2)	
print("-----------------------------")

def Combinacion():

	RanList3=[]

	for Valor in RanList1:
		if(Valor not in RanList3 and Valor in RanList2):
			RanList3.insert(0,Valor)

	print(RanList3)

if (__name__ == '__main__'):
	Combinacion()		
