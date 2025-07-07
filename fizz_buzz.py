'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

def fizz_buzz():
    count = 1
    while count <= 100:
        result = count
        if count % 15 == 0 :
            result = 'fizzbuzz'
        elif count % 3 == 0:
            result = 'fizz'
        elif count % 5 == 0:
            result = 'buzz'

        print(result)
        print("\n")
        count = count + 1

fizz_buzz()
