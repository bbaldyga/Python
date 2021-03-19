#statt with user that need to be verified
#and an empty list to hold comfirmed users.
uncomfirmed_users = ['alice','brian','candace']
comfired_users =[]
#verify each users until there are no more unconfirmed users
#move  each verified users into the list pf confirmed users
while uncomfirmed_users:
    current_user = uncomfirmed_users.pop()

    print("Veryfing user: "+ current_user.title())
    comfired_users.append(current_user)

#display all comfired users
print("\nThe followint users have been comfirmed")
for comfired_user in comfired_users:
    print(comfired_user.title())

#removing all instances of specific values form a list

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
while 'cat' in pets:
    pets.remove('cat')

print(pets)

#Filling dictionary with user inputs

responses ={}
#set a falg to incicate that polling is active
polling_active = True

while polling_active:
    #Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")
    #store response in dictionary
    responses[name] = response
    #find ouy if anyone else is going to take a poll
    repeat = input("\nWould you like to sign a petiton")
    if repeat =='no':
        polling_active = False

#polling is complete show the resoults
print("\n ---- Pols Results ---")
for name,response in responses.items():
    print(name +" would like to climb " +response+".") 