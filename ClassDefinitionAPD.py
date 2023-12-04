class FoodItemAPD:
    def __init__(self, name, amount):
        self.__name = name
        self.__amount = amount
        self.__ppp = 0
        self.__priceTotal = 0
        self.__PriceListAPD()

    def getNameAPD(self):
        return self.__name

    def getAmountAPD(self):
        return self.__amount

    def getPricePerPoundAPD(self):
        return self.__ppp

    def __PriceListAPD(self):
        if self.__name == "dry cured iberian ham":
            self.__ppp = 177.80
        elif self.__name == "wagyu steaks":
            self.__ppp = 450.00
        elif self.__name == "matsutake mushrooms":
            self.__ppp = 272.00
        elif self.__name == "kopi luwak coffee":
            self.__ppp = 306.50
        elif self.__name == "moose cheese":
            self.__ppp = 487.20
        elif self.__name == "white truffles":
            self.__ppp = 3600.00
        elif self.__name == "blue fin tuna":
            self.__ppp = 3603.00
        elif self.__name == "le bonnotte potatoes":
            self.__ppp = 270.81
        else:
            self.__ppp = 0.00

    def priceTotalAPD(self):
        self.__priceTotal = self.__amount * self.__ppp

        return self.__priceTotal

    def __str__(self):
        return f'The price of {self.__amount} lb of {self.__name} is ${self.priceTotalAPD()}'



