#conexion a la base de datos

#cmd.execute("Select * from leyes")


#funcion de menu principal
import mysql.connector

db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="sistema_leyes"
        )
class Leyes:

    def __init__(self, numero_registro=None,numero_normativa=None,fecha=None,descripcion=None,Normativas_idNormativa=None,categoria_idcategoria=None,jurisdiccion_idjurisdiccion=None):
        self.numero_registro = numero_registro
        self.numero_normativa = numero_normativa
        self.fecha = fecha
        self.descripcion = descripcion
        self.normativa_id = Normativas_idNormativa
        self.categoria_id = categoria_idcategoria
        self.jurisdiccion_id = jurisdiccion_idjurisdiccion

    @staticmethod
    def mostrar_registros():
        # Conexión a la base de datos


        # Obtener cursor
        cursor = db.cursor()

        # Ejecutar consulta SQL
        cursor.execute("SELECT * FROM normativas")

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
        #db.close()

        #conexion a la base de datos

#agregar registro a la base de datos

def agregarRegistro():

    cursor = db.cursor()
    
    #Ingreso de datos para nuevo registro

    numero_normativa = input('Ingrese el numero correspondiente a la normativa que desea cargar: ')
    fecha = input('Ingrese la fecha de creacion de la normativa (el formato debe ser AÑO-MES-DÍA): ')
    descripcion = input('Ingrese una descripcion de la normativa (hasta mil caracteres): ')
    idNormativa = input('Ingrese el ID correspondiente al tipo de normativa (101 - Ley, 102 - Resolución, 103 - Decreto): ')
    idCategoria = input('Ingrese el ID de la categoria (201 - Laboral, 202 - Penal, 203 - Civil, 204 - Comercial, 205 - Derecho Informático): ')
    idJurisdiccion = input('Ingrese el ID de la Jurisdicción (301 - Nacional, 302 - Provincial, 303 - Municipal): ')


    sentencia = "INSERT INTO normativas (numero_normativa, fecha, descripcion, Normativas_idNormativa, categorias_idcategoria, jurisdiccion_idjurisdiccion) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(numero_normativa, fecha, descripcion, idNormativa, idCategoria, idJurisdiccion)
    cursor.execute(sentencia)
    db.commit()


#eliminar registros de la base de batos
# sentencia = "DELETE FROM normativas WHERE numero_normativa = ('{}')".format(registroEliminar)
    # cursor.execute(sentencia)
    # db.commit()

def eliminarRegistro():

    cursor=db.cursor()
    #respUser = input()
    registroEliminar = input('Ingrese el numero de ley que desea eliminar: ')
    #lista de numeros normativas
    cursor.execute("SELECT numero_normativa FROM normativas")
    lista_normativas_numeros=cursor.fetchall()
    #verificamos si la respuesta del usuario se encuentra en la base de datos
    if (int(registroEliminar),) in lista_normativas_numeros:
        respuesta = input("¿Esta seguro que desea borrar la normativa N°" + registroEliminar + " (Si/No).\n")

        if respuesta.lower() == "no":
                print("Eliminación cancelada.")
        else:
                cursor.execute("SELECT numero_registro FROM normativas WHERE numero_normativa = "+registroEliminar)
                variable=cursor.fetchone()
                print("Eliminando...")
                cursor.execute("DELETE FROM normativas_has_palabra_clave WHERE normativas_numero_registro = "+str(variable[0]))
                cursor.execute("DELETE FROM normativas WHERE numero_normativa =" + registroEliminar)
                print("Se eliminó con exito.")
    else:
     print("Error no se encuentra la normativa...")
        
    db.commit()      




