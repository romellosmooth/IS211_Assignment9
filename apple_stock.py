# apple_stock.py
# This script scrapes Apple's historical stock prices from Yahoo Finance

# Step 1: Import required libraries
import requests  # Helps us fetch the webpage
from bs4 import BeautifulSoup  # Helps us extract data from the webpage


# Step 2: Function to scrape stock data
def scrape_stock_data():
    # URL to fetch stock data
    url = "https://finance.yahoo.com/quote/AAPL/history/?p=AAPL"

    # Get the webpage content
    response = requests.get(url)

    # Check if the webpage was fetched successfully
    if response.status_code == 200:  # 200 means "OK"
        # Parse the webpage content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Look for the table with stock data
        stock_table = soup.find("table", class_="W(100%) M(0)")  # Find the table
        rows = stock_table.find_all("tr")  # Get all rows in the table

        print("Apple Historical Stock Prices")
        print(f"{'Date':<15} {'Close Price':<10}")
        print("-" * 30)

        # Loop through all rows (skip the header row)
        for row in rows[1:]:  # Start at row 1 to skip the header
            columns = row.find_all("td")  # Get all columns in the row

            # Make sure the row has enough columns (valid stock data)
            if len(columns) >= 5:
                date = columns[0].text.strip()  # Extract date
                close_price = columns[4].text.strip()  # Extract closing price

                # Print the date and close price
                print(f"{date:<15} {close_price:<10}")
    else:
        print("Failed to load the webpage. Please check the URL or your internet connection.")


# Step 3: Run the function
if __name__ == "__main__":
    scrape_stock_data()
