"""
    Programa: herencia1
    Nombre:Oscar Adahir GS.
    Fecha:15/02/2023.
    Descripcion:creacion de objeto
"""
class Persona:# crea un clase
    __email = None# declara variable
    __nombre = None# declara variable
    def __init__(self):# define int
          print("Persona")# imprime persona 
    def setEmail(self,email):# alamacena email
        self.__email = email# llama clase 
    def setNombre(self,nombre):# alamacena nombre
        self.__nombre = nombre# llama nombre

    def getEmail(self):# accede a email
       return self.__email# retorna email
    def getNombre(self):# accede a nombre 
       return self.__nombre# retorna nombre


dejah = Persona()# crea objeto
dejah.setNombre("Dejah")# da valor a nombre 
print(dejah.getNombre())# imprime nommbre
dejah.setEmail("Dejah@utectulancingo.edu.mx")# da valor a email
print(dejah.getEmail())# imprime email