import random
import os

def clearConsole():
    command = 'cls'
    os.system(command)

firstNum = random.randint(1,11)
secondNum = random.randint(11,21)
answer = random.randint(firstNum + 1, secondNum - 1)

print("Guess Da Number\n")
print("I'm thinking of a number " + str(firstNum) + " to " + str(secondNum))

print("\nWhat do you think the number is: ", end="") 
userInput = int(input())

if userInput == answer: 
	clearConsole()
	print("Correct!")

else:
	clearConsole()
	print("Wrong, the number was: " + str(answer))
	print("You Picked: " + str(userInput))

	if answer > userInput:
		print("You were off by: " + str(answer - userInput))

	if answer < userInput:
		print("You were off by: " + str(userInput - answer))

input()