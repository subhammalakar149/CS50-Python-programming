from cs50 import get_float

# checking for the user's positive integer input
while True:
    try:
        input = get_float("Change : ")
        if input > 0:
            break
    except ValueError:
        print('Please input a non-negative value...')

coins = 0
change = input * 100 # rounding of value

# 25c coins
while change >= 25:
    change = change - 25
    coins = coins + 1

# 10c coins
while change >= 10:
    change = change - 10
    coins = coins + 1

# 5c coins
while change >= 5:
    change = change - 5
    coins = coins + 1

# 1c coins
while change >= 1:
    change = change - 1
    coins = coins + 1

print(coins)
