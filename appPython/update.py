import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1205",
    database="sistema_leyes"
)

class Leyes:
    def __init__(self, numero_registro=None, numero_normativa=None, fecha=None, descripcion=None, Normativas_idNormativa=None, categoria_idcategoria=None, jurisdiccion_idjurisdiccion=None):
        self.numero_registro = numero_registro
        self.numero_normativa = numero_normativa
        self.fecha = fecha
        self.descripcion = descripcion
        self.normativa_id = Normativas_idNormativa
        self.categoria_id = categoria_idcategoria
        self.jurisdiccion_id = jurisdiccion_idjurisdiccion

    @staticmethod
    def editarRegistro():
        cursor = db.cursor()

        # Ingreso de registro a actualizar
        numero_registro = input('Ingrese el número de registro que desea cambiar: ')
        nueva_normativa = input('Ingrese el nuevo número de normativa: ')
        nueva_fecha = input('Ingrese la fecha de creación de la normativa (el formato debe ser AÑO-MES-DÍA): ')
        descripcion = input('Ingrese una descripción de la normativa (hasta mil caracteres): ')
        idNormativa = input('Ingrese el ID correspondiente al tipo de normativa (101 - Ley, 102 - Resolución, 103 - Decreto): ')

        sentencia = """
            UPDATE normativas SET
            numero_normativa = %s,
            fecha = %s,
            descripcion = %s,
            Normativas_idNormativa = %s
            WHERE numero_registro = %s
        """
        valores = (nueva_normativa, nueva_fecha, descripcion, idNormativa, numero_registro)
        cursor.execute(sentencia, valores)
        db.commit()



