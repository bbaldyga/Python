filename = 'alice.txt'

try:
    with open(filename) as file_obj:
        contents = file_obj.read()
except FileNotFoundError:
    msg = "Sorry the file "+filename+" don't exist"
    print(msg)