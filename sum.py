def adds(value): #start of the function
	sum = 0 #start at sum = 0
	for i in range(1,value):#for loop from range 1 to value 
		sum+=i # keeps adding
	return sum # returns the sum
value = input("Enter value")#ask user to enter
print(adds(value)) #prints the sum
'''
	This program is design to ask a user for a value and sums from 1 to the
	the value given, returns the sum and prints to the user.
'''