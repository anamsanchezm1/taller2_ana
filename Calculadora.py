def suma(a, b):
    return a + b

def resta(a, b):
    if a < b:
        raise ValueError("El minuendo debe ser mayor o igual al sustraendo")
    else:   
        return a - b

def multiplicacion(a, b):
    return a * b

def calculadora():
    print("=== Calculadora ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Salir")
    
    while True:
        opcion = input("\nElige una opción (1/2/3): ")

        if opcion == "4":
            print("¡Hasta luego!")
            break
        elif opcion == "1":
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
            resultado = suma(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif opcion == "2":
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
            resultado = resta(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif opcion == "3":
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
            resultado = multiplicacion(num1, num2)
            print(f"Resultado: {num1} * {num2} = {resultado}")
        else:
            print("Opción no válida")

if __name__ == "__main__":
    calculadora()