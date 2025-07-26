# Stock Portfolio Tracker

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135
}

# Dictionary to store user input
portfolio = {}

# Get user input
print("Enter stock names and quantities (type 'done' to finish):")
while True:
    stock = input("Stock Symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in our database. Try again.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_investment = 0
print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares × ₹{price} = ₹{investment}")

print(f"\nTotal Investment: ₹{total_investment}")

# Optional: Save to file
save = input("Do you want to save the portfolio to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter file name (e.g., portfolio.txt or portfolio.csv): ")
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Investment\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock},{quantity},{price},{investment}\n")
        file.write(f"\nTotal Investment,,,{total_investment}")
    print(f"Portfolio saved to '{filename}'")
