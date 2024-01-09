from karel.stanfordkarel import *

"""
Ficheiro: 1_KarelApanhaBeeper.py
------------------------------
Neste momento, o ficheiro KarelApanhaBeeper não faz nada.
O seu trabalho nesta tarefa é adicionar o código necessário
para instruir a Karel para se dirigir até ao beeper e apanhá-lo.
"""

def main():
    turn_left()
    move()
    turn_left()
    move_twice()
    turn_left()
    move()
    pick_beeper()

def move_twice():
    for i in range(2):
        move()

    """
    Para executar esta tarefa, mais simples do que as demais (a exemplo da número 6), 
    apliquei apenas a função move_twice baseada em um laço de repetição(for) para 
    otimizar o algoritmo.
    
    """
# Não necessita de editar código para além deste ponto

if __name__ == "__main__":
    run_karel_program()
