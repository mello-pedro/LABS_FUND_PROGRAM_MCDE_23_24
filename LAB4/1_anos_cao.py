"""
File: 1_anos_cao.py
----------------------
This program continuously takes an input representing a human age and calculates
the equivalent age in dog years, assuming that 1 human year is equivalent to 7 dog years.
If the input is positive, it calculates and prints the dog years equivalent. If the input is negative,
it informs that the number is invalid and prompts for another input. If the input is 0, it terminates the program.
"""

anos_cao_por_ano_humano = 7

def main():
    while True:
        user_age = int(input("digite uma idade humana e diremos o quanto equivale em anos de um cão: "))
        idade_cao = user_age * anos_cao_por_ano_humano
        if user_age > 0:
            print(f"A idade inserida equivale a {idade_cao} anos de vida de um cão")
        elif user_age < 0:
            print("Número inválido. Tente novamente")
        elif user_age == 0:
            break


# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
