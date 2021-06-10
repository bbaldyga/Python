d1 = 0
d2 = 0
g1 = 1
g2 = 1
inputText = input("Wpisz tekst jaki mamy zakodowac: ")

dictionary_of_characters = {}
counter = 0
marker = ""

# Zliczanie znaków w pliku
for character in inputText:
    if character in dictionary_of_characters:
        dictionary_of_characters[character] += 1
    else:
        dictionary_of_characters[character] = 1
prob = []
# liczenie modelu
for key, value in dictionary_of_characters.items():
    prob.append(value/len(inputText))
print(dictionary_of_characters)
print(prob)

CreateF = []
CreateF.append(0)
keys_list = list(dictionary_of_characters)
for i in range(1, len(prob)+1):
    CreateF.append(CreateF[i-1] + prob[i-1])
    print(CreateF[i])


for letter in inputText:
    for key, value in dictionary_of_characters.items():
        if key == letter:
            counter = keys_list.index(key)+1
            marker += str(counter)
    d1 = d1 + (g1 - d1) * CreateF[counter-1]
    g2 = d2 + (g2 - d2) * CreateF[counter]
    d2 = d1
    g1 = g2

print("Znacznik " + inputText + " to " + str(((g2+d2)/2)))
print("Odkodowany znacznik to: " + marker)
