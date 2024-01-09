from karel.stanfordkarel import *

"""
Ficheiro: 4_KarelAprendeMetodos.py
------------------------------
Quando acabar de escrever este ficheiro, a 4_KarelAprendeMetodos
irá aprender a executar os três métodos descritos no enunciado:
MoveMile, MoveBackward e MoveKilomile.
"""


def main():

    """
    The main function may be used to test any of those functions defined below.
    """
## Since one mile is equivalent to 8 blocks, I've developed the move_mile function based on a for loop
# that instructs Karel to move 8 times in order to travel one mile.
def move_mile():
    for _ in range(8):
        move()

## Since the move_mile function makes Karel travel one mile, I've developed
# the move_kilo_mile function that, based on a for loop, repeats the move_mile function 1,000 times,
# moving Karel through a total of 8,000 blocks.

def move_kilo_mile():
    for _ in range(1000):
        move_mile()

## Assuming Karel is facing forward, to turn her in the opposite direction, simply make her
# turn left twice. This function will be an auxiliary function for the move_backwards function.
def around():
    for _ in range(2):
        turn_left()

## Building on the around function, this function turns Karel in the opposite direction, makes
# her move once backward, and then positions her facing forward again.
def move_backwards():
    around()
    move()
    around()

# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
