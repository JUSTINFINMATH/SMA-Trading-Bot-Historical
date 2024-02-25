import numpy as np
import pandas as pd

# Parameters
initial_balance = 10000  # Starting balance in hypothetical currency
transaction_cost = 0.01  # Assuming very low transaction cost for high-frequency trading
short_window = 120  # Short-term SMA window, equivalent to 2 minutes
long_window = 600  # Long-term SMA window, equivalent to 10 minutes
total_seconds = 23400  # Total trading seconds in a day

# Generate synthetic second-level price data
np.random.seed(42)
price_changes = np.random.randn(total_seconds) / 1000  # Small random price changes
stock_price = 100  # Starting stock price
stock_prices = pd.Series(stock_price + np.cumsum(price_changes))

# Calculate SMAs
short_sma = stock_prices.rolling(window=short_window, min_periods=1).mean()
long_sma = stock_prices.rolling(window=long_window, min_periods=1).mean()

# Initialize variables for simulation
balance = initial_balance
stock_owned = 0
transaction_history = []

# Trading strategy based on SMA crossover
for i in range(1, len(stock_prices)):
    if short_sma.iloc[i-1] < long_sma.iloc[i-1] and short_sma.iloc[i] > long_sma.iloc[i] and balance >= stock_prices.iloc[i] + transaction_cost:
        # Buy as much as possible
        stocks_to_buy = balance // (stock_prices.iloc[i] + transaction_cost)
        stock_owned += stocks_to_buy
        balance -= stocks_to_buy * (stock_prices.iloc[i] + transaction_cost)
        transaction_history.append(('buy', stock_prices.iloc[i], stocks_to_buy))
    elif short_sma.iloc[i-1] > long_sma.iloc[i-1] and short_sma.iloc[i] < long_sma.iloc[i] and stock_owned > 0:
        # Sell all owned stocks
        balance += stock_owned * (stock_prices.iloc[i] - transaction_cost)
        transaction_history.append(('sell', stock_prices.iloc[i], stock_owned))
        stock_owned = 0

# Calculate final values
final_stock_value = stock_owned * stock_prices.iloc[-1]
total_value = balance + final_stock_value
profit_or_loss = total_value - initial_balance

# Output results
print(f"Final Balance: {balance:.2f}")
print(f"Stocks Owned: {stock_owned}")
print(f"Value of Stocks Owned: {final_stock_value:.2f}")
print(f"Total Value: {total_value:.2f}")
print(f"Profit/Loss: {profit_or_loss:.2f}")
