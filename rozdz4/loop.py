magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title()+", TAK")
print("Kurtyna")

for value in range(1,5):
        print(value)
numbers = list(range(1,6))
print(numbers)
odd_numbers = list(range(1,12,2))
print(odd_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
squares2 = [value**2 for value in range(1,11)]
print(squares2)
for value in range(1,21):
    print(value)
#Zadania z milionem
milion = []
for value in range(1,1000001):
    milion.append(value)
#    print(value)
#print(min(milion))
#print(max(milion))
#print(sum(milion))
milion2 = milion[:]
thirds = list(range(3,31,3))
print(thirds)