# abstraction
"""
def main():
    for i in range(3):
        meow() # function meow() is called here

# meow once
def meow():
    print("meow")

main() # main function is called
"""

# abstraction with parameterization

def main():
    x = int(input("No. of times : "))
    meow(x)

# meow some number of times
def meow(n):
    for i in range(n):
        print("meow")

main()
