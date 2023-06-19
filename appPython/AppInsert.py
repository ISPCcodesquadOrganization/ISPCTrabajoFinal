import sqlite3

def agregar_ley():
    # Establecer conexión con la base de datos
    conexion = sqlite3.connect('')
    cursor = conexion.cursor()
    
    # Obtener los detalles de la nueva ley desde el usuario
    nombre = input("Ingrese el nombre de la ley: ")
    descripcion = input("Ingrese la descripción de la ley: ")
    
    # Ejecutar la sentencia INSERT para agregar la nueva ley
    sentencia = "INSERT INTO nombre_de_tabla (nombre, descripcion) VALUES (?, ?)"
    valores = (nombre, descripcion)
    cursor.execute(sentencia, valores)
    
    # Confirmar y cerrar la conexión
    conexion.commit()
    conexion.close()
    
    print("La ley se ha agregado correctamente.")

# Ejemplo de uso
agregar_ley()
