filename = 'programing.txt'
#with open(filename,'w') as file_object:
#    file_object.write("I love programing\n")
#    file_object.write("Bottom text\n")

with open(filename,'a') as file_object:
    file_object.write("Append 1\n")
    file_object.write("Append 2\n")
