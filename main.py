from data.deribit_api import DeribitAPI
from strategy.delta_neutral import DeltaNeutralStrategy
from backtesting.backtest import Backtest

def main():
    print("Starting the program...")
    
    api = DeribitAPI()
    spot_symbol = 'BTC-PERPETUAL'
    futures_symbol = 'BTC-27SEP24'

    print("Fetching historical data...")
    # Fetch historical data
    spot_data = api.get_historical_data(spot_symbol)
    futures_data = api.get_historical_data(futures_symbol)

    print(f"Spot data shape: {spot_data.shape}")
    print(f"Futures data shape: {futures_data.shape}")

    print("Initializing strategy...")
    # Initialize strategy
    strategy = DeltaNeutralStrategy(spot_symbol, futures_symbol)

    print("Running backtest...")
    # Run backtest
    backtest = Backtest(strategy, initial_capital=10000)
    backtest.run(spot_data, futures_data)

    print("Calculating and printing results...")
    # Print results
    results = backtest.results
    print(f"Total Return: {results['cumulative_returns'].iloc[-1] - 1:.2%}")
    print(f"Sharpe Ratio: {backtest.calculate_sharpe_ratio():.2f}")
    print(f"Max Drawdown: {backtest.calculate_max_drawdown():.2%}")

    print("Plotting results...")
    # Plot results
    backtest.plot_results()

    print("Program finished.")

if __name__ == '__main__':
    main()