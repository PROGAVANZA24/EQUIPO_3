class Curso_Tema:

    def __init__(self, id_CT, id_curso, id_tema):
        self.__id_CT = id_CT
        self.__id_curso = id_curso 
        self.__id_tema = id_tema

    def guardar(self,id_CT, id_curso, id_tema): 
        lista = [id_CT,"|", id_curso,"|", id_tema]
        f = open("c:/Archivos/Clonados/EQUIPO_3/Curso_Tema.txt","a",encoding="utf8")
        for numero in lista:
             f.write(str(numero)+'\n')
        f.close

    def consultar_todo(self):
        f = open("c:/Archivos/Clonados/EQUIPO_3/Curso_Tema.txt",encoding="utf8")

        print(f"{'ID CT':<10}{'ID Curso':>10} {'ID Tema':<10}")
        for linea in f:
            datos = linea.strip().split('|')
            print(f'{int(datos[0]):<15}{datos[1]:>10} {datos[2]:>10}')

        f.close

    def consultar_por_id(self,id_CT):
        f = open("c:/Archivos/Clonados/EQUIPO_3/Curso_Tema.txt",encoding="utf8")

        print(f"{'ID CT':<10}{'ID Curso':>10} {'ID Tema':<10}")
        for linea in f:
            datos = linea.strip().split('|')
            if int(datos[0]) == id_CT:
                print(f'{int(datos[0]):<15}{datos[1]:>10} {datos[2]:>10}')

        f.close