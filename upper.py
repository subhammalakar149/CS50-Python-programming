# converting a string to uppercase one at a time
"""
before = input ("Before: ")

print("After: ", end="") # end= continues the line without a line ending.

for c in before:
    print(c.upper(), end="")
print()
"""

# more simplified approach

before = input("Before: ")

after = before.upper()

print(f"After: {after}")
