class Tema:
    def __init__(self,id_tema,nombre):
        self.__id_tema = id_tema
        self.__nombre = nombre
    
    def guardar(self):
        lista = [1,"Programacion"]
        f = open("./EQUIPO_3/archivos_texto/Tema.txt","w",enconding="utf8")
        for numero in lista:
             f.write(str(numero)+'\n')
        f.close

    def consultar_todo(self):
        print(f'Informacion del tema; id_tema:{self.__id_tema}, nombre:{self.__nombre}')