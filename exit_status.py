# exits with explicit value, importing sys

from sys import exit,argv

if len(argv) != 2:
    print("Missing command-line arguement")
    exit(1)

print(f"Hello, {argv[1]}")
exit(0)
