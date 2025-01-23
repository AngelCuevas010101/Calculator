# Calculadora Básica

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División entre cero"

def calculadora():
    print("Bienvenido a la calculadora básica")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    try:
        opcion = int(input("Selecciona una operación (1-4): "))
        if opcion not in [1, 2, 3, 4]:
            print("Opción inválida. Por favor, elige entre 1 y 4.")
            return

        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == 1:
            resultado = sumar(num1, num2)
            print(f"El resultado de sumar {num1} y {num2} es: {resultado}")
        elif opcion == 2:
            resultado = restar(num1, num2)
            print(f"El resultado de restar {num1} y {num2} es: {resultado}")
        elif opcion == 3:
            resultado = multiplicar(num1, num2)
            print(f"El resultado de multiplicar {num1} y {num2} es: {resultado}")
        elif opcion == 4:
            resultado = dividir(num1, num2)
            print(f"El resultado de dividir {num1} entre {num2} es: {resultado}")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()
