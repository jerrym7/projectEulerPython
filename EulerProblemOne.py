'''
	This program is to get the sum of numbers that are
	multiple of 3 and 5
'''
def sum(value):
	sum = 0
	for i in range(1,value):
		if i % 3 == 0 or i % 5 == 0 :
			sum += i
	return sum	
print(sum(1000))