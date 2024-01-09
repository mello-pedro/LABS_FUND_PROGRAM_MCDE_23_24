from karel.stanfordkarel import *

"""
Ficheiro: 8_KarelDaVoltasAoQuarteiraoMelhor.py
------------------------------
Quando acabar de escrever este ficheiro, a 8_KarelDaVoltasAoQuarteiraoMelhor
irá continuar a conseguir dar as voltas ao quarteirão, como descrito
no enunciado do problema, mas a solução será suficientemente genérica 
para funcionar bem com qualquer dos três mundos fornecidos.
"""

def main():
    move()
    while True:
        if left_is_blocked():
            move()
        elif left_is_clear():
            turn_left()
            move()

    """
    In this main function, I moved Karel forward once to have the blockage on
    the left side. Then, I defined a while condition that specified that as long
    as the left side is blocked, Karel should move forward. When the first If statment
    becomes false, Karel should follow the Elif condition.
    """

# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
