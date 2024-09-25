import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Backtest:
    def __init__(self, strategy, initial_capital):
        self.strategy = strategy
        self.initial_capital = initial_capital
        self.results = None

    def run(self, spot_data, futures_data):
        signals = self.strategy.generate_signals(spot_data, futures_data)
        self.results = self._calculate_returns(signals)

    def _calculate_returns(self, signals):
        # Implement your return calculation logic here
        # This is a simplified example
        print("Calculating returns for signals:", signals)
        df = pd.DataFrame(signals)
        df['pnl'] = (df['spot_position'] * df['spot_price'].pct_change() +
                     df['futures_position'] * df['futures_price'].pct_change())
        df['cumulative_returns'] = (1 + df['pnl']).cumprod()
        return df

    def plot_results(self, save_path='backtest_results.png'):
        if self.results is None:
            raise ValueError("Backtest hasn't been run yet")
        
        plt.figure(figsize=(12, 6))
        plt.plot(self.results.index, self.results['cumulative_returns'])
        plt.title('Delta-Neutral Strategy Cumulative Returns')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns')
        plt.savefig(save_path)
        plt.close()
        print(f"Plot saved to {save_path}")

    def calculate_sharpe_ratio(self, risk_free_rate=0.02):
        returns = self.results['pnl']
        excess_returns = returns - risk_free_rate / 252  # Assuming daily returns
        return np.sqrt(252) * excess_returns.mean() / excess_returns.std()

    def calculate_max_drawdown(self):
        cumulative_returns = self.results['cumulative_returns']
        peak = cumulative_returns.expanding(min_periods=1).max()
        drawdown = (cumulative_returns / peak) - 1
        return drawdown.min()

    # Add more methods for calculating performance metrics, etc.
