"""
File: 4_area_circulo.py
----------------------
This program calculates the area of a circle using python's math library;
"""
import math

def main():
    raio = float(input("qual é o raio da circunferência? "))
    PI = math.pi
    area = (raio**2) * PI
    return print(f"A área do círculo é de {area}")


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
