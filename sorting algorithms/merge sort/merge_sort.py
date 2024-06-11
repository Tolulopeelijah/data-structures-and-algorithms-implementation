def merge_sort(array): #splitting
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    l = 0
    r = 0
    sorted = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted.append(left[l])
            l += 1
        else:
            sorted.append(right[r])
            r += 1
        
    while l < len(left):
        sorted.append(left[l])
        l += 1
    while r < len(right):
        sorted.append(right[r])
        r += 1

    return sorted


array = [5, 4, 2, 3, 1, 7, 9]
print(merge_sort(array))