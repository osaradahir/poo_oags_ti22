"""
    Programa5
    Nombre:Oscar Adahir GS.
    Fecha:30/01/2023.
    Descripcion: calcula el area y  perimetro de un triangulo
"""
lado1= int(input("Lado 1: "))# pide un valor int o float
lado2= int(input("Lado 2: "))# pide un valor int o float
base= int(input("Lado3: "))# pide un valor int o float
perimetro= lado1 + lado2 + base # da la suma de los lados
print("El perimetro del triangulo: ", perimetro)# imprimeperimetro
altura= int(input("Altura del triangulo: "))# pide un valor int o float
area=  (base* altura)/2 # calcula el area
print("El area del triangulo: ", area) # da el resultado de caalulo del area 
