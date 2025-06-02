def getNthFib(n):
    a, b = 0, 1
    if n == 0 or n == 1:
        return a
    if n == 2:
        return b
    while (n-2) > 0:
        c = a + b
        a = b 
        b = c

        n -= 1

    return c

    
        
    
