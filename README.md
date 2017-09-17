# BittrexProfitCalc
A simple python program to calculate the profit/loss you've done directly with Bittrex trades.

# Requirements

You need to install the python interpreter from https://www.python.org/downloads/
From there, open command line and install pandas "pip install pandas"

Download a cvs copy of your trades from Bittrex at  https://bittrex.com/History
Click the 'CVS' button under the 'COMPLETED' Section.
Move that file to the location the script is located and rename it to 'bittrex.cvs'

Run the script from command line.

# Output

  Bittrex Profit Calculator
    You've done 39 trades with 15 stocks since 09/05/2017 03:58:50 PM.
    
        (3)BTC-EDG       Hodling: 50.91083078     Profit: 0.002553
        (2)BTC-XVG       Hodling: 0.00000000      Profit: 0.000004
        (3)BTC-RISE      Hodling: 0.00000000      Profit: 0.003070
        (3)BTC-NEO       Hodling: 12.71804302     Profit: 0.000051
        (2)BTC-LSK       Hodling: 0.00000000      Profit: -0.000254
        (1)BTC-OK        Hodling: 0.00000000      Profit: -0.000386
        (1)BTC-PAY       Hodling: 31.18704870     Profit: 0.000000
        (0)BTC-XMR       Hodling: -0.49000000     Profit: 0.000000
        (1)ETH-QTUM      Hodling: 6.72553984      Profit: 0.000000
        (1)ETH-OMG       Hodling: 6.74945459      Profit: 0.000000
        (2)BTC-ETH       Hodling: 0.66081087      Profit: 0.000000
        (2)BTC-QTUM      Hodling: 5.44552309      Profit: 0.002143
        (2)BTC-OMG       Hodling: 3.16576057      Profit: 0.000093
        (1)BTC-STRAT     Hodling: 0.00000000      Profit: 0.000015
        (0)BTC-DCR       Hodling: -0.19546350     Profit: 0.000000
        
    You've made 0.007287BTC, and 0.000000ETH.                                                                               
    
    You made the most off BTC-RISE. You made the least of BTC-OK.
    You have deposited into Bittrex, 0.177421BTC and 0.499998ETH. 
    
# Limitaions
If you do any cross market trading (ie. you buy ETH/OMG and then sell it on BTC/OMG) it will report incorrect numbers.
I would suggest editing the CVS via excel or something and converting the ETH price to BTC, and the Type from 'ETH/' to 'BTC/' and you will get accurate numbers.
It doesn't currently support the USDT market.

# Credit
This was written by me! Davion!
As you can see by the output, Day Trader I am Not! :D So any tips are greatly appreciated!

ETH: 0xB5aa1F5736a87Fd06e0B139Bf11870e1C13e5018
BTC: 15g4fnWKQPJPV7K59gBv4BWvW6X4caHbLp
XMR: 46HrHXy5fBoW8NuJ5zMEARi1wdcKDKFqJF8f7RZfHavjF64JwxXdaFF9V7zjFkrVwMMMabTopVs42h19Q9EfFRfPJehYmHW
NEO: AJC9fqgHdrt4gbvr5VUaYPdaeVsXsnstbE

Thanks in advance!!