def editarRegistro():
    cursor = db.cursor()

    #Ingreso de registro a editar
    numero_registro = input('Ingrese el numero de registro desea cambiar: ')
    nueva_normativa = input('Ingrese el nuevo numero de normativa: ')
    nueva_fecha = input('Ingrese la fecha de creacion de la normativa (el formato debe ser AÑO-MES-DÍA): ')
    descripcion = input('Ingrese una descripcion de la normativa (hasta mil caracteres): ')
    idNormativa = input('Ingrese el ID correspondiente al tipo de normativa (101 - Ley, 102 - Resolución, 103 - Decreto): ')
    idCategoria = input('Ingrese el ID de la categoria (201 - Laboral, 202 - Penal, 203 - Civil, 204 - Comercial, 205 - Derecho Informático): ')
    idJurisdiccion = input('Ingrese el ID de la Jurisdicción (301 - Nacional, 302 - Provincial, 303 - Municipal): ')
    
    sentencia = """UPDATE normativas SET numero_normativa = '{}', fecha = '{}', descripcion = '{}',
        Normativas_idNormativa = '{}', categorias_idcategoria = '{}',
        jurisdiccion_idjurisdiccion = '{}' WHERE numero_registro = '{}'""".format(nueva_normativa, nueva_fecha, descripcion, idNormativa, idCategoria, idJurisdiccion, numero_registro)
    cursor.execute(sentencia)
    db.commit()

#Buscar un registro de la base de datos

def buscarRegistro():
    cursor = db.cursor()

    #Usuario ingresa palabra clave o numero de ley

    ingresoUsuario = input('Ingrese como desea buscar 1 - Numero de ley o  2 - Palabra clave: ')

    if ingresoUsuario == '1':
        numeroLey = input('Ingrese el numero de ley: ')
        sentencia = "SELECT * FROM normativas WHERE numero_normativa = '{}'".format(numeroLey)
    elif ingresoUsuario == '2':
        palabraClave = input('Ingrese palabra clave: ')
        sentenciaAuxiliar = "SELECT idPalabra_clave FROM palabra_clave WHERE Palabra = '{}'".format(palabraClave)

        cursor.execute(sentenciaAuxiliar)
        temporal = cursor.fetchone()

        sentenciaAuxiliar2 = "SELECT normativas_numero_registro FROM normativas_has_palabra_clave WHERE palabra_clave_idPalabra_clave = '{}'".format(temporal[0])

        cursor.execute(sentenciaAuxiliar2)
        temporal2 = cursor.fetchone()

        sentencia = "SELECT * FROM normativas WHERE numero_registro = '{}'".format(temporal2[0])
    else:
        print('Ingrese una opcion valida')
        return buscarRegistro()



    
    cursor.execute(sentencia)
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



'''import mysql.connector as mysql

conexion = mysql.connect(
    host = 'localhost',
    port = 3306,
    db = 'sistema_leyes',
    user = 'root',
    password = '1234')

cmd = conexion.cursor()

#cmd.execute("Select * from leyes")
'''

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
        leyes = Leyes(numero_registro=None,numero_normativa=None,fecha=None,descripcion=None,Normativas_idNormativa=None,categoria_idcategoria=None,jurisdiccion_idjurisdiccion=None)
        leyes.mostrar_registros(),
        print('Se muestran todas las leyes'),
         
        print('------------------------'),
        return seleccion_usuario()
    elif eleccion_usuario == '2':
        #Se inicia funcion de buscador
        buscarRegistro()
        print('Se da la opcion de escribir al usuario')
        print('------------------------')
        return seleccion_usuario()
    elif eleccion_usuario == '3':
        #Se dan al usuario los pasos para cargar un nuevo registro
        agregarRegistro()
        print('Se ha agregado un registro de forma exitosa')
        print('------------------------')
        return seleccion_usuario()
    elif eleccion_usuario == '4':
        #Se da la opcion al usuario de seleccionar que registro quiere modificar
        editarRegistro()
        print('Se ha modificado un registro')
        print('------------------------')
        return seleccion_usuario()
    elif eleccion_usuario == '5':
        #Se pregunta al usuario que registro quiere eliminar
        eliminarRegistro()
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

