"""
File: 1_collapse.py
----------------------
This program defines a function called `collapse` that takes a list of integers as input. If the length of
the list is even, the program creates a new list (`lista_sum`) by summing consecutive pairs of elements from the
original list. If the length is odd, it does the same for all but the last element,
and appends the last element unchanged.
"""

def collapse(lista):
    if len(lista) % 2 == 0:
        lista_sum = [lista[i] + lista[i +1] for i in range (0, len(lista)-1, 2)]
        print(lista_sum)
    else:
        lista_sum = [lista[i] + lista[i + 1] for i in range(0, len(lista)-1, 2)]
        lista_sum.append(lista[-1])
        print(lista_sum)


def main():
    user_input = input('insira uma lista de inteiros separados por espaços: ')
    lista = user_input.split()
    for i in range(len(lista)):
        lista[i] = int(lista[i])

    collapse(lista)


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
