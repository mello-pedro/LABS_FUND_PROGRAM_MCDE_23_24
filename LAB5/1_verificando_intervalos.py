"""
File: 1_verificando_intervalos.py
----------------------
The `in_range` function takes three parameters: `low`, `n`, and `high`. It checks if the value of `n` is within
the range specified by `low` (inclusive) and `high` (exclusive). If `n` is in the specified range, it prints
a message indicating that the number is between the given range. Otherwise, it prints a message indicating that
the number is not in the specified range.

The `main` function is then defined, which takes user input for three values: `low`, `n`, and `high`.
These values are obtained using the `input` function after converting them to integers. The `in_range` function
is then called with these user-input values.
"""

def in_range(low, n, high):
    if n in range(low, high):
        print(f'O número {n} está entre {low} e {high}!')
    else:
        print(f'O número {n} NÃO está entre {low} e {high}!')


def main():
    low = int(input("Escreva umm número para marcar o início do intervalo: "))
    n = int(input("escreva um número para saber se está compreendido no intervalo: "))
    high = int(input("Escreva um número para demarcar o fim do intervalo: "))
    in_range(low, n, high)


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
