# M25 - Métodos estáticos y de clase
# Soluciones


def ejercicio_1():

    class Calculadora:

        @staticmethod
        def sumar(a, b):
            return a + b

    return Calculadora.sumar(10, 5)


def ejercicio_2():

    class Calculadora:

        @staticmethod
        def restar(a, b):
            return a - b

    return Calculadora.restar(10, 5)


def ejercicio_3():

    class Conversor:

        @staticmethod
        def metros_a_centimetros(metros):
            return metros * 100

    return Conversor.metros_a_centimetros(2)


def ejercicio_4():

    class Validador:

        @staticmethod
        def es_mayor_de_edad(edad):
            return edad >= 18

    return Validador.es_mayor_de_edad(20)


def ejercicio_5():

    class Usuario:

        cantidad = 5

        @classmethod
        def mostrar_cantidad(cls):
            return cls.cantidad

    return Usuario.mostrar_cantidad()


def ejercicio_6():

    class Producto:

        iva = 21

        @classmethod
        def mostrar_iva(cls):
            return cls.iva

    return Producto.mostrar_iva()


def ejercicio_7():

    class Configuracion:

        modo = "Producción"

        @classmethod
        def mostrar_modo(cls):
            return cls.modo

    return Configuracion.mostrar_modo()


def ejercicio_8():

    class Texto:

        @staticmethod
        def convertir_mayusculas(texto):
            return texto.upper()

    return Texto.convertir_mayusculas("python")


def ejercicio_9():

    class Sistema:

        nombre = "Python Desde Cero"

        @classmethod
        def mostrar_nombre(cls):
            return cls.nombre

    return Sistema.mostrar_nombre()


def ejercicio_10():

    class Herramienta:

        version = "1.0"

        @staticmethod
        def saludar():
            return "Hola"

        @classmethod
        def mostrar_version(cls):
            return cls.version

    return Herramienta.saludar() + " " + Herramienta.mostrar_version()