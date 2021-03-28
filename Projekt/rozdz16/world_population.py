import json
from pygal.maps.world import COUNTRIES
from country_codes import get_country_code
#load the data into a list
for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#print the 2010 population for each rountry
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ": "+ str(population))
        else:
            print('ERROR - ' + country_name)
