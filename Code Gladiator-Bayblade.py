T = int(input())
while(T != 0):
    N = int(input())
    G_Rev = input().split()
    Opp = input().split()
    G_Rev = list(map(int, G_Rev))
    Opp = list(map(int, Opp))
    G_Rev.sort()
    Opp.sort()
    count = 0
    for i in range(N):
      if(a != N):
        for j in range(a, N):
            if(G_Rev[j] > Opp[i]):
                count += 1
                a += 1
                break
            a += 1
      else:
        break
            
    print(count)
    T -= 1