N = int(input())
b = input()
g = input()
bride = []
groom = []

for i in range(N):
  a = b[i]
  bride.append(a)

for i in range(N):
  a = g[i]
  groom.append(a)  

count = N

front = 0
c = 0

for i in range(N*N):
  if(len(bride) == 0):
    break
    
  if(bride[front] == groom[front]):
    bride.pop(front)
    groom.pop(front)
    count -= 1
    c = 0
    continue

  else:
    a = groom.pop(0)
    groom.append(a)
    c += 1
    
    if(c >= N):
      break

print(count)
print("\n")