from karel.stanfordkarel import *

"""
Ficheiro: 7_KarelFormigaApanhaMigalha.py
------------------------------
Quando acabar de escrever este ficheiro, a 7_KarelFormigaApanhaMigalha
vai ser capaz de apanhar a migalha, tal como descrito
no enunciado do problema. 
"""


def main():
    move_to_wall()
    subir_obstaculo_alto()
    move_to_beeper()

    """
    Running this main function, Karel will be able to perform the following moves:
    Move to an obstacle; climb it; Walk to the beeper; Pick beeper; and finally move 
    forward again untill the next wall.
    """

## Function developed by the teacher in class and that I use here to move Karel continuously until obstacles (walls)
def move_to_wall():
    while front_is_clear():
        move()

## Function to turn right using a for loop
def turn_right():
    for _ in range(3):
        turn_left()

## Function developed by the teacher in class and that I use here to make Karel descend from an obstacle
def descer_obstaculo():
    turn_right()
    move_to_wall()
    turn_left()

## An adaptation of the climb obstacle function used in previous exercises, but modified to climb taller obstacles.
def subir_obstaculo_alto():
    turn_left()
    while right_is_blocked():
        move_tree()
        turn_right()

## Function using a for loop to make Karel move forward 3 times
def move_tree():
    for _ in range(3):
        move()

## A function that uses two nested conditional structures, a while loop, and a compound If statement
# (including an Elif with a second condition) to make Karel, after climbing the obstacle, pick up any beeper in
# her path and keep moving.
def move_to_beeper():
    while True:
        if front_is_clear() and no_beepers_present():
            move()
        elif beepers_present():
            pick_beeper()
            move_to_wall()
            break


# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
