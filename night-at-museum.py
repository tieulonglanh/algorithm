def fib() :
    s = input()
    b = []
    for i in range(len(s)):
        b.append(s[i])
    
    s = 'abcdefghijklmnopqrstuvwxyz'
    l = []
    for i in range(len(s)):
        l.append(s[i])
    rt = 0    
    
    if abs(0 - l.index(b[0])) > (len(s) - abs(0 - l.index(b[0]))):
        rt += len(s) - abs(0 - l.index(b[0]))
    else:
        rt += abs(0 - l.index(b[0]))
        
    for i in range(len(b)-1):
        if abs(l.index(b[i+1]) - l.index(b[i])) > (len(s) - abs(l.index(b[i+1]) - l.index(b[i]))):
            rt += (len(s) - abs(l.index(b[i+1]) - l.index(b[i])))
        else:
            rt += abs(l.index(b[i+1]) - l.index(b[i]))
        
    return rt
            
        
print(fib())
