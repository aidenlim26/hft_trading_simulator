import asyncio
import random

from models import Order

from strategies import (
    MomentumBot, MeanReversionBot, BollingerBandsBot, DonchianChannelBot,
    ATRTrailingStopBot, RSICloseBot, MACDSignalBot, EMACrossoverBot,
    StochasticOscillatorBot, VWAPReversionBot, AccumulationDistributionBot,
    RSIBollingerComboBot, SupportResistanceBot, TimeInforceScalperBot, GridTraderBot
)

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

        try:
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

        except asyncio.CancelledError:
            print(f"⚙️ [DEBUG] market_thread_task successfully caught CancelledError!")
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
            if total_cost > (bot.cash * 0.3):
                print(f"❌[ORDER REJECTED] {bot.bot_id} violated Position Sizing Rule! Single trade cost exceeds 30% threshold.")
                return
            
            bot.cash -= total_cost

            current_shares = bot.portfolio.get(order.symbol, 0.0)
            old_avg = bot.entry_prices.get(order.symbol, 0.0)
            new_avg = ((old_avg * current_shares) + (order.price * order.quantity)) / (current_shares + order.quantity)
            bot.entry_prices[order.symbol] = round(new_avg, 2)      # Replaces the value in the directory of "old_avg"

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

            if bot.portfolio[order.symbol] == 0:
                del bot.entry_prices[order.symbol]          # Remove past data to prevent stale limits

            print(f"✅[ORDER SETTLED] {bot.bot_id} sold {order.quantity} shares of {order.symbol} @ ${order.price:.2f}")
            print(f"💼[PORTFOLIO UPDATE] --> Balance: ${bot.cash:.2f} | Inventory: {bot.portfolio}")

    def generate_final_summary(self):
        print("=" * 85)
        print(f"HFT TRADING SIMULATOR (20s) SUMMARY")
        print("=" * 85)

        print(f"{'Rank':<6}{'Bot Identifier':<18}{'Available Cash':<16}{'Inventory Valuation':<22}{'Net Asset Value (NAV)':<15}")
        print("-" * 85)

        leaderboard_data = []

        for bot_id, bot, in self.bots.items():      # bot is referring to the actual object (e.g. MomentumBot)
            inventory_value = 0.0
            
            for symbol, shares in bot.portfolio.items():
                current_price = self.market_prices.get(symbol, 0.0)
                inventory_value += shares * current_price

            net_asset_value = bot.cash + inventory_value
            leaderboard_data.append({
                "bot_id": bot_id,
                "cash": bot.cash,
                "inventory_value": inventory_value,
                "nav": net_asset_value
            })

        leaderboard_data.sort(key=lambda x: x["nav"], reverse=True)

        for rank, data in enumerate(leaderboard_data, 1):
            print(f" #{rank:<4}{data['bot_id']:<18}${data['cash']:<15,.2f}${data['inventory_value']:<21,.2f}${data['nav']:<15,.2f}")
            print("=" * 85)

async def main():
    desk = RealTimeRiskDesk()

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

    await asyncio.sleep(20)     
    
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


