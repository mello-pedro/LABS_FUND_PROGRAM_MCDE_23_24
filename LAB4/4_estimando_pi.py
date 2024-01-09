"""
File: 4_estimando_pi.py
----------------------
This program calculates an approximate value of PI using the monte carlo simulation.
Note that if you increase the number of points by modifying NUM_PONTOS, the number gets closer
to the real value of PI. But attention: More points demands more processing power and time
"""
import random

NUM_PONTOS = 100000
RAIO = 1

def main():
    pontos_circulo = 0
    for _ in range (NUM_PONTOS+1):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if (x**2 + y**2 < RAIO):
            pontos_circulo+=1
    pi_estimado = 4 * (pontos_circulo/NUM_PONTOS)
    print (f"O valor estimado de PI usando {NUM_PONTOS} pontos é: ", pi_estimado)



# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
