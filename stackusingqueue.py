#IN THIS PROGRAM POP IS MADE COSTLY(METHOD 2)

from queue import Queue

q1 = Queue()
q2 = Queue()
f1, f2, r1, r2 = -1, -1, -1, -1
while True:
  print("1.PUSH\n2.POP\n3.EXIT")
  opn = int(input("Enter the option:"))
  if (opn == 1):
    x = int(input("Enter the element:"))
    if(f1 == -1):
      q1.put(x)
      f1, r1 = 0, 0
    else:
      q1.put(x)
      r1 += 1
  elif(opn == 2):
    if(f1 == -1):
      print("Stack Underflow")
    else:
      while(f1 < r1):
        e = q1.get()
        q2.put(e)
        f2 = 0
        r2 += 1
        f1 += 1
      if(f1 == r1):
        print(q1.get())
        f1, r1 = -1, -1
      while(f2 <= r2 and f2 != -1):
        e = q2.get()
        q1.put(e)
        f2 += 1
        f1 = 0
        r1 += 1
      f2, r2 = -1, -1
  elif(opn == 3):
    break