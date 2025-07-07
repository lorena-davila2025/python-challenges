'''
* Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''

def is_anagram(word: str):
        count = len(word)
        chars = list(word)
        while count > 1:
            cond = chars.pop(0) == chars.pop(-1)
            if cond:
                print(chars, cond)
                print('next')
                count = count - 2
            else:
                return cond
                break

        return cond

print(is_anagram('ambcd12dcbma'))

# different solution

def is_anagram2(word: str):
        count = len(word)
        chars = list(word)
        if count % 2 != 0:
            chars.pop(count // 2)
            count = count - 1

        if chars[:count // 2] == chars[count // 2:]:
            return True
        else:
            return False

print(is_anagram('ambcd12dcbma'))

# ---time comparison----

import time

start = time.perf_counter()
is_anagram('amlb2xlma')
end = time.perf_counter()

print(f"Execution time is_anagram: {end - start:.6f} seconds")

# -------

start = time.perf_counter()
is_anagram2('amlb2xlma')
end = time.perf_counter()

print(f"Execution time is_anagram2: {end - start:.6f} seconds")
