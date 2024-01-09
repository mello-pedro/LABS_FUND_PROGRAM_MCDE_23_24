"""
File: 10_data_aleatoria.py
----------------------
The main function of this program gives as output a random date between 2024 and 2500.
"""
import numpy as np
import random

## First of all, I've developed a function to generate the day using random.randint. I tried to consider leap years
# to avoid mistakes on february, and tried to consider also the months with 30/31 days;

def generate_day(mes, ano):
    if mes == 2 and (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return random.randint(1, 29)
    elif mes == 2:
        return random.randint(1,28)
    elif mes in (1, 3, 5, 7, 8, 10, 12):
        return random.randint(1, 31)
    else:
        return random.randint(1,30)

## Next, I've developed the core function that generates the random dates between an defined start/end range.
# the variable day uses the auxiliary function generate_day with year and month defined previously as argument.

def generate_date():
    ano = random.randint(2024, 2500)
    mes = random.randint(1, 12)
    dia = generate_day(mes, ano)
    print("A data do seu evento futuro é: ", ano, "/", mes, "/", dia)

## I have tested three times, and the code give me 3 different dates (YYYY/MM/DD) as: 2154/2/1, 2301/12/29, 2219/2/9.

def main():
    generate_date()



# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
