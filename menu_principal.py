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

        print('Se muestran todas las leyes')
        print('------------------------')
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

