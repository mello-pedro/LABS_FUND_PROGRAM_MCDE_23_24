from karel.stanfordkarel import *

"""
Ficheiro: 9_KarelSaltaObstaculos.py
------------------------------
Quando acabar de escrever este ficheiro, a 9_KarelSaltaObstaculos
vai ser capaz de saltar os obstáculos, tal como descrito
no enunciado do problema. Tente obter uma solução genérica, 
que funcione em mundos diferentes.
"""


def main():
    for _ in range(4):
        move_to_wall()
        subir_obstaculo()
        move()
        descer_obstaculo()
    move_to_wall()

    """
    Knowing that there are 4 obstacles, I used
    a for loop to repeat the code 4 times to make Karel climbo onto 4 obstacles and keep
    moving forward.
    """

## Function to turn right using a for loop
def turn_right():
    for i in range(3):
        turn_left()

## Function developed by the teacher in class and that I use here to make Karel climb onto an obstacle
def subir_obstaculo():
    turn_left()
    while right_is_blocked():
        move()
        turn_right()

## Function developed by the teacher in class and that I use here to move Karel continuously until obstacles (walls)
def move_to_wall():
    while front_is_clear():
        move()

## Function developed by the teacher in class and that I use here to make Karel descend from an obstacle
def descer_obstaculo():
    turn_right()
    move_to_wall()
    turn_left()

# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
