class Curso:
    def __init__(self, id_curso, descripcion, empleado):
        self.__id_curso = id_curso
        self.__descripcion = descripcion 
        self.__empleado = empleado

    def guardar(self,id_curso, descripcion, empleado):
        lista = [id_curso,"|", descripcion,"|", empleado]
        f = open("c:/Archivos/Clonados/EQUIPO_3/clase_curso.txt","a",enconding="utf8")
        for numero in lista:
             f.write(str(numero)+'\n')
        f.close

    def consultar_todo(self):
        f = open("c:/Archivos/Clonados/EQUIPO_3/clase_curso.txt",encoding="utf8")

        print(f"{'idCurso':<10}{'Descripcion':>10}{'Empleado':>10}")
        for linea in f:
            datos = linea.strip().split('|')
            print(f'{int(datos[0]):<15}{datos[1]:>10}{datos[2]:>10}')

        f.close

    def consultar_por_id(self, id_curso):
        f = open("c:/Archivos/Clonados/EQUIPO_3/clase_curso.txt",encoding="utf8")

        print(f"{'idCurso':<10}{'Descripcion':>10}{'Empleado':<10}")
        for linea in f:
            datos = linea.strip().split('|')
            if int(datos[0]) == id_curso:
                print(f'{int(datos[0]):<15}{datos[1]:>10}{datos[2]:>10}')

        f.close