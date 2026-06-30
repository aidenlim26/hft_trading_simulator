from hft_trading_simulator.models import Order

import dataclasses 
from typing import Literal

@dataclasses.dataclass
class Order:
    order_id: str
    bot_id: str
    symbol: str
    side: Literal["BUY", "SELL"]
    price: float
    quantity: int



class BaseBot:
    # Master Class, other bots will inherit this
    def __init__(self, bot_id:str, initial_cash:float):
        self.bot_id = bot_id
        self.cash = initial_cash
        self.portfolio = {}             # Tracking stock inventory
        self.order_counter = 0          # Increments to give each submitted ticket a unique ID

    def generate_order_id(self) -> str:
        # Gives unique order ID's as a str
        self.order_counter += 1
        return f"{self.bot_id}_{self.order_counter:04d}"        # :04d means exactly 4 digits long
    
    def submit_order(self, symbol:str, side:str, price:float, quantity:int) -> Order:       # Returns in the format of the class "Order"
        return Order(
            order_id = self.generate_order_id(),
            bot_id = self.bot_id,
            symbol = symbol,
            side = side,
            price = round(price,2),
            quantity = quantity
        )
    
    def on_market_update(self, symbol:str, new_price:float):        # Temporary placeholder, for future inheritance to use
        pass


class MomentumBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.price_history = {}     # This dictionary is unique to MomentumBot, will store recent prices

    def on_market_update(self, symbol, new_price):
        # Everytime price changes in the market, this program is run
        
        # If it's a new stock, initilise an empty list
        if symbol not in self.price_history:
            self.price_history[symbol] = []

        history = self.price_history[symbol]            # Creates localised variable for the price history list
        history.append(new_price)                       # Adds new price


        # Keeping only the 3 most recent prices to check it's directional vectors
        if len(history) > 3:
            history.pop(0)

        # If theres 3 consecutive prices, check if they are going up
        if len(history) == 3:
            p1 = history[0]     # Oldest price
            p2 = history[1]
            p3 = history[2]     # Newest price

            if p3 > p2 > p1:    # Price increase twice in a row
                print(f"[STRATEGY MATCH] {self.bot_id} detected upward trend for {symbol}: {p1} -> {p2} -> {p3}")
                return self.submit_order(symbol, "BUY", new_price, quantity=10)

        return None     # If price didn't go up twice in a row
    

class MeanReversionBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.price_history = {}

    def on_market_update(self, symbol, new_price):
        if symbol not in self.price_history:
            self.price_history[symbol] = []

        history = self.price_history[symbol]
        history.append(new_price)

        if len(history) > 5:        # 5 values to find a reliable average
            history.pop(0)
            
        if len(history) == 5:
            moving_average = sum(history) / len(history)
            threshold = moving_average * 0.03               

            # If price is overvalued -> SELL
            if new_price > (moving_average + threshold):
                # Check that trader owns shares that they can sell
                if self.portfolio.get(symbol,-1) >= 10:
                    print(f"[STRATEGY MATCH] {self.bot_id} thinks {symbol} is OVERVALUED (${new_price:.2f} vs Avg: ${moving_average:.2f})")
                    return self.submit_order(symbol, "SELL", new_price, quantity=10)
                
            # If price is undervalued -> BUY
            elif new_price < (moving_average - threshold):
                print(f"🛒 [STRATEGY MATCH] {self.bot_id} thinks {symbol} is UNDERVALUED (${new_price:.2f} vs Avg: ${moving_average:.2f})")
                return self.submit_order(symbol, "BUY", new_price, quantity=10)
            
        return None





    

        