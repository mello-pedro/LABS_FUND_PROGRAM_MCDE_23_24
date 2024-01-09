from karel.stanfordkarel import *

"""
Ficheiro: 1_KarelReparaBuracoMelhor.py
------------------------------
Quando acabar de escrever este ficheiro, a KarelReparaBuracoMelhor
vai reparar o buraco como na versão anterior, mas problema será
resolvido com decomposição, resultando num código mais legível. 
"""


def main():
    move()
    descer_obstaculo()
    put_beeper()
    subir_obstaculo()
    move()

    """
    Next, I describe the auxiliary functions for the main function that I used
    to make KarelReparaBuraco's more readable and optimized.
    """

## Function to turn right using a for loop
def turn_right():
    for i in range(3):
        turn_left()

## Function developed by the teacher in class and that I use here to move Karel continuously until obstacles (walls)
def move_to_wall():
    while front_is_clear():
        move()

## Function developed by the teacher in class and that I use here to make Karel descend from an obstacle
def descer_obstaculo():
    turn_right()
    move_to_wall()
    turn_left()

## Function developed by the teacher in class and that I use here to make Karel climb onto an obstacle
def subir_obstaculo():
    turn_left()
    while right_is_blocked():
        move()
        turn_right()

# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()