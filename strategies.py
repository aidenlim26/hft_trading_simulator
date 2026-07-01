from models import Order

import dataclasses 
from typing import Literal

import math

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
        self.entry_prices = {}          # Tracking average purchase prices

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

    def calculate_dynamic_quantity(self, price: float, pct_allocation: float = 0.10) -> int:
        target_spend = self.cash * pct_allocation
        if target_spend < 100:  # Enforce minimum cash reserve
            return 0
        return int((self.cash * 0.25) / price)
    
    def on_market_update(self, symbol:str, new_price:float):        # Temporary placeholder, for future inheritance to use
        pass
        
    def check_basic_risk_exits(self, symbol:str, current_price:float) -> Order | None:
        # Take-profit / Stop-loss when necessary
        shares = self.portfolio.get(symbol,0)
        avg_cost = self.entry_prices.get(symbol, 0.0)

        if shares <= 0 or avg_cost == 0:
            return None
        
        # 5% above what bot paid for -> Take Profit
        if current_price >= (avg_cost * 1.05):
            print(f"💰 [RISK EXIT] {self.bot_id} triggered Take-Profit for {symbol} at ${current_price:.2f}")
            return self.submit_order(symbol, "SELL", current_price, shares)
        
        # 3% less than what bot paid for -> Stop Loss
        if current_price <= (avg_cost * 0.97):
            print(f"💥 [RISK EXIT] {self.bot_id} triggered Stop-Loss for {symbol} at ${current_price:.2f}")
            return self.submit_order(symbol, "SELL", current_price, shares)
        
        return None



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
                qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.12)

                if qty > 0:
                    print(f"📈 [STRATEGY MATCH] {self.bot_id} momentum entry on {symbol}.")
                    return self.submit_order(symbol, "BUY", new_price, qty)

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
                qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.12)

                if qty > 0:
                    print(f"🛒 [STRATEGY MATCH] {self.bot_id} thinks {symbol} is UNDERVALUED (${new_price:.2f} vs Avg: ${moving_average:.2f})")
                    return self.submit_order(symbol, "BUY", new_price, qty)
            
        return None
    
class BollingerBandsBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.price_history = {}
    
    def on_market_update(self, symbol, new_price):
        if symbol not in self.price_history:
            self.price_history[symbol] = []

        history = self.price_history[symbol]
        history.append(new_price)

        if len(history) > 10: history.pop(0)
            
        if len(history) == 10:
            ma = sum(history) / 10
            variance = sum((x - ma) ** 2 for x in history) / 10
            std_dev = math.sqrt(variance) if variance > 0 else 0.1
            
            if new_price > ma + (1.5 * std_dev):
                qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.10)
                if qty > 0:
                    print(f"⚡ [STRATEGY MATCH] {self.bot_id} Bollinger Upper Band Breakout on {symbol}!")
                    return self.submit_order(symbol, "BUY", new_price, qty)
                
            elif new_price < ma - (1.5 * std_dev):
                shares = self.portfolio.get(symbol, 0)

                if shares > 0:
                    print(f"🚨 [STRATEGY MATCH] {self.bot_id} Bollinger Lower Band Breakdown on {symbol}!")
                    return self.submit_order(symbol, "SELL", new_price, shares)
                
        return None
       

class DonchianChannelBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.price_history = {}

    def on_market_update(self, symbol, new_price):

        if symbol not in self.price_history:
            self.price_history[symbol] = []

        history = self.price_history[symbol]
        
        exit_order = self.check_basic_risk_exits(symbol, new_price)

        if exit_order: return exit_order

        if len(history) >= 7:
            highest_high = max(history[-7:])

            if new_price > highest_high:
                qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.15)

                if qty > 0:
                    print(f"🏔️ [STRATEGY MATCH] {self.bot_id} breached 7-period Donchian Peak on {symbol}!")
                    history.append(new_price)
                    return self.submit_order(symbol, "BUY", new_price, qty)
                    
        history.append(new_price)

        if len(history) > 20: 
            history.pop(0)

        return None

class ATRTrailingStopBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.price_history = {}

    def on_market_update(self, symbol, new_price):

        if symbol not in self.price_history:
            self.price_history[symbol] = []

        history = self.price_history[symbol]
        history.append(new_price)

        if len(history) > 6: history.pop(0)

        shares = self.portfolio.get(symbol, 0)

        if shares > 0 and len(history) >= 2:
            # Simple High-Freq pseudo-ATR approximation
            avg_range = sum(abs(history[i] - history[i-1]) for i in range(1, len(history))) / (len(history)-1)
            stop_floor = self.entry_prices.get(symbol, new_price) - (2.0 * max(avg_range, 0.5))

            if new_price < stop_floor:
                print(f"🛡️ [STRATEGY MATCH] {self.bot_id} triggered Volatility ATR Trailing Stop on {symbol}!")
                return self.submit_order(symbol, "SELL", new_price, shares)

        if len(history) >= 3 and history[-1] > history[-2]:
            qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.08)

            if qty > 0 and shares == 0:
                print(f"🎯 [STRATEGY MATCH] {self.bot_id} initial ATR-tracked breakout entry on {symbol}.")
                return self.submit_order(symbol, "BUY", new_price, qty)
            
        return None

class RSICloseBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.price_history = {}

    def on_market_update(self, symbol, new_price):

        if symbol not in self.price_history:
            self.price_history[symbol] = []

        history = self.price_history[symbol]
        history.append(new_price)

        if len(history) > 6: history.pop(0)

        if len(history) == 6:
            gains = sum(max(history[i] - history[i-1], 0) for i in range(1, 6))
            losses = sum(max(history[i-1] - history[i], 0) for i in range(1, 6))
            rs = gains / losses if losses > 0 else 999
            rsi = 100 - (100 / (1 + rs))

            if rsi < 25:  # Deeply Oversold
                qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.15)
                if qty > 0:
                    print(f"🔮 [STRATEGY MATCH] {self.bot_id} calculated Oversold RSI ({rsi:.1f}) on {symbol}!")
                    return self.submit_order(symbol, "BUY", new_price, qty)
            elif rsi > 75:  # Overbought
                shares = self.portfolio.get(symbol, 0)

                if shares > 0:
                    print(f"⚠️ [STRATEGY MATCH] {self.bot_id} calculated Overbought RSI ({rsi:.1f}) on {symbol}!")
                    return self.submit_order(symbol, "SELL", new_price, shares)
                
        return None


class MACDSignalBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.ema_12 = {}
        self.ema_26 = {}
        self.signal_line = {}

    def on_market_update(self, symbol, new_price):

        if symbol not in self.ema_12:
            self.ema_12[symbol], self.ema_26[symbol], self.signal_line[symbol] = new_price, new_price, 0.0
            return None

        # Mini High-Frequency Adjusted MACD Exp-Weightings
        self.ema_12[symbol] = (new_price - self.ema_12[symbol]) * (2/5) + self.ema_12[symbol]
        self.ema_26[symbol] = (new_price - self.ema_26[symbol]) * (2/11) + self.ema_26[symbol]

        macd_line = self.ema_12[symbol] - self.ema_26[symbol]
        prev_signal = self.signal_line[symbol]

        self.signal_line[symbol] = (macd_line - prev_signal) * (2/4) + prev_signal

        if macd_line > self.signal_line[symbol] and prev_signal >= macd_line:
            qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.10)

            if qty > 0:
                print(f"📡 [STRATEGY MATCH] {self.bot_id} MACD Line crossed over Signal Line on {symbol}!")
                return self.submit_order(symbol, "BUY", new_price, qty)
            
        elif macd_line < self.signal_line[symbol] and prev_signal <= macd_line:
            shares = self.portfolio.get(symbol, 0)

            if shares > 0:
                print(f"📉 [STRATEGY MATCH] {self.bot_id} MACD Line crossed under Signal Line on {symbol}!")
                return self.submit_order(symbol, "SELL", new_price, shares)
            
        return None


class EMACrossoverBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.fast_ema = {}
        self.slow_ema = {}

    def on_market_update(self, symbol, new_price):
        if symbol not in self.fast_ema:
            self.fast_ema[symbol], self.slow_ema[symbol] = new_price, new_price

            return None
            
        prev_fast, prev_slow = self.fast_ema[symbol], self.slow_ema[symbol]
        self.fast_ema[symbol] = (new_price - prev_fast) * (2/5) + prev_fast
        self.slow_ema[symbol] = (new_price - prev_slow) * (2/13) + prev_slow
        
        if prev_fast <= prev_slow and self.fast_ema[symbol] > self.slow_ema[symbol]:
            qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.10)

            if qty > 0:
                print(f"⚔️ [STRATEGY MATCH] {self.bot_id} Fast/Slow EMA Golden Cross on {symbol}!")
                return self.submit_order(symbol, "BUY", new_price, qty)
            
        elif prev_fast >= prev_slow and self.fast_ema[symbol] < self.slow_ema[symbol]:
            shares = self.portfolio.get(symbol, 0)

            if shares > 0:
                print(f"💀 [STRATEGY MATCH] {self.bot_id} Fast/Slow EMA Death Cross on {symbol}!")
                return self.submit_order(symbol, "SELL", new_price, shares)
            
        return None


class StochasticOscillatorBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.price_history = {}

    def on_market_update(self, symbol, new_price):

        if symbol not in self.price_history:
            self.price_history[symbol] = []

        history = self.price_history[symbol]
        history.append(new_price)

        if len(history) > 8: history.pop(0)

        if len(history) == 8:
            low_bound, high_bound = min(history), max(history)
            denom = (high_bound - low_bound)
            k_percent = ((new_price - low_bound) / denom * 100) if denom > 0 else 50

            if k_percent < 15:
                qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.12)

                if qty > 0:
                    print(f"🎰 [STRATEGY MATCH] {self.bot_id} Stochastic Oscillator Oversold (%K: {k_percent:.1f}) on {symbol}!")
                    return self.submit_order(symbol, "BUY", new_price, qty)
                
            elif k_percent > 85:
                shares = self.portfolio.get(symbol, 0)

                if shares > 0:
                    print(f"🎲 [STRATEGY MATCH] {self.bot_id} Stochastic Oscillator Overbought (%K: {k_percent:.1f}) on {symbol}!")
                    return self.submit_order(symbol, "SELL", new_price, shares)
                
        return None
    
class VWAPReversionBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.cumulative_pv = {}
        self.cumulative_vol = {}

    def on_market_update(self, symbol, new_price):
        if symbol not in self.cumulative_pv:
            self.cumulative_pv[symbol], self.cumulative_vol[symbol] = 0.0, 0
        
        # Simulate local intraday institutional volume block weightings
        simulated_volume = 1000 + (int(new_price * 7) % 500)
        self.cumulative_pv[symbol] += (new_price * simulated_volume)
        self.cumulative_vol[symbol] += simulated_volume
        
        vwap = self.cumulative_pv[symbol] / self.cumulative_vol[symbol]
        
        if new_price < vwap * 0.985:
            qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.14)

            if qty > 0:
                print(f"📊 [STRATEGY MATCH] {self.bot_id} buying deep discount underneath VWAP target for {symbol}!")
                return self.submit_order(symbol, "BUY", new_price, qty)
            
        elif new_price > vwap * 1.015:
            shares = self.portfolio.get(symbol, 0)

            if shares > 0:
                print(f"📈 [STRATEGY MATCH] {self.bot_id} distributing premium overvalued positions above VWAP for {symbol}!")
                return self.submit_order(symbol, "SELL", new_price, shares)
            
        return None


class AccumulationDistributionBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.ad_metric = {}

    def on_market_update(self, symbol, new_price):
        if symbol not in self.ad_metric:
            self.ad_metric[symbol] = 0.0
            return None

        # Emulating sub-tick structural micro-spread spreads
        close, low, high = new_price, new_price * 0.997, new_price * 1.002
        money_flow_multiplier = ((close - low) - (high - close)) / (high - low)
        sim_volume = 500 + (int(new_price) % 100)
        self.ad_metric[symbol] += (money_flow_multiplier * sim_volume)

        if self.ad_metric[symbol] > 400:
            qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.08)

            if qty > 0 and self.portfolio.get(symbol, 0) == 0:
                print(f"📦 [STRATEGY MATCH] {self.bot_id} institutional entry confirmation on {symbol} via A/D metric accumulation flow.")
                return self.submit_order(symbol, "BUY", new_price, qty)
            
        elif self.ad_metric[symbol] < -400:
            shares = self.portfolio.get(symbol, 0)

            if shares > 0:
                print(f"⚠️ [STRATEGY MATCH] {self.bot_id} liquidation signal via heavy A/D distribution out-flows for {symbol}!")
                self.ad_metric[symbol] = 0.0
                return self.submit_order(symbol, "SELL", new_price, shares)
            
        return None


class RSIBollingerComboBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.price_history = {}

    def on_market_update(self, symbol, new_price):
        if symbol not in self.price_history:
            self.price_history[symbol] = []

        history = self.price_history[symbol]
        history.append(new_price)

        if len(history) > 8: history.pop(0)

        if len(history) == 8:
            ma = sum(history) / 8
            var = sum((x - ma) ** 2 for x in history) / 8
            sd = math.sqrt(var) if var > 0 else 0.1
            
            gains = sum(max(history[i] - history[i-1], 0) for i in range(1, 8))
            losses = sum(max(history[i-1] - history[i], 0) for i in range(1, 8))
            rsi = 100 - (100 / (1 + (gains / losses))) if losses > 0 else 50

            # Double-layered confirmation filter execution
            if new_price < (ma - sd) and rsi < 30:
                qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.15)

                if qty > 0:
                    print(f"💎 [STRATEGY MATCH] CONSERVATIVE HYBRID entry on {symbol} (RSI: {rsi:.1f} + Bollinger Floor met).")
                    return self.submit_order(symbol, "BUY", new_price, qty)
                
            elif new_price > (ma + sd) and rsi > 70:
                shares = self.portfolio.get(symbol, 0)
                if shares > 0:

                    print(f"🔒 [STRATEGY MATCH] CONSERVATIVE HYBRID exit on {symbol} executed.")
                    return self.submit_order(symbol, "SELL", new_price, shares)
                
        return None


class SupportResistanceBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.floor = 110.0
        self.ceiling = 125.0

    def on_market_update(self, symbol, new_price):
        # Dynamically adjust bounding bands over macro range boundaries
        if symbol == "AAPL":
            self.floor, self.ceiling = 145.0, 165.0
            
        exit_order = self.check_basic_risk_exits(symbol, new_price)
        if exit_order: return exit_order

        if new_price <= self.floor * 1.01:
            qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.10)

            if qty > 0:
                print(f"🧱 [STRATEGY MATCH] {self.bot_id} buying the horizontal channel support floor for {symbol} @ ${new_price:.2f}")
                return self.submit_order(symbol, "BUY", new_price, qty)
            
        elif new_price >= self.ceiling * 0.99:
            shares = self.portfolio.get(symbol, 0)

            if shares > 0:
                print(f"🏛️ [STRATEGY MATCH] {self.bot_id} selling the horizontal channel resistance ceiling for {symbol} @ ${new_price:.2f}")
                return self.submit_order(symbol, "SELL", new_price, shares)
            
        return None

class TimeInforceScalperBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.ticks_held = {}

    def on_market_update(self, symbol, new_price):
        if symbol not in self.ticks_held:
            self.ticks_held[symbol] = 0

        shares = self.portfolio.get(symbol, 0)

        if shares > 0:
            self.ticks_held[symbol] += 1

            # Hard structural macro execution: Exit position unconditionally after 4 ticks
            if self.ticks_held[symbol] >= 4:
                print(f"⏱️ [STRATEGY MATCH] {self.bot_id} holding time expired. Closing {symbol} scalp position.")
                self.ticks_held[symbol] = 0
                return self.submit_order(symbol, "SELL", new_price, shares)
                
        # Look for heavy velocity volatility to enter
        qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.07)

        if qty > 0 and shares == 0:
            self.ticks_held[symbol] = 0
            return self.submit_order(symbol, "BUY", new_price, qty)
        
        return None


class GridTraderBot(BaseBot):
    def __init__(self, bot_id, initial_cash):
        super().__init__(bot_id, initial_cash)
        self.last_grid_price = {}

    def on_market_update(self, symbol, new_price):
        if symbol not in self.last_grid_price:
            self.last_grid_price[symbol] = new_price
            return None
            
        base_grid = self.last_grid_price[symbol]
        grid_interval = 4.00  # Execute adjustments every $4.00 movement step
        
        if new_price <= base_grid - grid_interval:
            qty = self.calculate_dynamic_quantity(new_price, pct_allocation=0.08)

            if qty > 0:
                print(f"🕸️ [STRATEGY MATCH] {self.bot_id} captured lower matrix grid line. Averaging down on {symbol}.")
                self.last_grid_price[symbol] = new_price
                return self.submit_order(symbol, "BUY", new_price, qty)
                
        elif new_price >= base_grid + grid_interval:
            shares = self.portfolio.get(symbol, 0)

            if shares > 0:
                print(f"🕸️ [STRATEGY MATCH] {self.bot_id} captured higher matrix grid line. Shaving profits on {symbol}.")
                self.last_grid_price[symbol] = new_price
                return self.submit_order(symbol, "SELL", new_price, shares)
            
        return None
    
