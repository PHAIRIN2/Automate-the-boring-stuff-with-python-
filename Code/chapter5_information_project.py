# get information
allGuests = {
    "Alice": {"apples": 2, "pretzels": 2},
    "Bob": {"apples": 4, "water": 3},
    "JJ": {"pretzels": 2, "apple pies": 5},
}


def totalBrought(guests, item):
    numberBrought = 0
    for k, v in guests.items():
        numberBrought = numberBrought + v.get(item, 0)
    return numberBrought


print("number of things being brought:")
print(" - Apples ", str(totalBrought(allGuests, "apples")))
print(" - Pretzels ", str(totalBrought(allGuests, "pretzels")))
print(" - Apple pies ", str(totalBrought(allGuests, "apple pies")))
print(" - Water ", str(totalBrought(allGuests, "water")))
