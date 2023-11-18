def fib() :
    s1 = input()
    s2 = input()
    length = len(s1)
    
    if len(s1) == 1:
        if ord(s1) + 1 < ord(s2):
            return chr(ord(s1) + 1)
        else:
            return 'No such string'
    
    pos = 0
    for i in range(length):
        if s1[i] != s2[i]:
           pos = i
           break
    
    if pos == length - 1:
        if ord(s1[-1]) + 1 < ord(s2[-1]):
            return s1[0:length - 1] + chr(ord(s1[-1]) + 1)
        else:
            return 'No such string'
    else:
        if ord(s1[-1]) + 1 > 122:
            tmp = ''
            for i in range(length - 1 - pos):
                tmp += 'a'
            return s2[0:pos + 1] + tmp
        
        return s1[0:length - 1] + chr(ord(s1[-1]) + 1)
        
print(fib())
