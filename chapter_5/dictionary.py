allGuests = {
    "Alice": {"apples": 5, "pretzels": 10},
    "Bruno": {"ham sandwiches": 8, "apples": 3},
    "Carol": {"cups": 8, "apple pies": 1},
}


def totalBrought(guests, item):
    numBrought = 0
    for (
        k,
        v,
    ) in (
        guests.items()
    ):  # string with the guest name is assigned to k and the items dictionary is assigned to v
        numBrought = numBrought + v.get(item, 0)
    return numBrought


print("Number of things being brought:")
print(" - Apples     " + str(totalBrought(allGuests, "apples")))
print(" - Cups     " + str(totalBrought(allGuests, "cups")))
print(" - Cakes     " + str(totalBrought(allGuests, "cakes")))
print(" - Ham sandwiches     " + str(totalBrought(allGuests, "ham sandwiches")))
print(" - Apple pies     " + str(totalBrought(allGuests, "apple pies")))
