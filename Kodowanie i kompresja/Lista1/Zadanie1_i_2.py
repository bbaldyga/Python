import collections
from Funkcje_Zadania import Zadanie1 as Z1
from Funkcje_Zadania import Zadanie2 as Z2
counter = 0
#filename = 'Test2.txt'
filename = 'Plik.txt'
dictionary_of_characters = {}
with open(filename, 'r') as file:
    for line in file:
        for character in line:
            if character in dictionary_of_characters:
                dictionary_of_characters[character] += 1
                counter += 1
            else:
                dictionary_of_characters[character] = 1
                counter += 1

Sorted_Dictionary = collections.OrderedDict(
    sorted(dictionary_of_characters.items()))
Z1(Sorted_Dictionary, counter)
print("\n")
Z2(Sorted_Dictionary, counter)
