# Automatic Dice Roller
# Written by Tim Weissman

from random import randint

print ("Automatic Dice Roller:") 
print("Press enter to roll or 'x' and then enter to exit.")
while True:
  action=input()#waits for the user to type and then press enter
  if len(action)==0:#Checks if the thing entered is length zero
    print(randint(1,6))#pick random number 1-6
  elif action == "x":
    break#stop
