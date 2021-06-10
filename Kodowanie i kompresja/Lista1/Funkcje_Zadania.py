import math


def Zadanie1(Sorted_Dictionary, counter):
    for key, value in Sorted_Dictionary.items():
        print(key+" wystepuje "+str(value) +
              " prawdopodobienstwo wynosi: "+str(value/counter))


def Zadanie2(Sorted_Dictionary, counter):
    Dictionary_with_entropy = {}
    for key, value in Sorted_Dictionary.items():
        val = value/counter
        val2 = counter/value
        val_log = math.log(val2, 2)
        Dictionary_with_entropy[key] = val_log*val
    outcome = 0
    for key, value in Dictionary_with_entropy.items():
        outcome += value
    print("Entropia wynosi "+str(outcome))
