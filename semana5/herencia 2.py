"""
    Programa: herencia2 
    Nombre:Oscar Adahir GS.
    Fecha:19/02/2023.
    Descripcion:creacion de objetos
"""
class Persona:# crea clase persona 

    def __init__(self):# define, declara para persona
         __nombre = None# declara variable
         print("Persona")# imprime persona 

class Alumno(Persona):# crea la clase alumno
    def __init__(self):# define y declara  para alumno
          super().__init__()# accesede a l clase persona
          print("Alumno")# imprime alumno

objeto_persona = Persona()# da valor a la clase person
objeto_alumno = Alumno()# da valor a la clase alumno

objeto_persona.nombre = "Dejah Thoris"# da valor a nombre de la clase persona
print(objeto_persona.nombre)# imprime nombre

objeto_alumno.nombre = "John Carter"# da valor a nombre de la clase alumno
print(objeto_alumno.nombre)# imprime nombre

objeto_alumno.email = "John@gmail.com.mx"# da valor a email
print(objeto_alumno.email)# imprime email 

print(dir(objeto_persona))# muestra lo que hay dentro de la clase persona
print(dir(objeto_alumno))# muestra lo hay dentro de la clase alumno
