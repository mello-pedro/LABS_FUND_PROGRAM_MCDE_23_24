"""
File: 8_raiz_quadrada.py
----------------------
This program calculates the square root of a given number using python's math library;
I've used also the time library to give an organic aspect/feeling to the user
"""
import math
import time

## The square_root function is an auxiliary function that uses given arguments from user
# to calculate the square root in main function.
def square_root(value):
    return math.sqrt(value)

def main():
    print("Bem-vindo à calculadora de Raíz quadrada!")
    time.sleep(2)
    raiz = int(input("Insira um número inteiro qualquer e eu retornarei a sua raíz quadrada: "))
    result = square_root(raiz)
    print(f'A raíz quadrada de {raiz} é: {result}')


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
