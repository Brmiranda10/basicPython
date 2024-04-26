def listMarket():
    market_list = []
    while True:
        item = input('Enter an item (or type "done" to finish): ')
        if item.lower() == "done":
            break
        market_list.append(item)
    return market_list


market_items = listMarket()

print("The market list contains: ")
for item in market_items:
    print(item)
