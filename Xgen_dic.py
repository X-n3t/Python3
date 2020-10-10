#!/usr/bin/python3
# Author: X

print("** Uso: python3 Xgen_dic.py **")
print("Ej. de construcción: range1+range2+range3+cola ==> 010191hi$ .. 311299hi$")
a1, a2 = int(input("Selecciona dos números para el 1º rango :")),int(input())
z1 = int(input("Número de digitos(rellena con ceros los faltantes):"))
b1, b2 = int(input("Selecciona dos números para el 2º rango :")),int(input())
z2 = int(input("Número de digitos(rellena con ceros los faltantes):"))
c1, c2 = int(input("Selecciona dos números para el 3º rango :")),int(input())
z3 = int(input("Número de digitos(rellena con ceros los faltantes):"))
cola = input("Selecciona un patrón fijo para el final")

param1 = range(a1, a2+1)
param2 = range(b1, b2+1)
param3 = range(c1, c2+1)

list1 = []
list2 = []
list3 = []

class Param1:
    def __init__(self):
        self.param1 = param1
        self.ia = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ia == len(self.param1):
            raise StopIteration
        val1 = self.param1[self.ia]
        self.ia = self.ia + 1
        val1 = str(val1)
        val1 = val1.zfill(z1)
        return val1


ID1 = Param1()


for i in ID1:
    list1.append(i)

print(list1)

class Param2:
    def __init__(self):
        self.param2 = param2
        self.ia = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ia == len(self.param2):
            raise StopIteration
        val2 = self.param2[self.ia]
        self.ia = self.ia + 1
        val2 = str(val2)
        val2 = val2.zfill(z2)
        return val2


ID2 = Param2()


for i in ID2:
    list2.append(i)

print(list2)

class Param3:
    def __init__(self):
        self.param3 = param3
        self.ia = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ia == len(self.param3):
            raise StopIteration
        val3 = self.param3[self.ia]
        self.ia = self.ia + 1
        val3 = str(val3)
        val3 = val3.zfill(z3)
        return val3


ID3 = Param3()


for i in ID3:
    list3.append(i)

print(list3)

for i in list1:
    for x in list2:
        for y in list3:
            print(i.rstrip()+x.rstrip()+y.rstrip()+str(cola))
