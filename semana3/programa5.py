"""
    Programa5
    Nombre:Oscar Adahir GS.
    Fecha:31/01/2023.
    Descripcion: calcula el area, perimetro de un circulo y cuadrado.
"""
radio=int(input("Radio: "))# solicita el radio de un circulo
PI=3.1416# constante de PI
perimetro_circulo= 2*radio*PI# calacula el perimetro de un circulo
area_circulo= PI*radio**2# calcula el area de un circulo 
print("El perimetro del circulo es: ", perimetro_circulo)# imprime el perimetro de un circulo
print("El area del circulo es: ", area_circulo)# imprime el area de un circulo
lado=int(input("Medida lado: "))# solicita el lado de un cuadrado
perimetro_cuadrado= lado*4# calcula perimetro de un cuadrado
area_cuadrado= lado*lado # calcula area de un cuadrado
print("El perimetro del cuadrado es: ", perimetro_cuadrado)# imprime el perimetro de un cuadrado
print("El area del cuadrado es: ", area_cuadrado)# imprime el area de un cuadrado
