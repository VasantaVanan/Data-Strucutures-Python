import math
k = int(input())
i = 0
def isPrime(i):
    if (i == 1):
        return False
    for j in range(2, int(math.sqrt(i) + 1)):
        if ((i % j) == 0):
            return False
    return True

while (k != 0):
    n = int(input())
    count = 0
    primeList = list()
    for i in range(2, n - 1):
        if (isPrime(i)):
            primeList.insert(count, i)
            count += 1

    primesCount = 0
    for i in range(1, count):
        s = 0
        for j in range(count):
            s = s + primeList[j]
            if (s == primeList[i]):
               primesCount += 1
    print(primesCount)