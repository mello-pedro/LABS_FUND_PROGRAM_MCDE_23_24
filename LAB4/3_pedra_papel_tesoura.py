"""
File: 3_pedra_papel_tesoura.py
----------------------
This program allows a user to play a rock-paper-scissors game against the computer for 5 rounds.
It records the number of rounds won by both the user and the computer and determines the overall winner
based on these results.
"""
import random

pedra = 1
papel = 2
tesoura = 3

def main():
    humano_ganhou = 0
    pc_ganhou = 0
    for _ in range(5):
        num_human = int(input("Digite 1 para pedra, 2 para papel e 3 para tesoura: "))
        num_pc = random.randint(1, 3)
        if num_human == 1 and num_pc == 3:
            humano_ganhou+=1
            print("Você venceu a rodada!")
        elif num_human == 1 and num_pc == 2:
            pc_ganhou+=1
            print("Você perdeu a rodada!")
        elif num_human == 2 and num_pc == 1:
            pc_ganhou+=1
            print("Você perdeu a rodada!")
        elif num_human == 2 and num_pc == 3:
            humano_ganhou+=1
            print("Você venceu a rodada!")
        elif num_human == 3 and num_pc == 1:
            pc_ganhou+=1
            print("Você perdeu a rodada!")
        elif num_human == 3 and num_pc == 2:
            humano_ganhou+=1
            print("Você venceu a rodada!")
        else:
            print("Empate!")
            pass
    if humano_ganhou > pc_ganhou:
        print(f"você venceu {humano_ganhou} rodadas e é o grande vencedor!")
    elif pc_ganhou > humano_ganhou:
        print(f"você perdeu! o Computador ganhou {pc_ganhou} rodadas e é o grande vencedor!")
    else:
        print("empate!")


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
