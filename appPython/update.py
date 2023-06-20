#Modificar datos en las leyes
class Ley:
    def __init__(self, titulo, tipo):
        self.titulo = titulo
        self.tipo = tipo
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
        nuevos_datos = {}

        nuevo_titulo = input("Ingrese el nuevo título de la ley: ")
        nuevos_datos['titulo'] = nuevo_titulo

        nuevo_tipo = input("Ingrese el nuevo tipo de la ley (nacional/provincial): ")
        nuevos_datos['tipo'] = nuevo_tipo
        nuevos_datos['organo_legislativo'] = self.obtener_organo_legislativo(nuevo_tipo)

        self.datos.update(nuevos_datos)

