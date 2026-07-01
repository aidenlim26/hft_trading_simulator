import asyncio
import random

from models import Order
from engine import MatchingEngine
from providers import YahooFinanceProvider, LocalFallbackProvider
from tabulate import tabulate

from strategies import (
    MomentumBot, MeanReversionBot, BollingerBandsBot, DonchianChannelBot,
    ATRTrailingStopBot, RSICloseBot, MACDSignalBot, EMACrossoverBot,
    StochasticOscillatorBot, VWAPReversionBot, AccumulationDistributionBot,
    RSIBollingerComboBot, SupportResistanceBot, TimeInforceScalperBot, GridTraderBot
)

SYMBOL = "AAPL"
class RealTimeRiskDesk:
    def __init__(self, data_provider):
        self.bots = {}
        self.market_prices = {"AAPL" : 150.00}
        self.provider = data_provider

        self.order_books = {"AAPL": {"BUY": [], "SELL": []}}

        self.is_running = True
        self.start_time = None

    def register_bot(self, bot):
        self.bots[bot.bot_id] = bot
        print(f"🔌[SYSTEM] {bot.bot_id} has connected to the Risk Desk. Cash: ${bot.cash:.2f}")


    async def simulate_market_feed(self):
        print("📡[MARKET] Live data stream initialized...")
        self.start_time = asyncio.get_event_loop().time()

        historical_prices = self.provider.fetch_historical_prices()

        if not historical_prices:
            print(f"⚠️ [ERROR] Provider returned zero records. Terminating.")
            return
        
        tick_index = 0
        total_ticks = len(historical_prices)

        try:
            while self.is_running and tick_index < total_ticks:
                await asyncio.sleep(0.4)    # Pause program for 0.05 seconds to simulate market trade timings

                symbol = "AAPL"

                self.order_books[symbol]["BUY"] = []
                self.order_books[symbol]["SELL"] = []

                historical_price = historical_prices[tick_index]

                self.market_prices[symbol] = round((historical_price * 0.95) + (self.market_prices[symbol] * 0.2), 2)      # 80% real pricing vectors, 20% live matching price swings
                live_price = self.market_prices[symbol]

                print(f"📊 [TICK] {symbol} Historical: ${historical_price:.2f} -> Live Blended: ${self.market_prices[symbol]:.2f}")

                # Midpoint mapping
                best_bid = self.get_best_bid(symbol)
                best_ask = self.get_best_ask(symbol)
                
                target_price = self.market_prices[symbol]
                if best_bid and best_ask:
                    target_price = (best_bid + best_ask) / 2
                elif best_bid:
                    target_price = best_bid
                elif best_ask:
                    target_price = best_ask

                for bot_id, bot in self.bots.items():
                    generated_order = bot.on_market_update(SYMBOL, target_price)
                    if generated_order:
                        self.risk_manager(generated_order)

                tick_index += 1

        except asyncio.CancelledError:
            pass

    
    def risk_manager(self, order: Order):      # All inputs must conform with the class "Order"'s format
        print(f"🛑[RISK MANAGER] Intercepted ticket {order.order_id} from {order.bot_id}")

        bot = self.bots[order.bot_id]

        # Pre-trade risk constraints
        if order.side == "BUY":
            total_cost = order.price * order.quantity

            # Check Capital Suffiency
            if bot.cash < total_cost:
                print(f"❌[ORDER REJECTED] {bot.bot_id} has insufficient funds! Cost: ${total_cost:.2f}, Cash: ${bot.cash:.2f}")
                return
            
            # Position Sizing Maxmimum Risk Limit - Prevent single trade from staking more than 30% of trader's capital
            if total_cost > (bot.cash * 0.8):
                print(f"❌[ORDER REJECTED] {bot.bot_id} violated Position Sizing Rule! Single trade cost exceeds 80% threshold.")
                return
            
            #bot.cash -= total_cost

            #current_shares = bot.portfolio.get(order.symbol, 0.0)
            #old_avg = bot.entry_prices.get(order.symbol, 0.0)
            #new_avg = ((old_avg * current_shares) + (order.price * order.quantity)) / (current_shares + order.quantity)
            #bot.entry_prices[order.symbol] = round(new_avg, 2)      # Replaces the value in the directory of "old_avg"

            #bot.portfolio[order.symbol] = bot.portfolio.get(order.symbol, 0) + order.quantity       # It's dictionary so they use the key to find and add up the new value
            #print(f"✅[ORDER SETTLED] {bot.bot_id} bought {order.quantity} shares of {order.symbol} @ ${order.price:.2f} ")
            #print(f"Updated Portfolio --> Balance: ${bot.cash:.2f} | Inventory: {bot.portfolio}")

        
        elif order.side == "SELL":
            # Inventory Stocks Sufficiency Check
            current_shares = bot.portfolio.get(order.symbol, 0)
            if current_shares < order.quantity:
                print(f"❌[ORDER REJECTED] {bot.bot_id} has insufficient inventory! Wants to sell {order.quantity}, holds {current_shares}")
                return
            
            #total_credit = order.price * order.quantity
            #bot.cash += total_credit
            #bot.portfolio[order.symbol] -= order.quantity

            #if bot.portfolio[order.symbol] == 0:
                #del bot.entry_prices[order.symbol]          # Remove past data to prevent stale limits

            #print(f"✅[ORDER SETTLED] {bot.bot_id} sold {order.quantity} shares of {order.symbol} @ ${order.price:.2f}")
            #print(f"💼[PORTFOLIO UPDATE] --> Balance: ${bot.cash:.2f} | Inventory: {bot.portfolio}")

        # MATCHING ENGINE
        symbol = order.symbol
        opposing_side = "SELL" if order.side == "BUY" else "BUY"

        # Sorting the books - BUY is descending, SELL is ascending
        if opposing_side == "SELL":
            self.order_books[symbol][opposing_side].sort(key=lambda x: x.price)
            
        else:
            self.order_books[symbol][opposing_side].sort(key=lambda x: x.price, reverse=True)

        matched_orders_to_remove = []

        for open_order in self.order_books[symbol][opposing_side]:
            if order.quantity <=0:
                break
                
            is_match = False
            if order.side == "BUY" and order.price >= open_order.price:
                is_match = True
            elif order.side == "SELL" and order.price <= open_order.price:
                is_match = True

            if is_match:
                execution_price = open_order.price
                execution_qty = min(order.quantity, open_order.quantity)

                buyer_bot = bot if order.side == "BUY" else self.bots[open_order.bot_id]
                seller_bot = self.bots[open_order.bot_id] if order.side == "BUY" else bot

                # peer-peer settlement
                self._execute_p2p_settlement(buyer_bot, seller_bot, symbol, execution_price, execution_qty)

                order.quantity -= execution_qty
                open_order.quantity -= execution_qty

                if open_order.quantity == 0:
                    matched_orders_to_remove.append(open_order)
            
        for filled_order in matched_orders_to_remove:
            self.order_books[symbol][opposing_side].remove(filled_order)
                
            
        # IF WITHIN FIRST 3 SECONDS OF SIMULATION, AN ORDER CANNOT FIND A BOT MATCH, MARKET MAKER SEEDS THE INVENTORY
        # SO THAT BOTS CAN BUILD A PORTFOLIO
        elapsed_time = asyncio.get_event_loop().time() - self.start_time if self.start_time else 0

        if order.quantity > 0 and elapsed_time < 3.0:
            print(f"🌱[SEED LIQUIDITY] Exchange matched remaining {order.quantity} shares of {order.symbol} for {order.bot_id} @ ${order.price:.2f}")

            if order.side == "BUY":
                bot.cash -= order.price * order.quantity
                bot.portfolio[symbol] = bot.portfolio.get(symbol, 0) + order.quantity
                bot.entry_prices[symbol] = order.price
                
            elif order.side == "SELL":
                bot.cash += order.price * order.quantity
                bot.portfolio[symbol] -= order.quantity
                
            order.quantity = 0

        # If order still partially fulfilled within first 3s, leave it in the book
        if order.quantity > 0:
            self.order_books[symbol][order.side].append(order)
            print(f"⏳[BOOKED] Volume ({order.quantity} shares) resting in {symbol} {order.side} queue.")
                 
            
    def _execute_p2p_settlement(self, buyer, seller, symbol, price, qty):
        total_value = price * qty
        fee = 0.05 * qty

        # Settle buyer
        buyer.cash -= total_value
        current_buyer_shares = buyer.portfolio.get(symbol, 0.0)
        old_buyer_avg = buyer.entry_prices.get(symbol, 0.0)

        new_buyer_avg = ((old_buyer_avg * current_buyer_shares) + total_value) / (current_buyer_shares + qty)
        buyer.entry_prices[symbol] = round(new_buyer_avg, 2)
        buyer.portfolio[symbol] = current_buyer_shares + qty

        # Settle seller
        seller.cash += (total_value - fee)
        seller.portfolio[symbol] -= qty

        if seller.portfolio[symbol] == 0:
            if symbol in seller.entry_prices:
                del seller.entry_prices[symbol]

    def get_best_bid(self, symbol):
        """Returns the highest price a buyer is currently offering in the book."""
        buys = self.order_books[symbol]["BUY"]
        return max([order.price for order in buys]) if buys else None

    def get_best_ask(self, symbol):
        """Returns the lowest price a seller is currently demanding in the book."""
        sells = self.order_books[symbol]["SELL"]
        return min([order.price for order in sells]) if sells else None

    
    def _update_market_price_from_spread(self, symbol):
        buys = self.order_books[symbol]["BUY"]
        sells = self.order_books[symbol]["SELL"]

        # Sort queues to find the highest bid and lowest ask
        if buys: buys.sort(key=lambda x: x.price, reverse=True)
        if sells: sells.sort(key=lambda x: x.price)

        if buys and sells:
            highest_bid = buys[0].price
            lowest_ask = sells[0].price
            midpoint = (highest_bid + lowest_ask) / 2
            self.market_prices[symbol] = round(midpoint, 2)
            print(f"⚖️ [ORDER SPREAD] {symbol} adjusted via Midpoint to ${self.market_prices[symbol]:.2f} (Bid: ${highest_bid:.2f} | Ask: ${lowest_ask:.2f})")

        elif buys:
            # One-sided buy pressure pushes price up
            highest_bid = buys[0].price

            if highest_bid > self.market_prices[symbol]:
                self.market_prices[symbol] = round((self.market_prices[symbol] * 0.95) + (highest_bid * 0.05), 2)
                print(f"📈[BUY PRESSURE] {symbol} pulled up to ${self.market_prices[symbol]:.2f} by resting buyers.")

        elif sells:
            # One-sided sell pressure drags price down
            lowest_ask = sells[0].price
            if lowest_ask < self.market_prices[symbol]:
                self.market_prices[symbol] = round((self.market_prices[symbol] * 0.95) + (lowest_ask * 0.05), 2)
                print(f"📉[SELL PRESSURE] {symbol} dragged down to ${self.market_prices[symbol]:.2f} by resting sellers.")

    
    def generate_final_summary(self):
        print("\n" + "=" * 40)
        print(f"  FINAL PERFORMANCE REPORT: {SYMBOL}")
        print("=" * 40)
        
        report_data = []
        for bot_id, bot in self.bots.items():
            # Calculate key metrics
            # Note: Ensure these dictionary keys match your bot's internal storage
            inv_val = bot.portfolio.get(SYMBOL, 0.0) * bot.entry_prices.get(SYMBOL, 150.00)
            nav = bot.cash + inv_val
            roi = ((nav - 10000.00) / 10000.00) * 100
            
            report_data.append([bot_id, f"${bot.cash:,.2f}", f"${inv_val:,.2f}", f"${nav:,.2f}", f"{roi:+.2f}%"])

        # Sort by Net Asset Value (NAV) descending to highlight the best performers
        report_data.sort(key=lambda x: float(x[3].replace('$', '').replace(',', '')), reverse=True)
        
        # Render pretty table
        headers = ["Strategy Bot", "Available Cash", "Inventory", "Total NAV", "ROI"]
        print(tabulate(report_data, headers=headers, tablefmt="fancy_grid"))
        print("\n")

