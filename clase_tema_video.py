class Curso_Tema_Video:
    def __init__(self, id_CTV, id_CT, id_video):
     self.__id_CTV = id_CTV
     self.__id_CT = id_CT
     self.__id_video = id_video

    def guardar(self,id_CTV, id_CT, id_video):
        lista = [id_CTV,"|", id_CT,"|", id_video]
        f = open("c:/Archivos/Clonados/EQUIPO_3/clase_tema_video.txt","a",encoding="utf8")
        for numero in lista:
             f.write(str(numero)+'\n')
        f.close

    def consultar_todo(self):
        f = open("c:/Archivos/Clonados/EQUIPO_3/clase_tema_video.txt",encoding="utf8")

        print(f"{'idCTV':<10}{'idCT':>10}{'idVIDEO':>10}")
        for linea in f:
            datos = linea.strip().split('|')
            print(f'{int(datos[0]):<15}{datos[1]:>10}{datos[2]:>10}')

        f.close

    def consultar_por_id(self, id_CTV):
        f = open("c:/Archivos/Clonados/EQUIPO_3/clase_tema_video.txt",encoding="utf8")

        print(f"{'IDCTV':<10}{'IDCT':>10}{'IDVIDEO':<10}")
        for linea in f:
            datos = linea.strip().split('|')
            if int(datos[0]) == id_CTV:
                print(f'{int(datos[0]):<15}{datos[1]:>10}{datos[2]:>10}')

        f.close