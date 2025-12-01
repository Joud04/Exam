def scoreOfString(s):
    score = 0
    
    for i in range(len(s) - 1):
        val = ord(s[i])
        val_s = ord(s[i+1])
        
        diff = abs(val - val_s)
        
        score += diff
        
    return score

print(scoreOfString("hello")) 
print(scoreOfString("zaz"))   