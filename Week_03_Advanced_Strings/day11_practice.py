def is_subsequence(s,t):
    i=0
    for ch in t:
        if i < len(s) and s[i]==ch:
            i+=1
    return i==len(s)

def longest_common_substring(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    result = 0

    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                result = max(result, dp[i+1][j+1])
    return result