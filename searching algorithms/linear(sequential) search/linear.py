#for unordered array
def seq(arr, ele):
    count = 0
    for each in arr:
        if each == ele:
            print(count)
            return True
        count += 1
    print(count)
    return False

# for ordered array
def ordered_seq(arr, ele):
    count = 0
    for each in arr:
        if each == ele:
            print(count)
            return True
        elif each > ele:
            print(count)
            return False
        count += 1
    print(count)
    return False 


array = [5, 6, 1, 2, 7, 9 ,10, 20, 9, 8] # len = 10
print(array, 3)           
print(seq(array, 3)) # False
print(array, 8)           
print(seq(array, 8)) #True

array.sort()
print(array, 3)
print(ordered_seq(array, 3)) # True
print(array, 8)           
print(ordered_seq(array, 8)) # False