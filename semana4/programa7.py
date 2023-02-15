"""
    Programa7
    Nombre:Oscar Adahir GS.
    Fecha:7/02/2023.
    Descripcion: condiciona que numero es mayor 
"""
numero1 = int(input("numero 1: "))# pide un numero
numero2 = int(input("numero 2: "))# pide un numero
#version 1
def mayor (numero1, numero2):# define un una funcion
  if numero1 > numero2:#  da una condicion 
    print(numero1)# imprimprime numero 1
  if numero2 > numero1:# da una condicion 
    print(numero2)# imprimprime numero 2
  if numero1 == numero2:# da una condicion 
    print(None)# imprimprime None
#version 2
if numero2 > numero1:# da una condicion 
    print(numero2)# imprimprime numero 2
if numero1 > numero2:# da una condicion 
    print(numero1)# imprimprime numero 1
    