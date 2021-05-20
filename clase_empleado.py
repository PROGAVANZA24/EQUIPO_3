class Empleado:
    def __init__(self,id_empleado,nombre,direccion):
        self.__id_empleado = id_empleado
        self.__nombre = nombre
        self.__direccion = direccion
    
    def guardar(self,id_empleado,nombre,direccion):
        lista = [id_empleado,"|",nombre,"|",direccion]
        f = open("c:/Archivos/Clonados/EQUIPO_3/Empleados.txt","a",encoding="utf8")
        for numero in lista:
             f.write(str(numero)+'\n')
        f.close

    def consultar_todo(self):
        f = open("c:/Archivos/Clonados/EQUIPO_3/Empleados.txt",encoding="utf8")

        print(f"{'ID Empleado':<10}{'Nombre':>10}{'Direccion':>10}")
        for linea in f:
            datos = linea.strip().split('|')
            print(f'{int(datos[0]):<15}{datos[1]:>10}{datos[2]:>10}')

        f.close

    def consultar_por_id(self,id_empleado):
        f = open("c:/Archivos/Clonados/EQUIPO_3/Empleados.txt",encoding="utf8")

        print(f"{'ID Empleado':<10}{'Nombre':>10}{'Direccion':>10}")
        for linea in f:
            datos = linea.strip().split('|')
            if int(datos[0]) == id_empleado:
                print(f'{int(datos[0]):<15}{datos[1]:>10}{datos[2]:>10}')

        f.close