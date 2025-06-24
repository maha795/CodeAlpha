import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 125,
    "MSFT": 300
}

def main():
    portfolio = []
    while True:
        symbol = input("Enter stock symbol (or 'quit' to finish): ").upper()
        if symbol == 'QUIT':
            break
        if symbol in stock_prices:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            portfolio.append((symbol, quantity, stock_prices[symbol]))
        else:
            print("Invalid symbol. Try again.")
    
    total_investment = sum(qty * price for symbol, qty, price in portfolio)
    print("Total Investment:", total_investment)
    
    save_choice = input("Save to file? (y/n): ").lower()
    if save_choice == 'y':
        with open("portfolio.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Symbol", "Quantity", "Price", "Total"])
            for symbol, qty, price in portfolio:
                writer.writerow([symbol, qty, price, qty * price])
            writer.writerow(["Total", "", "", total_investment])
        print("Data saved to portfolio.csv")

if __name__ == "__main__":
    main()
