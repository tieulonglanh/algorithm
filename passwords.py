def fib() :
    n,k = map(int, input().split())
    # create a list of 100 sub lists
    l = [[] for i in range(100)] 
    # store the passwords that have the same length into corresponding sub lists
    for i in range(n):
        tmp_ip = input()
        tmp_len = len(tmp_ip)
        l[tmp_len - 1].append(tmp_ip)
    # get real password and its length
    p = input()
    p_len = len(p)
    
    # limit the list of processing passwords (we do not need to process everything)
    exec_l = l[0:p_len]
    count_exec_p_min = 0
    count_exec_p_max = 0
    
    count = 0
    for i in range(p_len - 1):
        count += len(l[i])
    # get minimum amount of password that need to be input
    count_exec_p_min = count + 1
    # get maximum amount of password that need to be input
    count_exec_p_max = count + len(l[p_len - 1])
    min_time = 0
    max_time = 0
    
    # calculate min time
    if count_exec_p_min <= k:
        min_time = count_exec_p_min * 1
    else:
        i_min = count_exec_p_min // k
        r_min = count_exec_p_min % k
        if r_min != 0:
            min_time = k * i_min * 1 + i_min * 5 + r_min * 1
        else:
            min_time = k * i_min * 1 + (i_min - 1) * 5
    # calculate max time
    if count_exec_p_max <= k:
        max_time = count_exec_p_max * 1
    else:
        i_max = count_exec_p_max // k
        r_max = count_exec_p_max % k
        if r_max != 0:
            max_time = k * i_max * 1 + i_max * 5 + r_max * 1
        else:
            max_time = k * i_max * 1 + (i_max-1) * 5
    
    return str(min_time) + ' ' + str(max_time)
    
print(fib())
