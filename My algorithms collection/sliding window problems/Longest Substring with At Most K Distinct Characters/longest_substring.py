def longest_substring(s, k):
    if not s or k <= 0 or k > len(s):
        return

    maxi = ''
    count = {}
    start = end = 0
    while end < len(s):

        end_char = s[end]
        if end_char not in count:
            count[end_char] = 0
        count[end_char] += 1
        if end-start > len(maxi):
                maxi = s[start:end]
        while len(count) > k:
            count[s[start]] -= 1
            if  count[s[start]] == 0:
                del count[s[start]]
            start+= 1
        end += 1

    if end-start > len(maxi):
                maxi = s[start:end]
    return (maxi,  len(maxi))
                
print(longest_substring('araaci', 2))
