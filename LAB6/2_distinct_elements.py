"""
File: 2_distinct_elements.py
----------------------
This program defines a function named distinct_elements that takes a list of values as input.
It creates a new list (unique_values) containing only the distinct elements from the original list
and print the new list.
"""

def distinct_elements(lista):
    unique_values = []
    for element in lista:
        if element not in unique_values:
            unique_values.append(element)
    print(unique_values)



def main():
    user_input = input('Insira uma lista de valores separados por vírgulas e retornarei os valores únicos: ')
    lista = user_input.split(",")
    for i in lista:
        if i.isdigit():
            int(i)
        elif "." in i:
            float(i)
        else:
            i
    distinct_elements(lista)

# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
