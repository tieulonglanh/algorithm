def func():
    n,m = map(int, input().split())
    n_arr = list(map(int, input().split()))
    m_arr = list(map(int, input().split()))
    count = 0
    j = 0
    for i in range(n):
        is_available = False
        for k in range(j, m):
            if n_arr[i] <= m_arr[k]:
                j = k+1
                is_available = True
                break
        if is_available == False:
            count += 1
    return count

result = func()
print(result)
