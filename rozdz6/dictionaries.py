#example of dictionary
alien_0 = {"color":'green', 'points':5}
print(alien_0['color'])
print(alien_0["points"])
#adding new key and value
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#modyfing values
alien_0['y_position'] = 100
print(alien_0)
#create variable with empty dictionary
#alien_0 = {}
del alien_0['points']
print(alien_0)
favorite_languages ={'jen':'python','sarah':'ruby','edward':'c'}
print("Sarah favorite language is "+favorite_languages['sarah'].title()+".")