def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    # edge cases
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    
    output = []
    while lst1 and lst2:
        if lst1[0] <= lst2[0]:
            output.append(lst1[0])
            lst1 = lst1[1:]
        else:
            output.append(lst2[0])
            lst2 = lst2[1:]
    output += lst1 + lst2
    return output


class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2021
    >>> dime = mint.create(Dime)
    >>> dime.year
    2021
    >>> Mint.present_year = 2101  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Mint.present_year = 2176     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2021

    def __init__(self):
        self.update()
        
    def create(self, coin):
        return coin(self.year)

    def update(self):
        self.year = Mint.present_year


class Coin:
    cents = None  # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        if Mint.present_year - self.year > 50:
            return self.cents + Mint.present_year - self.year - 50
        else:
            return self.cents

class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.amount = 0
        self.balance = 0
    
    def vend(self):
        if self.amount == 0:
            return "Nothing left to vend. Please restock."
        if self.price > self. balance:
            return "You must add $" + str(self.price-self.balance) + ' more funds.'
        elif self.balance > self.price:
            change = self.balance - self.price
            self.balance = 0
            self.amount -= 1
            return "Here is your " + self.name + " and $" + str(change) + ' change.'
        elif self.balance == self.price:
            self.balance = 0
            self.amount -= 1
            return 'Here is your ' + self.name + '.'

    def add_funds(self, dollar):
        if self.amount == 0:
            return "Nothing left to vend. Please restock. Here is your $" + str(dollar) + '.'
        else:
            self.balance += dollar
            return "Current balance: $" + str(self.balance)

    def restock(self, amount):
        self.amount += amount
        return "Current " + self.name + ' stock: ' + str(self.amount)

