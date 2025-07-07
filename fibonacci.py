'''
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
'''
def print_fibonacci():
    sequence = [0, 1]

    while sequence[-1] + sequence[-2] <= 50:
      item = sequence[-1] + sequence[-2]
      sequence.append(item)

    result = ", ".join(str(x) for x in sequence)
    print(result)

print_fibonacci()
