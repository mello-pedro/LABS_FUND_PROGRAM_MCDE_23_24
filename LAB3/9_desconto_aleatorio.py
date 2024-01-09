"""
File: 9_desconto_aleatorio.py
----------------------
This program calculates a random discount, between a certain range given by the user
using python's random library;
I've used also the time library to give an organic aspect/feeling to the user
"""
import random
import time

## The discount function is an auxiliary function that uses given arguments from user
# as a range to trigger the random.uniform object in main function.
def discount(disc_min, disc_max):
    return random.uniform(disc_min, disc_max)

def main():
    print("Hoje é seu dia de sorte! \n ",
          "Insira um valor mínimo e um valor máximo entre 0 e 100 e calcularemos um desconto aleatório para conceder-lhe em nosso site!")
    disc_min = int(input("Insira aqui o valor mínimo: "))
    disc_max = int(input("Agora insira o máximo: "))
    print("Aguarde. Estamos a sortear o vosso desconto...")
    time.sleep(2)
    result = int(discount(disc_min, disc_max))
    print(f"O seu desconto será de {result}%! Aproveite!!")



# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
