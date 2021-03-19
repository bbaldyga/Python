#current_number = 1
#while current_number <=5:
#    print(current_number)
#    current_number+=1

#prompt = "\nTell me sonething and i wil repear ti back"
#prompt+="\nEnter 'quit' to end the program"
#message = ""
#while message != 'quit':
#    message = input(prompt)
#    print(message)

#using flag
#prompt = "\nTell me sonething and i wil repear ti back"
#prompt+="\nEnter 'quit' to end the program"
#message = ""
#active = True
#while active:
#    if message =='quit':
#        active = False
#    else:
#        message = input(prompt)
#        print(message)

#using break to exit loop
#prompt = "\nTell me sonething and i wil repear ti back"
#prompt+="\nEnter 'quit' to end the program"
#message = ""
#while True:
#    if message =='quit':
#        break
#    else:
#        message = input(prompt)
#        print(message)
#using continue
current_number = 0
while current_number<10:
    current_number+=1
    if current_number % 2 ==0:
        continue

    print(current_number)
#page 128