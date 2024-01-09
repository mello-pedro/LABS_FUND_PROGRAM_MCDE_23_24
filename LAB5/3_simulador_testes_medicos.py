"""
File: 3_simulador_testes_medicos.py
----------------------
The program uses a simulation to test a population for an infection.
- User inputs: population size, test accuracy, and infection rate.
- Simulates tests for each person, tracking true positives, false positives, true negatives, and false negatives.
- Prints the results and the percentage of true positives among all identified positives.
"""
import random

def simulate_tests(num_people, test_acc, infect_rate):
    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0
    for n in range(num_people):
        sick_true = random.random() < infect_rate
        test_true = random.random() < test_acc
        if sick_true == True and test_true == True:
            true_positive +=1
        elif sick_true == False and test_true == True:
            false_positive +=1
        elif sick_true == False and test_true == False:
            true_negative +=1
        else:
            false_negative +=1
        positive_percent = true_positive / (true_positive + false_positive) * 100

    print(f"O número de Verdadeiros Positivos foi {true_positive}")
    print(f"O número de Falsos Positivos foi {false_positive}")
    print(f"O número de Verdadeiros Negativos foi {true_negative}")
    print(f"O número de Falsos Negativos foi {false_negative}")
    print(f"O percentual de Verdadeiros Positivos dentre o total de testes \n identificados como positivos foi de{positive_percent}% !")


def main():
    num_people = int(input("Insira o tamanho da população a ser simulada: "))
    test_acc = float(input("Insira o percentual de acurácia do teste (entre 0 e 1): "))
    infect_rate = float(input("Insira o percentual da população infectado (entre 0 e 1): "))
    simulate_tests(num_people, test_acc, infect_rate)


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
