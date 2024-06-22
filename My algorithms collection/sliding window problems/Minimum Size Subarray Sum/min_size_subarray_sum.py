def min_sum(arr, s):
    result = 0
    for ele in arr:
        result += ele
    if not arr or result < s:
        return 

    start = 0
    end = len(arr)
    mini = len(arr) #minimum length
    
    while result >= s and end > start:
        if sum(arr[start+1:end]) > sum(arr[start:end-1]):
            start += 1    
            result -= arr[start]
        else:
            end -= 1
            result -= arr[end]
        mini -= 1


            
    return mini
            
        
print(min_sum([1,2,5,3,7,9,11,2,3,19, 30, 46, 1, 78], 20))
