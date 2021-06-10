import random
tab = []
filename = 'litery.txt'
with open(filename, 'r') as file:
    for lines in file:
        for character in lines:
            tab.append(character)
print(tab)
words = []
for randomised_words in range(0, 200):
    word = ""
    for created_words in range(0, 4):
        word += tab[random.randint(0, len(tab)-1)]
    words.append(word)
for word in words:
    print("\n Wyraz: "+word)
