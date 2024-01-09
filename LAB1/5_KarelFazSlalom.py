from karel.stanfordkarel import *

"""
Ficheiro: 5_KarelFazSlalom.py
------------------------------
Quando acabar de escrever este ficheiro, a KarelFazSlalom
deverá ser capaz de apanhar de fazer um oito no menor 
número possível de movimentos, como descrito no enunciado
do problema.
"""


def main():
    move()
    left_twice()
    left_twice()
    right_twice()
    right_twice()
    right_twice()
    right_twice()
    left_twice()
    turn_left()
    move()

    """"
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
