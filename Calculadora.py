def suma(a, b):
    return a + b

def resta(a, b):
    if a < b:
        raise ValueError("El minuendo debe ser mayor o igual al sustraendo")
    else:   
        return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    else:
        return a / b
    
def potencia(a, b):
    return a ** b

def calculadora():
    print("=== Calculadora ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Salir")

    while True:
        opcion = input("\nElige una opción (1/2/3/4/5): ")
        
        if opcion == "6":
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
        elif opcion == "4":
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
            resultado = division(num1, num2)
            print(f"Resultado: {num1} / {num2} = {resultado}")
        elif opcion == "5":
            num1 = float(input("Base: "))
            num2 = float(input("Exponente: "))
            resultado = potencia(num1, num2)
            print(f"Resultado: {num1} ^ {num2} = {resultado}")
        else:
            print("Opción no válida")

if __name__ == "__main__":
    calculadora()