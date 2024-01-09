from karel.stanfordkarel import *

"""
Ficheiro: 2_KarelReparaEstrada.py
------------------------------
Quando acabar de escrever este ficheiro, a 2_KarelReparaEstrada
vai ser capaz de reparar todos os buracos de uma estrada, tal
como descrito no enunciado do problema. 
"""


def main():
    for _ in range(5):
        move()
        descer_obstaculo()
        put_beeper()
        subir_obstaculo()
        move()

    """
    Knowing that there are 5 holes, and having decomposed the problem into a
    smaller solution in the previous exercise (KarelReparaBuracoMelhor), I used
    a for loop to repeat the code 5 times to repair all the holes.
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
