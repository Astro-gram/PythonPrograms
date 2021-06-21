import os
import random

def clearConsole():
    command = 'cls'
    os.system(command)

def easy():
    clearConsole()

    print("EASY\n")
    
    a = random.randint(1,101)
    b = random.randint(1,101)

    correctAnswer = a + b

    print(str(a) + " + " + str(b) + " = ", end="")
    answer = int(input())
    clearConsole()

    if correctAnswer == answer:
        print("Correct!")
    if correctAnswer != answer:
        print("Wrong")
        print("Answer was: " + str(correctAnswer))

def medium():
    clearConsole()
    print("MEDIUM\n")

    a = random.randint(1,21)
    b = random.randint(1,21)

    correctAnswer = a * b

    print(str(a) + " * " + str(b) + " = ", end="")
    answer = int(input())
    clearConsole()

    if correctAnswer == answer:
        print("Correct!")
    if correctAnswer != answer:
        print("Wrong")
        print("Answer was: " + str(correctAnswer))

def hard():
    clearConsole()
    print("HARD\n")

    a = random.randint(50,101)
    b = random.randint(1,21)
    c = random.randint(1,21)

    correctAnswer = (a / b) * c

    print("(" + str(a) + " / " + str(b) + " )" + " * " + str(c) + " = ", end="")
    answer = int(input())
    clearConsole()

    if correctAnswer == answer:
        print("Correct!")
    if correctAnswer != answer:
        print("Wrong")
        print("Answer was: " + str(correctAnswer))

print("Math\n")
print("1. Easy")
print("2. Medium")
print("3. Hard")
print("\nChoice: ", end="")
choice = int(input())

if choice == 1:
    easy()
if choice == 2:
    medium()
if choice == 3:
    hard()
if choice > 3:
    clearConsole()
    print("ERROR: difficulty not found")



print("\n\nPress '9' to go back: ", end="")
back = int(input())

if back == 9:
    clearConsole()
    print("Get pranked nerd B)")

input()
