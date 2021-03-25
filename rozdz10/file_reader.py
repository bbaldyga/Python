filename = 'pi_digits.txt'
pi_string = ''
with open(filename) as file_object:
        #print(line)
        #print(line.rstrip())
        lines = file_object.readlines()
    #contents = file_object.read()
    #print(contents)
    #print(contents.rstrip())
for line in lines:
    pi_string +=line.strip()
print(pi_string)
print(len(pi_string))
#page 194