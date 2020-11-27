import math
X = int(input())
Y = input()
N = int(input())
count = 0
i = 0
def isHappy(i):
    s = 0
    while(i > 0):
        s = s + (i % 10) * (i % 10)
        i = i // 10
    if (s == 1):
        return True
    elif (s == 4):
        return False
    return isHappy(s)

def isPrime(i):
    if (i == 1):
        return False
    for j in range(2, int(math.sqrt(i) + 1)):
        if ((i % j) == 0):
            return False
    return True

if(Y == '@'):
    print("Invalid Input")
else:
    Y = int(Y)
    if ((X > 0) or (Y > 0) or (Z > 0)):
        for i in range(X, Y+1):
            if(isPrime(i) and isHappy(i)):
                count += 1
            if (count == N):
                print(i)
                break
        else:
            print("No number is present at this index")