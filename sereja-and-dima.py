def bigofunc():
    n = int(input())
    n_arr = list(map(int, input().split()))
    
    sereja_points = 0
    dima_points = 0
    
    left = 0
    right = -1
    
    sereja_pick_count = 0
    dima_pick_count = 0
    
    for i in range(n):
        if i%2 == 0:
            if n_arr[left] > n_arr[right]:
                sereja_points += n_arr[left]
                left += 1
            else:
                sereja_points += n_arr[right]
                right -= 1
            sereja_pick_count += 1
        else:
            if n_arr[left] > n_arr[right]:
                dima_points += n_arr[left]
                left += 1
            else:
                dima_points += n_arr[right]
                right -= 1
            dima_pick_count += 1
        
        if sereja_pick_count + dima_pick_count == n:
            return [sereja_points, dima_points]
                
            
result = bigofunc()
print(result[0], result[1])
            
