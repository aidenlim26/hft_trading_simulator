import time

class Order:
    def __init__(self, order_id:str, trader_id:str, symbol:str, side:str, price:float, quantity:int):
        self.order_id = order_id
        self.trader_id = trader_id
        self.symbol = symbol.upper()
        self.side = side.upper()
        self.price = float(price)
        self.quantity = int(quantity)
        self.timestamp = time.time()
    
    def __repr__(self):     # repr stands for represent
        # This is to tell the program how to display outputs
        return f"[Order {self.order_id}] {self.trader_id} -> {self.side} {self.quantity}x {self.symbol} @ ${self.price:.2f}"
    

class Trader:
    def __init__(self, trader_id:str, initial_balance:float):
        self.trader_id = trader_id
        self.balance = float(initial_balance)
        self.portfolio = {}

    def can_buy(self, price:float, quantity:int) -> bool:       # Tryna see if buyer has enough cash in account
        total_cost = price * quantity
        return self.balance >= total_cost
    
    def can_sell(self, symbol:str, quantity:int) -> bool:
        symbol = symbol.upper()

        # Check if the stock is in the user's portfolio dictionary + if they have enough shares
        if symbol in self.portfolio and (self.portfolio[symbol] >= quantity):
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        return f"[Trader {self.trader_id}] Balance: ${self.balance:.2f} | Portfolio: {self.portfolio}"  # ":.2f means 2 decimal places"
    


