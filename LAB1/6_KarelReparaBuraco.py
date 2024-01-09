from karel.stanfordkarel import *

"""
Ficheiro: 6_KarelReparaBuraco.py
------------------------------
Quando acabar de escrever este ficheiro, a KarelReparaBuraco
deverá ser capaz de apanhar de reparar o buraco na estrada, 
como descrito no enunciado do problema.
"""


def main():
    move()
    turn_right()
    move()
    put_beeper()
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
    """
    Para executar esta tarefa, mais simples do que as demais (a exemplo da tarefa 1), 
    apliquei apenas a função turn_right baseada em um laço de repetição(for) 
    para otimizar o algoritmo.
    """

def turn_right():
    for i in range(3):
        turn_left()

# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
