def fib() :
    s1 = input()
    s2 = input()
    
    # if s2 can be found in s1, then return automaton
    if s1.find(s2) != -1:
        return 'automaton'
    else:
        if len(s1) > len(s2):
            # check if can be automaton
            re = check_automaton(s1, s2)
            if re == True:
                return 'automaton'
        
        s1_len = len(s1)
        s2_len = len(s2)
                
        count = 0
        for i in range(len(s2)):
            if s1.find(s2[i]) == -1:
                count += 1
        
        # if there is any character of s2 is not in s1, then we sure need tree
        if count >= 1:
            return 'need tree'
        else:
            l1 = [[] for i in range(122)]
            for i in range(len(s1)):
                l1[ord(s1[i]) - 1].append(s1[i])
                
            l2 = [[] for i in range(122)]
            for i in range(len(s2)):
                l2[ord(s2[i]) - 1].append(s2[i])
            
            count_gt = 0
            count_eq = 0
            for i in range(len(l2)):
                if len(l2[i]) > len(l1[i]):
                    count_gt += 1
                if len(l2[i]) == len(l1[i]):
                    count_eq += 1
            
            # if amount of any character in s2 is more than the one in s1 then need tree
            if count_gt >= 1:
                return 'need tree'
            
            # if amount of characters in s2 the same as amount of them in s1 then array only
            if count_eq == len(l2):
                return 'array'
            
            return 'both'
                
def check_automaton(s1, s2):
    if len(s2) > 0:
        pos = s1.find(s2[0])
        if pos != -1:
            s1 = s1[pos+1:]
            s2 = s2[1:]
            result = check_automaton(s1, s2)
        else:
            return False
    else:
        return True
    return result    
print(fib())
