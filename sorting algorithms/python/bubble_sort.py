def bubble_sort(array, visualize = False):
    swap = True
    step = 1
    while swap:
        swap = False
        for pos, i in enumerate(array[:-1]):
            if i <= array[pos+1]:
                pass
            else:
                array[pos], array[pos+1] = array[pos+1], array[pos]
                swap = True
        if visualize:
            print(f'list after step {step} -  {array}')
        step += 1
    return array

print(bubble_sort([1,6,7,9, 2, 3], True))