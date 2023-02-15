"""
    Programa8
    Nombre:Oscar Adahir GS.
    Fecha:07/02/2023.
    Descripcion: mayor de un numero tratndo defirndo "mayor" como numero 1 y numero 2. 
"""
def mayor (numero1, numero2): # define un una funcion de numeros 
    if numero1 > numero2:# da una condicion  
        print(numero1)# imprime numero1
    elif numero2 > numero1:# da una condicion 
        print(numero2)# imprime numero2
    else:# da una condicion 
        print(None)# imprime None
    
mayor(3,2)# 3
mayor(2,3)# 3
mayor(3,3)# None