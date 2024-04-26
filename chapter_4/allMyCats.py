catNames = []


def showCatNames():
    global catNames
    while True:
        print(
            "Enter the name of cat "
            + str(len(catNames) + 1)
            + "(Or enter nothing to stop.):"
        )
        name = input()
        if name == "":
            break
        catNames.append(name)
        ##catNames = catNames + [name]
    return catNames


for name in showCatNames():
    print("The cat names are: " + name)
