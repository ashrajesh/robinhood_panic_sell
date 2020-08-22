import robin_stocks as r

def logintoaccount():
    print("\nUpon entering your Email / Username and Password, everything in your portfolio will be sold off. The entire process may take up to a minute or more depending on the number of unique holdings you have.\n")
    print("Ensure that you have enabled Two-Factor Authentication in Robinhood before proceeding\n")
    print("Enter Email / username: ")
    username = input()
    print("Enter password: ")
    password = input()
    login = r.login(username, password)
    print("\nProcessing request...")

def sell_all():
    quant = r.account.get_open_stock_positions(info='quantity')
    stocks = r.build_holdings()
    numofholdings = 0
    ticker = []
    for key,value in stocks.items():
        ticker.append(key)
        numofholdings += 1
    print("\nTotal number of holdings: " + str(numofholdings))
    print("\nNow Selling:")
    for x in range(numofholdings):
        print(ticker[x]+", "+ str(float(quant[x])))
        r.orders.order_sell_fractional_by_quantity(ticker[x], float(quant[x]), timeInForce='gtc', extendedHours=False)

logintoaccount()
sell_all()