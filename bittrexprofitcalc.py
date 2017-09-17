## Bittrex Trade Profit Calculator
##  Usage:
##      You will need Python installed https://www.python.org/ftp/python/3.6.2/python-3.6.2.exe
##      Once installed, you need to install Pandas from the command line.
##            pip install pandas
##      Download your current trade list from Bittrex. So head to https://bittrex.com/History
##      and click the CSV button in the 'COMPLETED' section of Bittrex.
##      Copy the .csv file to the same directory as this script and rename it to bittrex.csv
##      Run the script from command line. Example:
##
##  Bittrex Profit Calculator
##    You've done 39 trades with 15 stocks since 09/05/2017 03:58:50 PM.
##    
##        (3)BTC-EDG       Hodling: 50.91083078     Profit: 0.002553
##        (2)BTC-XVG       Hodling: 0.00000000      Profit: 0.000004
##        (3)BTC-RISE      Hodling: 0.00000000      Profit: 0.003070
##        (3)BTC-NEO       Hodling: 12.71804302     Profit: 0.000051
##        (2)BTC-LSK       Hodling: 0.00000000      Profit: -0.000254
##        (1)BTC-OK        Hodling: 0.00000000      Profit: -0.000386
##        (1)BTC-PAY       Hodling: 31.18704870     Profit: 0.000000
##        (0)BTC-XMR       Hodling: -0.49000000     Profit: 0.000000
##        (1)ETH-QTUM      Hodling: 6.72553984      Profit: 0.000000
##        (1)ETH-OMG       Hodling: 6.74945459      Profit: 0.000000
##        (2)BTC-ETH       Hodling: 0.66081087      Profit: 0.000000
##        (2)BTC-QTUM      Hodling: 5.44552309      Profit: 0.002143
##        (2)BTC-OMG       Hodling: 3.16576057      Profit: 0.000093
##        (1)BTC-STRAT     Hodling: 0.00000000      Profit: 0.000015
##        (0)BTC-DCR       Hodling: -0.19546350     Profit: 0.000000
##        
##    You've made 0.007287BTC, and 0.000000ETH.                                                                               
##    
##    You made the most off BTC-RISE. You made the least of BTC-OK.
##    You have deposited into Bittrex, 0.177421BTC and 0.499998ETH. 

## Current Limiations:
## If you cross trade markets (Ie. buy ETH/OMG then sell it on BTC/OMG it'll report incorrect numbers).
## No market for USDT

import pandas as pd
from string import ascii_lowercase as abc

close = 'Closed Date'
open = 'Open Date'
coin = 'Market'
type = 'Type'
units = 'Units Filled'
rate = 'Actual Rate'
cost = 'Cost / Proceeds'

class Stock:
    def __init__(self, name):
        self.name = name
        self.total = 0.00000000
        self.purchases = []
    def __str__(self):
        return "%s: %f | %s\n" % (self.name, self.total, self.purchases)

    def buy(self, amount, price):
        # add a purchase with the amount, price, and remaining.
        self.purchases.append( [amount, price, amount, 0.00000] )
            
    def sell(self, amount, price):
        fulfilled = 0.0
        for i in reversed(range(0, len(self.purchases))):
            if self.purchases[i][2] == 0:
                continue
            added = 0.0
            if self.purchases[i][2] + fulfilled > amount:
                left = amount - fulfilled
                self.purchases[i][2] -= left
                fulfilled += left
                added = left

            elif self.purchases[i][2] + fulfilled < amount:
                fulfilled += self.purchases[i][2]
                added = self.purchases[i][2]
                self.purchases[i][2] = 0
            else:
                fulfilled = amount
                added = self.purchases[i][2]                
                self.purchases[i][2] = 0
            self.purchases[i][3] = (added * price) - (added * self.purchases[i][1])
            if fulfilled > amount:
                fulfilled = amount
            if fulfilled == amount:
                break

            
                
    def profit(self):
        profit = 0.0
        for i in self.purchases:
            profit += i[3]
        
        return profit
            
# Load csv
df = pd.read_csv("bittrex.csv") 

stocks = {}

for i in df['Market']:
	if i not in stocks:
		stocks[i] = Stock(i)
		
print("Bittrex Profit Calculator\n")
print("You've done %d trades with %d stocks since %s.\n" % (len(df[type]), len(stocks), df[close][len(df[close])-1]))
	
spent = {'BTC':0.00000000, 'ETH':0.00000000}
wallet = {'BTC':0.00000000, 'ETH':0.00000000}

for i in reversed(range(0, len(df[type]))):
    market = df[coin][i][:3]
    price = df[cost][i]
    perunit = df[rate][i]
    if price < 0.0000000:
        #Buy
        if wallet[market] < abs(price):
            #Didn't have enough money so it's a loadup from outside.
            spent[market] += abs(price)
        else:
            #had enough money so it's a buy.
            wallet[market] += price
        stocks[df[coin][i]].total += df[units][i]
        stocks[df[coin][i]].buy(df[units][i], perunit)
    else:
        #Sell
        stocks[df[coin][i]].sell(df[units][i], perunit)
        stocks[df[coin][i]].total -= df[units][i]
        wallet[market] += price
        #Check previous buy to see if this is profitable.
       
profit = {'BTC':0.00000000, 'ETH':0.00000000}
high = None
low = None
for k, stock in stocks.items():
    market = stock.name[:3]
    profit[market] += stock.profit()
    if not high:
        high = stock
    else:
        if high.profit() < stock.profit():
            high = stock
    if not low:
        low = stock
    else:
        if low.profit() > stock.profit():
            low = stock        
    
    print("\t(%d)%-10s    Hodling: %-15.8f Profit: %f" % (len(stock.purchases), k, stock.total, stock.profit()))

print("\nYou've made %fBTC, and %fETH." % (profit['BTC'], profit['ETH']) )
print("You made the most off %s. You made the least of %s.\n" %( high.name, low.name))
print("You have deposited into Bittrex, %fBTC and %fETH." % (spent['BTC'], spent['ETH']))