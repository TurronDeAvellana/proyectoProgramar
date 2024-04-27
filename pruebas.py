"""
#1 El famoso Fizz Buzz

* Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzBuzz():
    for i in range(100):
        if (i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
        elif(i % 3 == 0):
            print("fizz")
        elif(i % 5 == 0):
            print("buzz")
        else:
            print(i)


"""
# 2 ¿Es un anagrama? 

 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 
"""

def anagrama(w1,w2):
    list1 = [letter for letter in w1]
    list2 = [letter for letter in w2]
    auxList = []

    for letter in list1:
        for letter2 in list2:
            if (letter == letter2):
                auxList.append(letter)
            else:
                None

    if (len(auxList) == len(list1) and len(auxList) == len(list2)):
        print(True)
    else:
        print(False)
    
    
            

        


    