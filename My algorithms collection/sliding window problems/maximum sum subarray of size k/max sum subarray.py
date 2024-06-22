def subarray(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 
    
    max_sum = 0
    for i in range(k):
        max_sum += arr[i]
    maximum = max_sum
    for i in range(k, len(arr)):
        max_sum += arr[i]
        max_sum -= arr[i-k]
        if max_sum > maximum:
            maximum = max_sum

    return maximum

            
