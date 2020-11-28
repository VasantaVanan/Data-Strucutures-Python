n = input().split()
b = int(n[0])
n = int(n[1])

def BubbleSort(z):
    for i in range(n):
        for j in range(n - i - 1):
            if (z[j] > z[j + 1]):
                t = z[j]
                z[j] = z[j + 1]
                z[j + 1] = t

z = input().split()
if (z[0].isalpha()):
    print("Invalid Input")
else:
    z = list(map(int, z))
    BubbleSort(z)
    flag = 1
    for i in range(n):
        if (b < z[i]):
            flag = 0
            break
        b = b - ((z[i] % 2) + (z[i] / 2))

    if (flag == 1):
        print("YES")
    else:
        print("NO")