print("Sudoku\n\n")

for x in range(9):
    
    for y in range(9):
        
        print("1 ", end="")
        
        if y == 2:
            print(" | ", end="")
        if y == 5:
            print(" | ", end="")

    print("\n")
    if x == 2:
        print("-----------------------\n")
    if x == 5:
        print("-----------------------\n")


input()
