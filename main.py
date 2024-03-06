import requests
import pandas as pd
import matplotlib.pyplot as plt
import time

crypto_data = {'Timestamp': [], 'Price': []}
#Fetches price for a ticker,
def fetch_price(ticker):
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=' + ticker + '&vs_currencies=usd'
    response = requests.get(url)
    price_data = response.json()
    timestamp = pd.Timestamp.now()  # Get current timestamp
    return timestamp, price_data[ticker]['usd']


#adds stuff to data frame..a df is a 2D table (rows and columns, in this case: name and price)
def add_to_dataFrame(timestamp, price):
    crypto_data['Timestamp'].append(timestamp)
    crypto_data['Price'].append(price)


# the actual PLOTTING of the items, kind is the type of chart, x and y refer to the dataframe's 'Name' and 'Price'
def plot_prices(df):
    plt.plot(df['Timestamp'], df['Price'], marker='o')
    plt.xlabel('Timestamp')
    plt.ylabel('USD Price')
    current_price = df['Price'].iloc[-1]  # Get the last price in the DataFrame
    plt.title(f'Bitcoin Price Over Time\nCurrent Price: ${current_price:.2f}')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.pause(1)


#makes the plot interactive so the window can be updated automatically
plt.ion()

#Code to fetch BTC price specifically and then adds BTC to dataframe, then we plot BTC on a timer
while True:
    timestamp, bitcoin_price = fetch_price('bitcoin')
    add_to_dataFrame(timestamp, bitcoin_price)
    df = pd.DataFrame(crypto_data)
    plot_prices(df)
    time.sleep(60)  # Wait for 1 minute before updating the price again