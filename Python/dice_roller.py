# Automatic Dice Roller
# Written by Tim Weissman

from random import randint

print ("Automatic Dice Roller:") 
print("Press enter to roll or 'x' and then enter to exit.")
while True:
  user=input()#waits for the user to type and then press enter
  if len(user)==0:#If what the user typed nothing and then pressed enter it would be length zero
    print(randint(1,6))#pick random number 1-6
  elif user == "x":
    break#stop
