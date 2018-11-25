def sumOfDigits(num):
    sum = 0
    while(num > 0):
        sum += num % 10
        num = num // 10
    return sum
print(max([sumOfDigits(a ** b) for a in range(1,100) for b in range(1, 100)]))
