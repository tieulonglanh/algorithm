def fib() :
    n = int(input())
    b = list(map(int, input().split()))
    if b[0] > 15:
        return 15
        
    for i in range(n-1):
        t1 = b[i+1] - b[i]
        if t1 > 15:
            t2 = b[i] + 15
            if t2 > 90:
                return 90
            else:
                return t2
    
    if b[-1] + 15 < 90:
        return b[-1] + 15
    
    return 90    
        
print(fib())
