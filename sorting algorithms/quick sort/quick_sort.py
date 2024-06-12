def quick_sort(array, pivot):
    if len(array) <= 1:
        return array
    left = array[:pivot]
    right = array[pivot:]
    sort(left)
    sort(right)


def sort(left, right):
    r = l = 0
    while l <= r:
        if left[l] 