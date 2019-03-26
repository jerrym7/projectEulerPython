import math
def facList(numbers):
	sum = []
	for i in range(1, int (math.sqrt(numbers)) + 1):
		if numbers % i == 0 :
			sum.append(int (i))
			sum.append(int (numbers/i))
	return sum
def findPrime():
	list = facList(600851475143)
	maxNumber = -1
	primeList = []
	for i in list:
		if len(facList(i)) <= 2 :
			if maxNumber<i :
				maxNumber = i
				
	return maxNumber
print(findPrime())