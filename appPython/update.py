import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1205",
    database="sistema_leyes"
)

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
