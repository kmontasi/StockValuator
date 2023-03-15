# StockValuator

StockValuator is a Python program that searches for stocks using tickers that users search for. It shows user Intrinsic value using necessary data about the stocks. Alpha vantage api is used to retrieve the value, user has to supply their own api key from https://www.alphavantage.co/ .

## Installation
Clone the repository to your local machine.

```git clone https://github.com/kmontasi/StockValuator.git```

Install the required Python packages.

```pip install -r requirements.txt```

Usage

Open the terminal and navigate to the repository folder.

```cd StockValuator```

Run the stock_valuator.py file.

```python main.py```

Enter the required information when prompted.



## TODO
I intent to vastly expand upon the available formulas and the user interface.




## Features
Currently the program shows user:
-   The last price(last available price)
-   TTP EPS value (Trailing Earnings Per Share)
-   "GOOD" P/E value (price per earnings)
-   Grahams number (measures a stock's fundamental value)


## Contributing
Contributions are welcome! Please open an issue or pull request for any bugs or feature requests.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.