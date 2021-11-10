from typing import List

GARLIC = 'Garlic'
PEPPERONI = 'Pepperoni'


class Ingredient:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} (${self.price})'

    def __repr__(self):
        return f'Ingredient({self.name}, ${self.price})'


class Item:
    def cost(self):
        raise NotImplementedError()


class Pizza(Item):
    BASE_PRICE: float = 50

    def __init__(self, base=None, ingredients: List[Ingredient] = None):
        self.base = base
        self._ingredients: List[Ingredient] = ingredients if ingredients else []

    def __str__(self):
        return f'${self.cost()}'

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        raise AssertionError('ingredients cannot be set.')

    def cost(self):
        return self.BASE_PRICE


class WithGarlic(Pizza):
    GARLIC_BASE_PRICE: float = 10

    def __init__(self, base: Pizza):
        ingredients = base.ingredients + [Ingredient(GARLIC, self.GARLIC_BASE_PRICE)]  # AM I ANTI-PATTERN OR NOT
        super().__init__(base, ingredients)

    def cost(self):
        return self.base.cost() + self.GARLIC_BASE_PRICE


class WithPepperonis(Pizza):
    PEPPERONI_BASE_PRICE: float = 20

    def __init__(self, base: Pizza):
        ingredients = base.ingredients + [Ingredient(PEPPERONI, self.PEPPERONI_BASE_PRICE)]
        super().__init__(base, ingredients)

    def cost(self):
        return self.base.cost() + self.PEPPERONI_BASE_PRICE


class Offer:
    def __init__(self, offer_func):
        self._check_availability = offer_func

    def can_avail(self, pizza: Pizza):
        return self._check_availability(pizza)

    def apply(self, pizza: Pizza):
        # NOT IMPLEMENTED <-> FIX FAULTY DESIGN
        if self.can_avail(pizza):
            pass


class Order:
    def __init__(self, items: List[Item]):
        self.items = items if items else []

    def add_item(self, item: Item):
        self.items.append(item)

    def total_cost(self):
        # CACHE ME
        return sum(item.cost() for item in self.items)


def two_garlic_offer_checker(pizza: Pizza):  # AM I ANTI-PATTERN
    count = 0
    for ingredient in pizza.ingredients:
        if ingredient.name == GARLIC:
            count += 1
    return count >= 2


if __name__ == '__main__':
    pizza1 = WithPepperonis(WithGarlic(Pizza()))   # 50 + 10 + 20
    pizza2 = WithPepperonis(WithPepperonis(WithGarlic(Pizza())))   # 50 + 10 + 20 + 20
    pizza3 = WithPepperonis(WithPepperonis(WithGarlic(Pizza())))
    pizza4 = WithGarlic(WithGarlic(Pizza()))

    offer = Offer(two_garlic_offer_checker)

    print(pizza1)
    print(pizza2)
    print(pizza3.ingredients)
    print(offer.can_avail(pizza3))
    print(offer.can_avail(pizza4))
