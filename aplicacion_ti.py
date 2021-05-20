from clase_tema import Tema
from Clase_Video import Clase_Video
from clase_tema_video import Curso_Tema_Video
from Curso_Tema import Curso_Tema
from clase_curso import Curso
from clase_empleado import Empleado

clasePruebaTema = Tema("","")
clasePruebaVideo = Clase_Video("","","","")
clasePruebaTemaVideo = Curso_Tema_Video("","","")
clasePruebaCursoTema = Curso_Tema("","","")
clasePruebaCurso = Curso("","","")
clasePruebaEmpleado = Empleado("","","")

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
    elif resp2 == 3:
        print("Ingrese el ID que desea consultar")
        idConsulta = int(input())
        clasePruebaTema.consultar_por_id(idConsulta)
    else:
        print("Opcion invalida")
elif resp1.upper() == "B":
    if resp2 == 1:
        print("Ingrese el nombre del video nuevo")
        nomVideo = str(input())
        print("Ingrese el ID del video nuevo")
        idVideo = int(input())
        print("Ingrese la URL del nuevo video")
        urlVideo = str(input())
        print("Ingrese la fecha de publicacion (dd/mm/aa)")
        fechaVideo = str(input())
        nuevoVideo = Clase_Video(idVideo,nomVideo,urlVideo,fechaVideo)
        nuevoVideo.guardar()
    elif resp2 == 2:
        clasePruebaVideo.consultar_todo()
    elif resp2 == 3:
        print("Ingrese el ID que desea consultar")
        idConsulta = int(input())
        clasePruebaVideo.consultar_por_id(idConsulta)
    else:
        print("Opcion invalida")
elif resp1.upper() == "C":
    if resp2 == 1:
        print("Ingrese el ID del Curso Tema Video nuevo")
        idCTV = str(input())
        print("Ingrese el ID del Curso Tema nuevo")
        idCT = str(input())
        print("Ingrese el ID del Video nuevo")
        idV = str(input())
        nuevoCTV = Curso_Tema_Video(idCTV,idCT,idV)
        nuevoCTV.guardar()
    elif resp2 == 2:
        clasePruebaTemaVideo.consultar_todo()
    elif resp2 == 3:
        print("Ingrese el ID que desea consultar")
        idConsulta = int(input())
        clasePruebaTemaVideo.consultar_por_id(idConsulta)
    else:
        print("Opcion invalida")
elif resp1.upper() == "D":
    if resp2 == 1:
        print("Ingrese el ID del Curso Tema nuevo")
        idCursoTema = str(input())
        print("Ingrese el ID del Curso nuevo")
        idCurso = str(input())
        print("Ingrese el ID del Tema nuevo")
        idT = str(input())
        nuevoCursoTema = Curso_Tema_Video(idCursoTema,idCurso,idT)
        nuevoCursoTema.guardar()
    elif resp2 == 2:
        clasePruebaCursoTema.consultar_todo()
    elif resp2 == 3:
        print("Ingrese el ID que desea consultar")
        idConsulta = int(input())
        clasePruebaCursoTema.consultar_por_id(idConsulta)
    else:
        print("Opcion invalida")