"""
Programa: Calculadora de Áreas de Figuras Geométricas
Descripción: Este programa permite calcular el área de un triángulo, un rectángulo o un círculo,
utilizando entrada del usuario. Implementa distintos tipos de datos (int, float, str, bool),
siguiendo las convenciones de estilo en Python.
Autor: [Tu Nombre]
Fecha: [Fecha de hoy]
"""

import math

def calcular_area_triangulo(base: float, altura: float) -> float:
    """Calcula el área de un triángulo."""
    return (base * altura) / 2

def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo."""
    return base * altura

def calcular_area_circulo(radio: float) -> float:
    """Calcula el área de un círculo."""
    return math.pi * radio ** 2

def mostrar_menu():
    print("Seleccione la figura para calcular el área:")
    print("1. Triángulo")
    print("2. Rectángulo")
    print("3. Círculo")

def main():
    mostrar_menu()
    opcion: str = input("Ingrese el número de la opción deseada (1/2/3): ")

    if opcion == "1":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area:.2f}")
    elif opcion == "2":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area:.2f}")
    elif opcion == "3":
        radio = float(input("Ingrese el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area:.2f}")
    else:
        print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
