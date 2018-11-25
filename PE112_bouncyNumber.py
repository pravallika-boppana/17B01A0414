def isIncreasing(num):
    num = str(num)
    for i in range(0,len(num) - 1):
        if int(num[i]) > int(num[i + 1]):
            return False
    return True

def isDecreasing(num):
    num = str(num)
    for i in range(0,len(num) - 1):
        if int(num[i]) < int(num[i + 1]):
            return False
    return True

def isBouncy(num):
    if (not isIncreasing(num) and not isDecreasing(num)):
            return True
    return False

def leastNumber(percent):
    i = 100
    count = 0
    while True:
        if isBouncy(i):
            count += 1
                       
        if percent == int((count / i) * 100):
            return i
        i += 1
print(leastNumber(99))

 
