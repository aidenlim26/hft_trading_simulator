from hft_trading_simulator.models import Order

class OrderBook:
    def __init__(self, symbol:str):
        self.symbol = symbol.upper()
        self.buy_orders = []            # Active BUY orders
        self.sell_orders = []           # Active SELL orders
        
    def add_order(self, order: Order, traders_db: dict):      # Assigns the class "Order" to a local variable "order"
        # Appends an order to the correct list + sorts it
        if order.side == "BUY":
            self.buy_orders.append(order)
            self._sort_buy_orders()
        elif order.side == "SELL":
            self.sell_orders.append(order)
            self._sort_sell_orders()

        self.match_orders(traders_db)                 # Makes trades happen (or not, if doesn't match)
    
    def _sort_buy_orders(self):
        # Sorts BUY orders in descending order
        n = len(self.buy_orders)
        
        # Swap if current order price is LESS than next order price
        # Bubble sort

        for i in range(n):
            for j in range(0, n-i-1):
                if self.buy_orders[j].price < self.buy_orders[j+1].price:
                    self.buy_orders[j], self.buy_orders[j+1] = self.buy_orders[j+1], self.buy_orders[j]

                    
    def _sort_sell_orders(self):
        # Sorts SELL orders in ascending order
        n = len(self.sell_orders)
        
        # Swap if current order price is GREATER than next order price
        # Bubble sort

        for i in range(n):
            for j in range(0, n-i-1):
                if self.sell_orders[j].price > self.sell_orders[j+1].price:
                    self.sell_orders[j], self.sell_orders[j+1] = self.sell_orders[j+1], self.sell_orders[j]

    
    def display_book(self):
        print(f"ORDER BOOK: {self.symbol}")
        print(f"--- ASKS (SELL ORDERS) - Lowest Price First ---")
        for order in reversed(self.sell_orders):                        # "order" is just a variable name, can be "i" as well
            print(f"{order.price:.2f} x {order.quantity} shares ({order.trader_id})")
        
        print(f"------------------ CURRENT SPREAD ------------------")

        print("--- BIDS (BUY ORDERS) - Highest Price First ---")
        for order in self.buy_orders:     
            print(f"{order.price:.2f} x {order.quantity} shares ({order.trader_id})")

    def match_orders(self, traders_db: dict):     # Orders only go through when the buyer's maximum price > seller minimum price
        # While there is at least one buyer and seller
        while self.buy_orders and self.sell_orders:
            highest_bid = self.buy_orders[0]
            lowest_ask = self.sell_orders[0]

            if highest_bid.price >= lowest_ask.price:
                match_price = lowest_ask.price
                match_quantity = min(highest_bid.quantity, lowest_ask.quantity)     # Potentially a partial fill
                
                buyer = traders_db[highest_bid.trader_id]
                seller = traders_db[lowest_ask.trader_id]
                cash_transfer = match_price * match_quantity

                #SYNC BALANCE
                buyer.balance -= cash_transfer
                seller.balance += cash_transfer

                # SYNC PORTFOLIOS
                buyer.portfolio[self.symbol] = buyer.portfolio.get(self.symbol, -1) + match_quantity
                seller.portfolio[self.symbol] = seller.portfolio.get(self.symbol, -1) - match_quantity

                print(f"[MATCH TRADED] {match_quantity} shares of {self.symbol} crossed at ${match_price:.2f}")
                print(f"Buyer: {highest_bid.trader_id} <---> Seller: {lowest_ask.trader_id}")

                # Deduct filled quantity from both order objects 
                highest_bid.quantity -= match_quantity      # highest_bid refers to amount that the trader still wants to buy
                lowest_ask.quantity -= match_quantity       # lowest_ask refers to amount that trader still wants to sell

                if highest_bid.quantity == 0:
                    self.buy_orders.pop(0)  # Pop index 0
                if lowest_ask.quantity == 0:
                    self.sell_orders.pop(0)

            else:
                break



class MatchingEngine:
    def __init__(self):
        self.traders = {}
        self.books = {}
    
    def register_trader(self,trader):
        self.traders[trader.trader_id] = trader

    def get_or_create_book(self, symbol:str) -> OrderBook:
        symbol_upper = symbol.upper()
        if symbol_upper not in self.books:
            self.books[symbol_upper] = OrderBook(symbol_upper)
        return self.books[symbol_upper]
    
    def submit_order(self, order:Order):
        if order.trader_id not in self.traders:
            print(f"[REJECTED] Trader {order.trader_id} is not registered.")    
            return 
        
        trader = self.traders[order.trader_id]

        if order.side == "BUY":
            total_cost = order.price * order.quantity
            if trader.balance < total_cost:
                print(f"[REJECTED] {order.trader_id} has insufficient funds!")
                return
        
        elif order.side == "SELL":
            current_shares = trader.portfolio.get(order.symbol, -1)
            if current_shares < order.quantity:
                print(f"[REJECTED] {order.trader_id} has insufficient shares! Wants to sell: {order.quantity}, Owns {current_shares}")
                return
        
        book = self.get_or_create_book(order.symbol)
        
        print(f">>> Order Accepted: {order.trader_id} places {order.side} for {order.quantity} {order.symbol} @ ${order.price:.2f}")

        book.add_order(order, self.traders)   # Gives the order + self.traders so that the program can update the trader's balances
        
            