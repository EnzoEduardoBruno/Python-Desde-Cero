from practica import *

puntaje = 0
total = 10

print("\n🧪 Corrigiendo ejercicios...\n")


def corregir(numero, funcion, esperado):
    global puntaje

    try:
        resultado = funcion()

        if resultado == esperado:
            print(f"✅ Ejercicio {numero} correcto")
            puntaje += 1
        else:
            print(f"❌ Ejercicio {numero} incorrecto")
            print(f"   Esperado: {esperado}")
            print(f"   Recibido: {resultado}")

    except Exception as error:
        print(f"❌ Error en ejercicio {numero}")
        print(f"   Detalle: {error}")


corregir(1, ejercicio_1, "Hola mundo")
corregir(2, ejercicio_2, "Estoy aprendiendo a programar")
corregir(3, ejercicio_3, "Python es divertido")
corregir(4, ejercicio_4, "Programar es dar instrucciones")
corregir(5, ejercicio_5, "Un algoritmo es una serie de pasos")
corregir(6, ejercicio_6, "La programación secuencial ejecuta instrucciones en orden")
corregir(7, ejercicio_7, "Entrada")
corregir(8, ejercicio_8, "Proceso")
corregir(9, ejercicio_9, "Salida")
corregir(10, ejercicio_10, "Entrada Proceso Salida")

print("\n---------------------------")
print(f"🎯 Resultado final: {puntaje}/{total}")

if puntaje == total:
    print("🏆 ¡Excelente trabajo!")
elif puntaje >= 7:
    print("👍 ¡Muy bien!")
elif puntaje >= 4:
    print("🙂 Vas bien, seguí practicando.")
else:
    print("📚 Seguí practicando, es parte del proceso.")