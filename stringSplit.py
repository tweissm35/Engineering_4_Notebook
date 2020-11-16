s=input("Please enter a sentence: ")

arr = s.split(" ")#make a list with each element being a word separated by a space

for i in range(len(arr)):#repeat for each word
	for j in range(len(arr[i])):#repeat for each letter
		print(arr[i][j])#prints a letter
	print("-")
