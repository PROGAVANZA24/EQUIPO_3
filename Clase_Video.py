class Clase_Video:
    def __init__(self, id_video, nombre, url, fecha_publi):
        self.__id_video = id_video
        self.__nombre = nombre 
        self.__url = url
        self.__fecha_publi = fecha_publi

    def guardar(self,id_video, nombre, url,fecha_publi):
        lista = [id_video,"|", nombre,"|", url,"|",fecha_publi]
        f = open("c:/Archivos/Clonados/EQUIPO_3/Clase_Video.txt","a",enconding="utf8")
        for numero in lista:
             f.write(str(numero)+'\n')
        f.close

    def consultar_todo(self):
        f = open("c:/Archivos/Clonados/EQUIPO_3/Clase_Video.txt",encoding="utf8")

        print(f"{'id_video':<10}{'nombre':>10}{'url':>10}{'fecha_publi':>10}")
        for linea in f:
            datos = linea.strip().split('|')
            print(f'{int(datos[0]):<15}{datos[1]:>10}{datos[2]:>10}{datos[3]:>10}')

        f.close

    def consultar_por_id(self, id_video):
        f = open("c:/Archivos/Clonados/EQUIPO_3/Clase_Video.txt",encoding="utf8")

        print(f"{'IDCTV':<10}{'IDCT':>10}{'IDVIDEO':<10}")
        for linea in f:
            datos = linea.strip().split('|')
            if int(datos[0]) == id_video:
                print(f'{int(datos[0]):<15}{datos[1]:>10}{datos[2]:>10}{datos[3]:>10}')

        f.close