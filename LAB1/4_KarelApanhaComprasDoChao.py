from karel.stanfordkarel import *

"""
Ficheiro: 4_KarelApanhaComprasDoChao.py
------------------------------
Quando acabar de escrever este ficheiro, a KarelApanhaComprasDoChao
deverá ser capaz de apanhar as compras, como descrito no enunciado
do problema.
"""


def main():
    turn_left()
    left_twice()
    pick_beeper()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    move()
    turn_right()
    move()
    pick_beeper()
    move()
    pick_beeper()
    turn_left()
    left_twice()
    move()
    left_twice()
    move_twice()

    """
    Visando reduzir o número de comandos, bem como otimizar as funções
    adjacentes à função main, defini a função left_twice para combinar um 
    giro à esquerda ou à direita com um movimento duplo.
    
    A exemplo das demais funções, utilizei um laço de repetição(for) para
    reduzir o número de comandos nas funções adjacentes à main.
    """

def left_twice():
    turn_left()
    move_twice()


def move_twice():
    for i in range(2):
        move()


def turn_right():
    for i in range(3):
        turn_left()

# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
