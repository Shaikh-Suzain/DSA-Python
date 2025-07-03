def longest_palindrome(s):
    def expand(l,r):
        while l>=0 and r < len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
    
    result=""
    for i in range(len(s)):
        temp1=expand(i,i)

        temp2=expand(i,i+1)
        if len(temp1)>len(result):
            result=temp1
        if len(temp2)>len(result):
            result = temp2
    
    return result
print(longest_palindrome("babad")) 