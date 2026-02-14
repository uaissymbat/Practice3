def isUsual(num):
    n = abs(num)
    
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //= 5
    
    return n == 1

n = int(input())

if isUsual(n):
    print("Yes")
else:
    print("No")