#Stock Portfolio Tracker
stock_prices = {
    "AAPL":180,
    "TSLA":250,
    "GOOGL":140,
    "MSFT":420,
    "AMZN":185
}

total_investment = 0
print("==== Stock Portfolio Tracker ====")

while True:
    stock = input("\nEnter stock symbol(or 'done' to finish):").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not avaliable.Please choose from:",",".join(stock_prices.keys()))
        continue
    
    quantity = int(input("Enter quantity:"))
    
    investment = stock_prices[stock] * quantity
    total_investment += investment
    
    print("Stock Price:",stock_prices[stock])
    print("Investment Value:",investment)
    
    print("\n==== Portfolio Summary ====")
    print("Total Investment Value:$",total_investment)
    
    with open("portfolio_result.txt","w") as file:
        file.write("Stock Portfolio Tracker\n")
        file.write("============================\n")
        file.write("Total Investment Value:$" + str(total_investment))
        
    print("Result saved to portfolio_result.txt")    
    