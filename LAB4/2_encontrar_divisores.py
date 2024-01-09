"""
File: 2_encontrar_divisores.py
----------------------
This program continuously takes an input integer, and if the input is positive,
it prints all its divisors (factors), including 1 and itself. If the input is negative,
it informs that the number is invalid and prompts for another input. If the input is 0, it terminates the program.
"""

def main():
    while True:
        num = int(input("Introduza um número inteiro e retornarei todos os seus divisores: "))
        if num > 0:
            for i in range(1, (num+1)):
                if (num % i) == 0:
                    print(i)
        elif num < 0:
            print("Número inválido. Tente novamente")
        else:
            break



# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
