"""
File: 2_preco_com_iva.py
----------------------
This program calculates the price of a product plus taxes (Portuguese IVA);
The user has to input the price of the product and the iva percentage.
I've used the time library to give an organic aspect/feeling to the user
"""
import time

def main():
    print("Bem-vindo à calculadora de Preços + IVA!")
    time.sleep(2)
    preco_base = float(input("Qual é o preço do produto? "))
    iva = float(input("Qual é o percentual do iva? "))
    iva = iva/100
    preco_final = (preco_base * iva) + preco_base
    return print (f'O preço final, após a adição do IVA é de {preco_final} Euros')


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
