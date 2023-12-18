def func():
    n = int(input())
    input_arr = list(map(int, input().split()))
    
    alice_amount = 0
    alice_time = 0
    bob_amount = 0
    bob_time = 0
    alice_arr = input_arr[:]
    bob_arr = input_arr[::-1]
    
    
    for i in range(n):
        if alice_time <= bob_time:
            alice_amount += 1
            alice_time += alice_arr[alice_amount - 1]
        else:
            bob_amount += 1
            bob_time += bob_arr[bob_amount -1]
        if alice_amount + bob_amount == n:
            return [alice_amount, bob_amount]

result = func()
print(result[0], result[1])
            
