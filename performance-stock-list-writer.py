import time
import pytz
import yfinance as yf
from datetime import datetime, timedelta

# Modify the calculate_monthly_percentage_changes function to consider the past 2 months this year
def calculate_monthly_percentage_changes(stock, current_month, current_year):
    # Retrieve historical data for the past 1 year
    history = stock.history(period="1y")
    
    # Create a dictionary to store percentage changes for the past 2 months this year
    monthly_percentage_changes = {}
    
    for month in range(current_month - 2, current_month + 1):  # Consider the past 2 months and the current month
        if month <= 0:
            month += 12  # Handle year rollover
            year = current_year - 1
        else:
            year = current_year
        
        # Filter data for the current month
        monthly_data = history[(history.index.month == month) & (history.index.year == year)]
        
        if not monthly_data.empty:
            start_price = monthly_data['Open'][0]
            end_price = monthly_data['Close'][-1]
            percentage_change = ((end_price - start_price) / start_price) * 100
            monthly_percentage_changes[month] = percentage_change
    
    return monthly_percentage_changes

# Define the start and end times for when the program should run
start_time = datetime.now().replace(hour=8, minute=30, second=0, microsecond=0).time()
end_time = datetime.now().replace(hour=15, minute=59, second=0, microsecond=0).time()

# Initialize run count
run_count = 1

# Main program loop
while True:
    try:
        eastern = pytz.timezone('US/Eastern')
        now = datetime.now(eastern)
        
        if run_count == 1 or (now.weekday() in [0, 1, 2, 3, 4] and now.time() >= start_time and now.time() <= end_time):
            # Increment run count
            run_count += 1

            # Read the list of stock symbols from the input file
            with open("list-of-stock-symbols-to-scan.txt", "r") as input_file:
                stock_symbols = [line.strip() for line in input_file if line.strip()]
            
            # Initialize a dictionary to store stock data
            stock_data = {}
            
            # Fetch historical data and calculate percentage changes for each stock
            for symbol in stock_symbols:
                stock = yf.Ticker(symbol)
                print(f"Downloading the historical data for {symbol}...")
                
                # Fetch historical data for the past 1 day
                history_1_day = stock.history(period="1d")
                
                # Calculate percentage change for the past 1 day (or use default value if data is unavailable)
                if not history_1_day.empty:
                    start_price_1_day = history_1_day['Open'][0]
                    end_price_1_day = history_1_day['Close'][-1]
                    percentage_change_1_day = ((end_price_1_day - start_price_1_day) / start_price_1_day) * 100
                else:
                    percentage_change_1_day = 0  # Default value when data is unavailable

                # You can repeat similar checks and calculations for other timeframes (1 week, 14 days, 1 month)

                # Fetch historical data for the past 1 week
                history_1_week = stock.history(period="1wk")
                if not history_1_week.empty:
                    start_price_1_week = history_1_week['Open'][0]
                    end_price_1_week = history_1_week['Close'][-1]
                    percentage_change_1_week = ((end_price_1_week - start_price_1_week) / start_price_1_week) * 100
                else:
                    percentage_change_1_week = 0

                # Fetch historical data for the past 14 days
                history_14_days = stock.history(period="14d")
                if not history_14_days.empty:
                    start_price_14_days = history_14_days['Open'][0]
                    end_price_14_days = history_14_days['Close'][-1]
                    percentage_change_14_days = ((end_price_14_days - start_price_14_days) / start_price_14_days) * 100
                else:
                    percentage_change_14_days = 0

                # Fetch historical data for the past 1 month
                history_1_month = stock.history(period="1mo")
                if not history_1_month.empty:
                    start_price_1_month = history_1_month['Open'][0]
                    end_price_1_month = history_1_month['Close'][-1]
                    percentage_change_1_month = ((end_price_1_month - start_price_1_month) / start_price_1_month) * 100
                else:
                    percentage_change_1_month = 0

                # Retrieve monthly percentage changes
                monthly_percentage_changes = calculate_monthly_percentage_changes(stock, now.month, now.year)
                
                stock_data[symbol] = {
                    'percentage_change_1_day': percentage_change_1_day,
                    'percentage_change_1_week': percentage_change_1_week,
                    'percentage_change_14_days': percentage_change_14_days,
                    'percentage_change_1_month': percentage_change_1_month,
                    'monthly_percentage_changes': monthly_percentage_changes
                }
                time.sleep(2)  # Sleep for 2 seconds
                
            # Filter stocks based on historical performance for the current month and the past 2 months
            current_month = now.month
            current_year = now.year

            filtered_stocks = []
            for symbol, data in stock_data.items():
                if (
                    current_month in data['monthly_percentage_changes'] and
                    current_month - 1 in data['monthly_percentage_changes'] and
                    current_month - 2 in data['monthly_percentage_changes'] and
                    data['monthly_percentage_changes'][current_month] > 0 and
                    data['monthly_percentage_changes'][current_month - 1] > 0 and
                    data['monthly_percentage_changes'][current_month - 2] > 0 and
                    data['percentage_change_1_day'] >= 1 and
                    data['percentage_change_1_week'] >= 1 and
                    data['percentage_change_14_days'] >= 1 and
                    data['percentage_change_1_month'] >= 1
                ):
                    filtered_stocks.append((symbol, data['percentage_change_1_day']))
            
            # Sort the filtered stocks by percentage change for the current day
            sorted_stocks = sorted(filtered_stocks, key=lambda x: x[1], reverse=True)
            
            # Select the top 28 stocks
            top_stocks = sorted_stocks[:28]
            
            # Write the selected stock symbols to the output file
            with open("electricity-or-utility-stocks-to-buy-list.txt", "w") as output_file:
                for symbol, _ in top_stocks:
                    output_file.write(f"{symbol}\n")

            print("")
            print("Successful stocks list updated successfully.")
            print("")

        # Calculate the next run time
        if now.time() > end_time:
            next_run = now + timedelta(days=1, minutes=30)
            next_run = next_run.replace(hour=start_time.hour, minute=start_time.minute, second=0, microsecond=0)
        else:
            next_run = now + timedelta(minutes=5)
            next_run = next_run.replace(second=0, microsecond=0)
        
        main_message = f"Next run will be soon after the time of {next_run.strftime('%I:%M %p')} (Eastern Time)."
        print(main_message)
        print("")

        # Wait until after printing the list of stocks before calculating the next run time
        time_until_next_run = (next_run - now).total_seconds()
        time.sleep(time_until_next_run)

    except Exception as e:
        print("")
        print(f"An error occurred: {str(e)}")
        print("Restarting the program in 5 minutes...")
        print("")
        time.sleep(300)
