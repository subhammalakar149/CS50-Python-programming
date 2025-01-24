# prints a command-line arguements

from sys import argv

if len(argv) ==2:
    print(f"Hello, {argv[1]}") # printed using a formatted string
else:
    print("Hello, World")
