# importar a classe Circle de circle.py
from circle import Circle


def main():
    # construir um círculo de raio 5
    circle = Circle(5)

    # imprimir a área do círculo
    print("A área do círculo é " + str(circle.get_area()))

    # imprimir o perímetro do círculo
    print("O perímetro do círculo é " + str(circle.get_circumference()))


if __name__ == "__main__":
    main()

