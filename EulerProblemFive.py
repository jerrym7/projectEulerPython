'''
	#Checks for the minimum number to be divisible by 1-20
	Problem:
		Sample: 2520 is the smallest number that can be divided by 
		each of the numbers from 1 to 10 without any remainder.

		Question: What is the smallest positive number that is evenly 
		divisible by all of the numbers from 1 to 20?
'''
import time
def smallestMultiple(): #function to get smalles number divisible...
	x = [i for i in range(11,21,1)]
	num = 2520
	while True :
		if  all(num % i == 0 for i in x) : #check if all remainder are 0
			return num
		num = num + 2520
startTime = time.time() #check how much it takes(later use)
print(smallestMultiple()) #print number
deltaTime = time.time() - startTime #find the differnve
print(deltaTime) #print in miliseconds the time it took