from ClassDefinitionAPD import FoodItem


def createListAPD():
    foodList = list()
    while True:
        number_of_items = int(input("Enter the number of items: "))
        if number_of_items >= 1:
            break

    itemnum = 0
    for items in range(number_of_items):
        itemnum += 1
        print(f'Item #{itemnum}')

        name_of_items = input("Enter the name of the item: ")
        while True:
            pound_of_item = eval(input("Enter the amount of the item in pounds: "))
            if pound_of_item >= 1:
                break
        foodList.append(FoodItem(name_of_items, pound_of_item))

    return foodList


print(createListAPD())