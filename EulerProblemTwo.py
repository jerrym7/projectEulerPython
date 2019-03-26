'''
	In this program, we calculate the fibinacci sequence,
	then sum all even numbers from that list that are less than 
	4,000,000 and are even numbers and return the sum.
'''
def fib(numbers):
	sum = [1, 2]
	for i in range(0, numbers):
		if sum[i] + sum[i+1] > numbers :
			return sum
		else: sum.append(sum[i] + sum[i+1])
	return sum
	
def sumEvenFib():
	numbers = 4000000
	list = fib(numbers)
	sum = 0
	for i in range(0,len(list)):
		if list[i] > numbers :
			return sum
		else: 
			if list[i] % 2 == 0 :
				sum += list[i]
	return sum
print(sumEvenFib())