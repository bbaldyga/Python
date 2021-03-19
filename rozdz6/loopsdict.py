user_o ={
    'username': 'efermi',
    'first': 'enrico',
    'last':'fermi'
}
for key, value in user_o.items():
    print("\nKey "+key)
    print("\nValue "+value)

favorite_languages ={'jen':'python','sarah':'ruby','edward':'c'}
for name,language in favorite_languages.items():
    print(name.title()+ "'s favorite language is "+ language.title())

for name in favorite_languages.keys():
    print(name.title())
friend ={'sarah'}
for name in favorite_languages.keys():
    print(name.title())

    if(name in friend):
        print(" Hi " + name.title()+" , I see your language is "+
        favorite_languages[name].title()+"!")
#check if this key is in our keys in dict
if 'erin' not in favorite_languages.keys():
    print("Erin, test")
#looping throu sorted key in dict
for name in sorted(favorite_languages.keys()):
    print(name.title() + " thank you for takint the poll")
#looping throu values of dict
print("the following languages have been mentioned")
for language in favorite_languages.values():
    print(language.title())
