# Pseudo code for the sorting algorithms


## Bubble Sort
```function bubbleSort(arr)
    n = arr.length
    for i from 0 to n-1
        for j from 0 to n-i-1
            if arr[j] > arr[j+1]
                swap arr[j] and arr[j+1]
    return arr
```


## Selection Sort
```function selectionSort(arr)
    n = arr.length
    for i from 0 to n-1
        minIndex = i
        for j from i+1 to n-1
            if arr[j] < arr[minIndex]
                minIndex = j
        swap arr[i] and arr[minIndex]
    return arr
```


## Insertion Sort
```function insertionSort(arr)
    n = arr.length
    for i from 1 to n-1
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr
```


## Merge Sort
```function mergeSort(arr)
    if arr.length <= 1
        return arr
    mid = arr.length / 2
    left = mergeSort(arr[0...mid])
    right = mergeSort(arr[mid...])
    return merge(left, right)


function merge(left, right)
    result = []
    while left is not empty and right is not empty
        if left[0] <= right[0]
            result.push(left[0])
            left = left[1...]
        else
            result.push(right[0])
            right = right[1...]
    while left is not empty
        result.push(left[0])
        left = left[1...]
    while right is not empty
        result.push(right[0])
        right = right[1...]
    return result
```


## Quick Sort
```function quickSort(arr)
    if arr.length <= 1
        return arr
    pivot = arr[arr.length / 2]
    left = [], right = []
    for each x in arr
        if x < pivot
            left.push(x)
        else if x > pivot
            right.push(x)
    return concatenate(quickSort(left), [pivot], quickSort(right))
```
