from karel.stanfordkarel import *

"""
Ficheiro: 5_KarelEntraNaDivisao.py
------------------------------
Quando acabar de escrever este ficheiro, a 5_KarelEntraNaDivisao
vai ser capaz de entrar na divisão, tal
como descrito no enunciado do problema. Tente obter uma solução
genérica, que funcione em mundos diferentes.
"""


def main():
    move()
    if left_is_blocked():
        move_five()
        turn_left()
        move_tree()
        turn_left()
        move()

    """
    In this main function, I moved Karel forward once to have the blockage on
    the left side. Then, I defined an If statement that specified that as long
    as the left side is blocked, Karel should follow the commands untill the end.
    """

## Function using a for loop to make Karel move forward 5 times
def move_five():
    for _ in range(5):
        move()

## Function using a for loop to make Karel move forward 3 times
def move_tree():
    for _ in range(3):
        move()

# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
