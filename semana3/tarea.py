"""
    Programa5
    Nombre:Oscar Adahir GS.
    Fecha:30/01/2023.
    Descripcion: calcula el area y  perimetro de un triangulo
"""
medida1= int(input("Medida 1: "))# pide un valor int o float
medida2= int(input("medida 2: "))# pide un valor int o float
base= int(input("Base: "))# pide un valor int o float
resultado= medida1 + medida2 + base # da la suma de los lados
print("Perimetro: ",resultado)# imprimeperimetro
altura= int(input("Altura: "))# pide un valor int o float
calculo=  (base* altura)/2 # calcula el area
print("Area: ", calculo) # da el resultado de caalulo del area 
