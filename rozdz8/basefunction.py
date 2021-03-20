def greet_user(username):
    """Display a simple greetings"""
    print("Hello, "+username.title()+"!")
greet_user("Jesse")

#positional Argunemts
def descirbe_pet(animal_type,pet_name):
    """Display information about a pet"""
    print("\nI Have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")

descirbe_pet("Mice","Jerry")

#Keyword Arguments

descirbe_pet(animal_type="Hamster",pet_name="Harry")
descirbe_pet(pet_name="Harry",animal_type="Hamster")

#Default Values

def descirbe_pet(pet_name,animal_type ='dog'):
    """Display information about a pet"""
    print("\nI Have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
descirbe_pet(pet_name='Willie')
descirbe_pet(pet_name='Willie',animal_type="Hamster")

#Return Values

def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formated"""
    full_name = first_name+" "+last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)
def get_formatted_name(first_name,last_name,middle_name =''):
    """Return a full name, neatly formated"""
    if middle_name: 
        full_name = first_name+" "+middle_name+" "+last_name
    else:
        full_name = first_name+" "+last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('jimi','hendrix','Lee')
print(musician)

#returning a dictionary

def build_person(first_name,last_name,age=""):
    """Return a dictionary of information about a person"""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix',age=27)
print(musician)

#function with a while loop

while True:
    print("Please tell me your name: ")
    print("Enter q to quit")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formated_name = get_formatted_name(f_name,l_name)
    print("\nHello, "+formated_name+"!")

    #Passing list to a function
def greet_user(names):
    """Print a simple greeting to reach user in the list."""
    for name in names:
        msg = "Hello "+name.title()+"!"
        print(msg)

users = ["hanah","ty","margot"]
greet_user(users)

#modyfy a list
#Start with some designt that need to be printed
unprinted_design = ['iphone case', 'robot pedant', 'dodecahedron']
completed_desigh = []

#Simulate printing each desing until nene are left.
#move each design to completed design after printing
while unprinted_design:
    current_design = unprinted_design.pop()
    #Simulate creatng 3d printing form the design
    print("Printing model: "+current_design)
    completed_desigh.append(current_design)
#Display all completed models
print("\nThe folllowing models ahve been printed: ")
for completed_model in completed_desigh:
    print(completed_model)
def print_model(unprinted_design,compleated_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing. 
    """
    while unprinted_design:
        current_design = unprinted_design.pop()
        #Simulate creatng 3d printing form the design
        print("Printing model: "+current_design)
        completed_desigh.append(current_design)
def show_completed_models(completed_models):
    """Show all models that are completed"""
    print("\nThe folllowing models ahve been printed: ")
    for completed_model in completed_desigh:
        print(completed_model)
unprinted_design = ['iphone case', 'robot pedant', 'dodecahedron']
completed_desigh = []
print_model(unprinted_design,completed_desigh)
show_completed_models(completed_desigh)

#prevent function form modyfiong the list
#Send a copy of the list
print_model(unprinted_design[:],completed_desigh)
show_completed_models(completed_desigh)

#Passing arbitaty numbert of arguments
#page 151
