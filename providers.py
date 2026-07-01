import random

class YahooFinanceProvider:
    def __init__(self, ticker="AAPL", period="1d", interval="1m"):
        self.ticker = ticker
        self.period = period
        self.interval = interval
    
    def fetch_historical_prices(self) -> list:
        import yfinance as yf

        print(f"📥 [DATA API] Fetching single-market history from Yahoo Finance for {self.ticker}...")

        # Download the tracking data
        data = yf.download(tickers=self.ticker, period=self.period, interval=self.interval)

        close_prices = data["Close"].squeeze().dropna().tolist()

        return [round(float(price), 2) for price in close_prices]
    

class LocalFallbackProvider:
    def fetch_historical_prices(self) -> list:
        print("📁 [DATA API] Generating single-market sequence via Local Fallback...")

        price = 150.0
        sequence = []

        for i in range(500):
            price = round(price * (1 + random.uniform(-0.001, 0.001)), 2)
            sequence.append(price)
        return sequence