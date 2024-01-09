"""
File: 5_salario_liquido.py
----------------------
This program calculates the net salary of an employee;
The user has to input his salary and expected deductions.
I've used the time library to give an organic aspect/feeling to the user
"""
import time

def main():
    print("Bem-vindo à calculadora Salarial!")
    time.sleep(1)
    aliment = 220
    salario = float(input("Qual é o valor do vosso salário a termos brutos? "))
    descontos = float(input("Qual o valor dos descontos que incidem sobre o vosso salário? "))
    salario_c_deducoes = (salario - descontos) + aliment
    print("Aguarde um momento enquanto calculo o vosso salário líquido")
    time.sleep(2)
    print(f'O vosso salário a termos líquidos é de {salario_c_deducoes} euros')


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
