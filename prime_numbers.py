
'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''
def is_prime(n):
  number = 2
  while number < n:
    if n % number == 0:
      return False
    number = number + 1

  return True


def prime_numbers():
  number = 2

  while number < 100:
    if is_prime(number):
      print(number)
    number = number + 1

prime_numbers()
