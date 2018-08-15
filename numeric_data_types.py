# division in python - the result will always be a float (even when the two values going in are integers)

# how to get the floor of a number (not decimals)?

def floor_division(x, y):
    print(x // y)

floor_division(17, 3)


# ___
bill = 15.25
tax = 7.25
total = bill + (tax/100)*bill
print(total)
