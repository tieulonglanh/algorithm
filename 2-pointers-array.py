def fnc():
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))

    count_arr = [0] * (10**5 + 1)
    unique = 0
    left = 0
    right = 0
    for i in range(n):
        if count_arr[arr[i]] == 0:
          unique += 1
        count_arr[arr[i]] += 1
        if unique == k:
          right = i
          break;
    
    if unique < k:
        print (-1, -1)
    if right == 0:
        print(1,1)
        return
    
    for j in range(right):
        if count_arr[arr[j]] > 1:
          left = j + 1
          count_arr[arr[j]] -= 1
        else:
          print(left + 1, right + 1)
          break;

fnc()

