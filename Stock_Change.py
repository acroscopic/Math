# Using historical data from Yahoo Finance, the script pulls the value for the open and compares them over time. 

import yfinance as yf

WatchList = ('TSLA', 'NVDA', 'GOOG')
periods = ('2d', '5d', '31d')

def DeltaPercent(stock, period):
	# Request historical data for the specified period to compare
	data = yf.Ticker(stock).history(period=period)
	
	# removing null values to avoid errors
	data.dropna(inplace=True)
	
	# Calculate the percentage change between the first and last data points within the specified period
	if len(data) >= 2:
		first_open = data['Close'].iloc[0]
		last_open = data['Close'].iloc[-1]
		percentage_change = ((last_open - first_open) / first_open) * 100
	else:
		percentage_change = None  # Not enough data points

	# Checks if the percentage change is greater than 5%
	# This is unfinished. I plan on making it email me later for changes greater than 5%
	if percentage_change is not None and abs(percentage_change) > 5:
		print(f"Period: {period}\nPercentage Change: {percentage_change:.2f}%")
	elif percentage_change is not None:
		print(f"Period: {period}\nPercentage Change: {percentage_change:.2f}%")
	else:
		print(f"Period: {period}\nPercentage Change: N/A")

for stock in WatchList:
	print(f'\n{stock}:')
	for period in periods:
		DeltaPercent(stock, period)





