class Persona:
    __nombre = None
    __edad = None
    def __init__(self):
       print("Persona")

    def getNombre(self):
       return self._nombre

    def setNombre(self,nombre):
       self._nombre = nombre 

    def getEdad(self):
       return self._edad

    def setEdad(self,edad):
       self._edad = edad

objeto_persona = Persona()
#print(objeto_persona.nombre)
objeto_persona.nombre = "Hola"
print(objeto_persona.nombre)
objeto_persona.setNombre("Edwin")
print(objeto_persona.getNombre())
objeto_persona.setEdad("19")
print(objeto_persona.getEdad())


class Alumno(Persona):
    __nombre = None
    __matricula = None
    def __init__(self):
       print("Alumno")

    def getNombre(self):
       return self._nombre

    def setNombre(self,nombre):
       self._nombre = nombre 

    def getMatricula(self):
       return self._matricula

    def setMatricula(self,matricula):
       self._matricula = matricula

objeto_alumno = Alumno()
#print(objeto_alumno.nombre)
objeto_alumno.nombre = "Hola"
print(objeto_alumno.nombre)
objeto_alumno.setNombre("Dejah")
print(objeto_alumno.getNombre())
objeto_alumno.setMatricula("172212783")
print(objeto_alumno.getMatricula())


