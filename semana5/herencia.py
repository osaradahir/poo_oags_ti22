"""
    Programa: herencia 
    Nombre:Oscar Adahir GS.
    Fecha:15/02/2023.
    Descripcion:creacion de objeto
"""
class Alumno:# crea la clase alumno
    __nombre = None# da valor a nombre
    __matricula = None# da valor a matricula
    __carrera= None# da valor a carrera
    def __init__(self):# define clase
          print("Alumno")# immprime alumno
    def setNombre(self,nombre):# almacena nommbre
        self.__nombre = nombre# referncia al elemto del objeto
    def setMatricula(self,matricula):# alamcena matricula
        self.__matricula = matricula# referencia el elemento
    def setCarrera(self,carrera):# almacena carrera 
        self.__carrera = carrera# referencia al elemento 

    def getNombre(self):# obtine elemento
        return self.__nombre# retorna nombre
    def getMatricula(self):# obtine elemento
        return self.__matricula# retorna matricula
    def getCarrera(self):# obtine elemento
        return self.__carrera# retorna carrera

dejah = Alumno()# crea objeto
dejah.setNombre("liz")# da valor a nombre
print(dejah.getNombre())# imprime nombre
dejah.setMatricula("1210889775")# da valor a matricula
print(dejah.getMatricula())# imprime matricula
dejah.setCarrera("Informatica")# da valor a carrera
print(dejah.getCarrera())# imprime carrera 
