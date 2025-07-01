#Given a string, return the length of the longest substring without repeating characters.
def longest_unique_substring(s):
        #Two Pointers
    left = 0
    right = 0

#Set
    store=set()

    max_len=0
    while right < len(s):
        if s[right] not in store:
            store.add(s[right])
            right+=1
            max_len=max(max_len,right-left)
    
        else:
            store.remove(s[left])
            left+=1
    return max_len

s="abcabcbb"
leng=longest_unique_substring(s)
print(leng)

