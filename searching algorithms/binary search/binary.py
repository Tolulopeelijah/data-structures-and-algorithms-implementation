#sorted/ordered
def binary_search(arr, ele):
    while True:
        mid = len(arr) // 2
        if len(arr) == 1 and arr[mid] != ele:
            return False
        if arr[mid] == ele:
            return True
        elif arr[mid] < ele:
            arr = arr[mid:]
        arr = arr[:mid]




#using recursion 
def binary_search_recur(arr, ele):
    mid = len(arr) // 2
    if len(arr) == 1 and arr[mid] != ele:
        return False
    if arr[mid] == ele:
        return True
    elif arr[mid] > ele:
        return binary_search_recur(arr[:mid], ele)
    return binary_search_recur(arr[mid:], ele)


from random import randint
array = sorted([randint(0, 20) for i in range(10)])
ele = randint(0, 20)
print(f'array: {array}, element: {ele}')
print(binary_search_recur(array, ele))