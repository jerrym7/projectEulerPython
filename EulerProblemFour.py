def getProducts():
	max = 0
	for i in range(999,100,-1):
		for j in range(i,100,-1):
			result = i * j
			resultString = str(result)
			if checkIfPalin(resultString) == True :
				if max<result :
					max = result
	return max
			
def checkIfPalin(product):
	if product == product[::-1] : #check if the result is a palyndrome
		return True
	else: return False
print(getProducts())
	