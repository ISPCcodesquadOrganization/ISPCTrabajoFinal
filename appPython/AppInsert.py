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
