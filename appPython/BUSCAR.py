import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123459",
    database="sistema_leyes"
)

class Leyes:
    def __init__(self, numero_registro=None, numero_normativa=None, fecha=None, descripcion=None,
                 Normativas_idNormativa=None, categoria_idcategoria=None, jurisdiccion_idjurisdiccion=None):
        self.numero_registro = numero_registro
        self.numero_normativa = numero_normativa
        self.fecha = fecha
        self.descripcion = descripcion
        self.normativa_id = Normativas_idNormativa
        self.categoria_id = categoria_idcategoria
        self.jurisdiccion_id = jurisdiccion_idjurisdiccion

    @staticmethod
    def buscarRegistro():
        cursor = db.cursor()

        # Usuario ingresa palabra clave o numero de ley
        ingresoUsuario = input('Ingrese cómo desea buscar 1 - Numero de ley o 2 - Palabra clave: ')

        if ingresoUsuario == '1':
            numeroLey = input('Ingrese el número de ley: ')
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
            print('Ingrese una opción válida')

        cursor.execute(sentencia)
        # Obtener todos los registros
        registros = cursor.fetchall()

        # Cerrar la conexión a la base de datos
        db.close()

        return registros

