#Modificar datos en las leyes
class Ley:
    def __init__(self, titulo, tipo):
        self.datos = {
            'titulo': titulo,
            'tipo': tipo,
            'organo_legislativo': self.obtener_organo_legislativo(tipo)
        }

    def obtener_organo_legislativo(self, tipo):
        if tipo == 'nacional':
            return 'Congreso de la Nación'
        elif tipo == 'provincial':
            return 'Legislatura de Córdoba'
        else:
            return 'Órgano legislativo no definido'

    def actualizar_datos(self):
        nuevo_titulo = input("Ingrese el nuevo título de la ley: ")
        nuevo_tipo = input("Ingrese el nuevo tipo de la ley (nacional/provincial): ")

        self.titulo = nuevo_titulo
        self.tipo = nuevo_tipo
        self.organo_legislativo = self.obtener_organo_legislativo()


"""# Ejemplo de uso
ley = Ley('Ley de Educación', 'nacional')
print(ley.datos)  # Salida: {'titulo': 'Ley de Educación', 'tipo': 'nacional', 'organo_legislativo': 'Congreso de la Nación'}

nuevos_datos = {'titulo': 'Nueva Ley de Educación', 'tipo': 'provincial'}
ley.actualizar_datos(nuevos_datos)
print(ley.datos)  # Salida: {'titulo': 'Nueva Ley de Educación', 'tipo': 'provincial', 'organo_legislativo': 'Legislatura de Córdoba'}"""
