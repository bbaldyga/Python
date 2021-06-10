from permutacje_funkcje import permute_with_list
def split(word):
    return [char for char in word]
def eight_queens(permutations):
    out = []
    check = []
    for permutation in permutations:
        #check.clear()
        addperm = True
        #for letters in permutation:
        #    for letter in letters:
        #        check.append(letter)
        check = permutation
        for col in range(len(check)-1):
            if addperm == False:
                break
            colnum = col
            rownum = int(check[col])
            while (colnum>-1 and colnum<(len(check))):
                colnum +=1
                rownum += 1
                if colnum>-1 and colnum < (len(check)):
                    if check[colnum] == str(rownum):
                        addperm = False
            if addperm == False:
                break
            colnum = col
            rownum = int(check[col])
            while (colnum>-1 and colnum<(len(check))):
                colnum +=1
                rownum -= 1
                if colnum>-1 and colnum < (len(check)):
                    if check[colnum] == str(rownum):
                        addperm = False
            if addperm == False:
                break
            colnum = col
            rownum = int(check[col])
            while (colnum>-1 and colnum<(len(check))):
                colnum -=1
                rownum += 1
                if colnum>-1 and colnum < (len(check)):
                    if check[colnum] == str(rownum):
                        addperm = False
            if addperm == False:
                break
            colnum = col
            rownum = int(check[col])
            while (colnum>-1 and colnum<(len(check))):
                colnum -=1
                rownum -= 1
                if colnum>-1 and colnum < (len(check)):
                    if check[colnum] == str(rownum):
                        addperm = False
            if addperm == False:
                break
        if addperm == True:
            out.append(check)
    return out

l = permute_with_list(8)
#print(l)
answ = eight_queens(l)
print(answ)
print(len(answ))