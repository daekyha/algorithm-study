# lec 1104 - 거듭제곱 Iterative ver : 최선 O(log n)

def power(base, exp):
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    
    i=1
    res = base
    
    while i < exp:
        if 2*i <=exp:
            res  *= res
            i = 2*i
        else:
            res *= base 
            i += 1
            
    return res

print(power(2,1024))
            
    