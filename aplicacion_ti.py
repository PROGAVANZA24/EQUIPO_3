from clase_tema import Tema
from Clase_Video import Clase_Video
from clase_tema_video import Curso_Tema_Video
from Curso_Tema import Curso_Tema
from clase_curso import Curso
from clase_empleado import Empleado

clasePruebaTema = Tema("","")
clasePruebaClsVid = Clase_Video("","","","")
print("------------------------------")
print("Bienvenido al Menu Principal!")
print("Seleccione la opcion deseada.")
print("a. Tema")
print("b. Video")
print("c. Curso Tema Video")
print("d. Curso Tema")
print("e. Cursos")
print("f. Empleados")
print("------------------------------")

resp1 = str(input())

print("------------------------------")
print("Seleccione una opcion.")
print("1. Guardar")
print("2. Consultar todo")
print("3. Consultar por ID")

resp2 = int(input())

if resp1.upper() == "A":
    if resp2 == 1:
        print("Ingrese el nombre del tema nuevo")
        nomTema = str(input())
        print("Ingrese el ID del tema nuevo")
        idTema = int(input())
        nuevoTema = Tema(idTema,nomTema)
        nuevoTema.guardar()
    elif resp2 == 2:
        clasePruebaTema.consultar_todo()