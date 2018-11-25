def areSameDigits(a, b):
    return sorted(str(a)) == sorted(str(b))
x = 1
while True:
    if areSameDigits(x, 2 * x) and areSameDigits(x, 3 * x) and areSameDigits(x, 4 * x) and areSameDigits(x, 5 * x) and areSameDigits(x, 6 * x):
        print(x)
        exit()
    x += 1




