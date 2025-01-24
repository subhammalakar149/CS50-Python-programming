# Addition with int [using input]

try:
    # Prompt user for x
    x = int(input("x: "))

    # Prompt user for y
    y = int(input("y: "))

    # Perform addition
    # print(x + y)

    z = (x/y)
    print(f"{z:.50f}") # revealing the imprecision
    
except ValueError: # handling exceptions
    print("Not an integer.")
