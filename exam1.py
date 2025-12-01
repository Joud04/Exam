def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        s1 = expand(s, i, i)
        s2 = expand(s, i, i+1)
        
        if len(s1) > len(res): res = s1
        if len(s2) > len(res): res = s2
    return res

print(longest_palindrome("babad")) 
print(longest_palindrome("cbbd"))  