"""
File: 1_media3notas.py
----------------------
This program calculates the mean of an student using 3 given grades;
I've used the time library to give an organic aspect/feeling to the user
"""
import time

def main():
    print("Bem-vindo à calculadora de médias!")
    time.sleep(2)
    num1 = int(input("A primeira nota foi: "))
    num2 = int(input("A segunda nota foi: "))
    num3 = int(input("A terceira nota foi: "))
    media = (num1 + num2 + num3) / 3
    return print(f'A média final foi {media} pontos!')


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
