# first approach
def anagram_check(string1, string2):
    string1 = string1.replace(' ', '').lower()
    string2 = string2.replace(' ', '').lower()
    count1 = {}
    count2 = {}

    if set(string1) != set(string2):
        return False
    
    for i, j in zip(set(string1), set(string2)):
        count1[i] = string1.count(i)
        count2[j] = string2.count(j)
    if count1 == count2:
        return True
    
    return False

print(anagram_check('testing', 'test ing'))
print(anagram_check('public relations', 'crap built on lies'))

#string compression
def compress(strings):
    strings = sorted(strings)
    new = ''
    count = 1
    for i, j in enumerate(strings[:-1]):
        if j == strings[i+1]:
            count += 1
        else:
            new = new + j + str(count)
            count = 1
    return new

print(compress('aaaddccffoosj'))