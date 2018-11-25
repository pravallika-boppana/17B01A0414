def factorial(num):
    
    if num == 0:
       return 1
    f = num
    for i in range(2, num):
        f *= i
    return f
def NcR(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
print(NcR(5,5:))
print(len([NcR(n, r) for n in range(1, 101) for r in range(0, n + 1) if NcR(n,r) > 1000000]))


