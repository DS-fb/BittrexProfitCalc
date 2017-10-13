# BittrexProfitCalc
A simple python program to calculate the profit/loss you've done directly with Bittrex trades.

# Requirements

You need to install the python interpreter from https://www.python.org/downloads/
From there, open command line and install pandas "pip install pandas"

Download a csv copy of your trades from Bittrex at  https://bittrex.com/History
Click the 'CSV' button under the 'COMPLETED' Section.
Move that file to the location the script is located and rename it to 'bittrex.csv'
Using -z option will remove all the wallets holding 0 coins.

Run the script from command line.

# Output

    You've done 68 trades with 18 stocks since 09/05/2017 03:58:50 PM.
     Coin             Holdings        Profit       Average Price Per Coin      
    BTC-RISE        234.53810889    0.00733561      0.000129 on 9 trades.
    BTC-VTC         0.00000000      0.00010683      0.000352 on 1 trades.
    BTC-OK          0.00000000      -0.00299157     0.000116 on 2 trades.
    BTC-TRIG        -0.00000000     0.00188225      0.000310 on 4 trades.
    BTC-XRP         0.00000000      -0.00005080     0.000047 on 1 trades.
    BTC-EDG         99.15901166     0.00255259      0.000335 on 4 trades.
    BTC-ETH         0.16081087      0.00001800      0.070853 on 3 trades.
    BTC-PAY         0.00000000      -0.00137129     0.000614 on 1 trades.
    BTC-XVG         0.00000000      0.00000354      0.000002 on 2 trades.
    BTC-NEO         12.71804302     0.00005076      0.005452 on 3 trades.
    BTC-LSK         0.00000000      -0.00025414     0.001499 on 2 trades.
    BTC-XMR         -0.49000000     0.00000000      0.000000 on 0 trades.
    ETH-QTUM        6.72553984      0.00000000      0.037160 on 1 trades.
    ETH-OMG         6.74945459      0.00000000      0.036867 on 1 trades.
    BTC-QTUM        5.44552309      0.00214275      0.003450 on 2 trades.
    BTC-OMG         3.16576057      0.00009310      0.002771 on 2 trades.
    BTC-STRAT       0.00000000      0.00001471      0.001379 on 1 trades.
    BTC-DCR         -0.19546350     0.00000000      0.000000 on 0 trades.
    
    You've made 0.009532BTC, and 0.000000ETH.
    You made the most off BTC-RISE. You made the least of BTC-OK.
    You have deposited into Bittrex, 0.200385BTC and 0.499998ETH. 
    
# Limitaions
If you do any cross market trading (ie. you buy ETH/OMG and then sell it on BTC/OMG) it will report incorrect numbers.
I would suggest editing the CSV via excel or something and converting the ETH price to BTC, and the Type from 'ETH/' to 'BTC/' and you will get accurate numbers.
It doesn't currently support the USDT market.

# Credit
This was written by me! Davion!
As you can see by the output, Day Trader I am Not! :D So any tips are greatly appreciated!

    ETH: 0xB5aa1F5736a87Fd06e0B139Bf11870e1C13e5018
    BTC: 15g4fnWKQPJPV7K59gBv4BWvW6X4caHbLp
    XMR: 46HrHXy5fBoW8NuJ5zMEARi1wdcKDKFqJF8f7RZfHavjF64JwxXdaFF9V7zjFkrVwMMMabTopVs42h19Q9EfFRfPJehYmHW
    NEO: AJC9fqgHdrt4gbvr5VUaYPdaeVsXsnstbE

Thanks in advance!!
