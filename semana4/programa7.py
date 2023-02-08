"""
    Programa7
    Nombre:Oscar Adahir GS.
    Fecha:7/02/2023.
    Descripcion: 
"""
numero1 = int(input("numero 1: "))
numero2 = int(input("numero 2: "))
#version 1
def mayor (numero1, numero2):
  if numero1 > numero2:
    print(numero1)
  if numero2 > numero1:
    print(numero2)
  if numero1 == numero2:
    print(None)
#version 2
if numero2 > numero1:
    print(numero2)
if numero1 > numero2:
    print(numero1)
    