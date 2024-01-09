"""
File: 3_rotate_list_right.py
----------------------
This program defines a function called rotate_list_right that takes a list (lista) and an integer (n) as input.
It rotates the list to the right by N positions and prints the result.
"""

def rotate_list_right(lista, n):
    lista = lista[-n:] + lista[:-n]
    print(lista)


def main():
    rotate_list_right([1,3,11,14,23,67,49,13], 3)

# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
