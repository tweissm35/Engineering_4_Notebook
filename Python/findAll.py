def findAll(string, letter):
  return [i for i in range(len(string)) if string.startswith(letter, i)]
  #This elegent bit of code is from https://www.geeksforgeeks.org/python-all-occurrences-of-substring-in-string
  #It uses list comprehension with the startswith() method to find substrings all on one line!
