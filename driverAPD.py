from ClassDefinitionAPD import FoodItem


def createListAPD():
    foodList = []
    while True:
        number_of_items = int(input("Enter the number of items: "))
        if number_of_items >= 1:
            break

    itemnum = 0
    for items in range(number_of_items):
        itemnum += 1
        print(f'Item #{itemnum}')

        name_of_items = input("Enter the name of the item: ").lower()
        while True:
            pound_of_item = eval(input("Enter the amount of the item in pounds: "))
            if pound_of_item >= 1:
                break
        foodList.append(FoodItem(name_of_items, pound_of_item))

    return foodList


def displayListAPD(list):
    for item in list:
        print('\n')
        print(f'Item: {item.getNameAPD()}')
        print(f'Amount Ordered: {item.getAmountAPD()}')
        print("Price of Order:", '${:,.2f}'.format(item.getPricePerPoundAPD()))
        print("Price of Order:", '${:,.2f}'.format(item.priceTotalAPD()))
        print('\n')


def totalCostAPD(list):
    total = []
    for item in list:
        total.append(item.priceTotalAPD())
    summ = '${:,.2f}'.format(sum(total))
    thing = f'Total cost: {summ}'

    return thing


def mainAPD():
    list = createListAPD()
    displayListAPD(list)
    return totalCostAPD(list)

print(mainAPD())




