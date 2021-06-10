def permute(s):
    out = []
    if len(s) == 1:
        return s
    else:
        for i,let in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [let + perm]
    return out

def permute_with_list(s):
    list_of_strings = []
    for i in range(1,s+1):
        list_of_strings.append(str(i))
    return permute(list_of_strings)
    

