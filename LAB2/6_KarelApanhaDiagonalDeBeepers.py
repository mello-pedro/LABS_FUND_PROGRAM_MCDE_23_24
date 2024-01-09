from karel.stanfordkarel import *

"""
Ficheiro: 6_KarelApanhaDiagonalDeBeepers.py
------------------------------
Quando acabar de escrever este ficheiro, a 6_KarelApanhaDiagonalDeBeepers
vai ser capaz de apanhar todos os beepers na diagonal,
como descrito no enunciado do problema. Tente obter uma solução
genérica, que funcione em mundos diferentes.
"""


def main():
    turn_right()
    move()
    pick_beeper()
    turn_left()
    for _ in range(6):
        move()
        turn_left()
        move()
        pick_beeper()
        turn_right()
    """
    In this main function, I moved Karel first to an initial position on the left corner.
    Next, I created a for loop to make her repeat 6 times the same moves. To make this work on
    others worlds, you only have to put Karel first into the same initial position and count the 
    number of beepers to put this as an argument to the for loop above.
    """

## Function to turn right using a for loop
def turn_right():
    for i in range(3):
        turn_left()


# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
