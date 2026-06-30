from hft_trading_simulator.models import Order, Trader    # Importing module 
from hft_trading_simulator.engine import OrderBook, MatchingEngine 

# TESTING PLACING ORDERS
#print("-" * 50) 
#print("Test Placing ORDERS")

# Test BUY Order 1
#test_order_1 = Order("001", "TRADER_A", "timl", "buy", 150.50, 10)

# Test SELL Order 2
#test_order_2 = Order("002", "TRADER_B", "TIML", "sell", 152.00, 5)

#print(test_order_1)
#print(test_order_2)
#print("-" * 50)


# TESTING TRADER CLASS
#print("Test Trader State & Validation")

# Initialise a trader with 15k cash
#trader_payton = Trader(trader_id="JPD", initial_balance="15000")
#print(f"Initial State: {trader_payton}")
#print("-" * 50)

# Test BUY Validation
#print(f"Can JPD afford $1,500 order? {trader_payton.can_buy(price=150.00, quantity=10)}")
#print(f"Can JPD afford $21,000 order? {trader_payton.can_buy(price=210.00, quantity=100)}")
#print("-" * 50)

# Test SELL Validation (MANUALLY INJECTED SHARES TO TEST)
#print(f"Can JPD sell 10x TIML now? {trader_payton.can_sell(symbol="TIML", quantity=10)}")   
#print(f"Can JPD sell 50x TIML now? {trader_payton.can_sell(symbol="TIML", quantity=50)}")   
#print("-" * 50)



# Test Order Book Sorting Depth
#print("--- Testing Milestone 3: Order Book Sorting Depth ---")
#timl_book = OrderBook(symbol="TIML")

# Add random buyer orders
#order_b1 = Order("1", "BOB", "TIML", "BUY", 148.50, 100)
#order_b2 = Order("2", "CHARLIE", "TIML", "BUY", 151.00, 50)
#order_b3 = Order("3", "DAVID", "TIML", "BUY", 149.00, 75)

# Add BUY orders to the book
#timl_book.add_order(order_b1)
#timl_book.add_order(order_b2)
#timl_book.add_order(order_b3)

# Add radom seller orders
#order_s1 = Order("4", "ELON", "TIML", "SELL", 155.00, 10)
#order_s2 = Order("5", "FRANK", "TIML", "SELL", 153.25, 20)

# 5. Add SELL orders to the book
#timl_book.add_order(order_s1)
#timl_book.add_order(order_s2)

# Test Market View + Sorting Logic
#timl_book.display_book()

#print("-" * 50)
#print("--- Testing Milestone 4: Order Matching & Partial Fills ---")

# 1. Initialize the book
#market = OrderBook(symbol="TIML")

# 2. Bob places an order to SELL 50 shares at $150.00
#print("\n>>> Bob adds a SELL order for 50 shares at $150.00")
#bob_sell = Order("101", "BOB", "TIML", "SELL", 150.00, 50)
#market.add_order(bob_sell)
#market.display_book()

# 3. Payton arrives and crosses the spread! 
# He wants to BUY 75 shares up to a price of $152.00.
# Since $152.00 >= $150.00, a match should happen instantly!
#print("\n>>> Payton adds a BUY order for 75 shares at $152.00")
#payton_buy = Order("102", "PAYTON", "TIML", "BUY", 152.00, 75)
#market.add_order(payton_buy)

# 4. Let's see the leftover state of the book
#market.display_book()

print("--- Testing Milestone 5: End-to-End Market Settlement ---")

nyse = MatchingEngine()

bob = Trader(trader_id="BOB", initial_balance=5000.00)
bob.portfolio["TIML"] = 100     # Injecting stocks

payton = Trader(trader_id="JPD", initial_balance=15000.00)
payton.portfolio["TIML"] = 500

nyse.register_trader(bob)
nyse.register_trader(payton)

print(f"[INITIAL STATUS]")
print(f"Bob: Cash: ${bob.balance:.2f}, Portfolio: {bob.portfolio}")
print(f"Payton: Cash: ${payton.balance:.2f}, Portfolio: {payton.portfolio}")

print("\n--- Testing Risk Management System ---")
fake_sell = Order("999", "BOB", "TIML", "SELL", 150.00, 500)        # Bob only has 100 shares
nyse.submit_order(fake_sell)

# 4. Bob places a legal rest order to sell 50 shares
order_1 = Order("001", "BOB", "TIML", "SELL", 150.00, 50)
nyse.submit_order(order_1)

# 5. Payton arrives and submits a matching cross buy order
order_2 = Order("002", "JPD", "TIML", "BUY", 155.00, 50)
nyse.submit_order(order_2)

print(f"\n--- Post-Trade Final Account Audit Balance Verification ---")
print(f"Bob --> Cash: ${bob.balance:.2f}, Portfolio: {bob.portfolio}")
print(f"Payton --> Cash: ${payton.balance:.2f}, Portfolio: {payton.portfolio}")


timl_book = nyse.get_or_create_book("TIML")
timl_book.display_book()
