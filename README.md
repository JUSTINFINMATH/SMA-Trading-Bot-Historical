# SMA Trading Bot Historical
 SMA Trading Bot Historical

- Simulates a high-frequency trading (HFT) bot operating on synthetic, second-level stock price data over a single trading day.
- Begins with an initial balance, making buy or sell decisions based on short-term and long-term Simple Moving Average (SMA) crossovers.
- Generates synthetic stock price movements randomly to simulate real market fluctuations.
- Calculates short-term and long-term SMAs of the stock prices to identify buy (short-term SMA crosses above long-term SMA) or sell (short-term SMA crosses below long-term SMA) signals.
- Incorporates transaction costs for each trade, affecting the trading strategy's profitability.
- Executes trades to either buy as much as possible or sell all owned stocks based on SMA signals.
- Calculates the final financial outcome at the end of the trading day, including final balance, number of stocks owned, value of those stocks, total portfolio value, and overall profit or loss.
