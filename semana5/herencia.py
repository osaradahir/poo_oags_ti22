"""
    Programa: herencia 
    Nombre:Oscar Adahir GS.
    Fecha:15/02/2023.
    Descripcion:creacion de objeto
"""
class Alumno:
    __nombre = None
    __matricula = None
    __carrera= None
    def __init__(self):
          print("Alumno")
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setMatricula(self,matricula):
        self.__matricula = matricula
    def setCarrera(self,carrera):
        self.__carrera = carrera

    def getNombre(self):
        return self.__nombre
    def getMatricula(self):
        return self.__matricula
    def getCarrera(self):
        return self.__carrera

dejah = Alumno()
dejah.setNombre("liz")
print(dejah.getNombre())
dejah.setMatricula("1210889775")
print(dejah.getMatricula())
dejah.setCarrera("Informatica")
print(dejah.getCarrera())
