from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the pygam 2-digit country code form the given country"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    
    #If country wans found return none
    return None

print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))
