from helpers import is_negative, deposit_more
import sys

class Candy_Machine:
    
    def __init__(self):
        self.cash_register = Cash_Register()
        self.candy_dispenser = Dispenser()
        self.chip_dispenser = Dispenser()
        self.gum_dispenser = Dispenser()
        self.cookie_dispenser = Dispenser()

    def __str__(self):
        return f"CHOICE: {self.choice}"
        
    def program(self):
        """  """
    # TODO


    def sell_product(self):
        """ sell the products selected by the customer """
        print(self.choice.number_of_items)
        if self.choice.number_of_items <= 0:
            print("\nThe product is out of stock.")
            return self.show_selection()

        deposit = 0
        while deposit < self.choice.cost:
            try:
                new_deposit = deposit_more(self.choice.cost - deposit)
                if new_deposit == "q":
                    return self.show_selection()
                
                deposit += int(new_deposit)
            except KeyboardInterrupt:
                sys.exit()
            except:
                print("Must deposit using positive integers. (Q - to cancel purchase)")
        
        # TODO SELL PRODUCT

        # TODO ACCEPT MONEY, RETURN IF THEIR IS CHANGE









    def show_selection(self):
        """ displays the main menu, allow users to select and buy a product """
        item_key = {"1": self.candy_dispenser, "2": self.chip_dispenser, "3": self.gum_dispenser, "4": self.cookie_dispenser, "Q": "exit"}

        print("\nWelcome to \nMy Candy Machine")
        print("\nSelect an item to purchase by entering its value")
        print("1 - Candy \n2 - Chip \n3 - Gum \n4 - Cookie \nQ - Exit")
        choice = input("\nYour choice:  ")[0].upper() 

        if not choice or choice not in item_key:
            return self.show_selection()

        if choice == "exit":
            sys.exit("\n'My Candy Machine' is turning off")

        else:
            self.choice = item_key[choice]
            return self.sell_product()

    


        


class Cash_Register():

    def __init__(self, cash_on_hand=500):
        self.cash_on_hand = cash_on_hand

    # Getter
    @property
    def cash_on_hand(self):
        return self._cash_on_hand

    # Setter
    @cash_on_hand.setter
    def cash_on_hand(self, cash_on_hand):
        if isinstance(cash_on_hand, int):
            if cash_on_hand < 0:
                self._cash_on_hand = 500
            else:
                self._cash_on_hand = cash_on_hand
        else:
            raise TypeError("Cash on Hand must be an integer")

    def __str__(self):
        return f"Cash on hand is ${self.cash_on_hand:,.2f}"

    def cash_register(self, cash_in):
        """ """
        # TODO

    def current_balance(self):
        """ shows the current amount in the cash register """
        return self.cash_on_hand

    def accept_amount(self, amount_in):
        """ accepts the amount entered by the customer """
        if isinstance(amount_in, int) and amount_in > 0:
            self.cash_on_hand += amount_in
        
        else:
            raise TypeError("Amount In must be non negative integer")


class Dispenser:
    def __init__(self, cost=50, number_of_items=50):
        self.cost = cost
        self.number_of_items = number_of_items

    # Getter
    @property
    def cost(self):
        return self._cost

    # Setter
    @cost.setter
    def cost(self, cost):
        if isinstance(cost, int):
            if cost < 0:
                self._cost = 50 
            
            else:
                self._cost = cost 
        else:
            raise TypeError("Cost must be an integer")

    # Getter
    @property
    def number_of_items(self):
        return self._number_of_items

    # Setter
    @number_of_items.setter
    def number_of_items(self, number_of_items):
        if isinstance(number_of_items, int):
            if number_of_items < 0:
                self._number_of_items = 50 
            
            else:
                self._number_of_items = number_of_items 
        else:
            raise TypeError("Number of Items must be an integer")

    def __str__(self):
        return f"Cost is ${self.cost:,.2f} and Number of Items is {self.number_of_items}"

    def dispenser(self, set_no_of_items, set_cost):
        """  """
        # TODO

    def get_count(self):
        """ returns the number of items of a particular product """
        return self.number_of_items

    def get_product_cost(self):
        """ returns the cost of a product """
        return self.cost

    def makeSale(self):
        """ Product sold, reduce number of items by 1 """
        self.number_of_items -= 1



""" TESTINGS """
# a = Cash_Register(1000)
# a.accept_amount(3)
# a.accept_amount(5)
# print(a)

# b = Dispenser(3, 5)
# b.makeSale()
# print(b.get_count())

c = Candy_Machine()

c.candy_dispenser.number_of_items = 0
c.show_selection()
# print(c)
# print(c.cash_register)