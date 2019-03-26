def numPrime(num): #gets the numth prime number
	numOfPrimes = 0
	currentNum = 1
	while numOfPrimes != num :
		if isPrime(currentNum):
			numOfPrimes += 1
			print(currentNum)
			if numOfPrimes == num: #if the one we look is here, then 
				continue #we dont want to add one
			else: currentNum = currentNum + 1
		else:
			currentNum = currentNum + 1
		print("Current nth prime number is " +str(numOfPrimes))
	return currentNum
def isPrime(value):
	list = []
	for i in range(1, value + 1):
		   if value % i == 0:
			   list.append(i)
	if len(list) == 2 : #if factor only are of size 2 then it means
		return True #that the value is a prime number
	else:
		return False
print("Result is "+str(numPrime(10001)))