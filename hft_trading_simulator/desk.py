import asyncio
import random

from hft_trading_simulator.models import Order
from hft_trading_simulator.strategies import MomentumBot, MeanReversionBot

class RealTimeRiskDesk:
    def __init__(self):
        self.bots = {}
        self.market_prices = {
            "TIML" : 100.00,
            "AAPL" : 150.00
        }

        self.is_running = True

    def register_bot(self, bot):
        self.bots[bot.bot_id] = bot
        print(f"🔌[SYSTEM] {bot.bot_id} has connected to the Risk Desk. Cash: ${bot.cash:.2f}")

    async def simulate_market_feed(self):
        print("📡[MARKET] Live data stream initialized...")

        while self.is_running:
            await asyncio.sleep(0.4)    # Pause program for 0.4 seconds to simulate market trade timings
            symbol = random.choice(list(self.market_prices.keys()))

            # Shift price up or down by small percentage
            pct_change = random.uniform(-0.02, 0.025)
            prev_price = self.market_prices[symbol]
            self.market_prices[symbol] = round(self.market_prices[symbol] * (1 + pct_change), 2)
            new_price = self.market_prices[symbol]

            print(f"📊[TICK] {symbol} adjusted to ${new_price:.2f}, from {prev_price}. Percentage change: {pct_change}")

            for bot_id, bot in self.bots.items():       # .items() turns a dictionary into a paired tuples
                generated_order = bot.on_market_update(symbol, new_price)       # function from strategies

                if generated_order:                    # Basically means if theres a value in the variable the loop will run
                    self.risk_manager(generated_order)
    
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
            if total_cost > (bot.cash * 0.3):
                print(f"❌[ORDER REJECTED] {bot.bot_id} violated Position Sizing Rule! Single trade cost exceeds 30% threshold.")
                return
            
            bot.cash -= total_cost
            bot.portfolio[order.symbol] = bot.portfolio.get(order.symbol, 0) + order.quantity       # It's dictionary so they use the key to find and add up the new value
            print(f"✅[ORDER SETTLED] {bot.bot_id} bought {order.quantity} shares of {order.symbol} @ ${order.price:.2f} ")
            print(f"Updated Portfolio --> Balance: ${bot.cash:.2f} | Inventory: {bot.portfolio}")

        
        elif order.side == "SELL":
            # Inventory Stocks Sufficiency Check
            current_shares = bot.portfolio.get(order.symbol, 0)
            if current_shares < order.quantity:
                print(f"❌[ORDER REJECTED] {bot.bot_id} has insufficient inventory! Wants to sell {order.quantity}, holds {current_shares}")
                return
            
            total_credit = order.price * order.quantity
            bot.cash += total_credit
            bot.portfolio[order.symbol] -= order.quantity
            print(f"✅[ORDER SETTLED] {bot.bot_id} sold {order.quantity} shares of {order.symbol} @ ${order.price:.2f}")
            print(f"💼[PORTFOLIO UPDATE] --> Balance: ${bot.cash:.2f} | Inventory: {bot.portfolio}")


async def main():
    desk = RealTimeRiskDesk()

    # Deploy two bots
    trend_runner = MomentumBot("TREND_RUNNER", initial_cash=12000.00)
    payton = MeanReversionBot("PEIDONG", initial_cash=15000.00)

    payton.portfolio["TIML"] = 50

    desk.register_bot(payton)
    desk.register_bot(trend_runner)

    market_thread_task = asyncio.create_task(desk.simulate_market_feed())

    await asyncio.sleep(12)     # Let the market simulation run for 12 seconds
    
    await market_thread_task
    print(f"[SYSTEM] All background engine processing pipelines stopped successfully.")

if __name__ == "__main__":
    asyncio.run(main())