import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        """
        Add a stock to the portfolio.
        :param ticker: The stock ticker symbol (e.g., 'AAPL' for Apple).
        :param shares: The number of shares the user owns.
        """
        if ticker in self.portfolio:
            self.portfolio[ticker]['shares'] += shares
        else:
            self.portfolio[ticker] = {'shares': shares}
        print(f"Added {shares} shares of {ticker} to your portfolio.")
    
    def remove_stock(self, ticker, shares):
        """
        Remove a certain number of shares of a stock from the portfolio.
        :param ticker: The stock ticker symbol.
        :param shares: The number of shares to remove.
        """
        if ticker in self.portfolio:
            if self.portfolio[ticker]['shares'] >= shares:
                self.portfolio[ticker]['shares'] -= shares
                if self.portfolio[ticker]['shares'] == 0:
                    del self.portfolio[ticker]
                print(f"Removed {shares} shares of {ticker}.")
            else:
                print(f"Cannot remove {shares} shares. You only own {self.portfolio[ticker]['shares']} shares.")
        else:
            print(f"Stock {ticker} not found in portfolio.")
    
    def get_stock_price(self, ticker):
        """
        Fetch the current price of the stock from Yahoo Finance.
        :param ticker: The stock ticker symbol.
        :return: Current stock price.
        """
        stock = yf.Ticker(ticker)
        return stock.history(period='1d')['Close'].iloc[-1]

    def track_performance(self):
        """
        Track the performance of all the stocks in the portfolio.
        :return: Display the stock performance.
        """
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        print(f"{'Stock':<10}{'Shares':<10}{'Price ($)':<15}{'Total Value ($)':<15}")
        print("-" * 50)
        
        total_portfolio_value = 0
        
        for ticker, data in self.portfolio.items():
            current_price = self.get_stock_price(ticker)
            total_value = data['shares'] * current_price
            total_portfolio_value += total_value
            print(f"{ticker:<10}{data['shares']:<10}{current_price:<15.2f}{total_value:<15.2f}")

        print(f"\nTotal Portfolio Value: ${total_portfolio_value:.2f}")
    
    def portfolio_summary(self):
        """
        Show a summary of the stocks in the portfolio.
        """
        if not self.portfolio:
            print("Your portfolio is empty.")
        else:
            for ticker, data in self.portfolio.items():
                print(f"{ticker}: {data['shares']} shares")

# Example usage
portfolio = StockPortfolio()

# Adding stocks to the portfolio
portfolio.add_stock('AAPL', 10)  # Add 10 shares of Apple
portfolio.add_stock('GOOGL', 5)  # Add 5 shares of Google
portfolio.add_stock('TSLA', 15)   # Add 15 shares of Tesla
portfolio.add_stock('AMZN', 20)   # Add 20 shares of Amazon
portfolio.add_stock('MSFT', 10)   # Add 10 shares of Microsoft
portfolio.add_stock('NVDA', 25)   # Add 25 shares of NVIDIA
portfolio.add_stock('META', 8)    # Add 8 shares of Meta (Facebook)
portfolio.add_stock('KO', 30)     # Add 30 shares of Coca-Cola
portfolio.add_stock('PFE', 12)    # Add 12 shares of Pfizer

# Removing stocks from the portfolio
portfolio.remove_stock('AAPL', 2)  # Remove 2 shares of Apple
portfolio.remove_stock('TSLA', 5)   # Remove 5 shares of Tesla
portfolio.remove_stock('AMZN', 5)   # Remove 5 shares of Amazon
portfolio.remove_stock('NVDA', 10)  # Remove 10 shares of NVIDIA

# Tracking the performance of the portfolio
portfolio.track_performance()

# Showing a summary of the portfolio
portfolio.portfolio_summary()
