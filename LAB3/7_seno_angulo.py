"""
File: 7_seno_angulo.py
----------------------
This program calculates the sin of an angle inputed by user in radians;
"""
import math

## The seno function is an auxiliary function that uses given arguments from user
# to calculate the sin in main function.
def seno(value):
    return math.sin(value)

def main():
    angulo = float(input("Insira o valor do ângulo em Radianos: "))
    result = seno(angulo)
    print("O Seno do ângulo dado é: ", result)



# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
