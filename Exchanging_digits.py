i = str(input())

ip = i.split()

A = ip[0]
B = int(ip[1])

min = 10**7
count = 0
 
def permutation(str1, i, n, p): 
	global min, count 
	if (i == n): 
		
		str1 = "".join(str1) 
		q = int(str1) 

		if (q - p > 0 and q < min): 
			min = q 
			count = 1
	else: 
		for j in range(i, n + 1): 
			
			str1[i], str1[j] = str1[j], str1[i] 
			permutation(str1, i + 1, n, p) 
			str1[i], str1[j] = str1[j], str1[i] 

	return min 

str2 = str(A) 
str1 = [i for i in str2] 
le = len(str1) 

h = permutation(str1, 0, le - 1, B) 

if count == 1: 
	print(h) 
else: 
	print(-1)