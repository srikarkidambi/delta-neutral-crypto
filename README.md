# Delta-Neutral Crypto Trading Strategy

This project implements a delta-neutral hedging strategy for cryptocurrency derivatives using data from the Deribit exchange. It includes modules for data fetching, strategy implementation, and backtesting.

## Project Overview

The delta-neutral strategy aims to create a market-neutral position by balancing long and short positions in related cryptocurrency instruments. This project uses Bitcoin perpetual and futures contracts from Deribit to demonstrate the strategy.

## Features

- Deribit API integration for fetching real-time and historical data
- Implementation of a basic delta-neutral strategy
- Backtesting engine to evaluate strategy performance
- Visualization of backtest results

## Results 
![image](https://github.com/user-attachments/assets/9ea8b92c-ba15-4824-bec8-71eb9a40012b)


## Project Structure

delta_neutral_crypto/
├── data/
│ ├── init.py
│ └── deribit_api.py
├── strategy/
│ ├── init.py
│ └── delta_neutral.py
├── backtesting/
│ ├── init.py
│ └── backtest.py
├── main.py
└── requirements.txt


- `data/`: Contains the API wrapper for Deribit
- `strategy/`: Implements the delta-neutral strategy
- `backtesting/`: Contains the backtesting engine
- `main.py`: Entry point for running the strategy and backtest

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/delta-neutral-crypto.git
   cd delta-neutral-crypto
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main script to execute the strategy backtest:
This will fetch historical data, run the backtest, and display the results.

## Results

The backtest results include:
- Total Return
- Sharpe Ratio
- Maximum Drawdown
- A plot of cumulative returns over time

## Future Improvements

- Implement more sophisticated delta calculation and hedging logic
- Add support for additional cryptocurrency exchanges
- Incorporate transaction costs and slippage into the backtest
- Develop a live trading module

## Contributing

Contributions to improve the strategy or extend the project's functionality are welcome. Please feel free to submit pull requests or open issues to discuss potential changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is for educational purposes only. Cryptocurrency trading carries a high level of risk, and may not be suitable for all investors. Before deciding to trade cryptocurrency, you should carefully consider your investment objectives, level of experience, and risk appetite.




