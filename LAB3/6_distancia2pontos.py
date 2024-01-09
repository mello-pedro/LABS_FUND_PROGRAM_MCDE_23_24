"""
File: 6_distancia2pontos.py
----------------------
This program calculates the euclidean distance between two points using python's math library;
The user has to input two pairs of numbers.
"""
import math

## The euclid_dist function is an auxiliary function that uses given arguments from user
# to calculate the euclidean distance in main function.

def euclid_dist(x_1, y_1, x_2, y_2):
    return math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

def main():
    x_1 = int(input("insira um valor para o ponto X1: "))
    y_1 = int(input("insira um valor para o ponto Y1: "))
    x_2 = int(input("insira um valor para o ponto X2: "))
    y_2 = int(input("insira um valor para o ponto Y2: "))
    result = euclid_dist(x_1, y_1, x_2, y_2)
    print("O valor da distância euclideana para os pontos dados é: ", result)




# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
