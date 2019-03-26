from math import pow
def diff(num):
	eachSquare = 0
	allSquare = 0
	for i in range(1,num+1): #1 - 100
		eachSquare += pow(i,2)
	for i in range(1,num+1):
		allSquare += i
	allSquare = pow(allSquare,2)
	result = allSquare - eachSquare
	return result
print(int(diff(100)))