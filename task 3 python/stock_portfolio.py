import requests

def get_stock_data(symbol):
    api_key ='RMGUDHDWDYWALGY3'
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    if 'Global Quote' in data:
        return data['Global Quote']
    else:
        print("Error: Could not retrieve data for symbol:", symbol)
        return None

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] += quantity
        else:
            self.stocks[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] -= quantity
            if self.stocks[symbol] <= 0:
                del self.stocks[symbol]

    def get_portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.stocks.items():
            stock_data = get_stock_data(symbol)
            if stock_data and '05. price' in stock_data:
                price = float(stock_data['05. price'])
                total_value += price * quantity
        return total_value

portfolio = Portfolio()

while True:
    print("Portfolio Tracker")
    print("1. Add stock")
    print("2. Remove stock")
    print("3. View portfolio")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        symbol = input("Enter stock symbol: ")
        quantity = int(input("Enter quantity: "))
        portfolio.add_stock(symbol, quantity)
    elif choice == '2':
        symbol = input("Enter stock symbol: ")
        quantity = int(input("Enter quantity: "))
        portfolio.remove_stock(symbol, quantity)
    elif choice == '3':
        print("Portfolio Value:", portfolio.get_portfolio_value())
      
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again.")
