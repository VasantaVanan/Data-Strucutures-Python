N = int(input())
arr = list()
temp = [[0 for i in range(N)] for j in range(N)]
totalangle = 0

def rotate(angle):
    total = (angle / 90) % 4
    while(total > 0):
        for i in range(N):
            for j in range(N):
                temp[j][N - i - 1] = arr[i][j]
        for i in range(N):
            for j in range(N):
                arr[i][j] = temp[i][j]
                
        total -= 1



for i in range(N):
    e = input().split()
    arr.append(e)

while(True):
    choice = input().split()
    if(choice[0] == 'A'):
        angle = int(choice[1])
        rotate(angle)
        totalangle = totalangle + angle
    elif(choice[0] == 'Q'):
        row = int(choice[1])
        column = int(choice[2])
        print(arr[row - 1][column - 1])
    elif(choice[0] == 'U'):
        row = int(choice[1])
        column = int(choice[2])
        value = int(choice[3])
        rotate(360 - totalangle % 360)
        arr[row - 1][column - 1] = value
        rotate(totalangle)
    else:
        break        