#conexion a la base de datos

import mysql.connector as mysql

conexion = mysql.connect(
    host = 'localhost',
    port = 3306,
    db = 'sistema_leyes',
    user = 'root',
    password = '1234')

cmd = conexion.cursor()

#cmd.execute("Select * from leyes")


#funcion de menu principal

class Leyes:
    def __init__(self, numero_registro, numero_normativa, fecha, descripcion, normativa_id, categoria_id, jurisdiccion_id):
        self.numero_registro = numero_registro
        self.numero_normativa = numero_normativa
        self.fecha = fecha
        self.descripcion = descripcion
        self.normativa_id = normativa_id
        self.categoria_id = categoria_id
        self.jurisdiccion_id = jurisdiccion_id

    @staticmethod
    def mostrar_registros():
        # Conexión a la base de datos
        db = mysql.connector.connect(
            host="tu_host",
            user="tu_usuario",
            password="tu_contraseña",
            database="sistema_leyes"
        )

        # Obtener cursor
        cursor = db.cursor()

        # Ejecutar consulta SQL
        cursor.execute("SELECT * FROM leyes")

        # Obtener todos los registros
        registros = cursor.fetchall()

        # Mostrar los registros
        for registro in registros:
            print("Número de Registro:", registro[0])
            print("Número de Normativa:", registro[1])
            print("Fecha:", registro[2])
            print("Descripción:", registro[3])
            print("ID de Normativa:", registro[4])
            print("ID de Categoría:", registro[5])
            print("ID de Jurisdicción:", registro[6])
            print("--------------------")

        # Cerrar cursor y conexión a la base de datos
        cursor.close()
        db.close()

        #conexion a la base de datos

import mysql.connector as mysql

conexion = mysql.connect(
    host = 'localhost',
    port = 3306,
    db = 'sistema_leyes',
    user = 'root',
    password = 'root')

cmd = conexion.cursor()

#cmd.execute("Select * from leyes")


#funcion de menu principal


def seleccion_usuario():
    print('Por favor ingrese el numero de la opción que desea realizar.')
    menu = ['1 – Mostrar todas las normativas en el registro.', '2 – Buscar una normativa.', '3 – Agregar una normativa.',
            '4 – Modificar un registro.', '5 – Eliminar un registro.', '6 - Salir del programa']

    for i in menu:
        print(i)

    print('------------------------')

    eleccion_usuario = input('Ingrese una opción: ')

    if eleccion_usuario == '1':
        #Se muestran todas las normativas

        print('Se muestran todas las leyes'),
        leyes = Leyes(numero_normativa=None,fecha=None,descripcion=None,normativa_id=None,categoria_id=None,jurisdiccion_id=None)
        leyes.mostrar_registros(),
        print('------------------------'),
        return seleccion_usuario()
    elif eleccion_usuario == '2':
        #Se inicia funcion de buscador

        print('Se da la opcion de escribir al usuario')
        print('------------------------')
        return seleccion_usuario()
    elif eleccion_usuario == '3':
        #Se dan al usuario los pasos para cargar un nuevo registro

        print('Se ha agregado un registro de forma exitosa')
        print('------------------------')
        return seleccion_usuario()
    elif eleccion_usuario == '4':
        #Se da la opcion al usuario de seleccionar que registro quiere modificar

        print('Se ha modificado un registro')
        print('------------------------')
        return seleccion_usuario()
    elif eleccion_usuario == '5':
        #Se pregunta al usuario que registro quiere eliminar

        print('Se ha eliminado un registro')
        print('------------------------')
        return seleccion_usuario()
    elif eleccion_usuario == '6':
        print('Gracias por utilizar el sistema de gestión de normativas')
        return False

    else:
        print('"', eleccion_usuario, '" no es una opcion valida')
        print('------------------------')
        return seleccion_usuario()



#menu de inicio

print('Bienvenido al sistema de gestión de normativas.')
seleccion_usuario()

