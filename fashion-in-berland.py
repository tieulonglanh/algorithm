def fib() :
    n = int(input())
    b = list(map(int, input().split()))
    if(n == 1) :
        if b[0] == 1:
            return 'YES'
        else:
            return 'NO'
    else:
        count = 0
        for i in range(len(b)):
            if b[i] == 0:
                count+=1
        if count != 1:
            return 'NO'
        else:
            return 'YES'
print(fib())
