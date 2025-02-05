# Checking whether the user has input a positive integer between 1 and 8
while True:
    try:
        x = int(input("Height: "))
        if x >= 1 and x <= 8:
            break
    except ValueError:
        print('Please input a number between 1 & 8...')

# Function to create a pyramid
s = 1
for j in range(x):
    # prints spaces
    for s in range(x-j-1):
        print(" ", end="")

    # prints hashes
    for i in range(j+1):
        print("#", end="")
    print()
