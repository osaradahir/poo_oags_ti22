"""
    Programa8
    Nombre:Oscar Adahir GS.
    Fecha:7/02/2023.
    Descripcion: mayor de un numero tratndo defirndo "mayor" como numero 1 y numero 2. 
"""
#numero1 = int(input("ingrese un numero: "))
#numero2 = int(input("ingrese un numero: "))
def mayor(numero1: int, numero2: int) -> int:# define un una funcion de numeros enteros 
    mayor = None# da una variable 
    if numero1 > numero2: # da una condicion
        mayor = numero1# revisa si la funcion es igual a numero 1
    elif numero2 > numero1:#da una condicion  
        mayor = numero2
    else:#da una condicion  
        mayor = None# revisa si la funcion es igual a numero 1

    return mayor

print(mayor(3,2))# 3
print(mayor(2,3))# 3
print(mayor(3,3))# None
# version  2
def mayor (numero1, numero2): # define un una funcion de numeros  
    if numero1 > numero2:# da una condicion  
        print(numero1)# imprime numero1
    elif numero2 > numero1:#da una condicion  
        print(numero2)# imprime numero2
    else:#da una condicion  
        print(None)# imprime None
    
mayor(3,2)# 3
mayor(2,3)# 3
mayor(3,3)# None