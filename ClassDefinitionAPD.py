class FoodItem:
    def __init__(self, name, amount):
        self.__name = name
        self.__amount = amount
        self.__ppp = 0
        self.__priceTotal = 0
        self.__PriceListAPD()

    def getPriceTotal(self):
        return self.__priceTotal

    def __PriceListAPD(self):
        if self.__name == "Dry Cured Iberian Ham":
            self.__ppp = 177.80
        elif self.__name == "Wagyu Steaks":
            self.__ppp = 450.00
        elif self.__name == "Matsutake Mushrooms":
            self.__ppp = 272.00
        elif self.__name == "Kopi Luwak Coffee":
            self.__ppp = 306.50
        elif self.__name == "Moose Cheese":
            self.__ppp = 487.20
        elif self.__name == "White Truffles":
            self.__ppp = 3600.00
        elif self.__name == "Blue Fin Tuna":
            self.__ppp = 3603.00
        elif self.__name == "Le Bonnotte Potatoes":
            self.__ppp = 270.81
        else:
            self.__ppp = 0.00

    def priceTotalAPD(self):
        self.__priceTotal = self.__amount * self.__ppp

        return self.__priceTotal

    def __str__(self):
        return f'The price of {self.__amount} lb of {self.__name} is ${self.priceTotalAPD()}'


f1 = FoodItem("Moose Cheese", 2)

print(f1.__str__())
