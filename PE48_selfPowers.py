def sumOfSelfPowers(num):
    sum = 1
    for i in range(2, num + 1):
        sum += i ** i
    return sum
ans = sumOfSelfPowers(1000)
print(ans)
print(str(ans)[-10:])
