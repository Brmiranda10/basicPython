birthdays = {
    "Bruno": "Jan 23",
    "Vinicius": "Mar 21",
    "Leonardo": "Out 27",
    "Luiz": "Sep 20",
    "William": "Apr 27",
    "Daniel": "Ago 18",
    "Vitor": "Dez 16",
}

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "":
        break

    if name in birthdays:
        print(birthdays[name] + " is birthday of " + name)
    else:
        print("I do not have birthday date for " + name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.")
