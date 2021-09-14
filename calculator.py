def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def menu():
    opcion = 0
    while opcion < 1 or opcion > 6:
        print("Que operacion quiere hacer?")
        print("\t1 - Sumar")
        print("\t2 - Restar")
        print("\t3 - Dividir")
        print("\t4 - Multiplicar")
        print("\t5 - Limpiar")
        print("\t6 - Ya termine, salir")
        opcion = int(input("Operacion: "))

    return opcion


def main():
    resultado = 0.0
    opcion = menu()
    while opcion != 6:
        print("Resultado: ", resultado)
        res = 0.0

        if resultado == 0:
            resultado = float(input("Primer valor: "))

        if opcion == 1:
            res = add(resultado, float(input("Valor a sumar: ")))

        elif opcion == 2:
            res = subtract(resultado, float(input("Valor a restar: ")))

        elif opcion == 3:
            res = divide(resultado, float(input("Valor a dividir: ")))

        elif opcion == 4:
            res = multiply(resultado, float(input("Valor a multiplicar: ")))

        elif opcion == 5:
            res = 0.0

        resultado = res
        print("Resultado: ", resultado)
        opcion = menu()


main()