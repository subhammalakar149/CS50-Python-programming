"""
# printing column of bricks with a loop

while True:
    x = int(input("Height: "))
    if x > 0:
        break
for i in range(x):
    print("#")
"""
"""
# differment way to print bricks
def main():
    try:
        x = int(input("Height: "))
        mario(x)
    except ValueError:
        print("Please input integers only.")

def mario(n):
    for i in range(n):
        print("#")

main()
"""

# printing a 3-by-3 grid of bricks with loops
x = int(input("Grid of bricks: "))

for i in range(x):
    for j in range(x):
        print ("#", end="")
    print()
