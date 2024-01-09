"""
File: 2_fizzbuzz.py
----------------------
The `fizzbuzz` function takes an input parameter `num` and iterates through numbers from 1 to `num`.
It checks the divisibility of each number by 3, 5, or both, and prints "fizz," "buzz," "fizzbuzz," or
the number itself accordingly. It also keeps track of the counts for "fizz," "buzz," and "fizzbuzz."

Finally, it prints the total counts of "fizz," "buzz," and "fizzbuzz."

The `main` function takes user input for a number and calls the `fizzbuzz` function with that input.
"""


def fizzbuzz(num):
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0
    for i in range(1, (num+1)):
        if (i % 3) == 0 and (i % 5) == 0:
            fizzbuzz_count += 1
            print("fizzbuzz")
        elif (i % 3) == 0:
            fizz_count += 1
            print("fizz")
        elif (i % 5) == 0:
            buzz_count += 1
            print("buzz")
        else:
            print(i)

    print(f'Você teve {fizz_count} FIZZ! \n\n Você teve {buzz_count} BUZZ! \n\n Você teve {fizzbuzz_count} FIZZBUZZ!')

def main():
    num = int(input("Introduza um número inteiro para jogar o Fizzbuzz: "))
    fizzbuzz(num)

# Esta linha fornecida é necessária no final de um ficheiro Python
# para chamar a função main().
if __name__ == '__main__':
    main()
