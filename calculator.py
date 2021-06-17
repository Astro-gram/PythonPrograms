def Add(a, b):
    return a + b

def Sub(a, b):
    answer = a - b
    error = "error"
    if answer < 0:
        return error
    else:
        return answer
def Multi(a, b):
    return a * b

def Div(a, b):
    return a / b

print("Calculator\n")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. division")
print("\nChoice: ", end="");
choice = int(input());

if choice == 1:
    print("\na = ", end="");
    a = int(input())
    
    print("\nb = ", end="");
    b = int(input())
    
    answer = Add(a, b);
    print("\nAnswer: " + str(answer))
    
if choice == 2:
    print("\na = ", end="");
    a = int(input())
    
    print("\nb = ", end="");
    b = int(input())
    
    answer = Sub(a, b);

    if (answer == "error"):
        print("\n\nError - below 0")
    else:
        print("\nAnswer: " + str(answer))

if choice == 3:
    print("\na = ", end="");
    a = int(input())
    
    print("\nb = ", end="");
    b = int(input())
    
    answer = Multi(a, b);
    print("\nAnswer: " + str(answer))

if choice == 4:
    print("\na = ", end="");
    a = int(input())
    
    print("\nb = ", end="");
    b = int(input())
    
    answer = Div(a, b);
    print("\nAnswer: " + str(answer))
if choice > 4:
    print("Error")

input()        
