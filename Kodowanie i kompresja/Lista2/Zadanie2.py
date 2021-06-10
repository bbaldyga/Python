import random
tab = {}
filename = 'litery.txt'
with open(filename, 'r') as file:
    for lines in file:
        for character in lines:
            tab[character] = 0
print(tab)
words = []
counter = 0
filename2 = '4wyrazy.txt'
with open(filename2, 'r') as file:
    for lines in file:
        for character in lines:
            if(not character.isspace()):
                tab[character] += 1
                counter += 1
for key, value in tab.items():
    tab[key] = value/counter
for key, value in tab.items():
    print('\n Litera '+str(key)+" "+str(value))
# tablica prawdopodobienstwa
distrib = list(tab.values())
# talica liter
letters = list(tab.keys())
# obliczanie dystybuanty liter
for item in range(1, len(distrib)):
    distrib[item] += distrib[item-1]
for item in range(0, len(distrib)-1):
    print(distrib[item])
words = []
for randomised_word in range(0, 200):
    word = ""
    for created_word in range(0, 4):
        val = random.random()
        for item in range(0, len(distrib)-1):
            if(distrib[item] >= val):
                word += letters[item]
                break
    words.append(word)
for word in words:
    print("\n Wyraz "+word)
