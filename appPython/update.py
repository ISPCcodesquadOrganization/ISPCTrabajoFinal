#funcion de menu principal
import mysql.connector

db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1205",
            database="sistema_leyes"
        )

import mysql.connector as mysql

conexion = mysql.connect(
    host = 'localhost',
    port = 3306,
    db = 'sistema_leyes',
    user = 'root',
    password = '1205')

cmd = conexion.cursor()

class Leyes:
    
    def __init__(self, numero_registro=None,numero_normativa=None,fecha=None,descripcion=None,Normativas_idNormativa=None,categoria_idcategoria=None,jurisdiccion_idjurisdiccion=None):
        self.numero_registro = numero_registro
        self.numero_normativa = numero_normativa
        self.fecha = fecha
        self.descripcion = descripcion
        self.normativa_id = Normativas_idNormativa
        self.categoria_id = categoria_idcategoria
        self.jurisdiccion_id = jurisdiccion_idjurisdiccion

    def jurisdiccion_idjurisdiccion(self, tipo):
        if tipo == 'nacional':
            return 'Congreso de la Nación'
        elif tipo == 'provincial':
            return 'Legislatura de Córdoba'
        else:
            return 'Órgano legislativo no definido'

    def actualizar_datos(self):
        nuevos_datos = {}

        nueva_fecha = input("Ingrese la nueva fecha de actualización  de la ley: ")
        nuevos_datos['fecha'] = nueva_fecha

        nueva_descripcion = input("Ingrese la nueva descripción de la ley (nacional/provincial): ")
        nuevos_datos['descripcion'] = nueva_descripcion

        self.datos.update(nuevos_datos)


