def doMath(num1, num2, op):#defines function
	if op == 1:#If the operator is  a 1  do the following line
		result = num1+num2
	elif op == 2:
		result = num1-num2
	elif op == 3:
		result = num1*num2
	elif op == 4:
		result =round(num1/num2,2)#rounds the result to two decimal places
	elif op == 5:
		result = num1%num2
	return str(result)#casts the result as a string
#Get the input and cast them as integers
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
#Print each version
print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))