async def main():
    chosen_provider = YahooFinanceProvider(ticker=SYMBOL, period="8d", interval="1m")
    desk = RealTimeRiskDesk(data_provider = chosen_provider)

    # Deploy two bots
    #trend_runner = MomentumBot("TREND_RUNNER", initial_cash=12000.00)
    #payton = MeanReversionBot("PEIDONG", initial_cash=15000.00)

    #payton.portfolio["TIML"] = 50

    #desk.register_bot(payton)
    #desk.register_bot(trend_runner)

    # REGISTER ALL 15 BOT STRATEGIES
    desk.register_bot(MomentumBot("BOT_01_MOM", initial_cash=10000.00))
    desk.register_bot(MeanReversionBot("BOT_02_REV", initial_cash=10000.00))
    desk.register_bot(BollingerBandsBot("BOT_03_BB", initial_cash=10000.00))
    desk.register_bot(DonchianChannelBot("BOT_04_DONCHIAN", initial_cash=10000.00))
    desk.register_bot(ATRTrailingStopBot("BOT_05_ATR", initial_cash=10000.00))
    desk.register_bot(RSICloseBot("BOT_06_RSI", initial_cash=10000.00))
    desk.register_bot(MACDSignalBot("BOT_07_MACD", initial_cash=10000.00))
    desk.register_bot(EMACrossoverBot("BOT_08_EMA", initial_cash=10000.00))
    desk.register_bot(StochasticOscillatorBot("BOT_09_STOCH", initial_cash=10000.00))
    desk.register_bot(VWAPReversionBot("BOT_10_VWAP", initial_cash=10000.00))
    desk.register_bot(AccumulationDistributionBot("BOT_11_AD_FLOW", initial_cash=10000.00))
    desk.register_bot(RSIBollingerComboBot("BOT_12_HYBRID", initial_cash=10000.00))
    desk.register_bot(SupportResistanceBot("BOT_13_SUP_RES", initial_cash=10000.00))
    desk.register_bot(TimeInforceScalperBot("BOT_14_SCALPER", initial_cash=10000.00))
    desk.register_bot(GridTraderBot("BOT_15_GRID", initial_cash=10000.00))


    market_thread_task = asyncio.create_task(desk.simulate_market_feed())

    await asyncio.sleep(120)        # ADJUST SIMULATION RUN-TIME HERE
    
    print(f"\n🛑 [SYSTEM] Simulation time expired. Terminating market data feeds...")

    desk.is_running = False
    
    market_thread_task.cancel()

    try:
        await market_thread_task
    except asyncio.CancelledError:
        pass

    print(f"[SYSTEM] All background engine processing pipelines stopped successfully.")

    desk.generate_final_summary()
    
if __name__ == "__main__":
    asyncio.run(main())


