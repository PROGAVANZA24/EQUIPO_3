class Tema:
    def __init__(self,id_tema,tema):
        self.__id_tema = id_tema
        self.__tema = tema
    
    def guardar(self,id_tema,tema):
        lista = [id_tema,"|", tema]
        f = open("c:/Archivos/Clonados/EQUIPO_3/Tema.txt","a",encoding="utf8")
        for numero in lista:
             f.write(str(numero)+'\n')
        f.close

    def consultar_todo(self):
        f = open("c:/Archivos/Clonados/EQUIPO_3/Tema.txt",encoding="utf8")

        print(f"{'ID Tema':<10}{'Tema':>10}")
        for linea in f:
            datos = linea.strip().split('|')
            print(f'{int(datos[0]):<15}{datos[1]:>10}')

        f.close

    def consultar_por_id(self,id_tema):
        f = open("c:/Archivos/Clonados/EQUIPO_3/Tema.txt",encoding="utf8")

        print(f"{'ID Tema':<10}{'Tema':>10}")
        for linea in f:
            datos = linea.strip().split('|')
            if int(datos[0]) == id_tema:
                print(f'{int(datos[0]):<15}{datos[1]:>10}')

        f.close