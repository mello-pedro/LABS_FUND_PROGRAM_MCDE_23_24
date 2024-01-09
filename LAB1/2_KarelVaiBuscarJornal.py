from karel.stanfordkarel import *

"""
Ficheiro: 2_KarelVaiBuscarJornal.py
------------------------------
Quando acabar de escrever este ficheiro, a KarelVaiBuscarJornal
deverá ser capaz de ir buscar o jornal e voltar à cama. No 
final, a Karel termina na posição inicial (mesma esquina, mesma
direção) com o jornal.
"""


def main():
    left_twice()
    left_twice()
    left_twice()
    turn_left()
    move()
    pick_beeper()
    turn_left()
    move()
    turn_left()
    move()
    turn_right()
    move()
    right_twice()
    right_twice()
    turn_left()
    """
    Visando reduzir o número de comandos, bem como otimizar as funções
    adjacentes à função main, defini as funções left_twice e right_twice
    para combinar um giro à esquerda ou à direita com um movimento duplo.
    
    A exemplo das demais funções, utilizei um laço de repetição(for) para
    reduzir o número de comandos nas funções adjacentes à main.
    """
def move_twice():
    for i in range(2):
        move()

def turn_right():
    for i in range(3):
        turn_left()

def left_twice():
    turn_left()
    move_twice()

def right_twice():
    for i in range(3):
        turn_left()
    for i in range(2):
        move()

# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
