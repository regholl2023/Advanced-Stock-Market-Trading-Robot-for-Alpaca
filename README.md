# Advanced-Stock-Market-Trading-Bot-Version-2 

This code is so brand new that it is still in the beta testing phase right now.  

Advanced Stock Market Trading Bot

This is a stock market portfolio management application that helps minimize losses and maximize profits.
This works with the Alpaca stock market trading broker. 
Advanced Stock Market Trading Bot only works Monday through Friday: 9:30am - 4:00pm Eastern Time.

This is an Advanced buying and selling Python 3 Trading Robot to monitor a stock market symbol or a number of stock symbols that you type in. 

It will automatically buy more stock of the symbol that you have selected when there is a bull market 
or a price increase and it will automatically sell all shares of the same symbol when there is a bear market or a price decrease. 
It maximizes your profits by trading with all of the available Cash Equity in your stock broker account. Here's more information: 

Experience the power of Python 3's TA Library with our Advanced Stock Market Trading Bot. Turn data into insights, insights into decisions, and decisions into profit. Experience the future of trading with our Advanced Stock Market Trading Bot. 
Elevate your trading game, maximize your profits, and let our bot do the heavy lifting. This isn't just a bot, it's your 24/7 trading partner.

Imagine having a personal stock market advisor available 24/7, assessing opportunities, risks, and making decisions without ever needing a break. Welcome to the future of trading with our revolutionary Advanced Trading Bot! Our robot leverages the power of Alpaca API and the newest online stock market data to keep its finger on the pulse of the market. It continually monitors your specified stocks, utilizing the most advanced trading indicators including MACD, RSI, and Moving Averages to make the most informed buy and sell decisions.
Even better, it's not just about buying and selling. This trading bot is meticulous with your account management - keeping track of your account cash, monitoring day trade counts, and providing real-time updates on your positions: 
And the best part? You're in control. You can input the stock symbols you want to trade and edit them anytime. 
Plus, it's flexible, running in any market conditions. Whether the market is open or not, our bot is hard at work, strategizing and waiting for the right moment to buy profitable stock. In a world full of data, making sense of it all can be overwhelming. That's where our Stock Market Trading Bot and the power of Python 3's TA (Technical Analysis) Library come in. The TA Library is the master key to unlocking the potential of your trading. It is a comprehensive software suite that allows our bot to tap into a myriad of technical analysis indicators. This isn't just average data, this is high-precision, deeply-analyzed metrics that give you a cutting-edge advantage in the market. Our Advanced Stock Market Trading Bot, armed with the TA Library, processes market data in real-time, applying rigorous mathematical analysis to identify key trends and indicators. From Moving Averages, MACD, to RSI, this bot can leverage them all, providing you with clear, data-driven buy and sell signals. The TA Library isn't a perfect market prediction software tool, but it's close to being perfect.  With its predictive analytics capabilities, it enables our Robot to analyze price movements, estimate future price changes, and reduce risks, leading to more informed and profitable trading decisions.

To install:

Do not be the root user. This installs from a regular user account. Open a command line terminal from this folder location and type: sh install.sh

Remember that you just let the stockbot run for 24 hours. It watches the prices of the stocks that you own in your alpaca account. It sells the stocks to prevent losing money. This Python program will sell your stocks both during a price decrease and during a price increase to help you to not miss out on obtaining those rare profit opportunities that quickly take place in the stock market. If these fast price increases are not noticed quickly, then they are usually missed and then the price usually decreases afterwards.

After placing your alpaca keys at the bottom of /home/nameofyourhomefolderhere/.bashrc you simply run the command in a command terminal like:

python3 advanced-stock-market-trading-robot-v2.py



Disclaimer: Remember that all trading involves risks. The ability to successfully implement these strategies depends on both market conditions and individual skills and knowledge. As such, trading should only be done with funds that you can afford to lose. Always do thorough research before making investment decisions, and consider consulting with a financial advisor. This is use at your own risk software. This software does not include any warranty or guarantees other than the useful tasks that may or may not work as intended for the software application end user. The software developer shall not be held liable for any financial losses or damages that occur as a result of using this software for any reason to the fullest extent of the law. Using this software is your agreement to these terms. This software is designed to be helpful and useful to the end user.

Place your alpaca code keys in the location: /home/name-of-your-home-folder/.bashrc Be careful to not delete the entire .bashrc file. Just add the 4 lines to the bottom of the .bashrc text file in your home folder, then save the file. .bashrc is a hidden folder because it has the dot ( . ) in front of the name. Remember that the " # " pound character will make that line unavailable. To be helpful, I will comment out the real money account for someone to begin with an account that does not risk using real money. The URL with the word "paper" does not use real money. The other URL uses real money. Making changes here requires you to reboot your computer or logout and login to apply the changes.

The 4 lines to add to the bottom of .bashrc are:

export APCA_API_KEY_ID='zxzxzxzxzxzxzxzxzxzxz'

export APCA_API_SECRET_KEY='zxzxzxzxzxzxzxzxzxzxzxzxzxzxzxzxzxzxzxzx'

#export APCA_API_BASE_URL='https://api.alpaca.markets'

export APCA_API_BASE_URL='https://paper-api.alpaca.markets'
