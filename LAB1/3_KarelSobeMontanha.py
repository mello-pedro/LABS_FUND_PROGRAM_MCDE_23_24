from karel.stanfordkarel import *

"""
Ficheiro: 3_KarelSobeMontanha.py
------------------------------
Quando acabar de escrever este ficheiro, a KarelSobeMontanha
deverá ser capaz de escalar a montanha, colocar a bandeira,
e descer pelo lado oposto, como descrito no enunciado do 
problema.
"""


def main():
    move()
    left_twice()
    turn_right()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
    move()
    turn_right()
    move()
    turn_left()
    move()
    right_twice()
    turn_left()

    """
    Visando reduzir o número de comandos, bem como otimizar as funções
    adjacentes à função main, defini as funções left_twice e right_twice
    para combinar um giro à esquerda ou à direita com um movimento duplo.
    
    A exemplo das demais funções, utilizei um laço de repetição(for) para
    reduzir o número de comandos nas funções adjacentes à main.
    """

def left_twice():
    turn_left()
    move_twice()

def right_twice():
    for i in range(3):
        turn_left()
    for i in range(2):
        move()


def move_twice():
    for i in range(2):
        move()


def turn_right():
    for i in range(3):
        turn_left()


# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
