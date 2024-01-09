"""
File: 4_first_letter_index.py
----------------------
The program defines a function named first_list that takes a list of words (lista) as input.
It creates a dictionary (dicio) where keys are unique initial letters of the words, and values are
lists of words that start with the corresponding letter. By executing it, the main function calls
first_list with a predefined list of words and prints the resulting dictionary.
"""

def first_list(lista):
    unique_letters = []
    dicio = {}
    dicio_values = []
    for element in lista:
        if element[0] not in unique_letters:
            unique_letters.append(element[0])
    for element in lista:
        if element not in dicio_values:
            dicio_values.append(element)
    for i in unique_letters:
        dicio[i] = [word for word in dicio_values if word.startswith(i)]

    return dicio


def main():
    entrada = first_list(['banter', 'brahm', 'aardvark', 'python', 'antiquated'])
    print(entrada)


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
