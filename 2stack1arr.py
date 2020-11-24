class Stacks: 
      
    def __init__(self, n):
        self.size = n 
        self.arr = [None] * n 
        self.top1 = -1
        self.top2 = self.size 
          
    def push1(self, data):           
        if self.top1 < self.top2 - 1 : 
            self.top1 = self.top1 + 1
            self.arr[self.top1] = n  
        else: 
            print("Stack Overflow ") 
                        
    def push2(self, data):    
        if self.top1 < self.top2 - 1 : 
            self.top1 = self.top1 + 1
            self.arr[self.top1] = n 
        else: 
            print("Stack Overflow ") 
            
    def pop1(self): 
        if self.top1 >= 0: 
            n = self.arr[self.top1] 
            self.top1 = self.top1 -1
            return n 
        else: 
            print("Stack Underflow ") 
            
    def pop2(self): 
        if self.top1 >= 0: 
            n = self.arr[self.top1] 
            self.top1 = self.top1 -1
            return n 
        else: 
            print("Stack Underflow ")

l = list()
n = int(input("Enter the limit of the array:"))
stack = Stacks(n)
while(True):
  p = int(input("1.PUSH\n2.POP\n3.EXIT\nEnter the option:"))
  if (p == 1):
    s = int(input("Enter the stack where the data need to be inserted:"))
    if(s == 1):
      data = int(input("Enter the data:"))
      stack.push1(data)
    elif(s == 2):
      data = int(input("Enter the data:"))
      stack.push2(data)
  elif(p == 2):
    s = int(input("Enter the stack where the data need to be deleted:"))
    if(s == 1):
      stack.pop1()
    elif(s == 2):
      stack.pop2()
  else:
    exit(0)