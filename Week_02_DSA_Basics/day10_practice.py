def is_palindrome(s):
    # cleaned=""
    # for ch in s:
    #     if ch.isalnum():
    #         cleaned+=ch.lower()
    s=''.join(ch.lower() for ch in s if ch.isalnum())
    left =0
    right = len(s) - 1
    
    while left<right:
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    
    return True
print(is_palindrome("A man, a plan, a canal: Panama")) 
from collections import Counter

def find_anagrams(s,p):
    res=[]
    p_count= Counter(p)
    # z=len(p)
    # first_window=s[0:z]
    # window=Counter(first_window)
    
    window = Counter(s[0:len(p)])
    if window==p_count:
        res.append(0)
    
    for i in range(len(p),len(s)):
        window[s[i]]+=1
        
        window[s[i-len(p)]]-=1
        if window[s[i-len(p)]] == 0:
            del window[s[i-len(p)]]
            
        if window == p_count:
            res.append(i-len(p)+1)
    
    return res

print(find_anagrams("cbaebabacd", "abc"))       
