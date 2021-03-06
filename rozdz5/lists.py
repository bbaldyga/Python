avaible_toppings = ['mushrooms','olives','green peppers'
                    'pepperoni']
requested_topping =  ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_topping:
    if requested_topping in avaible_toppings:
        print("Adding " + requested_topping+".")
    else: 
        print("Sorry we don't have "+ requested_topping)

print("\nFinished making your pizza!")
