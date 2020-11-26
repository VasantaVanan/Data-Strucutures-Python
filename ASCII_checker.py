T = int(input())
strings = list()
while (T != 0):
    s = input()
    strings.append(s)
    T -= 1

for i in range(len(strings)):
    word = strings[i]
    length = len(word)
    arr = list()
    for j in range(26):
        arr.append(0)
    flag = 1
    for j in range(length):
        arr[ord(word[j]) - 97] += 1
    for j in range(26):
        if((arr[j] != 0) and (arr[j] != j+1)):
            flag = 0
            break
    if(flag == 1):
        print("Yes")
    else:
        print("No")
