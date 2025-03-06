import pytest


class Checkout:
    class Discount:
        def __init__(self, numofItems, price):
            self.numofItems = numofItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Item not found")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, count in self.items.items():
            total += self.calculateItemTotal(item, count)

        return total

    def calculateItemTotal(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.numofItems:
                total += self.calculateItemDiscountedTotal(item, count, discount)
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count

        return total

    def addDiscount(self, item, numofItems, price):
        discount = self.Discount(numofItems, price)
        self.discounts[item] = discount

    def calculateItemDiscountedTotal(self, item, count, discount):
        total = 0
        nbrofdisc = count / discount.numofItems
        total += nbrofdisc * discount.price
        remaining = count % discount.numofItems
        total += remaining * self.prices[item]
        return total

