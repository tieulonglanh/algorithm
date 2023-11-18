def fib() :
    n = int(input())
    l = []
    l_mix = []
    
    for i in range(n):
        ip = list(map(int, input().split()))
        l.append(ip)
        l_mix.append(ip[0])
        l_mix.append(ip[-1])
        
    min_val = min(l_mix)
    max_val = max(l_mix)
    
    for i in range(len(l)):
        if l[i][0] == min_val and l[i][-1] == max_val:
            return i + 1
            
    return -1
print(fib())
