from helpers import is_negative

class Candy_Machine:
    
    def program():
        """  """
    def sell_product():
        """  """
    def show_product():
        """  """


class Cash_Register:

    def __init__(self, cash_on_hand=500):
        self.cash_on_hand = cash_on_hand

    def __str__(self) -> str:
        return f"Cash on hand is ${self.cash_on_hand:,.2f}"

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

    def cash_register(self, cash_in):
        """ """

    def current_balance(self):
        """shows the current amount in the cash register"""
        return self.cash_on_hand

    def accept_amount(self, amount_in):
        """accepts the amount entered by the customer"""
        if isinstance(amount_in, int) and amount_in > 0:
            self.cash_on_hand += amount_in
        
        else:
            raise TypeError("Amount In must be non negative integer")


class Dispenser:
    def __init__(self, cost, number_of_items):
        """  """

    def dispenser(self, set_no_of_items, set_cost):
        """  """

    def get_count(self):
        """  """

    def get_product_cost(self):
        """  """

    def makeSale(self):
        """  """


a = Cash_Register(1000)
a.accept_amount(3)
a.accept_amount(5)
print(a.current_balance())