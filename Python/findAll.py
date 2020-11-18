def findAll(string, letter):
  return [i for i in range(len(string)) if string.startswith(letter, i)]
