dictOfWords = {}
with open('data.txt', 'r') as file:
    encrypthedText = file.read().replace('\n', '')

# wypełnianie slownika pojedynczymi literami
for letter in encrypthedText:
    if letter not in dictOfWords:
        dictOfWords[letter] = 1


for i in range(len(dictOfWords), 256):
    bestString = ""
    bestCount = -100
    for i in range(0, len(encrypthedText)):
        checkedForBest = encrypthedText[i:i+2]
        count = 0
        if checkedForBest in dictOfWords:
            continue
        for j in range(0, len(encrypthedText)):
            pair = encrypthedText[j:j+2]
            if checkedForBest == pair:
                count = count+1
        if(count > bestCount):
            bestCount = count
            bestString = checkedForBest
    dictOfWords[bestString] = 1

#print(dictOfWords.items())
dictLen = len(dictOfWords)-1
largest = bin(dictLen)[2:]
counter = 0
for key, val in dictOfWords.items():
    dictOfWords[key] = bin(counter)[2:].zfill(len(largest))
    counter = counter + 1
print(dictOfWords.items())
print('\n')
with open('dictionaryData.txt', 'w') as file:
    for key, value in dictOfWords.items():
        file.write(key + " :"+value+'\n')
encodedText = ""
for i in range(0, len(encrypthedText), 2):
    textToEncode = encrypthedText[i:i+2]
    if textToEncode in dictOfWords:
        encodedText += dictOfWords[textToEncode]
    else:
        encodedText += dictOfWords[textToEncode[0]]
        encodedText += dictOfWords[textToEncode[1]]
print(encodedText+'\n')
with open('encodedData.txt', 'w') as file:
    file.write(encodedText)

decodedText = ""
for i in range(0, len(encodedText), len(largest)):
    textToDecode = encodedText[i:i+len(largest)]
    for key, value in dictOfWords.items():
        if value == textToDecode:
            decodedText += key

print(decodedText+'\n')

print("Ilosc znakow przed kompresja: %d" % len(encrypthedText))
print("Ilosc znakow po kompresji: %d" %(len(encodedText)/8))