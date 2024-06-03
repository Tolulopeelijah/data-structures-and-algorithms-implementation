def bubble_sort(array, show_steps = False, ascending = True):
    swap = True
    step = 1
    while swap:
        swap = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                if ascending:
                    array[i], array[i+1] = array[i+1], array[i]
                    swap = True
            elif array[i] < array[i+1]:
                if not ascending:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swap = True

        if show_steps:
            print(f'list after step {step} -  {array}')
        step += 1
    return array


import random
random_array = [random.randint(0, 20) for _ in range(20)]
decreased_array = list(range(20, 0, -1))
increased_array = list(range(20))
print('randomized array: ', random_array)
print(bubble_sort(random_array, False, False))
print('array in its descreasing order: ', decreased_array)
print(bubble_sort(decreased_array, False,False))
print('array in its increasing order: ', increased_array)
print(bubble_sort(increased_array, False,False))