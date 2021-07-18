import math
import os

def clearConsole():
    command = 'cls'
    os.system(command)

def Add(a, b):
    clearConsole()
    return a + b

def Sub(a, b):
    clearConsole()
    answer = a - b
    error = "error"
    if answer < 0:
        return error
    else:
        return answer
def Multi(a, b):
    clearConsole()
    return a * b

def Div(a, b):
    clearConsole()
    return a / b
def Power(a, b):
    clearConsole()
    return math.pow(a, b)

print("Calculator\n")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")
print("5. Power")
print("\nChoice: ", end="");
choice = int(input());

if choice == 1:
    print("\na = ", end="");
    a = int(input())
    
    print("\nb = ", end="");
    b = int(input())
    
    answer = Add(a, b);
    print("Answer: " + str(answer))
    
if choice == 2:
    print("\na = ", end="");
    a = int(input())
    
    print("\nb = ", end="");
    b = int(input())
    
    answer = Sub(a, b);

    if (answer == "error"):
        print("\n\nError - below 0")
    else:
        print("Answer: " + str(answer))

if choice == 3:
    print("\na = ", end="");
    a = int(input())
    
    print("\nb = ", end="");
    b = int(input())
    
    answer = Multi(a, b);
    print("Answer: " + str(answer))

if choice == 4:
    print("\na = ", end="");
    a = int(input())
    
    print("\nb = ", end="");
    b = int(input())
    
    answer = Div(a, b);
    print("\nAnswer: " + str(answer))
    
if choice == 5:
    print("\nbase = ", end="");
    a = int(input())
    
    print("\nexponent = ", end="");
    b = int(input())

    answer = Power(a, b);
    print("Answer: " + str(answer))
    

if choice > 5:
    clearConsole()
    print("Error")

input()        
