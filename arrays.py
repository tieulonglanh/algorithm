def fib() :
    s = list(map(int, input().split()))
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if s[0] < p[0]:
        return 'NO'
    
    if s[1] < p[1]:
        return 'NO'
    
    if a[0] >= b[-1]:
        return 'NO'
    
    if a[-1] < b[0]:
        return 'YES'
    
    if a[p[0] - 1] < b[-p[1]]:
        return 'YES'
    
    for i in range(s[0] - p[0]):
        if a[i + p[0] - 1] >= b[-p[1]]:
            return 'NO'
        else:
            return 'YES'
    
    return 'NO'
            
        
print(fib())
