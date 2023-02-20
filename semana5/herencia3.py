"""
    Programa: herencia3 
    Nombre:Oscar Adahir GS.
    Fecha:15/02/2023.
    Descripcion:creacion de objeto
"""
class Persona:# se crea una clase
    __nombre = None# se declara v
    __edad = None# declara la esas

    def __init__(self):# conductor
        print("Persona")# imprime persona 

    def getNombre(self):# se obtiene un elemento 
        return self._nombre# retorna un nombre 

    def setNombre(self, nombre):# almacena nombre
        self._nombre = nombre# hace referencia para elementos de un objeto 

    def getEdad(self):# representa el conjunto edad
        return self._edad# retorna edad

    def setEdad(self, edad):# alamcena edad
        self._edad = edad# referencia para elementos de objeto


objeto_persona = Persona()# crea objeto
print(objeto_persona.nombre)# imprime nombre
objeto_persona.nombre = "Hola"# da valor a nombre
print(objeto_persona.nombre)# imprime nombre
objeto_persona.setNombre("Oscar")# da valor a nombre
print(objeto_persona.getNombre())# imprime lo almacenado 
objeto_persona.setEdad("19")# da valor a edad
print(objeto_persona.getEdad())# imprime edad


class Alumno(Persona):# crea clase alumno
    __nombre = None# define variable
    __matricula = None# define variable

    def __init__(self):# conductor
        print("Alumno")# imprime alumno

    def getNombre(self):# se obtiene elemento
        return self._nombre# retorna nombre

    def setNombre(self, nombre):# alamcena nombre 
        self._nombre = nombre# referencia al elemento del objeto

    def getMatricula(self):# se obtine elemeto
        return self._matricula# retorna matricula 

    def setMatricula(self, matricula):# alamcena matricula 
        self._matricula = matricula# referencia al elemento del objeto


objeto_alumno = Alumno()# crea objeto
print(objeto_alumno.nombre)# imprime onombre
objeto_alumno.nombre = "Hola"# da valor a nombre
print(objeto_alumno.nombre)# imprime nombre del objeto alumno
objeto_alumno.setNombre("Dejah")# almacena nombre
print(objeto_alumno.getNombre())# imprime nombre
objeto_alumno.setMatricula("172212783")# alamaen  valor a matricula
print(objeto_alumno.getMatricula())# imprime el  valor de matricula 
