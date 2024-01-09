"""
File: 3_imc.py
----------------------
This program calculates the IMC of a person;
The user has to input his height and weight.
I've used the time library to give an organic aspect/feeling to the user
"""
import time

def main():
    print("Bem-vindo à calculadora de IMC!")
    time.sleep(2)
    peso = float(input("Digite seu peso em KG: "))
    altura = float(input("Digite sua altura em Metros: "))
    imc = peso / (altura**2)
    print("Aguarde um momento enquanto calculo o seu IMC")
    time.sleep(2)
    print (f"O seu imc é {imc}")


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
