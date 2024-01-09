from karel.stanfordkarel import *

"""
Ficheiro: 3_KarelDaVoltasAoQuarteirao.py
------------------------------
Quando acabar de escrever este ficheiro, a 3_KarelDaVoltasAoQuarteirao
vai ser capaz de dar quatro voltas ao quarteirão, tal
como descrito no enunciado do problema.
"""

def main():
    move()
    while left_is_blocked():
            move_four()
            turn_left()
            move_five()
            turn_left()
            move_four()
            move()
            turn_left()
            move_five()
            turn_left()
            break

    """
    In this main function, I moved Karel forward once to have the blockage on
    the left side. Then, I defined a while condition that specified that as long
    as the left side is blocked, Karel should follow the commands, stopping the
    while loop with the break statement after one iteration.
    """

## Function using a for loop to make Karel move forward 4 times
def move_four():
    for _ in range(4):
        move()

## Function using a for loop to make Karel move forward 5 times
def move_five():
    for _ in range(5):
        move()

# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()