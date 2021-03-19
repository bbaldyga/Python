alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#empty list for sorting aliens
aliens =[]

#make 30 aliens
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] =='yellow':
        alien['color'] ='red'
        alien['speed'] = 15
#show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens are created
print("Total number of aliens: "+ str(len(aliens)))


#store inforamation about a pizza being ordered
pizza ={
    'crust':'thick',
    'toppings':['mushroms', 'extra cheese']
    }
#sumorise the order
print("you orderer a "+pizza['crust']+"- crust pizza "+ "with following topping")
for topping in pizza['toppings']:
    print("\t "+topping)
#nested dict
users ={'aeinstein':{
    'first': 'albert',
    'last': 'einstein',
    'location':'princeton',
},
'mcurie':{
    'first':'marie',
    'last':'curie',
    'location':'paris',
},
}
for username, userinfo in users.items():
    print("\nUsername: "+username)
    fullname = userinfo['first']+" "+userinfo['last']
    location = userinfo['location']

    print('\tFullName'+fullname.title())
    print('\tLocation'+ location.title())

